#!/usr/bin/env python3
"""Build the ground-truth dataset: per edition, diff the pipeline draft
(edition.md) against the human-reviewed final (edition-final.md) and the
published Substack post, and join the advisory findings (fact-check.json,
repetition.json) against the edits that actually happened.

Usage:
  build_dataset.py [--dates 2026-08-13,...] [--pull] [--out evals/dataset]

--pull fetches the current (published) Substack body for each date via
substack_mirror.py (read-only) and caches it in the dataset dir.
"""
import json, re, sys, argparse, subprocess, difflib
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT_ROOT = REPO / "pipeline/output/ai"

LINK_RE = re.compile(r"\[([^\]]*)\]\([^\)]*\)")
WS_RE = re.compile(r"\s+")


def norm(text):
    """Strip links/markup so drafts and ProseMirror text compare fairly."""
    t = LINK_RE.sub(r"\1", text or "")
    t = t.replace("**", "").replace("*", "").replace(" ", " ")
    return WS_RE.sub(" ", t).strip()


def parse_edition(md_text):
    """Edition markdown -> list of stories with tier, cluster, title, bullets."""
    stories = []
    tier, cluster, story = None, None, None
    for line in md_text.splitlines():
        if line.startswith("## "):  # tier heading (Grandes / Médias / Leia também)
            h = norm(line[3:]).lower()
            if "leia" in h:
                tier = "leia"
            elif "méd" in h or "med" in h:
                tier = "medias"
            elif "grande" in h:
                tier = "grandes"
            cluster = None
            continue
        if line.startswith("### ") and not line.startswith("####"):
            story = {"tier": tier or "grandes", "cluster": None,
                     "title": norm(line[4:]), "bullets": []}
            stories.append(story)
            continue
        if line.startswith("#### "):
            h = norm(line[5:])
            if h.lower().startswith("leia"):
                tier, cluster = "leia", None
            else:
                cluster = h
                if tier == "leia":
                    tier = "medias"
            story = None
            continue
        m = re.match(r"- \*\*(.+?)\.?\*\*\s*(.*)", line)
        if m:
            label, text = m.group(1), norm(m.group(2))
            if story is not None and cluster is None:
                story["bullets"].append({"label": label, "text": text})
            else:  # Médias/Leia bullet: each bullet is its own story
                stories.append({"tier": tier or "medias", "cluster": cluster,
                                "title": label, "bullets": [{"label": label, "text": text}]})
            continue
        # leia-também plain links: "- [title](url)"
        m = re.match(r"- \[(.+?)\]\(", line)
        if m and tier == "leia":
            stories.append({"tier": "leia", "cluster": cluster,
                            "title": norm(m.group(1)), "bullets": []})
    return stories


def pm_text(node):
    if node.get("type") == "text":
        return node.get("text", "")
    if node.get("type") in ("hard_break", "hardBreak"):
        return "\n"
    text = "".join(pm_text(c) for c in node.get("content", []))
    if node.get("type") in ("paragraph", "heading", "list_item", "listItem"):
        text += "\n"
    return text


