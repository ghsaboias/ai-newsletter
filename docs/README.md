# docs/

Git-tracked, synced-across-devices home for the newsletter's accumulated knowledge — consolidated 2026-07-10 from the per-machine Claude Code memory folders (`~/.claude/projects/…-ai-newsletter/memory/`), which had **diverged**: 29 editorial/workflow memories lived only on the Mac, 7 operational ones only on the Pi. Nothing was dropped in the merge.

| File | What it is |
|---|---|
| [editorial-principles.md](editorial-principles.md) | The distilled, deduplicated **voice/writing spec** — PT-BR language, jargon, trimming, framing, structure, link boundaries, paywall teasers, tiering, accuracy, and the review working-style. The actionable rules. |
| [editorial-review-log.md](editorial-review-log.md) | The dated **provenance** behind the principles — each review session's specific draft→final edits, kept for their before→after examples (2026-03-09 → 2026-07-01). |
| [newsletter-workflow.md](newsletter-workflow.md) | The **publishing machinery** — the publish gap, per-story images (selection + `substack_mirror.py` insertion), the recommendations section + archive cron, chart posts, the Substack API/format reference, the v2 restructure, coverage direction. |
| [operational-notes.md](operational-notes.md) | **Headless/harness** quirks — Bash bg-tasks dying at turn end, `sstats` running anywhere, nested subagents. The bucket destined for the Pi's `CLAUDE.md`. |
| [search-provider-benchmark.md](search-provider-benchmark.md) | The **research-step search layer** — o que os agentes de research realmente chamam (baseline medido), o que Exa/WebSearch/Firecrawl sabem fazer (filtro de data, parâmetros, custo), e o desenho do benchmark. Bloqueado até 2026-08-16. |
| [eval-findings.md](eval-findings.md) | **What instrumenting the pipeline found** (2026-08-14) — wall/token profile per stage (extract is the long pole; orchestrator ≈ half the spend), the ground-truth discovery (`edition-final.md` ≠ reviewed; published Substack body is), what the review actually edits (38% of bullets, ~zero selection/tiering changes), advisory acted-on rates, and the optimization queue. |
| [evals-pipeline.md](evals-pipeline.md) | **The evals infrastructure and how to use it** — `evals/` layout, trace extractor, ground-truth dataset builder, the sandboxed replay harness (`evals/run.sh`, unlimited reruns/day, no production writes), the scorer and its calibration numbers, metric caveats, and the ablation workflow. |

## Relationship to CLAUDE.md and memory

- **`CLAUDE.md` (repo) is the source of truth for the *current* pipeline** (the `research → facts → edition` agent chain). These docs are the accumulated *detail and learnings* behind it — some captured against the older prose pipeline and dated accordingly.
- The Claude Code **memory folders still exist** on each machine and remain the ad-hoc write path for now. Planned follow-ups (not done in this first pass): add pointers from `CLAUDE.md` to these docs; add an operational/headless section to the Pi's `CLAUDE.md` from `operational-notes.md`; then retire the divergent memory folders in favor of this git-tracked home.

## Editing

Point-in-time file/line citations may go stale — verify against current code before relying on a specific path or flag. When a review session or a new learning lands, update the relevant doc here (and the `editorial-review-log.md` for dated deltas) rather than writing a new one-off memory file.
