#!/usr/bin/env python3
"""
Partner insertions (ads) for the day's newsletter, from the Publicidade board.

  list   --date D      Cards on the Publicidade board (GitHub Project #5) with
                       Formato "📧 Newsletter" and "Data no ar" == D, each joined
                       with its model from newsletters/ai/insertions/registry.json
                       (keyed by the card's Cliente). JSON on stdout.
  insert --date D      Put every model of the day into the live Substack draft,
                       each in its own free-only block (dynamicContent, audiences
                       non_sub + free_sub), in the slot after the Grandes. On an
                       ad day the ad takes the paywall teaser's place, so the
                       "Abaixo, apenas para assinantes:" block is removed.
                       Re-runnable: prior ad blocks are swapped, never stacked.
                       Exits non-zero, draft untouched, if any card lacks a model.

The model is the Substack post template (editor "Templates" menu), read with
`sstats template <id> --body`, so edits Gui makes there are what goes out.

Usage:
  insertions.py list   --date YYYY-MM-DD
  insertions.py insert --date YYYY-MM-DD [--dir EDITION_DIR] [--id DRAFT_ID] [--dry-run]
"""

import os
import sys
import json
import argparse
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from substack_mirror import load_creds, get_draft, put_draft, DEFAULT_BYLINE  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRY = os.path.join(REPO, "newsletters", "ai", "insertions", "registry.json")
BOARD_OWNER, BOARD_NUMBER = "daily-journal-tech", "5"
NEWSLETTER_FORMAT = "📧 Newsletter"
FREE_AUDIENCES = ["non_sub", "free_sub"]
TEASER_PREFIX = "Abaixo, apenas para assinantes"


def board_items():
    out = subprocess.run(
        ["gh", "project", "item-list", BOARD_NUMBER, "--owner", BOARD_OWNER,
         "--format", "json", "-L", "1000"],
        capture_output=True, text=True, check=True).stdout
    return json.loads(out)["items"]


def day_insertions(date):
    registry = json.load(open(REGISTRY, encoding="utf-8"))
    found = []
    for it in board_items():
        if it.get("formato") != NEWSLETTER_FORMAT or it.get("data no ar") != date:
            continue
        c = it.get("content") or {}
        cliente = it.get("cliente")
        model = registry.get(cliente) if cliente else None
        found.append({
            "number": c.get("number"),
            "title": it.get("title"),
            "url": c.get("url"),
            "cliente": cliente,
            "status": it.get("status"),
            "body": c.get("body", ""),
            "model": model if isinstance(model, dict) else None,
        })
    found.sort(key=lambda x: x["number"] or 0)
    warnings = []
    seen = {}
    for f in found:
        if not f["cliente"]:
            warnings.append(f"#{f['number']} sem Cliente no board — não dá pra achar o modelo")
        elif f["cliente"] in seen:
            warnings.append(f"#{seen[f['cliente']]} e #{f['number']}: dois cards de {f['cliente']} "
                            f"no mesmo dia — card duplicado no board?")
        else:
            seen[f["cliente"]] = f["number"]
    return found, warnings


def cmd_list(args):
    found, warnings = day_insertions(args.date)
    for w in warnings:
        print(f"WARN: {w}", file=sys.stderr)
    json.dump({"date": args.date, "count": len(found), "warnings": warnings,
               "insertions": found}, sys.stdout, ensure_ascii=False, indent=1)
    print()


def text_of(node):
    if isinstance(node, dict):
        return node.get("text", "") + "".join(text_of(c) for c in node.get("content", []))
    return ""


def walk(node):
    yield node
    for c in node.get("content", []) or []:
        if isinstance(c, dict):
            yield from walk(c)


def is_teaser(node):
    return node.get("type") == "dynamicContent" and any(
        n.get("type") == "blockquote" and text_of(n).strip().startswith(TEASER_PREFIX)
        for n in walk(node))


def is_ad(node):
    return node.get("type") == "dynamicContent" and any(
        n.get("type") == "button"
        or (n.get("type") == "image2" and (n.get("attrs") or {}).get("href"))
        for n in walk(node))


def free_only(nodes):
    return {
        "type": "dynamicContent",
        "attrs": {"audiences": list(FREE_AUDIENCES),
                  "displayName": "Audience-specific content block",
                  "subscriberTagIds": None},
        "content": [{"type": "dynamicContentMatch", "content": nodes}],
    }


