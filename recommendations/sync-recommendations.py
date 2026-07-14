#!/usr/bin/env python3
"""Rebuild / update the RECOMMENDATIONS.md archive from PUBLISHED Substack posts.

The source of truth for "what was already recommended" is the *published*
Substack post — recommendations are finalized by hand in the editor, so the
generated `recs.json` is only a proposal and may differ from what ships. This
archive is therefore a pure projection of the published posts.

Each run re-fetches a recent window of editions and UPSERTS their recommendation
sections (re-extracting from the current published HTML and replacing whatever
was there). Nothing is frozen after first sight: if recommendations are added or
changed on a post after the first sync, a later run picks the change up. Older
editions fall outside the window and are treated as settled.

Modes:
  (default)      upsert the most-recent --window editions   (daily cron)
  --rebuild      rebuild the WHOLE archive from scratch      (full backfill)

Options:
  --window N     recent editions to (re)scan in default mode (default 14)
  --max N        cap on editions to list when rebuilding     (default 200)
  --archive PATH archive file (default: RECOMMENDATIONS.md next to this script)
  --dry-run FILE write the result to FILE instead of --archive (for diffing)

Editions are listed via `sstats emails`; each post's body via `sstats post
<id> --html`. Output is canonical (header preamble + `## DATE` sections sorted
ascending, one blank line between), so re-running over unchanged editions
produces byte-identical output and no spurious git diff.

On stdout, prints one space-separated line of the dates whose section changed
(empty if none) — the shell wrapper uses it for the commit message.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time

from extract_recs import extract, format_block

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ARCHIVE = os.path.join(HERE, "RECOMMENDATIONS.md")

HEADER = """# Recomendações da Newsletter

Arquivo das recomendações (vídeos e entrevistas) publicadas na newsletter de
AI/Tech. Cada seção é uma edição; sem edição nos fins de semana.

Atualizado automaticamente ao meio-dia (BRT) por
`recommendations/sync-recommendations.sh` (cron na Pi). Fonte: post publicado no
Substack, via `sstats post`."""

DATE_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})\s*$", re.M)


def log(msg: str) -> None:
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S %z')}] {msg}", file=sys.stderr)


def sstats(*args: str) -> str:
    """Run the sstats CLI and return stdout (empty string on failure)."""
    try:
        out = subprocess.run(
            ["sstats", *args],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        log(f"WARN: sstats {' '.join(args)} failed: {exc}")
        return ""
    if out.returncode != 0:
        log(f"WARN: sstats {' '.join(args)} exited {out.returncode}: {out.stderr.strip()[:200]}")
        return ""
    return out.stdout


def list_editions(max_n: int, page: int = 20):
    """Return [(date, post_id), ...] newest-first, from `sstats emails` (paginated)."""
    editions = []
    seen = set()
    offset = 0
    while offset < max_n:
        raw = sstats("emails", "-n", str(page), "--offset", str(offset))
        if not raw:
            break
        try:
            rows = json.loads(raw).get("rows", []) or []
        except json.JSONDecodeError:
            log(f"WARN: could not parse sstats emails page at offset {offset}")
            break
        rows = [r for r in rows if r.get("post_id") is not None]
        if not rows:
            break
        for r in rows:
            date = (r.get("post_date") or "")[:10]
            pid = str(r["post_id"])
            if date and pid not in seen:
                seen.add(pid)
                editions.append((date, pid))
        if len(rows) < page:
            break
        offset += page
        time.sleep(1)  # gentle between listing pages
    return editions[:max_n]


def build_block(date: str, post_id: str, pause: float = 3.0):
    """Fetch a published post and extract its recommendations block (or '')."""
    html = sstats("post", post_id, "--html")
    time.sleep(pause)  # be gentle with Substack
    if not html:
        log(f"WARN: empty HTML for {date} ({post_id})")
        return ""
    return format_block(date, extract(html))


def parse_archive(text: str):
    """Split an archive into (header, {date: block}). Blocks exclude trailing ws."""
    m = DATE_RE.search(text)
    if not m:
        return text.strip(), {}
    header = text[: m.start()].strip()
    sections = {}
    marks = list(DATE_RE.finditer(text))
    for i, mark in enumerate(marks):
        date = mark.group(1)
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        sections[date] = text[mark.start(): end].strip()
    return header, sections


def serialize(header: str, sections: dict) -> str:
    """Canonical archive: header + date sections sorted ascending, blank line between."""
    parts = [header]
    for date in sorted(sections):
        parts.append(sections[date])
    return "\n\n".join(parts) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true", help="rebuild the whole archive")
    ap.add_argument("--window", type=int, default=14, help="recent editions to rescan")
    ap.add_argument("--max", type=int, default=200, help="cap on editions when rebuilding")
    ap.add_argument("--archive", default=DEFAULT_ARCHIVE)
    ap.add_argument("--dry-run", dest="dry_run", default=None,
                    help="write to this path instead of --archive")
    args = ap.parse_args()

    if args.rebuild:
        header, sections = HEADER, {}
        editions = list_editions(args.max)
    else:
        try:
            with open(args.archive, encoding="utf-8") as fh:
                header, sections = parse_archive(fh.read())
        except FileNotFoundError:
            header, sections = HEADER, {}
        editions = list_editions(max(args.window, 20))[: args.window]

    if not editions:
        log("ERROR: no editions returned from sstats emails")
        return 1

    before = dict(sections)
    changed = []
    for date, pid in editions:
        block = build_block(date, pid)
        if not block:
            # No recs section (weekend/free/older) or transient fetch failure:
            # never wipe an existing good section on an empty read.
            if args.rebuild:
                log(f"skip {date} — no recommendations section")
            continue
        if sections.get(date) != block:
            sections[date] = block
            changed.append(date)
            n = block.count("https://www.youtube.com/")
            log(f"{'add' if date not in before else 'update'} {date} ({n} recs)")

    # Surface any editions that exist in the old archive but not in a rebuild —
    # data we would drop. Keep them (don't silently lose history); flag loudly.
    if args.rebuild:
        dropped = sorted(set(before) - set(sections))
        for date in dropped:
            log(f"WARN: {date} in old archive but not re-extracted — KEEPING old block")
            sections[date] = before[date]

    out_path = args.dry_run or args.archive
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(serialize(header, sections))

    log(f"wrote {out_path} — {len(sections)} editions, {len(changed)} changed")
    print(" ".join(changed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
