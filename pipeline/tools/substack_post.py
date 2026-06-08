#!/usr/bin/env python3
"""
Post a newsletter draft to Substack via their internal API.

Usage:
  python3 substack_post.py <html_file> <sid> <pub_host> [paywall_meta_json]

Reads:  substack.html, optionally paywall-meta.json
Effect: creates a draft post on Substack (not published)
Output: prints the draft URL on success
"""

import sys
import json
import os
import re
import urllib.request
from html.parser import HTMLParser

# Publication user ID — byline author for all posts
PUB_USER_ID = 473611573


# ---------------------------------------------------------------------------
# HTML → ProseMirror JSON converter
# ---------------------------------------------------------------------------

class HTMLToProseMirror(HTMLParser):
    """Convert pandoc-generated HTML into Substack's ProseMirror JSON format."""

    def __init__(self):
        super().__init__()
        self._stack = []
        self._doc_content = []
        self._active_marks = []
        self._current_block = None

    def _push_block(self, node):
        self._current_block = node
        self._stack.append(node)

    def _pop_block(self):
        node = self._stack.pop()
        parent = self._stack[-1] if self._stack else None
        if parent is not None:
            parent.setdefault("content", []).append(node)
        else:
            self._doc_content.append(node)
        self._current_block = self._stack[-1] if self._stack else None
        return node

    def _current_inline_parent(self):
        for node in reversed(self._stack):
            t = node.get("type")
            if t in ("paragraph", "heading", "list_item_para"):
                return node
        return None

    def _append_text(self, text):
        if not text:
            return
        # Collapse internal runs of whitespace to a single space, but PRESERVE
        # a leading/trailing space. pandoc emits a separate text node for the
        # text around each inline element (<a>, <strong>); ProseMirror then
        # concatenates adjacent text nodes with no separator, so trimming the
        # boundary space here fuses words ("O <a>primeiro" → "Oprimeiro").
        if text.strip():
            text = re.sub(r"\s+", " ", text)
        else:
            text = " "  # whitespace-only node between inline tags: keep the gap
        if not text:
            return
        parent = self._current_inline_parent()
        if parent is None:
            return
        content = parent.setdefault("content", [])
        node = {"type": "text", "text": text}
        if self._active_marks:
            node["marks"] = list(self._active_marks)
        content.append(node)

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "p":
            self._push_block({"type": "paragraph"})
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._push_block({"type": "heading", "attrs": {"level": int(tag[1])}})
        elif tag == "ul":
            self._push_block({"type": "bullet_list"})
        elif tag == "ol":
            self._push_block({"type": "ordered_list", "attrs": {"start": 1, "type": None, "order": 1}})
        elif tag == "li":
            self._push_block({"type": "list_item"})
            self._push_block({"type": "list_item_para"})
        elif tag in ("strong", "b"):
            self._active_marks.append({"type": "strong"})
        elif tag in ("em", "i"):
            self._active_marks.append({"type": "em"})
        elif tag == "a":
            href = attrs_dict.get("href", "")
            self._active_marks.append({
                "type": "link",
                "attrs": {"href": href, "target": "_blank",
                          "rel": "noopener noreferrer nofollow", "class": None},
            })
        elif tag == "br":
            self._append_text("\n")
        elif tag == "blockquote":
            self._push_block({"type": "blockquote"})
        elif tag == "hr":
            self._doc_content.append({"type": "horizontal_rule"})

    def handle_endtag(self, tag):
        if tag in ("p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "blockquote"):
            self._pop_block()
        elif tag == "li":
            inner = self._pop_block()   # list_item_para → paragraph
            inner["type"] = "paragraph"
            self._pop_block()           # list_item
        elif tag in ("strong", "b"):
            self._active_marks = [m for m in self._active_marks if m["type"] != "strong"]
        elif tag in ("em", "i"):
            self._active_marks = [m for m in self._active_marks if m["type"] != "em"]
        elif tag == "a":
            self._active_marks = [m for m in self._active_marks if m["type"] != "link"]

    def handle_data(self, data):
        self._append_text(data)

    def handle_entityref(self, name):
        entities = {"amp": "&", "lt": "<", "gt": ">", "quot": '"', "nbsp": " ",
                    "mdash": "—", "ndash": "–", "ldquo": "“", "rdquo": "”",
                    "lsquo": "‘", "rsquo": "’", "hellip": "…"}
        self._append_text(entities.get(name, f"&{name};"))

    def handle_charref(self, name):
        try:
            ch = chr(int(name[1:], 16)) if name.startswith("x") else chr(int(name))
            self._append_text(ch)
        except (ValueError, OverflowError):
            self._append_text(f"&#{name};")

    def get_doc(self):
        filtered = []
        for node in self._doc_content:
            if node.get("type") == "paragraph" and not node.get("content"):
                continue
            filtered.append(node)
        return {"type": "doc", "content": filtered}


# ---------------------------------------------------------------------------
# Title / subtitle / body extraction
# ---------------------------------------------------------------------------

class SubstackHTMLParser(HTMLParser):
    """Extract title, subtitle, and body HTML from pandoc output."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self.subtitle = ""
        self._in_h1 = False
        self._in_first_p = False
        self._h1_done = False
        self._first_p_done = False
        self._body_started = False
        self._body_segments = []

    def handle_starttag(self, tag, attrs):
        if tag == "h1" and not self._h1_done:
            self._in_h1 = True
            return
        if self._h1_done and not self._first_p_done and tag == "p":
            self._in_first_p = True
            return
        if self._first_p_done:
            self._body_started = True
            attr_str = ""
            if attrs:
                attr_str = " " + " ".join(
                    f'{k}="{v}"' if v is not None else k for k, v in attrs
                )
            self._body_segments.append(f"<{tag}{attr_str}>")

    def handle_endtag(self, tag):
        if self._in_h1 and tag == "h1":
            self._in_h1 = False
            self._h1_done = True
            return
        if self._in_first_p and tag == "p":
            self._in_first_p = False
            self._first_p_done = True
            return
        if self._body_started:
            self._body_segments.append(f"</{tag}>")

    def handle_data(self, data):
        if self._in_h1:
            self.title += data
        elif self._in_first_p:
            self.subtitle += data
        elif self._body_started:
            self._body_segments.append(data)

    def handle_entityref(self, name):
        ref = f"&{name};"
        if self._in_h1: self.title += ref
        elif self._in_first_p: self.subtitle += ref
        elif self._body_started: self._body_segments.append(ref)

    def handle_charref(self, name):
        ref = f"&#{name};"
        if self._in_h1: self.title += ref
        elif self._in_first_p: self.subtitle += ref
        elif self._body_started: self._body_segments.append(ref)

    def get_body_html(self):
        return "".join(self._body_segments).strip()


# ---------------------------------------------------------------------------
# Paywall teaser → ProseMirror blockquote
# ---------------------------------------------------------------------------

def build_teaser_blockquote(teasers: list) -> dict:
    """Convert teaser lines into a Substack paywall teaser blockquote node."""
    paragraphs = []

    # Header
    paragraphs.append({
        "type": "paragraph",
        "attrs": {"textAlign": None},
        "content": [{"type": "text", "marks": [{"type": "strong"}],
                     "text": "Abaixo, apenas para assinantes:"}],
    })

    # One paragraph per teaser line: "**Categoria.** Frase."
    for teaser in teasers:
        teaser = teaser.strip()
        if not teaser:
            continue
        m = re.match(r"\*\*(.+?)\*\*\s*(.*)", teaser)
        if m:
            category = m.group(1)
            rest = (" " + m.group(2)) if m.group(2) else ""
            content = [{"type": "text", "marks": [{"type": "strong"}], "text": category}]
            if rest:
                content.append({"type": "text", "text": rest})
        else:
            content = [{"type": "text", "text": teaser}]

        paragraphs.append({
            "type": "paragraph",
            "attrs": {"textAlign": None},
            "content": content,
        })

    return {"type": "blockquote", "content": paragraphs}


def inject_paywall(doc: dict, cut_after: int, teasers: list) -> dict:
    """Insert teaser blockquote + paywall node after the given paragraph index."""
    nodes = doc["content"]
    insert_at = cut_after + 1  # insert after the node at cut_after
    insert_at = max(1, min(insert_at, len(nodes)))  # clamp to valid range

    teaser_bq = build_teaser_blockquote(teasers)
    paywall_node = {"type": "paywall"}

    new_nodes = nodes[:insert_at] + [teaser_bq, paywall_node] + nodes[insert_at:]
    return {"type": "doc", "content": new_nodes}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def post_draft(html_file, sid, pub_host, paywall_meta_file=None):
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    splitter = SubstackHTMLParser()
    splitter.feed(html_content)

    title = " ".join(splitter.title.split())
    subtitle = " ".join(splitter.subtitle.split())
    body_html = splitter.get_body_html()

    if not title:
        raise ValueError("Could not extract title from HTML (no <h1> found)")

    converter = HTMLToProseMirror()
    converter.feed(body_html)
    pm_doc = converter.get_doc()

    # Inject paywall if meta file provided
    paywall_meta = None
    if paywall_meta_file and os.path.exists(paywall_meta_file):
        with open(paywall_meta_file, "r", encoding="utf-8") as f:
            paywall_meta = json.load(f)

    if paywall_meta:
        cut_after = paywall_meta.get("cut_after", 3)
        teasers = paywall_meta.get("teasers", [])
        pm_doc = inject_paywall(pm_doc, cut_after, teasers)
        print(f"  Paywall:  after node {cut_after}, {len(teasers)} teasers")

    draft_body = json.dumps(pm_doc, ensure_ascii=False)

    print(f"  Title:    {title}")
    print(f"  Subtitle: {subtitle[:80]}{'...' if len(subtitle) > 80 else ''}")
    print(f"  Nodes:    {len(pm_doc['content'])} top-level ProseMirror nodes")

    payload = {
        "draft_title": title,
        "draft_subtitle": subtitle,
        "draft_body": draft_body,
        "draft_bylines": [{"id": PUB_USER_ID}],
        "draft_section_id": None,
        "audience": "everyone",
        "draft_podcast_url": "",
        "draft_podcast_duration": None,
        "draft_video_upload_id": None,
        "type": "newsletter",
    }

    url = f"https://{pub_host}/api/v1/drafts"
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Cookie": f"substack.sid={sid}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        },
    )

    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    return result


def main():
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <html_file> <sid> <pub_host> [paywall_meta_json]",
              file=sys.stderr)
        sys.exit(1)

    html_file = sys.argv[1]
    sid = sys.argv[2]
    pub_host = sys.argv[3]
    paywall_meta_file = sys.argv[4] if len(sys.argv) > 4 else None

    try:
        result = post_draft(html_file, sid, pub_host, paywall_meta_file)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"  HTTP {e.code}: {e.reason}", file=sys.stderr)
        print(f"  Response: {body[:500]}", file=sys.stderr)
        sys.exit(1)

    draft_id = result.get("id")
    draft_url = f"https://{pub_host}/publish/post/{draft_id}"

    print(f"  Draft ID: {draft_id}")
    print(f"  URL:      {draft_url}")
    return draft_url


if __name__ == "__main__":
    main()
