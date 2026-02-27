#!/bin/bash
#
# Full newsletter pipeline: Generate → Translate → Extract → Ingest → Rewrite → Publish
#
# Usage: ./run-all.sh              # today's date
#        ./run-all.sh 2026-02-24   # specific date
#        ./run-all.sh 2026-02-24 --limit-urls 5
#        ./run-all.sh 2026-02-24 --execute
#        ./run-all.sh 2026-02-24 --limit 3 --execute
#

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$DIR/logs"
mkdir -p "$LOG_DIR"

# --- Args ---
DATE=""
EXECUTE=false
LIMIT_URLS=""
INGEST_LIMIT=""
prev_arg=""

for arg in "$@"; do
  case "$arg" in
    --execute)    EXECUTE=true ;;
    --limit-urls) ;; # value handled below
    --limit)      ;; # value handled below
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$arg" ;;
    test) DATE="test" ;;
    *)
      if [[ "$prev_arg" == "--limit-urls" ]]; then
        LIMIT_URLS="$arg"
      elif [[ "$prev_arg" == "--limit" ]]; then
        INGEST_LIMIT="$arg"
      fi
      ;;
  esac
  prev_arg="$arg"
done

# Default to today
if [[ -z "$DATE" ]]; then
  DATE=$(date +%Y-%m-%d)
fi

# --- Unified run log (tee all output to terminal + log file) ---
RUN_LOG="$LOG_DIR/$DATE-run.log"
exec > >(tee -a "$RUN_LOG") 2>&1

PIPELINE_START=$(date +%s)
echo "=== Full Newsletter Pipeline: $DATE ==="
echo "  Started: $(date '+%Y-%m-%d %H:%M:%S')"
echo "  Run log: $RUN_LOG"
echo ""

step_timer() {
  local step_name="$1" step_start="$2"
  local step_end=$(date +%s)
  local duration=$((step_end - step_start))
  echo ""
  echo "  [$step_name] completed in ${duration}s"
  echo ""
}

# --- Step 1: Generate ---
S=$(date +%s)
"$DIR/generate.sh" "$DATE"
step_timer "generate" "$S"

# --- Step 2: Translate ---
S=$(date +%s)
"$DIR/translate.sh" "$DATE"
step_timer "translate" "$S"

# --- Step 3: Extract ---
S=$(date +%s)
EXTRACT_ARGS=("$DATE")
[[ -n "$LIMIT_URLS" ]] && EXTRACT_ARGS+=("--limit-urls" "$LIMIT_URLS")
"$DIR/extract.sh" "${EXTRACT_ARGS[@]}"
step_timer "extract" "$S"

# --- Step 4: Ingest ---
S=$(date +%s)
INGEST_ARGS=("$DATE")
[[ "$EXECUTE" == true ]] && INGEST_ARGS+=("--execute")
[[ -n "$INGEST_LIMIT" ]] && INGEST_ARGS+=("--limit" "$INGEST_LIMIT")
[[ -n "$LIMIT_URLS" ]] && INGEST_ARGS+=("--test")
"$DIR/ingest.sh" "${INGEST_ARGS[@]}"
step_timer "ingest" "$S"

# --- Step 5: Rewrite links ---
S=$(date +%s)
"$DIR/rewrite-links.sh" "$DATE"
step_timer "rewrite" "$S"

# --- Step 6: Publish ---
S=$(date +%s)
"$DIR/publish.sh" "$DATE"
step_timer "publish" "$S"

# --- Summary ---
PIPELINE_END=$(date +%s)
TOTAL=$((PIPELINE_END - PIPELINE_START))
echo ""
echo "=== Pipeline Complete ==="
echo "  Date:     $DATE"
echo "  Duration: ${TOTAL}s ($(( TOTAL / 60 ))m $(( TOTAL % 60 ))s)"
echo "  Finished: $(date '+%Y-%m-%d %H:%M:%S')"
echo "  Run log:  $RUN_LOG"
