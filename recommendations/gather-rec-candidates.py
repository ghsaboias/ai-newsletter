#!/usr/bin/env python3
"""Gather candidate videos for the newsletter's "Recomendações de hoje" section.

For each whitelisted channel, emit the N most-recent `video_articles` rows
(status='done') that have NOT already been recommended — dedup is against the
YouTube IDs in recommendations/RECOMMENDATIONS.md (the live archive, synced daily
from the published Substack posts). The model downstream picks the final 2.

The whitelist strings must match the `channel` column byte-for-byte (it's the
youtubei.js channel display name). Keep this list in sync with the DJ auto-ingest.

Data source: DJ Supabase `video_articles`, queried via `sbq --sql` run from
~/daily-journal-platform (where its .env.local + SUPABASE_ACCESS_TOKEN live).

Self-locating: finds the archive next to this file and the DJ dir under $HOME,
so it runs unchanged on the Pi or the Mac. Output: JSON to stdout.

Usage:
    python3 gather-rec-candidates.py [--per-channel 2] [--date YYYY-MM-DD]
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Byte-for-byte the `channel` values youtubei.js stores. Order here is only the
# emit order; final selection is the model's call.
CHANNELS = [
    "Sequoia Capital",
    "Invest Like The Best",
    "a16z",
    "Dwarkesh Patel",
    "Peter H. Diamandis",
    "David Senra",
    "All-In Podcast",
]

ARCHIVE = Path(__file__).resolve().parent / "RECOMMENDATIONS.md"
DJ = Path.home() / "daily-journal-platform"          # holds .env.local for sbq
CHAPTER_RE = re.compile(r"(?m)^\s*\[?((?:\d{1,2}:)?\d{1,2}:\d{2})\]?\s+(\S.*?)\s*$")


def used_ids() -> set:
    """Every YouTube ID already recommended, from the archive."""
    if not ARCHIVE.exists():
        print(f"WARN: archive not found at {ARCHIVE}", file=sys.stderr)
        return set()
    text = ARCHIVE.read_text(encoding="utf-8")
    return set(re.findall(r"youtube\.com/watch\?v=([\w-]+)", text))


def sbq_sql(sql: str):
    """Run a raw SQL query through sbq from the DJ dir. Returns parsed rows."""
    env = dict(os.environ)
    # Cron/fresh shells may have a thin PATH; make sbq reachable.
    env["PATH"] = os.pathsep.join(
        [str(Path.home() / ".local/bin"), "/usr/local/bin", "/usr/bin", env.get("PATH", "")]
    )
    proc = subprocess.run(
        ["sbq", "--sql", sql], cwd=DJ, capture_output=True, text=True, env=env
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        sys.exit(f"ERROR: sbq failed (rc={proc.returncode}).\n{proc.stderr.strip()}\n"
                 f"Check {DJ}/.env.local has SUPABASE_ACCESS_TOKEN (needed for --sql).")
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        sys.exit(f"ERROR: sbq returned non-JSON:\n{proc.stdout[:400]}")
    if isinstance(data, dict) and data.get("code"):        # PostgREST error object
        sys.exit(f"ERROR: sbq/DB error: {data.get('message')}")
    return data


def parse_chapters(desc: str):
    """Best-effort chapter list from a YouTube description. Only trust it when
    there are >=3 timestamped lines (otherwise it's likely stray timestamps)."""
    if not desc:
        return []
    ch = [{"t": m.group(1), "label": m.group(2)[:80]} for m in CHAPTER_RE.finditer(desc)]
    return ch[:20] if len(ch) >= 3 else []


def first_paragraph(summary_md: str) -> str:
    """The DJ description shown under each rec = the first prose paragraph of the
    video's summary_md (the block under '## Contexto'), markdown stripped. This is
    verbatim what the newsletter has always used — not a fresh rewrite."""
    if not summary_md:
        return ""
    para = []
    for ln in summary_md.splitlines():
        s = ln.strip()
        if not para:
            if not s or s.startswith("#"):   # skip leading blanks / '## Contexto'
                continue
        elif not s or s.startswith(("#", "*", "-", ">")):
            break                            # paragraph ends at blank / heading / bullet
        para.append(s)
    text = " ".join(para)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)          # bold
    text = re.sub(r"\*(.+?)\*", r"\1", text)              # italics
    text = re.sub(r"\[(.+?)\]\([^)]+\)", r"\1", text)     # links -> label
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-channel", type=int, default=2,
                    help="how many most-recent-unused videos to keep per channel")
    ap.add_argument("--date", default=None, help="edition date label, YYYY-MM-DD")
    args = ap.parse_args()

    used = used_ids()
    in_list = ", ".join("'" + c.replace("'", "''") + "'" for c in CHANNELS)
    rows = sbq_sql(
        "SELECT youtube_id, title, channel, published_at, youtube_url, view_count, "
        "description, summary_md FROM video_articles "
        f"WHERE status='done' AND channel IN ({in_list}) "
        "ORDER BY channel, published_at DESC"
    )

    # Take the N most-recent UNUSED per channel (rows already sorted desc by date).
    kept: dict = {c: [] for c in CHANNELS}
    for r in rows:
        ch = r["channel"]
        if r["youtube_id"] in used or ch not in kept:
            continue
        if len(kept[ch]) < args.per_channel:
            kept[ch].append(r)

    candidates = []
    for ch in CHANNELS:
        for r in kept[ch]:
            desc = r.get("description") or ""
            candidates.append({
                "youtube_id": r["youtube_id"],
                "title": r["title"],
                "channel": ch,
                "published_at": (r.get("published_at") or "")[:10] or None,
                "url": r.get("youtube_url"),
                "view_count": r.get("view_count"),
                "chapters": parse_chapters(desc),
                "description_pt": first_paragraph(r.get("summary_md")),  # the rec's description
                "yt_description": desc[:700],   # YouTube blurb (guest names, extra signal)
                "summary_md": (r.get("summary_md") or "")[:1200],
            })

    empty = [c for c in CHANNELS if not kept[c]]
    print(json.dumps({
        "date": args.date,
        "channels": CHANNELS,
        "per_channel": args.per_channel,
        "archive_used_count": len(used),
        "channels_with_no_fresh_candidate": empty,
        "candidate_count": len(candidates),
        "candidates": candidates,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
