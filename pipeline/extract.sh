#!/bin/bash
#
# Step 3: Extract structured sources from PT-BR newsletter
#
# Usage: ./extract.sh 2026-02-24
#        ./extract.sh 2026-02-24 --limit-urls 5
#        ./extract.sh test --limit-urls 5
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=""
LIMIT_URLS=""
prev_arg=""

for arg in "$@"; do
  case "$arg" in
    --limit-urls) ;; # value handled below
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$arg" ;;
    test) DATE="test" ;;
    *)
      if [[ "$prev_arg" == "--limit-urls" ]]; then
        LIMIT_URLS="$arg"
      fi
      ;;
  esac
  prev_arg="$arg"
done

if [[ -z "$DATE" ]]; then
  echo "Usage: $0 YYYY-MM-DD [--limit-urls N]"
  exit 1
fi

PT_FILE="$LOOP_DIR/$DATE.pt.md"
EXTRACTION_PROMPT="$DIR/prompts/SOURCE_EXTRACTION.md"

if [[ -n "$LIMIT_URLS" ]]; then
  SOURCES_FILE="$LOOP_DIR/$DATE.sources.test.json"
else
  SOURCES_FILE="$LOOP_DIR/$DATE.sources.json"
fi

init_log "$DATE"

echo ""
echo "=== Extract: $DATE ==="
echo ""

# --- Validate ---
if [[ ! -f "$PT_FILE" ]]; then
  echo "Error: $PT_FILE not found (run translate.sh first)"
  exit 1
fi

if [[ ! -f "$EXTRACTION_PROMPT" ]]; then
  echo "Error: $EXTRACTION_PROMPT not found"
  exit 1
fi

STEP_START=$(date +%s)
echo "  Input:   $PT_FILE"
echo "  Output:  $SOURCES_FILE"
if [[ -n "$LIMIT_URLS" ]]; then
  echo "  Limit:   first $LIMIT_URLS URLs only (test mode)"
fi
echo "  Started: $(date '+%H:%M:%S')"
echo ""

# Build limit instruction if --limit-urls was passed
LIMIT_INSTRUCTION=""
if [[ -n "$LIMIT_URLS" ]]; then
  LIMIT_INSTRUCTION="

IMPORTANT: For this run, only process the first $LIMIT_URLS unique URLs you find in the article. Skip the rest. This is a test run to validate the output format. Save the output to output/$DATE.sources.test.json (not the regular .sources.json)."
fi

claude -p "$(cat "$EXTRACTION_PROMPT")$LIMIT_INSTRUCTION

---

Here is the translated PT-BR newsletter to extract sources from:

$(cat "$PT_FILE")" \
  --output-format stream-json \
  --verbose \
  --allowedTools "Write,Read,Edit,WebFetch,WebSearch,mcp__exa__web_search_exa" \
  2>&1 | show_progress "extract"

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$SOURCES_FILE" ]]; then
  echo ""
  echo "Error: Source extraction did not produce $SOURCES_FILE"
  echo "Check if Claude wrote to a different path."
  exit 1
fi

echo ""
echo "  Done in ${STEP_DURATION}s"

# --- Validation ---
if command -v jq &> /dev/null; then
  ENTITY_COUNT=$(jq '.news_entities | length' "$SOURCES_FILE")
  URL_COUNT=$(jq '.url_count' "$SOURCES_FILE")

  if [[ -z "$LIMIT_URLS" ]]; then
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
  else
    echo "  News entities:   $ENTITY_COUNT (test run, --limit-urls $LIMIT_URLS)"
    echo "  URLs in JSON:    $URL_COUNT"
  fi

  # Show entity headlines
  echo ""
  echo "  --- Entity headlines ---"
  jq -r '.news_entities[] | "  • " + .headline' "$SOURCES_FILE"
fi
