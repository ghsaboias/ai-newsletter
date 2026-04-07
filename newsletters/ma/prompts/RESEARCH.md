# Research — News Cluster

Search for M&A news **events that occurred** between **{{PREV_DATE}} 10:00 BRT** and **{{DATE}} 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — deal announcements, regulatory decisions, filings, advisory mandates. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Deal details matter**: always capture deal value, structure (cash/stock/mixed), premium to market price, and expected close timeline when available.
- **Pricing and valuation**: when disclosed, capture EV/EBITDA multiple, EV/Revenue multiple, P/E, % stake acquired, implied equity value, and target financials (revenue, EBITDA, margins). These go in `key_facts` with source excerpts.

## Tools

| Tool | Use for |
|---|---|
| `exa_search` | Best for dated news. Use single-topic queries — multi-topic loses focus. Set `startPublishedDate`/`endPublishedDate` for date scoping. Pass `contents: {text: true}` to get full article text inline — avoids a separate fetch. |
| `exa_get_contents` | Fetch full text from URLs you already have (e.g. from press releases, SEC filings, or a source you want to read in full). Pass an array of URLs. |

**Do NOT fetch these domains** (blocked/paywalled — use `exa_search` snippets instead):
reuters.com, bloomberg.com, axios.com, cnbc.com, politico.eu, seekingalpha.com, businessinsider.com, wired.com, wsj.com, ft.com, law360.com, mergermarket.com

## Workflow

1. Check the previous edition headlines at the end of this prompt to know what's already covered.
2. **Landscape scan**: Run 5 broad Exa searches covering deal announcements, antitrust decisions, advisory mandates, and market trends. This gives you the map.
3. **Go deeper on what matters**: For the most important deals, fetch source URLs to get exact terms — deal value, structure, premium, advisors, regulatory timeline. Skip fetching for minor stories where search results already gave you enough.
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
      "category": ["finance"],
      "entities": {
        "organizations": [],
        "people": [],
        "places": []
      }
    }
  ]
}
```

**Story fields**: `id` (unique kebab slug), `headline` (<100 chars), `key_facts` (3-8 sourced facts, each with `source_url` pointing to a listed source and `excerpt` with the supporting text), `sources`, `category` (1-3 from: finance, business, technology, healthcare, energy, industrials, regulation, antitrust), `entities` ({organizations, people, places} — named entities from sources only).

**Source fields**: `url`, `outlet`, `title`, `published_at` (YYYY-MM-DD, fallback today), `image_url` ("" if unavailable), `type` (news_article|press_release|government_filing|blog_post|paper|regulatory_decision).
