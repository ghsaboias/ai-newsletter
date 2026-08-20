#!/usr/bin/env python3
"""Check a variant run against the hand-written expectations oracle.

    check_expectations.py <expectations.json> <run_dir> [--run A|B]

Each expectation names a source (fact-check | repetition | edition), a regex and
whether the match must be present or absent. For finding sources the regex is
matched against the concatenated text of each finding (so it hits the claim, the
overlap or the suggestion, whichever carries the phrase); `require_severity`
additionally asserts the surviving finding kept its weight.

Exit 0 only if every checked expectation passes — so it works as a test.
"""
import json, re, sys
from pathlib import Path

FINDING_KEYS = {
    "fact-check": ("fidelity_issues", "dropped_facts"),
    "repetition": ("issues",),
}


def findings(path: Path, source: str):
    """[(text, severity)] for every finding in the file, or None if unreadable."""
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return None
    out = []
    for key in FINDING_KEYS[source]:
        for item in data.get(key) or []:
            text = " ".join(str(v) for v in item.values() if isinstance(v, str))
            out.append((text, item.get("severity")))
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only = None
    if "--run" in sys.argv:
        only = sys.argv[sys.argv.index("--run") + 1]
    spec = json.loads(Path(args[0]).read_text())
    run_dir = Path(args[1])

    rows, failed, skipped = [], 0, 0
    for exp in spec["expectations"]:
        if only and exp["run"] != only:
            continue
        source = exp["source"]
        rx = re.compile(exp["match"], re.IGNORECASE)

        if source == "edition":
            path = run_dir / "edition.md"
            hits = [(path.read_text(), None)] if path.is_file() else None
            hits = [h for h in hits if rx.search(h[0])] if hits is not None else None
        else:
            items = findings(run_dir / f"{source}.json", source)
            hits = [h for h in items if rx.search(h[0])] if items is not None else None

        if hits is None:
            status, detail = "SKIP", f"sem {source} em {run_dir.name}"
            skipped += 1
        elif exp["expect"] == "present":
            need = exp.get("require_severity")
            kept = [h for h in hits if not need or h[1] in need]
            if kept:
                status, detail = "PASS", f"{len(kept)} finding(s)" + (
                    f" sev={kept[0][1]}" if kept[0][1] else "")
            elif hits:
                status = "FAIL"
                detail = f"achado mas rebaixado: sev={hits[0][1]}, esperado {need}"
            else:
                status, detail = "FAIL", "nao encontrado"
        else:  # absent
            status = "FAIL" if hits else "PASS"
            detail = f"{len(hits)} match(es) indevido(s)" if hits else "ausente"

        failed += status == "FAIL"
        rows.append((status, exp["id"], exp["source"], detail))

    width = max(len(r[1]) for r in rows) if rows else 0
    for status, eid, source, detail in rows:
        print(f"  {status:4}  {eid:<{width}}  [{source}] {detail}")
    print(f"\n{len(rows) - failed - skipped} pass / {failed} fail / {skipped} skip")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
