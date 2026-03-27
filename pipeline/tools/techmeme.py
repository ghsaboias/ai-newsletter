#!/usr/bin/env python3
"""
Fetch and parse Techmeme headlines into structured text.

Usage:
    python3 techmeme.py              # fetch live
    python3 techmeme.py --json       # output as JSON
    python3 techmeme.py --file X.html # parse from local file (for testing)
"""

import re
import sys
import json
import urllib.request
import html as html_module


def fetch_html(url="https://www.techmeme.com/", timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def decode(text):
    """Decode HTML entities and clean whitespace."""
    text = html_module.unescape(text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_techmeme(raw_html):
    stories = []

    # Each story is wrapped in a DIV CLASS="itc2" block
    blocks = re.split(r'<DIV CLASS="itc2"', raw_html)[1:]

    for block in blocks:
        # Extract primary headline
        headline_match = re.search(
            r'CLASS="ourh" HREF="([^"]+)">([^<]+)</A></STRONG>', block
        )
        if not headline_match:
            continue

        url = headline_match.group(1)
        title = decode(headline_match.group(2))

        # Extract summary (text after mdash)
        summary = ""
        summary_match = re.search(
            r"</STRONG>\s*(?:&nbsp;\s*)?(?:&mdash;|—)\s*(?:&nbsp;\s*)?(.+?)</DIV>",
            block,
        )
        if summary_match:
            summary = decode(re.sub(r"<[^>]+>", "", summary_match.group(1)))

        # Extract source/author from CITE before headline
        source = ""
        cite_match = re.search(
            r"<CITE>(.*?)</CITE>\s*</td>.*?CLASS=\"ourh\"", block, re.DOTALL
        )
        if cite_match:
            source = decode(re.sub(r"<[^>]+>", "", cite_match.group(1)))
            source = source.rstrip(":")

        # Extract "More:" links (secondary sources)
        more_sources = []
        more_block = re.search(
            r'<SPAN CLASS="drhed">More:</SPAN>\s*(?:&nbsp;)?\s*<span class="bls">(.*?)</span>',
            block,
            re.DOTALL,
        )
        if more_block:
            more_links = re.findall(
                r'<A HREF="([^"]+)">([^<]+)</A>', more_block.group(1)
            )
            more_sources = [
                {"name": decode(name), "url": u} for u, name in more_links
            ]

        # Extract X/tweet highlights from expanded section
        highlights = []
        x_block = re.search(
            r'drhed">X:</DIV>(.*?)(?:<DIV CLASS="dbpt">|</DIV>\s*</DIV>\s*</DIV>)',
            block,
            re.DOTALL,
        )
        if x_block:
            tweets = re.findall(
                r'<CITE>.*?<A HREF="https://x\.com/(\w+)">@\1</A>.*?</CITE>\s*(?:&nbsp;)?\s*<A HREF="([^"]+)">(.+?)</A>',
                x_block.group(1),
                re.DOTALL,
            )
            for handle, tweet_url, text in tweets[:5]:
                clean = decode(re.sub(r"<[^>]+>", "", text))
                highlights.append(
                    {"handle": handle, "url": tweet_url, "text": clean}
                )

        stories.append(
            {
                "title": title,
                "url": url,
                "source": source,
                "summary": summary,
                "highlights": highlights,
                "more_sources": more_sources,
            }
        )

    return stories


def format_text(stories):
    lines = [f"# Techmeme — {len(stories)} stories\n"]
    for i, s in enumerate(stories, 1):
        lines.append(f"{i}. {s['title']}")
        lines.append(f"   {s['source']} — {s['url']}")
        if s["summary"]:
            lines.append(f"   {s['summary'][:200]}")
        for h in s.get("highlights", []):
            lines.append(f'   > @{h["handle"]}: {h["text"][:200]}')
        if s["more_sources"]:
            names = [m["name"] for m in s["more_sources"][:8]]
            extra = len(s["more_sources"]) - 8
            src_line = ", ".join(names)
            if extra > 0:
                src_line += f", +{extra} more"
            lines.append(f"   Also: {src_line}")
        lines.append("")
    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    output_json = "--json" in args
    file_path = None

    for i, arg in enumerate(args):
        if arg == "--file" and i + 1 < len(args):
            file_path = args[i + 1]

    if file_path:
        with open(file_path) as f:
            raw_html = f.read()
    else:
        raw_html = fetch_html()

    stories = parse_techmeme(raw_html)

    if output_json:
        json.dump(stories, sys.stdout, indent=2, ensure_ascii=False)
    else:
        print(format_text(stories))


if __name__ == "__main__":
    main()
