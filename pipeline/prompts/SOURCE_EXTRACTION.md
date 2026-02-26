# Newsletter Source Extraction — Instructions

Given a finished newsletter article (PT-BR markdown with inline links), extract structured source data for each unique URL. This data will be used to create news entities and article records on Daily Journal.

## Input

You will receive the translated PT-BR newsletter markdown (`YYYY-MM-DD.pt.md`). Each link follows the pattern `[anchor text](url)`. All anchor text and paragraph context is already in Portuguese.

## Process

### Step 1: Parse all unique URLs

Extract every URL from the article. Deduplicate (some URLs appear twice). For each, capture:
- The **anchor text** (the linked phrase)
- The **surrounding sentence** (the full sentence containing the link)
- The **paragraph theme** (what the paragraph is about)

### Step 2: Group URLs by story

Multiple links about the same event should be grouped into one source entry. For example, 3 links about "Anthropic vs DeepSeek distillation" — WSJ, The Decoder, Business Insider — all become one entry with multiple sources.

This grouping maps directly to how Daily Journal creates news entities — **one event = one entity**, backed by multiple source articles.

### Step 3: Fetch source content (parallel, best effort)

**Use subagents to fetch in parallel.** Split the URLs into batches of up to 5 and launch one Task subagent per batch. Each subagent must use `model: "opus"` (Opus 4.6). Pass each subagent:
- The batch of URLs to fetch
- The anchor text and surrounding sentence for each URL (from Step 1)
- Instructions to return per URL: **title**, **published date**, **image URL** (og:image or article thumbnail), **key facts**, and a **one-sentence summary**

Example: 36 URLs → 8 subagents of 4-5 URLs each, all running in parallel.

Each subagent should fetch and extract:
- **News articles** (Reuters, AP, TechCrunch, etc.) — title, published date, og:image, first paragraphs, key facts
- **X/Twitter posts** — tweet text, author, post date. Title = "Tweet de @handle: [first 80 chars]". No image_url.
- **Company blogs** (OpenAI, Waymo, etc.) — announcement title, date, og:image, details
- **YouTube** — video title, upload date, thumbnail URL, description
- **Paywalled sources** (WSJ, Bloomberg, FT) — use the anchor text + paragraph context as primary source. Search for the same story on non-paywalled outlets if needed. Title and summary from context; image_url from og:image if the page loads at all.

**Do not block on failed fetches.** The article text itself contains enough context for most sources — the anchor text is descriptive and the surrounding paragraph provides facts and numbers.

Once all subagents return, merge their results and proceed to Step 4.

### Step 4: Produce structured output

For each grouped source (one per news event), output a JSON object with two levels: the **news entity** (grouped story) and **per-source article data**.

```json
{
  "headline": "Anthropic acusa DeepSeek, Moonshot e MiniMax de ataque de destilação em escala industrial",
  "summary": "Labs chineses criaram 24 mil contas falsas e fizeram 16 milhões de consultas ao Claude para extrair capacidades de raciocínio e código.",
  "bullets": [
    "DeepSeek, Moonshot AI e MiniMax criaram 24.000 contas falsas na Anthropic",
    "16 milhões de consultas ao Claude para extrair capacidades de raciocínio, código e uso de ferramentas",
    "Labs rotearam consultas por proxies para evadir detecção",
    "Ataques cresceram em intensidade e sofisticação ao longo do tempo"
  ],
  "body": "A Anthropic publicou evidências de que três laboratórios chineses — DeepSeek, Moonshot AI e MiniMax — criaram mais de 24 mil contas fraudulentas para extrair capacidades do Claude em escala industrial. Ao todo, foram 16 milhões de consultas focadas em raciocínio, código e uso de ferramentas, com os labs roteando tráfego por proxies comerciais para evadir detecção.\n\nOs ataques cresceram em intensidade ao longo dos últimos meses, com a MiniMax liderando o volume de requisições. A Anthropic afirma que os dados extraídos foram usados para treinar modelos concorrentes, configurando destilação em violação dos termos de uso.",
  "category": ["technology", "world"],
  "entities": {
    "people": [],
    "organizations": ["Anthropic", "DeepSeek", "Moonshot AI", "MiniMax"],
    "places": []
  },
  "is_breaking": false,
  "sensitivity": "normal",
  "sources": [
    {
      "url": "https://www.wsj.com/tech/ai/anthropic-accuses-chinese-companies-of-siphoning-data-from-claude-63a13afc",
      "title": "Anthropic acusa empresas chinesas de extrair dados do Claude",
      "summary": "WSJ: DeepSeek, Moonshot e MiniMax criaram 24 mil contas falsas para extrair capacidades de raciocínio do Claude via 16 milhões de consultas.",
      "bullets": [
        "24 mil contas falsas criadas por três labs chineses",
        "16 milhões de consultas focadas em raciocínio, código e uso de ferramentas",
        "Anthropic detectou e bloqueou as campanhas, publicando relatório detalhado"
      ],
      "published_at": "2026-02-23",
      "image_url": "https://images.wsj.net/im-12345/social"
    },
    {
      "url": "https://the-decoder.com/anthropic-accuses-deepseek-moonshot-and-minimax-of-stealing-claudes-ai-data-through-16-million-queries/",
      "title": "Anthropic acusa DeepSeek, Moonshot e MiniMax de roubo de dados via 16 milhões de queries",
      "summary": "The Decoder: três labs chineses usaram proxies para esconder consultas em massa ao Claude, focando em raciocínio e código.",
      "bullets": [
        "MiniMax liderou com 13 milhões de requisições, migrando para novos modelos em 24h",
        "Moonshot AI focou em raciocínio de agentes e uso de ferramentas",
        "Labs usaram proxies comerciais para evadir detecção"
      ],
      "published_at": "2026-02-23",
      "image_url": "https://the-decoder.com/wp-content/uploads/2026/02/anthropic-deepseek.jpg"
    }
  ]
}
```

