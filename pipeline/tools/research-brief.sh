#!/usr/bin/env bash
# Build the day's shared research brief — ONE file the three cluster researchers
# (the `researcher` agent, one instance per cluster) Read as their first action, instead of the
# orchestrator pasting the same ~26KB brief into three Agent prompts (which
# forced the three dispatches to go out serially, 1-5 min apart).
#
# Usage: research-brief.sh <DATE> [mini]
#   → writes $DAY_DIR/research-brief.md (and $DAY_DIR/techmeme.md, fetched once)
#   → prints the brief path on stdout; a one-line summary on stderr
#
# Content, in order: newsletters/<topic>/prompts/RESEARCH.md with {{DATE}} /
# {{PREV_DATE}} substituted, the previous edition's headlines (most recent
# earlier day with research.json, up to 7 days back), the Techmeme scan, and
# the MINI MODE cap when asked. Idempotent: an existing techmeme.md is reused
# (same landscape for a re-run); the brief itself is always rewritten.
set -euo pipefail
source "$(dirname "$0")/../_lib.sh"

DATE="${1:?usage: research-brief.sh <DATE> [mini]}"
MINI=0; [[ "${2:-}" == "mini" ]] && MINI=1
init_day_dir
OUT="$DAY_DIR/research-brief.md"
PROMPT="$TOPIC_PROMPTS_DIR/RESEARCH.md"
[[ -s "$PROMPT" ]] || { echo "HALT: missing $PROMPT" >&2; exit 1; }

# PREV_DATE = most recent earlier day dir with a research.json (Monday → Friday),
# falling back to the calendar day before.
PREV_DATE=""; CHECK="$DATE"
for _ in 1 2 3 4 5 6 7; do
  CHECK=$(date -d "$CHECK - 1 day" "+%Y-%m-%d")
  [[ -s "$LOOP_DIR/$CHECK/research.json" ]] && { PREV_DATE="$CHECK"; break; }
done
[[ -n "$PREV_DATE" ]] || PREV_DATE=$(date -d "$DATE - 1 day" "+%Y-%m-%d")

PREV_HEADLINES="(none)"
if [[ -s "$LOOP_DIR/$PREV_DATE/research.json" ]]; then
  PREV_HEADLINES=$(jq -r '.stories[] | "- " + .id + ": " + .headline' "$LOOP_DIR/$PREV_DATE/research.json" 2>/dev/null || echo "(none)")
  [[ -n "$PREV_HEADLINES" ]] || PREV_HEADLINES="(none)"
fi

# Techmeme: fetch once per day dir, shared by all clusters.
TM="$DAY_DIR/techmeme.md"
if [[ ! -s "$TM" ]]; then
  python3 "$DIR/tools/techmeme.py" > "$TM.tmp" 2>/dev/null && mv "$TM.tmp" "$TM" || { rm -f "$TM.tmp"; : > "$TM"; }
fi
if [[ -s "$TM" ]]; then
  SCAN=$(cat "$TM")
else
  SCAN="(Techmeme fetch failed — no scan available; rely on your own searches)"
fi

{
  sed -e "s/{{DATE}}/$DATE/g" -e "s/{{PREV_DATE}}/$PREV_DATE/g" "$PROMPT"
  printf '\n---\n\n**Date:** %s\n**Research window:** %s 10:00 BRT → %s 10:00 BRT\n' "$DATE" "$PREV_DATE" "$DATE"
  printf '\n**Previous edition headlines (%s — skip unless genuinely new development):**\n%s\n' "$PREV_DATE" "$PREV_HEADLINES"
  printf '\n**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):\n\n%s\n' "$SCAN"
  if [[ "$MINI" == 1 ]]; then
    printf '\n**MINI MODE: Return at most 3 stories. Pick the 3 most important.**\n'
  fi
} > "$OUT"

echo "brief: $OUT ($(wc -c < "$OUT") bytes; prev=$PREV_DATE, techmeme=$(wc -c < "$TM") bytes, mini=$MINI)" >&2
echo "$OUT"
