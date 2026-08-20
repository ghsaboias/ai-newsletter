# Newsletter Workflow & Publishing Mechanics

The accumulated detail behind the newsletter's research → generation → publishing machinery: the publish gap, per-story media, the recommendations section, chart posts, and the Substack API/format reference.

> **Source of truth for the *current* pipeline is the repo `CLAUDE.md`** (the `research → facts → edition` agent chain orchestrated by the `newsletter-draft` skill). Some notes below were captured against the older `draft.sh` / `pt.md` / `finalize.sh` / `v2-generate.sh` path and are dated accordingly — the durable mechanics (Substack API, image insertion, publish gap, chart rendering, recs) still hold; the pipeline-plumbing specifics are historical context. Verify file/flag citations against current code before relying on them.

---

## The publish gap: `substack.html` ≠ the published post

The `.substack-draft.html` the pipeline generates is **only the article body**. What goes live has a **manual/injected layer** added at push time or by hand in the Substack editor. Confirmed by diffing the local artifact against the live post.

What the pipeline body does **not** contain, that appears only in the published post:
1. **Title & subtitle** — become Substack's own fields, not part of `body_html`.
2. **Paywall block** ("Abaixo, apenas para assinantes:") at the cut point. Above = free, below = paid. Teaser text comes from `paywall-meta.json`. **`substack_post.py` → `inject_paywall` injects teaser + paywall automatically** when creating the draft via API. If pasted into the editor by hand instead, it's manual.
   - **Only free readers see the teaser.** Since 2026-08-20 the blockquote is wrapped in Substack's audience-specific content block (`dynamicContent`, audiences `non_sub` + `free_sub`, no else branch), built by `wrap_for_free_readers`. Paid and founding subscribers get no "Abaixo, apenas para assinantes:" interruption between the Grandes and the Médias. In the editor it shows as an "SE / Público" box; tier availability is derived from the post's audience *except* above the `paywall` node, where it's treated as everyone — which is why a `non_sub`/`free_sub` block is valid on an `only_paid` post.
   - **Partner banner** between teaser and cut: **off since 2026-08-14** (the AbacatePay banner was removed; `TOPIC_PAYWALL_BANNER=""` in `newsletters/ai/config.sh` and the spec file is gone). The plumbing is intact for a future partner: upload the art with `python3 pipeline/tools/substack_upload.py <art.png> --href <url> > newsletters/ai/paywall-banner.json`, point `TOPIC_PAYWALL_BANNER` at it (or pass `--banner <file>` to `substack-preview.sh`), and `substack_post.py` inserts the `captionedImage`/`image2` node full-width (`resizeWidth: null`).
3. **Embeds/media** added in the editor: link cards (Reuters, National Geographic…), images, videos/tweets. None in the body.
4. **"Recomendações de hoje" section** at the foot (paid): video/interview picks. See the recommendations section below.
5. **Last-mile prose edits** in the editor.

**Fetch the live post and diff it** (`sstats` reads `.env.local` — now runs from anywhere, see operational-notes.md):
```bash
sstats post --meta | jq '{title,slug,wordcount,audience,canonical_url,post_date}'
sstats post --today --html > /tmp/published.html   # body_html, paywall bypassed (owner session)
pandoc -f html -t plain --wrap=none /tmp/published.html > /tmp/pub.txt
pandoc -f html -t plain --wrap=none <output>/.substack-draft.html > /tmp/loc.txt
diff /tmp/loc.txt /tmp/pub.txt
```
In the converted diff, "Ocorreu um erro / Não é possível executar o JavaScript" = an embed placeholder, **not** a real error.

**Why it matters:** when asked to review/audit "what was published," the local body misleads — it's missing the paywall, embeds, recommendations, and final edits. Fetch the live post; don't assume the local HTML equals what shipped. The paywall cut point and the recommendations section are Gui's per-edition decisions.

---

## Per-story images/videos

The newsletter's story images are added to the **live Substack draft** (they're not in the body HTML — see publish gap). Two halves: **which media to pick** (taste) and **how to insert it** (mechanics).

### Selection principles

