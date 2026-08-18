#!/usr/bin/env bash
# Replay harness: re-run the content stages (facts → edition) on a frozen
# research.json from a historical date, sandboxed in evals/runs/ — no ingest,
# no Substack, no Slack, no production writes. Score against the published
# ground truth (evals/dataset/<date>/published-body.json).
#
# Usage:
#   evals/run.sh <DATE> [VARIANT] [--stage facts|edition|score|all] [--from-facts]
#
#   VARIANT       label for this run (default: base). Agent definitions are
#                 whatever .claude/agents/ currently holds — to A/B a prompt
#                 change, edit the agent file (or use a worktree) and name the
#                 variant accordingly.
#   --stage       run a single stage (default all). Stages are idempotent —
#                 rerunning resumes at the first missing output.
#   --from-facts  seed the run with the PRODUCTION facts.md of that date
#                 (ablate the generator only; skips the facts stage).
#   MODEL=<m>     env var: pass --model to the headless claude calls.
#
# Each stage is a one-shot headless `claude -p` that dispatches the registered
# agent with the same paths-only task prompt the newsletter-draft skill uses.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

DATE="${1:?usage: run.sh <DATE> [VARIANT] [--stage ...] [--from-facts]}"; shift
VARIANT="base"
[ $# -gt 0 ] && [[ "$1" != --* ]] && { VARIANT="$1"; shift; }
STAGE="all"; FROM_FACTS=0
while [ $# -gt 0 ]; do
  case "$1" in
    --stage) STAGE="$2"; shift 2 ;;
    --from-facts) FROM_FACTS=1; shift ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

PROD="$REPO/pipeline/output/ai/$DATE"
RUN="$REPO/evals/runs/${DATE}__${VARIANT}"
mkdir -p "$RUN"
[ -s "$PROD/research.json" ] || { echo "HALT: no research.json for $DATE" >&2; exit 1; }
[ -s "$RUN/research.json" ] || cp "$PROD/research.json" "$RUN/research.json"
if [ "$FROM_FACTS" = 1 ] && [ ! -s "$RUN/facts.md" ]; then
  cp "$PROD/facts.md" "$RUN/facts.md"
  echo "seeded production facts.md (generator-only ablation)"
fi

CLAUDE_FLAGS=(--allowedTools "Agent,Task,Read,Write" --output-format json ${MODEL:+--model "$MODEL"})

run_stage() { # name, prompt -> saves transcript json, prints duration
  local name="$1" prompt="$2" t0 t1 out
  t0=$(date +%s)
  out=$(claude -p "$prompt" "${CLAUDE_FLAGS[@]}" 2>"$RUN/$name.stderr" || true)
  t1=$(date +%s)
  printf '%s' "$out" > "$RUN/$name.result.json"
  echo "[$name] $((t1-t0))s — $(printf '%s' "$out" | python3 -c 'import sys,json
try: d=json.load(sys.stdin); print((d.get("result") or "")[:160].replace(chr(10)," "))
except Exception: print("(unparseable result — see file)")')"
}

# ---- facts ----
if [[ "$STAGE" =~ ^(all|facts)$ ]] && [ ! -s "$RUN/facts.md" ]; then
  run_stage facts "Use the Agent tool to dispatch subagent_type \"facts\" with exactly this prompt, wait for completion, then reply with one line (its summary or FAILED: <reason>):
Date: $DATE.
Research (input): $RUN/research.json
Write the atomic fact base to: $RUN/facts.md"
fi
if [[ "$STAGE" =~ ^(all|facts|edition)$ ]]; then
  SEC=$(grep -c '^## ' "$RUN/facts.md" 2>/dev/null || echo 0)
  FON=$(grep -c '^\*\*Fontes:\*\*' "$RUN/facts.md" 2>/dev/null || echo 0)
  [ -s "$RUN/facts.md" ] && [ "$SEC" -gt 0 ] && [ "$FON" -eq "$SEC" ] \
    || { echo "HALT: facts gate failed (sections=$SEC fontes=$FON)" >&2; exit 1; }
  echo "OK facts: $SEC stories"
  python3 "$REPO/pipeline/tools/link-tokens.py" tokenize "$RUN/facts.md" >/dev/null
fi

# ---- edition ----
if [[ "$STAGE" =~ ^(all|edition)$ ]] && [ ! -s "$RUN/edition.md" ]; then
  # recent-grandes + previous-edition context, from real history relative to DATE
  ROOT="$REPO/pipeline/output/ai"; RECENT=""; PREV=""; CHECK="$DATE"
  for i in 1 2 3 4 5; do
    CHECK=$(date -d "$CHECK - 1 day" "+%Y-%m-%d")
    for f in edition-final.md edition.md; do
      [ -s "$ROOT/$CHECK/$f" ] || continue
      RECENT+=$(grep '^### ' "$ROOT/$CHECK/$f" | sed "s/^### /- $CHECK: /")$'\n'
      [ -n "$PREV" ] || PREV="$ROOT/$CHECK/$f"
      break
    done
  done
  run_stage edition "Use the Agent tool to dispatch subagent_type \"generator\" with exactly this prompt, wait for completion, then reply with one line (its summary or FAILED: <reason>):
Date: $DATE.
Fact base (input): $RUN/facts.md
Write the three-tier edition to: $RUN/edition.md

Recent Grandes (do NOT re-lead these — a story whose core event already led here demotes to Média, unless it has a genuinely new, dated in-window development to lead with):
${RECENT:-(nenhuma)}
Edição da véspera (READ this file before writing — any of today's stories whose core event already ran there, in ANY tier, must be framed as continuity per your Continuidade rule, never re-presented as fresh):
${PREV:-(nenhuma)}"
fi
if [[ "$STAGE" =~ ^(all|edition|score)$ ]] && [ -s "$RUN/edition.md" ]; then
  python3 "$REPO/pipeline/tools/link-tokens.py" expand "$RUN/edition.md" "$RUN/facts.md" >/dev/null \
    || { echo "HALT: link-token expand failed" >&2; exit 1; }
  G=$(grep -c '^### ' "$RUN/edition.md" || echo 0)
  echo "OK edition: $G grandes"
fi

# ---- score ----
if [[ "$STAGE" =~ ^(all|edition|score)$ ]] && [ -s "$RUN/edition.md" ]; then
  python3 "$REPO/evals/tools/score.py" "$RUN/edition.md" --date "$DATE" --json "$RUN/score.json"
fi