def parse_published(body):
    """Substack mirror pull ({draft_id,title,body:<pm doc>}) -> story structure.

    Published layout: H3 stories before the paywall node are Grandes, H4
    sections after it are Médias clusters, the 'Leia também' calloutBlock
    holds the leia items, and everything from the 'Recomendações' H3 on is
    out of scope. dynamicContent nodes (ads, paywall teaser) are skipped.
    """
    doc = body.get("body") or body.get("doc") or body
    stories, cluster, story = [], None, None
    tier = "grandes"
    for node in doc.get("content", []):
        t = node.get("type")
        if t == "paywall":
            tier, story, cluster = "medias", None, None
        elif t == "heading":
            level = (node.get("attrs") or {}).get("level")
            text = norm(pm_text(node))
            if text.lower().startswith("recomenda"):
                break
            if level == 3:
                story = {"tier": tier, "cluster": None, "title": text, "bullets": []}
                stories.append(story)
            elif level == 4:
                cluster, story, tier = text, None, "medias"
        elif t in ("bullet_list", "bulletList"):
            for li in node.get("content", []):
                text = norm(pm_text(li))
                m = re.match(r"(.+?)\.\s", text)
                label = m.group(1) if m and len(m.group(1)) < 60 else text[:40]
                body_text = text[len(label) + 1:].strip() if m else text
                if story is not None and cluster is None:
                    story["bullets"].append({"label": label, "text": body_text})
                else:
                    stories.append({"tier": "medias", "cluster": cluster,
                                    "title": label, "bullets": [{"label": label, "text": body_text}]})
        elif t == "calloutBlock":
            for raw in pm_text(node).split("\n"):
                text = norm(raw)
                if not text or text.lower().startswith("leia tamb"):
                    continue
                stories.append({"tier": "leia", "cluster": None, "title": text, "bullets": []})
    return stories


