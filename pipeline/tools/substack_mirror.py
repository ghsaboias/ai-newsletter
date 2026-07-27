#!/usr/bin/env python3
"""
Local mirror of a Substack draft's editable state (title, subtitle, body).

The pipeline pushes ONCE from HTML (substack_post.py); after that the Substack
draft is the source of truth and is edited in place (images, captions, video,
manual tweaks). This tool gives a safe local edit loop for that live draft:

  pull  -> GET the draft, write its title/subtitle/body (ProseMirror JSON) to a
           local mirror file. This INCLUDES images/video/captions already on the
           draft, so it never loses them.
  push  -> read the mirror file and PUT it back, preserving the author byline,
           section, audience and type (paywall/banner nodes live in `body`, so
           they're preserved automatically).
  media -> insert per-story images/videos into the live draft from an
           images-final.json plan (upload each image to CDN at 520px, add its
           caption, split the story's bullet_list at the right spot, embed
           videos), then push. Unified "add media to the draft" path that
           replaces injecting into substack.html. Re-runnable with --replace.

Edit the mirror JSON between pull and push — the `body` is the ProseMirror doc
(`{"type":"doc","content":[...]}`); `title` and `subtitle` are plain strings.

images-final.json (for `media`) is a list, one entry per story that gets media:
  { "heading": "OpenAI",           # substring that locates the story heading
    "after_bullet": "Participação", # omit for a Grande (image after whole bullet_list);
                                    # for a category, the bold label of the bullet to sit under
    "file": "/abs/path/img.jpg",   # local image (uploaded to CDN); omit for video-only
    "alt": "...", "caption": "Sujeito, contexto. Imagem: Fonte",
    "videoId": "iPyxwELiD9Q" }     # optional YouTube id, embedded right after the image

Usage:
  substack_mirror.py pull  [--id DRAFT_ID] [--dir EDITION_DIR] [--file PATH]
  substack_mirror.py push  [--id DRAFT_ID] [--dir EDITION_DIR] [--file PATH] [--byline ID]
  substack_mirror.py media --plan images-final.json [--replace] [--dry-run] [--id ...] [--dir ...]

Defaults:
  --dir   pipeline/output/${PIPELINE_TOPIC:-ai}/<today>
  --id    read from <dir>/.substack-draft-id
  --file  <dir>/substack-body.json
  --byline 473611573  (Daily Journal author)

Creds: SUBSTACK_SID / SUBSTACK_PUB_HOST from env, else ~/daily-journal-platform/.env.local
"""

import os
import sys
import json
import base64
import mimetypes
import argparse
import datetime
import urllib.request
import urllib.error

DEFAULT_BYLINE = 473611573
RESIZE_WIDTH = 520  # editorial image display width — the newsletter standard
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def load_creds():
    sid = os.environ.get("SUBSTACK_SID")
    host = os.environ.get("SUBSTACK_PUB_HOST")
    if not (sid and host):
        env = os.path.expanduser("~/daily-journal-platform/.env.local")
        if os.path.exists(env):
            for line in open(env):
                line = line.strip()
                if line.startswith("SUBSTACK_SID=") and not sid:
                    sid = line.split("=", 1)[1]
                elif line.startswith("SUBSTACK_PUB_HOST=") and not host:
                    host = line.split("=", 1)[1]
    if not sid or not host:
        sys.exit("Error: SUBSTACK_SID/SUBSTACK_PUB_HOST not set and not in .env.local")
    return sid, host


def resolve_paths(args):
    topic = os.environ.get("PIPELINE_TOPIC", "ai")
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(os.path.dirname(here))  # pipeline/tools -> repo root
    today = datetime.date.today().isoformat()
    d = args.dir or os.path.join(repo, "pipeline", "output", topic, today)
    draft_id = args.id
    if not draft_id:
        idf = os.path.join(d, ".substack-draft-id")
        if os.path.exists(idf):
            draft_id = open(idf).read().strip()
    if not draft_id:
        sys.exit(f"Error: no --id and no {os.path.join(d, '.substack-draft-id')}")
    path = args.file or os.path.join(d, "substack-body.json")
    return draft_id, path


def get_draft(host, sid, draft_id):
    req = urllib.request.Request(
        f"https://{host}/api/v1/drafts/{draft_id}",
        headers={"Cookie": f"substack.sid={sid}", "User-Agent": UA},
    )
    return json.loads(urllib.request.urlopen(req).read().decode("utf-8"))


