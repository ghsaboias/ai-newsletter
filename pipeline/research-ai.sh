#!/bin/bash
#
# Research: AI cluster only
#
# Usage: ./research-ai.sh              # today's date
#        ./research-ai.sh 2026-03-07   # specific date
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
PREV_DATE=$(date -j -v-1d -f "%Y-%m-%d" "$DATE" "+%Y-%m-%d" 2>/dev/null || date -d "$DATE - 1 day" "+%Y-%m-%d")
init_day_dir
OUTFILE="$DAY_DIR/research-ai.json"
RESEARCH_PROMPT="$(cat "$DIR/prompts/RESEARCH.md")"
RESEARCH_PROMPT="${RESEARCH_PROMPT//\{\{DATE\}\}/$DATE}"
RESEARCH_PROMPT="${RESEARCH_PROMPT//\{\{PREV_DATE\}\}/$PREV_DATE}"

init_log "$DATE"

echo ""
echo "=== Research AI: $DATE ==="
echo ""

if [[ -f "$OUTFILE" ]]; then
  STORY_COUNT=$(jq '.stories | length' "$OUTFILE" 2>/dev/null || echo "?")
  echo "  ⚠ $OUTFILE already exists ($STORY_COUNT stories)"
  echo "  Delete it first to re-research."
  exit 0
fi

CATEGORIES="AI capabilities (models, benchmarks, reasoning), agentic economy, recursive self-improvement, scientific automation. Start by fetching Techmeme."

ALLOWED_TOOLS="Write,Read,WebFetch,WebSearch,mcp__exa__web_search_exa,Bash(bird *)"

echo "  Output:  $OUTFILE"
echo "  Started: $(date '+%H:%M:%S')"
echo ""

claude -p "$RESEARCH_PROMPT
---
**Your categories:** $CATEGORIES
**Date:** $DATE
**Output file:** $OUTFILE" \
  --output-format stream-json \
  --verbose \
  --allowedTools "$ALLOWED_TOOLS" \
  2>&1 | show_progress "ai"

# --- Validation ---
if [[ -f "$OUTFILE" ]] && jq empty "$OUTFILE" 2>/dev/null; then
  STORY_COUNT=$(jq '.stories | length' "$OUTFILE")
  SOURCE_COUNT=$(jq '[.stories[].sources | length] | add' "$OUTFILE")
  echo ""
  echo "  Stories: $STORY_COUNT"
  echo "  Sources: $SOURCE_COUNT"
  echo ""
  echo "  --- Story headlines ---"
  jq -r '.stories[] | "  • " + .headline' "$OUTFILE"
else
  echo ""
  echo "  Error: No valid output produced"
  exit 1
fi
