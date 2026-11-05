#!/usr/bin/env python3
"""Check that every link in the edition points at a URL from the day's research.

The generator copies source URLs straight from research.json. This is the
deterministic guard on that copy: a link target that is not one of the
research's source URLs is a transcription error or an invented link.

Usage:
    check-links.py <edition.md> <research.json>

Exit 0 when every link target is a research URL, 1 otherwise (prints each
offending target with its line number).
"""
import json
import re
import sys

# Link target, allowing one level of parentheses inside the URL.
LINK_RE = re.compile(r'\]\(((?:[^()\s]|\([^()\s]*\))+)\)')


def research_urls(research):
    urls = set()
    for story in research.get('stories', []):
        for src in story.get('sources', []):
            if src.get('url'):
                urls.add(src['url'])
        for fact in story.get('key_facts', []):
            if fact.get('source_url'):
                urls.add(fact['source_url'])
    return urls


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    edition_path, research_path = sys.argv[1], sys.argv[2]
    with open(research_path, encoding='utf-8') as f:
        known = research_urls(json.load(f))
    if not known:
        sys.exit(f'check-links — ERROR: no source URLs in {research_path}')

    total, bad = 0, []
    with open(edition_path, encoding='utf-8') as f:
        for n, line in enumerate(f, 1):
            for target in LINK_RE.findall(line):
                total += 1
                if target not in known:
                    bad.append((n, target))

    if bad:
        print(f'check-links — FAIL: {len(bad)} of {total} link(s) not in {research_path}:')
        for n, target in bad:
            print(f'  line {n}: {target}')
        sys.exit(1)
    if total == 0:
        sys.exit(f'check-links — FAIL: no links found in {edition_path}')
    print(f'check-links — {total} links, all from research.json')


if __name__ == '__main__':
    main()
