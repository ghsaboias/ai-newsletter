#!/bin/bash
#
# Finalize: Extract → Ingest → Rewrite links → Substack
#
# Run this after reviewing and fixing pt.md.
#
# Usage: ./finalize.sh 2026-03-11              # dry-run ingest
#        ./finalize.sh 2026-03-11 --execute    # write to DB
#

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$DIR/logs"
mkdir -p "$LOG_DIR"

# --- Args ---
DATE=""
EXECUTE=false
INGEST_LIMIT=""
prev_arg=""

for arg in "$@"; do
  case "$arg" in
    --execute)    EXECUTE=true ;;
    --limit)      ;;
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$arg" ;;
    *)
      if [[ "$prev_arg" == "--limit" ]]; then
        INGEST_LIMIT="$arg"
      fi
      ;;
  esac
  prev_arg="$arg"
done

if [[ -z "$DATE" ]]; then
  DATE=$(date +%Y-%m-%d)
fi

DAY_DIR="$DIR/output/$DATE"

if [[ ! -f "$DAY_DIR/pt.md" ]]; then
  echo "  Error: $DAY_DIR/pt.md not found. Run draft.sh first."
  exit 1
fi

# --- Unified log ---
RUN_LOG="$LOG_DIR/$DATE-finalize.log"
exec > >(tee -a "$RUN_LOG") 2>&1

PIPELINE_START=$(date +%s)
echo "=== Finalize: $DATE ==="
echo "  Started: $(date '+%Y-%m-%d %H:%M:%S')"
echo "  Log:     $RUN_LOG"
if [[ "$EXECUTE" == true ]]; then
  echo "  Mode:    EXECUTE (will write to DB)"
else
  echo "  Mode:    dry-run (pass --execute to write to DB)"
fi
echo ""

step_timer() {
  local step_name="$1" step_start="$2"
  local step_end=$(date +%s)
  local duration=$((step_end - step_start))
  echo ""
  echo "  [$step_name] completed in ${duration}s"
  echo ""
}

# --- Step 1: Extract ---
S=$(date +%s)
"$DIR/extract.sh" "$DATE"
step_timer "extract" "$S"

# --- Step 2: Ingest ---
S=$(date +%s)
INGEST_ARGS=("$DATE")
[[ "$EXECUTE" == true ]] && INGEST_ARGS+=("--execute")
[[ -n "$INGEST_LIMIT" ]] && INGEST_ARGS+=("--limit" "$INGEST_LIMIT")
"$DIR/ingest.sh" "${INGEST_ARGS[@]}"
step_timer "ingest" "$S"

# --- Step 3: Rewrite links ---
S=$(date +%s)
"$DIR/rewrite-links.sh" "$DATE"
step_timer "rewrite-links" "$S"

# --- Step 4: Substack ---
S=$(date +%s)
"$DIR/substack.sh" "$DATE"
step_timer "substack" "$S"

# --- Summary ---
PIPELINE_END=$(date +%s)
TOTAL=$((PIPELINE_END - PIPELINE_START))

echo ""
echo "=== Finalize Complete ==="
echo "  Date:     $DATE"
echo "  Duration: ${TOTAL}s ($(( TOTAL / 60 ))m $(( TOTAL % 60 ))s)"
echo "  Output:   $DAY_DIR/final.md"
echo "  Substack: $DAY_DIR/substack.html"
