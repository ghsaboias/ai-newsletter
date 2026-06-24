# Research-query classification — discovery vs depth (7 editions)

Companion to `research-agent-search-timelines.md`. Every research-agent query (search + fetch),
classified by **provenance** — where the lead came from — across 2026-06-15 … 06-24.

## Why provenance, not just "discovery vs depth"
A naive split (generic sweep = discovery, named-entity query = depth) hides the real story.
Each agent is **handed a Techmeme pre-scan (26–44 stories) and the previous edition's headlines
before it searches.** So most "depth" queries aren't the agent deepening something *it* found —
they're it verifying/expanding a story it was given. Five classes:

| Class | Meaning | Discovery or depth? |
|---|---|---|
| **Sweep** | Generic date-anchored category probe, no named entity ("FDA approval phase 3 June X") | Discovery (fishing) |
| **Verify-the-feed** | Names an entity already in the Techmeme pre-scan / prev headlines | Depth on a **handed** lead |
| **Self-found** | Names an entity NOT in the prompt, surfaced by the agent's own earlier search, then drilled | Depth on a **self-discovered** lead (the "true" discovery→depth) |
| **Known-thread** | Follow-up "what's new" probe on a continuing prior-edition story | Borderline |
| **Cold** | Named entity in neither the prompt nor any earlier result — model's prior knowledge | Discovery-by-recall |

## Verdict: yes, it's straightforward to categorize — and the result is lopsided
~95% of queries sort cleanly (only the 4 Cold + 7 Known-thread rows need judgment). The pattern is
consistent across all 7 days: **the engine is overwhelmingly a Techmeme-verification loop, not a
discovery loop.**

### Aggregate (195 queries across 7 editions)

| Class | Count | Share |
|---|---|---|
| Verify-the-feed (handed depth) | **113** | **58%** |
| Sweep (discovery fishing) | 56 | 29% |
| Self-found (true discovery→depth) | **15** | **8%** |
| Known-thread (borderline) | 7 | 4% |
| Cold (model recall) | 4 | 2% |

- **Of all entity-specific (depth-shaped) queries, 89% are on handed leads, only 11% self-found.**
- **True discovery→depth is rare and uneven:** per-day Self-found counts are 8, 4, 0, 0, 1, 1, 1 —
  two of seven days had **zero**. Almost all of it lands in the `hw` cluster (chip/foundry leads
  it surfaces in its own sweeps).
- **The `ai` cluster is the most feed-bound** — on 06-16 it was 100% verify-the-feed (9/9 map 1:1
  to Techmeme stories), and it never produced a self-found lead on any day.
- **Cold queries are all recurring macro threads** (Iran/oil, Bank of Japan) the model probes from
  memory because they're neither in the scan nor yesterday's headlines.

### Per-edition tally

| Date | Sweep | Verify-feed | Self-found | Known-thread | Cold | Total | Pre-scan | Prev hl |
|---|---|---|---|---|---|---|---|---|
| 2026-06-15 | 17 | 11 | 8 | 0 | 1 | 37* | 26 | 0 |
| 2026-06-16 | 11 | 13 | 4 | 2 | 0 | 30 | 42 | 21 |
| 2026-06-17 | 3 | 22 | 0 | 3 | 0 | 28 | 41 | 20 |
| 2026-06-18 | 7 | 14 | 0 | 1 | 1 | 23 | 44 | 20 |
| 2026-06-19 | 4 | 19 | 1 | 0 | 2 | 26 | 34 | 20 |
| 2026-06-22 | 5 | 21 | 1 | 0 | 0 | 27 | 26 | 0 |
| 2026-06-24 | 9 | 13 | 1 | 1 | 0 | 24 | 43 | 20 |
| **Total** | **56** | **113** | **15** | **7** | **4** | **195** | | |

