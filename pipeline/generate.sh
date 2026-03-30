#!/bin/bash
#
# Step 2: Generate PT-BR newsletter article from research
#
# Usage: ./generate.sh 2026-02-24   # specific date
#        ./generate.sh              # today's date
#        ./generate.sh test         # use test label
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir
RESEARCH_FILE="$DAY_DIR/research.json"
PT_FILE="$DAY_DIR/pt.md"
# Prompt: prefer topic-specific, fall back to shared
if [[ -f "$TOPIC_PROMPTS_DIR/GENERATION.md" ]]; then
  GENERATE_PROMPT="$TOPIC_PROMPTS_DIR/GENERATION.md"
else
  GENERATE_PROMPT="$DIR/prompts/GENERATION.md"
fi

init_log "$DATE"

echo ""
echo "=== Generate: $DATE ==="
echo ""

# --- Validate ---
if [[ ! -f "$RESEARCH_FILE" ]]; then
  echo "Error: $RESEARCH_FILE not found (run research.sh first)"
  exit 1
fi

if [[ -f "$PT_FILE" ]]; then
  PT_WORDS=$(wc -w < "$PT_FILE" | tr -d ' ')
  echo "  ⚠ $PT_FILE already exists ($PT_WORDS words)"
  echo "  Delete it first to regenerate."
  exit 0
fi

STORY_COUNT=$(jq '.story_count' "$RESEARCH_FILE" 2>/dev/null || echo "?")
SOURCE_COUNT=$(jq '.source_count' "$RESEARCH_FILE" 2>/dev/null || echo "?")

# --- Slim research for generation (strips excerpts, source metadata, dedupes) ---
SLIM_FILE="$DAY_DIR/research-slim.json"
python3 "$DIR/tools/slim_research.py" "$DAY_DIR"
echo ""

STEP_START=$(date +%s)
echo "  Input:   $SLIM_FILE ($STORY_COUNT stories)"
echo "  Output:  $PT_FILE"
echo "  Started: $(date '+%H:%M:%S')"
echo ""

GENERATE_BODY="$(cat "$GENERATE_PROMPT")"
GENERATE_BODY="${GENERATE_BODY//\{date\}/$DATE}"
GENERATE_BODY="${GENERATE_BODY//\{day_dir\}/$DAY_DIR}"

claude -p "$GENERATE_BODY

Write today's article for $DATE. The research file is at $DAY_DIR/research-slim.json." \
    --output-format stream-json \
    --verbose \
    --allowedTools "Write,Read,Edit" \
    2>&1 | show_progress "generate"

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$PT_FILE" ]]; then
  echo ""
  echo "Error: Generation did not produce $PT_FILE"
  exit 1
fi

PT_WORDS=$(wc -w < "$PT_FILE" | tr -d ' ')
PT_LINKS=$(grep -oE 'https?://[^)]+' "$PT_FILE" | sort -u | wc -l | tr -d ' ')
echo ""
echo "  Done in ${STEP_DURATION}s"
echo "  Words: $PT_WORDS | Links: $PT_LINKS unique URLs"
