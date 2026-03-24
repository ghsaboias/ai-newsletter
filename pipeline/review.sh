#!/bin/bash
#
# Generate review.html for a given date
#
# Usage: ./review.sh 2026-03-08
#        ./review.sh              (defaults to today)
#
# Requires: research.json, pt.md
# Optional: audit.json, rewritten.md
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir

TEMPLATE="$DIR/review-template.html"
RESEARCH_FILE="$DAY_DIR/research.json"
PT_FILE="$DAY_DIR/pt.md"
AUDIT_FILE="$DAY_DIR/audit.json"
REWRITE_FILE="$DAY_DIR/rewritten.md"
OUTPUT_FILE="$DAY_DIR/review.html"

echo ""
echo "=== Review: $DATE ==="
echo ""

# --- Validate required files ---
if [[ ! -f "$RESEARCH_FILE" ]]; then
  echo "Error: $RESEARCH_FILE not found (run research.sh first)"
  exit 1
fi

if [[ ! -f "$PT_FILE" ]]; then
  echo "Error: $PT_FILE not found (run generate.sh first)"
  exit 1
fi

if [[ ! -f "$TEMPLATE" ]]; then
  echo "Error: $TEMPLATE not found"
  exit 1
fi

echo "  Research: $RESEARCH_FILE"
echo "  Article:  $PT_FILE"

# --- Optional files ---
AUDIT_JSON="null"
if [[ -f "$AUDIT_FILE" ]]; then
  AUDIT_JSON=$(cat "$AUDIT_FILE")
  echo "  Audit:    $AUDIT_FILE"
else
  echo "  Audit:    (none)"
fi

REWRITE_MD=""
if [[ -f "$REWRITE_FILE" ]]; then
  REWRITE_MD=$(cat "$REWRITE_FILE")
  echo "  Rewrite:  $REWRITE_FILE"
else
  echo "  Rewrite:  (none)"
fi

REVIEWED_FILE="$DAY_DIR/audit-reviewed.json"
if [[ -f "$REVIEWED_FILE" ]]; then
  echo "  Reviewed: $REVIEWED_FILE"
else
  echo "  Reviewed: (none)"
fi

echo "  Output:   $OUTPUT_FILE"
echo ""

# --- Build date nav from sibling directories that have review-eligible files ---
DATE_NAV_DATES=""
for sibling in "$LOOP_DIR"/20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]; do
  sdate=$(basename "$sibling")
  if [[ -f "$sibling/research.json" && -f "$sibling/pt.md" ]]; then
    DATE_NAV_DATES="$DATE_NAV_DATES $sdate"
  fi
done

# --- Embed data into template using python3 for safe JSON escaping ---
python3 -c "
import json, sys, os

# Read inputs
with open('$TEMPLATE', 'r') as f:
    template = f.read()

with open('$RESEARCH_FILE', 'r') as f:
    research = f.read()

with open('$PT_FILE', 'r') as f:
    article = f.read()

audit_path = '$AUDIT_FILE'
try:
    with open(audit_path, 'r') as f:
        audit = f.read().strip()
except FileNotFoundError:
    audit = 'null'

rewrite_path = '$REWRITE_FILE'
try:
    with open(rewrite_path, 'r') as f:
        rewrite = f.read()
except FileNotFoundError:
    rewrite = None

reviewed_path = '$REVIEWED_FILE'
try:
    with open(reviewed_path, 'r') as f:
        reviewed = f.read().strip()
except FileNotFoundError:
    reviewed = '[]'

# Build date nav HTML
current = '$DATE'
dates = '$DATE_NAV_DATES'.split()
nav_parts = []
for d in sorted(dates):
    # Show just MM-DD for compactness
    label = d[5:]  # e.g. '03-08'
    if d == current:
        nav_parts.append('<span class=\"current\">' + label + '</span>')
    else:
        nav_parts.append('<a href=\"../' + d + '/review.html\">' + label + '</a>')
date_nav = ' '.join(nav_parts)

# Embed as safe JS literals
html = template
html = html.replace('__DATE__', '$DATE')
html = html.replace('__DATE_NAV__', date_nav)
html = html.replace('__DATA_RESEARCH__', research.strip())
html = html.replace('__DATA_ARTICLE__', json.dumps(article))
html = html.replace('__DATA_AUDIT__', audit)
html = html.replace('__DATA_REWRITE__', json.dumps(rewrite) if rewrite else 'null')
html = html.replace('__DATA_REVIEWED__', reviewed)
html = html.replace('__REVIEWED_PATH__', reviewed_path)

with open('$OUTPUT_FILE', 'w') as f:
    f.write(html)
"

echo "  ✓ Generated $OUTPUT_FILE"
echo "  Open: file://$OUTPUT_FILE"
