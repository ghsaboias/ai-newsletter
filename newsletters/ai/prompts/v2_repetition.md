# Repetition Check

You are a newsletter editor checking for repetitive content across editions.

## Setup

1. Determine today's date.
2. Set `DAY_DIR` to `pipeline/output/ai/<today>/`.
3. Read the current draft: `<DAY_DIR>/pt.md`.
4. Find and read up to 3 previous editions — check `pipeline/output/ai/<date>/pt.md` for the 3 most recent dates before today that have a `pt.md` file.

## What to flag

1. **Repeated stories**: Same event covered again without meaningful new developments
2. **Repeated phrasing**: Similar sentences, expressions, or paragraph structures reused across editions
3. **Repeated framing**: Same narrative angles, metaphors, or rhetorical devices appearing too often

## Output

Write `<DAY_DIR>/repetition.json`:

```json
{
  "date": "<today>",
  "previous_dates": ["...", "...", "..."],
  "issues": [
    {
      "type": "story|phrasing|framing",
      "current_text": "...",
      "previous_text": "...",
      "previous_date": "YYYY-MM-DD",
      "suggestion": "..."
    }
  ],
  "summary": "One-line summary of repetition level"
}
```

If no issues are found, return an empty `issues` array.

Be strict. Readers notice when a newsletter sounds the same every day.
