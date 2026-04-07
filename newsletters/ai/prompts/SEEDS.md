# Research — Seeds

You are given a list of URLs that must be included in the newsletter research. Fetch each URL, extract the key facts, and produce a research JSON file in the same format as the other research clusters.

## Rules

- **Fetch every URL** in the seeds list. Use `exa_get_contents`.
- For tweets (x.com/twitter.com URLs), use `bird read <url>` via bash instead.
- Extract the same level of detail as a normal research story: headline, 3-8 key facts with source URLs and excerpts, entities.
- The seed URL is your primary source. Search for 1-2 additional sources to corroborate or add context if useful.
- `headline` and `key_facts` in English.
- Every fact in `key_facts` must come from a listed source.

## Output

Write to the file path given below. Use the same JSON format as other research clusters:

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
          "excerpt": "Exact quote or close paraphrase from the source"
        }
      ],
      "sources": [
        {
          "url": "https://...",
          "outlet": "Source Name",
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
