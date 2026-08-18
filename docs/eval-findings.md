# Eval findings — pipeline profile & ground truth (2026-08-14)

What we learned instrumenting the daily `/newsletter-draft` → `/newsletter-images` → `/newsletter-recs` flow. Sources: 34 daily-run session JSONLs (2026-07-06 → 2026-08-14, 29 complete runs) traced with `evals/tools/extract_trace.py`, and 34 editions of ground truth built with `evals/tools/build_dataset.py`. See [evals-pipeline.md](evals-pipeline.md) for the tooling itself.

## 1. Where the time goes

Critical path from the Slack prompt to the pushed Substack draft: **~30–35 min**, nearly all sequential. Medians across 29 runs:

| Phase | Median wall | Notes |
|---|---|---|
| Prompt → researchers launched | 2.5 min | Techmeme scan + setup; agent launches staggered 40–90s apart |
| Research (3 agents, parallel) | 8.2 min | Bounded by the slowest cluster |
| Facts | 4.4 min | |
| Edition (generator) | 3.0 min | |
| **Extract → sources.json** | **8.7 min** | Launched with the generator, but generator finishes in 3 min — extract adds **~5 min of pure wait** to the push |
| Ingest → cluster review → rewrite → push | ~6 min | Includes the orchestrator hand-reviewing cluster candidates |
| Images | ~8–10 min | After the push; ~9 parallel image agents |
| Recs | ~3 min | |

Per-stage medians (wall seconds / output tokens / cache-read tokens):

| Stage | n | wall | out tok | cache read |
|---|---|---|---|---|
| extract | 31 | 524s | 43.9k | 0.6M |
| researcher-world | 28 | 310s | 26.5k | 1.2M |
| researcher-ai | 28 | 301s | 24.3k | 1.0M |
| researcher-hw | 28 | 270s | 21.7k | 1.0M |
| facts | 28 | 266s | 22.2k | 0.2M |
| fact-verifier | 35 | 227s | 16.3k | 1.4M |
| generator | 28 | 180s | 14.2k | 0.1M |
| repetition-checker | 32 | 163s | 11.4k | 0.1M |
| paywall-teaser | 23 | 59s | 4.0k | 0.1M |
| image agents | 41 | 87s | 4.5k | 1.0M |

## 2. Cost profile

- **The orchestrator (main loop) is ~half the total spend**: 200–390k output tokens and 15–28M cache-read tokens per run — comparable to all subagents combined (~200k out). It burns turns on staggered agent launches, gate checks, and the ingest cluster review.
- **`extract` is the single worst stage**: slowest (median 8.7 min), biggest output (44k tokens — double any researcher), and its job is largely a mechanical URL join between `facts.md` Fontes blocks and `research.json` metadata. Top candidate to become a script with a small LLM pass for the PT-BR summary fields: ~5 min off the critical path and ~20% of subagent tokens.
- Research is already parallel; its 8 min are hard to compress without touching quality.

## 3. Ground truth: what the human review actually changes

Key discovery: **`edition-final.md` is NOT the reviewed version.** It differs from `edition.md` only by the DJ link rewrite — the pipeline writes it. The real review delta is edition-final vs the **published Substack body** (pulled read-only via `substack_mirror.py pull --id <.substack-draft-id>`; works after publication).

Across 34 editions (edition-final vs published):

- **Wording, not selection**: 334/880 bullets edited (**38%**, median 10/edition) — trims, rewording, de-jargonizing.
- **Selection & tiering already match taste**: 14 story cuts total (~0.4/edition), additions ≈ 0, tier moves **zero** in 34 editions.
- Implication: the residual quality gap is prose-level; selection/tiering changes should be evaluated mostly as regression risks, not improvement targets.

## 4. Advisory checks earn their keep

Measured by "flagged text no longer present in the published post" (text-presence heuristic — inflates somewhat, since bullets also get trimmed for unrelated reasons):

| Check | Acted on |
|---|---|
| fact-verifier, high severity | 5/5 |
| fact-verifier, all | 77/87 (~89%) |
| repetition-checker, lexicon | 34/34 (100%) |
| repetition-checker, all | 175/264 (~66%) |

High-severity fidelity flags clearly track real edits (e.g. 2026-08-13: the invented "Marinha/Golfo de Omã" specificity was flagged, and the Ormuz story died in review). **Do not ablate these agents.** The cheap win is the opposite direction: lexicon violations are fixed by hand 100% of the time, so making the generator obey the lexicon upfront (and/or auto-applying `apply-lexicon.py` pre-push) removes that whole class of review work.

## 5. Session/transcript facts worth keeping

- Subagent transcripts **persist indefinitely** at `~/.claude/projects/-home-guilhermesaboia-ai-newsletter/<session-id>/subagents/agent-*.jsonl` — only the `/tmp` symlinks die. Full history stays minable; no archiving cron needed.
- Async agent completions appear in the parent transcript as `<task-notification>` user entries; launches are `Agent` tool_use entries. Wall time per stage = notification ts − launch ts.
- From 2026-07-31 the daily session grew ~600KB → 6–8MB: images + recs (and the review chatter) now share the draft session.

## 6. Optimization queue (as of 2026-08-14)

1. **Establish replay noise band** — 3–5 `base` replays of one date before trusting any ablation delta.
2. **URL-based story matching in the scorer** — kills Médias label noise (~0.1 P/R underestimate).
3. **extract → deterministic script** + small LLM pass (biggest single win: ~5 min + ~20% subagent tokens).
4. **Generator lexicon compliance upfront** (prompt already has the rules; measure violations/edition via the scorer, tighten until 0).
5. **Model-tier ablation** for generator/facts (`MODEL=sonnet evals/run.sh <date> <variant> --from-facts`).
6. **Orchestrator thinning** — more deterministic glue in the skill's gate/launch steps.
