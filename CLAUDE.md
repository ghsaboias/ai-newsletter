# AI Newsletter

Public Jekyll site for Fast Takeoff. Deploys to GitHub Pages via Actions.

## Pipeline

Full newsletter generation pipeline lives in `pipeline/`.

```
pipeline/run-all.sh [YYYY-MM-DD] --execute   # Full cycle (all 6 steps)
pipeline/research.sh [YYYY-MM-DD]             # Step 1: Research → .research.json
pipeline/generate.sh [YYYY-MM-DD]             # Step 2: Generate PT-BR article → .pt.md
pipeline/extract.sh YYYY-MM-DD               # Step 3: Extract sources → .sources.json
pipeline/ingest.sh YYYY-MM-DD --execute       # Step 4: Ingest into DB
pipeline/rewrite-links.sh YYYY-MM-DD         # Step 5: Replace URLs with DJ links
pipeline/publish.sh YYYY-MM-DD               # Step 6: Push to Jekyll site
```

Prompts: `pipeline/prompts/` (RESEARCH.md, GENERATION.md, SOURCE_EXTRACTION.md)
Output: `pipeline/output/` (per-date .research.json, .pt.md, .sources.json, .links.json, .final.md)

Research (step 1) does all web fetching and outputs structured JSON. Generate (step 2) writes the article from research data only — no web access, fast iteration. Extract (step 3) assembles DJ source data from research.json + article — no re-fetching.

Each step skips if output already exists. Delete the output file to rerun.
Step 4 (ingest) is dry-run by default — pass `--execute` to write to DB.
Step 6 (publish) commits and pushes immediately unless `--dry-run`.

### Prompt sampling

`pipeline/sample.sh` runs a prompt N times against existing data to compare outputs. Useful for calibrating prompt wording before committing to a full run.

```
pipeline/sample.sh generate 2026-03-03              # 5 samples (default)
pipeline/sample.sh generate 2026-03-03 -n 10        # 10 samples
pipeline/sample.sh generate 2026-03-03 -q "Write only the opening and closing lines."
pipeline/sample.sh source_extraction 2026-03-03 -q "List the 5 most important stories."
```

Saves to `pipeline/output/samples/` and prints all results at the end.

## Substack

Convert a generated article to Substack-ready HTML with pandoc:

```
pandoc pipeline/output/YYYY-MM-DD.pt.md --from markdown-tex_math_dollars --to html -o pipeline/output/YYYY-MM-DD.substack.html
```

`-tex_math_dollars` prevents `$` amounts from being parsed as LaTeX. Paste the output into Substack's HTML editor (`</>` button).

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
