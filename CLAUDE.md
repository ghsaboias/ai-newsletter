# AI Newsletter

The pipeline is recursive self-improvement. LLM handles facts, recency, accuracy. Human handles taste, writing, relevance. Learnings feed back into prompts so future generations need fewer corrections.

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

Prompts: `pipeline/prompts/` (RESEARCH.md, GENERATION.md, REPETITION_CHECK.md, AUDIT.md, SOURCE_EXTRACTION.md)
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
