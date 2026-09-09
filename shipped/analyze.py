#!/usr/bin/env python3
"""Review-delta analysis: pipeline output (edition-final.md + paywall-teaser.md)
vs what actually SHIPPED on Substack (shipped/<date>.md + <date>.teasers.md).

Writes shipped/delta/<date>.json (per-edition structured diff) and
shipped/delta/REPORT.md (corpus aggregates + example lists to read by eye).
"""
import json, re, sys, difflib, collections
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "pipeline/output/ai"
SHIP = REPO / "shipped"
DELTA = SHIP / "delta"

LINK_RE = re.compile(r"\[([^\]]*)\]\([^\)]*\)")
WS_RE = re.compile(r"\s+")


def fold(t):
    t = (t or "").replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    t = t.replace(" ", " ").replace(" ", " ")
    return WS_RE.sub(" ", t).strip()


def plain(t):
    """No links, no emphasis."""
    t = LINK_RE.sub(r"\1", fold(t))
    t = t.replace("**", "").replace("*", "").replace("\\", "")
    return WS_RE.sub(" ", t).strip()


def marked(t):
    """Keep emphasis, drop links."""
    return WS_RE.sub(" ", LINK_RE.sub(r"\1", fold(t)).replace("\\", "")).strip()


BULLET_RE = re.compile(r"^-\s+(.*)$")
LABEL_RE = re.compile(r"^\*\*(.+?)\.?\*\*\s*(.*)$")


def parse_md(text, shipped=False):
    """Edition markdown (local or pandoc-from-Substack) -> dict."""
    doc = {"title": None, "subtitle": None, "stories": [], "leia": []}
    tier, cluster, story = "grandes", None, None
    lines = text.splitlines()
    seen_title = False
    for raw in lines:
        line = raw.rstrip()
        if not line or line.startswith("<") or line.startswith("</"):
            continue
        if line.startswith("# ") and not seen_title:
            doc["title"] = plain(line[2:]); seen_title = True; continue
        if line.startswith("# "):
            continue  # stray H1 inside embeds ("Ocorreu um erro.")
        if doc["subtitle"] is None and seen_title and not line.startswith("#") and not line.startswith("-") and not line.startswith("Por:") and not line.startswith("---"):
            doc["subtitle"] = plain(line); continue
        if line.startswith("Por:") or line.startswith("---"):
            continue
        if line.startswith("### ") and not line.startswith("####"):
            if plain(line[4:]).lower().startswith("recomenda"):
                break
            story = {"tier": tier, "cluster": None, "title": plain(line[4:]), "bullets": []}
            doc["stories"].append(story); continue
        if line.startswith("#### "):
            h = plain(line[5:])
            if h.lower().startswith("leia"):
                tier, cluster, story = "leia", None, None
            else:
                tier, cluster, story = "medias", h, None
            continue
        m = BULLET_RE.match(line)
        if m:
            body = m.group(1).strip()
            if tier == "leia":
                doc["leia"].append(plain(body)); continue
            lm = LABEL_RE.match(body)
            if lm:
                label, rest = lm.group(1), lm.group(2)
            else:
                label, rest = None, body
            b = {"label": label, "text": plain(rest), "marked": marked(rest)}
            if story is not None and cluster is None:
                story["bullets"].append(b)
            else:
                doc["stories"].append({"tier": "medias", "cluster": cluster,
                                       "title": label or plain(rest)[:60], "bullets": [b]})
            continue
        # subtitle already captured; ignore other prose (captions etc.)
    return doc


