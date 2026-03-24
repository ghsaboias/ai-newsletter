#!/bin/bash
#
# Repetition Check: Compare current newsletter against previous 3 editions
#
# Usage: ./repetition-check.sh              # today's date
#        ./repetition-check.sh 2026-03-05   # specific date
#
# Reads:  pt.md from current + up to 3 previous dates
# Writes: repetition.json
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir
PT_FILE="$DAY_DIR/pt.md"
OUTPUT_FILE="$DAY_DIR/repetition.json"

init_log "$DATE"

echo ""
echo "=== Repetition Check: $DATE ==="
echo ""

if [[ -f "$OUTPUT_FILE" ]]; then
  ISSUE_COUNT=$(jq '.issues | length' "$OUTPUT_FILE" 2>/dev/null || echo "?")
  echo "  ⚠ $OUTPUT_FILE already exists ($ISSUE_COUNT issues)"
  echo "  Delete it first to re-check."
  exit 0
fi

if [[ ! -f "$PT_FILE" ]]; then
  echo "  Error: $PT_FILE not found. Run generate first."
  exit 1
fi

# --- Find previous editions ---
PREV_FILES=()
PREV_DATES=()
CHECK_DATE="$DATE"

for i in 1 2 3; do
  CHECK_DATE=$(date -j -v-1d -f "%Y-%m-%d" "$CHECK_DATE" "+%Y-%m-%d" 2>/dev/null || date -d "$CHECK_DATE - 1 day" "+%Y-%m-%d")
  PREV_PT="$LOOP_DIR/$CHECK_DATE/pt.md"
  if [[ -f "$PREV_PT" ]]; then
    PREV_FILES+=("$PREV_PT")
    PREV_DATES+=("$CHECK_DATE")
  fi
done

if [[ ${#PREV_FILES[@]} -eq 0 ]]; then
  echo "  No previous editions found. Skipping."
  exit 0
fi

echo "  Current:  $PT_FILE"
echo "  Previous: ${PREV_DATES[*]}"
echo "  Output:   $OUTPUT_FILE"
echo ""

STEP_START=$(date +%s)

# --- Build prompt ---
PROMPT="$(cat "$DIR/prompts/REPETITION_CHECK.md")"
PROMPT="${PROMPT//\{\{DATE\}\}/$DATE}"

CONTEXT="Read the current draft from: $PT_FILE

Previous editions to compare against:"
for idx in "${!PREV_FILES[@]}"; do
  CONTEXT="$CONTEXT
- ${PREV_DATES[$idx]}: ${PREV_FILES[$idx]}"
done
CONTEXT="$CONTEXT

Write your analysis to: $OUTPUT_FILE"

LOG_FILE="$LOG_DIR/$DATE-repetition.log"

echo "  Analyzing..."

claude -p "$PROMPT
---
$CONTEXT" \
  --output-format stream-json \
  --verbose \
  --allowedTools "Read,Write" \
  2>&1 | show_progress "repetition"

# --- Verify ---
STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$OUTPUT_FILE" ]]; then
  echo ""
  echo "  Error: Claude did not produce $OUTPUT_FILE"
  exit 1
fi

if ! jq empty "$OUTPUT_FILE" 2>/dev/null; then
  echo ""
  echo "  Error: $OUTPUT_FILE is not valid JSON"
  exit 1
fi

# --- Summary ---
ISSUE_COUNT=$(jq '.issues | length' "$OUTPUT_FILE")
SUMMARY=$(jq -r '.summary // "No summary"' "$OUTPUT_FILE")

echo ""
echo "  Issues found: $ISSUE_COUNT"
echo "  Summary: $SUMMARY"

if [[ $ISSUE_COUNT -gt 0 ]]; then
  echo ""
  jq -r '.issues[] | "  • [\(.type)] \(.suggestion)"' "$OUTPUT_FILE"
fi

echo ""
echo "  Done in ${STEP_DURATION}s"
