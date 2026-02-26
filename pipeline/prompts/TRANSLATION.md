# Newsletter Translation — EN → PT-BR

Translate the newsletter article from English to Brazilian Portuguese. The output should read as if it were originally written in Portuguese — not a translation.

## Input

A finished newsletter markdown file from `pipeline/output/YYYY-MM-DD.md`.

## Voice & Tone

The original article has a specific voice: accelerationist, sardonic, dense, narrative. **Preserve all of it.** The translation should carry the same:

- **Conviction** — no hedging, no "talvez" or "pode ser que"
- **Sardonic humor** — dry wit, especially in the opening and closing lines
- **Density** — every sentence carries weight. Don't inflate word count
- **Metaphors** — adapt to Portuguese equivalents that hit as hard. Don't translate literally if it sounds awkward. Find the Portuguese metaphor that lands.
- **Present tense, active voice** — "X lança" not "X lançou" or "X anunciou o lançamento de"

## Structure

Preserve exactly:
- Opening "A Singularidade..." line (translate the metaphor, keep the punch)
- Paragraph structure (same number of paragraphs, same thematic grouping)
- Bold paragraph openers
- Closing one-liner (this is the signature — spend time on it)
- All inline links in their original positions with original URLs

## Translation rules

- **Proper nouns** — Keep in English: company names, product names, model names (GPT-5.3-Codex-Spark, Claude Opus 4.6, Blackwell), benchmark names (SWE-bench, Jenova), people's names
- **Technical terms** — Keep in English when there's no natural Portuguese equivalent: tokens, benchmark, chips, data center, startups, drones. Use Portuguese when natural: inteligência artificial, rede neural, aprendizado de máquina
- **Numbers and units** — Keep dollar signs and numeric format ($65.7, 67%, $5.2). Translate units to Portuguese: billion → bilhão/bilhões, million → milhão/milhões, trillion → trilhão/trilhões. Example: "$65.7 billion" → "$65,7 bilhões". Use Brazilian decimal convention (comma for decimals) in translated numbers.
- **Acronyms** — Keep: CEO, P/E, YoY, DOE, FDA, IPO, SaaS. Spell out on first use only if the original does
- **Links** — Keep every URL exactly as-is. The anchor text gets translated but the URL stays

## Quality bar

- **Every link must survive.** Count links in the original, count links in the translation. They must match exactly. A dropped link is a bug.
- **Read the translation aloud.** If any sentence sounds like translated English — awkward preposition, unnatural word order, calque — rewrite it. Portuguese has its own rhythm.
- **The opening and closing lines are the hardest part.** They carry the personality of the piece. Spend disproportionate time on them. If the metaphor doesn't land in Portuguese, find one that does — don't settle for a flat literal translation.
- **Verify numbers and proper nouns survived intact.** $65.7 billion → $65,7 bilhões (correct). Dollar amounts and percentages must keep their values. Names must not be misspelled or altered.
- **Word count should be within 10% of the original.** Portuguese tends to run slightly longer, but if you're 20%+ over, you're inflating. Cut filler.
- **Read the original twice before translating.** Understand the argument each paragraph is making, not just the words. Translate the argument.

## What NOT to do

- Don't add explanatory context that isn't in the original ("para quem não sabe, ...")
- Don't soften the tone — if the original is blunt, be blunt
- Don't expand sentences — if anything, Portuguese should be tighter
- Don't translate the frontmatter fields (date, url, title, wordcount, generated)
- Don't change "The Singularity" to anything other than "A Singularidade"

## Output format

Save to `pipeline/output/YYYY-MM-DD.pt.md` with the same frontmatter, adding `language: pt-br`:

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

[Translated article body]
```
