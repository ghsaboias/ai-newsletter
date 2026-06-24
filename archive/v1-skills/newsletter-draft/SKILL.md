---
name: newsletter-draft
description: >-
  Orquestra a fase 1 do pipeline da newsletter de AI/Tech: encadeia research → generate → draft-review → rewrite em sequência, parando se algum passo falhar. Equivalente em skill ao pipeline/draft.sh. Ao final o pt.md está pronto pra revisão humana parágrafo a parágrafo (NÃO roda finalize, NÃO inicia a revisão). Aciona quando o usuário diz "rodar o draft", "fazer o draft do dia", "draftar a newsletter", "fase 1 inteira", "/newsletter-draft". Aceita `YYYY-MM-DD` e a flag `mini` (smoke test ponta a ponta).
allowed-tools: Skill, Read, Write, Bash, Agent, Grep, Glob
---

## When this skill runs

User wants all of Phase 1 in one shot instead of running the four step-skills by hand. This is the skill analog of `pipeline/draft.sh`. It chains, in order:

1. `newsletter-research`     → `research.json`
2. `newsletter-generate`     → `pt.md`
3. `newsletter-draft-review` → `repetition.json`
4. `newsletter-rewrite`      → `pt.md` (overwritten) + `pt-original.md` + `rewrite-notes.json`

When it finishes, **`pt.md` is a draft ready for the human paragraph-by-paragraph review.** This skill does **not** run finalize and does **not** start the review — it stops at exactly the point `draft.sh` stops.

## Args

Invoked as `/newsletter-draft [args]`. Parse from the user message:

- `YYYY-MM-DD` — run for a specific date (overrides "today")
- `mini` — **pass-through to research only** (1 cluster, 3-story cap). Generate/review/rewrite then run normally on those 3 stories. Fast end-to-end smoke test of the whole chain.
- (no args) — today's date, full run

## Step 0: Resolve the date ONCE

Run `date '+%Y-%m-%d %H:%M:%S %Z'`. Set `DATE` = today unless an explicit `YYYY-MM-DD` arg was passed.

**Resolve `DATE` here and pass it explicitly to every child skill.** Don't let the children each call `date` independently — a run that crosses midnight could otherwise split across two day-dirs. One date, four steps, one `pipeline/output/ai/$DATE/` directory.

Record the start time for the final duration:

```bash
date '+%Y-%m-%d %H:%M:%S %Z'; date +%s   # second number = START, keep it
```

## Orchestration model

This skill is **thin**. It does not dispatch research/writer/reviewer agents itself — each child skill already owns that logic, its own idempotency, validation, and reporting. The orchestrator has three jobs only:

1. **Invoke each child skill in order via the Skill tool**, passing `$DATE` (and `mini` to research when the flag is set).
2. **Gate between steps.** After each child returns, verify its expected output exists/is valid *before* invoking the next. If it's missing, **STOP the whole chain and report which step failed** — never run a downstream step on missing input. This reproduces `set -euo pipefail` from `draft.sh`.
3. **Print one final roll-up** at the end.

Each child is idempotent (skips instantly if its output already exists), so re-running `/newsletter-draft` after a mid-chain failure **resumes from the first incomplete step** — completed steps return immediately.

## Step 1: Research

```
Skill({ skill: "newsletter-research", args: "<DATE>" })       # append " mini" when mini flag is set, e.g. "<DATE> mini"
```

Gate (run after the skill returns):

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
if [ -s "$D/research.json" ] && jq -e '.story_count > 0' "$D/research.json" >/dev/null 2>&1; then
  echo "OK research: $(jq '.story_count' "$D/research.json") stories"
else
  echo "HALT: research.json missing or empty"
fi
```

If it prints `HALT`, do **not** invoke Step 2. Report the failure and stop.

## Step 2: Generate

```
Skill({ skill: "newsletter-generate", args: "<DATE>" })
```

Gate:

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
[ -s "$D/pt.md" ] && echo "OK generate: $(wc -w < "$D/pt.md") words" || echo "HALT: pt.md missing"
```

`HALT` → stop, don't run Step 3.

## Step 3: Draft review (repetition check)

