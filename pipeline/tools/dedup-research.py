#!/usr/bin/env python3
"""Merge per-cluster research JSONs with semantic cross-cluster dedup.

Beyond exact-id dedup (which misses the same story slugged differently across
clusters, e.g. an Agility SPAC that both hw and world picked): two stories are
near-duplicates if their headlines are highly similar, OR they share their
dominant organization entity with overlapping categories. Keeps the richer
story (more sourced facts, then more sources). Reports every collapse so
cross-cluster overlap is measurable — the key signal for whether de-conflicted
cluster beats are working.

Usage:
  dedup-research.py <date> <out.json> <cluster:file> [cluster:file ...]
  e.g. dedup-research.py 2026-06-24 out.json ai:ai.json hw:hw.json world:world.json
"""
import json
import re
import sys
from difflib import SequenceMatcher

HL_RATIO = 0.55      # headline sequence-similarity threshold
HL_JACCARD_MIN = 0.35  # minimum content overlap for structural headline matches
TOK_JACCARD = 0.50   # headline token-overlap threshold
ENTITY_RATIO = 0.30  # softer headline threshold when org+category also match


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).strip()


def toks(s):
    return set(norm(s).split())


def top_org(st):
    orgs = ((st.get("entities") or {}).get("organizations")) or []
    return norm(orgs[0]) if orgs else None


def richness(st):
    return (len(st.get("key_facts", [])), len(st.get("sources", [])))


def near_dup(a, b):
    r = SequenceMatcher(None, norm(a["headline"]), norm(b["headline"])).ratio()
    ta, tb = toks(a["headline"]), toks(b["headline"])
    jac = len(ta & tb) / max(1, len(ta | tb))
    same_org = bool(top_org(a)) and top_org(a) == top_org(b)
    cat_overlap = bool(set(a.get("category", [])) & set(b.get("category", [])))
    # Entity path requires real token overlap (jaccard), NOT just SequenceMatcher
    # ratio — ratio rewards shared structure ("Anthropic launches…" vs
    # "Anthropic's Mythos…") and would wrongly merge two distinct same-company
    # stories with zero content words in common.
    if (r >= HL_RATIO and jac >= HL_JACCARD_MIN) or jac >= TOK_JACCARD or (
        same_org and cat_overlap and jac >= ENTITY_RATIO
    ):
        return True, f"hl={r:.2f} jac={jac:.2f} same_org={same_org}"
    return False, ""


def main():
    date, out = sys.argv[1], sys.argv[2]
    stories = []
    for spec in sys.argv[3:]:
        cluster, path = spec.split(":", 1)
        with open(path) as f:
            for st in json.load(f).get("stories", []):
                st["_cluster"] = cluster
                stories.append(st)

    kept, dups = [], []
    for st in stories:
        hit = None
        for k in kept:
            is_dup, reason = near_dup(st, k)
            if is_dup:
                hit = (k, reason)
                break
        if hit is None:
            kept.append(st)
            continue
        k, reason = hit
        loser, winner = (k, st) if richness(st) > richness(k) else (st, k)
        if loser is k:
            kept[kept.index(k)] = st
        dups.append((loser["_cluster"], loser["headline"], winner["_cluster"],
                     winner["headline"], reason))

    final = [dict(st) for st in kept]
    for st in final:
        st.pop("_cluster", None)
    res = {
        "date": date,
        "stories": final,
        "story_count": len(final),
        "source_count": sum(len(s.get("sources", [])) for s in final),
    }
    with open(out, "w") as f:
        json.dump(res, f, indent=2, ensure_ascii=False)

    cross = [d for d in dups if d[0] != d[2]]
    print(f"merged {len(stories)} → {len(final)} stories ({res['source_count']} sources); "
          f"{len(dups)} collapsed ({len(cross)} cross-cluster)")
    for lc, lh, wc, wh, reason in dups:
        tag = "CROSS" if lc != wc else "intra"
        print(f"  [{tag}] dropped [{lc}] {lh[:58]!r}")
        print(f"         kept    [{wc}] {wh[:58]!r}  ({reason})")


if __name__ == "__main__":
    main()
