# Newsletter v2 — new format (handoff)

Point a fresh session at this file. It carries the decided format, the working tooling, and the plan, so we don't re-derive anything.

## Goal for the next session

1. **Convert today's edition into a draft in the new format** (already mostly done — see draft D below; polish if wanted).
2. **Automate it** — make the draft-generation engine emit this format by default, so every edition comes out three-tiered without hand-restructuring.

## Where we landed: the format

A **three-tier depth ladder**. Block size = story importance. No TLDR box, no pull-quote (tried, cut by Gui). Decided 2026-06-23.

```
[byline]

# GRANDES  → heading H3 (real headline) + 2–3 short paragraphs
  (the must-reads; ~3 stories)

──────────  (horizontal_rule)

# MÉDIAS   → H4 thematic cluster + dense bullets (bold lead-in + 1 sentence)
  Clusters used today: Segurança · Infraestrutura & energia · Rodadas · Hardware & modelos

──────────

# PEQUENAS → "Leia também" callout box, one line each (bold label + sentence)
  (the genuinely minor items)
```

Principles baked in (these are the three problems Gui flagged, solved):
- **Smaller paragraphs** — long blocks broken into 2–3 sentence units.
- **More/better formatting** — headings, dividers, bullets, callout box carry the hierarchy.
- **Small stories don't eat equal space** — they drop to one-liners in "Leia também".

The visual hierarchy *is* the editorial hierarchy — a story's tier is signalled by how much room its block gets, not by a label.

## Current state / drafts

All on `dailyjournalnews.substack.com`, `only_paid`, titled with a `FORMATO`/`ZZ` prefix (safe to delete; not published):

| Draft | id | What |
|---|---|---|
| **D — Grandes/Médias/Pequenas** | **203302947** | **the chosen format, today's content** ← start here |
| A — Manchetes | 203301597 | headline-driven (inspiration) |
| B — Resumo + seções | 203301598 | TLDR + themed sections (inspiration) |
| C — Digest denso | 203301599 | bullet-first (inspiration) |
| ZZ inventory drafts | 203295452 / 203299938 | format inventory probes |

Content base = the **2026-06-23 edition**: `pipeline/output/ai/2026-06-23/final.md` (canonical, DJ links) or live via `cd ~/daily-journal-platform && sstats post --today --html`.

Tiering used in D (Gui's to adjust):
- **Grandes:** SpaceX (lead), Kospi, EUA-Irã.
- **Médias (bullets):** Cibersegurança, Chevron/Microsoft, Oracle, Groq/Modular/AppsFlyer, LineShine, Nvidia Halos, Sakana.
- **Pequenas (Leia também):** Bending Spoons IPO, Definium/LSD, FDA/Regenxbio.

## How to build / update a draft

Reference renderer (persisted): **`v2/build_format_options.py`**. It holds today's content as structured functions (`spacex_paras()`, `funding_items()`, `leia_items()`, …) and four renderers (`option_A/B/C/D`). `option_D()` is the chosen format.

```bash
cd ~/daily-journal-platform && set -a && source <(grep -E '^SUBSTACK_(SID|PUB_HOST)=' .env.local) && set +a
python3 ~/ai-newsletter/v2/build_format_options.py     # currently PUT-updates draft 203302947 with option_D()
```

API (creds in `~/daily-journal-platform/.env.local`, header `Cookie: substack.sid=$SID`):
- `POST /api/v1/drafts` — create (returns `id`)
- `PUT  /api/v1/drafts/<id>` — update in place (keeps the same URL)
- `GET  /api/v1/drafts/<id>` — read `draft_body` back to verify node JSON

Body = `{"draft_title","draft_subtitle","draft_body": <stringified ProseMirror doc>, "draft_bylines":[{"id":473611573}], "audience","type":"newsletter"}`.

PM node cheatsheet (full reference: **`substack_inventory.md`**):
- heading `{type:"heading",attrs:{level}}` · paragraph `{textAlign}` · `horizontal_rule`
- bullets `bullet_list › list_item › paragraph` · `blockquote`
- **callout (the Leia também box):** `{type:"calloutBlock",content:[paragraph,…]}`
- button `{type:"button",attrs:{url,text}}` · paywall `{type:"paywall"}` · image `captionedImage › image2`
- marks: `strong, em, link, strikethrough, code, superscript, subscript`

Browser preview/verify: the live Brave session is driven via the `browser-tools` skill (CDP). Editor screenshots render at an inconsistent scale — trust `getBoundingClientRect` (CSS px) for clicks, not screenshot pixels. Page-level CDP is gated; drive ProseMirror with synthetic `keydown` (Enter/ArrowDown work; arrow-selection does not). Inner scroll container is `.editor-scroll`.

## Automation plan (goal #2)

Today's pipeline: `generate.sh` → `pt.md` (markdown) → `finalize.sh`/`substack.sh` (pandoc) → `substack.html` → `substack_post.py` (HTML→ProseMirror) → draft.

Two ways to emit the new format:

- **Option 1 — structured renderer (recommended).** Have generation output a structured edition object (stories with `tier` grande|media|pequena, `headline`, `body` paras, `cluster`, `links`) and render straight to ProseMirror JSON with a generalized version of `v2/build_format_options.py::option_D`. Bypasses pandoc; the format lives in code, not in fragile markdown conventions. The LLM decides prose + tiering; the renderer decides layout.
- **Option 2 — extend the markdown path.** Teach `GENERATION.md` to write the three tiers in markdown (H3 for grandes, H4+bullets for médias, a marked "Leia também" block) and teach `pipeline/tools/substack_post.py` to map them — crucially it has **no `calloutBlock` handling today**, so the Leia também box needs adding there.

Key files for #2:
- `newsletters/ai/prompts/GENERATION.md` — the generation prompt (voice + structure). Tiering heuristic lives here.
- `pipeline/generate.sh` — runs generation → `pt.md`.
- `pipeline/tools/substack_post.py` — HTML→ProseMirror converter (handles p/h1-6/ul/ol/li/strong/em/a/br/blockquote/hr; **missing calloutBlock**).
- `pipeline/substack.sh` / `pipeline/format.sh` — markdown→HTML stage.

Open design question for #2: **who decides tiering** — the generation LLM (semantic: importance/novelty), or a rule (lead = biggest market/funding/geopolitics; Leia também = single-fact items)? Lean LLM-decides with the heuristic written into GENERATION.md, since that also serves the voice goal ([[newsletter-v2-roadmap]] #6).

## Open decisions (carried from the chat)
- Tiering specifics: is LineShine / Oracle a *grande* instead of *média*? How many grandes (3 felt right)?
- Images: one per *grande*? *médias* and Leia também without?
- Paywall cut placement in the three-tier structure (after grandes? mid-médias?).

## File map
- `substack_inventory.md` — every format → API node mapping (task #4 output)
- `v2-context.md` — the original v2 brief (6 tasks)
- `v2/build_format_options.py` — reference renderer (A/B/C/D)
- `v2/build_inventory_draft.py` — the all-formats inventory draft builder
- memory: `newsletter-v2-roadmap`, `substack-format-inventory` (in `~/.claude/projects/-Users-guilherme-ai-newsletter/memory/`)
