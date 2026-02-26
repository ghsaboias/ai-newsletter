# AI Newsletter

Public Jekyll site for Fast Takeoff. Deploys to GitHub Pages via Actions.

## Pipeline

Full newsletter generation pipeline lives in `pipeline/`.

```
pipeline/run-all.sh [YYYY-MM-DD] --execute   # Full cycle (all 6 steps)
pipeline/generate.sh [YYYY-MM-DD]             # Step 1: Generate EN article
pipeline/translate.sh YYYY-MM-DD              # Step 2: Translate EN → PT-BR
pipeline/extract.sh YYYY-MM-DD               # Step 3: Extract sources → .sources.json
pipeline/ingest.sh YYYY-MM-DD --execute       # Step 4: Ingest into DB
pipeline/rewrite-links.sh YYYY-MM-DD         # Step 5: Replace URLs with DJ links
pipeline/publish.sh YYYY-MM-DD               # Step 6: Push to Jekyll site
```

Prompts: `pipeline/prompts/` (INNERLOOP_UPDATE.md, TRANSLATION.md, SOURCE_EXTRACTION.md)
Output: `pipeline/output/` (per-date .md, .pt.md, .sources.json, .links.json, .final.md)

Each step skips if output already exists. Delete the output file to rerun.
Step 4 (ingest) is dry-run by default — pass `--execute` to write to DB.
Step 6 (publish) commits and pushes immediately unless `--dry-run`.

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