Per-story image/video curation (inferred from Gui's manual editions, confirmed 2026-07-02). **Excludes** the "Leia também" recommendations.

- **One media per strong block, not per bullet.** Each category gets ~1 image, anchored on its most visual item. Pure-finance / pure-macro / pure-geopolitics stories usually get **no image** (low visual appeal).
- **Subject archetypes, in order:** (1) **face** of the person who personifies the company/decision; (2) **physical product** when it's the point (humanoid robot, chip/HBM module); (3) **product screenshot/UI** for software; (4) **editorial/stock** only as a fallback when there's no single subject.
- **Source priority:** first-party official asset > press photo (Reuters/Bloomberg) > stock/Wikimedia. Always credit.
- **Caption format:** `"<Sujeito>, <cargo/contexto>. Imagem: <Fonte>"` (PT-BR). A well-known face can drop the credit.
- **Prefer landscape** (~3:2 to 16:9). A near-square headshot is OK for a person.
- **Video** when the product *is* media/generative, or when a strong **official demo** exists. Send video as a link only — third-party/reviewer videos don't count as official.
- Contrast adjacent images (a person photo next to a building photo) when two similar stories sit together.
- **Don't** put two images of the same company in adjacent paragraphs; **don't** add a decorative stock image to a negotiation/geopolitics story that isn't a product launch; a deal/partnership with named principals (CEOs) gets their handshake/portrait, not "só logos."

### Insertion standard (`substack_mirror.py`)

Editorial images use **`resizeWidth: 520`** (px) — Gui's standard, set 2026-07-02 (after trying 560/560). Non-destructive update of the existing draft (**never rebuild from HTML after the first push; the Substack draft is source of truth**).

**Canonical edit loop = `pipeline/tools/substack_mirror.py`** (built 2026-07-02). The pushed `.substack-draft.html` is a stale one-way source — re-running `substack_post.py` from it **overwrites** the live draft and wipes images/video (that HTML re-push path is retired). Instead:
- `substack_mirror.py pull` writes `<edition-dir>/substack-body.json` (title/subtitle/body ProseMirror JSON, includes existing media); edit it; `push` PUTs it back preserving byline/section/audience/paywall.
- `substack_mirror.py media --plan images-final.json` = the unified "add per-story media" path: uploads each image to CDN at 520px, adds its caption, splits the story's `bullet_list` at `after_bullet` (omit for a Grande → after the whole list), embeds `videoId` (YouTube), then pushes. `--replace` makes it re-runnable (strips prior editorial media, keeps the href'd paywall banner + the Leia também callout); `--dry-run` previews.

**Gotchas:**
- **On PUT always send `draft_bylines:[{"id":473611573}]`** (the Daily Journal author). GET returns `draft_bylines:null`, so sending `[]` wipes the byline. Learned the hard way.
- When bulk-setting widths, **skip any href'd `captionedImage`** — a partner banner (none runs today) is an ad and stays full-width `resizeWidth:null`. Only images **without** an `href` are editorial → 520.
- Creds from env or `~/daily-journal-platform/.env.local` (`SUBSTACK_SID`, `SUBSTACK_PUB_HOST`), same loader as `substack_upload.py`.

### `newsletter-images` skill (built 2026-06-22, historical mechanics)

Automates the by-hand pick. Project-local `~/ai-newsletter/.claude/skills/newsletter-images/`. Recommendations-section videos are **out of scope**. `gather.py` is pure mechanism (curl + ImageMagick, no browser, no key); the LLM does the two judgment steps (author the per-story plan; rank → picks). Notable findings from building it:
- **Search arm = DuckDuckGo `i.js` JSON endpoint** (curl, no key, no per-call approval — browser-tools was rejected as approval-gated for an unattended pipeline). Two-step: GET `duckduckgo.com/?q=...&iax=images&ia=images`, scrape `vqd=([\d-]+)`, then GET `duckduckgo.com/i.js?...&vqd=...` with `Referer: https://duckduckgo.com/`. Landscape-filter on width/height.
- **og:image** = curl + regex `og:image`/`twitter:image`; filter placeholder logos (`default-logo`, `opengraph-illustration`, `social/images`, …).
- **Archetype router:** protagonist/team → image search on the person; official announcement → source og:image harvested from **all** sources (not just primary); benchmark/model card → scrape page-**body** `<img>` (the chart is in the body, not og); product/equipment → search + vendor site; scene/geopolitics → og or search.
- **Landscape is a strong PREFERENCE, not a hard cut** (a hard `width>height` empties the pool for less-photographed people and leaves only logos). Feed the vision ranker ~10 candidates, not 3.
- Every **skipped** story must be recorded (`{idx,label,skip:true,reason}`) so Gui can veto a skip — never omit silently.
- ImageMagick `montage`/`convert` exist but **Freetype/ghostscript missing → `-label`/`-pointsize` text fails**; montage without labels and track order in code.

