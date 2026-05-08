#!/bin/bash
#
# Sample N variations from a pipeline prompt against existing data.
# Useful for calibrating prompts before committing to a full run.
#
# For step=generate: emulates generate.sh exactly — same tools
# (read,write,edit), same placeholder substitution ({day_dir}, {date}),
# same trailing instruction. Each sample lands in its own subdir under
# samples/, so pt.md in the day dir is never touched.
#
# Usage: ./sample.sh generate 2026-04-16              # 5 full-article samples
#        ./sample.sh generate 2026-04-16 -n 1         # 1 sample (fast check)
#        ./sample.sh generate 2026-04-16 -q "..."     # extra instruction appended
#        ./sample.sh source_extraction 2026-04-16     # legacy stdout-capture mode
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

# --- Parse args ---
STEP=""
DATE=""
NUM=5
QUERY=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -n) NUM="$2"; shift 2 ;;
    -q) QUERY="$2"; shift 2 ;;
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$1"; shift ;;
    *) STEP="$1"; shift ;;
  esac
done

list_steps() {
  for dir in "$TOPIC_PROMPTS_DIR" "$DIR/prompts"; do
    [[ -d "$dir" ]] || continue
    for f in "$dir"/*.md; do
      [[ -f "$f" ]] || continue
      basename "$f" .md | tr '[:upper:]' '[:lower:]'
    done
  done
}

if [[ -z "$STEP" ]]; then
  echo "Usage: ./sample.sh <step> [YYYY-MM-DD] [-n count] [-q query]"
  echo ""
  echo "Steps:"
  list_steps | sed 's/^/  /'
  exit 1
fi

DATE="${DATE:-$(date +%Y-%m-%d)}"

# Find prompt file: topic-specific first, then shared
PROMPT_FILE=""
STEP_LC="$(echo "$STEP" | tr '[:upper:]' '[:lower:]')"

# Alias common step names to their prompt filenames
case "$STEP_LC" in
  generate) PROMPT_NAME="generation" ;;
  *)        PROMPT_NAME="$STEP_LC" ;;
esac

for dir in "$TOPIC_PROMPTS_DIR" "$DIR/prompts"; do
  [[ -d "$dir" ]] || continue
  for f in "$dir"/*.md; do
    [[ -f "$f" ]] || continue
    name=$(basename "$f" .md | tr '[:upper:]' '[:lower:]')
    if [[ "$name" == "$PROMPT_NAME" ]]; then
      PROMPT_FILE="$f"
      break 2
    fi
  done
done

if [[ -z "$PROMPT_FILE" ]]; then
  echo "Error: No prompt found for step '$STEP'"
  echo "Available: $(list_steps | tr '\n' ' ')"
  exit 1
fi

init_day_dir
OUTDIR="$LOOP_DIR/samples"
mkdir -p "$OUTDIR"
TIMESTAMP=$(date +%H%M%S)

echo ""
echo "=== Sample: $STEP x$NUM ($DATE) ==="
echo ""
echo "  Prompt:  $PROMPT_FILE"
[[ -n "$QUERY" ]] && echo "  Query:   $QUERY"
echo ""

# --- Mode: emulate generate.sh ---
if [[ "$STEP_LC" == "generate" ]]; then
  SLIM_FILE="$DAY_DIR/research-slim.json"
  if [[ ! -f "$SLIM_FILE" ]]; then
    echo "Error: $SLIM_FILE not found."
    echo "Run the real pipeline at least once for $DATE so research-slim.json exists:"
    echo "  pipeline/draft.sh $DATE"
    exit 1
  fi

  echo "  Output:  $OUTDIR/$DATE-generate-$TIMESTAMP-{1..$NUM}/pt.md"
  echo ""

  for i in $(seq 1 "$NUM"); do
    SAMPLE_DIR="$OUTDIR/$DATE-generate-$TIMESTAMP-$i"
    mkdir -p "$SAMPLE_DIR"
    ln -sf "$SLIM_FILE" "$SAMPLE_DIR/research-slim.json"

    BODY="$(cat "$PROMPT_FILE")"
    BODY="${BODY//\{date\}/$DATE}"
    BODY="${BODY//\{day_dir\}/$SAMPLE_DIR}"

    PROMPT_TMP="$SAMPLE_DIR/.prompt.md"
    printf '%s' "$BODY

Write today's article for $DATE. The research file is at $SAMPLE_DIR/research-slim.json." > "$PROMPT_TMP"
    if [[ -n "$QUERY" ]]; then
      printf '\n\n%s\n' "$QUERY" >> "$PROMPT_TMP"
    fi

    STEP_START=$(date +%s)
    echo "  [$i/$NUM] running → $SAMPLE_DIR/pt.md"
    $CLAUDE_CMD -p --model "$CLAUDE_MODEL" --allowedTools "Read,Write,Edit" \
      < "$PROMPT_TMP" > "$SAMPLE_DIR/.stdout.log" 2>&1 || true
    STEP_END=$(date +%s)
    rm -f "$PROMPT_TMP"

    if [[ -f "$SAMPLE_DIR/pt.md" ]]; then
      WORDS=$(wc -w < "$SAMPLE_DIR/pt.md" | tr -d ' ')
      echo "  [$i/$NUM] done  → $WORDS words in $((STEP_END - STEP_START))s"
    else
      echo "  [$i/$NUM] FAILED (no pt.md, see $SAMPLE_DIR/.stdout.log)"
    fi
  done

  echo ""
  echo "=== Samples ==="
  for i in $(seq 1 "$NUM"); do
    SAMPLE_DIR="$OUTDIR/$DATE-generate-$TIMESTAMP-$i"
    echo ""
    echo "--- Sample $i: $SAMPLE_DIR/pt.md ---"
    if [[ -f "$SAMPLE_DIR/pt.md" ]]; then
      cat "$SAMPLE_DIR/pt.md"
    else
      echo "(no output)"
    fi
  done
  exit 0
fi

# --- Legacy mode: stdout capture for other steps ---
if [[ -z "$QUERY" ]]; then
  QUERY="Only output the opening sentence of each body paragraph (5-8 sentences), numbered. No links, no elaboration."
fi

echo "  Output:  $OUTDIR/$DATE-$STEP-$TIMESTAMP-*.txt"
echo ""

for i in $(seq 1 "$NUM"); do
  OUTFILE="$OUTDIR/$DATE-$STEP-$TIMESTAMP-$i.txt"
  echo "  [$i/$NUM] running..."

  $CLAUDE_CMD -p --model "$CLAUDE_MODEL" --allowedTools "Read" \
    <<< "$(cat "$PROMPT_FILE")

Date: $DATE. Research file: $DAY_DIR/research.json.

$QUERY" \
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