def put_draft(host, sid, draft_id, payload):
    req = urllib.request.Request(
        f"https://{host}/api/v1/drafts/{draft_id}",
        data=json.dumps(payload).encode("utf-8"),
        method="PUT",
        headers={"Content-Type": "application/json",
                 "Cookie": f"substack.sid={sid}", "User-Agent": UA},
    )
    return json.loads(urllib.request.urlopen(req).read().decode("utf-8"))


def cmd_pull(args):
    sid, host = load_creds()
    draft_id, path = resolve_paths(args)
    d = get_draft(host, sid, draft_id)
    body = d.get("draft_body")
    body = json.loads(body) if isinstance(body, str) else body
    mirror = {
        "draft_id": str(draft_id),
        "title": d.get("draft_title"),
        "subtitle": d.get("draft_subtitle"),
        "body": body,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(mirror, f, ensure_ascii=False, indent=1)
    n = len(body.get("content", [])) if isinstance(body, dict) else "?"
    imgs = sum(1 for x in body.get("content", []) if x.get("type") == "captionedImage")
    vids = sum(1 for x in body.get("content", []) if x.get("type") in ("youtube2", "video", "twitter2"))
    print(f"pulled draft {draft_id} -> {path}")
    print(f"  {n} nodes | {imgs} captionedImage | {vids} embeds")
    print(f"  title: {mirror['title']!r}")


def cmd_push(args):
    sid, host = load_creds()
    draft_id, path = resolve_paths(args)
    if not os.path.exists(path):
        sys.exit(f"Error: mirror file not found: {path} (run pull first)")
    mirror = json.load(open(path, encoding="utf-8"))
    if str(mirror.get("draft_id")) != str(draft_id):
        print(f"  warning: mirror draft_id {mirror.get('draft_id')} != target {draft_id}")
    body = mirror["body"]
    # Preserve section/audience/type from the live draft.
    live = get_draft(host, sid, draft_id)
    payload = {
        "draft_title": mirror.get("title"),
        "draft_subtitle": mirror.get("subtitle"),
        "draft_body": json.dumps(body, ensure_ascii=False),
        "draft_bylines": [{"id": args.byline}],
        "draft_section_id": live.get("draft_section_id"),
        "audience": live.get("audience", "everyone"),
        "draft_podcast_url": "",
        "draft_podcast_duration": None,
        "draft_video_upload_id": None,
        "type": live.get("type", "newsletter"),
    }
    try:
        r = put_draft(host, sid, draft_id, payload)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:400]}")
    n = len(body.get("content", []))
    print(f"pushed {path} -> draft {draft_id}")
    print(f"  {n} nodes | byline id {args.byline} | updated_at {r.get('draft_updated_at')}")
    print(f"  editor: https://{host}/publish/post/{draft_id}")


# ---------------------------------------------------------------------------
# media: insert per-story images/videos into the live draft (unified path)
# ---------------------------------------------------------------------------

def upload_image(host, sid, path, alt):
    data = open(path, "rb").read()
    ctype = mimetypes.guess_type(path)[0] or "image/png"
    datauri = f"data:{ctype};base64," + base64.b64encode(data).decode()
    req = urllib.request.Request(
        f"https://{host}/api/v1/image",
        data=json.dumps({"image": datauri}).encode("utf-8"), method="POST",
        headers={"Content-Type": "application/json",
                 "Cookie": f"substack.sid={sid}", "User-Agent": UA})
    r = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
    return {"src": r["url"], "width": r.get("imageWidth"), "height": r.get("imageHeight"),
            "bytes": r.get("bytes"), "type": r.get("contentType"), "alt": alt}


def image_node(spec, caption):
    node = {"type": "captionedImage", "content": [{
        "type": "image2", "attrs": {
            "src": spec["src"], "srcNoWatermark": None, "fullscreen": None, "imageSize": None,
            "height": spec.get("height"), "width": spec.get("width"), "resizeWidth": RESIZE_WIDTH,
            "bytes": spec.get("bytes"), "alt": spec.get("alt"), "title": None, "type": spec.get("type"),
            "href": None, "belowTheFold": False, "topImage": False, "internalRedirect": None,
            "isProcessing": False, "align": None, "offset": False}}]}
    if caption:
        node["content"].append({"type": "caption", "content": [{"type": "text", "text": caption}]})
    return node


