#!/bin/bash
#
# Audit: Check that stories in the newsletter are actually fresh
#
# Reads pt.md and research.json, uses WebSearch as fallback to verify
# when events actually happened.
#
# Usage: ./audit.sh              # today's date
#        ./audit.sh 2026-02-24   # specific date
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
PREV_DATE=$(date -j -v-1d -f "%Y-%m-%d" "$DATE" "+%Y-%m-%d" 2>/dev/null || date -d "$DATE - 1 day" "+%Y-%m-%d")
init_day_dir
PT_FILE="$DAY_DIR/pt.md"
RESEARCH_FILE="$DAY_DIR/research.json"
AUDIT_FILE="$DAY_DIR/audit.json"

init_log "$DATE"

echo ""
echo "=== Audit: $DATE ==="
echo ""

if [[ -f "$AUDIT_FILE" ]]; then
  ISSUE_COUNT=$(jq '.issues | length' "$AUDIT_FILE" 2>/dev/null || echo "?")
  echo "  ⚠ $AUDIT_FILE already exists ($ISSUE_COUNT issues)"
  echo "  Delete it first to re-audit."
  exit 0
fi

if [[ ! -f "$PT_FILE" ]]; then
  echo "  Error: $PT_FILE not found. Run generate first."
  exit 1
fi

if [[ ! -f "$RESEARCH_FILE" ]]; then
  echo "  Error: $RESEARCH_FILE not found. Run research first."
  exit 1
fi

echo "  Article:  $PT_FILE"
echo "  Research: $RESEARCH_FILE"
echo "  Window:   $PREV_DATE 10:00 → $DATE 10:00 BRT"

STEP_START=$(date +%s)
echo "  Output:   $AUDIT_FILE"
echo "  Started:  $(date '+%H:%M:%S')"
echo ""

AUDIT_PROMPT="$(cat "$DIR/prompts/AUDIT.md")"
AUDIT_PROMPT="${AUDIT_PROMPT//\{date\}/$DATE}"
AUDIT_PROMPT="${AUDIT_PROMPT//\{day_dir\}/$DAY_DIR}"

LOG_FILE="$LOG_DIR/$DATE-audit.log"

claude -p "$AUDIT_PROMPT" \
  --output-format stream-json \
  --verbose \
  --allowedTools "Read,Write,WebSearch" \
  2>&1 | show_progress "audit"

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$AUDIT_FILE" ]]; then
  echo ""
  echo "  Error: Claude did not produce $AUDIT_FILE"
  exit 1
fi

if ! jq empty "$AUDIT_FILE" 2>/dev/null; then
  echo ""
  echo "  Error: $AUDIT_FILE is not valid JSON"
  exit 1
fi

# Inject metadata if missing
jq --arg date "$DATE" --arg window "$PREV_DATE 10:00 → $DATE 10:00 BRT" '
  .date //= $date |
  .window //= $window
' "$AUDIT_FILE" > "$AUDIT_FILE.tmp" && mv "$AUDIT_FILE.tmp" "$AUDIT_FILE"

# --- Summary ---
ISSUE_COUNT=$(jq '.issues | length' "$AUDIT_FILE")

echo ""
echo "  Issues: $ISSUE_COUNT"

if [[ $ISSUE_COUNT -gt 0 ]]; then
  echo ""
  echo "  --- Stale events ---"
  jq -r '.issues[] | "  • \(.event)\n    actual: \(.actual_date) — \(.detail)"' "$AUDIT_FILE"
fi

echo ""
echo "  Done in ${STEP_DURATION}s"
