#!/bin/bash
#
# Step 10: Convert final newsletter to Substack-ready HTML
#
# Usage: ./substack.sh              # today's date
#        ./substack.sh 2026-03-05   # specific date
#
# Reads:  final.md
# Writes: substack.html
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir
FINAL_FILE="$DAY_DIR/final.md"
OUTPUT_FILE="$DAY_DIR/substack.html"

echo ""
echo "=== Substack: $DATE ==="
echo ""

if [[ ! -f "$FINAL_FILE" ]]; then
  echo "  Error: $FINAL_FILE not found. Run rewrite-links first."
  exit 1
fi

pandoc "$FINAL_FILE" --from markdown-tex_math_dollars --to html -o "$OUTPUT_FILE"

echo "  Input:  $FINAL_FILE"
echo "  Output: $OUTPUT_FILE"
echo ""
echo "  Paste into Substack's HTML editor (</>)."