def template_nodes(template_id):
    out = subprocess.run(["sstats", "template", str(template_id), "--body"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"Error: sstats template {template_id} falhou: {out.stderr.strip()[:300]}")
    doc = json.loads(out.stdout)
    nodes = doc.get("content") or []
    if not nodes:
        sys.exit(f"Error: template {template_id} está vazio")
    return nodes


def slot_index(content):
    """Right after the horizontal_rule that closes the Grandes (the first rule
    after the first heading). The paywall node, when present, follows it."""
    seen_heading = False
    for i, n in enumerate(content):
        if n.get("type") == "heading":
            seen_heading = True
        elif seen_heading and n.get("type") == "horizontal_rule":
            return i + 1
        elif seen_heading and n.get("type") == "paywall":
            return i
    return None


def cmd_insert(args):
    found, warnings = day_insertions(args.date)
    for w in warnings:
        print(f"WARN: {w}")
    if not found:
        print(f"Nenhuma inserção de newsletter no board para {args.date}.")
        return
    missing = [f for f in found if not f["model"]]
    if missing:
        sys.exit("Sem modelo no registry para: " + ", ".join(
            f"#{f['number']} ({f['cliente']})" for f in missing) + " — crie o modelo antes.")

    unique = {}
    for f in found:
        unique.setdefault(f["cliente"], f)  # one block per Cliente, first card wins
    found = list(unique.values())
    blocks = [free_only(template_nodes(f["model"]["template_id"])) for f in found]

    sid, host = load_creds()
    d = args.dir or os.path.join(REPO, "pipeline", "output", "ai", args.date)
    draft_id = args.id
    if not draft_id:
        idf = os.path.join(d, ".substack-draft-id")
        if not os.path.exists(idf):
            sys.exit(f"Error: sem --id e sem {idf}")
        draft_id = open(idf).read().strip()

    live = get_draft(host, sid, draft_id)
    if live.get("is_published"):
        sys.exit(f"Error: post {draft_id} já está publicado — não mexo.")
    doc = json.loads(live["draft_body"])
    content = doc["content"]

    removed = [i for i, n in enumerate(content) if is_teaser(n) or is_ad(n)]
    if removed:
        at = removed[0]
        content = [n for i, n in enumerate(content) if i not in removed]
    else:
        at = slot_index(content)
        if at is None:
            sys.exit("Error: não achei o fim das Grandes (horizontal_rule depois do 1º heading).")
    doc["content"] = content[:at] + blocks + content[at:]

    print(f"draft {draft_id}: removi {len(removed)} bloco(s) (teaser/inserção anterior), "
          f"inseri {len(blocks)} inserção(ões) no nó {at}: "
          + ", ".join(f"#{f['number']} {f['cliente']} (template {f['model']['template_id']})" for f in found))
    if args.dry_run:
        print("[dry-run] nada empurrado.")
        return

    payload = {
        "draft_title": live.get("draft_title"), "draft_subtitle": live.get("draft_subtitle"),
        "draft_body": json.dumps(doc, ensure_ascii=False),
        "draft_bylines": [{"id": DEFAULT_BYLINE}],
        "draft_section_id": live.get("draft_section_id"), "audience": live.get("audience", "everyone"),
        "draft_podcast_url": "", "draft_podcast_duration": None, "draft_video_upload_id": None,
        "type": live.get("type", "newsletter")}
    put_draft(host, sid, draft_id, payload)

    chk = json.loads(get_draft(host, sid, draft_id)["draft_body"])["content"]
    got = sum(1 for n in chk if is_ad(n))
    if got != len(blocks):
        sys.exit(f"!! servidor ficou com {got} bloco(s) de inserção, esperado {len(blocks)}")
    print(f"ok: {got} inserção(ões) no draft, só para não-assinantes + free")
    print(f"  editor: https://{host}/publish/post/{draft_id}")


def main():
    ap = argparse.ArgumentParser(description="Partner insertions from the Publicidade board.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("list")
    p.add_argument("--date", required=True)
    p = sub.add_parser("insert")
    p.add_argument("--date", required=True)
    p.add_argument("--dir", default=None)
    p.add_argument("--id", default=None)
    p.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    {"list": cmd_list, "insert": cmd_insert}[args.cmd](args)


if __name__ == "__main__":
    main()
