#!/bin/bash
#
# Step 1: Research today's news via parallel cluster searches + merge
#
# Launches each cluster as a tmux pane so you can watch progress live.
#
# Usage: ./research.sh              # today's date
#        ./research.sh 2026-02-24   # specific date
#        ./research.sh test         # use test label
#        ./research.sh --test       # output to tests/output/ instead
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
PREV_DATE=$(date -j -v-1d -f "%Y-%m-%d" "$DATE" "+%Y-%m-%d" 2>/dev/null || date -d "$DATE - 1 day" "+%Y-%m-%d")

# Previous headlines: check test output first, fall back to real output
if [[ "$*" == *"--test"* ]]; then
  LOOP_DIR="$DIR/../tests/output"
fi
init_day_dir

PREV_RESEARCH="$LOOP_DIR/$PREV_DATE/research.json"
if [[ ! -f "$PREV_RESEARCH" ]]; then
  PREV_RESEARCH="$DIR/output/$TOPIC/$PREV_DATE/research.json"
fi
RESEARCH_FILE="$DAY_DIR/research.json"

# Prompt: topic-specific (required)
if [[ ! -f "$TOPIC_PROMPTS_DIR/RESEARCH.md" ]]; then
  echo "Error: $TOPIC_PROMPTS_DIR/RESEARCH.md not found"
  exit 1
fi
RESEARCH_PROMPT="$(cat "$TOPIC_PROMPTS_DIR/RESEARCH.md")"
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

# --- Extract previous headlines for dedup ---
PREV_HEADLINES=""
if [[ -f "$PREV_RESEARCH" ]]; then
  PREV_HEADLINES=$(jq -r '.stories[] | "- " + .id + ": " + .headline' "$PREV_RESEARCH")
  echo "  Previous: $(echo "$PREV_HEADLINES" | wc -l | tr -d ' ') headlines from $PREV_DATE"
else
  echo "  Previous: none found"
fi
echo ""

# --- Pre-research scan (topic-specific, e.g. Techmeme for AI) ---
PRE_RESEARCH=""
if [[ -n "${TOPIC_PRE_RESEARCH_CMD:-}" ]]; then
  echo "  Fetching pre-research..."
  PRE_RESEARCH=$(eval "$TOPIC_PRE_RESEARCH_CMD")
  PR_COUNT=$(echo "$PRE_RESEARCH" | head -1 | grep -oE '[0-9]+' || echo "0")
  echo "  Pre-research: $PR_COUNT stories"
else
  echo "  Pre-research: none configured"
fi
echo ""

# --- Cluster definitions (from topic config) ---
for _cluster_name in ${TOPIC_CLUSTERS:-ai hw world}; do
  _upper=$(echo "$_cluster_name" | tr '[:lower:]' '[:upper:]')
  eval "CLUSTER_${_upper}=\${TOPIC_CLUSTER_${_upper}:-}"
done

# --- Tmux window name ---
TMUX_WIN="research-$DATE"

# --- Launch parallel cluster searches ---
NAMES=()

run_cluster() {
  local name="$1"
  local categories="$2"
  local outfile="$DAY_DIR/research-${name}.json"

  if [[ -f "$outfile" ]]; then
    echo "  [$name] already exists, skipping"
    return
  fi

  echo "  [$name] starting in tmux pane..."

  local prompt="$RESEARCH_PROMPT
---
**Your categories:** $categories
**Date:** $DATE
**Output file:** $outfile
${PREV_HEADLINES:+
**Previous edition headlines (skip unless genuinely new development):**
$PREV_HEADLINES}

**Pre-research scan:**
$PRE_RESEARCH"

  # Write prompt to temp file to avoid shell escaping issues
  local prompt_file="$DAY_DIR/.prompt-${name}.md"
  printf '%s' "$prompt" > "$prompt_file"

  local runner="$DIR/tools/run-agent.sh"
  local cmd="cd $ROOT_DIR && $runner $outfile done-$name $PI_CMD --model $PI_MODEL --tools read,write,bash $PI_BLOCK_DOMAINS @$prompt_file"

  # First cluster creates the window, rest split into panes
  if ! tmux list-windows -F '#{window_name}' 2>/dev/null | grep -qx "$TMUX_WIN"; then
    tmux new-window -n "$TMUX_WIN" -d "$cmd"
  else
    tmux split-window -t "$TMUX_WIN" -v -d "$cmd"
    tmux select-layout -t "$TMUX_WIN" tiled 2>/dev/null || true
  fi

  NAMES+=("$name")
}

