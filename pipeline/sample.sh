#!/bin/bash
#
# Sample N variations from a pipeline prompt against existing data.
# Useful for calibrating prompts before committing to a full run.
#
# Usage: ./sample.sh generate 2026-03-03          # 5 samples (default)
#        ./sample.sh generate 2026-03-03 -n 10    # 10 samples
#        ./sample.sh generate 2026-03-03 -q "Only output the opening sentence of each body paragraph, numbered."
#        ./sample.sh research-ai 2026-03-03        # any prompt that has a .md in prompts/
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

# --- Parse args ---
STEP=""
DATE=""
NUM=5
QUERY="Only output the opening sentence of each body paragraph (5-8 sentences), numbered. No links, no elaboration."

while [[ $# -gt 0 ]]; do
  case "$1" in
    -n) NUM="$2"; shift 2 ;;
    -q) QUERY="$2"; shift 2 ;;
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$1"; shift ;;
    *) STEP="$1"; shift ;;
  esac
done

if [[ -z "$STEP" ]]; then
  echo "Usage: ./sample.sh <step> [YYYY-MM-DD] [-n count] [-q query]"
  echo ""
  echo "Steps (from pipeline/prompts/):"
  for f in "$DIR/prompts/"*.md; do
    basename "$f" .md | tr '[:upper:]' '[:lower:]'
  done
  exit 1
fi

DATE="${DATE:-$(date +%Y-%m-%d)}"

# Find prompt file (case-insensitive match)
PROMPT_FILE=""
for f in "$DIR/prompts/"*.md; do
  name=$(basename "$f" .md | tr '[:upper:]' '[:lower:]')
  if [[ "$name" == "$(echo "$STEP" | tr '[:upper:]' '[:lower:]')" ]]; then
    PROMPT_FILE="$f"
    break
  fi
done

if [[ -z "$PROMPT_FILE" ]]; then
  echo "Error: No prompt found for step '$STEP'"
  echo "Available: $(ls "$DIR/prompts/"*.md | xargs -I{} basename {} .md | tr '\n' ' ')"
  exit 1
fi

OUTDIR="$LOOP_DIR/samples"
mkdir -p "$OUTDIR"
TIMESTAMP=$(date +%H%M%S)

echo ""
echo "=== Sample: $STEP x$NUM ($DATE) ==="
echo ""
echo "  Prompt:  $PROMPT_FILE"
echo "  Query:   $QUERY"
echo "  Output:  $OUTDIR/$DATE-$STEP-*.txt"
echo ""

for i in $(seq 1 "$NUM"); do
  OUTFILE="$OUTDIR/$DATE-$STEP-$TIMESTAMP-$i.txt"
  echo "  [$i/$NUM] running..."

  claude -p "$(cat "$PROMPT_FILE")

Date: $DATE. Research file: pipeline/output/$DATE.research.json.

$QUERY" \
    --allowedTools "Read" \
    --output-format text \
    2>/dev/null > "$OUTFILE"

  echo "  [$i/$NUM] done → $OUTFILE"
done

echo ""
echo "=== Results ==="
echo ""

for i in $(seq 1 "$NUM"); do
  OUTFILE="$OUTDIR/$DATE-$STEP-$TIMESTAMP-$i.txt"
  echo "--- Sample $i ---"
  cat "$OUTFILE"
  echo ""
  echo ""
done
