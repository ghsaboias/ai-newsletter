#!/bin/bash
#
# Step 1: Research today's news via 3 parallel cluster searches + merge
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

# Previous headlines always come from real output
PREV_RESEARCH="$LOOP_DIR/$PREV_DATE/research.json"

if [[ "$*" == *"--test"* ]]; then
  LOOP_DIR="$DIR/../tests/output"
fi
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
if [[ -f "$PREV_RESEARCH" ]]; then
  PREV_HEADLINES=$(jq -r '.stories[] | "- " + .id + ": " + .headline' "$PREV_RESEARCH")
  echo "  Previous: $(echo "$PREV_HEADLINES" | wc -l | tr -d ' ') headlines from $PREV_DATE"
else
  echo "  Previous: none found"
fi
echo ""

# --- Techmeme scan (shared across all clusters) ---
echo "  Fetching Techmeme..."
TECHMEME=$(python3 "$DIR/tools/techmeme.py" 2>/dev/null || echo "[Techmeme fetch failed]")
TM_COUNT=$(echo "$TECHMEME" | head -1 | grep -oE '[0-9]+' || echo "0")
echo "  Techmeme: $TM_COUNT stories"
echo ""

ALLOWED_TOOLS="Write,Read,WebFetch,WebSearch,mcp__exa__web_search_exa,Bash(bird *)"

# --- Cluster definitions ---
read -r -d '' CLUSTER_AI << 'EOF' || true
- AI capabilities: new model releases, updates, benchmark results (frontier and open-source)
- Reasoning, coding, and multimodal capability jumps
- Agentic systems: tool use, computer use, autonomous coding, long-horizon tasks
- AI safety: alignment, evaluations, red-teaming, governance proposals
- AI in science: protein folding, drug discovery, materials, math proofs
- AI economics: pricing, API changes, adoption metrics, enterprise deals
- Recursive self-improvement: AI training AI, automated ML research
Key X accounts: @sama, @AnthropicAI, @OpenAI, @GoogleDeepMind, @scaling01, @metr_evals, @epochairesearch, @arcprize
EOF

read -r -d '' CLUSTER_HW << 'EOF' || true
- Chips & semiconductors: Nvidia, AMD, Intel, Broadcom, custom silicon (Google TPU, Amazon Trainium, Microsoft Maia)
- Foundries: TSMC, Samsung, Intel Foundry — capacity, process nodes, orders
- Data centers: new builds, power deals, cooling tech, geographic expansion
- Energy for compute: nuclear, solar, grid upgrades, power purchase agreements
- Export controls: US-China chip restrictions, ASML/EUV, sanctions
- Robotics: humanoids (Tesla Optimus, Figure, Unitree), industrial automation, warehouse robots
- Drones: military, commercial, autonomous delivery, counter-drone systems
- Autonomous vehicles: Waymo, Cruise, Tesla FSD, Chinese players
- Space: launches, satellite constellations, orbital compute, space-based infrastructure
Key X accounts: @elonmusk, @jimfanAI, @chilobrandt
EOF

read -r -d '' CLUSTER_WORLD << 'EOF' || true
- Geopolitics: conflicts, alliances, sanctions, trade wars, diplomatic shifts
- Military: operations, weapons systems, defense deals, intelligence
- Economics: jobs reports, GDP, inflation, central bank moves, oil/energy prices
- Labor & AI displacement: layoffs citing AI, hiring freezes, workforce shifts
- Markets: major moves in equities, commodities, crypto tied to news events
- Funding: major rounds, IPOs, acquisitions, SPAC deals
- Biotech: drug approvals, clinical trial results, CRISPR/gene therapy, longevity research
- Health policy: FDA decisions, pandemic preparedness, health system changes
- Climate/energy: transition milestones, extreme events, policy moves
Key X accounts: @xaborsa
Key sources: Reuters, AP, BBC, Al Jazeera, FT, STAT News, BioPharma Dive, Nature Medicine
EOF

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
$PREV_HEADLINES}

**Techmeme scan:**
$TECHMEME" \
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
