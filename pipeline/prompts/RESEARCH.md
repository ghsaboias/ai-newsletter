# Research — News Cluster

Search for news **events that occurred** between **{{PREV_DATE}} 10:00 BRT** and **{{DATE}} 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

Your output will be merged with other clusters into the final research file.

## Rules

- **At least 7 stories.** If you have fewer, search more.
- Every URL must come from a search result or fetched page. Never invent URLs.
- **Recency: the underlying event must have occurred within the research window ({{PREV_DATE}} 10:00 BRT to {{DATE}} 10:00 BRT).** Sources published shortly after the window closes are acceptable, but the event itself must fall within it. Skip stories about events from before the window.
- Every fact in `key_facts` must come from a **listed source** — one that appears in the story's `sources` array. No background knowledge, no facts from pages you visited but didn't cite. If you found a fact via a tweet, search snippet, or secondary article, add that URL to `sources`.
- At least one source with a real URL per story.
- `headline` and `key_facts` in English.
- The previous edition's headlines are listed at the end of this prompt. Skip stories already covered unless there's a genuinely new development.
- **Date-scope all searches** to {{PREV_DATE}} and {{DATE}}. This is critical when researching past editions.

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

1. Check the previous edition headlines at the end of this prompt to know what's already covered.
2. **Landscape scan**: Start broad — fetch Techmeme, run 3-5 Exa searches across your categories. This gives you the map.
3. **Go deeper on what matters**: For the most important stories, fetch source URLs to get exact facts, quotes, and numbers. Skip fetching for minor stories where search results already gave you enough.
4. **No duplicate work**: Never re-run a search you already ran. Never re-fetch a URL. If a search didn't return what you need, try a *different* query, don't repeat.
5. Write the JSON output file.

## Output

Write to the file path given below. Format:

```json
{
  "stories": [
    {
      "id": "kebab-case-slug",
      "headline": "Factual headline under 100 chars",
      "key_facts": [
        {
          "fact": "Specific claim with numbers/names/dates",
          "source_url": "https://...",
          "excerpt": "Exact quote or close paraphrase from the source supporting this fact"
        }
      ],
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

**Story fields**: `id` (unique kebab slug), `headline` (<100 chars), `key_facts` (3-8 sourced facts, each with `source_url` pointing to a listed source and `excerpt` with the supporting text), `sources`, `category` (1-3 from: technology, world, economy, finance, business, politics, brazil, sports, entertainment), `entities` ({organizations, people, places} — named entities from sources only).

**Source fields**: `url`, `outlet`, `title` (tweets: "Tweet by @handle: [first 80 chars]"), `published_at` (YYYY-MM-DD, fallback today), `image_url` ("" if unavailable), `type` (news_article|tweet|blog_post|paper|press_release|video|government_filing).