---

## "Recomendações de hoje" — the video section

The published newsletter's paid "Recomendações de hoje" section (video/interview picks) has two related pieces: **building it** (`/newsletter-recs` skill) and **archiving it** (the noon Pi cron).

### `/newsletter-recs` skill (built 2026-07-07)

`.claude/skills/newsletter-recs/SKILL.md` auto-selects the videos **and** pushes the section into the day's Substack draft.
- `recommendations/gather-rec-candidates.py` — queries DJ `video_articles` (status='done') via `sbq --sql` (run from `~/daily-journal-platform`) for the **7 whitelisted channels**, dedups against YouTube IDs in `RECOMMENDATIONS.md`, keeps the 2 most-recent-unused per channel, parses chapters, and extracts `description_pt` = first paragraph of the video's `summary_md` (`## Contexto` block, markdown stripped — the rec's description verbatim, not a model rewrite).
- `pipeline/tools/substack_recs.py` — **the push**. Builds the recs section as ProseMirror nodes (heading L3 bold + paragraph bold `"Title:"` + `" desc:"` + `youtube2` embed with `startTime` `"Ns"`|null, `horizontal_rule` between videos), appends after the "Leia também" callout. **Idempotent** (strips existing recs first). `--id`/`--dir` push in place; `--duplicate-from POST_ID` copies to a `[TESTE]` draft (safe testing).
- `recommendations/render-recs-html.py` — HTML preview only (the real push uses PM nodes; HTML→PM would drop the YouTube embeds).
- **The 7 channels** (byte-for-byte match to the `channel` column): Sequoia Capital, Invest Like The Best, a16z, Dwarkesh Patel, Peter H. Diamandis, David Senra, All-In Podcast. DJ auto-ingests their newest uploads into `video_articles` daily.
- **Selection = taste:** pick 2 of the ≤14 candidates, favoring **AUTHORITY** (features an important tech figure) then **RECENCY**; keep the original title, write a 1–2 sentence PT-BR blurb, trim the start-time past the intro via parsed chapters.
- **Open gap:** the push does **not** yet append chosen IDs to `RECOMMENDATIONS.md`, so a dedup lag persists (recs pushed today aren't in the archive until the noon sync of the *published* post) — treat any recs already on today's post as used.

### The archive cron (`RECOMMENDATIONS.md`)

`recommendations/sync-recommendations.sh` — **Pi cron `0 12 * * *` BRT, runs from `~/ai-newsletter`**. Lists recent editions via `sstats emails --offset` pagination → for each date not already in the archive, `sstats post <id> --html` → `extract_recs.py` parses the section (uses the **last** "Recomendaç… de hoje" header, since some editions carry a pre-paywall teaser header) → appends → commit + push (scoped to the archive file only). Idempotent, so re-runs and weekends are safe. Log: `~/logs/newsletter-recs.log`. Format: `## YYYY-MM-DD`, `**title**`, description, `https://www.youtube.com/watch?v=ID`.

**`sstats` quirks:** the `emails` endpoint caps page size at ~20 (paginate with `--offset`); the `events`/growth feed trails publication by a few days (misses same-day editions), so it's unfit for the daily run.

**Pi git history note (resolved 2026-06-08):** `~/ai-newsletter` on the Pi used to be a diverged local-commit accumulator (an old 7am `cron.sh` did `draft.sh` + commit + push but never pulled). That draft cron was **disabled** and the clone `git reset --hard origin/main` back to a clean single-writer clone; the recs sync now runs from it. `pipeline/output/` **is** tracked on origin by design; only `pipeline/logs/`, `output/samples/`, `.review-session`, and `images/` scratch are gitignored. **`origin/main` advances on its own** from this noon cron — `git pull --rebase origin main` before pushing from any clone, or the push is rejected as non-fast-forward.

---

## Chart posts (`/chart-post`)

Recurring task: "craft a substack post with a chart" off the day's edition. Chart = reliable historical/comparison data that tells the story on its own; promotes that edition. Files in `posts/` (brand spec in `CLAUDE.md` "Posts"). Full skill: `.claude/skills/chart-post/`.

**Flow:** read today's edition → propose 3–4 chart candidates via AskUserQuestion (ASCII previews) → Gui picks → research from **PRIMARY** sources (annual reports, official releases — not aggregators; Exa + WebFetch) → present verified data + surface any method fork via AskUserQuestion → build by copying brand scaffolding from an existing `posts/chart-*.html` → render → iterate labels on screenshots → write prose.

**Gui's data-rigor taste (the heart of it):**
- **Citable > derived.** He rejects numbers computed/interpolated (e.g. a cumulative built by summing annual shipments). Plot the raw reported series.
- **Drop the problematic series rather than fudge it** (06-18 cut the US for methodology mismatch; 06-19 cut China's flat "0" line). The dropped angle moves to the prose, not the chart.
- **Currency:** keep the source's native unit when converting adds an assumption (06-19: € not US$, because €→US$ needs a rate = a derived number). Flag the trade-off, recommend the citable one.
- **Preliminary/forecast data is fine IF marked:** projection color `#7DB89B`, dashed segment, hollow point, `≥`/`~`/"est." labels.
- **All ressalvas go in the chart caption, NOT the prose.** Post prose = the story paragraphs only. Caption carries: what's measured (flow vs stock), price/method notes, what's estimated. Currency caveat lives in the legend label.
- **Method fork — self-reported vs third-party:** when a company's own prospectus/PR claims a number and an independent research house (Omdia/IDC/Counterpoint) measures a different one, use the **third-party, single source for the whole chart** and put the discrepancy in the caption bridge — never splice the self-reported number onto the third-party tail.

**Render mechanics — `render.sh` is platform-aware (2026-07-06 port):**
- **Mac:** browser-tools into the **real Brave**, not headless (headless Brave hangs on first-run profile setup). `cd ~/agent-tools/browser-tools`; target flag is `-t=ID` (**with** equals). 2× retina export = measure card height → resize → **reload after forcing `deviceScaleFactor:2`** (Chart.js rasters the canvas at load-time DPR, so DSF must be set *before* reload or the canvas is pixelated while HTML text stays sharp — that split is the tell) → screenshot → crop to `#capture` ×2.
- **Pi (Linux):** headless Chromium via `.claude/skills/chart-post/headless-render.js` (dependency-free CDP, Node 22 built-in WebSocket) — same output, verified pixel-close to the Mac render (Pi crops via CDP screenshot clip, needs no ImageMagick).
- `render.sh <slug> --eval '<js>'` works on both platforms for chartArea/logo measurements.
- To judge label overlap, crop the PNG (`magick <png> -crop WxH+X+Y +repage /tmp/x.png`) then Read it — a full-image Read downscales too much to see collisions.

**Scaffold bugs to fix when copying an old `chart-*.html`:** legend swatch not vertically centered (use per-item `inline-flex; align-items:center`, drop `vertical-align` from `.swatch`); logo placement is per-chart visual judgment, not always bottom-right (may center within an empty gridline band — measure with `c.scales.x.getPixelForValue(...)`); short/clear title beats descriptive-long (the angle stays in the subtitle). **Dual-axis gridline alignment:** pick maxes so tick fractions coincide (e.g. left 0/25/50/75, right €0/€6/€12/€18); keep `grid` on one axis only. Posts are committed to the repo (charts + `posts/data/*.json` auditable data), then pasted into the Substack editor by hand (publish gap).

---

## Substack editor format ↔ API reference

The full catalog of Substack editor formats and how to produce each via the API lives in the repo: **`~/ai-newsletter/substack_inventory.md`** (v2 work, 2026-06-23).

- Substack editor = **TipTap/ProseMirror**. A post body is a PM doc (`{"type":"doc","content":[…]}`) stringified into `draft_body`. Every format is a block node or an inline mark.
- API: `POST /api/v1/drafts` (create), `GET /api/v1/drafts/<id>` (read body back), `POST /api/v1/image` (upload). Auth header `Cookie: substack.sid=<SID>`; creds in `~/daily-journal-platform/.env.local`. Used by `pipeline/tools/substack_post.py` (HTML→PM converter) + `substack_upload.py`.
- **Probing method that worked:** create a sandbox draft → insert blocks via the live editor (browser-tools CDP) → `GET` the body to read authoritative node JSON. Page-level CDP is gated in Brave 146 (the daemon holds the one browser connection), so drive ProseMirror with **synthetic `keydown` events** (Enter/ArrowDown work; arrows-for-selection do NOT — need trusted events). For marks, use the **stored-mark trick**: caret in a paragraph → toggle mark → type → typed text carries the mark.
- **Realistic palette:** headings H2–H4, `calloutBlock` (teaser box), `bullet_list`/`ordered_list`, `horizontal_rule`, `blockquote`, footnotes (`footnoteAnchor`+`footnote`), `button`, `paywall`, `captionedImage`.
- `substack_post.py --callout-heading "<section>"` post-processes the HTML→PM doc to wrap a heading + its list into a `calloutBlock` — **so the markdown path produces calloutBlock** (used for the "Leia também" box).

---

## v2 format restructure (history — now the current format)

The three-tier format was designed and automated 2026-06-23. It **is** the current published format (see `CLAUDE.md`); the plumbing below is historical (the old `draft.sh` steps have since been replaced by the agent pipeline).

**The format (three-tier depth ladder, block size = importance):**
- **Grandes** — the must-reads: `### real headline` + labeled bullets (`**Dívida.** / **Ação.** / **Compute.**`). **Capped at 3, no fixed count** (see the tiering rule in editorial-principles.md).
- **Médias** — the substantial middle, grouped into `#### thematic clusters` (Segurança · Infra & energia · Hardware & modelos · Mundo…), one dense bullet each (`**Entidade.** + 1 sentence`).
- **Leia também** — the genuinely minor/off-core items as **headline-only links** (no description), in a **callout box**. World/politics/climate stories drop here even when big in absolute terms — tech-relevance ranks them down.
- The generation step decides tiering (importance × tech-relevance × BR-audience).

**Paywall placement = after the Grandes**, deterministic: `substack_post.py --paywall-after-grandes` sets `cut_after` = the index of the first `horizontal_rule` (the divider after Grande #3). Grandes are free; Médias + Leia também + recs are paid. The cut is **structural**, not count-based — safe regardless of how many Grandes.

**v2 roadmap (2026-06-23) — 6 tasks, status:**
1. **DJ db audit** — were past-edition stories in the DJ db *before* ingest? Which areas can the db be trusted as a research source? (Input to #2.) *[open]*
2. **Simplify research** — drop the 3-cluster fan-out, use the DJ db (Techmeme already ingested) as pre-made research + thin agentic search for gaps. Depends on #1. *[open]*
3. **Ingestion clustering check** — verify article ingestion goes through the app's matching/clustering logic instead of creating duplicates within thresholds. *[open]*
4. **Explore Substack formats** — **DONE** (the format inventory above).
5. **Restructure the newsletter** — **DONE + automated** (the three-tier format above).
6. **Draft voice = zero human corrections** — the one Gui calls most important. Neutral, dense, content speaks for itself. **The correction trail in editorial-review-log.md IS the spec** — fold those learnings into the generation prompt so the draft needs no per-paragraph hand-edits. *[ongoing]*

Hard orderings: #1→#2, #4→#5. Everything else is reorderable by taste.

---

## Coverage direction: startup funding (Vini)

Cover **more startup funding rounds** in the AI/Tech newsletter — a **mix of stages**: include early-stage (seed, Series A), not just megarounds, but not *only* early-stage either. Goal is broader coverage of the funding landscape, not a pivot to one stage.

**Why:** editorial direction from Vinicius Gushiken (co-byline) — the newsletter is underweight on the startup formation/funding signal relative to model releases and big-tech moves.

**How to apply:** during research, actively look for funding-round news (seed → late-stage) in AI/tech, not just M&A and IPOs; weight a well-sourced Series A or seed as a viable pick — don't auto-skip it for being "small"; mix stages across editions. AI newsletter only (`newsletters/ai/`), not the M&A topic.