# --- Mini mode: 1 cluster, capped stories ---
if [[ "${PIPELINE_MINI:-}" == "1" ]]; then
  MINI_CLUSTER="${PIPELINE_CLUSTERS:-ai}"
  echo "  [mini] Running cluster: $MINI_CLUSTER (3-story cap)"
  RESEARCH_PROMPT="$RESEARCH_PROMPT

**MINI MODE: Return at most 3 stories. Pick the 3 most important.**"
  run_cluster "$MINI_CLUSTER" "$(eval echo "\$CLUSTER_$(echo "$MINI_CLUSTER" | tr '[:lower:]' '[:upper:]')")"
else
  for _cluster_name in ${PIPELINE_CLUSTERS:-${TOPIC_CLUSTERS:-ai hw world}}; do
    _upper=$(echo "$_cluster_name" | tr '[:lower:]' '[:upper:]')
    run_cluster "$_cluster_name" "$(eval echo "\$CLUSTER_${_upper}")"
  done
fi

# --- Seeds (user-submitted URLs) ---
SEEDS_FILE="$DAY_DIR/seeds.md"
if [[ "${PIPELINE_MINI:-}" == "1" ]]; then
  echo "  [seeds] skipped (mini mode)"
elif [[ -f "$SEEDS_FILE" ]] && [[ -s "$SEEDS_FILE" ]]; then
  SEEDS_PROMPT="$(cat "$TOPIC_PROMPTS_DIR/SEEDS.md" 2>/dev/null || cat "$DIR/prompts/SEEDS.md")"
  SEEDS_URLS="$(cat "$SEEDS_FILE")"
  SEEDS_OUT="$DAY_DIR/research-seeds.json"

  if [[ -f "$SEEDS_OUT" ]]; then
    echo "  [seeds] already exists, skipping"
  else
    echo "  [seeds] $(grep -c 'http' "$SEEDS_FILE") URLs found"

    local prompt_file="$DAY_DIR/.prompt-seeds.md"
    printf '%s' "$SEEDS_PROMPT
---
**Date:** $DATE
**Output file:** $SEEDS_OUT
**URLs to research:**
$SEEDS_URLS" > "$prompt_file"

    local runner="$DIR/tools/run-agent.sh"
    local cmd="cd $ROOT_DIR && $runner $SEEDS_OUT done-seeds $PI_CMD --model $PI_MODEL --tools read,write,bash $PI_BLOCK_DOMAINS @$prompt_file"

    tmux split-window -t "$TMUX_WIN" -v -d "$cmd"
    tmux select-layout -t "$TMUX_WIN" tiled 2>/dev/null || true
    NAMES+=("seeds")
  fi
else
  echo "  [seeds] no seeds.md found, skipping"
fi

# --- Wait for all clusters ---
echo ""
echo "  Waiting for ${#NAMES[@]} agents: ${NAMES[*]}"
echo "  Watch live: tmux select-window -t $TMUX_WIN"
echo ""

FAILURES=0
for name in "${NAMES[@]}"; do
  if ! tmux wait-for "done-$name" 2>/dev/null; then
    echo "  ⚠ [$name] signal failed"
    ((FAILURES++)) || true
  fi
done

# Clean up tmux window
tmux kill-window -t "$TMUX_WIN" 2>/dev/null || true

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))
echo "  Clusters done in ${STEP_DURATION}s ($FAILURES failures)"

# --- Merge partial files ---
PARTIALS=()
for name in ${TOPIC_CLUSTERS:-ai hw world} seeds; do
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
  stories: [.[].stories[] | {id, headline, key_facts, sources, category, entities}] | unique_by(.id),
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
