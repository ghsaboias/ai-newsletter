#!/usr/bin/env python3
"""extract.py — deterministic half of the facts→sources.json extract step.

The extract agent used to do the whole job (join + prose) in one LLM pass.
Now the split is:

  skeleton  — parse facts.md sections + **Fontes:** blocks, join every URL
              against research.json (metadata lookup), resolve the owner
              story per section (category/entities), and write
              sources-skeleton.json with every deterministic field filled
              and the prose fields empty.
  merge     — combine sources-skeleton.json + sources-prose.json (the
              agent-written prose fields) into the final sources.json,
              validating structure, coverage and field constraints.

The agent's job shrinks to: run skeleton, read facts.md + the skeleton,
write sources-prose.json (prose only, no URLs, no metadata), run merge.

Usage:
  extract.py skeleton <YYYY-MM-DD> [--dir DAY_DIR]
  extract.py merge    <YYYY-MM-DD> [--dir DAY_DIR] [--out FILE]
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

TOPIC = "ai"
DEFAULT_ROOT = Path(__file__).resolve().parent.parent / "output"

DJ_CATEGORIES = {
    "technology", "science", "world", "economy", "finance",
    "business", "politics", "brazil", "sports", "entertainment",
}

ENTITY_PROSE_FIELDS = ("headline", "summary", "bullets", "body")
SOURCE_PROSE_FIELDS = ("title", "summary", "bullets")

FONTE_RE = re.compile(r"^-\s*(?:\[S\d+\]\s*)?(.+?)\s+—\s+(https?://\S+)\s*$")


def parse_facts(path: Path):
    """facts.md → [{title, urls: [(outlet, url), ...]}] per ## section."""
    sections = []
    cur = None
    in_fontes = False
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            cur = {"title": line[3:].strip(), "urls": []}
            sections.append(cur)
            in_fontes = False
        elif cur is not None and line.strip().startswith("**Fontes"):
            in_fontes = True
        elif in_fontes and cur is not None:
            m = FONTE_RE.match(line.strip())
            if m:
                cur["urls"].append((m.group(1), m.group(2)))
            elif line.strip() and not line.strip().startswith("-"):
                in_fontes = False
    return sections


def build_lookup(research):
    """url → (source_obj, story_obj). First hit wins on duplicates."""
    lut = {}
    for story in research.get("stories", []):
        for s in story.get("sources", []):
            lut.setdefault(s.get("url", ""), (s, story))
    return lut


def cmd_skeleton(day_dir: Path, date: str) -> int:
    facts_path = day_dir / "facts.md"
    research_path = day_dir / "research.json"
    for p in (facts_path, research_path):
        if not p.is_file():
            print(f"HALT: {p} missing", file=sys.stderr)
            return 1
    sections = parse_facts(facts_path)
    if not sections:
        print("HALT: no ## sections found in facts.md", file=sys.stderr)
        return 1
    research = json.load(open(research_path))
    lut = build_lookup(research)

    entities = []
    misses = []
    for sec in sections:
        srcs = []
        owners = {}
        seen = set()
        for outlet, url in sec["urls"]:
            if url in seen:
                continue
            seen.add(url)
            hit = lut.get(url)
            if hit is None:
                misses.append({"section": sec["title"], "url": url})
                srcs.append({
                    "url": url, "title": "", "summary": "", "bullets": [],
                    "published_at": date, "image_url": "",
                })
                continue
            src, story = hit
            key = id(story)
            owners.setdefault(key, [0, story])[0] += 1
            srcs.append({
                "url": url, "title": "", "summary": "", "bullets": [],
                "published_at": src.get("published_at") or date,
                "image_url": src.get("image_url") or "",
            })
        owner = max(owners.values(), key=lambda v: v[0])[1] if owners else None
        category = list(owner.get("category", [])) if owner else []
        bad = [c for c in category if c not in DJ_CATEGORIES]
        if bad:
            print(f"WARN: section '{sec['title']}' has non-DJ categories {bad}",
                  file=sys.stderr)
        entities.append({
            "headline": "", "summary": "", "bullets": [], "body": "",
            "category": category,
            "entities": owner.get("entities", {}) if owner else
                        {"people": [], "organizations": [], "places": []},
            "is_breaking": False,
            "sensitivity": "normal",
            "sources": srcs,
            "_section": sec["title"],
        })

    out = {
        "date": date,
        "newsletter_file": f"{date}/edition.md",
        "source_count": len(entities),
        "url_count": sum(len(e["sources"]) for e in entities),
        "news_entities": entities,
    }
    skel_path = day_dir / "sources-skeleton.json"
    skel_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    if misses:
        print(f"WARN: {len(misses)} Fontes URL(s) not found in research.json "
              f"(fallback metadata used):", file=sys.stderr)
        for m in misses:
            print(f"  - [{m['section']}] {m['url']}", file=sys.stderr)
    print(f"skeleton OK: {out['source_count']} entities, {out['url_count']} sources "
          f"-> {skel_path}")
    return 0


