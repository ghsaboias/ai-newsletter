# Research — Hardware & Physical AI Cluster

You are researching news for a daily newsletter. The user will provide a **target date**. Your research window is the 24 hours before it: **previous day 10:00 BRT → target date 10:00 BRT**.

Search for news events that **occurred** within that window. Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

Your output will be merged with other clusters into the final research file.

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

## Rules

- **At least 7 stories.** If you have fewer, search more.
- Every URL must come from a search result or fetched page. Never invent URLs.
- **Recency: the underlying event must have occurred within the research window.** Sources published shortly after the window closes are acceptable, but the event itself must fall within it. Skip stories about events from before the window.
- Every fact in `key_facts` must come from a **listed source** — one that appears in the story's `sources` array. No background knowledge, no facts from pages you visited but didn't cite. If you found a fact via a tweet, search snippet, or secondary article, add that URL to `sources`.
- At least one source with a real URL per story.
- `headline` and `key_facts` in English.
- Read the previous edition's research first. Skip stories already covered unless there's a genuinely new development.
- **Date-scope all searches** to the target date and the day before.

## Tools

Use `mcp__exa__web_search_exa` for dated news (single-topic queries). Use `WebSearch` as a supplement. Use `WebFetch` for specific URLs (always pass `timeout: 15000`). Use `Bash` with `bird search` or `bird read` for X/Twitter.

**Techmeme** (`WebFetch https://www.techmeme.com/`, timeout: 15000) — curated tech headlines, good landscape scan.

Key X accounts: `@elonmusk`, `@jimfanAI`, `@chilobrandt`

## Workflow

1. Read the previous edition's research file (`pipeline/output/{previous date}/research.json`) to know what's already covered.
2. **Landscape scan**: Fetch Techmeme, run 3-5 Exa searches across your categories.
3. **Go deeper on what matters**: For the most important stories, fetch source URLs to get exact facts, quotes, and numbers.
4. **No duplicate work**: Never re-run a search you already ran. Never re-fetch a URL.
5. Write the JSON output file to `pipeline/output/{date}/research-hw.json`.

## Output

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
