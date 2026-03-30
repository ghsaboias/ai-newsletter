# Audit — Freshness Check

You are auditing a newsletter for stale news. The user will provide a **target date**. Your job: verify that every story presented as news actually happened within the edition's time window.

The research window is: **previous day 10:00 BRT** to **target date 10:00 BRT**.

## Inputs

Read these files:
- **Article**: `{day_dir}/pt.md`
- **Research**: `{day_dir}/research.json` (for source context — dates, excerpts)

## Process

1. Read both files.
2. For each distinct event in the article, check when it actually happened. Use research.json first (check `published_at` fields and excerpts). If unclear, use `WebSearch` to find the original announcement date.
3. Flag events **presented as news** that happened before the window opened.

**Roundup articles** (e.g., "45K layoffs in 2026") bundle old events under a fresh date. Check the individual events, not the article's publication date.

**Background context** supporting a fresh story is fine — don't flag it.

## Output

Write `{day_dir}/audit.json`:

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
