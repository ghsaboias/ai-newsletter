#!/bin/bash
#
# Step 5: Rewrite source links in PT-BR newsletter with Daily Journal URLs
#
# Usage: ./rewrite-links.sh 2026-02-24
#        ./rewrite-links.sh test
#
# Reads:  YYYY-MM-DD.pt.md   (PT-BR newsletter)
#         YYYY-MM-DD.links.json (source URL → DJ URL mapping, from ingest.ts)
# Writes: YYYY-MM-DD.final.md (newsletter with DJ links)
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
PT_FILE="$LOOP_DIR/$DATE.pt.md"
LINKS_FILE="$LOOP_DIR/$DATE.links.json"
FINAL_FILE="$LOOP_DIR/$DATE.final.md"

echo ""
echo "=== Rewrite Links: $DATE ==="
echo ""

# --- Validate ---
if [[ ! -f "$PT_FILE" ]]; then
  echo "Error: $PT_FILE not found (run translate.sh first)"
  exit 1
fi

if [[ ! -f "$LINKS_FILE" ]]; then
  echo "Error: $LINKS_FILE not found (run ingest.ts first)"
  exit 1
fi

MAPPING_COUNT=$(jq 'length' "$LINKS_FILE")
echo "  Input:    $PT_FILE"
echo "  Links:    $LINKS_FILE ($MAPPING_COUNT mappings)"
echo "  Output:   $FINAL_FILE"
echo ""

# --- Rewrite ---
cp "$PT_FILE" "$FINAL_FILE"

replaced=0
skipped=0

while IFS=$'\t' read -r source_url dj_url; do
  # Use | as sed delimiter since URLs don't contain it
  # Escape & in URLs (special in sed replacement)
  escaped_source=$(printf '%s' "$source_url" | sed 's/[&]/\\&/g')
  escaped_dj=$(printf '%s' "$dj_url" | sed 's/[&]/\\&/g')

  if grep -qF "$source_url" "$FINAL_FILE"; then
    if [[ "$(uname)" == "Darwin" ]]; then
      sed -i '' "s|${escaped_source}|${escaped_dj}|g" "$FINAL_FILE"
    else
      sed -i "s|${escaped_source}|${escaped_dj}|g" "$FINAL_FILE"
    fi
    replaced=$((replaced + 1))
  else
    skipped=$((skipped + 1))
    echo "  ⚠ Not found in markdown: $source_url"
  fi
done < <(jq -r 'to_entries[] | "\(.key)\t\(.value)"' "$LINKS_FILE")

echo ""
echo "  Replaced: $replaced links"
if [[ $skipped -gt 0 ]]; then
  echo "  Skipped:  $skipped (not found in markdown)"
fi

# --- Validate: check for remaining external links ---
remaining=$(grep -oE 'https?://[^)]+' "$FINAL_FILE" | grep -v 'dailyjournal.news' | sort -u | wc -l | tr -d ' ')
if [[ "$remaining" -gt 0 ]]; then
  echo ""
  echo "  ⚠ $remaining external links still in final output:"
  grep -oE 'https?://[^)]+' "$FINAL_FILE" | grep -v 'dailyjournal.news' | sort -u | while read -r url; do
    echo "    $url"
  done
fi

echo ""
echo "  ✓ Output: $FINAL_FILE"
