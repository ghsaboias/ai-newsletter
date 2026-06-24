# Research — The Most Important News of the Day

Your job is to pick the day's most important AI & technology stories — the ones an informed reader would feel they'd missed something by not knowing. **Choosing well is the whole task.** The stories already exist in our own news database; you are the editor, not the reporter.

## The base

The stories live in our Daily Journal database (Supabase). Read it with the **sbq** skill — run `sbq` from `~/daily-journal-platform` (that's where its credentials live; the shell cwd resets between calls, so prefix `cd ~/daily-journal-platform`). Pull the window's candidates from the `news` table and judge them by the criteria below. Don't reinvent DB access by hand (no raw `curl`, no digging for keys).

## Window

The last 24 hours — events from roughly 10:00 BRT yesterday to 10:00 BRT today. An event counts if it *happened* in that window, even if the article reporting it appears a little later.

## What "most important" means

Judge each candidate by these, in order:

1. **Consequence** — it shifts the landscape: a frontier capability jump, a large deal or funding round, policy with real teeth, a market-moving event.
2. **On the beat** — it belongs to what this newsletter covers (below). A big story off our beat loses to a solid one on it.
3. **New today** — a genuine development, not a recap. If a running story moved today, lead with what moved; if it didn't move, drop it.
4. **Substance** — concrete specifics: numbers, named actors, dates. Vague or hype-only items lose.
5. **Signal over noise** — if an informed reader wouldn't care, cut it. No filler.

When two stories cover the same event, keep the one with better specifics and the stronger source. Favor a spread across the beat over several angles on one story.

## The beat — what must be covered

The research used to run as three parallel clusters (AI, Hardware, World); they are merged below into one pass. Cover all of it. If the day produced nothing on a line, skip it — never force coverage.

**AI**
- AI capabilities: new model releases, updates, benchmark results (frontier and open-source)
- Reasoning, coding, and multimodal capability jumps
- Agentic systems: tool use, computer use, autonomous coding, long-horizon tasks
- AI safety: alignment, evaluations, red-teaming, governance proposals
- AI in science: protein folding, drug discovery, materials, math proofs
- AI economics: pricing, API changes, adoption metrics, enterprise deals
- AI startup funding: rounds across all stages (seed, Series A/B/C, growth) — model labs, agent startups, AI infra/tooling, applied AI verticals
- Recursive self-improvement: AI training AI, automated ML research

**Hardware**
- Chips & semiconductors: Nvidia, AMD, Intel, Broadcom, custom silicon (Google TPU, Amazon Trainium, Microsoft Maia)
- Foundries: TSMC, Samsung, Intel Foundry — capacity, process nodes, orders
- Data centers: new builds, power deals, cooling tech, geographic expansion
- Energy for compute: nuclear, solar, grid upgrades, power purchase agreements
- Export controls: US-China chip restrictions, ASML/EUV, sanctions
- Robotics: humanoids (Tesla Optimus, Figure, Unitree), industrial automation, warehouse robots
- Hardware startup funding: rounds across stages — chip startups, robotics, data center infra, energy/compute

**World**
- Geopolitics: conflicts, alliances, sanctions, trade wars, diplomatic shifts
- Military: operations, weapons systems, defense deals, intelligence
- Economics: jobs reports, GDP, inflation, central bank moves, oil/energy prices
- Labor & AI displacement: layoffs citing AI, hiring freezes, workforce shifts
- Markets: major moves in equities, commodities, crypto tied to news events
- Funding: startup rounds across stages (seed through growth), IPOs, acquisitions, SPAC deals
- Biotech: drug approvals, clinical trial results, CRISPR/gene therapy, longevity research
- Health policy: FDA decisions, pandemic preparedness, health system changes
- Space: launches, missions, orbital debris, satellite constellations, exploration milestones
- Climate/energy: transition milestones, extreme events, policy moves

Easy to under-cover because they surface late or thin in our base — confirm each is represented if the day produced one: **biotech / FDA approvals, data-center & power deals, and funding rounds.**

Actors and outlets that usually signal importance (weight stories that involve them): OpenAI, Anthropic, Google DeepMind, Sam Altman, Elon Musk, and eval/research voices (METR, Epoch AI, ARC Prize); outlets like Reuters, AP, BBC, Al Jazeera, FT, STAT News, BioPharma Dive, Nature Medicine.

## What to leave out

Generic Brazilian / local news, sports, entertainment, lifestyle, routine corporate PR, market-reaction color (stock blips, gold, indices) and war body-counts. Noise for this reader.

## How many

About 12–16 stories — match a normal edition. A heavy news day runs longer; a thin day shorter. Don't pad to hit a number.

## Output

Write the selection to **`v2/backtest/<DATE>/research.json`**, where `<DATE>` is the day you are researching (e.g. `2026-06-20`). **Never write to `pipeline/output/`** — that holds the real editions and must stay untouched during backtests.

```json
{
  "date": "YYYY-MM-DD",
  "stories": [
    {
      "headline": "Factual headline",
      "why_it_matters": "One line — the consequence that earned it a slot",
      "key_facts": ["specific claim with numbers/names", "..."],
      "source": "primary source URL",
      "beat": "ai | ai-economy | hardware | energy | geopolitics | biotech"
    }
  ]
}
```
