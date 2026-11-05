#!/usr/bin/env bash
# Replay harness: re-run the content stage (research → edition) on a frozen
# research.json from a historical date, sandboxed in evals/runs/ — no ingest,
# no Substack, no Slack, no production writes. Score against the published
# ground truth (evals/dataset/<date>/published-body.json).
#
# Usage:
#   evals/run.sh <DATE> [VARIANT] [--stage edition|advisory|score|all]
#
#   VARIANT       label for this run (default: base). Agent definitions are
#                 whatever .claude/agents/ currently holds — to A/B a prompt
#                 change, edit the agent file (or use a worktree) and name the
#                 variant accordingly.
#   --stage       run a single stage (default all). Stages are idempotent —
#                 rerunning resumes at the first missing output.
#
# The `advisory` stage runs the two non-gating auditors (fact-verifier and
# repetition-checker) against the run's edition.md, writing fact-check.json and
# repetition.json INTO THE RUN DIR — production's copies are never touched. If
# the run has no edition.md it seeds the production one, so you can re-audit a
# shipped edition with edited agent prompts. It is NOT part of `all`; ask for it.
#   MODEL=<m>     env var: pass --model to the headless claude calls.
#
# Each stage is a one-shot headless `claude -p` that dispatches the registered
# agent with the same paths-only task prompt the newsletter-draft skill uses.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

DATE="${1:?usage: run.sh <DATE> [VARIANT] [--stage ...]}"; shift
VARIANT="base"
[ $# -gt 0 ] && [[ "$1" != --* ]] && { VARIANT="$1"; shift; }
STAGE="all"
while [ $# -gt 0 ]; do
  case "$1" in
    --stage) STAGE="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

PROD="$REPO/pipeline/output/ai/$DATE"
RUN="$REPO/evals/runs/${DATE}__${VARIANT}"
mkdir -p "$RUN"
[ -s "$PROD/research.json" ] || { echo "HALT: no research.json for $DATE" >&2; exit 1; }
[ -s "$RUN/research.json" ] || cp "$PROD/research.json" "$RUN/research.json"

# Previous editions relative to DATE (up to 3, walking back up to 7 days), from
# real history. Same list the newsletter-draft skill gives the generator and
# the two auditors.
ROOT="$REPO/pipeline/output/ai"; PREVLIST=""; N=0; CHECK="$DATE"
for i in 1 2 3 4 5 6 7; do
  CHECK=$(date -d "$CHECK - 1 day" "+%Y-%m-%d")
  [ -s "$ROOT/$CHECK/edition.md" ] || continue
  PREVLIST+="$CHECK: $ROOT/$CHECK/edition.md"$'\n'; N=$((N+1))
  [ "$N" -ge 3 ] && break
done

CLAUDE_FLAGS=(--allowedTools "Agent,Task,Read,Write,Bash,WebSearch,WebFetch" --output-format json ${MODEL:+--model "$MODEL"})

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

# ---- edition ----
if [[ "$STAGE" =~ ^(all|edition)$ ]] && [ ! -s "$RUN/edition.md" ]; then
  run_stage edition "Use the Agent tool to dispatch subagent_type \"generator\" with exactly this prompt, wait for completion, then reply with one line (its summary or FAILED: <reason>):
Date: $DATE ($(LC_ALL=pt_BR.UTF-8 date -d "$DATE" +%A)).
Pesquisa do dia (research.json): $RUN/research.json
Edições anteriores, da mais recente para a mais antiga:
${PREVLIST:-(nenhuma)}
Princípios editoriais: $REPO/CLAUDE.md (seção \"Editorial Principles\")
Escreva a edição em: $RUN/edition.md"
fi
if [[ "$STAGE" =~ ^(all|edition|score)$ ]] && [ -s "$RUN/edition.md" ]; then
  python3 "$REPO/pipeline/tools/check-links.py" "$RUN/edition.md" "$RUN/research.json" \
    || { echo "HALT: edition links not in research.json" >&2; exit 1; }
  G=$(grep -c '^### ' "$RUN/edition.md" || echo 0)
  echo "OK edition: $G grandes"
fi

# ---- advisory (fact-verifier + repetition-checker) ----
# Not in `all`: opt in with --stage advisory. Audits $RUN/edition.md, seeding the
# production edition when the run has none (re-audit of a shipped edition).
if [ "$STAGE" = "advisory" ]; then
  if [ ! -s "$RUN/edition.md" ]; then
    [ -s "$PROD/edition.md" ] || { echo "HALT: no edition.md in run or production for $DATE" >&2; exit 1; }
    cp "$PROD/edition.md" "$RUN/edition.md"; echo "seeded production edition.md (advisory re-audit)"
  fi
  PREV_ED=$(printf '%s' "$PREVLIST" | head -1 | cut -d' ' -f2-)
  [ -s "$RUN/fact-check.json" ] || run_stage fact-check "Use the Agent tool to dispatch subagent_type \"fact-verifier\" with exactly this prompt, wait for completion, then reply with one line (its summary or FAILED: <reason>):
Date: $DATE.
research.json: $RUN/research.json
Edition (edition.md): $RUN/edition.md
Edição da véspera (árbitro da classe 'atribuição inventada'): ${PREV_ED:-(nenhuma)}
Write findings to: $RUN/fact-check.json"

  [ -s "$RUN/repetition.json" ] || run_stage repetition "Use the Agent tool to dispatch subagent_type \"repetition-checker\" with exactly this prompt, wait for completion, then reply with one line (its summary or FAILED: <reason>):
Date: $DATE.
Current edition: $RUN/edition.md
Previous editions to compare against:
${PREVLIST:-(none found)}
Write findings to: $RUN/repetition.json"

  for f in fact-check repetition; do
    python3 "$REPO/pipeline/tools/validate-findings.py" "$f" "$RUN/$f.json" \
      || echo "WARN: $f.json fora do schema"
  done
  echo "OK advisory: $RUN/fact-check.json + $RUN/repetition.json"
fi

# ---- score ----
if [[ "$STAGE" =~ ^(all|edition|score)$ ]] && [ -s "$RUN/edition.md" ]; then
  python3 "$REPO/evals/tools/score.py" "$RUN/edition.md" --date "$DATE" --json "$RUN/score.json"
fi
