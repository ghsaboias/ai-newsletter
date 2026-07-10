#!/usr/bin/env python3
"""Render a selections JSON into the exact "Recomendações de hoje" HTML block.

The HTML mirrors byte-for-byte how Substack stores the hand-added section today
(verified against a live published post), so iteration 2's draft push can reuse
this output verbatim instead of the model retyping the embed markup.

Input (stdin or --in FILE), the schema the skill writes to recs.json:

    {
      "section_title": "Recomendações de hoje:",
      "items": [
        {"title": "...", "description_pt": "...", "youtube_id": "abc123",
         "start_seconds": 39, "channel": "...", "published_at": "2026-07-05"}
      ]
    }

`start_seconds` may be null (no trim). Output: HTML to stdout.
"""
import argparse
import html
import json
import sys

EMBED = (
    '<div id="youtube2-{vid}" class="youtube-wrap" '
    'data-attrs="{attrs}" data-component-name="Youtube2ToDOM">'
    '<div class="youtube-inner">'
    '<iframe src="https://www.youtube-nocookie.com/embed/{vid}?{qs}'
    'rel=0&amp;autoplay=0&amp;showinfo=0&amp;enablejsapi=0" '
    'frameborder="0" loading="lazy" gesture="media" '
    'allow="autoplay; fullscreen" allowautoplay="true" allowfullscreen="true" '
    'width="728" height="409"></iframe></div></div>'
)
SEP = "<div><hr></div>"


def esc(s: str) -> str:
    return html.escape(s or "", quote=False)


def embed(vid: str, start_seconds) -> str:
    start = f"{int(start_seconds)}s" if start_seconds not in (None, "", 0) else None
    attrs_obj = {"videoId": vid, "startTime": start, "endTime": None}
    # Substack stores data-attrs as HTML-escaped JSON (quotes -> &quot;).
    attrs = html.escape(json.dumps(attrs_obj, separators=(",", ":")), quote=True)
    qs = f"start={start}&amp;" if start else ""
    return EMBED.format(vid=vid, attrs=attrs, qs=qs)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="infile", default=None)
    args = ap.parse_args()
    raw = open(args.infile, encoding="utf-8").read() if args.infile else sys.stdin.read()
    data = json.loads(raw)

    title = data.get("section_title", "Recomendações de hoje:")
    out = [f"<h4><strong>{esc(title)}</strong></h4>"]
    items = data.get("items", [])
    for i, it in enumerate(items):
        desc = it.get("description_pt") or it.get("blurb_pt") or ""
        out.append(f"<p><strong>{esc(it['title'])}</strong>: {esc(desc)}:</p>")
        out.append(embed(it["youtube_id"], it.get("start_seconds")))
        if i < len(items) - 1:
            out.append(SEP)
    sys.stdout.write("".join(out) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
