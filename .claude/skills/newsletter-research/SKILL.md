---
name: newsletter-research
description: >-
  Roda a etapa de research da newsletter de AI/Tech. Pesquisa as notícias do dia em 3 clusters paralelos (ai, hw, world) usando os 3 sub-agentes especialistas (researcher-ai/-hw/-world, cada um com seu beat de-conflitado no próprio system prompt), depois mergeia com dedup semântico (pipeline/tools/dedup-research.py) num único research.json. Substitui pipeline/research.sh. Aciona quando o usuário diz "rodar research", "pesquisa do dia", "research da newsletter", "/newsletter-research", ou pede explicitamente para rodar a pesquisa. Aceita flag `mini` para teste rápido (1 cluster, 3 stories).
allowed-tools: Read, Write, Bash, Agent
---

The 3 specialist agents own the research methodology (beat, de-confliction, key
accounts) in their own system prompts. This skill is the thin orchestrator: pick
the window, build the one shared brief file, dispatch the 3 specialists **in one
message**, merge. It does **not** inject cluster categories — that lives in the agents.

## When this skill runs

User wants to research today's news for the AI/Tech newsletter — the first step of the pipeline, before the facts/edition agents.

## Args

Invoked as `/newsletter-research [args]`. Parse from the user message:

- `mini` — **mini mode**: run only the `ai` cluster with a 3-story cap. For testing.
- `YYYY-MM-DD` — research for a specific date (overrides "today").
- (no args) — today's date, all 3 clusters.

## Step 0: Establish the date

**Before anything else**, run `date '+%Y-%m-%d %H:%M:%S %Z'`. The system clock is the source of truth — don't trust dates assumed from context.

Set `DATE` = today (YYYY-MM-DD) unless the user passed an explicit date. The
research window (`PREV_DATE 10:00 BRT` → `DATE 10:00 BRT`, where `PREV_DATE` is
the most recent earlier day that has a `research.json`) is resolved by the brief
script in Step 2 — you don't compute it.

## Step 1: Paths and idempotency

```
REPO     = $(git -C "$(dirname "$0")" rev-parse --show-toplevel)   # the repo root; on the Pi: /home/guilhermesaboia/ai-newsletter
DAY_DIR  = $REPO/pipeline/output/ai/$DATE
OUTFILE  = $DAY_DIR/research.json
```

`mkdir -p "$DAY_DIR"`. **If `$OUTFILE` already exists**: print its story/source count and stop. Idempotent — the user deletes it to re-run.

## Step 2: Build the shared brief (ONE file, ONE fetch)

The brief is everything the three specialists used to receive inline —
`RESEARCH.md` with the window substituted, the previous edition's headlines, the
Techmeme scan, and the mini cap. It is built **once**, by a script, into a file
the agents `Read` as their first action:

```bash
BRIEF=$(bash "$REPO/pipeline/tools/research-brief.sh" "$DATE")          # append " mini" in mini mode
[ -s "$BRIEF" ] && echo "OK brief: $BRIEF" || echo "HALT: brief not written"
```

It prints the brief path (`$DAY_DIR/research-brief.md`) and, on stderr, a summary
(size, `PREV_DATE`, Techmeme bytes). It also writes `$DAY_DIR/techmeme.md` (the
audit copy; reused on a re-run). If the Techmeme fetch failed the brief says so
and the agents rely on their own searches — that is not a HALT.

**Why a file, not inline text.** Pasting the ~26KB brief into each Agent prompt
made the orchestrator *type* it three times, one call per turn, so the three
"parallel" dispatches actually went out 1–5 minutes apart (measured on every
September 2026 run). With the brief on disk each Agent prompt is four lines, the
three calls fit in one message, and the specialists' own system prompts make the
`Read` mandatory before any search.

`HALT` → stop; do not dispatch.

## Step 3: Dispatch the 3 specialists in parallel — one message

Each cluster has a registered specialist whose system prompt carries its beat +
de-confliction and the rule to `Read` the brief first:

