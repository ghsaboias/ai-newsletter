# Newsletter Platform

Multi-topic newsletter engine. Same pipeline, different configs. LLM handles facts, recency, accuracy. Human handles taste, writing, relevance. Learnings feed back into prompts so future generations need fewer corrections.

## Architecture

```
newsletters/
  ai/                          # AI & Tech newsletter (default)
    config.sh                  # clusters, byline, tools, title prefix
    prompts/                   # RESEARCH.md, GENERATION.md, SEEDS.md
  ma/                          # M&A newsletter
    config.sh                  # deals, regulatory, advisors clusters
    prompts/                   # M&A-specific voice, structure, editorial
pipeline/                      # topic-agnostic engine
  _lib.sh                      # loads topic config, shared utilities
  draft.sh / finalize.sh       # orchestrators
  research.sh / generate.sh    # steps (read config, not hardcode)
  prompts/                     # shared: REPETITION_CHECK.md, SOURCE_EXTRACTION.md
  output/<topic>/YYYY-MM-DD/   # namespaced by topic
  logs/<topic>/                # namespaced by topic
```

All scripts default to `--topic ai`. Override with `PIPELINE_TOPIC=ma` env var or `--topic ma` arg (when wired).

## Pipeline

Two-phase pipeline. Draft generates and quality-checks. You review with Claude and fix pt.md. Finalize handles mechanical post-processing.

```
pipeline/draft.sh [YYYY-MM-DD]                 # Phase 1: Research → Generate → Repetition check → Draft rewrite
                                                #   (review pt.md paragraph by paragraph)
pipeline/finalize.sh YYYY-MM-DD [--execute]    # Phase 2: Extract → Ingest → Rewrite links → Substack
```

### Phase 1: draft.sh

Runs four sequential steps, each a separate Claude process:

1. `research.sh` — web research → `research.json`
2. `generate.sh` — PT-BR article from research data → `pt.md`
3. `repetition-check.sh` — compare against previous 3 editions → `repetition.json`
4. `draft-rewrite.sh` — apply repetition findings surgically → `pt.md` (overwritten), `pt-original.md` (backup), `rewrite-notes.json`

After draft completes, open a Claude session to review pt.md. Flow: Claude presents the subtitle for Gui's review → Gui comments → when Gui says move on, Claude presents paragraph 1 → and so on through the article. One block at a time, Gui drives the pace. **Read memory files first**: `~/.claude/projects/-Users-guilherme-ai-newsletter/memory/`

### Phase 2: finalize.sh

Runs four mechanical steps (no human judgment needed):

1. `extract.sh` — extract sources from research + article → `sources.json`
2. `ingest.sh` — ingest into DB → `links.json` (dry-run by default, `--execute` to write)
3. `rewrite-links.sh` — replace URLs with DJ links → `final.md`
4. `substack.sh` — convert to Substack HTML → `substack.html`

### Notes

Topic prompts: `newsletters/<topic>/prompts/` (RESEARCH.md, GENERATION.md, SEEDS.md)
Shared prompts: `pipeline/prompts/` (REPETITION_CHECK.md, SOURCE_EXTRACTION.md)
Topic config: `newsletters/<topic>/config.sh` (clusters, byline, tools, pre-research)
Output: `pipeline/output/<topic>/YYYY-MM-DD/`

Each step skips if output already exists. Delete the output file to rerun.

### Prompt sampling

`pipeline/sample.sh` runs a prompt N times against existing data to compare outputs. Useful for calibrating prompt wording before committing to a full run.

```
pipeline/sample.sh generate 2026-03-03              # 5 samples (default)
pipeline/sample.sh generate 2026-03-03 -n 10        # 10 samples
pipeline/sample.sh generate 2026-03-03 -q "Write only the opening and closing lines."
pipeline/sample.sh source_extraction 2026-03-03 -q "List the 5 most important stories."
```

Saves to `pipeline/output/samples/` and prints all results at the end.

## Editorial Principles

