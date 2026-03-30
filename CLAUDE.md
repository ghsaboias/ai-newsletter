# Newsletter Platform

Multi-topic newsletter engine. Same pipeline, different configs. LLM handles facts, recency, accuracy. Human handles taste, writing, relevance. Learnings feed back into prompts so future generations need fewer corrections.

## Architecture

```
newsletters/
  ai/                          # AI & Tech newsletter (default)
    config.sh                  # clusters, byline, tools, title prefix
    prompts/                   # RESEARCH.md, GENERATION.md, SEEDS.md
    output/YYYY-MM-DD/         # (future: per-topic output)
pipeline/                      # topic-agnostic engine
  _lib.sh                      # loads topic config, shared utilities
  draft.sh / finalize.sh       # orchestrators
  research.sh / generate.sh    # steps (read config, not hardcode)
  prompts/                     # shared: AUDIT.md, REPETITION_CHECK.md, SOURCE_EXTRACTION.md
```

All scripts default to `--topic ai`. Override with `PIPELINE_TOPIC=ma` env var or `--topic ma` arg (when wired).

## Pipeline

Two-phase pipeline. Draft generates and quality-checks. You review with Claude and fix pt.md. Finalize handles mechanical post-processing.

```
pipeline/draft.sh [YYYY-MM-DD]                 # Phase 1: Research → Generate → Repetition check → Audit
                                                #   (review repetition.json + audit.json, fix pt.md)
pipeline/finalize.sh YYYY-MM-DD [--execute]    # Phase 2: Extract → Ingest → Rewrite links → Substack
```

### Phase 1: draft.sh

Runs four sequential steps, each a separate Claude process:

1. `research.sh` — web research → `research.json`
2. `generate.sh` — PT-BR article from research data → `pt.md`
3. `repetition-check.sh` — compare against previous 3 editions → `repetition.json`
4. `audit.sh` — freshness check (flags stale news) → `audit.json`

After draft completes, open a Claude session to review repetition.json + audit.json and fix pt.md. **Read memory files first**: `~/.claude/projects/-Users-guilherme-ai-newsletter/memory/`

### Phase 2: finalize.sh

Runs four mechanical steps (no human judgment needed):

1. `extract.sh` — extract sources from research + article → `sources.json`
2. `ingest.sh` — ingest into DB → `links.json` (dry-run by default, `--execute` to write)
3. `rewrite-links.sh` — replace URLs with DJ links → `final.md`
4. `substack.sh` — convert to Substack HTML → `substack.html`

### Notes

Topic prompts: `newsletters/<topic>/prompts/` (RESEARCH.md, GENERATION.md, SEEDS.md)
Shared prompts: `pipeline/prompts/` (AUDIT.md, REPETITION_CHECK.md, SOURCE_EXTRACTION.md)
Topic config: `newsletters/<topic>/config.sh` (clusters, byline, tools, pre-research)
Output: `pipeline/output/YYYY-MM-DD/`

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

## Publishing

Drop a new markdown file into `posts/_posts/` with the naming convention `YYYY-MM-DD-title.md`. Push. Auto-deploys.

Frontmatter:

```yaml
---
layout: post
date: YYYY-MM-DD
title: "Welcome to Month Day, Year"
---
```
