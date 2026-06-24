#!/bin/bash
#
# Step 5: Rewrite source links in a PT-BR newsletter file with Daily Journal URLs
#
# Usage: ./rewrite-links.sh 2026-02-24
#        ./rewrite-links.sh test
#        ./rewrite-links.sh 2026-06-22 --in pt.md --out final.md   # explicit
#        ./rewrite-links.sh 2026-06-22 --in v2.md --out v2-final.md --quiet
#
# Reads:  <input>     (PT-BR newsletter, default pt.md)
#         links.json  (source URL → DJ URL mapping, from ingest.ts)
# Writes: <output>    (newsletter with DJ links, default final.md)
#
# Options:
#   --in <file>   input markdown   (default: pt.md)
#   --out <file>  output markdown  (default: final.md)
#   --quiet       suppress per-link "not found in markdown" warnings (for the
#                 v2 pass, whose links are a subset of links.json)
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir

IN_FILE="$DAY_DIR/pt.md"
OUT_FILE="$DAY_DIR/final.md"
QUIET=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --in)    IN_FILE="$2"; shift 2 ;;
    --out)   OUT_FILE="$2"; shift 2 ;;
    --quiet) QUIET=true; shift ;;
    *)       shift ;;
  esac
done

LINKS_FILE="$DAY_DIR/links.json"

echo ""
echo "=== Rewrite Links: $DATE ==="
echo ""

# --- Validate ---
if [[ ! -f "$IN_FILE" ]]; then
  echo "Error: $IN_FILE not found"
  exit 1
fi

if [[ ! -f "$LINKS_FILE" ]]; then
  echo "Error: $LINKS_FILE not found (run ingest.ts first)"
  exit 1
fi

MAPPING_COUNT=$(jq 'length' "$LINKS_FILE")
echo "  Input:    $IN_FILE"
echo "  Links:    $LINKS_FILE ($MAPPING_COUNT mappings)"
echo "  Output:   $OUT_FILE"
echo ""

# --- Rewrite ---
cp "$IN_FILE" "$OUT_FILE"

replaced=0
skipped=0

while IFS=$'\t' read -r source_url dj_url; do
  # Use | as sed delimiter since URLs don't contain it
  # Escape & in URLs (special in sed replacement)
  escaped_source=$(printf '%s' "$source_url" | sed 's/[&]/\\&/g')
  escaped_dj=$(printf '%s' "$dj_url" | sed 's/[&]/\\&/g')

  if grep -qF "$source_url" "$OUT_FILE"; then
    if [[ "$(uname)" == "Darwin" ]]; then
      sed -i '' "s|${escaped_source}|${escaped_dj}|g" "$OUT_FILE"
    else
      sed -i "s|${escaped_source}|${escaped_dj}|g" "$OUT_FILE"
    fi
    replaced=$((replaced + 1))
  else
    skipped=$((skipped + 1))
    [[ "$QUIET" == true ]] || echo "  ⚠ Not found in markdown: $source_url"
  fi
done < <(jq -r 'to_entries[] | "\(.key)\t\(.value)"' "$LINKS_FILE")

echo ""
echo "  Replaced: $replaced links"
if [[ $skipped -gt 0 ]]; then
  echo "  Skipped:  $skipped (not found in markdown)"
fi

# --- Validate: check for remaining external links ---
remaining=$(grep -oE 'https?://[^)]+' "$OUT_FILE" | grep -v 'dailyjournal.news' | sort -u | wc -l | tr -d ' ' || true)
if [[ "$remaining" -gt 0 ]]; then
  echo ""
  echo "  ⚠ $remaining external links still in final output:"
  grep -oE 'https?://[^)]+' "$OUT_FILE" | grep -v 'dailyjournal.news' | sort -u | while read -r url; do
    echo "    $url"
  done
fi

echo ""
echo "  ✓ Output: $OUT_FILE"
