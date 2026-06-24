#!/usr/bin/env python3
"""
Upload a local image to Substack's CDN and emit a paywall-banner.json spec.

Use this to (re)generate the partner banner spec consumed by substack_post.py
when the artwork changes. The image only needs to be uploaded once — the CDN
URL it returns is stable and reused on every edition.

Usage:
  python3 substack_upload.py <image_path> [--href URL] [--alt TEXT] [--resize-width N]

Credentials: SUBSTACK_SID / SUBSTACK_PUB_HOST from the environment, falling back
to ~/daily-journal-platform/.env.local (same as substack-post.sh).

Prints the banner spec JSON to stdout. Redirect it into the topic's banner file:

  python3 substack_upload.py ~/abacatepay-parceria.png --href https://abacatepay.com \
    > newsletters/ai/paywall-banner.json
"""

import sys
import os
import json
import base64
import argparse
import mimetypes
import urllib.request
import urllib.error


def load_creds():
    sid = os.environ.get("SUBSTACK_SID")
    host = os.environ.get("SUBSTACK_PUB_HOST")
    if not (sid and host):
        env = os.path.expanduser("~/daily-journal-platform/.env.local")
        if os.path.exists(env):
            with open(env) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("SUBSTACK_SID=") and not sid:
                        sid = line.split("=", 1)[1]
                    elif line.startswith("SUBSTACK_PUB_HOST=") and not host:
                        host = line.split("=", 1)[1]
    if not sid or not host:
        sys.exit("Error: SUBSTACK_SID/SUBSTACK_PUB_HOST not set and not found in .env.local")
    return sid, host


def upload(path, sid, host):
    data = open(path, "rb").read()
    ctype = mimetypes.guess_type(path)[0] or "image/png"
    datauri = f"data:{ctype};base64," + base64.b64encode(data).decode()
    payload = json.dumps({"image": datauri}).encode("utf-8")
    req = urllib.request.Request(
        f"https://{host}/api/v1/image",
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Cookie": f"substack.sid={sid}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        },
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description="Upload an image to Substack and emit a banner spec.")
    ap.add_argument("image", help="path to the local image file")
    ap.add_argument("--href", default=None, help="link the banner points to (e.g. https://abacatepay.com)")
    ap.add_argument("--alt", default=None, help="alt text")
    ap.add_argument("--resize-width", type=int, default=None,
                    help="display width in px (omit for full content width)")
    args = ap.parse_args()

    path = os.path.expanduser(args.image)
    if not os.path.exists(path):
        sys.exit(f"Error: not found: {path}")

    sid, host = load_creds()
    try:
        res = upload(path, sid, host)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")

    spec = {
        "src": res["url"],
        "width": res.get("imageWidth"),
        "height": res.get("imageHeight"),
        "resizeWidth": args.resize_width,
        "bytes": res.get("bytes"),
        "type": res.get("contentType"),
        "alt": args.alt,
        "href": args.href,
    }
    print(json.dumps(spec, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
