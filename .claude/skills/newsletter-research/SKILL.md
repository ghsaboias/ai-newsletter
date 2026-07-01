---
name: newsletter-research
description: >-
  Roda a etapa de research da newsletter de AI/Tech. Pesquisa as notícias do dia em 3 clusters paralelos (ai, hw, world) usando os 3 sub-agentes especialistas (researcher-ai/-hw/-world, cada um com seu beat de-conflitado no próprio system prompt), depois mergeia com dedup semântico (pipeline/tools/dedup-research.py) num único research.json. Substitui pipeline/research.sh. Aciona quando o usuário diz "rodar research", "pesquisa do dia", "research da newsletter", "/newsletter-research", ou pede explicitamente para rodar a pesquisa. Aceita flag `mini` para teste rápido (1 cluster, 3 stories).
allowed-tools: Read, Write, Bash, Agent
---

The 3 specialist agents own the research methodology (beat, de-confliction, key
accounts) in their own system prompts. This skill is the thin orchestrator: pick
the window, fetch the one shared input (Techmeme), dispatch the 3 specialists,
merge. It does **not** inject cluster categories — that lives in the agents.

## When this skill runs

User wants to research today's news for the AI/Tech newsletter — the first step of the pipeline, before `pipeline/generate.sh`.

## Args

Invoked as `/newsletter-research [args]`. Parse from the user message:

- `mini` — **mini mode**: run only the `ai` cluster with a 3-story cap. For testing.
- `YYYY-MM-DD` — research for a specific date (overrides "today").
- (no args) — today's date, all 3 clusters.

## Step 0: Establish the research window

**Before anything else**, run `date '+%Y-%m-%d %H:%M:%S %Z'`. The system clock is the source of truth — don't trust dates assumed from context.

Set:
- `DATE` = today (YYYY-MM-DD) unless the user passed an explicit date
- `PREV_DATE` = day before `DATE` (`date -j -v-1d -f "%Y-%m-%d" "$DATE" "+%Y-%m-%d"` on macOS)
- Research window = `PREV_DATE 10:00 BRT` → `DATE 10:00 BRT` (24h)

All 3 agents must research this **same** window — that's why it's computed once here.

## Step 1: Paths and idempotency

```
ROOT       = /Users/guilherme/ai-newsletter
DAY_DIR    = $ROOT/pipeline/output/ai/$DATE
PREV_DIR   = $ROOT/pipeline/output/ai/$PREV_DATE
OUTFILE    = $DAY_DIR/research.json
RESEARCH_PROMPT_FILE = $ROOT/newsletters/ai/prompts/RESEARCH.md
DEDUP      = $ROOT/pipeline/tools/dedup-research.py
TECHMEME   = python3 $ROOT/pipeline/tools/techmeme.py
```

`mkdir -p "$DAY_DIR"`. **If `$OUTFILE` already exists**: print its story/source count and stop. Idempotente — the user deletes it to re-run.

## Step 2: Previous headlines (dedup hint)

If `$PREV_DIR/research.json` exists, extract `id: headline` lines to inline into each agent's prompt as "skip unless genuinely new":

```bash
jq -r '.stories[] | "- " + .id + ": " + .headline' "$PREV_DIR/research.json"
```

If the file doesn't exist, leave the section empty.

## Step 3: Techmeme scan (fetch once, inline)

Fetch the landscape scan **once** in text mode and `tee` it to an audit copy. One fetch, shared by all 3 agents — keeps them looking at the same landscape and avoids 3× the fetch:

```bash
python3 /Users/guilherme/ai-newsletter/pipeline/tools/techmeme.py 2>/dev/null \
  | tee "$DAY_DIR/techmeme.md" \
  || echo "[Techmeme fetch failed]"
```

~16KB, one block per story. **Paste it inline** into every cluster prompt (Step 5) — the agent must receive it directly, never be told to read it from a file (inline scans are used; file pointers get skipped/paginated). If the fetch returns empty, tell the agents no scan is available.

## Step 4: Read the research prompt

```
Read /Users/guilherme/ai-newsletter/newsletters/ai/prompts/RESEARCH.md
```

