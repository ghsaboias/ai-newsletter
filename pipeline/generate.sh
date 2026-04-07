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
# Prompt: topic-specific (required)
if [[ ! -f "$TOPIC_PROMPTS_DIR/GENERATION.md" ]]; then
  echo "Error: $TOPIC_PROMPTS_DIR/GENERATION.md not found"
  exit 1
fi
GENERATE_PROMPT="$TOPIC_PROMPTS_DIR/GENERATION.md"

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

# Run in a visible tmux pane
RUNNER="$DIR/tools/run-agent.sh"
PROMPT_FILE="$DAY_DIR/.prompt-generate.md"
printf '%s' "$GENERATE_BODY

Write today's article for $DATE. The research file is at $DAY_DIR/research-slim.json." > "$PROMPT_FILE"

TMUX_WIN="generate-$DATE"
tmux new-window -n "$TMUX_WIN" -d "cd $ROOT_DIR && $RUNNER $PT_FILE done-generate $PI_CMD --model $PI_MODEL --no-extensions --tools read,write,edit @$PROMPT_FILE"

echo "  Watch live: tmux select-window -t $TMUX_WIN"
tmux wait-for done-generate
tmux kill-window -t "$TMUX_WIN" 2>/dev/null || true
rm -f "$PROMPT_FILE"

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
