# Audit — Freshness Check

You are auditing a newsletter for stale news. Verify that every story presented as news actually happened within the edition's time window.

## Setup

1. Determine today's date and yesterday's date.
2. Set `DAY_DIR` to `pipeline/output/ai/<today>/`.
3. The research window is: **yesterday 10:00 BRT** to **today 10:00 BRT**.

## Inputs

Read these files:
- **Article**: `<DAY_DIR>/pt.md`
- **Research**: `<DAY_DIR>/research.json` (for source context — dates, excerpts)

## Process

1. Read both files.
2. For each distinct event in the article, check when it actually happened. Use research.json first (check `published_at` fields and excerpts). If unclear, use `WebSearch` to find the original announcement date.
3. Flag events **presented as news** that happened before the window opened.

**Roundup articles** (e.g., "45K layoffs in 2026") bundle old events under a fresh date. Check the individual events, not the article's publication date.

**Background context** supporting a fresh story is fine — don't flag it.

## Output

Write `<DAY_DIR>/audit.json`:

```json
{
  "issues": [
    {
      "event": "Short description",
      "article_text": "The sentence(s) from the article",
      "actual_date": "YYYY-MM-DD or approximate",
      "source": "URL of earliest coverage found",
      "detail": "Why this is stale"
    }
  ]
}
```

If all events are fresh: `{"issues": []}`

Do NOT flag background context. Do NOT invent issues.
