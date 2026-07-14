#!/usr/bin/env python3
"""Extract the "Recomendações de hoje" section from a published Substack post.

Reads post body_html on stdin (as produced by `sstats post <id> --html`) and
prints a structured Markdown block for the day's video recommendations:

    ## YYYY-MM-DD

    **Title**
    Description paragraph.
    https://www.youtube.com/watch?v=VIDEOID

Prints nothing (exit 0) when the post has no recommendations section — e.g.
weekend, free editions, or older editions that predate the feature. That empty
output is the signal the caller uses to skip the edition.

Notes on the source HTML:
- The real recommendations section is the LAST "Recomendaç... de hoje" header.
  Some editions carry a pre-paywall teaser header with no embeds; the actual
  section (with video embeds) sits at the end of the post, after the paywall.
- Each recommendation is a <p><strong>Title</strong>: description:</p> followed
  immediately by a <div class="youtube-wrap" data-attrs="{...videoId...}">.
- Article bodies can also embed YouTube videos, so we only pair embeds that
  fall inside the recommendations region.
"""

import argparse
import html as htmllib
import re
import sys


def clean(fragment: str) -> str:
    """Strip tags, unescape entities, collapse whitespace."""
    text = re.sub(r"<[^>]+>", "", fragment)
    text = htmllib.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def extract(doc: str):
    headers = list(re.finditer(r"Recomenda\w+\s+de\s+hoje", doc))
    if not headers:
        return []
    region = doc[headers[-1].end():]

    recs = []
    for div in re.finditer(r'<div[^>]*class="youtube-wrap"[^>]*>', region):
        tag = div.group(0)
        vm = re.search(r"videoId&quot;:&quot;([\w-]+)", tag) or re.search(
            r"youtube2-([\w-]+)", tag
        )
        if not vm:
            continue
        video_id = vm.group(1)

        # The recommendation's title/description is the last <p> closing before
        # this embed.
        preceding = region[: div.start()]
        paragraphs = list(re.finditer(r"<p\b[^>]*>(.*?)</p>", preceding, re.S))
        if not paragraphs:
            continue
        block = paragraphs[-1].group(1)

        strong = re.search(r"<strong\b[^>]*>(.*?)</strong>", block, re.S)
        if strong:
            title = clean(strong.group(1)).rstrip(":").strip()
            desc = clean(block[strong.end():])
        else:
            title = ""
            desc = clean(block)
        desc = desc.lstrip(":").strip().rstrip(":").strip()

        recs.append((title, desc, video_id))
    return recs


def format_block(date: str, recs) -> str:
    """Render a list of (title, desc, video_id) as the archive's Markdown block.

    Returns the canonical `## DATE` section (no trailing newline). Empty recs
    yield an empty string so callers can treat "no recommendations" uniformly.
    """
    if not recs:
        return ""
    lines = [f"## {date}", ""]
    for title, desc, video_id in recs:
        if title:
            lines.append(f"**{title}**")
        if desc:
            lines.append(desc)
        lines.append(f"https://www.youtube.com/watch?v={video_id}")
        lines.append("")
    return "\n".join(lines).rstrip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Edition date, YYYY-MM-DD")
    args = parser.parse_args()

    block = format_block(args.date, extract(sys.stdin.read()))
    if not block:
        return 0
    sys.stdout.write(block + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