| cluster | `subagent_type` |
|---|---|
| `ai`    | `researcher-ai` |
| `hw`    | `researcher-hw` |
| `world` | `researcher-world` |

- **Normal mode**: `ai`, `hw`, `world` (3 agents)
- **Mini mode**: only `researcher-ai` (1 agent)

### Per-cluster prompt (short — the brief carries the rest)

```
Date: <DATE>.
Brief (READ THIS FILE FIRST, in full, before any search): <BRIEF>
Output file: <DAY_DIR>/research-<name>.json

Write the JSON to the output file path above, copied character-for-character. Honor your beat boundaries — do not spend a slot on a story that belongs to a sibling cluster. Do not invent URLs — every source must come from a search result or fetched page.
```

### Agent call shape

For each cluster `<name>` ∈ {ai, hw, world}, with `<type>` the matching specialist:

```
Agent({
  description: "Research cluster: <name>",
  subagent_type: "<type>",            // researcher-ai | researcher-hw | researcher-world
  prompt: "<the per-cluster prompt above>"
})
```

**All three `Agent` calls go in ONE assistant message** — that is the whole point
of Step 2. Never emit them one per turn. The specialist already has
`mcp__exa__web_search_exa`, `mcp__exa__web_fetch_exa`, `Read`, `Write`, `Bash`.
It writes `research-<name>.json` and returns a one-line summary (`<name> — N stories`).

## Step 4: Merge (semantic dedup)

After the agents return, collect the partials and verify each is valid JSON (`jq empty`); skip + warn on any invalid. If **zero** valid partials exist, stop with an error.

Merge with the semantic-dedup tool (catches the same story slugged differently across clusters — which plain `unique_by(.id)` misses — and reports cross-cluster overlap):

```bash
D="$REPO/pipeline/output/ai/$DATE"
python3 "$REPO/pipeline/tools/dedup-research.py" "$DATE" "$D/research.json" \
  ai:"$D/research-ai.json" hw:"$D/research-hw.json" world:"$D/research-world.json"
```

Pass one `cluster:file` arg **per valid partial only** — drop any cluster that failed. In mini mode pass just `ai:...`. The tool writes `research.json` (deduped, with `story_count`/`source_count`) and prints how many dups it collapsed, tagged intra/CROSS. **A non-zero CROSS count means the beats are drifting** — surface it.

## Step 5: Report

One tight block, no narration of internal steps:
- Total stories / sources
- Cross-cluster duplicates collapsed (expect 0; flag if >0)
- Headlines (`jq -r '.stories[] | "  • " + .headline' research.json`)
- Which clusters succeeded / failed

## Behavioral rules

- **Trust the system date.** Run `date` first; never assume it from prior context.
- **Parallel dispatch is non-negotiable** in normal mode — three Agent calls in one message. The brief file exists so that this is cheap; don't paste its contents into the prompts.
- **Don't read the brief yourself** — it's for the agents. The orchestrator only needs the path.
- **Don't read the sub-agent's verbose output back into context.** Each returns a one-line summary; trust the JSON on disk.
- **Idempotência first.** If `research.json` exists, do nothing.
- **No comments in the JSON.** The shape must match the schema in `RESEARCH.md`.

## Verifying the dispatch (no eval harness needed)

Two checks on the session's JSONL after a run — the pipeline trace already
measures the first:

- `python3 evals/tools/extract_trace.py <session.jsonl>` → the three
  `researcher-*` agents must share the same `launched_at` minute (spread ≈ 0).
- In each `subagents/agent-*.jsonl` the first `tool_use` must be `Read` on
  `research-brief.md`, before any `mcp__exa__web_search_exa`.

## Testing

Fast smoke test — runs only `researcher-ai` with a 3-story cap (~3 min), produces `research.json` with `story_count: 3`:

```
/newsletter-research mini
```

Full run: `/newsletter-research` (or `/newsletter-research 2026-05-19` for a specific date).
