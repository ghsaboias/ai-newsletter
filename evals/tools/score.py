#!/usr/bin/env python3
"""Score a candidate edition.md against a date's published ground truth.

Metrics:
  selection   precision/recall of story selection vs the published edition
  tiering     tier agreement among matched stories (grandes/medias/leia)
  structure   grandes count (1-3), cluster count, bullets per grande
  lexicon     violations of the generator's hard lexicon rules (generator.md)
  prose_sim   mean text similarity of matched bullets to the published text
              (proxy for how much editing the human would still do)

Usage: score.py <edition.md> --date YYYY-MM-DD [--json out.json]
Ground truth comes from evals/dataset/<date>/published-body.json (build_dataset.py --pull).
"""
import json, re, sys, argparse, statistics
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_dataset import parse_edition, parse_published, match_stories, sim, norm

REPO = Path(__file__).resolve().parents[2]

# High-precision subset of generator.md's lexicon (line 241) + no-dashes rule.
LEXICON_RULES = [
    ("codificação", r"\bcodificaç"),
    ("ante (standalone)", r"\bante\b"),
    ("modo furtivo", r"\bmodo furtivo\b"),
    ("pilha (tech stack)", r"\bpilha (?:de tecnologia|tecnológica)\b"),
    ("fundo de hedge", r"\bfundos? de hedge\b"),
    ("salvaguardas", r"\bsalvaguardas?\b"),
    ("arcabouço", r"\barcabouço\b"),
    ("tokens de entrada/saída", r"\btokens? de (?:entrada|saída)\b"),
    ("em-dash", "—"),
    # "avaliação" in the valuation sense: same sentence as a money figure
    ("avaliação (valuation)", r"avaliaç[ãa]o[^.]*us\$|us\$[^.]*avaliaç[ãa]o"),
]


def lexicon_check(text):
    low = text.lower()
    hits = []
    for name, pat in LEXICON_RULES:
        for m in re.finditer(pat, low):
            ctx = low[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
            hits.append({"rule": name, "context": f"…{ctx}…"})
    return hits


def score(edition_path, date, dataset_root):
    pub_p = dataset_root / date / "published-body.json"
    if not pub_p.exists():
        sys.exit(f"no ground truth: {pub_p} (run build_dataset.py --pull --dates {date})")
    raw = Path(edition_path).read_text()
    cand = parse_edition(raw)
    pub = parse_published(json.loads(pub_p.read_text()))
    if not cand:
        sys.exit(f"could not parse any stories from {edition_path}")

    pairs, cand_only, pub_only = match_stories(cand, pub)
    matched = len(pairs)
    precision = matched / len(cand) if cand else 0
    recall = matched / len(pub) if pub else 0

    tier_agree = sum(1 for i, j, _ in pairs if cand[i]["tier"] == pub[j]["tier"])
    tier_diffs = [{"title": cand[i]["title"][:70], "cand": cand[i]["tier"], "pub": pub[j]["tier"]}
                  for i, j, _ in pairs if cand[i]["tier"] != pub[j]["tier"]]

    # prose similarity: matched stories' bullets vs published bullets
    bullet_sims = []
    for i, j, _ in pairs:
        bp, _, _ = match_stories(
            [{"title": b["label"], "bullets": [b]} for b in cand[i]["bullets"]],
            [{"title": b["label"], "bullets": [b]} for b in pub[j]["bullets"]])
        for bi, bj, _r in bp:
            bullet_sims.append(sim(cand[i]["bullets"][bi]["text"], pub[j]["bullets"][bj]["text"]))

    grandes = [s for s in cand if s["tier"] == "grandes"]
    n_clusters = len({s["cluster"] for s in cand if s["cluster"]})

    return {
        "edition": str(edition_path),
        "date": date,
        "selection": {
            "candidate_stories": len(cand), "published_stories": len(pub),
            "matched": matched, "precision": round(precision, 3), "recall": round(recall, 3),
            "candidate_only": [cand[i]["title"][:70] for i in cand_only],
            "published_only": [pub[j]["title"][:70] for j in pub_only],
        },
        "tiering": {
            "agreement": round(tier_agree / matched, 3) if matched else None,
            "diffs": tier_diffs,
        },
        "structure": {
            "grandes": len(grandes), "grandes_ok": 1 <= len(grandes) <= 3,
            "clusters": n_clusters,
            "bullets_per_grande": [len(s["bullets"]) for s in grandes],
        },
        "lexicon": {"violations": lexicon_check(raw)},
        "prose_sim": {
            "matched_bullets": len(bullet_sims),
            "mean": round(statistics.mean(bullet_sims), 3) if bullet_sims else None,
            "min": round(min(bullet_sims), 3) if bullet_sims else None,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("edition")
    ap.add_argument("--date", required=True)
    ap.add_argument("--dataset", default=str(REPO / "evals/dataset"))
    ap.add_argument("--json", help="also write full score JSON here")
    args = ap.parse_args()
    s = score(args.edition, args.date, Path(args.dataset))
    if args.json:
        Path(args.json).write_text(json.dumps(s, indent=1, ensure_ascii=False))
    sel, ti, st, lx, ps = s["selection"], s["tiering"], s["structure"], s["lexicon"], s["prose_sim"]
    print(f"score {args.date}  {args.edition}")
    print(f"  selection  P={sel['precision']} R={sel['recall']}  ({sel['matched']}/{sel['candidate_stories']} cand, {sel['published_stories']} pub)")
    print(f"  tiering    agreement={ti['agreement']}  diffs={len(ti['diffs'])}")
    print(f"  structure  grandes={st['grandes']} ({'ok' if st['grandes_ok'] else 'OUT OF CAP'})  clusters={st['clusters']}")
    print(f"  lexicon    {len(lx['violations'])} violations" + (": " + "; ".join(v["rule"] for v in lx["violations"][:6]) if lx["violations"] else ""))
    print(f"  prose_sim  mean={ps['mean']} min={ps['min']} over {ps['matched_bullets']} bullets")


if __name__ == "__main__":
    main()
