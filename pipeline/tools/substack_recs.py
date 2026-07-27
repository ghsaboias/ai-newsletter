#!/usr/bin/env python3
"""Push the "Recomendações de hoje" section into a Substack draft.

Builds the section as ProseMirror nodes — heading (h3, bold) + per-video
paragraph (bold "Title:" then " description:") + youtube2 embed, horizontal_rule
between videos — and appends it to the END of the draft body, after the "Leia
também" callout. Node shapes mirror byte-for-byte what the editor produces by
hand (verified against a live post).

Idempotent: strips any existing recs section (its heading + the divider before
it, through end) before appending, so re-running REPLACES rather than stacks.

Input: a recs.json selection written by the /newsletter-recs skill —
    {"section_title": "Recomendações de hoje:",
     "items": [{"title": "...", "description_pt": "...", "youtube_id": "...",
                "start_seconds": 142 | null, ...}]}

Target (pick one):
  --id DRAFT_ID            push into that draft in place
  --dir EDITION_DIR        read the id from <dir>/.substack-draft-id
  --duplicate-from POST_ID copy that post to a NEW draft and push into the copy
                           (safe testing — the original is never touched)

Usage:
  substack_recs.py --file recs.json --id 205752967
  substack_recs.py --file recs.json --duplicate-from 205752967   # test on a copy
  substack_recs.py --file recs.json --dir pipeline/output/ai/2026-07-07 --dry-run

Creds: SUBSTACK_SID / SUBSTACK_PUB_HOST from env, else ~/daily-journal-platform/.env.local
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from substack_mirror import DEFAULT_BYLINE, UA, get_draft, load_creds, put_draft

RECS_HEADING = "Recomendações de hoje:"


# --- ProseMirror node builders (shapes verified against a live draft) ---------

def heading_node(text):
    return {"type": "heading", "attrs": {"textAlign": None, "level": 3},
            "content": [{"type": "text", "marks": [{"type": "strong"}], "text": text}]}


def rec_paragraph(title, desc):
    # Bold "Title:", then " description:" — the leading space and trailing colon
    # match the hand-made format (the colon leads into the embed). Drop a trailing
    # period on the description so it doesn't read ".:" before the leading colon
    # (an ellipsis is left alone).
    desc = desc.rstrip()
    if desc.endswith(".") and not desc.endswith(".."):
        desc = desc[:-1]
    return {"type": "paragraph", "attrs": {"textAlign": None}, "content": [
        {"type": "text", "marks": [{"type": "strong"}], "text": f"{title}:"},
        {"type": "text", "text": f" {desc}:"}]}


def youtube_node(vid, start_seconds):
    start = f"{int(start_seconds)}s" if start_seconds not in (None, "", 0) else None
    return {"type": "youtube2", "attrs": {"videoId": vid, "startTime": start, "endTime": None}}


def build_section(items, title=RECS_HEADING):
    nodes = [{"type": "horizontal_rule"}, heading_node(title)]
    for i, it in enumerate(items):
        desc = it.get("description_pt") or it.get("blurb_pt") or ""
        nodes.append(rec_paragraph(it["title"], desc))
        nodes.append(youtube_node(it["youtube_id"], it.get("start_seconds")))
        if i < len(items) - 1:
            nodes.append({"type": "horizontal_rule"})
    return nodes


def strip_recs(content):
    """Drop an existing recs section: its heading, the divider immediately before
    it, and everything after — returns (kept_content, num_removed)."""
    for i, n in enumerate(content):
        if n.get("type") == "heading":
            txt = "".join(c.get("text", "") for c in n.get("content", []) if isinstance(c, dict))
            if "Recomenda" in txt:
                start = i - 1 if i and content[i - 1].get("type") == "horizontal_rule" else i
                return content[:start], len(content) - start
    return content, 0


# --- Substack ----------------------------------------------------------------

def post_new_draft(host, sid, src, byline):
    body = src.get("draft_body")
    payload = {
        "draft_title": "[TESTE] " + (src.get("draft_title") or ""),
        "draft_subtitle": src.get("draft_subtitle") or "",
        "draft_body": body if isinstance(body, str) else json.dumps(body, ensure_ascii=False),
        "draft_bylines": [{"id": byline}],
        "draft_section_id": src.get("draft_section_id"),
        "audience": src.get("audience", "everyone"),
        "draft_podcast_url": "", "draft_podcast_duration": None,
        "draft_video_upload_id": None, "type": src.get("type", "newsletter"),
    }
    req = urllib.request.Request(
        f"https://{host}/api/v1/drafts", data=json.dumps(payload).encode("utf-8"),
        method="POST", headers={"Content-Type": "application/json",
                                "Cookie": f"substack.sid={sid}", "User-Agent": UA})
    return json.loads(urllib.request.urlopen(req).read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, help="recs.json selection")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--id", help="target draft id (in place)")
    g.add_argument("--dir", help="edition dir; reads <dir>/.substack-draft-id")
    g.add_argument("--duplicate-from", help="post id to copy into a new test draft")
    ap.add_argument("--byline", type=int, default=DEFAULT_BYLINE)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    sel = json.load(open(args.file, encoding="utf-8"))
    items = sel.get("items", [])
    if not items:
        sys.exit(f"no items in {args.file}")
    title = sel.get("section_title", RECS_HEADING)

    sid, host = load_creds()

    if args.duplicate_from:
        src = get_draft(host, sid, args.duplicate_from)
        draft_id = post_new_draft(host, sid, src, args.byline).get("id")
        print(f"duplicated post {args.duplicate_from} -> new draft {draft_id}")
    else:
        draft_id = args.id
        if not draft_id and args.dir:
            idf = os.path.join(args.dir, ".substack-draft-id")
            draft_id = open(idf).read().strip() if os.path.exists(idf) else None
        if not draft_id:
            sys.exit("need --id, --dir, or --duplicate-from")

    live = get_draft(host, sid, draft_id)
    body = live["draft_body"]
    doc = json.loads(body) if isinstance(body, str) else body
    kept, removed = strip_recs(doc.get("content", []))
    section = build_section(items, title)
    doc["content"] = kept + section
    print(f"  stripped {removed} old recs node(s); appended {len(section)} node(s) "
          f"for {len(items)} video(s)")

    if args.dry_run:
        print("[dry-run] not pushing. New section nodes:")
        print(json.dumps(section, ensure_ascii=False, indent=1))
        return

    payload = {
        "draft_title": live.get("draft_title"), "draft_subtitle": live.get("draft_subtitle"),
        "draft_body": json.dumps(doc, ensure_ascii=False), "draft_bylines": [{"id": args.byline}],
        "draft_section_id": live.get("draft_section_id"), "audience": live.get("audience", "everyone"),
        "draft_podcast_url": "", "draft_podcast_duration": None, "draft_video_upload_id": None,
        "type": live.get("type", "newsletter"),
    }
    try:
        r = put_draft(host, sid, draft_id, payload)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:400]}")
    print(f"pushed recs -> draft {draft_id} | {len(doc['content'])} nodes | "
          f"updated_at {r.get('draft_updated_at')}")
    print(f"  editor: https://{host}/publish/post/{draft_id}")


if __name__ == "__main__":
    main()
