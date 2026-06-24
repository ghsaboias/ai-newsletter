#!/bin/bash
#
# Generate paywall teaser block from final.md.
#
# Usage: ./paywall-teaser.sh              # today's date
#        ./paywall-teaser.sh 2026-06-02   # specific date
#
# Reads:  final.md
# Writes: paywall-teaser.md, paywall-meta.json

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
source "$DIR/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir

# --v2: generate teasers for the v2 three-tier draft (reads v2.md; cut is
# structural — after the grandes — so the meta carries teasers, not a cut index).
V2=false
for arg in "$@"; do [[ "$arg" == "--v2" ]] && V2=true; done

if [[ "$V2" == true ]]; then
  LABEL="-v2"
  FINAL_FILE="$DAY_DIR/v2.md"
  OUTPUT_MD="$DAY_DIR/paywall-v2-teaser.md"
  OUTPUT_META="$DAY_DIR/paywall-v2-meta.json"
  PROMPT_TEMPLATE="$DIR/prompts/PAYWALL_TEASER_V2.md"
else
  LABEL=""
  FINAL_FILE="$DAY_DIR/final.md"
  OUTPUT_MD="$DAY_DIR/paywall-teaser.md"
  OUTPUT_META="$DAY_DIR/paywall-meta.json"
  PROMPT_TEMPLATE="$DIR/prompts/PAYWALL_TEASER.md"
fi
EXAMPLE="$DIR/../pipeline/output/ai/2026-05-29/paywall-teaser.md"

echo ""
echo "=== Paywall Teaser: $DATE ==="
echo ""

if [[ ! -f "$FINAL_FILE" ]]; then
  echo "  Error: $FINAL_FILE not found. Run rewrite-links.sh first."
  exit 1
fi

if [[ -f "$OUTPUT_META" ]] && [[ -f "$OUTPUT_MD" ]]; then
  CUT=$(jq -r '.cut_after' "$OUTPUT_META")
  COUNT=$(jq '.teasers | length' "$OUTPUT_META")
  echo "  Already exists — cut_after=$CUT, $COUNT teasers"
  echo "  Delete $OUTPUT_META to regenerate."
  exit 0
fi

PROMPT_FILE="$DAY_DIR/.prompt-paywall-teaser${LABEL}.md"
PROMPT_BODY="$(cat "$PROMPT_TEMPLATE")"
PROMPT_BODY="${PROMPT_BODY//\{\{FINAL_FILE\}\}/$FINAL_FILE}"
PROMPT_BODY="${PROMPT_BODY//\{\{V2_FILE\}\}/$FINAL_FILE}"
PROMPT_BODY="${PROMPT_BODY//\{\{OUTPUT_MD\}\}/$OUTPUT_MD}"
PROMPT_BODY="${PROMPT_BODY//\{\{OUTPUT_META\}\}/$OUTPUT_META}"
PROMPT_BODY="${PROMPT_BODY//\{\{EXAMPLE\}\}/$EXAMPLE}"
printf '%s' "$PROMPT_BODY" > "$PROMPT_FILE"

echo "  Input:  $FINAL_FILE"
echo "  Output: $OUTPUT_MD + $OUTPUT_META"
echo ""

STEP_START=$(date +%s)

SIG="done-paywall${LABEL}-$DATE"
TMUX_WIN="paywall${LABEL}-$DATE"
tmux new-window -n "$TMUX_WIN" -d \
  "cd $ROOT_DIR && $DIR/tools/run-agent.sh $OUTPUT_META $SIG $CLAUDE_CMD --model $CLAUDE_MODEL --allowedTools Read,Write < $PROMPT_FILE"

echo "  Watch: tmux select-window -t $TMUX_WIN"
tmux wait-for "$SIG"
tmux kill-window -t "$TMUX_WIN" 2>/dev/null || true
rm -f "$PROMPT_FILE"

STEP_END=$(date +%s)

if [[ ! -f "$OUTPUT_META" ]]; then
  echo "  Error: paywall-meta.json not produced."
  exit 1
fi

if ! jq empty "$OUTPUT_META" 2>/dev/null; then
  echo "  Error: paywall-meta.json is not valid JSON."
  exit 1
fi

CUT=$(jq -r '.cut_after' "$OUTPUT_META")
COUNT=$(jq '.teasers | length' "$OUTPUT_META")
DASHES=$(grep -o '—' "$OUTPUT_MD" 2>/dev/null | wc -l | tr -d ' ' || echo "0")

echo "  cut_after:  $CUT"
echo "  Teasers:    $COUNT"
[[ "$DASHES" -gt 0 ]] && echo "  WARNING: $DASHES em-dashes found (voice rule violated)"
echo "  Done in $((STEP_END - STEP_START))s"
