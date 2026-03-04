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
RESEARCH_FILE="$LOOP_DIR/$DATE.research.json"
PT_FILE="$LOOP_DIR/$DATE.pt.md"
SOURCES_FILE="$LOOP_DIR/$DATE.sources.json"
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

claude -p "$(cat "$EXTRACTION_PROMPT")

---

Extract sources for $DATE.
- Research file: pipeline/output/$DATE.research.json
- Article file: pipeline/output/$DATE.pt.md" \
  --output-format stream-json \
  --verbose \
  --allowedTools "Write,Read,Edit" \
  2>&1 | show_progress "extract"

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