def sim(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


def story_key_text(s):
    return (s["title"] + " " + " ".join(b["text"] for b in s["bullets"]))[:600]


def match_stories(src, dst):
    """Greedy best-match src->dst on title+body similarity."""
    pairs, used = [], set()
    for i, s in enumerate(src):
        best, best_r = None, 0.0
        for j, d in enumerate(dst):
            if j in used:
                continue
            r = max(sim(s["title"], d["title"]), sim(story_key_text(s), story_key_text(d)) if s["bullets"] else 0)
            if r > best_r:
                best, best_r = j, r
        if best is not None and best_r >= 0.45:
            pairs.append((i, best, round(best_r, 2)))
            used.add(best)
    matched_src = {i for i, _, _ in pairs}
    return pairs, [i for i in range(len(src)) if i not in matched_src], [j for j in range(len(dst)) if j not in used]


def diff_layers(a, b, name):
    """Structured diff story-set a -> story-set b."""
    pairs, cut, added = match_stories(a, b)
    out = {"layer": name, "cut": [a[i]["title"] for i in cut],
           "added": [b[j]["title"] for j in added],
           "tier_moves": [], "title_edits": [], "bullet_edits": [],
           "bullets_total": sum(len(s["bullets"]) for s in a)}
    for i, j, r in pairs:
        sa, sb = a[i], b[j]
        if sa["tier"] != sb["tier"]:
            out["tier_moves"].append({"title": sa["title"], "from": sa["tier"], "to": sb["tier"]})
        if norm(sa["title"]) != norm(sb["title"]) and sim(sa["title"], sb["title"]) < 0.995:
            out["title_edits"].append({"before": sa["title"], "after": sb["title"]})
        bp, bcut, badd = match_stories(
            [{"title": x["label"], "bullets": [x]} for x in sa["bullets"]],
            [{"title": x["label"], "bullets": [x]} for x in sb["bullets"]])
        for bi, bj, _ in bp:
            ta, tb = sa["bullets"][bi]["text"], sb["bullets"][bj]["text"]
            if ta != tb:
                out["bullet_edits"].append({"story": sa["title"], "label": sa["bullets"][bi]["label"],
                                            "sim": round(sim(ta, tb), 3), "before": ta, "after": tb})
        for bi in bcut:
            out["bullet_edits"].append({"story": sa["title"], "label": sa["bullets"][bi]["label"],
                                        "sim": 0.0, "before": sa["bullets"][bi]["text"], "after": None})
    return out


def check_advisory(date_dir, final_text_norm):
    """Did the human act on each advisory finding? (text-presence heuristic)"""
    res = {"fact_check": [], "repetition": []}
    fc_p, rep_p = date_dir / "fact-check.json", date_dir / "repetition.json"
    if fc_p.exists():
        fc = json.loads(fc_p.read_text())
        for f in (fc.get("fidelity_issues") or []) + (fc.get("dropped_facts") or []):
            claim = norm(f.get("claim") or f.get("fact") or "")
            if not claim:
                continue
            probe = claim[:120]
            res["fact_check"].append({"severity": f.get("severity"),
                                      "claim": claim[:160],
                                      "acted_on": probe not in final_text_norm})
    if rep_p.exists():
        rep = json.loads(rep_p.read_text())
        for f in rep.get("issues") or []:
            cur, fix = norm(f.get("current_text") or ""), norm(f.get("fix") or "")
            if not cur:
                continue
            gone = cur[:120] not in final_text_norm
            fixed = bool(fix) and fix[:120] in final_text_norm
            res["repetition"].append({"type": f.get("type"), "severity": f.get("severity"),
                                      "text": cur[:120], "acted_on": gone or fixed})
    return res


def build_date(date, out_root, pull):
    d = OUT_ROOT / date
    ed_p, fin_p = d / "edition.md", d / "edition-final.md"
    if not (ed_p.exists() and fin_p.exists()):
        return None
    ds_dir = out_root / date
    ds_dir.mkdir(parents=True, exist_ok=True)

    draft = parse_edition(ed_p.read_text())
    final = parse_edition(fin_p.read_text())

    pub_p = ds_dir / "published-body.json"
    if pull and not pub_p.exists() and (d / ".substack-draft-id").exists():
        did = (d / ".substack-draft-id").read_text().strip()
        r = subprocess.run([sys.executable, str(REPO / "pipeline/tools/substack_mirror.py"),
                            "pull", "--id", did, "--dir", str(d), "--file", str(pub_p)],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print(f"  pull failed for {date}: {r.stderr.strip()[:120]}", file=sys.stderr)
    published, pub_text_norm = None, None
    if pub_p.exists():
        pub_body = json.loads(pub_p.read_text())
        published = parse_published(pub_body)
        pub_text_norm = norm(pm_text(pub_body.get("body") or pub_body.get("doc") or pub_body))

    # judge advisory findings against what actually shipped (published if we have it)
    final_text_norm = pub_text_norm or norm(fin_p.read_text())
    record = {
        "date": date,
        "counts": {"draft": len(draft), "final": len(final),
                   "published": len(published) if published is not None else None},
        "draft_vs_final": diff_layers(draft, final, "draft_vs_final"),
        "final_vs_published": diff_layers(final, published, "final_vs_published") if published is not None else None,
        "advisory": check_advisory(d, final_text_norm),
    }
    (ds_dir / "diff.json").write_text(json.dumps(record, indent=1, ensure_ascii=False))
    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dates")
    ap.add_argument("--pull", action="store_true")
    ap.add_argument("--out", default=str(REPO / "evals/dataset"))
    args = ap.parse_args()
    out_root = Path(args.out)
    dates = args.dates.split(",") if args.dates else sorted(
        p.name for p in OUT_ROOT.iterdir() if re.match(r"\d{4}-\d{2}-\d{2}$", p.name))
    rows = []
    for date in dates:
        rec = build_date(date, out_root, args.pull)
        if not rec:
            continue
        dv = rec["draft_vs_final"]
        adv = rec["advisory"]
        fc_act = sum(1 for x in adv["fact_check"] if x["acted_on"])
        rep_act = sum(1 for x in adv["repetition"] if x["acted_on"])
        rows.append(rec)
        print(f"{date}  stories {rec['counts']['draft']}->{rec['counts']['final']}"
              f"  cut={len(dv['cut'])} add={len(dv['added'])} moves={len(dv['tier_moves'])}"
              f"  bullet_edits={len(dv['bullet_edits'])}/{dv['bullets_total']}"
              f"  fc_acted={fc_act}/{len(adv['fact_check'])}"
              f"  rep_acted={rep_act}/{len(adv['repetition'])}")
    (out_root / "summary.json").write_text(json.dumps(
        [{k: r[k] for k in ("date", "counts")} for r in rows], indent=1))
    print(f"\n{len(rows)} editions -> {out_root}")


if __name__ == "__main__":
    main()
