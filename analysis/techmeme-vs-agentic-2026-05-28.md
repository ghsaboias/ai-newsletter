# Techmeme vs agentic search — source attribution audit (update)

**Date of analysis:** 2026-05-29
**Window:** 7 editions since the last audit (2026-05-20, 05-21, 05-22, 05-25, 05-26, 05-27, 05-28). No editions on 05-23/05-24 (weekend).
**Extends:** [techmeme-vs-agentic-2026-05-19.md](techmeme-vs-agentic-2026-05-19.md) (the original 8-edition audit). Same method, same classifier conventions.
**Method:** 7 parallel sub-agents, one per edition. For each pt.md, split into distinct stories (one event = one story), matched to research.json by entities/headline/key_facts, then semantically classified against that day's Techmeme morning brief.
- For 05-21, 05-22, 05-25, 05-27, 05-28 the brief was read from each day's `.prompt-ai.md`.
- For 05-26 the brief was read from a standalone `techmeme.md` saved that morning.
- For 05-20 the brief was recovered from a research sub-agent session log (`7c05996c`) — that day's skill flow did not persist `.prompt-*.md`. Brief snapshot saved to `/tmp/techmeme-2026-05-20.txt` (ephemeral).

## Headline

**This window: 124 published stories. 69 from Techmeme (56%) · 55 from agentic search (44%).**

The Techmeme share dropped 8 points versus the original window (64% → 56%), driven almost entirely by two collapse days bracketing the US Memorial Day holiday.

**Full record to date (15 editions, 05-09 → 05-28): 252 stories. 151 Techmeme (60%) · 101 agentic (40%).**

## Per-edition breakdown (this window)

| Date | Brief size | Stories | Techmeme | Agentic | % Techmeme |
|------|-----------:|--------:|---------:|--------:|----------:|
| 2026-05-20 | 51 | 19 | 16 | 3 | **84%** |
| 2026-05-21 | 42 | 22 | 15 | 7 | 68% |
| 2026-05-22 | 43 | 17 | 11 | 6 | 65% |
| 2026-05-28 | 46 | 18 | 11 | 7 | 61% |
| 2026-05-27 | 39 | 20 | 11 | 9 | 55% |
| 2026-05-25 | 20 | 10 | 2 | 8 | 20% |
| 2026-05-26 | 23 | 18 | 3 | 15 | **17%** |
| **Total** | — | **124** | **69** | **55** | **56%** |

The spread is even wider than last window: a 5× gap between the best day (05-20, 84%) and the worst (05-26, 17%). Techmeme contribution remains volatile, not a steady floor — and this window produced the two lowest-yield days in the entire 15-edition record (previous low was 05-11 at 27%).

## The Memorial Day collapse

The two worst days, 05-25 (20%) and 05-26 (17%), bracket the US Memorial Day holiday (Monday 05-25). The mechanism is clean:

- **Techmeme's brief thins around US holidays.** 05-25 carried only 20 items and 05-26 only 23 — the two smallest briefs in the window, against 39–51 on normal days. US-tech-corporate news (the brief's core) slows when US markets and offices are closed.
- **The world doesn't stop.** Both editions ran heavy on clusters Techmeme structurally omits: the full geopolitics block (US-Iran deal, Russia's Oreshnik strike on Kyiv, HSBC oil/inflation, Asia heatwave on 05-25; Abraham Accords, Zelensky on 05-26), Asian infra (Vifan, Google's India hub, China's underwater data center), and biotech (Gilead Hepcludex, Eli Lilly retatrutide).
- **Divergence, not just thinness.** 05-26 proves brief *size* isn't the whole story: its 23-item brief skewed to stories the newsletter chose to skip (Pony AI, Spotify, FTC, EU Google fine, SoftBank, Tether), so even the available Techmeme stories didn't land. Low yield was thin-brief *and* editorial divergence stacked together.

This sharpens the original finding: **the agentic step is what carries the newsletter through US-holiday lulls.** On the two days Techmeme had the least to offer, agentic search supplied 83% and 83% of the edition.

## New pattern: agentic now substitutes inside Techmeme's core clusters

The original audit found agentic search did pure *scope expansion* — it only surfaced clusters Techmeme structurally omits (biotech, geopolitics, Asian rounds, early-stage), never the US-tech-corporate stories Techmeme owns.

That boundary broke on 05-26. With Techmeme's brief diverging hard, agentic search supplied stories squarely in Techmeme's home turf:
- **AI labs** (normally Techmeme-reliable): AlphaProof Nexus solving Erdős problems, Google's Agent Executor open-source runtime, Gemini 3.5 Flash Low, the METR deception study — all four agentic.
- **Chips** (normally Techmeme-reliable): AMD's HBM-bottleneck Computex story and the Blackstone-Google $5B TPU JV — both agentic.

So agentic search isn't *only* a coverage-surface extension anymore. On a day when Techmeme's ranking diverged from the newsletter's editorial picks, agentic search backfilled even AI-lab and chip stories. That's a more capable role than the original audit credited it with — and a useful insurance property, but also a signal that the two surfaces can drift out of agreement on what the day's tech story even is.

## What each surface still delivers

