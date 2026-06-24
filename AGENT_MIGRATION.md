# Newsletter Pipeline → Agent Migration

Living plan. We're migrating the newsletter pipeline from headless `claude -p`
shell steps to in-session **Agent-tool subagents**, and streamlining the shape
around the **v2 format** that started shipping **2026-06-24**.

Worked across multiple sessions. Update the Progress log as we go.

---

## North star

1. Replace each headless `claude -p` pipeline step with a custom subagent
   (`.claude/agents/*.md`), orchestrated in-session.
2. Add new agents for genuine gaps (fact-verify, PT proofread).
3. Streamline toward **research → facts → v2** directly — cutting the old
   full-prose `pt.md` / generator — **pending evals**.

## Decisions (as of 2026-06-24)

- **v2 is the product.** First shipped 2026-06-24. The three-tier format
  (Grandes / Médias / Leia também) is what goes out, not the old full-prose v1.
- **The shipped artifact is the live Substack draft**, not a local `.md`.
  Images, video, and last-mile text are hand-added in the editor. After the first
  push the Substack draft is source of truth; local files must not clobber it.
- **finalize must relink in place.** DJ-link rewriting has to PUT links onto the
  live ProseMirror body (mark-by-mark), not regenerate from a local md and
  re-push (that clobbers the hand-added media). On 2026-06-24 this was a
  hand-written `swap_links.py` — promote it to a real finalize step.
- **research → facts → v2 directly (cut `pt.md`/generator): DECIDED 2026-06-24.**
  The gating eval passed on craft (see log). `generate.sh` (`generator`) and
  `draft-rewrite.sh` (`draft-rewriter`) are **cuts** — deleted, not migrated.
  `repetition-check.sh` is **kept and migrated** to a `repetition-checker` agent
  (runs against the v2/facts output vs prior editions). Only open item: calibrate
  `v2-generator`'s selection-taste (Gui, later).
- **Phase 3 reorder — link BEFORE push, review IN Substack: DECIDED 2026-06-24 (Gui).**
  The artifact Gui reviews is a Substack draft that **already has DJ links in place**.
  So DJ-linking moves *ahead* of the push (baked onto `v2.md` → `v2-final.md`), not
  after it. Consequences: (a) the planned mark-by-mark **`relink-in-place` finalize
  step is RETIRED** — links are in the md before the first push, nothing to PUT onto a
  live body; (b) **no post-review re-push** from local md (it would clobber hand-added
  images/video/text — after the first push the Substack draft is source of truth);
  (c) `ingest --execute` (a real production DB write creating ~21 `auto_created` DJ
  news pages) now runs **before** review — Gui **accepted** this, incl. the orphan-page
  risk for any story cut in review; (d) the **paywall split is baked into the pre-review
  push** (`substack_post.py --paywall-after-grandes`), so the draft Gui reviews is
  already DJ-linked *and* paywalled.
- **`extract` → a facts.md-driven agent: DECIDED 2026-06-24 (Gui).** Extraction is a
  *data* op, so it keys off the *fact base* (`facts.md`), not the editorial product
  (`v2.md`) or raw `research.json`. facts.md already carries one `##` per story (= one
  DJ news entity — grouping done), per-story `**Fontes:**` blocks (= the multi-source
  array), and clean PT-BR atomic bullets (= entity/source bullets, already
  translated+glossed) — so facts→`sources.json` is near-mechanical and yields *richer
  multi-source* DJ pages than the old prose-parse. `research.json` stays the metadata
  lookup (per-source `published_at`/`image_url`/`title`, story `category`/`entities`).
  `links.json` then covers all Fontes URLs; `v2.md`'s ~25 anchors are a subset, so
  `rewrite-links --quiet` swaps them cleanly. Replaces the headless `claude -p`
  `extract.sh` + the prose-driven `SOURCE_EXTRACTION.md`.

## Target shape

```
PHASE 1 — DRAFT (in-session, subagents)
  research → 3 parallel `researcher-{ai,hw,world}` specialists → programmatic merge → research.json

PHASE 2 — DISTILL TO PRODUCT + PUBLISH DRAFT  (all in the `newsletter-draft-v2` skill)
  facts (`facts`)      → facts.md   (+ tokenize Fontes)
  v2 (`v2-generator`)  → v2.md      (+ expand source-link tokens)
  LINK + PAYWALL + PUSH (Step 3.5):
    extract (`extract`, facts.md-driven) ∥ paywall-teaser (`paywall-teaser`)
                                                      → sources.json + paywall-v2-meta.json
    ingest --execute                                  → links.json + ~21 DJ news pages
    rewrite-links --in v2.md --out v2-final.md --quiet → DJ links baked into the md
    substack-preview.sh v2-final.md draft "Leia também" --paywall-after-grandes
      --paywall-meta paywall-v2-meta.json             → push ONE Substack draft (DJ-linked + paywalled)
                                                         [create-once via .substack-draft-id]
  advisory ∥ (`repetition-checker` · `fact-verifier` on v2.md) → repetition.json + fact-check.json

PHASE 2.5 — REVIEW (human, IN Substack)
  review the DJ-linked + paywalled draft directly; hand-add images+video+text in the editor
  ← Substack draft is source of truth; NO further local re-push

PHASE 3 — (RETIRED) relink-in-place no longer exists — links are baked pre-push (decision above)
```

## Agent roster

| Agent | Status | Replaces / adds |
|---|---|---|
| `researcher-{ai,hw,world}` | **done + validated (v3)** | `research.sh` per-cluster `claude -p` (3 de-conflicted specialists) |
| `facts` | **done + validated live (w/ provenance)** | `facts.sh` |
| `v2-generator` | **done + validated live (craft eval + token-link fix)** | `v2-generate.sh` |
| `repetition-checker` | **done + validated live (advisory-only)** | `repetition-check.sh` |
| `extract` | **done + eval'd (facts.md-driven; 65/65 coverage, ingest dry-run clean)** | `extract.sh` + `SOURCE_EXTRACTION.md` (headless `claude -p`, prose-parse) |
| `paywall-teaser` | **done + eval'd (18/18 paid stories, 0 em-dash, injects clean)** | `paywall-teaser.sh --v2` + `PAYWALL_TEASER_V2.md` (headless `claude -p`) |
| `format` | planned (M&A-only) | `format.sh` |
| `fact-verifier` | **done + validated live (+ negative control)** | — (also: did v2 drop a load-bearing fact?) |
| `pt-proofreader` | deferred (Gui — maybe never) | — (flag-only, review-time) |
| `generator` | **CUT (decided 2026-06-24)** — no prose `pt.md` in research→facts→v2 | `generate.sh` → delete |
| `draft-rewriter` | **CUT (decided 2026-06-24)** | `draft-rewrite.sh` → delete |

---

## Progress log

### 2026-06-24 — research migration (session 1a35b534)

Scope: migrate the **research** phase only.

- Built a v1 single shared-prompt research agent (one prompt, dispatched 3× for
  ai/hw/world). Methodology stayed canonical in
  `newsletters/ai/prompts/RESEARCH.md`, passed as the task prompt (so the eval
  isolated the *mechanism*, not the prompt). **This v1 agent was superseded by
  the 3 specialists below and has since been removed.**
- Created `pipeline/tools/merge-research.sh` — programmatic jq merge, extracted
  verbatim from `research.sh` so both paths share it.
- Eval: spawned 3 `researcher` agents (ai/hw/world) for 2026-06-24 and compared
  against the script-based baseline (21 stories / 68 sources, from the 08:38
  `draft.sh` run). **[results appended below after the run]**

Findings / notes:
- `research.sh` flattens cluster categories via `eval echo "\$CLUSTER_X"`
  (newlines → spaces). Replicated here for a clean A/B; consider preserving
  newlines in the agent path later — likely the original intent.
- The `block-domains.json` settings hook isn't applied to subagents. The domain
  blocklist still lives in `RESEARCH.md` (prompt-level), so the guardrail is
  softer (instruction, not enforcement). Revisit if agents fetch blocked domains.

#### Eval results

