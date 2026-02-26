#!/bin/bash
#
# Step 2: Translate EN newsletter to PT-BR
#
# Usage: ./translate.sh 2026-02-24
#        ./translate.sh test
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
EN_FILE="$LOOP_DIR/$DATE.md"
PT_FILE="$LOOP_DIR/$DATE.pt.md"
TRANSLATION_PROMPT="$DIR/prompts/TRANSLATION.md"

init_log "$DATE"

echo ""
echo "=== Translate: $DATE ==="
echo ""

# --- Validate ---
if [[ ! -f "$EN_FILE" ]]; then
  echo "Error: $EN_FILE not found (run generate.sh first)"
  exit 1
fi

if [[ ! -f "$TRANSLATION_PROMPT" ]]; then
  echo "Error: $TRANSLATION_PROMPT not found"
  exit 1
fi

if [[ -f "$PT_FILE" ]]; then
  PT_WORDS=$(wc -w < "$PT_FILE" | tr -d ' ')
  echo "  ⚠ $PT_FILE already exists ($PT_WORDS words)"
  echo "  Delete it first to retranslate."
  exit 0
fi

EN_WORDS=$(wc -w < "$EN_FILE" | tr -d ' ')
EN_LINKS=$(grep -oE 'https?://[^)]+' "$EN_FILE" | sort -u | wc -l | tr -d ' ')

STEP_START=$(date +%s)
echo "  Input:   $EN_FILE ($EN_WORDS words, $EN_LINKS links)"
echo "  Output:  $PT_FILE"
echo "  Started: $(date '+%H:%M:%S')"
echo ""

claude -p "$(cat "$TRANSLATION_PROMPT")

---

Here is the article to translate:

$(cat "$EN_FILE")" \
    --output-format stream-json \
    --verbose \
    --allowedTools "Write,Read,Edit" \
    2>&1 | show_progress "translate"

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$PT_FILE" ]]; then
  echo ""
  echo "Error: Translation did not produce $PT_FILE"
  echo "Check if Claude wrote to a different path."
  exit 1
fi

PT_WORDS=$(wc -w < "$PT_FILE" | tr -d ' ')
PT_LINKS=$(grep -oE 'https?://[^)]+' "$PT_FILE" | sort -u | wc -l | tr -d ' ')
echo ""
echo "  Done in ${STEP_DURATION}s"
echo "  PT words: $PT_WORDS (EN was $EN_WORDS, ratio: $(echo "scale=2; $PT_WORDS / $EN_WORDS" | bc)x)"
echo "  PT links: $PT_LINKS unique URLs (EN had $EN_LINKS)"
if [[ "$PT_LINKS" != "$EN_LINKS" ]]; then
  echo "  ⚠ Link count changed — translation may have dropped links"
fi
