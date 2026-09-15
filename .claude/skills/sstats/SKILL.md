---
name: sstats
description: Query Substack newsletter stats using the sstats CLI. Use when checking email performance, open rates, subscriber growth, or revenue metrics.
allowed-tools: Bash
---

# sstats — Substack Stats CLI

All output is JSON (except `post --html`, which emits raw HTML) — pipe to `jq` for filtering.

```bash
sstats summary                    # quick overview
sstats emails [-n 20]             # per-post: opens, clicks, views, engagement
sstats post [id|slug] [--html|--json|--meta]
                                  # published post HTML; no arg = today's latest
sstats open-rate                  # 30-day open rate
sstats views                      # 30-day views
sstats followers [days=90]        # follower timeseries
sstats growth [days=30]           # traffic/subscriber/revenue by source
sstats growth-ts [days=30]        # per-source timeseries
sstats paid [days=90]             # paid subscriber growth
sstats network [days=90]          # subscriber attribution
sstats geo [global|usa]           # geographic breakdown
sstats unsubscribes [days=90]     # unsubscribe trend
sstats notes [limit=20]           # subscriber notes (testimonials)
sstats published-notes [limit=20] [--table]   # Notes the pub published (JSON: date, url, reactions, restacks, replies, body)
sstats templates [--json]         # post templates (editor "Templates" menu): id, date, nodes, name
sstats template <id|name> [--body|--text|--json]   # one template; name = case-insensitive substring
sstats template-create <name> <doc.json>           # doc.json = ProseMirror {"type":"doc","content":[...]}
sstats template-update <id|name> <doc.json> [--name N]
sstats template-delete <id|name>
```

## Post templates (ad insertions)

Substack's editor "Templates" live at `/api/v1/post-templates` (GET list, GET/PUT/DELETE
`/post-templates/<id>`, POST `{name, body}`). `body` is a JSON **string** holding a
ProseMirror doc. The partner insertion models (Locaweb, Solana Hackathon) are
templates; source docs are versioned in `newsletters/ai/insertions/*.json`.

```bash
sstats template locaweb --text                    # quick read of the copy + links
sstats template solana --body > /tmp/solana.json  # edit, then:
sstats template-update solana /tmp/solana.json
```

Insertion anatomy (mirror it for new partners): `captionedImage` (1272×312 banner,
`href` = tracked link) → centered paragraphs, bold lead + plain tail → `button`
(same URL) → empty centered paragraph. Upload the banner with
`pipeline/tools/substack_upload.py <png> --href URL` to get the CDN `src`.

## Common usage

```bash
# Recent post performance
sstats emails -n 5 | jq '.rows[] | {title, open_rate, views}'

# Quick health check
sstats summary | jq '.'

# Growth trend
sstats growth --days 7 | jq '.'

# QA loop: grab exactly what published today, save to file
sstats post --today --html > /tmp/published.html   # full body, paywall bypassed
sstats post --meta | jq '{title, slug, wordcount, audience, canonical_url}'
sstats post <slug> --json | jq '.body_html'         # by slug or numeric id
```

`post` resolves today's most recent email post by default (warns on stderr if
the latest post isn't from today). Output is the published `body_html` — the
editorial content, not the email template chrome. Owner session bypasses the
paywall so `only_paid` posts come back in full.

## Auth

`SUBSTACK_SID` session cookie in `.env.local`. Expires periodically — if requests return HTML instead of JSON, refresh from browser DevTools → Application → Cookies → `substack.com`.

CLI source: `~/.local/bin/sstats`
