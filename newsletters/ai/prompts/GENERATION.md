# Daily Newsletter — Generation

The user will provide a **target date**. Write that day's newsletter article in Brazilian Portuguese using the research file as your sole source material. Do not search the web. Every fact and link must come from `{day_dir}/research-slim.json`.

Read the research file first. Save output to `{day_dir}/pt.md`.

## Structure

### Title
`[Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]`

### Opening Line
A single sentence that introduces and summarizes the day. Max ~180 characters — this doubles as the Substack subtitle. Use abbreviations ($2bi, 5GW) to stay tight.

### Body
5-8 thematic paragraphs. Each paragraph:
1. Groups related stories (typically 2-4) with **inline links on key phrases**
2. Weaves stories into a narrative arc — not a bullet list disguised as prose

Stories within a paragraph should relate to each other. Prioritize clusters that the research naturally supports — typically AI/infrastructure, hardware/semiconductors, geopolitics, and biotech. If a domain has no stories in the research, skip it. Don't force coverage.

## Voice & Tone

- **Conviction** — no hedging. Treats acceleration as inevitable and already underway, not aspirational
- **Dense and specific** — every claim is linked. Uses exact numbers: percentages, dollar amounts, ratings, time horizons
- **Narrative, not listicle** — reads like dispatches from the front line, not a news roundup
- **Named actors** — specific names: Musk, Altman, researchers, companies
- **Juxtaposition as a signature move** — the best sentences pair a grand claim with an absurd or contradictory detail in the same breath. This tension between the sublime and the ridiculous is core to the voice
- **Zero filler** — every word earns its place
- **Only what's in the research** — all claims come from research-slim.json.

## Accessibility — Write for Non-Specialists

The audience is educated but not technical. Every sentence must be clear to someone who doesn't work in tech, finance, or defense.

### Explain every entity on first mention

If a company, organization, or person isn't a household name, add a descriptor clause. Use the `entities` field in the research data to identify actors. Check the `key_facts` for context about what they do.

- ✅ `a FANUC, maior fabricante de robôs industriais do Japão`
- ✅ `Karen Hao, jornalista de tecnologia do Wall Street Journal`
- ✅ `o Drift Protocol, plataforma de derivativos na blockchain Solana`
- ✅ `a Shimizu, construtora japonesa`
- ❌ `a FANUC colabora com a NVIDIA` (reader doesn't know what FANUC is)
- ❌ `Karen Hao publicou...` (reader doesn't know who she is)

Names that don't need explanation: OpenAI, Google, Microsoft, Apple, Meta, Amazon, Tesla, Nvidia, Samsung, SpaceX, NASA, Elon Musk, Sam Altman, Trump.

### Simplify technical terms

Never assume the reader knows jargon. Rewrite or add inline context:

- ✅ `máquinas de litografia ultravioleta extrema (EUV)` on first use, then `EUV`
- ✅ `um recurso da Solana que permite pré-assinar transações sem prazo de validade`
- ✅ `certificação de segurança de dados (SOC 2)`
- ❌ `DRAM 1c`, `HBM4`, `plataforma Rubin` (meaningless to non-specialists)
- ❌ `durable nonce`, `dual listing`, `misbranding` (English jargon without context)

If a technical concept can't be explained in a clause, either simplify to its consequence ("chips de memória mais rápidos") or cut it.

### Formatting rules

- **Currency**: always `US$` — never bare `$`, never `¥`, `€`, `₩`, or "trilhões de wons". Convert foreign currencies to US$ using the research data.
- **Approximation**: `por volta de`, `cerca de`, `aproximadamente` — never `~`
- **Abbreviations**: `quarto trimestre` not `Q4`. `primeiro semestre` not `H1`. `ano contra ano` → `em relação ao mesmo período do ano anterior` or just state both numbers.
- **Outlet names**: `Wall Street Journal` not `WSJ`. `New York Times` not `NYT`. Spell out on first use.
- **Units**: kilometers, not miles. Celsius, not Fahrenheit. Convert if the source uses imperial.
- **English words**: use Portuguese equivalents when they exist. `diferença` not `gap`. `delator` not `whistleblower`. `listagem dupla` not `dual listing`.

## Link Density & Formatting

- **20-40 inline links per article** — nearly every factual claim links to a source
- Links go on the most descriptive phrase, not on "aqui" or "isso"
- Format: `[descriptive phrase](url)` — the linked text should make sense even without clicking
- Every URL must come from `research-slim.json`. Do not invent or guess URLs.

## Word Count

Target: **550-800 words**. When research yields more stories than fit, cut the weakest — stories with less concrete data, less reader impact, or weaker connections to the day's main threads. Don't try to mention everything.

## Self-Check Before Saving

After writing the article, re-read it once and fix:

1. **Every company/person has a descriptor on first mention?** Scan each entity name — if a reader wouldn't know who they are, add a clause.
2. **Any unexplained technical term?** If you'd need a glossary to understand it, rewrite.
3. **All currency is US$?** No bare $, no foreign currencies without conversion.
4. **No English jargon?** Read each sentence — any word a Portuguese-speaking non-specialist wouldn't know?
5. **Every sentence would make sense read aloud to someone with no tech background?**

Fix problems in place. Do not leave notes or TODOs.

## Output Format

Save to `{day_dir}/pt.md`:

```markdown
---
date: YYYY-MM-DD
url:
title: "[Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]"
wordcount: NNN
generated: true
language: pt-br
---

# [Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]

[Article body]
```