1. **Freshness honesty** — never imply simultaneity between stories from different dates. Use "Separadamente" or acknowledge timing explicitly.
2. **No political editorializing** — don't frame political positions as deficiencies. Present facts neutrally.
3. **Explain jargon inline** — acronyms get brief parenthetical explainers on first use (RLHF, ARR, TCEQ). Technical terms like "yield" need plain-language rewrites.
4. **Clarity of reference** — vague terms need specifics ("plataformas" → "redes sociais"). Pronouns and verbs must be unambiguous about who does what to whom.
5. **Say what the company does** — don't assume the reader knows. One clause is enough.
7. **Repetition = reframe, not repeat** — if a number or narrative ran in recent editions, convey continuity or find the genuinely new angle. Don't present stale facts as fresh.
8. **Paragraph coherence** — stories live with their thematic neighbors. China trade investigations go with US-China tech friction, not the Iran thread.
9. **Kill low-signal items** — cut quotes and stories that add noise, not signal. No guilt.

## Review Workflow

1. **One finding at a time** — present context, get a decision, move on. Don't batch.
2. **Always show updated text after every change** — no exceptions.
3. **"Unclear" = propose 3 rewrites** — don't explain, don't ask what's wrong, just offer options.
4. **Don't fix until told** — flag, discuss, get approval, then edit.
5. **Show full text without links for proofreading** — links are visual noise when reviewing prose.
6. **Spell things out** — show the before, show the after, show what changed. Don't summarize.
7. **3-5 options at decision points** — Guilherme picks. He has strong taste and drives.
8. **Portuguese precision** — gender agreement (elas not eles), prepositions (na *Science* not em *Science*), cadence matters as much as content.
9. **Cadence is real** — if a sentence is technically correct but reads clunky, restructure: invert order, break into shorter sentences, vary rhythm.

## Adding a New Topic

1. `cp -r newsletters/ai newsletters/<topic>`
2. Edit `config.sh`: clusters, byline, title prefix, allowed tools, pre-research command
3. Edit prompts: voice, structure, domain rules
4. Run: `PIPELINE_TOPIC=<topic> pipeline/draft.sh`

## vibe-review (prototype)

Web UI for the draft review loop. Prototype — under active testing, expect rough edges.

Location: `~/tools/vibe-review/` (sibling to `ai-newsletter`; server `cwd`s into this repo so CLAUDE.md and memory load automatically).

Run: `cd ~/tools/vibe-review && npm start` → http://localhost:4175/review/YYYY-MM-DD.

Backend spawns `claude --print --output-format stream-json --resume <id>` per turn; session id persisted to `pipeline/output/ai/<date>/.review-session`.

## Posts (charts for Substack/social)

`posts/` holds per-edition chart HTML + JSON research data. Charts promote a specific edition; data is auditable.

Pattern:
1. Research data first. Save to `posts/data/<slug>.json` with `sources` (label + url) and `notes` (what's measured vs. estimated).
2. Build chart at `posts/chart-<slug>.html`. Self-contained. Chart.js via CDN. `animation: false`, `tooltip: { enabled: false }`.
3. Portuguese titles, source line, captions.

Brand:
- 720px card, `padding: 36px 40px`, white background
- H1: Helvetica Neue, 24px, weight 700, `letter-spacing: -0.8px`
- Header: title only, full width (`max-width: none`); `border-bottom: 3px solid #044B2E`. The DJ logo is NOT in the header (a header logo steals width and wraps long titles) — it goes inside the chart, see Logo below
- Footer: source label left, `dailyjournal.news` right; 10px, `#999`; `border-top: 1px solid #E5E5E5`
- Palette: `#044B2E` primary, `#7DB89B` projection/forecast, `#0012bf` `#D7001E` `#E88E00` `#E4ABEB` `#ccc` for multi-series

Logo: `<img src="../../daily-journal-platform/public/images/logo/logo-green-horizontal.png">`, placed *inside* the chart as a watermark — an absolutely-positioned `.chart-logo` (height ~15px) inside the `position:relative` `.chart-container`. Default bottom-right; move it to whichever plot quadrant is empty (visual judgment after rendering — a climbing series leaves the bottom-right open; a falling/left-heavy one needs it elsewhere). Align it to the plot, don't eyeball: measure with browser-eval (`Chart.getChart('<id>').chartArea` + the container's clientWidth/Height), then for bottom-right set `right = containerW − chartArea.right` (logo's right edge meets the x-axis line's end) and `bottom = containerH − chartArea.bottom + ~12` (a gap above the axis line). Canonical asset lives in daily-journal-platform; never duplicate into ai-newsletter.

Annotations: label endpoints and milestones only, not every bar. Use a Chart.js `afterDraw` plugin to draw value labels above bars.

Two-panel pattern works for time-series: long arc (annual) on top, recent acceleration (monthly) below — different time signatures, same y-axis unit.
