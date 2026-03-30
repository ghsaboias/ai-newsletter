#!/bin/bash
#
# Seed test fixtures from recent real pipeline output.
#
# Creates:
#   fixtures/research-mini.json     — 5 stories from latest research
#   fixtures/prev-editions/{date}/  — 2 recent pt.md files (for repetition check)
#
# Usage: ./tests/seed-fixtures.sh
#        ./tests/seed-fixtures.sh 2026-03-30   # use specific date as source
#

set -euo pipefail

TESTS_DIR="$(cd "$(dirname "$0")" && pwd)"
REAL_OUTPUT="$TESTS_DIR/../pipeline/output"
FIXTURES="$TESTS_DIR/fixtures"

# --- Find source date ---
SOURCE_DATE="${1:-}"
if [[ -z "$SOURCE_DATE" ]]; then
  SOURCE_DATE=$(ls -d "$REAL_OUTPUT"/2026-*/ 2>/dev/null | sort | tail -1 | xargs basename)
fi

if [[ ! -f "$REAL_OUTPUT/$SOURCE_DATE/research.json" ]]; then
  echo "Error: No research.json found for $SOURCE_DATE"
  echo "Available dates:"
  ls -d "$REAL_OUTPUT"/2026-*/ | xargs -I{} basename {} | tail -10
  exit 1
fi

echo "=== Seeding fixtures from $SOURCE_DATE ==="
echo ""

# --- Mini research: 5 stories from latest ---
mkdir -p "$FIXTURES"
jq '{
  date: .date,
  stories: .stories[:5],
  story_count: (.stories[:5] | length),
  source_count: ([.stories[:5][].sources | length] | add)
}' "$REAL_OUTPUT/$SOURCE_DATE/research.json" > "$FIXTURES/research-mini.json"

STORY_COUNT=$(jq '.story_count' "$FIXTURES/research-mini.json")
echo "  research-mini.json: $STORY_COUNT stories"

# --- Previous editions for repetition check ---
# Find 2 dates before the source that have pt.md
PREV_COUNT=0
CHECK_DATE="$SOURCE_DATE"

for i in 1 2 3 4 5; do
  CHECK_DATE=$(date -j -v-1d -f "%Y-%m-%d" "$CHECK_DATE" "+%Y-%m-%d" 2>/dev/null || date -d "$CHECK_DATE - 1 day" "+%Y-%m-%d")
  PREV_PT="$REAL_OUTPUT/$CHECK_DATE/pt.md"

  if [[ -f "$PREV_PT" ]]; then
    mkdir -p "$FIXTURES/prev-editions/$CHECK_DATE"
    cp "$PREV_PT" "$FIXTURES/prev-editions/$CHECK_DATE/pt.md"
    WORDS=$(wc -w < "$PREV_PT" | tr -d ' ')
    echo "  prev-editions/$CHECK_DATE/pt.md: $WORDS words"
    ((PREV_COUNT++))
    [[ $PREV_COUNT -ge 2 ]] && break
  fi
done

if [[ $PREV_COUNT -eq 0 ]]; then
  echo "  ⚠ No previous editions found for repetition check fixtures"
fi

echo ""
echo "Done. Fixtures in $FIXTURES/"
