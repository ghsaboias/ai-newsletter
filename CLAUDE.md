# Newsletter Platform

Multi-topic newsletter engine. Same pipeline, different configs. LLM handles facts, recency, accuracy. Human handles taste, writing, relevance. Learnings feed back into the agents/prompts so future generations need fewer corrections.

## Architecture

```
newsletters/
  ai/                          # AI & Tech newsletter (default)
    config.sh                  # clusters, byline, tools, title prefix
    prompts/RESEARCH.md        # research brief (injected into the researcher agents)
  ma/                          # M&A newsletter (dormant)
.claude/agents/                # the in-session pipeline:
                               #   researcher-{ai,hw,world}, facts, v2-generator,
                               #   extract, paywall-teaser, repetition-checker, fact-verifier
pipeline/                      # topic-agnostic helpers the agents call
  _lib.sh                      # loads topic config, shared utilities
  ingest.sh / rewrite-links.sh / substack-preview.sh
  tools/                       # dedup-research.py, link-tokens.py, substack_post.py, …
  output/<topic>/YYYY-MM-DD/   # namespaced by topic
```

Skills (global, `~/.claude/skills/`): `newsletter-research`, `newsletter-draft-v2`, `newsletter-no-dashes`.
All scripts default to topic `ai`. Override with `PIPELINE_TOPIC=ma`.

## Pipeline

One in-session agent chain, orchestrated by the `newsletter-draft-v2` skill (`/newsletter-draft-v2 [YYYY-MM-DD] [mini]`). No intermediate prose (`pt.md`); the product is a three-tier edition (**Grandes** / **Médias** / **Leia também**).

1. **research** — `newsletter-research` skill spawns 3 de-conflicted cluster researchers (ai / hw / world) + dedup → `research.json`
2. **facts** — `facts` agent atomizes research into a sourced fact base → `facts.md`
3. **v2** — `v2-generator` agent writes the tiered edition → `v2.md`
4. **link + paywall + push** — `extract` ∥ `paywall-teaser` → `ingest --execute` → `rewrite-links` → `substack-preview.sh` pushes **one** DJ-linked, paywalled Substack draft
5. **advisory checks** (non-gating, parallel) — `repetition-checker` ∥ `fact-verifier` → `repetition.json` + `fact-check.json`

The artifact is a Substack draft already DJ-linked and paywalled. **Human review happens in the Substack editor** — approving/adjusting tiering, adding images/video by hand. After the first push the Substack draft is source of truth; the skill never re-pushes. **Read memory first**: `~/.claude/projects/-Users-guilherme-ai-newsletter/memory/`

## Editorial Principles

1. **Freshness honesty** — never imply simultaneity between stories from different dates. Use "Separadamente" or acknowledge timing explicitly.
2. **No political editorializing** — don't frame political positions as deficiencies. Present facts neutrally.
3. **Explain jargon inline** — acronyms get brief parenthetical explainers on first use (RLHF, ARR, TCEQ). Technical terms like "yield" need plain-language rewrites.
4. **Clarity of reference** — vague terms need specifics ("plataformas" → "redes sociais"). Pronouns and verbs must be unambiguous about who does what to whom.
5. **Say what the company does** — don't assume the reader knows. One clause is enough.
7. **Repetition = reframe, not repeat** — if a number or narrative ran in recent editions, convey continuity or find the genuinely new angle. Don't present stale facts as fresh.
8. **Paragraph coherence** — stories live with their thematic neighbors. China trade investigations go with US-China tech friction, not the Iran thread.
9. **Kill low-signal items** — cut quotes and stories that add noise, not signal. No guilt.

## Adding a New Topic

1. `cp -r newsletters/ai newsletters/<topic>`
2. Edit `config.sh`: clusters, byline, title prefix, allowed tools, pre-research command
3. Edit `prompts/RESEARCH.md`: domain, voice, structure
4. Run the draft via the skill with `PIPELINE_TOPIC=<topic>`

## Posts (charts for Substack/social)

`posts/` holds per-edition chart HTML + JSON research data. Charts promote a specific edition; data is auditable.

Pattern:
1. Research data first. Save to `posts/data/<slug>.json` with `sources` (label + url) and `notes` (what's measured vs. estimated).
2. Build chart at `posts/chart-<slug>.html`. Self-contained. Chart.js via CDN. `animation: false`, `tooltip: { enabled: false }`.
3. Portuguese titles, source line, captions.

Brand:
- 720px card, `padding: 36px 40px`, white background
- H1: Helvetica Neue, 24px, weight 700, `letter-spacing: -0.8px`
- Header: title only, full width (`max-width: none`); `border-bottom: 3px solid #044B2E`. The DJ logo is NOT in the header (a header logo steals width and wraps long titles) — it goes inside the chart, see Logo below
- Footer: source label left, `dailyjournal.news` right; 10px, `#999`; `border-top: 1px solid #E5E5E5`
- Palette: `#044B2E` primary, `#7DB89B` projection/forecast, `#0012bf` `#D7001E` `#E88E00` `#E4ABEB` `#ccc` for multi-series

Logo: `<img src="../../daily-journal-platform/public/images/logo/logo-green-horizontal.png">`, placed *inside* the chart as a watermark — an absolutely-positioned `.chart-logo` (height ~15px) inside the `position:relative` `.chart-container`. Default bottom-right; move it to whichever plot quadrant is empty (visual judgment after rendering — a climbing series leaves the bottom-right open; a falling/left-heavy one needs it elsewhere). Align it to the plot, don't eyeball: measure with browser-eval (`Chart.getChart('<id>').chartArea` + the container's clientWidth/Height), then for bottom-right set `right = containerW − chartArea.right` (logo's right edge meets the x-axis line's end) and `bottom = containerH − chartArea.bottom + ~12` (a gap above the axis line). Canonical asset lives in daily-journal-platform; never duplicate into ai-newsletter.

Annotations: label endpoints and milestones only, not every bar. Use a Chart.js `afterDraw` plugin to draw value labels above bars.

Two-panel pattern works for time-series: long arc (annual) on top, recent acceleration (monthly) below — different time signatures, same y-axis unit.
