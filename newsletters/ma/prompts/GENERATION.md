# M&A Newsletter — Generation

The user will provide a **target date**. Write that day's M&A newsletter in Brazilian Portuguese using the research file as your sole source material. Do not search the web. Every fact and link must come from `{day_dir}/research-slim.json`.

Read the research file first. Save output to `{day_dir}/pt.md`.

## Structure

### Title
`[M&A] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]`

### Opening Line
A single sentence that captures the day's biggest deal or most consequential development. Max ~180 characters — this doubles as the Substack subtitle.

### Body
4-7 thematic paragraphs. Each paragraph:
1. Chains 2-3 related stories with **inline links on key phrases**
2. Weaves stories into a narrative arc — not a bullet list disguised as prose

Stories within a paragraph must relate to each other. Natural groupings:
- Megadeals and headline acquisitions
- Regulatory/antitrust developments
- Sector-specific deal clusters (tech, healthcare, energy, etc.)
- Advisory moves and market dynamics

## Voice & Tone

- **Precise and deal-literate** — always state deal value, structure, premium, and timeline. Readers are professionals.
- **Narrative, not listicle** — reads like a market briefing, not a deal log
- **Name all parties** — acquirer, target, advisors when known. No vague references.
- **Strategic context** — why this deal matters: consolidation play, regulatory signal, sector trend, valuation benchmark
- **Dense and specific** — every claim is linked. Uses exact numbers: deal value, premium %, expected close date
- **Neutral authority** — no cheerleading, no doom. State what happened, what it means, what to watch.
- **Zero filler** — every word earns its place
- **Only what's in the research** — all claims come from research-slim.json.

## Link Density & Formatting

- **15-30 inline links per article** — factual claims link to sources
- Links go on the most descriptive phrase, not on "aqui" or "isso"
- Format: `[descriptive phrase](url)` — the linked text should make sense even without clicking
- Every URL must come from `research-slim.json`. Do not invent or guess URLs.

## Word Count

Target: **500-750 words**. Err on the side of density over length.

## Output Format

Save to `{day_dir}/pt.md`:

```markdown
---
date: YYYY-MM-DD
url:
title: "[M&A] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]"
wordcount: NNN
generated: true
language: pt-br
---

# [M&A] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]

[Article body]
```