def _fail(errors):
    for e in errors:
        print(f"HALT: {e}", file=sys.stderr)
    return 1


def cmd_merge(day_dir: Path, date: str, out_path: Path | None) -> int:
    skel_path = day_dir / "sources-skeleton.json"
    prose_path = day_dir / "sources-prose.json"
    errors = []
    for p in (skel_path, prose_path):
        if not p.is_file():
            errors.append(f"{p} missing")
    if errors:
        return _fail(errors)
    skel = json.load(open(skel_path))
    prose = json.load(open(prose_path))

    pents = prose.get("entities")
    sents = skel["news_entities"]
    if not isinstance(pents, list) or len(pents) != len(sents):
        return _fail([f"prose has {len(pents) if isinstance(pents, list) else 'no'} "
                      f"entities, skeleton has {len(sents)} — must match 1:1 in order"])

    warnings = []
    for i, (se, pe) in enumerate(zip(sents, pents)):
        label = f"entity {i} ('{se.get('_section', '?')}')"
        for f in ENTITY_PROSE_FIELDS:
            v = pe.get(f)
            ok = isinstance(v, list) and v if f == "bullets" else \
                 isinstance(v, str) and v.strip()
            if not ok:
                errors.append(f"{label}: prose field '{f}' missing/empty")
        hl = pe.get("headline") or ""
        if len(hl) > 80:
            errors.append(f"{label}: headline {len(hl)} chars (max 80): {hl!r}")
        if len(pe.get("summary") or "") > 150:
            warnings.append(f"{label}: summary >150 chars")
        nb = len(pe.get("bullets") or [])
        if nb and not 3 <= nb <= 8:
            warnings.append(f"{label}: {nb} bullets (spec says 3-8)")
        for f in ("is_breaking", "sensitivity"):
            if f in pe:
                se[f] = pe[f]
        if se["sensitivity"] not in ("normal", "violent", "adult",
                                     "political_high_risk"):
            errors.append(f"{label}: bad sensitivity {se['sensitivity']!r}")
        for f in ENTITY_PROSE_FIELDS:
            se[f] = pe.get(f)

        psrcs = {s.get("url"): s for s in pe.get("sources", [])}
        extra = set(psrcs) - {s["url"] for s in se["sources"]}
        if extra:
            errors.append(f"{label}: prose has URLs not in skeleton: {sorted(extra)}")
        for ss in se["sources"]:
            ps = psrcs.get(ss["url"])
            if ps is None:
                errors.append(f"{label}: no prose for source {ss['url']}")
                continue
            for f in SOURCE_PROSE_FIELDS:
                v = ps.get(f)
                ok = isinstance(v, list) and v if f == "bullets" else \
                     isinstance(v, str) and v.strip()
                if not ok:
                    errors.append(f"{label}: source {ss['url']}: '{f}' missing/empty")
            for f in SOURCE_PROSE_FIELDS:
                ss[f] = ps.get(f)
        se.pop("_section", None)

    if errors:
        return _fail(errors)
    for w in warnings:
        print(f"WARN: {w}", file=sys.stderr)

    skel["source_count"] = len(sents)
    skel["url_count"] = sum(len(e["sources"]) for e in sents)
    out_path = out_path or day_dir / "sources.json"
    out_path.write_text(json.dumps(skel, ensure_ascii=False, indent=2) + "\n")
    print(f"extract — {skel['source_count']} entidades, {skel['url_count']} fontes "
          f"-> {out_path}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["skeleton", "merge"])
    ap.add_argument("date", help="YYYY-MM-DD")
    ap.add_argument("--dir", type=Path, default=None,
                    help="day dir (default pipeline/output/ai/<date>)")
    ap.add_argument("--out", type=Path, default=None,
                    help="merge only: output path (default <dir>/sources.json)")
    args = ap.parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        ap.error("date must be YYYY-MM-DD")
    day_dir = args.dir or DEFAULT_ROOT / TOPIC / args.date
    if args.command == "skeleton":
        sys.exit(cmd_skeleton(day_dir, args.date))
    sys.exit(cmd_merge(day_dir, args.date, args.out))


if __name__ == "__main__":
    main()
