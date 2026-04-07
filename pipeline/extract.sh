#!/bin/bash
#
# Step 3: Extract structured sources for Daily Journal from research + article
#
# Uses research.json for source metadata and the article for story grouping.
# No web fetching — all data comes from the research step.
#
# Usage: ./extract.sh 2026-02-24
#        ./extract.sh test
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir
RESEARCH_FILE="$DAY_DIR/research.json"
PT_FILE="$DAY_DIR/pt.md"
SOURCES_FILE="$DAY_DIR/sources.json"
EXTRACTION_PROMPT="$DIR/prompts/SOURCE_EXTRACTION.md"

init_log "$DATE"

echo ""
echo "=== Extract: $DATE ==="
echo ""

# --- Validate ---
if [[ ! -f "$RESEARCH_FILE" ]]; then
  echo "Error: $RESEARCH_FILE not found (run research.sh first)"
  exit 1
fi

if [[ ! -f "$PT_FILE" ]]; then
  echo "Error: $PT_FILE not found (run generate.sh first)"
  exit 1
fi

if [[ -f "$SOURCES_FILE" ]]; then
  ENTITY_COUNT=$(jq '.news_entities | length' "$SOURCES_FILE" 2>/dev/null || echo "?")
  echo "  ⚠ $SOURCES_FILE already exists ($ENTITY_COUNT entities)"
  echo "  Delete it first to re-extract."
  exit 0
fi

STEP_START=$(date +%s)
echo "  Research: $RESEARCH_FILE"
echo "  Article:  $PT_FILE"
echo "  Output:   $SOURCES_FILE"
echo "  Started:  $(date '+%H:%M:%S')"
echo ""

EXTRACTION_BODY="$(cat "$EXTRACTION_PROMPT")"
EXTRACTION_BODY="${EXTRACTION_BODY//\{date\}/$DATE}"
EXTRACTION_BODY="${EXTRACTION_BODY//\{day_dir\}/$DAY_DIR}"

PROMPT_FILE="$DAY_DIR/.prompt-extract.md"
printf '%s' "$EXTRACTION_BODY

---

Extract sources for $DATE.
- Research file: $DAY_DIR/research.json
- Article file: $DAY_DIR/pt.md" > "$PROMPT_FILE"

TMUX_WIN="extract-$DATE"
tmux new-window -n "$TMUX_WIN" -d "cd $ROOT_DIR && $DIR/tools/run-agent.sh $SOURCES_FILE done-extract $PI_CMD --model $PI_MODEL --no-extensions --tools read,write,edit @$PROMPT_FILE"

echo "  Watch live: tmux select-window -t $TMUX_WIN"
tmux wait-for done-extract
tmux kill-window -t "$TMUX_WIN" 2>/dev/null || true
rm -f "$PROMPT_FILE"

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$SOURCES_FILE" ]]; then
  echo ""
  echo "Error: Source extraction did not produce $SOURCES_FILE"
  exit 1
fi

echo ""
echo "  Done in ${STEP_DURATION}s"

# --- Validation ---
if command -v jq &> /dev/null; then
  ENTITY_COUNT=$(jq '.news_entities | length' "$SOURCES_FILE")
  URL_COUNT=$(jq '.url_count' "$SOURCES_FILE")
  ARTICLE_URLS=$(grep -oE 'https?://[^)]+' "$PT_FILE" | sort -u | wc -l | tr -d ' ')

  echo "  News entities:   $ENTITY_COUNT"
  echo "  URLs in JSON:    $URL_COUNT"
  echo "  URLs in article: $ARTICLE_URLS"

  if [[ "$URL_COUNT" != "$ARTICLE_URLS" ]]; then
    echo ""
    echo "  ⚠ URL count mismatch — some links may be missing from sources"
  else
    echo ""
    echo "  ✓ All URLs accounted for"
  fi

  echo ""
  echo "  --- Entity headlines ---"
  jq -r '.news_entities[] | "  • " + .headline' "$SOURCES_FILE"
fi
