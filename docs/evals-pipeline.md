# Evals pipeline — replay, ground truth & scoring (2026-08-14)

The eval infrastructure in `evals/`. It breaks the once-per-day constraint: the content stages (facts → edition) can be replayed on frozen inputs as many times as needed, sandboxed, and scored against what actually got published. Findings that motivated it: [eval-findings.md](eval-findings.md).

## Layout

```
evals/
  run.sh                    # replay harness (sandboxed facts → edition → score)
  tools/
    extract_trace.py        # session JSONL → per-run trace (agents, wall, tokens)
    build_dataset.py        # ground-truth diffs vs the published Substack post
    score.py                # score any edition.md against a date's ground truth
  traces/<date>_<sid>.json  # one trace per daily run
  dataset/<date>/
    published-body.json     # cached pull of the published Substack body
    diff.json               # structured draft→final→published delta + advisory join
  runs/<date>__<variant>/   # replay outputs (research.json, facts.md, edition.md, score.json)
```

Principles: replay never touches production (no ingest, no Substack push, no Slack, no DB); ground truth is the **published** Substack body, never `edition-final.md` (which the pipeline itself writes — only links differ from `edition.md`); all scoring is against what Gui actually shipped.

## 1. Traces — where time/tokens go

```bash
python3 evals/tools/extract_trace.py --all          # every daily-run session
python3 evals/tools/extract_trace.py <session.jsonl>  # one session
```

Finds daily runs by the canonical Slack prompt ("rode o /newsletter-draft"), parses the parent session + its persisted subagent transcripts (`~/.claude/projects/…/<session-id>/subagents/agent-*.jsonl`), and writes one `evals/traces/<date>_<sid>.json` per run: every agent launch/completion with wall seconds, tokens by bucket (input/output/cache), tool counts, model; plus skill invocations, Bash steps, and the human prompts. Re-run after new editions to keep the profile current.

## 2. Ground truth — what the review changed

```bash
python3 evals/tools/build_dataset.py --pull                       # all dates
python3 evals/tools/build_dataset.py --pull --dates 2026-08-13    # one date
```

Per date, produces `evals/dataset/<date>/diff.json`:

- `draft_vs_final` — pipeline-internal delta (mostly the DJ link rewrite; ~0 real edits).
- `final_vs_published` — **the human review**: story cuts/adds, tier moves, title edits, and every bullet's before/after with similarity.
- `advisory` — each `fact-check.json` / `repetition.json` finding joined against the published text: `acted_on` = flagged text no longer present (heuristic; slightly inflated).

`--pull` fetches the current Substack body via `substack_mirror.py pull --id <.substack-draft-id>` (read-only, works post-publication) and caches it; without the cache the published layer is skipped. Pulls are cached — re-running without `--pull` is free and offline.

## 3. Replay — rerun content stages on frozen inputs

```bash
evals/run.sh <DATE> [VARIANT] [--stage facts|edition|score] [--from-facts]

evals/run.sh 2026-08-13 base                      # full: frozen research → facts → edition → score (~10 min)
evals/run.sh 2026-08-13 gen-v2 --from-facts       # generator-only: seeds production facts.md (~4 min)
MODEL=sonnet evals/run.sh 2026-08-13 gen-sonnet --from-facts   # model-tier ablation
```

What it does: copies the date's frozen `research.json` into `evals/runs/<DATE>__<VARIANT>/`, then dispatches the **registered** `facts` and `generator` agents via headless `claude -p` with the *same paths-only task prompts the `newsletter-draft` skill uses* — including the recent-Grandes / previous-edition context, computed from real history relative to the frozen date. Runs `link-tokens.py tokenize/expand` between stages exactly like production, applies the same gates (Fontes==sections; 1–3 Grandes), then scores.

- **Idempotent**: rerunning resumes at the first missing output; delete `facts.md`/`edition.md` in the run dir to force a stage.
- **Stages are separable**: `--stage facts` then `--stage edition` keeps each headless call under the Bash tool timeout.
- **Variants = agent definitions**: the harness runs whatever `.claude/agents/*.md` currently holds. To A/B a prompt change, edit the agent file (or use a git worktree) and name the variant accordingly — the run dir records nothing about the definition, so the variant name is your provenance.
- Per-stage transcripts land in the run dir (`facts.result.json`, `edition.result.json`) with the headless usage/cost data.

## 4. Scoring

```bash
python3 evals/tools/score.py <edition.md> --date 2026-08-13 [--json out.json]
```

Metrics vs the date's published ground truth:

| Metric | Meaning |
|---|---|
| `selection` P/R | precision = of what the candidate selected, how much shipped; recall = of what shipped, how much the candidate had |
| `tiering` | tier agreement (grandes/medias/leia) among matched stories |
| `structure` | Grandes count (1–3 cap), cluster count, bullets/Grande |
| `lexicon` | violations of the generator's hard lexicon rules (`generator.md` léxico line) + em-dash ban |
| `prose_sim` | mean bullet similarity to the published wording |

Calibration (so you know what "good" looks like): production editions score **P≈0.9, R=1.0, tiering 1.0, prose_sim≈0.98**; a wrong-day control collapses to P=0.17, prose_sim=0.09. A first live replay of 2026-08-13 scored P=0.75/R=0.79, tiering 1.0.

### Known caveats — read before comparing variants

1. **`prose_sim` structurally favors the production run**: the published text descends from production's wording, so an equally-good but differently-worded edition scores low. Compare variants on selection/tiering/lexicon; use prose_sim only within a lineage (e.g. same facts.md).
2. **Médias matching is label-based and noisy**: same story can carry different bullet labels ("Accelerant" vs "Thoma Bravo"), failing the match. P/R underestimates by ~0.1. Known fix: match stories via their source URLs back to `research.json` ids.
3. **Run-to-run variance is unmeasured** as of 2026-08-14 — run 3–5 `base` replays of one date to establish the noise band before reading any ablation delta as signal.

## 5. Ablation workflow

1. Pick a frozen date with ground truth (`evals/dataset/<date>/published-body.json` exists).
2. Run `base` replays until the metric noise band is known.
3. Make the change (agent prompt edit, `MODEL=`, stage rewrite), name the variant, replay — `--from-facts` when only the generator is under test.
4. Compare `score.json` against the base band; promote only deltas that clear it.
5. Promoted changes go to the real agent files; the next production run is the regression check (`build_dataset.py --pull` the day after extends the ground truth automatically).