Ran 3 `researcher` agents (ai/hw/world) for 2026-06-24, same date/window as the
08:38 `draft.sh` baseline. Parallel, ~3 min wall-clock; ~262k tokens total
(91k/78k/93k). Merged via `merge-research.sh`.

**Counts:** agent **19 stories / 50 sources** vs baseline **21 / 68**. (7+7+7=21
minus 2 id-collisions = 19.)

**Schema integrity: clean.** 0 orphan facts (every `key_fact.source_url` is a
listed source), no headline >100 chars, all categories in the allowed set, only
2 single-source stories.

**Coverage vs baseline:**
- **HW — near-identical (6/7).** Matched Agility SPAC, SK Hynix ADR, Qualcomm·
  ByteDance, Nvidia black-market, xLight, Hadrian. Missed only Cerebras Q1.
- **AI — strong + arguably better (4/7 match, 3 net-new).** Matched Claude Tag,
  Mistral OCR 4, Krea 2, Probook. Net-new incl. **OpenAI·Broadcom Jalapeño** —
  the day's biggest chip story, which the baseline *missed*. Dropped BioNeMo,
  Engram, Menlo Ventures.
- **World — high divergence (~1.5/7).** Only SpaceX Starfall cleanly matched;
  US-Iran appeared via a different facet (oil-sanctions waiver vs nuclear
  inspections). Missed the baseline's defense/geopolitics slate (Takeda, Poland
  Patriot, France drones, FCC AWS-3, Alibaba·Pentagon); went tech/biotech/space
  instead (Galectin MASH, Whoop FDA, China satellite).

**Verdict: the mechanism works.** Parallel subagents + programmatic merge produce
a valid, schema-conformant research.json. Quality on ai/hw is at or above the
script. World diverges — partly news moving (run 3h later), partly that "world"
is the broadest cluster with the most candidates for only 7 slots.

**Issues found (mechanism-level):**
1. **Path corruption.** The world agent hallucinated the output UUID and wrote to
   a stray dir; recovered by hand. Long opaque absolute paths are unsafe for
   agents to transcribe. → have agents **return JSON** (orchestrator writes), or
   use short/relative paths.
2. **Dedup is fragile.** 3 cross-cluster semantic dups (Jalapeño, SK Hynix,
   Agility); `unique_by(.id)` caught 2 but missed Agility (different slug, same
   story). → semantic dedup (headline/entity), not just id.
3. **Cluster beats overlap.** With one shared prompt, clusters grab the same big
   stories — wasted 3 of 21 slots, and `world` leaked into `hw`'s lane (SK Hynix,
   Agility) at the cost of its own defense/geopolitics beat. → **evidence for
   cluster-specialist agents with de-conflicted beats** (see below).
4. Minor: thinner sourcing (2.6 vs 3.2 sources/story).

**On 3 cluster-specialist agents (Gui's open question):** the eval *supports* it,
but for de-confliction, not raw quality — ai/hw were already great. Sharper,
non-overlapping beats would (a) kill the cross-cluster dups, (b) free `world`'s
slots for the geopolitics/defense stories it missed by spending them on chip
IPOs. Cheapest first step: tighten boundary language in the shared prompt / give
each cluster an explicit "not yours: X" line, re-eval, and only split into 3
agent files if overlap persists.

---

### 2026-06-24 — output-contract fix + 3 specialists (same session)

Decision (Gui): go **3 cluster specialists**, fix the output contract, re-eval.

Built:
- `.claude/agents/researcher-{ai,hw,world}.md` — 3 specialist agents. Each reuses
  the shared methodology (task prompt) and adds a **"Beat boundaries —
  de-confliction"** section: what it owns + what to leave to siblings (with the
  owning cluster named). Targets the 3 observed overlaps directly: silicon →
  hw (even from an AI lab); chip/robotics IPOs/SPACs → hw; AI-lab funding → ai.
- `pipeline/tools/dedup-research.py` — semantic merge. Beyond exact-id: collapses
  near-dups by headline similarity OR shared-org+category, keeps the richer
  story, and **reports cross-cluster collapses** (the overlap metric).

Output-contract fix: agents write to a **short, orchestrator-owned path**
(`/tmp/rsch3/<cluster>.json`, no UUID) copied verbatim, + a post-run landing
check and stray-dir sweep. Rationale: the programmatic jq/py merge needs files,
so literal "return JSON, orchestrator writes" would force hand-relaying ~28KB
blobs (its own corruption source); the real bug was the 60-char random UUID, so
a short semantic path + validation kills it cleanly. **Held — all 3 files landed
at the exact path, zero stray dirs** (v1 had the world agent hallucinate the UUID).

#### Eval results (v2, 3 specialists)

| run | stories | sources | cross-cluster dups | world cluster |
|---|---|---|---|---|
| baseline (script) | 21 | 68 | 0 | defense-heavy |
| v1 (1 shared prompt) | 19 | 50 | **3** (Jalapeño, SK Hynix, Agility) | leaked into hw |
| **v2 (3 specialists)** | **21** | **60** | **0** | **rescued** |

- **Overlap solved.** De-confliction took cross-cluster dups 3 → 0. The ai agent
  explicitly skipped Jalapeño (silicon → hw) and the Agility robot.
