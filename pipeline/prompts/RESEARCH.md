# Research — News Cluster

Search for today's news in the categories listed below. Produce a JSON file of verified stories with sources.

Your output will be merged with other clusters into the final research file.

## Rules

- **At least 7 stories.** If you have fewer, search more.
- Every URL must come from a search result or fetched page. Never invent URLs.
- **All sources must be from the current date or previous 24 hours.** Older papers/posts can only appear if a new development references them — and the story's headline must be about the new development, not the old source.
- Every fact in `key_facts` must come from source content — no background knowledge. State facts as reported.
- At least one source with a real URL per story.
- `headline` and `key_facts` in English.
- Read yesterday's research from `pipeline/output/` first. Skip stories unless there's a genuinely new development.

## Tools

| Tool | Use for |
|---|---|
| `mcp__exa__web_search_exa` | Best for dated news. Use single-topic queries — multi-topic loses focus. |
| `WebSearch` | Broader web search. Supplement to Exa. |
| `WebFetch` | Fetch specific URLs. **Always pass `timeout: 15000`** — sites hang without it. |
| `bird search "query"` | X/Twitter. Use specific terms or `from:` queries — broad queries return noise. |
| `bird read <url>` | Fetch full tweet text. |

**Techmeme** (`WebFetch https://www.techmeme.com/`, timeout: 15000) — curated tech headlines, good landscape scan.

Key X accounts: `sama`, `elonmusk`, `OpenAI`, `AnthropicAI`, `GoogleDeepMind`, `scaling01`, `metr_evals`, `epochairesearch`, `arcprize`, `xaborsa`

## Workflow

1. Read yesterday's research file to know what's already covered.
2. Search across your categories with Exa and WebSearch.
3. Use WebFetch (timeout: 15000) only when search results lack title, date, or key facts.
4. Write the JSON output file.

## Output

Write to the file path given below. Format:

```json
{
  "stories": [
    {
      "id": "kebab-case-slug",
      "headline": "Factual headline under 100 chars",
      "key_facts": ["Specific fact with numbers/names/dates", "..."],
      "sources": [
        {
          "url": "https://...",
          "outlet": "Reuters",
          "title": "Article headline",
          "published_at": "YYYY-MM-DD",
          "image_url": "",
          "type": "news_article"
        }
      ],
      "category": ["technology"],
      "entities": {
        "organizations": [],
        "people": [],
        "places": []
      }
    }
  ]
}
```

**Story fields**: `id` (unique kebab slug), `headline` (<100 chars), `key_facts` (3-8 sourced facts), `sources`, `category` (1-3 from: technology, world, economy, finance, business, politics, brazil, sports, entertainment), `entities` ({organizations, people, places} — named entities from sources only).

**Source fields**: `url`, `outlet`, `title` (tweets: "Tweet by @handle: [first 80 chars]"), `published_at` (YYYY-MM-DD, fallback today), `image_url` ("" if unavailable), `type` (news_article|tweet|blog_post|paper|press_release|video|government_filing).