```
Skill({ skill: "newsletter-draft-review", args: "<DATE>" })
```

Gate:

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
jq empty "$D/repetition.json" 2>/dev/null && echo "OK review: $(jq '.issues|length' "$D/repetition.json") issues" || echo "HALT: repetition.json missing/invalid"
```

`HALT` → stop, don't run Step 4.

## Step 4: Rewrite

```
Skill({ skill: "newsletter-rewrite", args: "<DATE>" })
```

**Zero-issue case is success, not failure.** `newsletter-rewrite` self-skips when `repetition.json` has 0 issues — then `rewrite-notes.json` may not be written and `pt.md` is unchanged. Gate accordingly:

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
ISSUES=$(jq '.issues|length' "$D/repetition.json")
if [ "$ISSUES" -gt 0 ]; then
  [ -s "$D/rewrite-notes.json" ] && echo "OK rewrite" || echo "WARN: $ISSUES issues but rewrite-notes.json missing"
else
  echo "OK rewrite: 0 issues, nothing to apply"
fi
```

A `WARN` here is worth surfacing but does not invalidate the draft — `pt.md` still exists.

## Step 5: Final roll-up

Mirror `draft.sh`'s tail. One block, then the hand-off line:

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
echo "=== Draft Complete: <DATE> ==="
[ -f "$D/repetition.json" ] && echo "  Repetition issues: $(jq '.issues|length' "$D/repetition.json")"
if [ -f "$D/rewrite-notes.json" ]; then
  A=$(jq '[.findings[]|select(.action=="applied")]|length' "$D/rewrite-notes.json")
  S=$(jq '[.findings[]|select(.action=="skipped")]|length' "$D/rewrite-notes.json")
  F=$(jq '[.findings[]|select(.action=="flagged")]|length' "$D/rewrite-notes.json")
  echo "  Rewrites: $A applied, $S skipped, $F flagged"
fi
echo "  Duration: $(( ($(date +%s) - START) / 60 ))m $(( ($(date +%s) - START) % 60 ))s"
```

Then print the hand-off:

> `pt.md` pronto. Próximo passo: **revisão humana parágrafo a parágrafo** (leia os memory files em `~/.claude/projects/-Users-guilherme-ai-newsletter/memory/` primeiro), depois `/newsletter-finalize`. Diff do que o rewrite mudou: `diff $D/pt-original.md $D/pt.md`.

Do **not** re-print each child's report — they already printed their own. The orchestrator adds only this roll-up.

## Behavioral rules

- **Sequential and gated.** Each step's input is the previous step's output. A missing/invalid output halts the chain — never run a downstream step on bad input. This is the whole point of mirroring `set -euo pipefail`.
- **One DATE, passed explicitly to all four children.** Resolve once in Step 0; never let children re-derive it.
- **Delegate, don't reimplement.** The orchestrator never dispatches research/writer/reviewer/rewriter agents directly. It only calls the four child skills via the Skill tool. All logic lives in them; this skill just sequences and gates.
- **Stop at the draft.** Like `draft.sh`, this ends *before* finalize and *before* the human review. Do not auto-run `/newsletter-finalize`. Do not start the paragraph-by-paragraph review — that's interactive and Gui-driven.
- **Idempotent resume.** Re-running picks up at the first incomplete step. To force a clean full rerun, delete the day-dir outputs you want regenerated (`research.json`, `pt.md`, `repetition.json`, `rewrite-notes.json`) — each child re-runs only when its output is gone.
- **Tight output.** Children self-report; the orchestrator narrates only the gate lines and the final roll-up. No step-by-step play-by-play.

## Why this exists

`draft.sh` chains four bash scripts with `set -euo pipefail` + `caffeinate` + a unified log, then stops and tells the user to review `pt.md` and run `finalize.sh`. The four scripts are now skills (`newsletter-research` / `-generate` / `-draft-review` / `-rewrite`). This skill is their orchestrator: **same order, same halt-on-failure, same stop-before-review hand-off** — but it sequences skills via the Skill tool instead of subprocesses, so each step runs natively in the conversation with its own parallel-agent dispatch and its own reporting. No tmux, no `run-agent.sh`, no `wait-for` polling.
