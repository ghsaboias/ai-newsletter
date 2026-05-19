# Techmeme vs agentic search — source attribution audit

**Date of analysis:** 2026-05-19
**Window:** 7 editions (2026-05-09, 05-11, 05-12, 05-13, 05-14, 05-15, 05-18)
**Method:** 4 parallel sub-agents. For each pt.md, split into distinct stories, matched to research.json by entities/headline/key_facts, then semantically classified against the `**Pre-research scan:**` section of `.prompt-ai.md` (Techmeme's ~30-story morning brief).

Today's edition (2026-05-19) excluded — the skill-flow migration changed file layout and `.prompt-*.md` is not preserved.

## Headline

**111 published stories total. 68 from Techmeme (61%) · 43 from agentic search (39%).** Zero ambiguous, zero pt.md stories without a research.json match.

## Per-edition breakdown

| Date | Stories | Techmeme | Agentic | % Techmeme |
|------|--------:|---------:|--------:|----------:|
| 2026-05-13 | 14 | 13 | 1 | **93%** |
| 2026-05-14 | 15 | 12 | 3 | 80% |
| 2026-05-09 | 15 | 10 | 5 | 67% |
| 2026-05-18 | 18 | 11 | 7 | 61% |
| 2026-05-15 | 19 | 11 | 8 | 58% |
| 2026-05-12 | 15 | 7 | 8 | 47% |
| 2026-05-11 | 15 | 4 | 11 | **27%** |
| **Total** | **111** | **68** | **43** | **61%** |

The headline 61/39 hides a 3.4× spread between best and worst day. Techmeme contribution is volatile, not a steady floor.

## What each surface actually delivers

**Techmeme reliably surfaces** (across all 7 days):
- US/Asia big-tech earnings (Foxconn, Cisco, Baidu, Alibaba, SoftBank, CXMT)
- AI lab announcements (Anthropic rounds, Claude safety research, Codex/Grok agent releases)
- IPOs and large funding rounds (Cerebras, Quantinuum, Anduril, Helsing, DayOne)
- Major-company M&A and acquisitions (Apple/Intel, Anthropic/Stainless, Microsoft/Inception, Analog Devices/Empower)
- Chip industry headlines (Samsung strike, NAND/DRAM pricing, motherboards)
- US tech-policy news (White House AI EO, Bannon letter, Anthropic-FSB)

**Agentic search is the only path for:**
- **Biotech / FDA approvals** — every Enhertu, Tecentriq, Bizengri, Beqalzi, Inqovi, Biogen, Ocrevus story was agentic. Techmeme structurally doesn't index this.
- **Geopolitics / war / macro** — Ukraine drone strikes, Iran/Hormuz, Trump-Xi summit news that broke after the morning brief, OPEC+, Fed/Treasury moves, UK elections, UAE Barakah strike.
- **Asian funding rounds & regional infra** — DeepSeek $7.35B, Samsung-AMD 2nm, MiniMax M2.1, Vbot, Unitree, Reliance Andhra data center, Tata-ASML India fab, AtkinsRéalis nuclear, regional data-center capex.
- **Early/mid-stage rounds below Techmeme's threshold** — Fractile $220M, Sereact, Tessera, Pit, WIRobotics.
- **Labor / employee organizing** — Meta MCI protest (the only agentic story on 05-13).

## Two patterns worth noting

1. **Techmeme yield correlates with Techmeme's own AI-density that day.** 05-11 had only 27 Techmeme items and a thin AI day → 27% yield. 05-13 had a brief packed with the day's marquee tech stories → 93% yield. The agentic step is what protects the newsletter from "Techmeme had a slow day."

2. **The agentic share is doing scope expansion, not redundancy.** In 111 stories, there were zero cases where agentic found the same story Techmeme already had. Across all 7 days the agentic-surfaced stories belong to clusters Techmeme structurally omits (biotech, macro/geopolitics, Asian rounds, early-stage). The value of the agentic step isn't "found the same news faster" — it's expanding the coverage surface beyond US-tech-corporate.

## Implication for the pipeline

If you killed Techmeme tomorrow, you'd lose ~60% of stories on average but **93% on a heavy AI-news day** — exactly when the newsletter most needs to land. If you killed agentic search, you'd lose the entire biotech and geopolitics blocks plus most Asian funding/infra coverage.

The two are complements, not redundancies. Today's skill-flow migration is a good moment to verify both paths are still wired in.

## Method notes / caveats

- Story-splitting granularity is "one event/announcement = one story." pt.md often packs 2-3 events per paragraph; agents split them. A pt.md paragraph covering "Apple MacBook Neo + Siri beta" was split into two stories, both matching Techmeme.
- Semantic match criterion: same entity + same event = match. Same entity + different angle = ambiguous (none triggered).
- Sample agent transcripts in `/private/tmp/claude-501/-Users-guilherme-ai-newsletter/.../tasks/` (ephemeral, not preserved).
- Per-story classifications with research IDs and Techmeme item numbers live in each agent's output and were not concatenated into a single JSON file — re-run against this doc if needed.
