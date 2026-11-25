#!/usr/bin/env python3
"""
Partner insertions (ads) for the day's newsletter, from the comercial CRM.

  list   --date D      The CRM's newsletter deliveries (deal_deliveries, format
                       'newsletter', due_date == D, not delivered), each joined
                       with its model from newsletters/ai/insertions/registry.json
                       (keyed by the deal's company name). JSON on stdout.
                       The GitHub board (Project #5) went out of use on 04/11/2026.
  insert --date D      Put every model of the day into the live Substack draft,
                       each in its own free-only block (dynamicContent, audiences
                       non_sub + free_sub), in the slot after the Grandes. On an
                       ad day the ad takes the paywall teaser's place, so the
                       "Abaixo, apenas para assinantes:" block is removed.
                       Re-runnable: prior ad blocks are swapped, never stacked.
                       Exits non-zero, draft untouched, if any delivery lacks a model.

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
COMERCIAL_PATH = os.environ.get("COMERCIAL_PATH", os.path.expanduser("~/comercial"))
CRM_URL = "https://dj-comercial.vercel.app"
FREE_AUDIENCES = ["non_sub", "free_sub"]
TEASER_PREFIX = "Abaixo, apenas para assinantes"


def crm_rows(sql):
    """SELECT against the comercial CRM (Supabase), through the CRM repo's own
    read-only runner, which loads that repo's .env.local."""
    out = subprocess.run(["bun", "run", "scripts/query.ts", sql], cwd=COMERCIAL_PATH,
                         capture_output=True, text=True)
    if out.returncode != 0 or out.stdout.startswith("HTTP"):
        sys.exit(f"Error: consulta ao CRM falhou: {(out.stdout + out.stderr).strip()[:300]}")
    return json.loads(out.stdout)


def day_insertions(date):
    """The day's newsletter deliveries in the CRM (deal_deliveries): format
    'newsletter', due_date == date, not yet delivered. The Cliente is the deal's
    company name, the key of registry.json."""
    registry = json.load(open(REGISTRY, encoding="utf-8"))
    if not (len(date) == 10 and date[4] == date[7] == "-" and date.replace("-", "").isdigit()):
        sys.exit(f"Error: data inválida: {date}")
    rows = crm_rows(
        "select x.id, x.label, x.group_label, x.status, x.note, x.position, x.github_issue,"
        " d.name deal, d.description, c.name company"
        " from deal_deliveries x join deals d on d.id = x.deal_id"
        " left join companies c on c.id = d.company_id"
        f" where x.format = 'newsletter' and x.due_date = '{date}' and x.delivered_at is null"
        " order by x.position, x.id")
    found = []
    for r in rows:
        cliente = r.get("company")
        model = registry.get(cliente) if cliente else None
        label = " ".join(v for v in (r.get("label"), r.get("group_label")) if v)
        body = "\n\n".join(v for v in (
            f"Deal: {r.get('deal')}", r.get("description") or "",
            f"Nota da entrega: {r['note']}" if r.get("note") else "") if v)
        found.append({
            "number": r["id"][:8],
            "id": r["id"],
            "title": f"{cliente} — {label}" if cliente else label,
            "url": f"{CRM_URL}/entregas/{r['id']}",
            "cliente": cliente,
            "status": r.get("status"),
            "github_issue": r.get("github_issue"),
            "body": body,
            "model": model if isinstance(model, dict) else None,
        })
    warnings = []
    seen = {}
    for f in found:
        if not f["cliente"]:
            warnings.append(f"#{f['number']} sem empresa no deal do CRM — não dá pra achar o modelo")
        elif f["cliente"] in seen:
            warnings.append(f"#{seen[f['cliente']]} e #{f['number']}: duas entregas de {f['cliente']} "
                            f"no mesmo dia — entrega duplicada no CRM?")
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
        print(f"Nenhuma inserção de newsletter no CRM para {args.date}.")
        return
    missing = [f for f in found if not f["model"]]
    if missing:
        sys.exit("Sem modelo no registry para: " + ", ".join(
            f"#{f['number']} ({f['cliente']})" for f in missing) + " — crie o modelo antes.")

    unique = {}
    for f in found:
        unique.setdefault(f["cliente"], f)  # one block per Cliente, first delivery wins
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
    ap = argparse.ArgumentParser(description="Partner insertions from the comercial CRM.")
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