- **World rescued.** Now geopolitics (Iran nuclear talks), defense (Poland
  Patriots + Estonia IRIS-T — the baseline's Poland story is back), space
  (Starfall), biotech (Pfizer ADC Phase 3 miss), energy (DOE $17.5B nuclear),
  climate (Europe heatwave), macro (Brazil Selic). No chip-IPO leakage.
- **HW** owns Jalapeño / SK Hynix / Agility / Cerebras cleanly; **AI** is pure
  software/capabilities. Schema clean: 0 orphan facts, all categories valid.
- Dedup bug found + fixed: entity path was collapsing two *distinct* same-company
  stories (Claude Tag vs Mythos, jac=0.00) on SequenceMatcher ratio alone; now
  requires real token overlap.
- Minor residue: sources still a touch under baseline (60 vs 68; 2 single-source
  stories), 1 headline at 102 chars (Multiverse Pulsar). Candidates for a prompt
  tweak (≥2 sources) + a post-merge lint.

**Verdict: 3 specialists win.** Cleaner than the shared prompt and at/above the
script baseline. The de-confliction text lives in the agent files; the eval
injected the identical text via the task prompt (new agent files don't register
until a session restart — see constraint below), so the result is faithful.

> **Constraint learned:** `.claude/agents/*.md` files load at **session start**.
> A file written mid-session isn't callable until restart. Plan migrations so the
> agent files exist before the session that runs them (or restart between).

### 2026-06-24 — real specialists validated (v3, after restart)

Restarted so `researcher-{ai,hw,world}` registered. Ran them on prompts with
**no injected de-confliction** — so the beats came purely from the agent files.

Result: **21 stories / 58 sources, 0 cross-cluster dups, 0 orphan facts** — ≈ v2.
Each agent reasoned about its boundaries unprompted (ai → handed Jalapeño/Agility
to hw; world kept pharma M&A but dropped chip/AI financing). **The agent files
are self-sufficient; research migration is validated end-to-end.**

Note: macOS `/tmp` → `/private/tmp` symlink made the naive stray-dir sweep
false-positive. The production landing-check should just verify the 3 expected
files exist+validate (canonicalize before any stray hunt).

### 2026-06-24 — thinned `newsletter-research` skill + key accounts (same session)

The "wrap the orchestration as a reusable surface" item is **done**:
`~/.claude/skills/newsletter-research/SKILL.md` rewritten to a thin 7-step
orchestrator: window+idempotency → prev-headlines → **Techmeme once (inline)** →
read RESEARCH.md → dispatch `researcher-{ai,hw,world}` → `dedup-research.py`
merge → report.
- **Removed**: cluster-category injection (beats live in the agents now), the
  seeds 4th agent (nuked), the "why replaces research.sh" prose.
- **Kept inline** (validated, not bloat): RESEARCH.md + Techmeme + prev headlines.
- Rationale for thinness: the specialists own methodology/beat/de-confliction in
  their own system prompts, so the skill only does what an agent *can't* —
  pick one shared window, fetch the one shared input, dispatch, merge.

Agent files: added the missing "Key X accounts" so each beat is self-contained
without category injection — **then dropped 3 unverified handles** Gui flagged
(`@jimfanAI`, `@chilobrandt`, `@xaborsa`). They'd been copied verbatim from
`config.sh` without vetting; `@jimfanAI` is wrong (Jim Fan = `@DrJimFan`), the
other two unrecognizable. Now: `ai` keeps its 8 (all real), `hw` keeps
`@elonmusk` only, `world` has none (Key sources line only).

> ✅ **Resolved 2026-06-24 (next session):** the thinned skill ran live and
> passed — see the validation entry below. The handle-drop agent edits were live
> from session start (the run used them, no restart needed).
> ⚠️ Constraint still holds in general: agent-file edits written *mid-session*
> don't register until the next session.

### 2026-06-24 — thinned skill validated live (first run, new session)

First-ever execution of the thinned `newsletter-research` skill — the milestone
the UNRUN flag was waiting on. Ran ~13:35, full mode, with today's shipped
research backed up and **byte-exact reverted** afterward (md5-verified against the
baseline fingerprint; eval snapshots kept in scratch). All 7 steps clean: window
→ prev-headlines → one Techmeme fetch → RESEARCH.md → 3 parallel specialists →
`dedup-research.py` → report.

| run | stories | sources | cross-cluster dups |
|---|---|---|---|
| baseline (`draft.sh`, 08:08) | 21 | 68 | 0 |
| raw agents v3 (no skill) | 21 | 58 | 0 |
| **thinned skill (first live)** | **21** | **67** | **0** |

- **Mechanism validated.** 21/67 at baseline parity; dedup reported `21 → 21, 0
  collapsed (0 cross-cluster)`. De-confliction held with **no** category
  injection: `ai` handed Jalapeño + Agility to `hw`; `world` dropped the Energy
  Fuels rare-earth M&A to `hw` and filled its own lane (Iran talks, SpaceX
  Starfall, Colombia runoff, Brent/Hormuz, BOJ hike, Romania, Pfizer ADC miss).
- **3 prompt-level lints** (not mechanism): (1) 1 orphan fact — Cerebras cites a
  StockTitan 10-Q URL but lists the 8-K in `sources`; (2) 1 headline at 107 chars
  (Mythos); (3) 1 single-source story (BOJ). Reconfirms the two prompt tweaks
  already in Next, and adds an orphan-fact post-merge lint.
- Same session: **`config.sh` cleaned** (dropped `@jimfanAI`/`@chilobrandt` →
  `@elonmusk` only on line 55; removed the `@xaborsa` line — agents already
  matched) and **`researcher.md` removed** (v1 single shared-prompt agent,
  superseded by the 3 specialists).

### 2026-06-24 — de-confliction made canonical + validated (new session)

The hand-off matrix now lives in **one** place: a "Cluster boundaries
(de-confliction)" table in `RESEARCH.md` (injected into every agent), and the 3
agent files trimmed their duplicated "Not yours" blocks to a one-line pointer
("own your column; the matrix is in your brief"). Each `## Your beat` ownership
stays.

Validated after a session restart with a full live run (baseline backed up +
byte-exact reverted): **21 stories / 65 sources, 0 cross-cluster dups, 0 orphan
facts, 0 over-long headlines** — at/above the embedded-rules run, with
de-confliction reaching the agents **only** through the canonical matrix (the
agents are now trimmed). Each agent cited the matrix columns in its notes (`ai` →
Jalapeño / SK Hynix / Agility / RunPod / xLight to `hw`; `hw` → nuclear-energy
items to `world`; `world` → the chip selloff to `hw`). The salience worry didn't
materialize. The two earlier-flagged prompt lints (orphan fact, >100-char
headline) both came back clean this run.

### 2026-06-24 — `facts` agent built + eval'd (research→facts path)

Built `.claude/agents/facts.md` — the first step of Phase 2. Decision (Gui): test
the **straight research→facts path** (read `research.json` directly, skip the
prose `pt.md`/generator), since that's the architecture the "cut the generator"
lean points at. The agent absorbs the two jobs the generator silently did that
the old `facts.sh` (pt.md→facts) never saw: **EN→PT translation** and **jargon
glossing**; covers **all** stories with **no editorial selection** (tiering moves
to v2-generate); atomizes compound `key_facts` into one-fact bullets.

**Eval (vs today's shipped `facts.md`, derived from the reviewed pt.md):**

| | research→facts (agent) | pt.md→facts.md (shipped) |
|---|---|---|
| stories | **21** (full base) | 19 (review dropped Hadrian + Probook) |
| atomic facts | 256 (v1) / 215 (v2 run) | 148 |
| language | EN→PT, clean/natural | PT (generator already translated) |
| glossing | SPAC/PIPE/IPO/OCR/ADR/HBM/EUV/AIEA/VPU/NCII/CSAM — all accurate | same set, fewer |
| fidelity | **0 hallucinations** — every number/name/quote/benchmark traces to research.json | (trivially faithful) |

Method: avg `key_fact` is ~200 chars (rich, compound), so 98 key_facts atomizing
to ~215–256 bullets is legitimate, not invention — verified by grepping specific
high-risk claims (1260H, OlmOCRBench 85.20, "A Shortfall of Gravitas", Pieter
Abbeel, Brendan Carr, "Seventeen bidders", Summers 2,542) all present in
research.json. The only grep "misses" were the agent's correct PT-BR number
formatting (`14,0`, `2.542`) vs research's English (`14.0`, `2,542`).

**Provenance added (Gui's call), then re-validated.** The straight path drops the
link source `pt.md` provided, so the agent now closes each `##` with a
`**Fontes:**` block (`- <outlet> — <url>`, all of `sources[]`, URLs verbatim;
fact bullets stay link-free). Aligned to how v2-generate links (story-level, ~1
link/bullet). Re-run: **21/21 stories carry a Fontes block; all 68 source URLs
verbatim from research.json — 0 hallucinated, 0 altered, 0 leaked into fact
bullets.** Output format clean (verified SK Hynix + others).

**Verdict.** research→facts is faithful, complete, richer, well-translated,
well-glossed, and now carries link provenance. Strengthens the case to **cut the
generator/pt.md** — the generator's jobs (translate, gloss, select, trim, prose)
are now: translate+gloss → facts; select+trim+prose → v2-generate. The remaining
open test before committing the cut: **does v2-generate produce as good a product
from the rich 256-fact base as from the pre-trimmed 148-fact base?** (the
trimming the human review used to do now lands entirely on v2.)

> Both evals ran via prompt-injection into a `general-purpose` agent (the
> mid-session-written agent file doesn't register until reload — same technique
> as the researcher evals). Output is faithful to what the registered agent
> produces. **Provenance edit is mid-session → needs one reload to go live.**

### 2026-06-24 — `v2-generator` built + gating eval (research→facts→v2, no pt.md)

Built `.claude/agents/v2-generator.md` — terminal content step. Ports
V2_GENERATION.md's tuned tiering/subtitle/voice/mechanics faithfully; changes only
what the no-`pt.md` path needs: **links come from facts.md's `**Fontes:**` blocks**
(not pt.md), and the **title is built from facts.md's title line** (standing
`# [Tech] - Bem-vindo(a) a <data>`; `[Tech]` = config `TOPIC_TITLE_PREFIX`).
facts.md only — no pt.md dependency anywhere. Registered after reload; ran live
from a **paths-only** prompt → self-sufficient.

**Gating eval — rich research→facts base (today's `facts-live.md`, 21 stories /
253 facts / Fontes) vs today's shipped v2.md (human-trimmed 148-fact base + pt.md
links):**

| | shipped v2 (trimmed base + pt.md) | rich v2 (research→facts, no pt.md) |
|---|---|---|
| grandes ×3 | SK Hynix · **Alibaba · EUA-Irã** | SK Hynix · **Anthropic Claude Tag · Nvidia black-market** |
| lean | geopolitics-forward | **tech-forward** |
| clusters | 6 | 5 |
| leia também | FCC · Krea | FCC · Probook · Takeda |
| stories | 19 (Hadrian+Probook cut) | **21** (carries both) |
| links | from pt.md | **26/26 verbatim from Fontes — 0 invented** |
| craft | — | **at parity; no bloat from the bigger base** |

- **Mechanism flawless.** Correct title, 3/5/1 tiers, dividers, Fontes blocks
  dropped from output, every link traces to a Fontes URL of its own story.
- **The bloat worry didn't materialize.** The agent trimmed the 253-fact base to
  the same shape as the shipped edition; grandes are tight, médias are 1–2
  sentences, leia também headline-only.
- **The one real difference is editorial tiering taste** — which is exactly the
  judgment we moved into v2. The agent led tech-forward (Anthropic launch + Nvidia
  chips), demoting Alibaba + Iran to a Geopolítica cluster; Gui's review led
  geopolitics. Both defensible. Root cause: the prompt's only ranking signal is
  one line — `importância = relevância tech/IA + peso da notícia + relevância BR`
  — with no weighting/tiebreak, so the agent legitimately read product-launch
  salience above hard-news weight.

**Verdict.** research→facts→v2 produces a publishable edition with **no prose
intermediate**. The generator's mechanical jobs (translate/gloss/prose/link) are
fully absorbed; what's left in v2 is selection/tiering, and human review shifts
from *rewriting prose* to *approving/adjusting tiering* — less work, higher up the
stack. **Cut is justified on craft;** the open item is calibrating the tiering
taste (below), not the mechanism.

### 2026-06-24 — `repetition-checker` + `fact-verifier` built + validated (new session)

Decision (Gui): build the two review-time agents next, **defer `pt-proofreader`**
(may never do it). Both are **advisory-only** — they emit structured findings for
the human review; nothing auto-applies (the old `draft-rewrite` is cut). Authored
both in one batch, restarted to register, validated live on today's edition.

Built:
- `.claude/agents/repetition-checker.md` — migrates `repetition-check.sh`.
  Self-sufficient (methodology inlined like `facts`/`v2-generator`; task prompt
  passes only date + current-edition path + a list of prev-edition paths + output
  path). Reads the **`v2.md`** edition (not `pt.md`) vs prior editions; same
  `repetition.json` schema (`issues[]` of story/phrasing/framing + suggestion).
  Tuned for the itemized format (phrasing déjà-vu lives in `**Rótulo.**` labels,
  `###` headlines, bullet openers); keeps the entity-characterization rule (vary
  the angle, never remove). The orchestrator resolves which prev editions exist
  and passes their paths — handles the **mixed-format transition** (06-22 already
  has a `v2.md`; 06-23/06-19 are old `pt.md`).
- `.claude/agents/fact-verifier.md` (new) — two checks, advisory. **(1) Fidelity:**
  every number/name/quote/date/benchmark in `facts.md` **and** `v2.md` traces to
  `research.json`; flags altered values, non-literal quotes, **invented
  specificity**. Explicitly does *not* flag PT-BR number reformatting
  (`14.0`→`14,0`), jargon glosses, or faithful EN→PT translation — the
  false-positive traps from the facts eval. **(2) Dropped load-bearing fact:**
  only for stories that **made** the edition — did the trim cut an anchor fact
  (contract / size figure / load-bearing mechanism)? A story *demoted or cut on
  purpose* is out of scope (that's tiering). Has `Bash` to grep/jq-trace claims
  against `research.json`. Output `fact-check.json` (`fidelity_issues[]` +
  `dropped_facts[]`, severity-tagged).

#### Validation (today's edition, 2026-06-24)

- **`repetition-checker` — 6 issues (3 story / 2 phrasing / 1 framing).** Real
  catches: the SK Hynix **"Coroa"** bullet re-presenting a 2-day-old headline
  (SK Hynix > Samsung) as news ("Esta semana"); Iran-thread continuity (4th
  edition — flagged as *legitimate continuity but re-staged framing*, not lazy
  repetition); Pentagon-blacklist recap; HBM/EUV glosses (correctly "vary the
  angle, não remover"). Themes **converge with the shell baseline**
  (`repetition.json`, 9 issues) — Iran, blacklist, HBM glosses. The 6-vs-9 gap is
  expected: shell ran on prose `pt.md`, agent on the terser `v2.md`. Wrote to
  `repetition-agent.json` to keep the A/B clean.
- **`fact-verifier` — 0 fidelity / 0 dropped on the real edition.** Grep-traced
  dozens of specific claims (SK Hynix US$29,4 bi, Cerebras US$193,4 mi, US$20 bi
  OpenAI, FCC tranches, Menlo US$3 bi/US$14 bi, Agility US$420+200 mi …) — all
  confirmed. Correct **false-positive discipline** on 4 borderline items (RTX
  "150%" *derived* from 50k→130k yuan = 160%; "mid-70s" margins; "monopólio" vs
  "dominance"; Foxconn gloss) — traced + left unflagged.
- **Negative control (the load-bearing test).** A clean 0/0 only proves it doesn't
  false-positive — never that it *fires*. So: doctored a copy of `v2.md` with 3
  planted defects and re-ran. Caught **all 3, none spurious**: Cerebras
  `193,4`→`258,7` (`número alterado`, high — *reconciled the 94% growth arithmetic
  to prove 193,4 is right*); Claude Tag "5 milhões de usuários no primeiro dia"
  (`especificidade inventada`, high — noted research has no such figure); Menlo
  "US$3 bi, maior fundo" → "um novo fundo" (`dropped`, high — clincher: "o próprio
  slug da fonte diz `victorious-3b-fund`"). **A verifier that stays quiet when it
  should and fires when it should.**

**Verdict: both validated, both advisory.** Self-sufficient, paths-only dispatch —
identical to the shape the orchestration skill will use. `pt-proofreader` deferred.

### 2026-06-24 — `newsletter-draft-v2` skill + shadow eval + URL-token fix (new session)

Built the **orchestration skill** (Gui's call: a skill, not a rewired `draft.sh`)
and shadow-ran it against today's shipped edition.

- `~/.claude/skills/newsletter-draft-v2/SKILL.md` — thin, gated orchestrator of the
  **agent chain**: research (`newsletter-research` skill) → facts (`facts` agent) →
  v2 (`v2-generator` agent). Gates between steps (`set -euo pipefail` analog),
  idempotent resume, stops at the draft (no advisory checks, no finalize, no
  review). It's the **cutover candidate** to replace the old prose `newsletter-draft`.

**Shadow run (research frozen).** Ran at 16:12 BRT — 8h past the 08:00 baseline, so
fresh research would measure news drift, not the chain. Froze research to today's
`research.json` (that file *is* the research step's output; research was already
validated live today) and ran facts → v2 fresh into a scratch shadow dir, never
touching the shipped artifacts.

| | shadow (agent chain) | shipped (shell + human review) |
|---|---|---|
| facts | 21 stories / 317 bullets | 19 / 148 (review dropped Hadrian+Probook) |
| coverage | **all 21 placed** | 19 |
| grandes | SK Hynix · **Cerebras** · Alibaba | SK Hynix · Alibaba · **Irã** |
| links | 28, **27 trace / 1 ALTERED** | from pt.md |

- **Mechanism: PASS.** Both skill gates green (facts 21==21 Fontes; v2 3 grandes +
  6 clusters + Leia também). Subtitle = 3 curiosity questions on the grandes.
- **Tiering taste diverged** (expected): 3rd grande Cerebras (tech-forward) vs Iran
  (geopolitics-forward); Iran correctly *demoted* to a Mundo bullet, not dropped.
  This is a **third** different grandes set vs the gating eval's Anthropic+Nvidia —
  v2-generator's grande pick is unstable run-to-run → reinforces the deferred
  taste-calibration item.
- **Quirk:** the `facts` agent's return line miscounted ("16/191" vs actual
  21/317). The skill gate trusts the file, so harmless — but the summary line is
  unreliable; never gate on it.

**Bug found → root-caused → fixed (the eval's payoff).** v2-generator **altered a
URL**: it took the Qualcomm Yahoo article ID but spliced in `-services` from the
two *sibling* sources' slugs (`custom-chip-design-services-to-ByteDance`),
producing a 404-class link absent from both facts.md and research.json. Root cause
(same as the research-path corruption earlier in this doc): **agents hand-
transcribing long opaque URLs**. Fix (Gui picked "token links" over a lint or the
deepest research.json-id scheme):

- `pipeline/tools/link-tokens.py` — deterministic, two subcommands. `tokenize`
  adds `[S<n>]` tags to every facts.md Fontes source line (in place, idempotent,
  re-numbers fresh). `expand` resolves every `](S<n>)` in v2.md to the real URL
  from facts.md's token map and **hard-fails on unknown tokens or raw-URL
  regressions** (leaving the file untouched) — link provenance *by construction*,
  replacing the after-the-fact lint. Idempotent: a no-op on already-expanded v2.md.
- `v2-generator.md` — Links section rewritten: cite the **token** (`[âncora](S12)`),
  never a URL; schema + input examples updated to `[S<n>]`. The agent now copies a
  3-char tag, never an 80-char string — the corruption mode is gone.
- `newsletter-draft-v2/SKILL.md` — Step 2 runs `tokenize` after the facts gate;
  Step 3 runs `expand` after v2-generator (hard-fail halts the chain).

**Re-validated end-to-end** (v2-generator edit is mid-session → injected the
on-disk prompt into a `general-purpose` agent, the doc's standard technique, on the
**tokenized** facts): the agent emitted **26 token targets, 0 raw URLs**; `expand`
resolved all 26 (0 unknown / 0 regressions); the **Qualcomm link is now the correct
Yahoo URL**; `comm -23` of v2 URLs vs facts Fontes URLs is **empty** (100% trace).
The bug is structurally eliminated.

> **Mid-session edits pending one restart to go live:** `v2-generator.md` (token
> contract). `link-tokens.py` + `SKILL.md` are not agents and are live now. The
> `newsletter-draft-v2` skill registered immediately this session.
> ✅ **Restart done (next session, 2026-06-24)** — the `v2-generator` token
> contract is now live for the registered agent. See the run-attempt entry below.

### 2026-06-24 — advisory step wired + restart + live-run attempt (new session)

- **Advisory step added to `newsletter-draft-v2`** (Gui's call): after v2, the skill
  fires `repetition-checker ∥ fact-verifier` in **parallel, non-gating** (Step 4) →
  `repetition.json` + `fact-check.json` for the human review. Both audit the
  *finished edition*, so they can't run earlier (fact-verifier's dropped-fact check
  is facts.md-vs-edition; repetition-checker reads the published `v2.md`). The skill
  resolves prev-editions for repetition-checker (walk back 3 days, prefer `v2.md`,
  fall back to `pt.md`). Only the content steps (research/facts/v2) gate.
- **Restarted** → the `v2-generator` token contract is live for the registered agent
  (was injection-validated only, last session).
- **Live E2E run attempted via the skill, then interrupted** (Gui will do the full
  run in a fresh session). Got through Step 0 (date) + Step 1 dispatch (the 3
  research specialists) before stopping; nothing downstream ran.
- ⚠️ **Operational learning — do NOT run the skill on an already-shipped day's dir
  as-is.** `2026-06-24` already held the shipped edition, so (a) idempotency would
  *skip* research/facts/v2 (no real run), and (b) `tokenize` would **mutate the
  shipped `facts.md` in place** while advisory overwrote `repetition.json`. Two safe
  options: **(i) run the full E2E on the next un-shipped edition day** (no dir, no
  collision, real production conditions) — *recommended* for the fresh-session test;
  or **(ii)** backup → clear regen targets → run → restore byte-exact (done + md5-
  verified this session when the run was aborted).

### 2026-06-24 — full cold E2E run via the skill (backup dance) — the cutover gate cleared

The milestone the runbook was built for: the first **full cold end-to-end run** of
`/newsletter-draft-v2` with **fresh research** (not frozen / injected / shadow). Ran
option (ii) — backup → clear → run → restore — on the already-shipped 06-24 dir:
185-file persistent backup + md5 fingerprint → cleared the 8 regen targets → ran the
skill cold → restored byte-exact (full-dir verified, all 185 files). The fresh output
is preserved at `pipeline/output/ai/.eval-runs/2026-06-24-coldrun/` as an A/B data
point. ~16 min wall-clock. The research window is fixed (PREV 10:00 → DATE 10:00 BRT),
so running at 17:07 still researched the **same** 24h window as the 08:08 baseline —
drift is largely controlled by design.

**Mechanism: PASS — every gate green, no hand-holding.**

| step | result | gate |
|---|---|---|
| research (3 specialists ∥ → dedup) | 21 stories / 65 sources | **0 cross-cluster dups** |
| facts | 21 stories / 286 bullets / 21 Fontes | sections == Fontes ✓ |
| tokenize | 65 source tokens | — |
| v2 | 3 grandes / 6 clusters / 4 leia também | 3 grandes ✓ |
| expand | 25 tokens → URLs, **0 raw / 0 regressions** | hard-fail clean ✓ |
| advisory ∥ | repetition 6 issues · fact-check **0/0** | non-gating ✓ |

- **De-confliction held cold** (no category injection): `ai` handed Jalapeño, Qualcomm
  Dragonfly/Modular, SK Hynix, Agility, RunPod, Ornn, Qualcomm·ByteDance to `hw`;
  `world` stayed in geopolitics / biotech / non-tech finance and avoided the chip
  selloff. Merge: `21 → 21, 0 collapsed (0 cross-cluster)`.
- **Token contract held by construction** — the URL-corruption class is gone (25
  resolved, 0 raw URLs, 0 regressions).
- **repetition-checker handled the mixed-format transition** (v2.md vs a 06-23 `pt.md`
  + 06-22 `v2.md`): 6 nuanced issues — US-Iran 4th-edition continuity (lead with the
  new working groups, not the repeated mediators / 60-day clause), SK Hynix
  entity-characterization (vary the angle, **não remover**), Qualcomm-Modular "advanced
  talks → confirmed" progression, and a sophisticated *internal* same-edition framing
  mirror (Mythos ↔ China 360, both "model finds vulnerabilities"). **fact-verifier
  0 fidelity / 0 dropped** on the real edition.

**Reconfirmed quirks (none blocking):**
- The `facts` agent's **return-line miscount** fired again ("18 stories" vs the actual
  **21** on disk — 21 `##` / 21 Fontes / 286 bullets). The gate trusts the file → green.
  As logged: never gate on the summary line.
- **v2-generator's grande pick is still tech-forward and run-to-run unstable.** Cold
  grandes = **Jalapeño · SK Hynix · Mythos** (tech-forward); the shipped human-reviewed
  edition led **SK Hynix · Alibaba·Pentágono · EUA-Irã** (geopolitics-forward). That's a
  **fourth** distinct grandes set across the evals (gating: Anthropic+Nvidia; shadow:
  SK Hynix+Cerebras+Alibaba; cold: Jalapeño+SK Hynix+Mythos). Like the shadow run, it
  correctly **demoted** US-Iran to a Mundo bullet rather than dropping it → reinforces
  the deferred taste-calibration item, hard.

**Content is not directly comparable to the shipped edition.** The fresh 17:07 research
surfaced a substantially different slate than the 08:08 shipped run (Jalapeño /
Qualcomm-Dragonfly / Gemini-computer-use / 360-Tulongfeng / Runlayer / RunPod / Ornn /
Seltz / Energy-Fuels vs the shipped Cerebras / Alibaba / Mistral-OCR / Claude-Tag /
Menlo / Engram / xLight / France-drones / Poland-Patriot / BioNeMo / FCC) — partly news
moving across the day, partly research non-determinism. So this validates the
**mechanism**, which is exactly what a cutover test must prove; it is **not** a
content-equivalence claim.

**Verdict: the cutover gate is cleared.** The agent chain runs cold, end-to-end, fresh,
on a real day, every gate green, the link-corruption mode structurally eliminated.
Remaining for full cutover: **(b)** push ONE Substack draft from `v2.md`; **(c)** promote
`newsletter-draft-v2` → replace the prose `newsletter-draft` + fold in the v2 rename;
**then** delete the superseded `.sh`. v2-generator's grande taste stays a parallel
(Gui-owned) tuning track — not a mechanism blocker.

### 2026-06-24 — `extract` + `paywall-teaser` agents built + LINK+PUSH wired (new session)

Scope (Gui's call: "whole LINK+PUSH block"). Built the two remaining Phase-2 agents
and wired the full LINK+PAYWALL+PUSH block into `newsletter-draft-v2`. **Guardrail
held all session: no real `ingest --execute` and no live Substack push** — both evals
ran via the doc's standard injection technique + `ingest --dry-run`; the live writes
are the real cutover (Gui, fresh day). Shipped 06-24 artifacts untouched.

Built:
- `.claude/agents/extract.md` — facts.md-driven source extraction (replaces the
  prose-parse `extract.sh` + `SOURCE_EXTRACTION.md`). One `##` section → one news
  entity (grouping done); Fontes URLs (ignoring `[S<n>]` tokens) → the entity's
  multi-source array; **URL is the join key** into `research.json` for per-source
  `title`/`published_at`/`image_url`/`outlet` + story `category`/`entities`; PT-BR
  entity/source fields synthesized from the atomic facts. `tools: Read, Write, Bash`
  (Bash for a deterministic jq URL→metadata join + a coverage self-check). Schema
  unchanged → `ingest.ts` consumes as-is.
- `.claude/agents/paywall-teaser.md` — faithful port of `PAYWALL_TEASER_V2.md` (the
  decision-(d) gap fix; Gui chose "build the agent" over the headless `--v2` shell or
  a hand paywall). Reads `v2.md`, one teaser per **paid** story (each Médias bullet +
  each Leia-também item; the 3 Grandes stay free), writes `paywall-v2-meta.json`
  (`{cut_after: null, teasers[]}`) + `paywall-v2-teaser.md`. `tools: Read, Write`.

#### Evals (cold-run substrate `/.eval-runs/2026-06-24-coldrun/`, the real agent-chain
output: tokenized 21-story `facts.md` + matching `research.json` + `v2.md`)

| check | result |
|---|---|
| `extract` → sources.json | **21 entities / 65 sources**; `url_count` == actual |
| URL coverage | **65/65 Fontes URLs present, 0 missing, 0 invented/altered** |
| grouping / fields | 21 entities == 21 `##` sections; 0 over-long headlines; all categories in DJ vocab; per-source summaries lead with outlet; `entities` verbatim from research |
| **`ingest.ts --dry-run`** | **parses clean** — 65 articles / 65 article_ai / 21 news / 65 junctions; proper slugs + DJ URLs; wrote links.json (65 mappings) |
| rewrite-links precondition | v2.md's 25 anchors ⊆ links.json's 65 keys → **0 uncovered** |
| `paywall-teaser` → meta | **18 teasers == 18 paid bullets** (0 from Grandes); schema OK; **0 em-dashes**; all category labels; injects into `build_teaser_blockquote` (1 header + 18) |

- **One paywall-teaser voice nit (calibration, not a defect):** one teaser kept
  "Fase 3" (a digit the *vague* rule says to cut). Borderline — it's a clinical-phase
  label, not a quantity. Candidate tightening of rule 3, low priority.
- **Register note:** both new agent files are mid-session writes → callable as
  `subagent_type` only **after a restart**. The evals injected each on-disk prompt
  into a `general-purpose` agent (the doc's standard technique). The skill dispatch
  shape (`subagent_type: extract` / `paywall-teaser`, paths-only) is already wired.

Wired into `~/.claude/skills/newsletter-draft-v2/SKILL.md`:
- **Step 3.5 (LINK + PAYWALL + PUSH)** inserted between the v2 gate and advisory:
  **3.5a** `extract` ∥ `paywall-teaser` (parallel agents, independent inputs) →
  gate extract on `source_count>0 && url_count==actual`; **3.5b** `ingest.sh
  --execute` (skip if `links.json` exists) → gate on mappings>0; **3.5c**
  `rewrite-links.sh --in v2.md --out v2-final.md --quiet` → soft gate on DJ-link
  count; **3.5d** push ONE draft via `substack-preview.sh … draft "…" "Leia também"
  --paywall-after-grandes --paywall-meta paywall-v2-meta.json`.
- **Create-once push guard:** `.substack-draft-id` present → **skip** the push (never
  clobber the hand-edited editor copy). The doc's `--id-out .substack-draft-id`
  target = `substack-preview.sh`'s `draft` suffix.
- **Mini guard:** `mini` runs skip Step 3.5 entirely (no prod DB write, no live push).
- **Hand-off + charter flipped:** roll-up now surfaces sources/ingest/paywall + the
  **Substack draft URL**; the hand-off points the review *into Substack* (no
  `/newsletter-finalize`); description + behavioral rules + "Why this exists" updated
  to "links before push, review in Substack, never re-push"; skill is now the cutover
  candidate to replace **both** `newsletter-draft` *and* `newsletter-finalize`.

**Picked `substack-preview.sh` (not raw `substack_post.py`)** as the push tool — it
already does md→HTML, creds, the "Leia também" callout box, `--paywall-after-grandes`/
`--paywall-meta`, and idempotent create-or-update via `.substack-<suffix>-id`. The
planned `substack_post.py v2-final.md --paywall-after-grandes` shorthand glossed over
(a) md→HTML and (b) that `--paywall-after-grandes` is a **silent no-op without a
teaser meta** — which is the decision-(d) gap the `paywall-teaser` agent now closes.

**Remaining for cutover:** restart (register the 2 agents) → **ship ONE real edition**
through the skill on a fresh un-shipped day (the first real `ingest --execute` + live
paywalled push). Then → **Deletion**.

### 2026-06-24 — full inventory + bucket-(a) deletion (new session)

Did the ACTIVE track: re-derived the whole-surface wiring map fresh (the prior
map was flagged stale), partitioned into (a)/(b)/(c), backed everything up to git,
deleted bucket (a). Commits on `origin/main`: `f236923` (backup of the entire
migration surface — agents, new scripts/tools/prompts, edition text artifacts),
`b9bdce6` (the deletion).

**Inventory — the live `.sh` path and the agent path coexist; nothing in prod uses
the agents yet** (`cron.sh → draft.sh`/`finalize.sh` still orchestrate the headless
`.sh` steps via `tools/run-agent.sh`).

**Partition:**
- **(c) keep** — `_lib.sh`, `config.sh`, `ingest.sh`, `rewrite-links.sh`,
  `substack-preview.sh`, tools `dedup-research.py`/`link-tokens.py`/`substack_post.py`/
  `substack_upload.py`/`techmeme`/`techmeme.py`, `RESEARCH.md`, all 9 agents, skills
  `newsletter-research`/`newsletter-draft-v2`/`newsletter-no-dashes`.
- **(b) cutover-gated** — `cron.sh`, `draft.sh`, `finalize.sh`, `research.sh`,
  `generate.sh`, `repetition-check.sh`, `draft-rewrite.sh`, `facts.sh`,
  `v2-generate.sh`, `extract.sh`, `substack.sh`, `substack-post.sh`,
  `paywall-teaser.sh`, `sample.sh`; tools `run-agent.sh`, `slim_research.py`; prompts
  `GENERATION.md`/`DRAFT_REWRITE.md`/`SEEDS.md`/`FACTS.md`/`V2_GENERATION.md`/
  `REPETITION_CHECK.md`/`PAYWALL_TEASER.md`/`PAYWALL_TEASER_V2.md`/`SOURCE_EXTRACTION.md`;
  skills `newsletter-draft`/`-finalize`/`-generate`/`-draft-review`/`-rewrite`/
  `-paywall-teaser`.
- **(a) deleted now** — `tools/merge-research.sh`, `review.sh`, `review-parallel.sh`,
  `seed.sh` (all zero-caller, verified whole-repo).

**Two corrections to this doc (re-derivation caught both):**
1. **`merge-research.sh` was NOT "keep"** — nothing calls it; `dedup-research.py`
   (the research skill's merger) superseded it. Deleted.
2. **The old prompt briefs are bucket (b), not "keep as agent briefs."** The built
   agents inline all methodology and read **none** of `REPETITION_CHECK.md` /
   `PAYWALL_TEASER_V2.md` / etc. (only the researchers read `RESEARCH.md`, injected by
   the skill). Those prompts die with their `.sh` at cutover; zero cost to retain as docs.

**Notes / flags:**
- `substack_upload.py` is **not** an orphan — `substack_post.py` imports it. Kept.
- `format.sh` + `FORMAT.md` are **M&A-only**, outside the AI migration — kept, out of scope.
- `cron.sh → draft.sh` is the only production *entrypoint*; no crontab on this Mac and no
  recent `Auto: draft` commits — the daily auto-draft may already be dormant (Pi draft
  cron retired 2026-06-08). Verify Pi-side before retiring `draft.sh`; doesn't change the
  partition.
- `.gitignore` gained `.env.local` (Substack `SUBSTACK_SID` secret — was **not** ignored,
  nearly got pushed) + the `.eval-runs/`/`.shipped-backups/` local-scratch dirs. Edition
  image scratch (`images/_c*`) stays ignored; edition **text** artifacts are committed
  per the existing convention (18 text files/edition, zero images).

## Next

### ▶ ACTIVE — inventory + reliable-now deletion (cutover PARKED)

> **Step 1 (inventory) + step 3 (delete bucket (a)) DONE 2026-06-24** — see the progress
> entry above (commits `f236923` backup, `b9bdce6` deletion). Bucket (b) waits for the
> cutover; bucket (c) stays. What remains under this track is now just the cutover itself.

**Decision (2026-06-24, Gui): the cutover full-run is NOT the next step — parked.**
The whole agent chain is built, eval'd, and wired (LINK+PUSH entry above; the
`extract` + `paywall-teaser` agents are **registered now** — no restart pending). The
immediate track is **not** shipping an edition; it's mapping the surface and pruning
what's already safe to remove.

**Next session (Gui will drive):**
1. **Full inventory of the entire surface** — every `pipeline/*.sh`,
   `pipeline/tools/*`, `.claude/agents/*.md`, `~/.claude/skills/newsletter-*`, and the
   prompts (`newsletters/ai/prompts/*`, `pipeline/prompts/*`). For each: what it is,
   who calls it, and which lane it's in — **live `.sh` path** (`draft.sh`/`finalize.sh`
   still call it), **agent path** (the new chain uses it), or **orphan** (nothing calls
   it). Seed: the "who calls what" map in the Deletion section below — **re-derive and
   confirm it, don't trust it stale** (this session added `substack-preview.sh`,
   `paywall-teaser` agent, etc.).
2. **Partition** the surface into three buckets:
   - **(a) reliably deletable NOW** — dead/orphaned or fully superseded with **no live
     caller** (deletion is independent of the cutover).
   - **(b) deletable only after cutover** — still load-bearing for the live
     `draft.sh`/`finalize.sh` prose path.
   - **(c) keep** — tools the skill calls (`ingest.sh`, `rewrite-links.sh`,
     `substack-preview.sh`/`substack_post.py`, `link-tokens.py`, `dedup-research.py`,
     `merge-research.sh`).
3. **Delete bucket (a) now.** Leave (b) until the cutover.

**Cutover — PARKED (not scrapped).** Shipping one real edition through
`/newsletter-draft-v2` (first real `ingest --execute` + live paywalled push) is still
what unlocks the **big** deletions (bucket (b) — the live `.sh` orchestration). It is
no longer the immediate next step; inventory + reliable-now deletion comes first. When
it does run: confirm the reviewed Substack draft (DJ links in place, paywall after the
Grandes, "Leia também" callout). ⚠️ Step 3.5 now does **live** writes — `mini` skips it
(safe smoke test); a true LINK+PUSH test must be a real fresh edition, never an
already-shipped day.

- ~~Reload to register the provenance `facts` agent, then a real `subagent_type:
  facts` run~~ — ✅ **done** (validated live after reload): paths-only task prompt
  → 21/21 stories + Fontes blocks, 253 fact bullets, **68/68 source URLs verbatim,
  0 hallucinated / 0 altered / 0 leaked** — exact parity with the injected eval.
  The agent file is self-sufficient.
- ~~**Gating eval**: v2-generate from the rich research→facts base vs the trimmed
  pt.md→facts base~~ — ✅ **done** (2026-06-24, see entry above). Craft at parity,
  no bloat, links 26/26 from Fontes. Cut justified on craft; only tiering taste
  diverges.
- **[FUTURE — Gui will do later] Sharpen `v2-generator`'s selection criteria.**
  Today the only ranking signal is one line — `importância = relevância tech/IA +
  peso da notícia + relevância BR` — no weighting, no tiebreak, no candidate-grande
  heuristics. That's why the agent's grandes diverged from Gui's (tech-forward vs
  geopolitics-forward). Encode Gui's real tiering taste into the `## Os três níveis`
  block: (a) rank/weight the three importância factors, (b) candidate-grande rules
  (e.g. "a major US-China / geopolitics story is a grande candidate"; "a
  frontier-lab launch is a candidate but yields to a hard-news lead"), (c) a
  negative rule against 2-of-3 same-cluster grandes. Harvest from a few A/B days
  rather than guessing up front.
- **Orchestration cutover (this is what unlocks deletion).** Nothing in production
  uses the agents yet — `draft.sh` still calls the headless `.sh` steps end to end
  (it produced today's 08:08 edition). Build a Phase-2 agent orchestrator (skill or
  rewired `draft.sh`) that runs research(agents) → facts(agent) → v2(agent), cut
  production over to it, **then** delete the superseded shell steps. Until cutover,
  the `.sh` steps are load-bearing — see "Deletion" below.
- ~~Test the thinned `newsletter-research` skill live~~ — ✅ **done** (validated
  2026-06-24, first live run — see entry above).
- ~~Clean `config.sh` lines 55 & 69~~ — ✅ **done** (3 bad handles dropped).
- ~~Fold de-confliction into one canonical place~~ — ✅ **done** (2026-06-24):
  the hand-off matrix now lives once in `RESEARCH.md` ("Cluster boundaries
  (de-confliction)"), injected into every agent; the 3 agent files trimmed their
  duplicated "Not yours" blocks to a one-line pointer (each `## Your beat`
  ownership stays). ✅ **Validated after restart** (2026-06-24) — full live run:
  21/65, **0 cross-cluster dups**, 0 orphan facts, 0 over-long headlines, with
  de-confliction reaching the agents only via the canonical matrix. See the entry
  above.
- ~~Migrate `facts` and `v2-generator` to agents~~ — ✅ **done** (both validated
  live; see entries above).
- ~~Build the eval harness for cutting the full-prose `generator`~~ — ✅ **done**
  (the gating eval above served this; craft-cut justified, taste-calibration
  pending).
- ~~`fact-verifier` (advise, not gate — also: did v2 drop a load-bearing fact?)~~
  — ✅ **done + validated** (2026-06-24, see entry above; clean on the real
  edition + caught all 3 planted defects on a negative control). `pt-proofreader`
  (flag-only, review-time) **deferred** by Gui — may never build it.
- **Orchestration skill — BUILT + shadow-validated** (2026-06-24, see entry above):
  `~/.claude/skills/newsletter-draft-v2/SKILL.md` chains research → facts → v2 via
  the agents, with `tokenize`/`expand` link steps, and a final **advisory step** —
  `repetition-checker ∥ fact-verifier` run in parallel on the finished edition,
  non-gating → `repetition.json` + `fact-check.json` for the review (Gui's call:
  yes, after v2 — both need the edition as input, so they can't run earlier). Shadow
  ran clean against today's edition; URL-corruption bug found + fixed (token links).
  **Remaining for full cutover:** (a) ✅ **DONE** — cold E2E skill run, every gate
  green (2026-06-24); (b) ✅ **DONE** — the LINK+PUSH block (Step 3.5: extract ∥
  paywall-teaser → ingest → rewrite-links → substack-preview push) is built, eval'd,
  and wired (2026-06-24, see entry above); (c) promote `newsletter-draft-v2` → replace
  the old prose `newsletter-draft` **and** `newsletter-finalize`, fold in the v2
  rename — happens **at** the cutover (parked). Only after a real edition ships through
  it → delete superseded `.sh`.
- **v2 rename — DEFERRED into the cutover** (decided 2026-06-24). Drop the `v2`
  suffix (`v2-generator`/`V2_GENERATION.md`/`v2.md`), but **only as part of the
  cutover**, after the old prose `generate.sh`/`GENERATION.md` are deleted — doing
  it before would collide with those names. Skip renaming `v2-generate.sh` (it's
  deleted, not renamed). Mechanical once the old generator is gone.
- ~~Rework finalize's link step into `relink-in-place`~~ — **RETIRED** (Phase-3
  reorder decision, 2026-06-24): links are baked into the md **before** the first push
  (Step 3.5c `rewrite-links → v2-final.md`), so there's no live ProseMirror body to PUT
  onto. `swap_links.py` is **not** promoted; it can go in the inventory's bucket-(a)
  sweep (one-off hand script, no caller).

## Live-test runbook — running `/newsletter-draft-v2` on an already-shipped day

On a **fresh, un-shipped edition day** you just run `/newsletter-draft-v2` — no prep.
But to re-run it on a day that **already shipped** (e.g. for a live E2E test), the
day-dir already holds the edition, so: idempotency would *skip* research/facts/v2
(no real run), `tokenize` would **mutate the shipped `facts.md` in place**, and the
advisory step would overwrite `repetition.json`. Use this **backup → clear → run →
restore** dance. The backup goes to a **persistent** dot-prefixed location (not
scratch, which dies on session end; dot-prefix keeps it off the `YYYY-MM-DD` globs).

```bash
ROOT=/Users/guilherme/ai-newsletter
DATE=2026-06-24                                  # the shipped day to re-run
DIR=$ROOT/pipeline/output/ai/$DATE
BAK=$ROOT/pipeline/output/ai/.shipped-backups/$DATE

# 1. BACKUP (persistent) + fingerprint, so the restore is verifiable
mkdir -p "$ROOT/pipeline/output/ai/.shipped-backups"; rm -rf "$BAK"; cp -Rp "$DIR" "$BAK"
md5 -r "$BAK"/research.json "$BAK"/facts.md "$BAK"/v2.md "$BAK"/repetition.json "$BAK"/fact-check.json

# 2. CLEAR the regen targets so the skill runs fresh (all safe in $BAK)
rm -f "$DIR"/research.json "$DIR"/research-ai.json "$DIR"/research-hw.json \
      "$DIR"/research-world.json "$DIR"/facts.md "$DIR"/v2.md \
      "$DIR"/repetition.json "$DIR"/fact-check.json "$DIR"/techmeme.md

# 3. RUN  →  /newsletter-draft-v2 <DATE>   (review the fresh output it produces)

# 4. RESTORE the shipped edition byte-exact (LAST step, after review)
rsync -a --delete "$BAK/" "$DIR/"
md5 -r "$DIR"/research.json "$DIR"/facts.md "$DIR"/v2.md "$DIR"/repetition.json "$DIR"/fact-check.json
#   ↑ must match the fingerprints printed in step 1
```

Steps 1–2 run **before** invoking the skill; step 4 runs **after** the review. The
shipped artifacts are untracked in git, so `$BAK` is their only local copy until
restored — don't delete it before step 4.

## Deletion — what's safe to remove, and when

> **▶ Approach (2026-06-24, Gui): inventory-first, not cutover-first.** Next session
> does a **full inventory** of the surface (see ACTIVE above) and partitions it into
> **(a) reliably deletable now**, **(b) cutover-gated**, **(c) keep**. The text below
> is the *cutover-gated* analysis — it's still correct for bucket (b), but it is **not
> the whole story**: the inventory may surface bucket-(a) orphans (scripts nothing
> calls, fully-superseded files) that are deletable now, independent of the cutover.
> Re-derive the wiring map below before acting — it predates this session's additions
> (`substack-preview.sh`, `paywall-teaser` agent, `extract` agent, the wired Step 3.5).

**The big deletions are still cutover-gated.** The migration has built + validated
agent *replacements*, but the live *orchestration* has not been cut over:
`pipeline/draft.sh` still calls every headless `.sh` step directly (research →
generate → repetition-check → draft-rewrite → facts → v2-generate), and that is the
live path (it produced today's edition). The agents/skills run *in parallel* but
nothing in production invokes them. Deleting any **live-path** step script now breaks
`draft.sh` and its dependents — those wait for the cutover (bucket (b)).

Wiring as of 2026-06-24 — **STALE, re-derive in the inventory** (who calls what):
- `research.sh` ← `draft.sh`, `extract.sh`, `generate.sh`, `merge-research.sh`,
  `review.sh`
- `generate.sh` ← `draft.sh`, `draft-rewrite.sh`, `extract.sh`, `v2-generate.sh`,
  `sample.sh`, `review.sh`
- `repetition-check.sh` ← `draft.sh`, `draft-rewrite.sh`, `tests/test-draft.sh`
- `draft-rewrite.sh` ← `draft.sh`
- `facts.sh` ← `draft.sh`, `v2-generate.sh`
- `v2-generate.sh` ← `draft.sh`

**The cutover that unlocks deletion** (defined 2026-06-24): a real edition ships
end-to-end through `newsletter-draft-v2` *including the new LINK+PUSH block* — i.e.
the skill produces the **DJ-linked + paywalled Substack draft** Gui reviews, with no
shell `draft.sh`/`finalize.sh` in the loop. The cold E2E gate (research→facts→v2 +
advisory) is already cleared; LINK+PUSH (`extract` agent + Step 3.5) is the last build
before this.

Safe-deletion sequence (do in order):
1. **Cut over the orchestrator.** Ship a real edition through `newsletter-draft-v2`
   with LINK+PUSH wired (research/facts/v2 agents + `extract` agent + ingest/
   rewrite-links/substack push). Confirm the reviewed Substack draft is correct.
2. Once stable, delete the *replaced* content steps: `research.sh`, `facts.sh`,
   `v2-generate.sh`, **`extract.sh` + `SOURCE_EXTRACTION.md`** (→ `extract` agent),
   and the **v2 path of `paywall-teaser.sh` + `PAYWALL_TEASER_V2.md`** (→
   `paywall-teaser` agent; the script's v1/`pt.md` mode dies with the prose path)
   — **and** prune their references in `review.sh`, `merge-research.sh`, `sample.sh`.
3. Generator cut is **decided** (2026-06-24): delete `generate.sh` +
   `draft-rewrite.sh` + `GENERATION.md` and the `pt.md` track in
   `draft.sh`/`finalize.sh`. **`repetition-check.sh` is NOT deleted** — it's
   migrated to a `repetition-checker` agent (keep `REPETITION_CHECK.md` as its
   brief). Update `tests/test-draft.sh`.
4. **Shrink/retire `finalize.sh`.** Its extract→ingest→rewrite-links→push steps move
   *into the skill's Phase 2* (pre-review); the planned `relink-in-place` is **retired**
   (links baked pre-push). What's left post-review is hand-work in the editor (recs
   footer, video) — so `finalize.sh` either disappears or shrinks to a tiny optional
   helper. **KEEP the tools** the skill calls: `ingest.sh`, `rewrite-links.sh`,
   `substack-preview.sh` + `substack_post.py`, `link-tokens.py`, `dedup-research.py`,
   `merge-research.sh`.
5. Then retire `draft.sh` itself (skill fully orchestrates Phase 1–2 + publish).

Already removed (per log): the v1 single-shared-prompt `researcher.md`; and the
bucket-(a) orphans `tools/merge-research.sh`, `review.sh`, `review-parallel.sh`,
`seed.sh` (2026-06-24, commit `b9bdce6`). The repo-root `facts_*.md` are reference
fixtures — keep.