**Techmeme reliably surfaces** (confirmed again this window):
- Big-tech earnings and milestones (Nvidia record Q1, Xiaomi −57%, Micron/SK Hynix crossing $1T, Salesforce Agentforce ARR)
- Major funding/IPOs (SpaceX & OpenAI IPO filings, Cognition $26B, Hark $700M, Modal, Cursor, Exa, Fireworks, Baseten)
- The marquee AI-lab story of the day (Gemini 3.5 Flash at I/O, the Erdős proof, OpenAI Guaranteed Capacity, Karpathy → Anthropic)
- Chip-industry headlines (AMD Taiwan packaging, Samsung labor, Huawei Tau Scaling Law, China RTX ban)
- US tech-policy (Trump's killed AI EO, Newsom worker-displacement EO, Take It Down Act, Illinois SB 315)

**Agentic search is still the only path for** (55 stories this window):
- **Geopolitics / war / macro — 17 stories, every one agentic.** Iran threads (postponed strike, peace talks, Hormuz, Binance/IRGC funding sits on the techmeme side as a finance story), Xi-Putin summit, Russia's Oreshnik strike, gas prices, Fed minutes, Bank of Korea, Israel-Lebanon.
- **Biotech / FDA — 7 of 8 stories agentic.** GPCR miniproteins (Nature), FDA Baxfendy, Gilead Hepcludex, Eli Lilly retatrutide, AbbVie Decnupaz, Lucis, Rocklin's protein dataset. The lone exception: Perceptic's $12M seed (05-27) — Techmeme indexed it as a *funding round*, not as clinical/regulatory news. That's the seam: Techmeme catches biotech only when it's framed as a startup raise.
- **Asian funding & regional infra — 8 stories.** Robot Era/Geely, AGILINK, Bloom-Nebius, HIVE Toronto, Vifan, Google's $15B India hub, China's underwater data center, C2i Semiconductors India.
- **Early/mid-stage rounds below Techmeme's threshold** — Viktor $75M, Doozy, Pace $46M.

## Patterns worth noting

1. **Techmeme yield still tracks the brief's own AI-density, but divergence amplifies the low end.** Heavy AI day (05-20, Google I/O, 51-item brief) → 84%. Holiday lull with a diverging brief (05-26, 23 items) → 17%. The new lesson from 05-26 is that a thin brief *plus* editorial divergence compounds — you can't predict yield from brief size alone.

2. **Complementarity holds — still essentially zero redundancy.** Across all 124 stories, agents found no case where agentic search duplicated a story Techmeme already had on the same day. Where the same entity appeared on both sides (e.g. 05-22 Iran: Binance/IRGC funding was Techmeme #20, the uranium/Hormuz/oil thread was agentic), they were genuinely different events. The two surfaces expand each other rather than overlap.

3. **Brief persistence is still intermittent and still a risk.** 2 of 7 editions (05-20, 05-26) did not persist `.prompt-*.md`. 05-26 happened to have a manually-saved `techmeme.md`; 05-20's brief survived only because it was buried in a sub-agent session JSONL. The recommendation from the prior audit stands: **have the skill flow persist the morning brief to the edition directory.** It's the only evidence of what Techmeme delivered that morning, and the live page has moved on by the time anyone audits.

## Implication for the pipeline

The original takeaway holds and is now stress-tested: kill Techmeme and you lose ~56% of stories on a normal day but only ~17–20% on a holiday lull (because agentic already carries those days); kill agentic search and you lose the entire biotech and geopolitics blocks, most Asian funding/infra, *and* — as 05-26 showed — your only coverage on days when Techmeme's ranking diverges from your editorial line.

The two are complements. The 05-26 data adds a wrinkle: they can disagree about what the day's tech story even is. When they diverge, the newsletter currently follows agentic search. That's defensible (it kept 05-26 from being a 3-story edition) but worth a periodic human gut-check — a 17% Techmeme day is also a "did we miss what everyone else covered?" day.

## Data-integrity flag: untracked provenance

This window surfaced something the original did not: **2 published stories had no research.json match** (05-25 Gilead Hepcludex; 05-26 Eli Lilly retatrutide) — both biotech. The original window had zero. These facts entered pt.md without a logged source in research.json, meaning their provenance isn't auditable from the pipeline artifacts. Both are plausible and likely correct, but they were either written from model knowledge during generation or had their research entries pruned. Worth investigating: biotech is exactly the cluster where a hallucinated drug name or approval date would be hardest to catch and most damaging.

## Method notes / caveats

- Story-splitting granularity is "one event/announcement = one story," consistent with the prior audit. pt.md paragraphs that pack 2–3 events were split (e.g. 05-20 "Nvidia Vera CPU + Dell PowerEdge" → two stories; 05-22 Trump-EO postponement vs the Musk/Zuckerberg/Sacks lobbying angle → two).
- Semantic match criterion unchanged: same entity + same event = match (record brief item #); same entity + different event/angle = agentic.
- Subtitle/lede counted as a story only when it introduced something not in the body (e.g. 05-26 Blackstone-Google TPU JV appeared only in the subtitle).
- Per-story classifications with research IDs and Techmeme item numbers live in each sub-agent's output (this run) and were not concatenated into a standalone JSON. Re-run against this doc if a fuller table is needed.
- 05-20 brief reconstructed from `~/.claude/projects/-Users-guilherme-ai-newsletter/7c05996c*.jsonl`; line-number prefixes from the Read tool-result were stripped before classification.
