# Newsletter Source Extraction — Instructions

Given a finished PT-BR newsletter article and its research data, produce structured source data for Daily Journal. **Do not fetch any URLs** — all metadata comes from the research file.

## Input

You will receive two files:
- `YYYY-MM-DD.research.json` — structured research with per-story metadata (URLs, titles, dates, images, key facts, categories, entities)
- `YYYY-MM-DD.pt.md` — the finished PT-BR newsletter with inline links

## Process

### Step 1: Parse URLs from the article

Extract every URL from the article markdown. Deduplicate. For each, capture:
- The **anchor text** (the linked phrase, in Portuguese)
- The **surrounding sentence**
- The **paragraph theme**

### Step 2: Group URLs by story

Multiple links about the same event become one news entity. Use the article's paragraph structure as the primary grouping signal — links in the same paragraph about the same topic belong together.

One event = one entity, backed by multiple source articles.

### Step 3: Match with research data

For each URL, look it up in `research.json` to pull:
- `title` — from the source's `title` field
- `published_at` — from the source's `published_at` field
- `image_url` — from the source's `image_url` field
- `outlet` — from the source's `outlet` field
- `key_facts` — from the parent story's `key_facts`
- `category` — from the parent story's `category`
- `entities` — from the parent story's `entities`

If a URL from the article doesn't appear in research.json (edge case), use the anchor text and paragraph context to fill in the fields as best you can.

### Step 4: Produce structured output

For each news entity, write the DJ fields in PT-BR using the article text and research data.

```json
{
  "headline": "Objetos atingem data center da AWS nos Emirados e derrubam serviços em todo o Oriente Médio",
  "summary": "Incêndio forçou corte de energia em duas zonas de disponibilidade, derrubando S3, DynamoDB e mais de 60 serviços.",
  "bullets": [
    "Objetos não identificados atingiram data center da AWS nos EAU no domingo",
    "Bombeiros cortaram energia de duas zonas de disponibilidade",
    "S3, DynamoDB e mais de 60 serviços ficaram fora do ar"
  ],
  "body": "Objetos não identificados atingiram um data center da Amazon Web Services nos Emirados Árabes Unidos...",
  "category": ["technology", "world"],
  "entities": {
    "people": [],
    "organizations": ["Amazon Web Services"],
    "places": ["UAE"]
  },
  "is_breaking": false,
  "sensitivity": "normal",
  "sources": [
    {
      "url": "https://www.reuters.com/...",
      "title": "AWS reporta queda após data center nos EAU ser atingido por 'objetos'",
      "summary": "Reuters: Objetos não identificados provocaram incêndio no data center da AWS nos EAU.",
      "bullets": [
        "Objetos atingiram data center por volta das 7h30 ET",
        "Bombeiros cortaram energia; restauração esperada para várias horas"
      ],
      "published_at": "2026-03-02",
      "image_url": ""
    }
  ]
}
```

### News entity fields

| Field | Type | Description |
|---|---|---|
| `headline` | string | Título factual em PT-BR: o que aconteceu, quem, quando. Máximo 100 caracteres. |
| `summary` | string | Frase direta com o fato principal e consequência imediata. Máximo 150 caracteres. |
| `bullets` | string[] | 3-8 fatos específicos. Cada bullet = 1 fato concreto com número, nome ou data. |
| `body` | string | 1-3 parágrafos sintetizando a notícia. Não repita headline ou summary — expanda com contexto e detalhes. Separe parágrafos com `\n\n`. |
| `category` | string[] | Editorial categories from research.json. Primary category first. |
| `entities` | object | `{people: string[], organizations: string[], places: string[]}` from research.json, supplemented by article context. |
| `is_breaking` | boolean | `true` only for genuinely breaking news. Default `false`. |
| `sensitivity` | string | `"normal"`, `"violent"`, `"adult"`, or `"political_high_risk"`. |

### Per-source article fields

| Field | Type | Description |
|---|---|---|
| `url` | string | Original URL from the article. |
| `title` | string | Headline in PT-BR. Translate from research.json `title` if needed. |
| `summary` | string | One sentence: what **this specific source** reports. Start with outlet name. |
| `bullets` | string[] | 2-5 fatos from this source. Different from entity bullets — focus on what this article specifically covers. |
| `published_at` | string | From research.json. Fall back to newsletter date. |
| `image_url` | string | From research.json. Use `""` if not available. |

## Quality bar

- **Every URL in the article must appear in the output.** Count unique URLs in the markdown vs URLs across all `sources` arrays. They must match.
- **Grouping must be correct.** Same event → same entity. Different events → different entities, even if same company.
- **headline must read as a news headline.** Factual, specific, under 100 characters.
- **summary must add context beyond the headline.** Key consequence or number the headline omits.
- **Per-source title must be a proper headline** in PT-BR, not a URL slug or raw anchor text.
- **Per-source summary must be source-specific.** "Reuters: X happened" — each source covers a different angle.
- **All text fields must be in PT-BR.**
- **category must use DJ's vocabulary** (see reference below).

## Output format

Save to `pipeline/output/YYYY-MM-DD.sources.json`:

```json
{
  "date": "2026-03-02",
  "newsletter_file": "2026-03-02.pt.md",
  "source_count": 8,
  "url_count": 29,
  "news_entities": [
    { ... }
  ]
}
```

`source_count` = number of entries in `news_entities`.
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

Assign 1-3 categories per entity.
