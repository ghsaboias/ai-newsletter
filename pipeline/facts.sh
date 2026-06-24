#!/bin/bash
#
# v2 step: Decompose the reviewed article into a clean fact base
#
# Reads:  pt.md
# Writes: facts.md
#
# Usage: ./facts.sh              # today's date
#        ./facts.sh 2026-06-22   # specific date
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir

PT_FILE="$DAY_DIR/pt.md"
FACTS_FILE="$DAY_DIR/facts.md"
FACTS_PROMPT="$TOPIC_PROMPTS_DIR/FACTS.md"

echo ""
echo "=== Facts: $DATE ==="
echo ""

if [[ ! -f "$FACTS_PROMPT" ]]; then
  echo "  Error: $FACTS_PROMPT not found"
  exit 1
fi
if [[ ! -f "$PT_FILE" ]]; then
  echo "  Error: $PT_FILE not found (run draft.sh through generate first)"
  exit 1
fi
if [[ -f "$FACTS_FILE" ]]; then
  echo "  ⚠ $FACTS_FILE already exists — skipping (delete to regenerate)."
  exit 0
fi

STEP_START=$(date +%s)
echo "  Input:   $PT_FILE"
echo "  Output:  $FACTS_FILE"
echo ""

BODY="$(cat "$FACTS_PROMPT")"
BODY="${BODY//\{day_dir\}/$DAY_DIR}"
BODY="${BODY//\{date\}/$DATE}"

run_claude --tools "Read,Write" "$BODY"

if [[ ! -f "$FACTS_FILE" ]]; then
  echo ""
  echo "  Error: did not produce $FACTS_FILE"
  exit 1
fi

STEP_END=$(date +%s)
echo ""
echo "  Done in $((STEP_END - STEP_START))s — $(grep -c '^- ' "$FACTS_FILE" | tr -d ' ') facts in $(grep -c '^## ' "$FACTS_FILE" | tr -d ' ') stories"
