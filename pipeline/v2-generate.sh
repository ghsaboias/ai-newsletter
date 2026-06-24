#!/bin/bash
#
# v2 step: Generate the three-tier itemized edition (Grandes/Médias/Leia também)
#
# Reads:  facts.md (content/tiering), pt.md (source links)
# Writes: v2.md
#
# Usage: ./v2-generate.sh              # today's date
#        ./v2-generate.sh 2026-06-22   # specific date
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir

FACTS_FILE="$DAY_DIR/facts.md"
PT_FILE="$DAY_DIR/pt.md"
V2_FILE="$DAY_DIR/v2.md"
V2_PROMPT="$TOPIC_PROMPTS_DIR/V2_GENERATION.md"

echo ""
echo "=== v2 generate: $DATE ==="
echo ""

if [[ ! -f "$V2_PROMPT" ]]; then
  echo "  Error: $V2_PROMPT not found"
  exit 1
fi
if [[ ! -f "$FACTS_FILE" ]]; then
  echo "  Error: $FACTS_FILE not found (run facts.sh first)"
  exit 1
fi
if [[ ! -f "$PT_FILE" ]]; then
  echo "  Error: $PT_FILE not found"
  exit 1
fi
if [[ -f "$V2_FILE" ]]; then
  echo "  ⚠ $V2_FILE already exists — skipping (delete to regenerate)."
  exit 0
fi

STEP_START=$(date +%s)
echo "  Input:   $FACTS_FILE (+ $PT_FILE for links)"
echo "  Output:  $V2_FILE"
echo ""

BODY="$(cat "$V2_PROMPT")"
BODY="${BODY//\{day_dir\}/$DAY_DIR}"
BODY="${BODY//\{date\}/$DATE}"

run_claude --tools "Read,Write" "$BODY"

if [[ ! -f "$V2_FILE" ]]; then
  echo ""
  echo "  Error: did not produce $V2_FILE"
  exit 1
fi

STEP_END=$(date +%s)
GRANDES=$(grep -c '^### ' "$V2_FILE" | tr -d ' ')
CLUSTERS=$(grep -c '^#### ' "$V2_FILE" | tr -d ' ')
echo ""
echo "  Done in $((STEP_END - STEP_START))s — $GRANDES grandes, $CLUSTERS clusters (médias + leia também)"