def video_node(video_id):
    return {"type": "youtube2", "attrs": {"videoId": video_id, "startTime": None, "endTime": None}}


def _heading_idx(content, sub):
    # Exact heading match wins over substring, so a short category name that is
    # also a substring of an earlier, longer heading resolves to its own section
    # (e.g. the Médias "OpenAI" category vs the Grande "OpenAI libera o GPT-5.6…").
    for i, n in enumerate(content):
        if n.get("type") == "heading" and "".join(c.get("text", "") for c in n.get("content", [])) == sub:
            return i
    for i, n in enumerate(content):
        if n.get("type") == "heading" and sub in "".join(c.get("text", "") for c in n.get("content", [])):
            return i
    return None


def _next_heading(content, start):
    for j in range(start + 1, len(content)):
        if content[j].get("type") == "heading":
            return j
    return len(content)


def _li_label(li):
    for p in li.get("content", []):
        for c in p.get("content", []):
            if c.get("type") == "text":
                return c["text"]
    return ""


def insert_after_bulletlist(doc, heading_sub, media):
    """Grande: insert media after the story's whole bullet_list."""
    c = doc["content"]
    hi = _heading_idx(c, heading_sub)
    if hi is None:
        return f"heading '{heading_sub}' not found"
    nh = _next_heading(c, hi)
    last = None
    for j in range(hi + 1, nh):
        if c[j].get("type") == "bullet_list":
            last = j
    if last is None:
        return f"no bullet_list under '{heading_sub}'"
    c[last + 1:last + 1] = media
    return "ok"


def insert_after_bullet(doc, heading_sub, label, media):
    """Category: split the bullet_list after the labelled item, insert media."""
    c = doc["content"]
    hi = _heading_idx(c, heading_sub)
    if hi is None:
        return f"heading '{heading_sub}' not found"
    nh = _next_heading(c, hi)
    for j in range(hi + 1, nh):
        if c[j].get("type") == "bullet_list":
            items = c[j]["content"]
            for idx, li in enumerate(items):
                if _li_label(li).startswith(label):
                    before, after = items[:idx + 1], items[idx + 1:]
                    repl = [{"type": "bullet_list", "content": before}] + media
                    if after:
                        repl.append({"type": "bullet_list", "content": after})
                    c[j:j + 1] = repl
                    return "ok"
    return f"bullet '{label}' not found under '{heading_sub}'"


def strip_editorial_media(doc):
    """Remove previously-inserted editorial media so `media` is re-runnable.
    Drops top-level captionedImage without href (ads keep their href) and
    youtube2/video embeds — but STOPS at the recommendations boundary
    (a calloutBlock, or a paragraph mentioning 'Recomendações'/'Leia também'),
    so curated recommendation embeds are preserved.
    """
    out, removed = [], 0
    for n in doc["content"]:
        t = n.get("type")
        txt = "".join(c.get("text", "") for c in n.get("content", []) if isinstance(c, dict)) if t == "paragraph" else ""
        if t == "calloutBlock" or ("Recomenda" in txt or "Leia também" in txt):
            out.append(n)
            out.extend(doc["content"][doc["content"].index(n) + 1:])
            break
        if t == "captionedImage" and not n["content"][0]["attrs"].get("href"):
            removed += 1; continue
        if t in ("youtube2", "video"):
            removed += 1; continue
        out.append(n)
    doc["content"] = out
    return removed


