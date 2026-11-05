#!/usr/bin/env python3
"""Render a pulled Substack draft mirror (substack-body.json) back to the
edition markdown format. Lossy for push-only artifacts (banner/paywall), which
are emitted as HTML comments so a diff against the source edition is legible.

With --edition, render only what the generator writes: no image or paywall
comments, and nothing from the sections appended after the edition
(recommendations, funding rounds). Those are told apart by structure, not by
title, since titles get edited by hand: the lead stories are the only h3
headings before the first rule, so an h3 after it starts an appended section."""
import json, sys

def _fmt(node):
    t = node.get("text", "")
    marks = {m["type"]: m for m in node.get("marks", [])}
    if "strong" in marks:
        t = f"**{t}**"
    if "em" in marks:
        t = f"*{t}*"
    return t, (marks["link"]["attrs"]["href"] if "link" in marks else None)

def inline(nodes):
    # Coalesce consecutive text nodes sharing the same link href into a single
    # [..](href) span so an edited link doesn't render as two adjacent links.
    nodes = [n for n in (nodes or []) if n.get("type") == "text"]
    out, i = "", 0
    while i < len(nodes):
        seg, href = _fmt(nodes[i])
        if href is not None:
            i += 1
            while i < len(nodes):
                s2, h2 = _fmt(nodes[i])
                if h2 != href:
                    break
                seg += s2
                i += 1
            out += f"[{seg}]({href})"
        else:
            out += seg
            i += 1
    return out

def bullets(node, out):
    for li in node.get("content", []):
        for p in li.get("content", []):
            if p.get("type") == "paragraph":
                out.append("- " + inline(p.get("content", [])))

def render(m, edition=False):
    out = []
    past_leads = False
    if m.get("title"):
        out += ["# " + m["title"], ""]
    if m.get("subtitle"):
        out += [m["subtitle"], ""]
    for node in m["body"]["content"]:
        t = node["type"]
        if t == "horizontal_rule":
            past_leads = True
        if edition and past_leads and t == "heading" and node["attrs"]["level"] <= 3:
            break
        if edition and t in ("captionedImage", "paywall"):
            continue
        if t == "paragraph":
            txt = inline(node.get("content", []))
            if txt.strip():
                out += [txt, ""]
        elif t == "heading":
            out += ["#" * node["attrs"]["level"] + " " + inline(node.get("content", [])), ""]
        elif t == "bullet_list":
            bullets(node, out); out.append("")
        elif t == "blockquote":
            for p in node.get("content", []):
                out.append("> " + inline(p.get("content", [])))
            out.append("")
        elif t == "horizontal_rule":
            out += ["---", ""]
        elif t == "captionedImage":
            a = node["content"][0]["attrs"]
            out += [f'<!-- image: {a.get("alt","")} | {a.get("src","")} -->', ""]
        elif t == "paywall":
            out += ["<!-- paywall -->", ""]
        elif t == "calloutBlock":
            for c in node.get("content", []):
                if c["type"] == "heading":
                    out += ["#" * c["attrs"]["level"] + " " + inline(c.get("content", [])), ""]
                elif c["type"] == "bullet_list":
                    bullets(c, out); out.append("")
    while out and out[-1] in ("", "---"):
        out.pop()
    return "\n".join(out) + "\n"


def main():
    args = [a for a in sys.argv[1:] if a != "--edition"]
    m = json.load(open(args[0], encoding="utf-8"))
    sys.stdout.write(render(m, edition="--edition" in sys.argv))

if __name__ == "__main__":
    main()
