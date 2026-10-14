#!/usr/bin/env python3
"""
Build a partner-insertion model from a small spec and publish it as a Substack
post template, then register it for the Cliente in registry.json.

Spec (newsletters/ai/insertions/<slug>.spec.json):
  {
    "cliente": "Praso",                       # the board's Cliente field = registry key
    "slug": "praso-trainee",
    "template_name": "Inserção Praso (trainee)",
    "link": "https://...?...utm...",          # the card's tracked link: banner href + button url
    "banner_png": "praso-trainee-banner.png", # relative to the insertions dir; 1272×312
    "banner_alt": "Programa de trainee da Praso",
    "paragraphs": ["A **Praso** ...", "**Salário de R$ 10 mil** e R$ 1.800 em benefícios", ...],
    "button": "Conhecer mais"
  }

`**bold**` in a paragraph becomes a strong mark. The doc mirrors the existing
models: captionedImage (banner, href) → centered paragraphs → button → rule.

Usage:
  insertion_model.py create <spec.json> [--dry-run]
    Uploads the banner, writes <slug>.json (the ProseMirror doc), creates the
    template (or updates it, when the Cliente is already registered), and
    upserts registry.json. --dry-run builds the doc with a placeholder src and
    prints it, touching nothing.
"""

import os
import re
import sys
import json
import argparse
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from substack_upload import load_creds, upload  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INS_DIR = os.path.join(REPO, "newsletters", "ai", "insertions")
REGISTRY = os.path.join(INS_DIR, "registry.json")


def inline(text):
    out = []
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", text)):
        if not part:
            continue
        node = {"type": "text", "text": part}
        if i % 2:
            node["marks"] = [{"type": "strong"}]
        out.append(node)
    return out


def build_doc(spec, banner):
    image = {
        "type": "captionedImage",
        "content": [{"type": "image2", "attrs": {
            "src": banner["src"], "srcNoWatermark": None, "fullscreen": None, "imageSize": None,
            "height": banner.get("height"), "width": banner.get("width"), "resizeWidth": None,
            "bytes": banner.get("bytes"), "alt": spec.get("banner_alt", ""), "title": None,
            "type": banner.get("type"), "href": spec["link"], "belowTheFold": False,
            "topImage": False, "internalRedirect": None, "isProcessing": False,
            "align": None, "offset": False}}],
    }
    paras = [{"type": "paragraph", "attrs": {"textAlign": "center"}, "content": inline(p)}
             for p in spec["paragraphs"]]
    button = {"type": "button", "attrs": {"url": spec["link"], "text": spec.get("button", "Conhecer mais"),
                                          "action": None, "class": None}}
    return {"type": "doc", "content": [image, *paras, button, {"type": "horizontal_rule"}]}


def sstats(*args):
    r = subprocess.run(["sstats", *args], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Error: sstats {' '.join(args)}: {r.stderr.strip()[:300]}")
    return json.loads(r.stdout)


def cmd_create(args):
    spec = json.load(open(args.spec, encoding="utf-8"))
    for k in ("cliente", "slug", "template_name", "link", "banner_png", "paragraphs"):
        if not spec.get(k):
            sys.exit(f"Error: spec sem '{k}'")
    png = os.path.join(INS_DIR, spec["banner_png"])
    if not os.path.exists(png):
        sys.exit(f"Error: banner não encontrado: {png}")

    if args.dry_run:
        doc = build_doc(spec, {"src": "<upload>", "width": 1272, "height": 312, "type": "image/png"})
        print(json.dumps(doc, ensure_ascii=False, indent=1))
        return

    sid, host = load_creds()
    res = upload(png, sid, host)
    banner = {"src": res["url"], "width": res.get("imageWidth"), "height": res.get("imageHeight"),
              "bytes": res.get("bytes"), "type": res.get("contentType")}
    doc = build_doc(spec, banner)
    doc_path = os.path.join(INS_DIR, f"{spec['slug']}.json")
    with open(doc_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)

    registry = json.load(open(REGISTRY, encoding="utf-8"))
    entry = registry.get(spec["cliente"])
    if isinstance(entry, dict) and entry.get("template_id"):
        t = sstats("template-update", str(entry["template_id"]), doc_path, "--name", spec["template_name"])
        action = "updated"
    else:
        t = sstats("template-create", spec["template_name"], doc_path)
        action = "created"
    registry[spec["cliente"]] = {"template_id": t["id"], "source": os.path.basename(doc_path),
                                 "notes": os.path.basename(args.spec)}
    with open(REGISTRY, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"{action} template {t['id']} '{t['name']}' for {spec['cliente']} | doc {doc_path} | banner {banner['src']}")


def main():
    ap = argparse.ArgumentParser(description="Create/update a partner-insertion model.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("create")
    p.add_argument("spec")
    p.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    {"create": cmd_create}[args.cmd](args)


if __name__ == "__main__":
    main()
