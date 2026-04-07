#!/bin/bash
#
# Mini draft pipeline for testing changes end-to-end.
#
# Runs the same 4 steps as pipeline/draft.sh but:
#   - Output goes to tests/output/ (never touches pipeline/output/)
#   - Research runs 1 cluster with 3-story cap
#   - Fixtures provide previous editions for repetition check
#
# Usage: ./tests/test-draft.sh                          # full mini pipeline, today
#        ./tests/test-draft.sh 2026-03-30               # specific date
#        ./tests/test-draft.sh --skip-research           # use fixture research data
#        ./tests/test-draft.sh --only research           # just research step
#        ./tests/test-draft.sh --only generate           # just generate (needs research.json)
#        ./tests/test-draft.sh --cluster hw              # test hw cluster instead of ai
#        ./tests/test-draft.sh --validate                # just run validation on existing output
#        ./tests/test-draft.sh --clean                   # wipe test output for date, then run
#        ./tests/test-draft.sh --full                    # full pipeline (all clusters, no story cap)
#

set -euo pipefail

# Prevent macOS idle sleep while pipeline runs
if [[ -z "${CAFFEINATED:-}" ]] && command -v caffeinate &>/dev/null; then
  exec env CAFFEINATED=1 caffeinate -i "$0" "$@"
fi

TESTS_DIR="$(cd "$(dirname "$0")" && pwd)"
PIPELINE_DIR="$TESTS_DIR/../pipeline"

# --- Parse args ---
DATE=""
SKIP_RESEARCH=false
ONLY=""
CLUSTER="ai"
VALIDATE_ONLY=false
CLEAN=false
FULL=false
EXTRA_ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$1"; shift ;;
    --skip-research) SKIP_RESEARCH=true; shift ;;
    --only)          ONLY="$2"; shift 2 ;;
    --cluster)       CLUSTER="$2"; shift 2 ;;
    --validate)      VALIDATE_ONLY=true; shift ;;
    --clean)         CLEAN=true; shift ;;
    --full)          FULL=true; shift ;;
    *)               EXTRA_ARGS+=("$1"); shift ;;
  esac
done

DATE="${DATE:-$(date +%Y-%m-%d)}"

# --- Export env for pipeline scripts ---
export PIPELINE_OUTPUT="$TESTS_DIR/output"
if [[ "$FULL" != true ]]; then
  export PIPELINE_MINI=1
  export PIPELINE_CLUSTERS="$CLUSTER"
fi

TEST_OUTPUT="$PIPELINE_OUTPUT/$DATE"
FIXTURES="$TESTS_DIR/fixtures"

MODE_LABEL="mini ($CLUSTER)"
if [[ "$FULL" == true ]]; then
  MODE_LABEL="full (all clusters)"
fi
[[ -n "$ONLY" ]] && MODE_LABEL="$ONLY only"

echo ""
echo "=== Test Draft: $DATE ==="
echo "  Output:  $TEST_OUTPUT"
echo "  Mode:    $MODE_LABEL"
echo ""

# --- Validate only ---
if [[ "$VALIDATE_ONLY" == true ]]; then
  "$TESTS_DIR/validate.sh" "$DATE" --verbose
  exit $?
fi

# --- Clean ---
if [[ "$CLEAN" == true ]]; then
  if [[ -d "$TEST_OUTPUT" ]]; then
    echo "  Cleaning $TEST_OUTPUT..."
    rm -rf "$TEST_OUTPUT"
  fi
fi

mkdir -p "$TEST_OUTPUT"

# --- Seed fixtures if needed ---
if [[ ! -d "$FIXTURES/prev-editions" ]]; then
  echo "  Seeding fixtures (first run)..."
  "$TESTS_DIR/seed-fixtures.sh"
  echo ""
fi

# --- Copy previous editions for repetition check ---
if [[ -d "$FIXTURES/prev-editions" ]]; then
  for prev in "$FIXTURES/prev-editions"/*/; do
    prev_date=$(basename "$prev")
    if [[ ! -f "$PIPELINE_OUTPUT/$prev_date/pt.md" ]]; then
      mkdir -p "$PIPELINE_OUTPUT/$prev_date"
      cp "$prev/pt.md" "$PIPELINE_OUTPUT/$prev_date/pt.md"
      echo "  Fixture: $prev_date/pt.md"
    fi
  done
fi

# --- Skip-research: use fixture data ---
if [[ "$SKIP_RESEARCH" == true ]] && [[ ! -f "$TEST_OUTPUT/research.json" ]]; then
  if [[ -f "$FIXTURES/research-mini.json" ]]; then
    cp "$FIXTURES/research-mini.json" "$TEST_OUTPUT/research.json"
    STORIES=$(jq '.story_count' "$TEST_OUTPUT/research.json")
    echo "  Using fixture research ($STORIES stories)"
  else
    echo "  Error: No fixture research data. Run seed-fixtures.sh first."
    exit 1
  fi
fi

echo ""

# --- Step runner ---
PIPELINE_START=$(date +%s)
STEPS_RUN=0

run_step() {
  local name="$1"
  local script="$2"

  # Skip if --only is set and doesn't match
  if [[ -n "$ONLY" ]] && [[ "$ONLY" != "$name" ]]; then
    return
  fi

  echo "--- $name ---"
  local step_start=$(date +%s)

  "$PIPELINE_DIR/$script" "$DATE" ${EXTRA_ARGS[@]:+"${EXTRA_ARGS[@]}"} || {
    echo "  ⚠ $name failed (exit $?)"
    return 1
  }

  local step_end=$(date +%s)
  local duration=$((step_end - step_start))
  echo "  [$name] ${duration}s"
  echo ""
  STEPS_RUN=$((STEPS_RUN + 1))
}

# --- Run steps ---
if [[ "$SKIP_RESEARCH" != true ]]; then
  run_step "research"         "research.sh"
fi
run_step "generate"           "generate.sh"
run_step "repetition-check"   "repetition-check.sh"
run_step "audit"              "audit.sh"

PIPELINE_END=$(date +%s)
TOTAL=$((PIPELINE_END - PIPELINE_START))

echo ""
echo "=== Test Draft Complete ==="
echo "  Steps: $STEPS_RUN"
echo "  Duration: ${TOTAL}s ($(( TOTAL / 60 ))m $(( TOTAL % 60 ))s)"
echo ""

# --- Auto-validate ---
echo "=== Running validation ==="
"$TESTS_DIR/validate.sh" "$DATE" --verbose