Substitute `{{DATE}}` and `{{PREV_DATE}}` with the actual values. This is the shared methodology/rules/tool-guide/blocklist/schema — every cluster gets it; the per-cluster **beat** comes from the specialist agent, not here.

## Step 5: Dispatch the 3 specialists in parallel

The core. **In a single message, fire one `Agent` call per cluster** so they run concurrently. Each cluster has a registered specialist whose system prompt carries its beat + de-confliction (what it owns vs. what to leave to siblings — e.g. an AI-lab's inference chip → `hw`, a chip/robotics IPO → `hw` not `world`):

| cluster | `subagent_type` |
|---|---|
| `ai`    | `researcher-ai` |
| `hw`    | `researcher-hw` |
| `world` | `researcher-world` |

- **Normal mode**: `ai`, `hw`, `world` (3 agents)
- **Mini mode**: only `researcher-ai` (1 agent)

### Per-cluster prompt template

Build each prompt with actual values (note: **no "Your categories" block** — the beat is in the agent's own system prompt):

```
<RESEARCH_PROMPT with {{DATE}} and {{PREV_DATE}} substituted>

---
**Date:** <DATE>
**Output file:** /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/research-<name>.json

**Previous edition headlines (skip unless genuinely new development):**
<previous-headlines or "(none)">

**Pre-research scan:** (review before searching — full Techmeme text pasted below; do not read a file for it)
<full techmeme text from Step 3, pasted verbatim>
```

**Mini mode** — append only when the `mini` flag is set:

```

**MINI MODE: Return at most 3 stories. Pick the 3 most important.**
```

### Agent call shape

For each cluster `<name>` ∈ {ai, hw, world}, with `<type>` the matching specialist:

```
Agent({
  description: "Research cluster: <name>",
  subagent_type: "<type>",            // researcher-ai | researcher-hw | researcher-world
  prompt: "<the full per-cluster prompt above>\n\nWrite the JSON to the output file path given above, copied character-for-character. Honor your beat boundaries — do not spend a slot on a story that belongs to a sibling cluster. Do not invent URLs — every source must come from a search result or fetched page."
})
```

The specialist already has `mcp__exa__web_search_exa`, `mcp__exa__web_fetch_exa`, `Read`, `Write`, `Bash`. It writes `research-<name>.json` and returns a one-line summary (`<name> — N stories`). **Fire all clusters in one message** — never await them sequentially.

## Step 6: Merge (semantic dedup)

After the agents return, collect the partials and verify each is valid JSON (`jq empty`); skip + warn on any invalid. If **zero** valid partials exist, stop with an error.

Merge with the semantic-dedup tool (catches the same story slugged differently across clusters — which plain `unique_by(.id)` misses — and reports cross-cluster overlap):

```bash
python3 /Users/guilherme/ai-newsletter/pipeline/tools/dedup-research.py <DATE> \
  /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/research.json \
  ai:/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/research-ai.json \
  hw:/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/research-hw.json \
  world:/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/research-world.json
```

Pass one `cluster:file` arg **per valid partial only** — drop any cluster that failed. In mini mode pass just `ai:...`. The tool writes `research.json` (deduped, with `story_count`/`source_count`) and prints how many dups it collapsed, tagged intra/CROSS. **A non-zero CROSS count means the beats are drifting** — surface it.

## Step 7: Report

One tight block, no narration of internal steps:
- Total stories / sources
- Cross-cluster duplicates collapsed (expect 0; flag if >0)
- Headlines (`jq -r '.stories[] | "  • " + .headline' research.json`)
- Which clusters succeeded / failed

## Behavioral rules

- **Trust the system date.** Run `date` first; never assume it from prior context.
- **Parallel dispatch is non-negotiable** in normal mode — three Agent calls in one message.
- **Don't read the sub-agent's verbose output back into context.** Each returns a one-line summary; trust the JSON on disk.
- **Idempotência first.** If `research.json` exists, do nothing.
- **No comments in the JSON.** The shape must match what `generate.sh` expects (see RESEARCH.md schema).

## Testing

Fast smoke test — runs only `researcher-ai` with a 3-story cap (~3-5 min), produces `research.json` with `story_count: 3`:

```
/newsletter-research mini
```

Full run: `/newsletter-research` (or `/newsletter-research 2026-05-19` for a specific date).
