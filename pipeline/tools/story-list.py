#!/usr/bin/env python3
"""story-list.py — the day's stories, in the edition and left out, for Gui.

Sent with the draft URL so Gui reviews the selection next to the draft: what
went in (by tier), what the writer left out of the research, the window's
most-covered stories the recall check rejected, and what the researchers
considered and dropped. Every left-out story carries its reason and coverage.
Reads only files the run already wrote; makes no calls.

Writes <DAY_DIR>/stories.md (everything) and prints the first three sections.

Usage: story-list.py <YYYY-MM-DD> [--dir DAY_DIR] [--top N]
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "output" / "ai"
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def load(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return None


def coverage(sal):
    if not sal:
        return ""
    parts = []
    if sal.get("dj_articles"):
        parts.append(f"DJ {sal['dj_articles']} artigos")
    if sal.get("techmeme_rank"):
        parts.append(f"Techmeme #{sal['techmeme_rank']}")
    return f" ({', '.join(parts)})" if parts else ""


def plain(text, n=110):
    text = LINK.sub(r"\1", text)
    text = re.sub(r"[*_]", "", text).strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def edition_items(edition):
    """(tier, theme, text, urls) per item, in edition order."""
    items, tier, theme, cur = [], None, None, None
    for line in edition.splitlines():
        if line.startswith("### "):
            tier, theme = "Grande", None
            cur = {"tier": tier, "theme": None, "text": plain(line[4:], 140), "urls": []}
            items.append(cur)
        elif line.startswith("#### "):
            theme = line[5:].strip()
            tier = "Leia também" if theme.lower().startswith("leia também") else "Média"
            cur = None
        elif line.startswith("- ") and tier:
            urls = [u for _, u in LINK.findall(line)]
            if tier == "Grande" and cur is not None:
                cur["urls"] += urls
            else:
                items.append({"tier": tier, "theme": theme, "text": plain(line[2:]), "urls": urls})
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date")
    ap.add_argument("--dir", type=Path)
    ap.add_argument("--top", type=int, default=10, help="recall rejects to show")
    a = ap.parse_args()
    d = a.dir or ROOT / a.date

    research = load(d / "research.json")
    edition_path = d / "edition.md"
    if not research or not edition_path.is_file():
        print(f"HALT: research.json or edition.md missing in {d}", file=sys.stderr)
        return 1
    edition = edition_path.read_text()
    stories = research.get("stories", [])
    url_story = {s["url"]: st for st in stories for s in st.get("sources", []) if s.get("url")}

    out = [f"# Histórias de {a.date}", ""]

    # 1. In the edition, by tier
    items = edition_items(edition)
    used = set()
    out.append(f"## Na edição ({len(items)})")
    for tier in ("Grande", "Média", "Leia também"):
        tier_items = [i for i in items if i["tier"] == tier]
        if not tier_items:
            continue
        out += ["", f"**{tier}s**" if tier != "Leia também" else "**Leia também**"]
        for i in tier_items:
            st = next((url_story[u] for u in i["urls"] if u in url_story), None)
            if st:
                used.add(st["id"])
            theme = f"[{i['theme']}] " if tier == "Média" else ""
            out.append(f"- {theme}{i['text']}{coverage(st.get('salience') if st else None)}")

    # 2. Researched, left out by the writer
    left = [st for st in stories if st["id"] not in used]
    out += ["", f"## Pesquisadas, fora da edição ({len(left)})"]
    for st in left:
        origin = " · via recall" if st.get("origin") == "recall" else ""
        out.append(f"- {st['headline']}{coverage(st.get('salience'))}{origin}")
    if not left:
        out.append("- (nenhuma)")

    # 3. The window's most-covered stories the recall check rejected
    cands = {c["key"]: c for c in (load(d / "recall-candidates.json") or {}).get("candidates", [])}
    recall = load(d / "recall.json") or {}
    rejected = []
    for dec in recall.get("decisions", []):
        if dec.get("action") != "reject":
            continue
        c = cands.get(dec.get("candidate"), {})
        head = c.get("headline_pt") or c.get("headline") or dec.get("candidate")
        if c.get("source") == "dj":
            cov, key = f"DJ {c.get('articles_in_window', '?')} artigos", (0, -(c.get("articles_in_window") or 0))
        else:
            cov, key = f"Techmeme #{c.get('rank', '?')}", (1, c.get("rank") or 99)
        rejected.append((key, f"- {plain(head, 120)} ({cov}): {dec.get('reason', '')}"))
    rejected.sort()
    shown = rejected[: a.top]
    out += ["", f"## Mais cobertas na janela, recusadas no recall ({len(shown)} de {len(rejected)})"]
    out += [line for _, line in shown] or ["- (nenhuma)"]
    head_part = "\n".join(out)

    # 4. Everything the researchers considered and dropped (file only)
    out += ["", "## Consideradas e recusadas pelos pesquisadores"]
    seen = set()
    for cl in ("ai", "hw", "world"):
        for r in (load(d / f"research-{cl}.json") or {}).get("rejected", []):
            h = r.get("headline", "").strip()
            if not h or h.lower() in seen:
                continue
            seen.add(h.lower())
            out.append(f"- [{cl}] {h}: {r.get('reason', '')}")

    (d / "stories.md").write_text("\n".join(out) + "\n")
    print(head_part)
    print(f"\n(lista completa, com as {len(seen)} recusadas pelos pesquisadores: {d / 'stories.md'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
