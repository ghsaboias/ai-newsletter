#!/bin/bash
#
# Draft Rewrite: Apply repetition-check findings surgically to pt.md
#
# Reads:  pt.md, repetition.json, GENERATION.md, feedback memories
# Writes: pt.md (overwritten), pt-original.md (backup), rewrite-notes.json
#
# Usage: ./draft-rewrite.sh              # today's date
#        ./draft-rewrite.sh 2026-04-16   # specific date
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir

PT_FILE="$DAY_DIR/pt.md"
PT_ORIGINAL="$DAY_DIR/pt-original.md"
REP_FILE="$DAY_DIR/repetition.json"
NOTES_FILE="$DAY_DIR/rewrite-notes.json"

init_log "$DATE"

echo ""
echo "=== Draft Rewrite: $DATE ==="
echo ""

if [[ -f "$NOTES_FILE" ]]; then
  APPLIED=$(jq '[.findings[] | select(.action == "applied")] | length' "$NOTES_FILE" 2>/dev/null || echo "?")
  echo "  ⚠ $NOTES_FILE already exists ($APPLIED applied)"
  echo "  Delete it (and restore pt.md from pt-original.md if desired) to re-run."
  exit 0
fi

if [[ ! -f "$PT_FILE" ]]; then
  echo "  Error: $PT_FILE not found (run generate.sh first)."
  exit 1
fi

if [[ ! -f "$REP_FILE" ]]; then
  echo "  Error: $REP_FILE not found (run repetition-check.sh first)."
  exit 1
fi

ISSUE_COUNT=$(jq '.issues | length' "$REP_FILE")
if [[ $ISSUE_COUNT -eq 0 ]]; then
  echo "  No issues in repetition.json. Skipping rewrite."
  exit 0
fi

GENERATION_PROMPT="$TOPIC_PROMPTS_DIR/GENERATION.md"
REWRITE_PROMPT="$DIR/prompts/DRAFT_REWRITE.md"
MEMORY_DIR="$HOME/.claude/projects/-Users-guilherme-ai-newsletter/memory"

if [[ ! -f "$GENERATION_PROMPT" ]]; then
  echo "  Error: $GENERATION_PROMPT not found."
  exit 1
fi
if [[ ! -f "$REWRITE_PROMPT" ]]; then
  echo "  Error: $REWRITE_PROMPT not found."
  exit 1
fi

# Backup pt.md if we haven't already (retry-safe: preserves the true original).
if [[ ! -f "$PT_ORIGINAL" ]]; then
  cp "$PT_FILE" "$PT_ORIGINAL"
fi

echo "  Original: $PT_ORIGINAL ($ISSUE_COUNT findings)"
echo "  Output:   $PT_FILE (overwritten)"
echo "  Notes:    $NOTES_FILE"
echo ""

STEP_START=$(date +%s)

PROMPT_BODY="$(cat "$REWRITE_PROMPT")"
PROMPT_BODY="${PROMPT_BODY//\{\{DATE\}\}/$DATE}"
PROMPT_BODY="${PROMPT_BODY//\{\{PT_ORIGINAL\}\}/$PT_ORIGINAL}"
PROMPT_BODY="${PROMPT_BODY//\{\{PT_OUT\}\}/$PT_FILE}"
PROMPT_BODY="${PROMPT_BODY//\{\{REPETITION_JSON\}\}/$REP_FILE}"
PROMPT_BODY="${PROMPT_BODY//\{\{GENERATION_MD\}\}/$GENERATION_PROMPT}"
PROMPT_BODY="${PROMPT_BODY//\{\{NOTES_JSON\}\}/$NOTES_FILE}"
PROMPT_BODY="${PROMPT_BODY//\{\{MEMORY_DIR\}\}/$MEMORY_DIR}"

PROMPT_FILE="$DAY_DIR/.prompt-rewrite.md"
printf '%s' "$PROMPT_BODY" > "$PROMPT_FILE"

TMUX_WIN="rewrite-$DATE"
tmux new-window -n "$TMUX_WIN" -d "cd $ROOT_DIR && $DIR/tools/run-agent.sh $NOTES_FILE done-rewrite $PI_CMD --model $PI_MODEL --no-extensions --tools read,write,edit @$PROMPT_FILE"

echo "  Watch live: tmux select-window -t $TMUX_WIN"
tmux wait-for done-rewrite
tmux kill-window -t "$TMUX_WIN" 2>/dev/null || true
rm -f "$PROMPT_FILE"

STEP_END=$(date +%s)
STEP_DURATION=$((STEP_END - STEP_START))

if [[ ! -f "$NOTES_FILE" ]]; then
  echo ""
  echo "  Error: did not produce $NOTES_FILE"
  exit 1
fi

if ! jq empty "$NOTES_FILE" 2>/dev/null; then
  echo ""
  echo "  Error: $NOTES_FILE is not valid JSON"
  exit 1
fi

APPLIED=$(jq '[.findings[] | select(.action == "applied")] | length' "$NOTES_FILE")
SKIPPED=$(jq '[.findings[] | select(.action == "skipped")] | length' "$NOTES_FILE")
FLAGGED=$(jq '[.findings[] | select(.action == "flagged")] | length' "$NOTES_FILE")

echo ""
echo "  Applied: $APPLIED"
echo "  Skipped: $SKIPPED"
echo "  Flagged: $FLAGGED"

if [[ $SKIPPED -gt 0 ]]; then
  echo ""
  jq -r '.findings[] | select(.action == "skipped") | "  • [skipped] \(.reason)"' "$NOTES_FILE"
fi
if [[ $FLAGGED -gt 0 ]]; then
  echo ""
  jq -r '.findings[] | select(.action == "flagged") | "  • [flagged] \(.reason)"' "$NOTES_FILE"
fi

echo ""
echo "  Done in ${STEP_DURATION}s"
echo "  Diff:  diff $PT_ORIGINAL $PT_FILE"