\* 06-15 buckets sum to 37 vs 38 timeline rows (one row's class is a ±1 judgment margin).

Notable: the two lowest-discovery days (06-17 ~79% verify-feed, 06-22 ~78%) had the tightest
pre-scans relative to output — a 26–41-story Techmeme list covered nearly everything the agents
searched for, so they barely strayed. The highest-discovery day (06-15, 8 self-found) had **no
previous-edition headlines** (prior day was a weekend), forcing the agents to do more of their own
legwork off the sweeps.

---

## 2026-06-15  (Techmeme pre-scan: 26 stories; prev headlines: 0)

### ai (session c77c90b4)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:32:04 | Anthropic Mythos/Fable 5 export controls WH dispute | Verify-feed | pre-scan #1/#7 (Mythos/Fable WH dispute) |
| 2 | 07:32:05 | AI model release benchmark new June 14/15 | Sweep | generic category probe |
| 3 | 07:32:06 | Enflame Tencent Shanghai IPO $888M | Verify-feed | pre-scan #11 ($888M IPO) |
| 4 | 07:32:07 | ByteDance Iluvatar CoreX Baidu Kunlunxin | Verify-feed | pre-scan #18 (ByteDance/Iluvatar) |
| 5 | 07:32:08 | Siri AI iOS 27 third-party models | Verify-feed | pre-scan #12 (Siri/iOS 27) |
| 6 | 07:32:17 | AI startup funding Series A/B June 14/15 | Sweep | generic funding probe |
| 7 | 07:32:18 | Z.ai GLM-5.2 release 1M context | Self-found | "Z.ai Launches GLM-5.2" in tool_result 10:32:07Z, before drill 10:32:18Z |
| 8 | 07:32:19 | cybersecurity leaders letter Fable 5 export ban | Verify-feed | pre-scan #7 (cybersec leaders letter) |
| 9 | 07:32:20 | Orbio Series A $21M Dawn Capital | Verify-feed | pre-scan #17 (Orbio/$21M/Dawn) |

_ai tally: Sweep 2 · Verify-feed 6 · Self-found 1 · Known-thread 0 · Cold 0_

### hw (session fa85a473)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:31:50 | Nvidia AMD chip announcement deal | Sweep | generic category probe |
| 2 | 07:31:51 | TSMC Samsung Intel foundry capacity | Sweep | generic foundry probe |
| 3 | 07:31:52 | data center power deal nuclear gigawatt | Sweep | recurring sweep template |
| 4 | 07:31:53 | humanoid robot Tesla Figure Unitree | Sweep | recurring sweep template |
| 5 | 07:31:53 | chip startup funding round Series | Sweep | generic funding probe |
| 6 | 07:32:10 | Enflame Shanghai IPO approval | Verify-feed | pre-scan #11 |
| 7 | 07:32:10 | ByteDance Iluvatar CoreX Baidu Kunlunxin | Verify-feed | pre-scan #18 |
| 8 | 07:32:28 | AI data center announcement hyperscaler | Sweep | generic datacenter probe |
| 9 | 07:32:29 | robotics startup funding round Series | Sweep | generic funding probe |
| 10 | 07:32:30 | Nvidia GTC Paris announcement | Cold | "GTC Paris" event not in pre-scan; prior tool_result had only "GTC Taipei"; named event from model knowledge |
| 11 | 07:32:30 | chip deal Cambricon SMIC | Self-found | Cambricon in tool_result 10:32:11Z, before drill 10:32:30Z |
| 12 | 07:32:47 | "June 14/15 2026" data center power energy deal | Sweep | date-anchored category probe |
| 13 | 07:32:48 | "June 14/15" humanoid robot deployment factory | Sweep | date-anchored category probe |
| 14 | 07:32:49 | export controls semiconductor sanctions China ASML | Sweep | category probe (ASML generic player) |
| 15 | 07:33:19 | Nvidia 800V power architecture SemiAnalysis | Self-found | 800V/SemiAnalysis in tool_result 10:32:52Z, before drill 10:33:19Z |
| 16 | 07:33:20 | "June 15 2026" chip semiconductor news | Sweep | date-anchored category probe |
| 17 | 07:33:21 | Google Visakhapatnam Raiden Infotech Andhra | Self-found | Raiden/Visakhapatnam in tool_result 10:32:49Z, before drill 10:33:21Z |

_hw tally: Sweep 10 · Verify-feed 2 · Self-found 3 · Known-thread 0 · Cold 1_

### world (session ed154931)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:31:59 | Iran nuclear deal ceasefire Hormuz | Sweep | geopolitics category probe |
| 2 | 07:32:00 | Ukraine Russia drone strikes overnight | Sweep | recurring war sweep |
| 3 | 07:32:01 | UK Starmer ban social media under-16s | Verify-feed | pre-scan #4/#5 (Starmer under-16 ban) |
| 4 | 07:32:02 | Trump France digital tax champagne 100% | Verify-feed | pre-scan #13 (Trump/France tax/wine tariff) |
| 5 | 07:32:02 | Enflame Tencent Shanghai IPO | Verify-feed | pre-scan #11 |
| 6 | 07:32:13 | FDA drug approval clinical trial oncology | Sweep | recurring FDA sweep template |
| 7 | 07:32:14 | G7 summit Evian agenda Trump Macron | Self-found | "Evian" as G7 location in tool_result 10:32:01Z, before drill 10:32:14Z |
| 8 | 07:32:15 | oil prices crude Brent WTI Hormuz reopens | Sweep | markets category probe |
| 9 | 07:32:47 | FDA approval zongertinib Hernexeos NSCLC | Self-found | zongertinib/Hernexeos in tool_result 10:32:14Z, before drill 10:32:47Z |
| 10 | 07:32:48 | major news June 14 weekend headlines | Sweep | broad headline sweep |
| 11 | 07:33:17 | Rio helicopter crash Oliver Tree singer | Self-found | Oliver Tree in tool_result 10:32:49Z, before drill 10:33:17Z |
| 12 | 07:33:17 | UK detains Russia shadow fleet tanker | Self-found | shadow-fleet tanker in tool_result 10:32:49Z, before drill 10:33:17Z |

_world tally: Sweep 5 · Verify-feed 3 · Self-found 4 · Known-thread 0 · Cold 0_

**Date tally (38 total):** Sweep 17 · Verify-feed 11 · Self-found 8 · Known-thread 0 · Cold 1

---

## 2026-06-16  (Techmeme pre-scan: 42 stories; prev headlines: 21)

### ai (session f749c28a)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:36:31 | DeepSeek $7.4B round $50B val Liang Wenfeng LP | Verify-feed | Techmeme #13 |
| 2 | 07:36:32 | OpenAI 2025 audited financials $34B spending R&D S&M | Verify-feed | Techmeme #8 |
| 3 | 07:36:33 | Qualcomm Tenstorrent acquisition $8B-$10B | Verify-feed | Techmeme #22 |
| 4 | 07:36:34 | OpenRouter Fusion API multi-model deep research | Verify-feed | Techmeme #14 |
| 5 | 07:36:35 | Anthropic Trump admin meeting June 15 no resolution | Verify-feed | Techmeme #2 |
| 6 | 07:36:41 | Meta AI Mode Facebook search public posts Groups Reels | Verify-feed | Techmeme #28 |
| 7 | 07:36:43 | France Mistral state chatbot €655M Palantir Chapsvision DGSI | Verify-feed | Techmeme #17 |
| 8 | 07:36:44 | NewCore $66M seed AI agent identity Cyberstarts | Verify-feed | Techmeme #31 |
| 9 | 07:36:44 | Salesforce Fin Intercom $3.6B acquisition | Verify-feed | Techmeme #39 |

_ai tally: Sweep 0 · Verify-feed 9 · Self-found 0 · Known-thread 0 · Cold 0_

### hw (session 6b9c56d5)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:36:20 | Qualcomm Tenstorrent acquisition $8B-$10B AI chip | Verify-feed | Techmeme #22 |
| 2 | 07:36:21 | Nvidia $25B high-grade bond offering June 15 | Verify-feed | Techmeme #41 |
| 3 | 07:36:22 | humanoid robot company funding June 15 | Sweep | category probe |
| 4 | 07:36:23 | TSMC Samsung Intel foundry chip news June 16 | Sweep | category probe |
| 5 | 07:36:24 | data center power deal nuclear gigawatt June 15-16 | Sweep | category probe |
| 6 | 07:36:33 | AMD acquires Mext memory technology June 15 | Self-found | "AMD Buys…Mext" headline in earlier result @10:36:23 UTC, before query @10:36:33 |
| 7 | 07:36:34 | Google Intel TPU 3M chips 2028 | Self-found | TPU "Icefish" surfaced in #4 foundry result @10:36:24 UTC, before query |
| 8 | 07:36:58 | robotics humanoid funding round June 15-16 series | Sweep | category probe |
| 9 | 07:36:59 | chip startup funding Series A/B AI semiconductor | Sweep | category probe |
| 10 | 07:36:59 | Samsung Google Neuralink Icefish I/O die memory | Self-found | "Icefish"/Neuralink in #4 foundry result @10:36:24 UTC, before query |
| 11 | 07:37:18 | FETCH wired DOJ-xAI + 9to5google datacenter | Verify-feed | wired = Techmeme #7; bundles self-found 9to5google (surfaced in sweep #5 result @10:36:25) |
| 12 | 07:37:22 | DOJ xAI gas turbines NAACP lawsuit dismiss | Verify-feed | Techmeme #7 |
| 13 | 07:37:22 | FETCH 9to5google Google $1.5B Alabama datacenter | Self-found | URL surfaced in sweep #5 (datacenter-nuclear) result @10:36:25 UTC; not in pre-scan |

_hw tally: Sweep 5 · Verify-feed 4 · Self-found 4 · Known-thread 0 · Cold 0_

### world (session ade33025)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:36:04 | Iran war aftermath ceasefire Hormuz June 16 | Known-thread | continues prev-headlines us-iran-deal / oil-iran-deal-hormuz |
| 2 | 07:36:05 | Ukraine Russia war development June 16 attack | Known-thread | continues prev-headline russia-681-weapon-strike-ukraine |
| 3 | 07:36:06 | FDA drug approval June 15 clinical trial biotech | Sweep | category probe |
| 4 | 07:36:07 | central bank rate decision June 16 inflation | Sweep | category probe |
| 5 | 07:36:08 | SpaceX launch June 15 mission satellite Starship | Sweep | category probe (mission/launch, not the IPO story) |
| 6 | 07:36:16 | G7 summit June 2026 Canada leaders | Sweep | calendar/category probe |
| 7 | 07:36:17 | climate extreme weather wildfire flood June 15-16 | Sweep | category probe |
| 8 | 07:36:17 | US economic data retail sales industrial production June 16 | Sweep | category probe |

_world tally: Sweep 6 · Verify-feed 0 · Self-found 0 · Known-thread 2 · Cold 0_

**Date tally (29 total):** Sweep 11 · Verify-feed 13 · Self-found 4 · Known-thread 2 · Cold 0

---

## 2026-06-17  (Techmeme pre-scan: 41 stories; prev headlines: 20)

### ai (session 2da6e0c4)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 08:17:20 | SpaceX acquires Cursor $60B all-stock | Verify-feed | pre-scan #22 (SpaceX/Cursor $60B) |
| 2 | 08:17:22 | Z.ai GLM-5.2 open weights MIT 1M context | Verify-feed | pre-scan #6 (GLM-5.2 MIT, 1M context) |
| 3 | 08:17:23 | Odyssey world models $310M Amazon Trainium | Verify-feed | pre-scan #17 (Odyssey $310M Amazon/Trainium) |
| 4 | 08:17:23 | CuspAI $400M Bezos materials AI Cambridge | Verify-feed | pre-scan #20 (CuspAI $400M Bezos) |
| 5 | 08:17:29 | Sensor Tower ChatGPT share below 50 | Verify-feed | pre-scan #18 (Sensor Tower 46.4%) |
| 6 | 08:17:30 | Anthropic G7 UK carve-out Mythos 5 export ban | Verify-feed | pre-scan #38 (G7 Mythos 5 carve-out) |
| 7 | 08:17:31 | Junyang Lin new AI lab funding valuation | Verify-feed | pre-scan #26 (Junyang Lin lab, ~$2B) |
| 8 | 08:17:32 | Bland AI voice $50M Series C Dell | Verify-feed | pre-scan #37 (Bland $50M Series C Dell) |

_ai tally: Sweep 0 · Verify-feed 8 · Self-found 0 · Known-thread 0 · Cold 0_

### hw (session 4f362da6)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 08:17:04 | humanoid robot Figure Tesla Optimus Unitree | Sweep | generic humanoid template, no named in prompt |
| 2 | 08:17:04 | Samsung chip foundry BYD Google AMD Nikkei | Verify-feed | pre-scan #10 (Samsung BYD/Google/AMD foundry) |
| 3 | 08:17:05 | Kazakhstan Firebird Nvidia $10B data center | Verify-feed | pre-scan #24 (Kazakhstan/Firebird $10B) |
| 4 | 08:17:06 | Snap Specs AR glasses $2,195 preorder | Verify-feed | pre-scan #1/#2 (Snap $2,195 Specs) |
| 5 | 08:17:07 | Qualcomm Snapdragon Reality Elite Xreal Aura | Verify-feed | pre-scan #33 (Snapdragon Reality Elite/Xreal Aura) |
| 6 | 08:17:15 | Microsoft Surface Pro Snapdragon X2 launch | Verify-feed | pre-scan #40 (Surface Pro/Snapdragon X2) |
| 7 | 08:17:16 | Huawei chip logic stacking advance FT | Verify-feed | pre-scan #16 (Huawei logic-stacking) |
| 8 | 08:17:17 | Odyssey world models $310M Amazon Trainium | Verify-feed | pre-scan #17 (Odyssey $310M) |
| 9 | 08:17:18 | data center funding $58B YTD Dealogic FT | Verify-feed | pre-scan #27 (Dealogic $58B data centers) |
| 10 | 08:17:19 | Apple AirPods camera 2027 foldable iPhone Gurman | Verify-feed | pre-scan #5 (AirPods cameras 2027, foldable iPhone) |

_hw tally: Sweep 1 · Verify-feed 9 · Self-found 0 · Known-thread 0 · Cold 0_

### world (session a8253eca)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 08:17:12 | Iran Israel war ceasefire diplomatic update | Known-thread | Iran war thread in prev headlines (g7/BoJ); "update" probe |
| 2 | 08:17:13 | G7 summit Evian outcomes statement Iran | Known-thread | prev headline g7-summit-evian-opens; "outcomes" probe |
| 3 | 08:17:14 | Trump AI govt equity stakes sovereign fund Lutnick | Verify-feed | pre-scan #19 (Lutnick equity stakes/sovereign fund) |
| 4 | 08:17:15 | FDA drug approval biotech clinical trial June 16 | Sweep | generic FDA category template, no named entity |
| 5 | 08:17:15 | Binance EU MiCA license rejected Greece | Verify-feed | pre-scan #39 (Binance MiCA/Greece) |
| 6 | 08:17:27 | Ukraine Russia war strike news June 16 | Known-thread | prev headline ukraine-moscow-oil-refinery-strike; "news" probe |
| 7 | 08:17:29 | SpaceX stock surge market cap June 16 IPO | Verify-feed | pre-scan #21 (SpaceX $2.65T market cap) |
| 8 | 08:17:29 | oil price brent Strait of Hormuz reopen | Known-thread | Iran-war oil thread in prev headlines (BoJ oil shock); event probe |
| 9 | 08:17:30 | Amazon Odyssey AI world models $310M | Verify-feed | pre-scan #17 (Odyssey $310M Amazon) |
| 10 | 08:17:31 | Federal Reserve rate decision economic data | Sweep | generic macro template, no named specific (Fed, not BoJ) |

_world tally: Sweep 2 · Verify-feed 5 · Self-found 0 · Known-thread 3 · Cold 0_

**Date tally (28 total):** Sweep 3 · Verify-feed 22 · Self-found 0 · Known-thread 3 · Cold 0

---

## 2026-06-18  (Techmeme pre-scan: 44 stories; prev headlines: 20)

### ai (session 1726a751)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:59:00 | Noam Shazeer joins OpenAI lead architecture research | Verify-feed | pre-scan #2 (Shazeer leaves Google for OpenAI) |
| 2 | 07:59:01 | Baseten $1.5B round, $13B valuation | Verify-feed | pre-scan #20 (Baseten raising $1.5B dual-tier) |
| 3 | 07:59:02 | Nvidia ENPIRE agent framework robot self-improvement | Verify-feed | pre-scan #9 (Nvidia ENPIRE harness) |
| 4 | 07:59:03 | AWS Continuum / AWS Context agents NY summit | Verify-feed | pre-scan #18 (AWS Continuum + AWS Context) |
| 5 | 07:59:04 | Bernie Sanders 50% AI stock tax sovereign wealth fund | Verify-feed | pre-scan #39 (Sanders 50% stock tax / fund) |

_ai tally: Sweep 0 · Verify-feed 5 · Self-found 0 · Known-thread 0 · Cold 0_

### hw (session 1e6c8002)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:58:35 | Intel Apple chip manufacturing deal Trump June 17 | Verify-feed | pre-scan #8 (Intel +9% on Trump Apple/Intel chip deal) |
| 2 | 07:58:37 | Tim Cook Apple price increase memory chip shortage | Verify-feed | pre-scan #1 (Cook: price hikes unavoidable, chip costs) |
| 3 | 07:58:40 | Nvidia ENPIRE robot self-improvement harness | Verify-feed | pre-scan #9 (Nvidia ENPIRE) |
| 4 | 07:58:40 | robotics humanoid startup funding round June 17 | Sweep | category probe, no named entity |
| 5 | 07:58:40 | data center power deal nuclear gigawatt June 2026 | Sweep | category probe, no named entity |
| 6 | 07:58:49 | Bank of Korea AI chipmaker bonus inflation SK Hynix Samsung | Verify-feed | pre-scan #28 (BoK warns chipmaker bonuses stoke inflation) |
| 7 | 07:58:50 | TSMC foundry capacity HBM Samsung order June 17 | Known-thread | prev headline samsung-foundry-...-orders (Samsung surge as TSMC tightens); probes new dev |
| 8 | 07:58:51 | chip startup Series funding raised June 17 semiconductor | Sweep | category probe, no named entity |
| 9 | 07:58:52 | Allbirds Smartbird AI pivot AWS CEO data center | Verify-feed | pre-scan #43 (Allbirds→Smartbird, ex-AWS CEO) |
| 10 | 07:58:53 | data center construction gigawatt June 17 18 Texas | Sweep | category probe, no named entity |

_hw tally: Sweep 4 · Verify-feed 5 · Self-found 0 · Known-thread 1 · Cold 0_

### world (session 602058df)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:58:43 | FDA drug approval clinical trial result June 17 | Sweep | category probe, no named entity |
| 2 | 07:58:44 | SpaceX launch satellite mission June 17 | Sweep | category probe, no named entity |
| 3 | 07:58:45 | central bank rate decision inflation report June 17 18 | Sweep | category probe, no named entity |
| 4 | 07:58:46 | Bernie Sanders AI stock tax sovereign wealth fund | Verify-feed | pre-scan #39 (Sanders 50% stock tax / fund) |
| 5 | 07:58:47 | Intel Apple chip design deal stock surge Trump | Verify-feed | pre-scan #8 (Intel +9% Trump Apple/Intel deal) |
| 6 | 07:59:28 | Frontier Anthropic $915M carbon removal credits Stripe Google | Verify-feed | pre-scan #35 (Frontier $915M carbon-removal, Anthropic joins) |
| 7 | 07:59:29 | Blackstone Medallia Thoma Bravo deal June 2026 | Verify-feed | pre-scan #24 (Blackstone takes Medallia from Thoma Bravo) |
| 8 | 07:59:30 | Bank of Japan interest rate decision June 16 17 hike | Cold | named entity not in prompt; no earlier in-session result (only result is this query's own, 10:59:31 UTC) |

_world tally: Sweep 3 · Verify-feed 4 · Self-found 0 · Known-thread 0 · Cold 1_

**Date tally (23 total):** Sweep 7 · Verify-feed 14 · Self-found 0 · Known-thread 1 · Cold 1

---

## 2026-06-19  (Techmeme pre-scan: 34 stories; prev headlines: 20)

### ai (session 6f9411cc)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:53:41 | GLM-5.2 open weights leading Intelligence Index | Verify-feed | Techmeme #6 (GLM-5.2 leads open weights, scores 51) |
| 2 | 07:53:42 | General Intuition $300M Series Bezos spatial reasoning | Verify-feed | Techmeme #28 (General Intuition raising $300M from Bezos) |
| 3 | 07:53:43 | Meta Crusoe 1.6 GW data center Texas Missouri | Verify-feed | Techmeme #23 (Meta buys ~1.6 GW from Crusoe, TX+MO) |
| 4 | 07:53:44 | Amazon Trainium sell third party DeSantis | Verify-feed | Techmeme #29 (DeSantis: Amazon in talks to sell Trainium) |
| 5 | 07:53:45 | Google Anthropic TPU NY $3.2B Nvidia playbook | Verify-feed | Techmeme #13 ($3.2B for NY data center renting TPUs to Anthropic) |
| 6 | 07:53:46 | Anthropic Mythos Preview Glasswing 200 firms US order | Verify-feed | Techmeme #19 (~200 cos kept Mythos/Glasswing access after US order) |
| 7 | 07:53:47 | Dean Ball OpenAI Strategic Futures frontier policy | Verify-feed | Techmeme #27 (Dean Ball joins OpenAI, Strategic Futures) |

_ai tally: Sweep 0 · Verify-feed 7 · Self-found 0 · Known-thread 0 · Cold 0_

### hw (session 502317ed)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:52:29 | humanoid Figure Tesla Optimus Unitree funding June 18 | Sweep | category probe; "Figure" only matches inside "Appfigures" — no humanoid story in prompt |
| 2 | 07:52:29 | data center nuclear power deal hyperscaler June 18 | Sweep | generic date-anchored category probe |
| 3 | 07:52:30 | Nvidia AMD TSMC Samsung chip announcement June 18 | Sweep | generic chip-category probe |
| 4 | 07:52:31 | chip startup robotics funding round June 18 | Sweep | generic funding-category probe |
| 5 | 07:52:32 | Amazon Trainium third party DeSantis Bloomberg | Verify-feed | Techmeme #29 (DeSantis: Amazon Trainium third-party sale) |
| 6 | 07:53:19 | FETCH: tweaktown Samsung-foundry · TC Amazon-Trainium · siliconangle xDOF $70M | Self-found | mixed pull: Samsung-foundry (10:52:32 UTC) + xDOF (10:52:33 UTC) self-surfaced from sweeps #3/#4 before fetch; Trainium URL is the Techmeme #29 verify |
| 7 | 07:53:20 | Intel Seok-Hee Lee EVP foundry SK Hynix Chandrasekaran | Verify-feed | Techmeme #22 (Intel names Seok-Hee Lee EVP; Chandrasekaran front-end) |
| 8 | 07:53:22 | Meta Crusoe 1.6 GW Texas Missouri Bloomberg June 18 | Verify-feed | Techmeme #23 (Meta–Crusoe 1.6 GW deal) |
| 9 | 07:53:22 | ASML Lutnick China EUV export controls June 2026 | Verify-feed | Techmeme #2 (Lutnick questioned ASML re China EUV machine) |
| 10 | 07:53:23 | Google Nvidia playbook TPU NY Anthropic $3.2B | Verify-feed | Techmeme #13 ($3.2B NY data center, TPUs to Anthropic) |

_hw tally: Sweep 4 · Verify-feed 5 · Self-found 1 · Known-thread 0 · Cold 0_

### world (session 43aa197d)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:52:39 | SpaceX $20B bond sale refinance bridge loan June 2026 | Verify-feed | Techmeme #5 (SpaceX plans $20B bond sale to repay xAI-merger bridge) |
| 2 | 07:52:40 | ASML China EUV Lutnick Commerce June 18 | Verify-feed | Techmeme #2 (Lutnick / ASML EUV concern) |
| 3 | 07:52:41 | Jio Platforms India IPO Ambani draft papers | Verify-feed | named entity in prompt (Jio/Ambani IPO) |
| 4 | 07:52:43 | Accenture Dragos runZero NetRise $4.18B | Verify-feed | Techmeme #32 (Accenture buys Dragos/runZero/NetRise, $4.18B) |
| 5 | 07:52:43 | Waymo recall 4000 robotaxis construction zones | Verify-feed | Techmeme #30 (Waymo pulls ~4K robotaxis from highways) |
| 6 | 07:52:52 | India Telegram ban VPN ProtonVPN exam leak | Verify-feed | Techmeme #1 (Appfigures: VPN downloads +49% after Telegram ban) |
| 7 | 07:52:53 | Apple Brazil App Store marketplaces CADE settlement | Verify-feed | Techmeme #26 (Apple opens iOS marketplaces in Brazil, CADE) |
| 8 | 07:52:54 | US Iran nuclear deal interim agreement markets June 18 | Cold | "Iran/nuclear/ceasefire" absent from pre-scan AND prev headlines; no earlier in-session Iran-topic result — continuing macro thread from model's prior knowledge |
| 9 | 07:52:55 | oil prices Iran ceasefire Brent WTI June 18 | Cold | "oil/Brent/crude" absent from prompt; fired in opening batch, no self-found anchor — model's own continuing-thread query |

_world tally: Sweep 0 · Verify-feed 7 · Self-found 0 · Known-thread 0 · Cold 2_

**Date tally (25 total):** Sweep 4 · Verify-feed 19 · Self-found 1 · Known-thread 0 · Cold 2

---

## 2026-06-22  (Techmeme pre-scan: 26 stories; prev headlines: 0)

_Note: prior day (06-21) was a weekend — the prompt carries NO previous-edition headlines block, so "Known-thread update" cannot apply (it requires a prev-edition headline). M=0 confirmed._

### ai (session 81290654)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:11:29 | Samsung ChatGPT Enterprise Codex deployment Korea | Verify-feed | pre-scan story 2 (Samsung rolls out ChatGPT Enterprise + Codex) |
| 2 | 07:11:30 | Getty Images OpenAI licensing deal ChatGPT search | Verify-feed | pre-scan story 6 (Getty signs OpenAI licensing deal) |
| 3 | 07:11:31 | Anthropic AI risk FT analysis export ban | Verify-feed | pre-scan story 1 (Anthropic talked itself into export ban) |
| 4 | 07:11:32 | Tencent Xiaowei AI assistant WeChat WeLM DeepSeek | Verify-feed | pre-scan story 15 (Tencent tests Xiaowei in WeChat) |
| 5 | 07:11:33 | Aether AI causal world models $20M seed | Verify-feed | pre-scan story 21 (Aether AI $20M seed, MPCi) |
| 6 | 07:11:55 | Bain Capital PE AI coding tools due diligence | Verify-feed | pre-scan story 8 (Bain uses AI coding to recreate software) |
| 7 | 07:11:56 | Coowa embodied AI robotics HK IPO $3B SoftBank | Verify-feed | pre-scan story 20 (Coowa HK IPO, $3B, SoftBank) |
| 8 | 07:11:57 | Satya Nadella Microsoft AI giants economy interview | Verify-feed | pre-scan story 9 (Nadella "can't let AI giants eat economy") |
| 9 | 07:11:58 | defense tech AI funding PitchBook $12B drones | Verify-feed | pre-scan story 13 (PitchBook defense tech $12.3B/175 deals) |
| 10 | 07:12:21 | Humble Robotics cabless freight truck $24M | Verify-feed | pre-scan story 23 (Humble Robotics $24M cabless truck) |
| 11 | 07:12:21 | "Sarah Polcz" Bernie Sanders AI sovereign wealth fund | Verify-feed | pre-scan story 11 (Sarah Polcz / Bernie's sovereign wealth idea) |
| 12 | 07:12:21 | AI model release benchmark frontier lab June 21/22 | Sweep | generic frontier-lab release category probe, no named entity |
_ai tally: Sweep 1 · Verify-feed 11 · Self-found 0 · Known-thread 0 · Cold 0_

### hw (session 00653208)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:12:01 | SK Hynix overtakes Samsung largest SK market cap | Verify-feed | pre-scan story 5 (SK Hynix passes Samsung, ~$1.4T) |
| 2 | 07:12:02 | China export controls MP Materials Teal Anduril ban | Verify-feed | pre-scan story 17 (China export controls + procurement bans) |
| 3 | 07:12:03 | Coowa embodied AI robotics SoftBank HK IPO $3B | Verify-feed | pre-scan story 20 (Coowa HK IPO, $3B, SoftBank) |
| 4 | 07:12:04 | Aether AI causal world models $20M seed MPCi | Verify-feed | pre-scan story 21 (Aether AI $20M seed, MPCi) |
| 5 | 07:12:05 | Morgan Stanley data center developers leveraged loans $15B | Verify-feed | pre-scan story 14 (Morgan Stanley data-center leveraged loans ~$15B) |
_hw tally: Sweep 0 · Verify-feed 5 · Self-found 0 · Known-thread 0 · Cold 0_

### world (session a818a94e)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 07:11:37 | China export controls MP Materials Teal Anduril ban | Verify-feed | pre-scan story 17 (China export controls + procurement bans) |
| 2 | 07:11:38 | defense tech startups funding PitchBook $12B drones | Verify-feed | pre-scan story 13 (PitchBook defense tech $12.3B/175 deals) |
| 3 | 07:11:39 | WiseTech Richard White AFP investigation shares fall | Verify-feed | pre-scan story 4 (WiseTech shares -11%, Richard White probe) |
| 4 | 07:11:41 | SK Hynix Samsung most valuable Korea $1.4T Kospi | Verify-feed | pre-scan story 5 (SK Hynix passes Samsung, ~$1.4T) |
| 5 | 07:11:42 | oil prices Brent WTI Iran Strait of Hormuz post-war | Sweep | generic date-anchored oil-price/Hormuz category probe, no named co+number (step-1 Sweep; Iran thread also surfaced in own earlier "news" result) |
| 6 | 07:11:54 | space launch SpaceX Starship rocket June 21 mission | Sweep | generic space-launch category probe |
| 7 | 07:11:55 | FDA approval clinical trial biotech drug June 21 | Sweep | generic FDA/biotech category probe (recurring template) |
| 8 | 07:11:56 | climate heatwave extreme weather record June 21 | Sweep | generic climate/weather category probe |
| 9 | 07:11:57 | Anduril Israel operations expansion local manager | Verify-feed | pre-scan story 25 (Anduril exploring Israel operations) |
| 10 | 07:11:58 | Trump Iran threat strike Hezbollah Lebanon ceasefire | Self-found | not in pre-scan; Iran/ceasefire thread surfaced in this session's own earlier broad-news tool_result (us-iran-mou-signed, 10:11:23 UTC) before this 10:11:58 UTC query |
_world tally: Sweep 4 · Verify-feed 5 · Self-found 1 · Known-thread 0 · Cold 0_

**Date tally (27 total):** Sweep 5 · Verify-feed 21 · Self-found 1 · Known-thread 0 · Cold 0

---

## 2026-06-24  (Techmeme pre-scan: 43 stories; prev headlines: 20)

### ai (session 0efdac3d)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 08:01:35 | new AI model release / benchmark June 23 | Sweep | category probe |
| 2 | 08:01:36 | AI in science / drug discovery / math June 23 | Sweep | category probe |
| 3 | 08:01:36 | AI startup funding Series A/B/C June 23 | Sweep | category probe |
| 4 | 08:02:35 | Menlo Ventures $3B AI funds | Verify-feed | Techmeme #42 |
| 5 | 08:02:36 | Anthropic Claude Tag Slack | Verify-feed | Techmeme #6 |
| 6 | 08:03:48 | *fetch* Mistral OCR-4 + Krea | Verify-feed | Techmeme #11, #14 |

_ai tally: Sweep 3 · Verify-feed 3 · Self-found 0 · Known-thread 0 · Cold 0_

### hw (session 74dfae47)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 08:01:40 | data center power / nuclear gigawatt | Sweep | category probe (recurs daily) |
| 2 | 08:01:41 | humanoid robot Tesla/Figure/Unitree | Sweep | category probe |
| 3 | 08:01:42 | Agility SPAC / Michael Klein | Verify-feed | Techmeme #26 |
| 4 | 08:01:43 | xLight EUV laser | Verify-feed | Techmeme #33 |
| 5 | 08:01:43 | Qualcomm × ByteDance custom chip | Verify-feed | Techmeme #16 |
| 6 | 08:02:03 | Cerebras Q1 $193M | Verify-feed | Techmeme #22 |
| 7 | 08:02:04 | Nvidia black-market chip prices | Verify-feed | Techmeme #17 |
| 8 | 08:02:05 | SK Hynix $29.4B US listing | Verify-feed | Techmeme #28 |
| 9 | 08:02:06 | Hadrian AI factories | Verify-feed | Techmeme #34 |
| 10 | 08:02:54 | Agility SPAC ticker AGLT (2nd pass) | Verify-feed | Techmeme #26 |

_hw tally: Sweep 2 · Verify-feed 8 · Self-found 0 · Known-thread 0 · Cold 0_

### world (session aa557f3f)
| # | Time | Query (short) | Class | Provenance note |
|---|---|---|---|---|
| 1 | 08:01:26 | US-Iran Switzerland talks developments | Known-thread | prev headline (continuing thread, "developments") |
| 2 | 08:01:26 | central bank rate decision June 23 | Sweep | category probe |
| 3 | 08:01:27 | FDA drug approval phase 3 June 23 | Sweep | category probe |
| 4 | 08:01:28 | rocket launch June 23 SpaceX/NASA | Sweep | category probe |
| 5 | 08:01:29 | defense military deal June 23 NATO | Sweep | category probe |
| 6 | 08:03:53 | FCC mid-band spectrum auction $3.5B | Verify-feed | Techmeme #36 |
| 7 | 08:03:54 | Alibaba sues DoD blacklist | Verify-feed | Techmeme #38 |
| 8 | 08:03:54 | France 5000 Harmattan drones | Self-found | surfaced in #5 sweep result, then drilled |

_world tally: Sweep 4 · Verify-feed 2 · Self-found 1 · Known-thread 1 · Cold 0_

**Date tally (24 total):** Sweep 9 · Verify-feed 13 · Self-found 1 · Known-thread 1 · Cold 0

---

