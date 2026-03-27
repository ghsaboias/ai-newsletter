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
PREV_DATE=$(date -j -v-1d -f "%Y-%m-%d" "$DATE" "+%Y-%m-%d" 2>/dev/null || date -d "$DATE - 1 day" "+%Y-%m-%d")
init_day_dir
RESEARCH_FILE="$DAY_DIR/research.json"
RESEARCH_PROMPT="$(cat "$DIR/prompts/RESEARCH.md")"
RESEARCH_PROMPT="${RESEARCH_PROMPT//\{\{DATE\}\}/$DATE}"
RESEARCH_PROMPT="${RESEARCH_PROMPT//\{\{PREV_DATE\}\}/$PREV_DATE}"

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

# --- Extract previous headlines for dedup (avoids 3 agents each reading 88K) ---
PREV_HEADLINES=""
PREV_RESEARCH="$LOOP_DIR/$PREV_DATE/research.json"
if [[ -f "$PREV_RESEARCH" ]]; then
  PREV_HEADLINES=$(jq -r '.stories[] | "- " + .id + ": " + .headline' "$PREV_RESEARCH")
  echo "  Previous: $(echo "$PREV_HEADLINES" | wc -l | tr -d ' ') headlines from $PREV_DATE"
else
  echo "  Previous: none found"
fi
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
  local outfile="$DAY_DIR/research-${name}.json"

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
**Output file:** $outfile
${PREV_HEADLINES:+
**Previous edition headlines (skip unless genuinely new development):**
$PREV_HEADLINES}" \
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

# --- Seeds (user-submitted URLs) ---
SEEDS_FILE="$DAY_DIR/seeds.md"
if [[ -f "$SEEDS_FILE" ]] && [[ -s "$SEEDS_FILE" ]]; then
  SEEDS_PROMPT="$(cat "$DIR/prompts/SEEDS.md")"
  SEEDS_URLS="$(cat "$SEEDS_FILE")"
  SEEDS_OUT="$DAY_DIR/research-seeds.json"

  if [[ -f "$SEEDS_OUT" ]]; then
    echo "  [seeds] already exists, skipping"
  else
    echo "  [seeds] $(grep -c 'http' "$SEEDS_FILE") URLs found"
    (
      LOG_FILE="$LOG_DIR/$DATE-research-seeds.log"
      claude -p "$SEEDS_PROMPT
---
**Date:** $DATE
**Output file:** $SEEDS_OUT
**URLs to research:**
$SEEDS_URLS" \
        --output-format stream-json \
        --verbose \
        --allowedTools "$ALLOWED_TOOLS" \
        2>&1 | show_progress "seeds"
    ) &
    PIDS+=($!)
    NAMES+=("seeds")
  fi
else
  echo "  [seeds] no seeds.md found, skipping"
fi

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
for name in ai hw world seeds; do
  f="$DAY_DIR/research-${name}.json"
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