def cmd_media(args):
    sid, host = load_creds()
    draft_id, mirror_path = resolve_paths(args)
    plan = json.load(open(args.plan, encoding="utf-8"))
    live = get_draft(host, sid, draft_id)
    doc = json.loads(live["draft_body"])

    if args.replace:
        r = strip_editorial_media(doc)
        print(f"  --replace: stripped {r} existing editorial media node(s)")
    else:
        pre = sum(1 for n in doc["content"]
                  if n.get("type") == "captionedImage" and not n["content"][0]["attrs"].get("href"))
        if pre:
            sys.exit(f"Draft already has {pre} editorial image(s). Re-run with --replace, "
                     f"or edit via pull/push instead.")

    results = []
    for e in plan:
        media = []
        if e.get("file"):
            spec = upload_image(host, sid, os.path.expanduser(e["file"]), e.get("alt") or e.get("caption", ""))
            media.append(image_node(spec, e.get("caption", "")))
        if e.get("videoId"):
            media.append(video_node(e["videoId"]))
        if not media:
            results.append((e.get("heading"), "no file/videoId — skipped")); continue
        if e.get("after_bullet"):
            r = insert_after_bullet(doc, e["heading"], e["after_bullet"], media)
        else:
            r = insert_after_bulletlist(doc, e["heading"], media)
        results.append((f"{e.get('heading')}/{e.get('after_bullet') or '(grande)'}", r))

    for name, r in results:
        print(f"  insert [{name}] -> {r}")
    ok = all(r == "ok" for _, r in results if r not in ("no file/videoId — skipped",))

    if args.dry_run:
        print(f"\n[dry-run] no push. body would have {len(doc['content'])} nodes.")
        return
    if not ok:
        sys.exit("\nAborted push — some inserts failed; draft untouched.")

    payload = {
        "draft_title": live.get("draft_title"), "draft_subtitle": live.get("draft_subtitle"),
        "draft_body": json.dumps(doc, ensure_ascii=False), "draft_bylines": [{"id": args.byline}],
        "draft_section_id": live.get("draft_section_id"), "audience": live.get("audience", "everyone"),
        "draft_podcast_url": "", "draft_podcast_duration": None, "draft_video_upload_id": None,
        "type": live.get("type", "newsletter")}
    r = put_draft(host, sid, draft_id, payload)
    imgs = sum(1 for n in doc["content"] if n.get("type") == "captionedImage")
    print(f"\npushed media -> draft {draft_id} | {len(doc['content'])} nodes, {imgs} captionedImage | "
          f"updated_at {r.get('draft_updated_at')}")

    # Verify the server actually retained what we sent (the printed count above is
    # the LOCAL doc, not a re-fetch). Re-GET and count server-side so a silent
    # strip surfaces immediately instead of being discovered later in the editor.
    try:
        chk = json.loads(get_draft(host, sid, draft_id)["draft_body"])
        got_img = sum(1 for n in chk["content"] if n.get("type") == "captionedImage")
        got_vid = sum(1 for n in chk["content"] if n.get("type") in ("youtube2", "video", "twitter2"))
        want_vid = sum(1 for n in doc["content"] if n.get("type") in ("youtube2", "video", "twitter2"))
        if got_img >= imgs and got_vid >= want_vid:
            print(f"  verified server-side: {got_img} captionedImage, {got_vid} embed(s) retained")
        else:
            print(f"  !! WARNING: server kept {got_img}/{imgs} images, {got_vid}/{want_vid} embeds — some were dropped on PUT")
    except Exception as ex:
        print(f"  (verify skipped: {ex})")

    print(f"  editor: https://{host}/publish/post/{draft_id}")
    print("  IMPORTANT: media lives in draft_body via the API. The Substack web editor")
    print("  keeps its own live copy and its autosave-on-open OVERWRITES this push if a")
    print("  warm/stale editor tab was open. To keep the images: fully CLOSE any open")
    print("  editor tab for this post, then reopen it COLD (hard refresh) so it hydrates")
    print("  from the server. Never leave a warm editor tab open across a media push.")


def main():
    ap = argparse.ArgumentParser(description="Pull/push/media a Substack draft body mirror.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("pull", "push", "media"):
        p = sub.add_parser(name)
        p.add_argument("--id", default=None, help="draft id (default: <dir>/.substack-draft-id)")
        p.add_argument("--dir", default=None, help="edition dir (default: pipeline/output/<topic>/<today>)")
        p.add_argument("--file", default=None, help="mirror path (default: <dir>/substack-body.json)")
        if name in ("push", "media"):
            p.add_argument("--byline", type=int, default=DEFAULT_BYLINE, help="author id")
        if name == "media":
            p.add_argument("--plan", required=True, help="images-final.json (per-story media plan)")
            p.add_argument("--replace", action="store_true", help="strip prior editorial media first (re-runnable)")
            p.add_argument("--dry-run", action="store_true", help="show planned inserts, do not push")
    args = ap.parse_args()
    {"pull": cmd_pull, "push": cmd_push, "media": cmd_media}[args.cmd](args)


if __name__ == "__main__":
    main()
