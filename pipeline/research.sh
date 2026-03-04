#!/bin/bash
#
# Step 1: Research today's news via 3 parallel cluster searches + merge
#
# Usage: ./research.sh              # today's date
#        ./research.sh 2026-02-24   # specific date
#        ./research.sh test         # use test label
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
RESEARCH_FILE="$LOOP_DIR/$DATE.research.json"
RESEARCH_PROMPT="$(cat "$DIR/prompts/RESEARCH.md")"

init_log "$DATE"

echo ""
echo "=== Research: $DATE ==="
echo ""

if [[ -f "$RESEARCH_FILE" ]]; then
  STORY_COUNT=$(jq '.story_count' "$RESEARCH_FILE" 2>/dev/null || echo "?")
  SOURCE_COUNT=$(jq '.source_count' "$RESEARCH_FILE" 2>/dev/null || echo "?")
  echo "  ⚠ $RESEARCH_FILE already exists ($STORY_COUNT stories, $SOURCE_COUNT sources)"
  echo "  Delete it first to re-research."
  exit 0
fi

STEP_START=$(date +%s)
echo "  Output:  $RESEARCH_FILE"
echo "  Started: $(date '+%H:%M:%S')"
echo ""

ALLOWED_TOOLS="Write,Read,WebFetch,WebSearch,mcp__exa__web_search_exa,Bash(bird *)"

# --- Cluster definitions ---
CLUSTER_AI="AI capabilities (models, benchmarks, reasoning), agentic economy, recursive self-improvement, scientific automation. Start by fetching Techmeme."
CLUSTER_HW="Hardware & compute (chips, data centers, energy), robotics & physical AI (humanoids, autonomous vehicles, drones), space & orbital compute."
CLUSTER_WORLD="Geopolitics & military, economics & labor (layoffs, funding, market moves), biotech & longevity."

# --- Launch parallel cluster searches ---
PIDS=()
NAMES=()

run_cluster() {
  local name="$1"
  local categories="$2"
  local outfile="$LOOP_DIR/$DATE.research-${name}.json"

  if [[ -f "$outfile" ]]; then
    echo "  [$name] already exists, skipping"
    return
  fi

  echo "  [$name] starting..."

  (
    LOG_FILE="$LOG_DIR/$DATE-research-${name}.log"
    claude -p "$RESEARCH_PROMPT
---
**Your categories:** $categories
**Date:** $DATE
**Output file:** $outfile" \
      --output-format stream-json \
      --verbose \
      --allowedTools "$ALLOWED_TOOLS" \
      2>&1 | show_progress "$name"
  ) &

  PIDS+=($!)
  NAMES+=("$name")
}

run_cluster "ai"    "$CLUSTER_AI"
run_cluster "hw"    "$CLUSTER_HW"
run_cluster "world" "$CLUSTER_WORLD"

# --- Wait for all clusters ---
FAILURES=0
for i in "${!PIDS[@]}"; do
  if ! wait "${PIDS[$i]}"; then
    echo "  ⚠ [${NAMES[$i]}] failed"
    ((FAILURES++)) || true
  fi
done

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))
echo ""
echo "  Clusters done in ${STEP_DURATION}s ($FAILURES failures)"

# --- Merge partial files ---
PARTIALS=()
for name in ai hw world; do
  f="$LOOP_DIR/$DATE.research-${name}.json"
  if [[ -f "$f" ]] && jq empty "$f" 2>/dev/null; then
    PARTIALS+=("$f")
  else
    echo "  ⚠ [$name] no valid output"
  fi
done

if [[ ${#PARTIALS[@]} -eq 0 ]]; then
  echo ""
  echo "  Error: No clusters produced valid output"
  exit 1
fi

echo "  Merging ${#PARTIALS[@]} clusters..."

jq -s '{
  date: "'"$DATE"'",
  stories: [.[].stories[]],
} | .story_count = (.stories | length)
  | .source_count = ([.stories[].sources | length] | add)' \
  "${PARTIALS[@]}" > "$RESEARCH_FILE"

# --- Validation ---
STORY_COUNT=$(jq '.story_count' "$RESEARCH_FILE")
SOURCE_COUNT=$(jq '.source_count' "$RESEARCH_FILE")

echo ""
echo "  Stories: $STORY_COUNT"
echo "  Sources: $SOURCE_COUNT"
echo "  Done in ${STEP_DURATION}s"
echo ""
echo "  --- Story headlines ---"
jq -r '.stories[] | "  • " + .headline' "$RESEARCH_FILE"
