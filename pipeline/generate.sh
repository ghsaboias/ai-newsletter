#!/bin/bash
#
# Step 1: Generate EN newsletter article
#
# Usage: ./generate.sh              # today's date
#        ./generate.sh 2026-02-24   # specific date
#        ./generate.sh test         # use test.md
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
EN_FILE="$LOOP_DIR/$DATE.md"
GENERATE_PROMPT="$DIR/prompts/INNERLOOP_UPDATE.md"

init_log "$DATE"

echo ""
echo "=== Generate: $DATE ==="
echo ""

if [[ -f "$EN_FILE" ]]; then
  EN_WORDS=$(wc -w < "$EN_FILE" | tr -d ' ')
  echo "  ⚠ $EN_FILE already exists ($EN_WORDS words)"
  echo "  Delete it first to regenerate."
  exit 0
fi

STEP_START=$(date +%s)
echo "  Output:  $EN_FILE"
echo "  Started: $(date '+%H:%M:%S')"
echo "  (research + writing — this is the longest step)"
echo ""

claude -p "$(cat "$GENERATE_PROMPT")

Generate today's article for $DATE." \
    --output-format stream-json \
    --verbose \
    --allowedTools "Write,Read,Edit,WebFetch,WebSearch,mcp__exa__web_search_exa,Bash(bird *)" \
    2>&1 | show_progress "generate" || \
  claude -p "$(cat "$GENERATE_PROMPT")

Generate today's article for $DATE." \
    --allowedTools "Write,Read,Edit,WebFetch,WebSearch,mcp__exa__web_search_exa,Bash(bird *)" \
    2>&1 | tail -5

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$EN_FILE" ]]; then
  echo ""
  echo "Error: Generation did not produce $EN_FILE"
  exit 1
fi

EN_WORDS=$(wc -w < "$EN_FILE" | tr -d ' ')
EN_LINKS=$(grep -oE 'https?://[^)]+' "$EN_FILE" | sort -u | wc -l | tr -d ' ')
echo ""
echo "  Done in ${STEP_DURATION}s"
echo "  Words: $EN_WORDS | Links: $EN_LINKS unique URLs"