def sim(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


def key(s):
    return (s["title"] + " " + " ".join(b["text"] for b in s["bullets"]))[:700]


def match(src, dst, thr=0.45):
    pairs, used = [], set()
    for i, s in enumerate(src):
        best, br = None, 0
        for j, d in enumerate(dst):
            if j in used:
                continue
            r = max(sim(s["title"], d["title"]), sim(key(s), key(d)))
            if r > br:
                best, br = j, r
        if best is not None and br >= thr:
            pairs.append((i, best, round(br, 2))); used.add(best)
    return pairs, [i for i in range(len(src)) if i not in {p[0] for p in pairs}], [j for j in range(len(dst)) if j not in used]


TOK = re.compile(r"\w+|[^\w\s]", re.U)

MARKET_RE = re.compile(r"(ações|ação|papéis|subiram|subiu|caíram|caiu|recuaram|recuou|avançaram|avançou|dispararam|disparou|desabaram|pré-mercado|after-hours|pós-mercado|pregão|nasdaq|s&p|dow jones|bolsa|cotação|negociação|treasury|rendimento|índice|valor de mercado|fecharam|fechou em alta|fechou em queda|ADR|capitalização)", re.I)
TIMING_RE = re.compile(r"(na véspera|ontem|como noticiado|noticiad[oa] (na|no|em)|informad[oa] anteriormente|um dia (após|depois)|anunciad[oa] (na|no) (segunda|terça|quarta|quinta|sexta)|na (segunda|terça|quarta|quinta|sexta)-feira|nesta (segunda|terça|quarta|quinta|sexta)|na semana passada|no início d[ao] (semana|mês)|semanas atrás|dias atrás)", re.I)
HEDGE_RE = re.compile(r"(segundo|de acordo com|ainda que|embora|apesar|não (respondeu|comentou|divulgou|detalhou|informou)|sem (detalhar|informar|divulgar)|não está claro|não ficou claro|ressalva|pondera|alerta que|observa que)", re.I)
QUOTE_RE = re.compile(r'"[^"]{6,}"')


def classify_span(txt):
    cats = []
    if MARKET_RE.search(txt) and ("%" in txt or re.search(r"\b(ações|papéis|pregão|bolsa|pré-mercado|after-hours|treasury|rendimento|índice)\b", txt, re.I)):
        cats.append("market")
    if TIMING_RE.search(txt):
        cats.append("timing")
    if QUOTE_RE.search(txt):
        cats.append("quote")
    if txt.strip().startswith("("):
        cats.append("gloss")
    if HEDGE_RE.search(txt):
        cats.append("hedge/attribution")
    if re.search(r"\d", txt) and not cats:
        cats.append("number-bearing")
    if not cats:
        cats.append("other")
    return cats


def span_diff(a, b):
    """Token-level diff -> list of ops {op, before, after}."""
    ta, tb = TOK.findall(a), TOK.findall(b)
    ops = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        ops.append({"op": tag, "before": " ".join(ta[i1:i2]), "after": " ".join(tb[j1:j2]),
                    "nb": i2 - i1, "na": j2 - j1})
    return ops


ITAL_RE = re.compile(r"(?<!\*)\*([^*\n]{1,40}?)\*(?!\*)")
BOLD_RE = re.compile(r"\*\*([^*\n]{1,40}?)\*\*")


def emph_set(marked_text, rx):
    return set(m.group(1).strip().lower() for m in rx.finditer(marked_text))


def analyze(date):
    d = OUT / date
    loc_p, ship_p = d / "edition-final.md", SHIP / f"{date}.md"
    if not (loc_p.exists() and ship_p.exists()):
        return None
    L, S = parse_md(loc_p.read_text()), parse_md(ship_p.read_text(), shipped=True)
    rec = {"date": date, "counts": {"local": len(L["stories"]), "shipped": len(S["stories"]),
                                    "local_leia": len(L["leia"]), "shipped_leia": len(S["leia"])}}
    # --- subtitle
    ls, ss = L["subtitle"] or "", S["subtitle"] or ""
    if fold(ls) == fold(ss):
        sub_kind = "unchanged"
    elif "|" in ss:
        sub_kind = "rewritten-declarative-pipes"
    elif "?" in ss:
        sub_kind = "questions-edited" if sim(ls, ss) > 0.5 else "questions-rewritten"
    else:
        sub_kind = "rewritten-other"
    rec["subtitle"] = {"kind": sub_kind, "local": ls, "shipped": ss, "sim": round(sim(ls, ss), 2)}
    # --- stories
    pairs, cut, added = match(L["stories"], S["stories"])
    rec["cut"] = [{"tier": L["stories"][i]["tier"], "cluster": L["stories"][i]["cluster"], "title": L["stories"][i]["title"]} for i in cut]
    rec["added"] = [{"tier": S["stories"][j]["tier"], "title": S["stories"][j]["title"]} for j in added]
    rec["tier_moves"], rec["title_edits"], rec["label_edits"] = [], [], []
    rec["bullet_deleted"], rec["bullet_added"], rec["bullet_edits"] = [], [], []
    rec["cluster_renames"] = []
    n_bullets = 0
    for i, j, r in pairs:
        a, b = L["stories"][i], S["stories"][j]
        if a["tier"] != b["tier"]:
            rec["tier_moves"].append({"title": a["title"], "from": a["tier"], "to": b["tier"]})
        if a["cluster"] and b["cluster"] and a["cluster"] != b["cluster"]:
            rec["cluster_renames"].append({"from": a["cluster"], "to": b["cluster"]})
        if a["tier"] == "grandes" and fold(a["title"]) != fold(b["title"]):
            rec["title_edits"].append({"before": a["title"], "after": b["title"]})
        # bullets
        n_bullets += len(a["bullets"])
        bp, bcut, badd = match([{"title": x["label"] or "", "bullets": [x]} for x in a["bullets"]],
                               [{"title": x["label"] or "", "bullets": [x]} for x in b["bullets"]], thr=0.35)
        for bi in bcut:
            x = a["bullets"][bi]
            rec["bullet_deleted"].append({"story": a["title"], "tier": a["tier"], "label": x["label"], "text": x["text"], "cats": classify_span(x["text"])})
        for bj in badd:
            x = b["bullets"][bj]
            rec["bullet_added"].append({"story": a["title"], "tier": a["tier"], "label": x["label"], "text": x["text"]})
        for bi, bj, _ in bp:
            x, y = a["bullets"][bi], b["bullets"][bj]
            if (x["label"] or "") != (y["label"] or "") and x["label"] and y["label"]:
                rec["label_edits"].append({"story": a["title"], "before": x["label"], "after": y["label"]})
            if x["text"] != y["text"] or x["marked"] != y["marked"]:
                ops = span_diff(x["text"], y["text"]) if x["text"] != y["text"] else []
                ital_add = sorted(emph_set(y["marked"], ITAL_RE) - emph_set(x["marked"], ITAL_RE))
                ital_rm = sorted(emph_set(x["marked"], ITAL_RE) - emph_set(y["marked"], ITAL_RE))
                bold_add = sorted(emph_set(y["marked"], BOLD_RE) - emph_set(x["marked"], BOLD_RE))
                rec["bullet_edits"].append({
                    "story": a["title"], "tier": a["tier"], "label": x["label"],
                    "sim": round(sim(x["text"], y["text"]), 3),
                    "len_before": len(x["text"]), "len_after": len(y["text"]),
                    "ops": [dict(o, cats=classify_span(o["before"] or o["after"])) for o in ops],
                    "ital_add": ital_add, "ital_rm": ital_rm, "bold_add": bold_add,
                    "before": x["text"], "after": y["text"]})
    rec["bullets_total"] = n_bullets
    # leia também
    lp, lcut, ladd = match([{"title": t, "bullets": []} for t in L["leia"]], [{"title": t, "bullets": []} for t in S["leia"]], thr=0.5)
    rec["leia_cut"] = [L["leia"][i] for i in lcut]
    rec["leia_added"] = [S["leia"][j] for j in ladd]
    rec["leia_edits"] = [{"before": L["leia"][i], "after": S["leia"][j]} for i, j, _ in lp if fold(L["leia"][i]) != fold(S["leia"][j])]
    # teasers
    tl_p, ts_p = d / "paywall-teaser.md", SHIP / f"{date}.teasers.md"
    tl = [plain(x) for x in tl_p.read_text().splitlines() if x.strip()] if tl_p.exists() else []
    ts = [plain(x) for x in ts_p.read_text().splitlines() if x.strip()] if ts_p.exists() else []
    tl = [x for x in tl if not x.lower().startswith("abaixo")]
    ts = [x for x in ts if not x.lower().startswith("abaixo")]
    if tl or ts:
        tp, tcut, tadd = match([{"title": t[:40], "bullets": [{"text": t}]} for t in tl], [{"title": t[:40], "bullets": [{"text": t}]} for t in ts], thr=0.4)
        rec["teasers"] = {"local_n": len(tl), "shipped_n": len(ts),
                          "kind": "unchanged" if [fold(x) for x in tl] == [fold(x) for x in ts] else ("absent-shipped" if not ts else ("absent-local" if not tl else "edited")),
                          "cut": [tl[i] for i in tcut], "added": [ts[j] for j in tadd],
                          "edits": [{"sim": round(sim(tl[i], ts[j]), 2), "before": tl[i], "after": ts[j], "ops": span_diff(tl[i], ts[j])} for i, j, _ in tp if fold(tl[i]) != fold(ts[j])]}
    else:
        rec["teasers"] = None
    return rec


def report(recs):
    C = collections.Counter
    out = []
    n = len(recs)
    out.append(f"# Review delta — {n} editions ({recs[0]['date']} → {recs[-1]['date']})\n")
    # subtitle
    sk = C(r["subtitle"]["kind"] for r in recs)
    out.append("## Subtitle\n")
    out.append("| kind | n |\n|---|---|")
    for k, v in sk.most_common():
        out.append(f"| {k} | {v} |")
    out.append("\nBy month:")
    bym = collections.defaultdict(C)
    for r in recs:
        bym[r["date"][:7]][r["subtitle"]["kind"]] += 1
    for m in sorted(bym):
        out.append(f"- {m}: " + ", ".join(f"{k}={v}" for k, v in bym[m].most_common()))
    out.append("\nExamples (local → shipped):")
    for r in recs[-12:]:
        s = r["subtitle"]
        out.append(f"- **{r['date']}** [{s['kind']}]\n  - L: {s['local']}\n  - S: {s['shipped']}")
    # structure
    out.append("\n## Structure\n")
    tot = lambda k: sum(len(r[k]) for r in recs)
    out.append(f"- stories cut: {tot('cut')} (editions with ≥1 cut: {sum(1 for r in recs if r['cut'])})")
    out.append(f"- stories added: {tot('added')}")
    out.append(f"- tier moves: {tot('tier_moves')}")
    out.append(f"- Grande headline edits: {tot('title_edits')} / {sum(1 for r in recs for s in [r] )*3} (editions: {sum(1 for r in recs if r['title_edits'])})")
    out.append(f"- Média label edits: {tot('label_edits')}")
    out.append(f"- cluster renames: {tot('cluster_renames')}")
    out.append(f"- bullets deleted whole: {tot('bullet_deleted')} / {sum(r['bullets_total'] for r in recs)}  (editions: {sum(1 for r in recs if r['bullet_deleted'])})")
    out.append(f"- bullets added: {tot('bullet_added')}")
    out.append(f"- bullets edited in place: {tot('bullet_edits')} / {sum(r['bullets_total'] for r in recs)}")
    out.append(f"- Leia também cut: {tot('leia_cut')} / {sum(r['counts']['local_leia'] for r in recs)}; added: {tot('leia_added')}; retitled: {tot('leia_edits')}")
    out.append("\nCut stories (tier/cluster → title):")
    for r in recs:
        for c in r["cut"]:
            out.append(f"- {r['date']} [{c['tier']}/{c['cluster']}] {c['title']}")
    out.append("\nTier moves:")
    for r in recs:
        for c in r["tier_moves"]:
            out.append(f"- {r['date']} {c['from']}→{c['to']}: {c['title']}")
    out.append("\nGrande headline edits:")
    for r in recs:
        for c in r["title_edits"]:
            out.append(f"- {r['date']}\n  - B: {c['before']}\n  - A: {c['after']}")
    out.append("\nMédia label edits:")
    for r in recs:
        for c in r["label_edits"]:
            out.append(f"- {r['date']}: {c['before']} → {c['after']}")
    out.append("\nCluster renames:")
    for r in recs:
        for c in r["cluster_renames"]:
            out.append(f"- {r['date']}: {c['from']} → {c['to']}")
    # deleted bullets
    out.append("\n## Bullets deleted whole\n")
    lc = C((b["label"] or "(no label)") for r in recs for b in r["bullet_deleted"])
    out.append("Labels: " + ", ".join(f"{k}={v}" for k, v in lc.most_common(25)))
    cc = C(c for r in recs for b in r["bullet_deleted"] for c in b["cats"])
    out.append("Categories: " + ", ".join(f"{k}={v}" for k, v in cc.most_common()))
    for r in recs:
        for b in r["bullet_deleted"]:
            out.append(f"- {r['date']} [{b['tier']}] {b['story'][:50]} / **{b['label']}** {b['cats']}: {b['text'][:220]}")
    # in-place edits
    out.append("\n## In-place bullet edits\n")
    edits = [(r["date"], e) for r in recs for e in r["bullet_edits"]]
    shrink = sum(1 for _, e in edits if e["len_after"] < e["len_before"] - 5)
    grow = sum(1 for _, e in edits if e["len_after"] > e["len_before"] + 5)
    out.append(f"- {len(edits)} edits; shrink={shrink} grow={grow} same-length≈{len(edits)-shrink-grow}")
    out.append(f"- chars removed total: {sum(max(0,e['len_before']-e['len_after']) for _,e in edits)}; added: {sum(max(0,e['len_after']-e['len_before']) for _,e in edits)}")
    dc = C(c for _, e in edits for o in e["ops"] if o["op"] == "delete" for c in o["cats"])
    out.append("Deleted-span categories: " + ", ".join(f"{k}={v}" for k, v in dc.most_common()))
    out.append(f"- editions with ≥1 market-span deletion (bullet edit or whole bullet): {sum(1 for r in recs if any('market' in c for e in r['bullet_edits'] for o in e['ops'] if o['op']=='delete' for c in o['cats']) or any('market' in b['cats'] for b in r['bullet_deleted']))}")
    ital = C(w for _, e in edits for w in e["ital_add"])
    out.append("\nWords newly italicized by editor (top 40): " + ", ".join(f"{k}={v}" for k, v in ital.most_common(40)))
    itrm = C(w for _, e in edits for w in e["ital_rm"])
    out.append("Italics removed (top 20): " + ", ".join(f"{k}={v}" for k, v in itrm.most_common(20)))
    bold = C(w for _, e in edits for w in e["bold_add"])
    out.append("Bold added (top 20): " + ", ".join(f"{k}={v}" for k, v in bold.most_common(20)))
    # substitutions
    subs = C()
    for _, e in edits:
        for o in e["ops"]:
            if o["op"] == "replace" and o["nb"] <= 4 and o["na"] <= 4:
                subs[(o["before"].lower(), o["after"].lower())] += 1
    out.append("\nShort substitutions (≤4 tokens each side), top 80:")
    for (a, b), v in subs.most_common(80):
        out.append(f"- {v}× `{a}` → `{b}`")
    # deleted spans ≥ 4 tokens
    out.append("\nDeleted spans ≥5 tokens (all, newest first) — for reading:")
    for date, e in reversed(edits):
        for o in e["ops"]:
            if o["op"] in ("delete", "replace") and o["nb"] >= 5:
                out.append(f"- {date} [{e['tier']}/{e['label']}] {o['cats']} −«{o['before'][:260]}»" + (f" +«{o['after'][:160]}»" if o["after"] else ""))
    out.append("\nInserted spans ≥5 tokens:")
    for date, e in reversed(edits):
        for o in e["ops"]:
            if o["op"] in ("insert", "replace") and o["na"] >= 5:
                out.append(f"- {date} [{e['tier']}/{e['label']}] +«{o['after'][:260]}»" + (f" (was «{o['before'][:120]}»)" if o["before"] else ""))
    # leia
    out.append("\n## Leia também\n")
    for r in recs:
        for t in r["leia_cut"]:
            out.append(f"- {r['date']} CUT: {t}")
        for c in r["leia_edits"]:
            out.append(f"- {r['date']} EDIT: {c['before']} → {c['after']}")
    # teasers
    out.append("\n## Paywall teasers\n")
    tk = C(r["teasers"]["kind"] for r in recs if r["teasers"])
    out.append("| kind | n |\n|---|---|")
    for k, v in tk.most_common():
        out.append(f"| {k} | {v} |")
    out.append(f"- editions where teaser COUNT changed: {sum(1 for r in recs if r['teasers'] and r['teasers']['local_n']!=r['teasers']['shipped_n'])}")
    for r in recs:
        t = r["teasers"]
        if not t or t["kind"] in ("unchanged",):
            continue
        out.append(f"- **{r['date']}** {t['kind']} local={t['local_n']} shipped={t['shipped_n']}")
        for c in t["cut"]:
            out.append(f"  - CUT: {c[:200]}")
        for c in t["added"]:
            out.append(f"  - ADD: {c[:200]}")
        for e in t["edits"]:
            out.append(f"  - EDIT sim={e['sim']}\n    - B: {e['before'][:300]}\n    - A: {e['after'][:300]}")
    return "\n".join(out)


def main():
    DELTA.mkdir(exist_ok=True)
    dates = sys.argv[1:] or sorted(p.stem for p in SHIP.glob("2026-*.md") if p.name.count(".") == 1)
    recs = []
    for date in dates:
        r = analyze(date)
        if not r:
            continue
        (DELTA / f"{date}.json").write_text(json.dumps(r, ensure_ascii=False, indent=1))
        recs.append(r)
        print(f"{date} sub={r['subtitle']['kind']:28s} cut={len(r['cut'])} add={len(r['added'])} moves={len(r['tier_moves'])} "
              f"bdel={len(r['bullet_deleted'])} bedit={len(r['bullet_edits'])}/{r['bullets_total']} tit={len(r['title_edits'])} "
              f"leia-cut={len(r['leia_cut'])} teaser={(r['teasers'] or {}).get('kind')}")
    (DELTA / "REPORT.md").write_text(report(recs))
    print(f"\n{len(recs)} editions → {DELTA}/REPORT.md")


if __name__ == "__main__":
    main()