### News entity fields

| Field | Type | Description |
|---|---|---|
| `headline` | string | Título factual: o que aconteceu, quem, quando. Máximo 100 caracteres. |
| `summary` | string | Frase direta com o fato principal e consequência imediata. Máximo 150 caracteres. |
| `bullets` | string[] | 3-8 fatos específicos. Cada bullet = 1 fato concreto com número, nome ou data. |
| `body` | string | 1-3 parágrafos sintetizando a notícia em narrativa coesa. Não repita o headline ou summary — expanda com contexto, consequências e detalhes dos sources. Separe parágrafos com `\n\n`. |
| `category` | string[] | One or more editorial categories (see reference below). Primary category first. |
| `entities` | object | `{people: string[], organizations: string[], places: string[]}`. Only named entities explicitly mentioned. |
| `is_breaking` | boolean | `true` only for genuinely breaking news (first report of a major event). Default `false`. |
| `sensitivity` | string | `"normal"`, `"violent"`, `"adult"`, or `"political_high_risk"`. Most sources are `"normal"`. Use `"violent"` for graphic military/attack content, `"political_high_risk"` for stories that need editorial caution. |

### Per-source article fields

| Field | Type | Description |
|---|---|---|
| `url` | string | Original URL from the newsletter. |
| `title` | string | Article title in PT-BR. Translate from English if needed. Should read as a standalone headline. |
| `summary` | string | One sentence describing what **this specific source** reports. Start with outlet name (e.g. "Reuters: ..."). Different from the parent entity summary — this is about what this one article says. |
| `bullets` | string[] | 2-5 fatos específicos deste source individual. Devem ser diferentes dos bullets da entity — foque no que **este artigo em particular** reporta, não no evento geral. Cada bullet = 1 fato concreto com número, nome ou data. |
| `published_at` | string | Publication date in `YYYY-MM-DD` format. Extract from the page, or use the newsletter date as fallback. |
| `image_url` | string | The article's og:image or main thumbnail URL. If not found, use `""` (empty string). |

## Quality bar

- **Every link in the article must appear in the output.** Count the unique URLs in the markdown. Count the URLs across all `sources` arrays. They must match. A missing URL means a missing source — go back and add it.
- **Grouping must be correct.** URLs about the same event go together. URLs about different events stay separate — even if they mention the same company. "Anthropic acusa DeepSeek de destilação" and "Pentágono convoca CEO da Anthropic" are different events, different source entries.
- **headline must read as a news headline.** Factual, specific, under 100 characters. If you read just the headline, you know what happened.
- **summary must add context beyond the headline.** Not a rephrasing — it should include the key consequence or number that the headline omits. Under 150 characters.
- **bullets must contain at least 3 concrete details per source.** Numbers, dates, dollar amounts, percentages, names. If you can't find 3, re-read the paragraph context and try fetching the source again.
- **Entities must be exhaustive for what's mentioned.** Don't list 2 people when the paragraph names 4. Scan the surrounding text carefully.
- **Per-source title must be a real headline.** Not a URL slug, not anchor text verbatim. A proper title that describes the article.
- **Per-source summary must be source-specific.** "Reuters: X happened" — not a copy of the parent summary. Each source covers a slightly different angle or detail.
- **Per-source image_url must be a direct image URL** (ending in .jpg, .png, .webp, or from a known CDN like images.wsj.net, static.reuters.com). If the page doesn't load or has no image, use `""`.
- **Per-source published_at must be accurate.** Extract from the page's date metadata. If genuinely unavailable, use the newsletter date.
- **Fetch before falling back.** Try to crawl every URL. Only fall back to article context when the fetch genuinely fails (paywall, 403, timeout). The fetched content will have details the article omits.
- **All text fields must be in PT-BR.** The input is already in Portuguese — match it. Source titles from English outlets should be translated.
- **category must use DJ's vocabulary.** See reference below. A source can have multiple categories — list the most specific first.

## Output format

Save to `innermost-loop/YYYY-MM-DD.sources.json`:

```json
{
  "date": "2026-02-24",
  "newsletter_file": "2026-02-24.pt.md",
  "source_count": 12,
  "url_count": 35,
  "news_entities": [
    { ... },
    { ... }
  ]
}
```

`source_count` = number of entries in `news_entities` (grouped stories).
`url_count` = total URLs across all `sources` arrays (must match unique URLs in the article).

## Categories reference

Use ONLY these exact English values (same as Daily Journal database):

| Category | Covers |
|---|---|
| technology | AI models, benchmarks, LLM releases, hardware, chips, data centers, software platforms, scientific automation, biotech |
| world | Export controls, sanctions, military policy, international relations, defense, autonomous weapons, geopolitics |
| economy | Markets, funding rounds, valuations, IPOs, earnings, labor, stock moves, investor sentiment |
| finance | Banking, interest rates, monetary policy, fiscal policy, analyst reports |
| business | Startups, partnerships, M&A, corporate strategy, enterprise AI adoption |
| politics | Regulation, legislation, government AI policy, political figures acting on tech/AI |
| brazil | Any story specifically about Brazil |
| sports | Sports-related stories |
| entertainment | Entertainment, media, culture |

Assign 1-3 categories per entity. Most AI newsletter stories will use `technology` as primary, combined with `world`, `economy`, `business`, or `politics` as secondary.
