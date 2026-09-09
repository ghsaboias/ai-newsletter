#!/usr/bin/env bash
# Fetch the PUBLISHED Substack post for each edition into shipped/:
#   <date>.json        full post object via `sstats post <id> --json` (title, subtitle, body_html, stats)
#   <date>.md          title + subtitle + body_html→markdown (pandoc gfm) for diffing
#   <date>.body.json   ProseMirror doc via substack_mirror.py pull (keeps the paywall-teaser
#                      dynamicContent block, which body_html strips)
#   <date>.teasers.md  the "Abaixo, apenas para assinantes" block as shipped
# Post id = pipeline/output/ai/<date>/.substack-draft-id (draft id survives publication).
set -euo pipefail
cd "$(dirname "$0")/.."
for d in pipeline/output/ai/2026-*; do
  date=$(basename "$d")
  [ -f "$d/.substack-draft-id" ] && [ -f "$d/edition-final.md" ] || continue
  id=$(tr -d '[:space:]' < "$d/.substack-draft-id")
  out="shipped/$date.json"
  if [ ! -s "$out" ] || ! jq -e '.is_published==true' "$out" >/dev/null 2>&1; then
    sstats post "$id" --json > "$out.tmp" && mv "$out.tmp" "$out" || { echo "FAIL post $date ($id)"; rm -f "$out.tmp"; continue; }
  fi
  { printf '# %s\n\n%s\n\n' "$(jq -r .title "$out")" "$(jq -r '.subtitle // ""' "$out")";
    jq -r .body_html "$out" | pandoc -f html -t gfm --wrap=none; } > "shipped/$date.md"
  body="shipped/$date.body.json"
  if [ ! -s "$body" ]; then
    python3 pipeline/tools/substack_mirror.py pull --id "$id" --dir "$d" --file "$body" >/dev/null 2>&1 || echo "FAIL body $date ($id)"
  fi
  [ -s "$body" ] && python3 - "$body" "shipped/$date.teasers.md" <<'PY'
import json, sys
doc = json.load(open(sys.argv[1])); doc = doc.get("body") or doc
def txt(n):
    if n.get("type") == "text": return n["text"]
    if n.get("type") in ("hard_break", "hardBreak"): return "\n"
    return "".join(txt(c) for c in n.get("content", []))
out = []
for n in doc.get("content", []):
    if n.get("type") == "paywall": break
    if n.get("type") not in ("dynamicContent", "blockquote"): continue
    lines = []
    def walk(x):
        if x.get("type") == "paragraph":
            for t in txt(x).split("\n"):
                t = t.strip()
                if t: lines.append(t)
        for c in x.get("content", []): walk(c)
    walk(n)
    for i, t in enumerate(lines):
        if t.startswith("Abaixo, apenas para assinantes"):
            out = lines[i:]
open(sys.argv[2], "w").write("\n".join(out) + ("\n" if out else ""))
PY
  echo "$date $(jq -r .is_published "$out") $(jq -r .wordcount "$out")w teasers=$(grep -c . "shipped/$date.teasers.md" 2>/dev/null || echo 0)"
done
