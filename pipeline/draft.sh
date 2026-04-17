#!/bin/bash
#
# Draft: Research → Generate → Repetition check → Audit
#
# After this completes, review repetition.json and fix pt.md.
# Then run finalize.sh.
#
# Usage: ./draft.sh              # today's date
#        ./draft.sh 2026-03-11   # specific date
#

set -euo pipefail

# Prevent macOS idle sleep while pipeline runs
if [[ -z "${CAFFEINATED:-}" ]] && command -v caffeinate &>/dev/null; then
  exec env CAFFEINATED=1 caffeinate -i "$0" "$@"
fi

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

# --- Args ---
DATE=""
for arg in "$@"; do
  case "$arg" in
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$arg" ;;
  esac
done

if [[ -z "$DATE" ]]; then
  DATE=$(date +%Y-%m-%d)
fi

init_day_dir

# --- Unified log ---
RUN_LOG="$LOG_DIR/$DATE-draft.log"
exec > >(tee -a "$RUN_LOG") 2>&1

PIPELINE_START=$(date +%s)
echo "=== Draft: $DATE ==="
echo "  Started: $(date '+%Y-%m-%d %H:%M:%S')"
echo "  Log:     $RUN_LOG"
echo ""

step_timer() {
  local step_name="$1" step_start="$2"
  local step_end=$(date +%s)
  local duration=$((step_end - step_start))
  echo ""
  echo "  [$step_name] completed in ${duration}s"
  echo ""
}

# --- Step 1: Research ---
S=$(date +%s)
"$DIR/research.sh" "$DATE"
step_timer "research" "$S"

# --- Step 2: Generate ---
S=$(date +%s)
"$DIR/generate.sh" "$DATE"
step_timer "generate" "$S"

# --- Step 3: Repetition check ---
S=$(date +%s)
"$DIR/repetition-check.sh" "$DATE"
step_timer "repetition-check" "$S"

# --- Step 4: Draft rewrite (apply repetition findings surgically) ---
S=$(date +%s)
"$DIR/draft-rewrite.sh" "$DATE"
step_timer "draft-rewrite" "$S"

# --- Summary ---
PIPELINE_END=$(date +%s)
TOTAL=$((PIPELINE_END - PIPELINE_START))

echo ""
echo "=== Draft Complete ==="
echo "  Date:     $DATE"
echo "  Duration: ${TOTAL}s ($(( TOTAL / 60 ))m $(( TOTAL % 60 ))s)"
echo ""

# Show repetition summary
if [[ -f "$DAY_DIR/repetition.json" ]]; then
  REP_COUNT=$(jq '.issues | length' "$DAY_DIR/repetition.json" 2>/dev/null || echo "?")
  echo "  Repetition issues: $REP_COUNT"
fi

# Show rewrite summary
if [[ -f "$DAY_DIR/rewrite-notes.json" ]]; then
  RW_APPLIED=$(jq '[.findings[] | select(.action == "applied")] | length' "$DAY_DIR/rewrite-notes.json" 2>/dev/null || echo "?")
  RW_SKIPPED=$(jq '[.findings[] | select(.action == "skipped")] | length' "$DAY_DIR/rewrite-notes.json" 2>/dev/null || echo "?")
  RW_FLAGGED=$(jq '[.findings[] | select(.action == "flagged")] | length' "$DAY_DIR/rewrite-notes.json" 2>/dev/null || echo "?")
  echo "  Rewrites: $RW_APPLIED applied, $RW_SKIPPED skipped, $RW_FLAGGED flagged"
fi

echo ""
echo "  Review rewrite-notes.json, diff pt-original.md vs pt.md, then run finalize.sh"
