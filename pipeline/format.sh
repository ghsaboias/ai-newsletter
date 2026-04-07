#!/bin/bash
#
# Format: Reformat newsletter into styled HTML for Substack
#
# Only runs if the topic has a FORMAT.md prompt (e.g. M&A).
# Reads final.md, outputs substack.html (overwrites pandoc version).
#
# Usage: ./format.sh 2026-03-30
#        PIPELINE_TOPIC=ma ./format.sh 2026-03-30
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir

FORMAT_PROMPT="$TOPIC_PROMPTS_DIR/FORMAT.md"
FINAL_FILE="$DAY_DIR/final.md"
OUTPUT_FILE="$DAY_DIR/substack-formatted.html"

init_log "$DATE"

echo ""
echo "=== Format: $DATE ==="
echo ""

# --- Skip if no format prompt for this topic ---
if [[ ! -f "$FORMAT_PROMPT" ]]; then
  echo "  No FORMAT.md for topic '$TOPIC' — skipping."
  exit 0
fi

if [[ ! -f "$FINAL_FILE" ]]; then
  echo "  Error: $FINAL_FILE not found. Run finalize.sh first."
  exit 1
fi

STEP_START=$(date +%s)
echo "  Input:   $FINAL_FILE"
echo "  Output:  $OUTPUT_FILE"
echo "  Started: $(date '+%H:%M:%S')"
echo ""

FORMAT_BODY="$(cat "$FORMAT_PROMPT")"
FORMAT_BODY="${FORMAT_BODY//\{day_dir\}/$DAY_DIR}"

run_pi --tools read,write "$FORMAT_BODY"

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$OUTPUT_FILE" ]]; then
  echo ""
  echo "  Error: did not produce $OUTPUT_FILE"
  exit 1
fi

echo ""
echo "  Done in ${STEP_DURATION}s"
echo "  Output: $OUTPUT_FILE"
