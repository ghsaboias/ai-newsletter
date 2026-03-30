#!/usr/bin/env python3
"""
Produce research-slim.json from research.json.

Deduplicates stories (keeps first by headline similarity), strips
excerpts, source metadata, and entities. Output is just what generate
needs: id, headline, category, key_facts (fact + url).
"""

import json, sys
from pathlib import Path


def dedupe_stories(stories: list) -> list:
    """Keep first occurrence of each story by word overlap in headline."""
    kept = []
    seen_words = []
    for s in stories:
        words = set(s["headline"].lower().split())
        is_dupe = False
        for prev in seen_words:
            overlap = len(words & prev) / max(len(words | prev), 1)
            if overlap > 0.4:
                is_dupe = True
                break
        if not is_dupe:
            kept.append(s)
            seen_words.append(words)
    return kept


def slim_story(story: dict) -> dict:
    return {
        "id": story["id"],
        "headline": story["headline"],
        "category": story.get("category", []),
        "key_facts": [
            {"fact": kf["fact"], "url": kf.get("source_url", "")}
            for kf in story.get("key_facts", [])
        ],
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: slim_research.py <day_dir>", file=sys.stderr)
        sys.exit(1)

    day_dir = Path(sys.argv[1])
    src = day_dir / "research.json"
    dst = day_dir / "research-slim.json"

    if not src.exists():
        print(f"Error: {src} not found", file=sys.stderr)
        sys.exit(1)

    data = json.loads(src.read_text())
    stories = dedupe_stories(data.get("stories", []))
    slim = {
        "date": data.get("date", ""),
        "story_count": len(stories),
        "stories": [slim_story(s) for s in stories],
    }

    dst.write_text(json.dumps(slim, indent=2, ensure_ascii=False))

    orig_size = src.stat().st_size
    slim_size = dst.stat().st_size
    dupes_removed = len(data.get("stories", [])) - len(stories)
    print(f"  {src.name}: {len(data.get('stories', []))} stories, {orig_size:,} bytes")
    print(f"  {dst.name}: {len(stories)} stories, {slim_size:,} bytes ({slim_size * 100 // orig_size}%)")
    if dupes_removed:
        print(f"  Deduped: {dupes_removed} duplicate stories removed")


if __name__ == "__main__":
    main()
