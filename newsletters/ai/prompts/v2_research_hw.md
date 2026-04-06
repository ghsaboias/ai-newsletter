# Research — Hardware & Infrastructure Cluster

Search for news **events that occurred in the last 24 hours** (yesterday 10:00 BRT to today 10:00 BRT). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

Your output will be merged with other clusters (AI, World) into the final research file.

## Setup

1. Determine today's date and yesterday's date.
2. Set `DAY_DIR` to `pipeline/output/ai/<today>/` — create it if needed.
3. Check if `pipeline/output/ai/<yesterday>/research.json` exists. If so, read the headlines for dedup (skip stories already covered unless there's a genuinely new development).
4. Read `<DAY_DIR>/techmeme.txt` for a pre-research scan of current headlines. Use this as a starting map — some stories may be relevant to your categories.
5. Your output file is `pipeline/output/ai/<today>/research-hw.json`.

## Your categories

- Chips & semiconductors: Nvidia, AMD, Intel, Broadcom, custom silicon (Google TPU, Amazon Trainium, Microsoft Maia)
- Foundries: TSMC, Samsung, Intel Foundry — capacity, process nodes, orders
- Data centers: new builds, power deals, cooling tech, geographic expansion
- Energy for compute: nuclear, solar, grid upgrades, power purchase agreements
- Export controls: US-China chip restrictions, ASML/EUV, sanctions
- Robotics: humanoids (Tesla Optimus, Figure, Unitree), industrial automation, warehouse robots
- Drones: military, commercial, autonomous delivery, counter-drone systems
- Autonomous vehicles: Waymo, Cruise, Tesla FSD, Chinese players
- Space: launches, satellite constellations, orbital compute, space-based infrastructure

Key X accounts: @elonmusk, @jimfanAI, @chilobrandt

## Rules

- **At least 7 stories.** If you have fewer, search more.
- Every URL must come from a search result or fetched page. Never invent URLs.
- **Recency: the underlying event must have occurred within the research window.** Sources published shortly after the window closes are acceptable, but the event itself must fall within it. Skip stories about events from before the window.
- Every fact in `key_facts` must come from a **listed source** — one that appears in the story's `sources` array. No background knowledge, no facts from pages you visited but didn't cite. If you found a fact via a tweet, search snippet, or secondary article, add that URL to `sources`.
- At least one source with a real URL per story.
- `headline` and `key_facts` in English.
- **Date-scope all searches** to yesterday and today.

## Tools

| Tool | Use for |
|---|---|
| `mcp__exa__web_search_exa` | Best for dated news. Use single-topic queries — multi-topic loses focus. |
| `mcp__exa__crawling_exa` | Fetch full article text from URLs. Accepts an array of URLs in one call. Use for **all news sites** — especially those that block WebFetch. |
| `WebFetch` | Fetch non-news URLs only (press releases, gov sites, blogs). **Always pass `timeout: 15000`.** |
| `WebSearch` | Broader web search. Supplement to Exa. |
| `bird search "query"` | X/Twitter. Use specific terms or `from:` queries — broad queries return noise. |
| `bird read <url>` | Fetch full tweet text. |

**Do NOT WebFetch these domains** (blocked/paywalled — use `crawling_exa` instead):
reuters.com, bloomberg.com, axios.com, cnbc.com, politico.eu, seekingalpha.com, businessinsider.com, wired.com, business-standard.com, datacenterdynamics.com, etnownews.com, archynewsy.com, wccftech.com

## Workflow

1. Check previous edition headlines (if found) to know what's already covered.
2. **Landscape scan**: Run 5 Exa searches across your categories to build the map.
3. **Go deeper on what matters**: For the most important stories, fetch source URLs to get exact facts, quotes, and numbers. Skip fetching for minor stories where search results already gave you enough.
4. **No duplicate work**: Never re-run a search you already ran. Never re-fetch a URL. If a search didn't return what you need, try a *different* query, don't repeat.
5. Write the JSON output file.

## Output

Write to `pipeline/output/ai/<today>/research-hw.json`. Format:

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
