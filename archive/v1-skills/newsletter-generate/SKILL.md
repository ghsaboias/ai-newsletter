---
name: newsletter-generate
description: >-
  Gera o artigo PT-BR da newsletter de AI/Tech a partir do research.json do dia. Etapa 2 do pipeline (depois de newsletter-research, antes de newsletter-repetition-check). Lê as 3 últimas edições para evitar repetição upstream. Aciona quando o usuário diz "gerar a newsletter", "rodar generate", "criar o pt.md", "/newsletter-generate", ou pede explicitamente para gerar o draft. Substitui pipeline/generate.sh.
allowed-tools: Read, Write, Bash, Agent, Grep, Glob
---

## When this skill runs

User wants to generate today's PT-BR newsletter draft (`pt.md`) from an already-completed `research.json`. This is **step 2** of the pipeline:

1. `newsletter-research` → `research.json`
2. **`newsletter-generate`** → `pt.md` ← this skill
3. `newsletter-repetition-check` → `repetition.json`
4. `newsletter-rewrite` → `pt.md` (overwritten) + `rewrite-notes.json`

## Args

Invoked as `/newsletter-generate [args]`. Parse from user message:

- `YYYY-MM-DD` — generate for a specific date (overrides "today")
- (no args) — use today's date

No `mini` mode for generate — generation is single-pass already.

## Step 0: Establish the date

Run `date '+%Y-%m-%d %H:%M:%S %Z'` first. The system clock is the source of truth — don't assume the date from context.

Set `DATE` = today (or explicit arg).

## Step 1: Paths and idempotência

```
ROOT       = /Users/guilherme/ai-newsletter
DAY_DIR    = $ROOT/pipeline/output/ai/$DATE
RESEARCH   = $DAY_DIR/research.json
SLIM       = $DAY_DIR/research-slim.json
PT_FILE    = $DAY_DIR/pt.md
PROMPT_MD  = $ROOT/newsletters/ai/prompts/GENERATION.md
SLIM_TOOL  = $ROOT/pipeline/tools/slim_research.py
```

Checks:
- **`$PT_FILE` exists** → print word count and stop. Idempotente; user deletes to regenerate.
- **`$RESEARCH` missing** → stop with error. Run `/newsletter-research` first.

## Step 2: Slim the research

Run the slim tool, which strips excerpts/source metadata and dedupes:

```bash
python3 /Users/guilherme/ai-newsletter/pipeline/tools/slim_research.py /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE
```

This writes `research-slim.json` next to `research.json`. The slim file is what generation reads — never the full research.

## Step 3: Find the 3 previous editions

Find the **3 most recent existing** `pt.md` files before `$DATE` — by directory listing, not calendar walk. Calendar walking breaks when there are gaps (weekends, skipped days). Look at what's actually on disk:

```bash
ls -1 /Users/guilherme/ai-newsletter/pipeline/output/ai/*/pt.md 2>/dev/null \
  | awk -F'/' -v today="$DATE" '$(NF-1) < today { print $(NF-1), $0 }' \
  | sort -r \
  | head -3
```

Each line of the output is `YYYY-MM-DD /full/path/pt.md`. Format into the `PREV_LIST` string:

```
- 2026-05-18: /Users/guilherme/ai-newsletter/pipeline/output/ai/2026-05-18/pt.md
- 2026-05-15: /Users/guilherme/ai-newsletter/pipeline/output/ai/2026-05-15/pt.md
- 2026-05-14: /Users/guilherme/ai-newsletter/pipeline/output/ai/2026-05-14/pt.md
```

If the command returns 0 lines (first-ever edition), set `PREV_LIST` to `(nenhuma edição anterior encontrada)`.

## Step 4: Read and substitute the prompt template

Read `$PROMPT_MD` (the AI topic's GENERATION.md). Substitute placeholders:

- `{date}` → `$DATE`
- `{day_dir}` → `$DAY_DIR`
- `{prev_editions}` → the multi-line `PREV_LIST` from Step 3

The substituted text is the **system prompt** for the sub-agent.

## Step 5: Dispatch the writer sub-agent

Single Agent call. No parallelism needed — generation is one task.

```
Agent({
  description: "Generate newsletter draft for <DATE>",
  subagent_type: "general-purpose",
  prompt: "<substituted GENERATION.md content>\n\nWrite today's article for <DATE>. The research file is at <DAY_DIR>/research-slim.json. Read the 3 previous editions listed in the prompt before writing. Save to <PT_FILE>."
})
```

The sub-agent has Read/Write/Edit access. It:
1. Reads `research-slim.json`
2. Reads each of the 3 previous `pt.md` files (full, no skipping)
3. Writes `pt.md` following the structure/voice rules in GENERATION.md

## Step 6: Validate

After the sub-agent returns:

```bash
test -f /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE/pt.md || echo "ERROR: pt.md missing"
wc -w < /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE/pt.md
grep -oE 'https?://[^)]+' /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE/pt.md | sort -u | wc -l
```

No hard word-count target — comprimento é referência viva (as 3 edições anteriores). Validação é existência + plausibilidade básica do output.

## Step 7: Report

Print:
- Word count (informativo, não target)
- Unique link count
- Path to `pt.md`

Keep it tight — 3–5 lines. No narration of intermediate steps.

## Behavioral rules

- **Trust the system date.** Always `date` first.
- **The 3 previous editions are non-negotiable inputs**, not optional context. The sub-agent must read all 3 (when available) before writing. This is how we prevent the repetitions that the repetition-check step currently catches.
- **Idempotência first.** If `pt.md` exists, stop. The user re-runs by deleting.
- **No web access.** Generation reads `research-slim.json` and previous editions only. All facts and URLs come from research.
- **One sub-agent, not three.** Unlike newsletter-research, generation is not parallel. Don't try to split.

## Why this replaces generate.sh

The old `generate.sh` spawned a Claude CLI process in tmux, polled for the output file, signaled via `tmux wait-for`. Same orchestration bash overhead as research.sh. The skill collapses to: orchestrator runs a few Bash setup commands → dispatches one Agent → reports.

**Plus a real behavioral change**: the sub-agent now receives the 3 previous editions as required reading. The old script left generation blind to history, which is why `repetition-check` consistently finds 5 issues per edition. This change should cut those findings substantially (story/framing repeats become visible; phrasing repeats partially solved upstream).
