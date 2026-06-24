---
name: sbq
description: Query the Daily Journal Supabase database using the sbq CLI. Use when inspecting tables, counting rows, filtering data, running raw SQL, or debugging ingestion/news state.
allowed-tools: Bash
---

# sbq — Supabase Query CLI

## Credentials / where to run

`sbq` is a global CLI (`~/.local/bin/sbq`) but it finds its DB credentials by
looking for `.env.local` in the current directory and walking up the tree. **This
repo (`ai-newsletter`) has no such file** — the Supabase creds live in
`~/daily-journal-platform/.env.local`. So **run `sbq` from `~/daily-journal-platform`**:

```bash
cd ~/daily-journal-platform && sbq news "select=headline,created_at&order=created_at.desc&limit=5"
```

The shell cwd resets between Bash calls, so prefix `cd ~/daily-journal-platform` on every `sbq` call. `--sql` additionally needs `SUPABASE_ACCESS_TOKEN` set in that `.env.local`.

## Safety

- `sbq` can't be used for write operations.
- If writing is needed, get explicit user permission first.

```bash
sbq <table> [query] [--count]
sbq --tables                              # list all tables
sbq --rpcs                                # list RPC functions
sbq --sql "SELECT ..."                    # raw SQL (CTEs, joins, aggregates)
```

## Common queries

```bash
sbq articles "select=id,title&limit=5"
sbq articles --count
sbq article_ai "matched_topics=not.is.null&limit=5"
sbq ingestion_runs "order=started_at.desc&limit=5"
sbq topics "select=slug,title&limit=10"
sbq news "select=headline,created_at&order=created_at.desc&limit=5"
```

## Column-name gotchas

The headline column is **not** named the same across tables. Don't assume `title`.

- `news`, `news_candidates` → `headline` (no `title` column — querying `title` errors)
- `articles`, `topics` → `title`

When unsure of a table's columns, check first instead of guessing:

```bash
sbq --sql "SELECT column_name FROM information_schema.columns WHERE table_name = 'news' ORDER BY ordinal_position"
```

## Operators

`eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`, `ilike`, `is.null`, `not.is.null`, `in.(a,b,c)`, `not.eq`

## Joins

```bash
sbq articles "select=id,title,article_ai(one_sentence)&limit=5"
```

## Order & limit

```bash
sbq articles "order=published_at.desc&limit=10"
```

## Raw SQL

```bash
sbq --sql "SELECT type, status, COUNT(*) FROM assignment_jobs GROUP BY type, status"
```

**--sql tips:**
- Apostrophes: use SQL `''` → `"SELECT * WHERE title LIKE '%Trump''s%'"`
- UUIDs: always cast → `WHERE id = 'abc-123'::uuid`
- JSON: `->>'key'` → `"SELECT raw_rss_json->>'title' FROM articles"`
- Empty results return `[]`
- pgvector `<=>` (cosine distance) FAILS here — the `vector` type lives in the `extensions` schema and the operator won't resolve. Use keyword/regex search instead.

## Shell gotchas

**Don't mix jq + echo** — jq treats unquoted words as filenames:
```bash
# WRONG
echo "=== label ===" && sbq articles | jq '.'
# RIGHT — just pipe
sbq articles | jq '.'
```

**Complex jq aggregations break** — do them in SQL instead:
```bash
# Bad
sbq jobs "limit=50" | jq 'group_by(.type + "-" + .status) | ...'
# Good
sbq --sql "SELECT type, status, COUNT(*) FROM assignment_jobs GROUP BY type, status"
```

## Array vs JSONB columns

Postgres arrays (`TEXT[]`, `UUID[]`) come back as JSON arrays but are native types.
- Use junction tables (`news_articles`, `news_topics`) for writes
- Array columns are caches, auto-synced via triggers

CLI source: `~/.local/bin/sbq`
