# Daily Newsletter — Generation

Write today's newsletter article in Brazilian Portuguese using the research file as your sole source material. Do not search the web. Every fact and link must come from `pipeline/output/YYYY-MM-DD.research.json`.

Save output to `pipeline/output/YYYY-MM-DD.pt.md`.

## Input

Read `pipeline/output/YYYY-MM-DD.research.json`. This contains today's verified stories with URLs, key facts, and metadata.

## Structure

### Title
`Bem-vindo(a) a [Dia] de [Mês] de [Ano]`

### Opening Line
A single sentence that introduces and summarizes the day.

### Body
5-8 thematic paragraphs. Each paragraph:
1. Chains 2-4 related stories with **inline links on key phrases**
2. Weaves stories into a narrative arc — not a bullet list disguised as prose

Stories within a paragraph must relate to each other. Each paragraph cluster should represent a distinct domain — ensure hardware, geopolitics, and biotech all get at least one paragraph.

## Voice & Tone

- **Conviction** — no hedging. Treats acceleration as inevitable and already underway, not aspirational
- **Dense and specific** — every claim is linked. Uses exact numbers: percentages, dollar amounts, ratings, time horizons
- **Narrative, not listicle** — reads like dispatches from the front line, not a news roundup
- **Named actors** — specific names: Musk, Altman, researchers, companies
- **Juxtaposition as a signature move** — the best sentences pair a grand claim with an absurd or contradictory detail in the same breath. This tension between the sublime and the ridiculous is core to the voice
- **Zero filler** — every word earns its place
- **Only what's in the research** — all claims come from research.json.

## Link Density & Formatting

- **20-40 inline links per article** — nearly every factual claim links to a source
- Links go on the most descriptive phrase, not on "aqui" or "isso"
- Format: `[descriptive phrase](url)` — the linked text should make sense even without clicking
- Every URL must come from `research.json`. Do not invent or guess URLs.

## Word Count

Target: **550-800 words**. Err on the side of density over length.

## Output Format

Save to `pipeline/output/YYYY-MM-DD.pt.md`:

```markdown
---
date: YYYY-MM-DD
url:
title: "Bem-vindo(a) a [Dia] de [Mês] de [Ano]"
wordcount: NNN
generated: true
language: pt-br
---

# Bem-vindo(a) a [Dia] de [Mês] de [Ano]

[Article body]
```
