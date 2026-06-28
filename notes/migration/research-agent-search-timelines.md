# Research-agent search timelines

Per-edition timeline of every search/fetch call made by the research-phase agents, in
chronological order, with local timestamps (UTC-3, America/São_Paulo) and the tool used.

## How this was built
- Each `pipeline/research.sh` run spawns one headless `claude` subprocess per cluster
  (**ai**, **hw**, **world**) via `pipeline/tools/run-agent.sh` in a tmux pane. Each writes
  its own `research-<cluster>.json`.
- These subprocess sessions are **not** listed by `session list` (that only shows interactive
  sessions). They were located by their JSONL files in
  `~/.claude/projects/-Users-guilherme-ai-newsletter/`, matched to date+cluster via the
  `output/ai/<date>/research-<cluster>.json` path baked into each prompt, then disambiguated
  from interactive sessions that merely *reference* the path (the real agent is the one that
  actually issues the Exa searches).
- Tool calls extracted from each JSONL's `tool_use` entries; timestamps are the message-level
  `timestamp`, converted UTC→UTC-3.

## Key finding: it's Exa-only
Every research agent is launched with
`--allowedTools Read,Write,Bash,mcp__exa__web_search_exa,mcp__exa__web_fetch_exa`.
The native `WebSearch`/`WebFetch` tools are **not** in the allowlist, so the agents can't reach
them. Across all 21 agents / 7 editions there are **0** native web-search calls — **every one of
the 192 searches went through Exa** (`mcp__exa__web_search_exa`). The only non-search web calls
are 4 Exa fetches (`mcp__exa__web_fetch_exa`).

## Summary

| Date | ai (searches) | hw | world | Total searches | Fetches | Tool |
|---|---|---|---|---|---|---|
| 2026-06-15 | 9 | 17 | 12 | **38** | 0 | Exa |
| 2026-06-16 | 9 | 11 | 8 | **28** | 2 (hw) | Exa |
| 2026-06-17 | 8 | 10 | 10 | **28** | 0 | Exa |
| 2026-06-18 | 5 | 10 | 8 | **23** | 0 | Exa |
| 2026-06-19 | 7 | 9 | 9 | **25** | 1 (hw) | Exa |
| 2026-06-22 | 12 | 5 | 10 | **27** | 0 | Exa |
| 2026-06-24 | 5 | 10 | 8 | **23** | 1 (ai) | Exa |
| **All** | 55 | 72 | 65 | **192** | 4 | Exa |

Notable pattern: searches arrive in tight bursts (sub-second apart within a batch, then a ~10–60s
gap before the next batch) — the agents fire several `web_search_exa` calls in parallel, read the
results, then fire the next round.

---

## 2026-06-15

### Cluster: ai  (session c77c90b4)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:32:04 | Exa Search | Search | Anthropic Mythos Fable 5 export controls White House dispute June 14 2026 |
| 2 | 07:32:05 | Exa Search | Search | AI model release benchmark new June 14 15 2026 |
| 3 | 07:32:06 | Exa Search | Search | Enflame Tencent Shanghai IPO AI chip approval $888 million June 2026 |
| 4 | 07:32:07 | Exa Search | Search | ByteDance Iluvatar CoreX Baidu Kunlunxin AI chip purchase June 2026 |
| 5 | 07:32:08 | Exa Search | Search | Siri AI iOS 27 hands-on review third party AI models Apple intelligence June 2026 |
| 6 | 07:32:17 | Exa Search | Search | AI startup funding Series A B raise June 14 15 2026 |
| 7 | 07:32:18 | Exa Search | Search | Z.ai GLM-5.2 release 1M context coding model |
| 8 | 07:32:19 | Exa Search | Search | cybersecurity leaders letter Anthropic Fable 5 Mythos export ban June 15 2026 |
| 9 | 07:32:20 | Exa Search | Search | Orbio Series A 21 million Dawn Capital frontline workers AI agents |

_9 searches, 0 fetches._

### Cluster: hw  (session fa85a473)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:31:50 | Exa Search | Search | Nvidia AMD chip announcement deal June 14 2026 |
| 2 | 07:31:51 | Exa Search | Search | TSMC Samsung Intel foundry capacity June 14 2026 |
| 3 | 07:31:52 | Exa Search | Search | data center power deal nuclear gigawatt announcement June 14 2026 |
| 4 | 07:31:53 | Exa Search | Search | humanoid robot announcement Tesla Figure Unitree June 14 2026 |
| 5 | 07:31:53 | Exa Search | Search | chip startup funding round Series Nvidia robotics June 2026 |
| 6 | 07:32:10 | Exa Search | Search | Enflame Shanghai IPO approval AI chip June 15 2026 |
| 7 | 07:32:10 | Exa Search | Search | ByteDance Iluvatar CoreX AI chip Baidu Kunlunxin June 2026 |
| 8 | 07:32:28 | Exa Search | Search | AI data center announcement deal June 14 2026 hyperscaler |
| 9 | 07:32:29 | Exa Search | Search | robotics startup funding round Series announcement June 14 2026 |
| 10 | 07:32:30 | Exa Search | Search | Nvidia GTC Paris announcement June 14 2026 |
| 11 | 07:32:30 | Exa Search | Search | chip semiconductor deal Cambricon SMIC June 14 15 2026 |
| 12 | 07:32:47 | Exa Search | Search | "June 14, 2026" OR "June 15, 2026" data center power energy deal announcement |
| 13 | 07:32:48 | Exa Search | Search | "June 14" OR "June 15" 2026 humanoid robot deployment factory launch |
| 14 | 07:32:49 | Exa Search | Search | export controls semiconductor sanctions China June 14 2026 ASML |
| 15 | 07:33:19 | Exa Search | Search | Nvidia 800V power architecture data center June 2026 SemiAnalysis |
| 16 | 07:33:20 | Exa Search | Search | "June 15, 2026" chip semiconductor news announcement |
| 17 | 07:33:21 | Exa Search | Search | Google Visakhapatnam Raiden Infotech power license Andhra Pradesh data center |

_17 searches, 0 fetches._

### Cluster: world  (session ed154931)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:31:59 | Exa Search | Search | Iran nuclear deal ceasefire signing June 14 2026 Strait of Hormuz |
| 2 | 07:32:00 | Exa Search | Search | Ukraine Russia drone strikes overnight June 14 2026 air defense |
| 3 | 07:32:01 | Exa Search | Search | UK Starmer ban social media under 16s announcement June 14 2026 |
| 4 | 07:32:02 | Exa Search | Search | Trump France digital services tax champagne tariff 100% threat June 2026 |
| 5 | 07:32:02 | Exa Search | Search | Enflame Tencent Shanghai IPO approval AI chip June 15 2026 |
| 6 | 07:32:13 | Exa Search | Search | FDA drug approval clinical trial June 14 2026 biotech oncology |
| 7 | 07:32:14 | Exa Search | Search | G7 summit Evian June 15 2026 agenda Trump Macron leaders |
| 8 | 07:32:15 | Exa Search | Search | oil prices crude markets June 14 15 2026 brent WTI Hormuz reopens |
| 9 | 07:32:47 | Exa Search | Search | FDA approval zongertinib Hernexeos NSCLC accelerated date June 2026 |
| 10 | 07:32:48 | Exa Search | Search | major news June 14 2026 weekend headlines world economy |
| 11 | 07:33:17 | Exa Search | Search | Rio de Janeiro helicopter crash Oliver Tree singer June 14 2026 |
| 12 | 07:33:17 | Exa Search | Search | "June 14" OR "June 15" 2026 Britain UK detains Russia shadow fleet tanker |

_12 searches, 0 fetches._

---

## 2026-06-16

### Cluster: ai  (session f749c28a)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:36:31 | Exa Search | Search | DeepSeek $7.4 billion funding round $50 billion valuation Liang Wenfeng LP structure June 2026 |
| 2 | 07:36:32 | Exa Search | Search | OpenAI 2025 audited financials $34 billion spending R&D sales marketing June 2026 |
| 3 | 07:36:33 | Exa Search | Search | Qualcomm Tenstorrent acquisition talks $8 billion $10 billion June 2026 |
| 4 | 07:36:34 | Exa Search | Search | OpenRouter Fusion API multi-model parallel deep research launch announcement |
| 5 | 07:36:35 | Exa Search | Search | Anthropic Trump administration meeting June 15 2026 no resolution White House |
| 6 | 07:36:41 | Exa Search | Search | Meta AI Mode Facebook launch search public posts Groups Reels June 15 2026 |
| 7 | 07:36:43 | Exa Search | Search | France Mistral state chatbot 655 million euros AI investments Palantir Chapsvision DGSI June 2026 |
| 8 | 07:36:44 | Exa Search | Search | NewCore $66 million seed AI agent identity Cyberstarts launch June 2026 |
| 9 | 07:36:44 | Exa Search | Search | Salesforce Fin Intercom $3.6 billion acquisition AI customer service June 2026 |

_9 searches, 0 fetches._

### Cluster: hw  (session 6b9c56d5)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:36:20 | Exa Search | Search | Qualcomm Tenstorrent acquisition talks $8 billion to $10 billion AI chip designer June 2026 |
| 2 | 07:36:21 | Exa Search | Search | Nvidia $25 billion high-grade bond offering June 15 2026 demand investor |
| 3 | 07:36:22 | Exa Search | Search | humanoid robot company funding announcement June 15 2026 |
| 4 | 07:36:23 | Exa Search | Search | TSMC Samsung Intel foundry chip news June 16 2026 |
| 5 | 07:36:24 | Exa Search | Search | data center power deal nuclear gigawatt AI announcement June 15 16 2026 |
| 6 | 07:36:33 | Exa Search | Search | AMD acquires Mext memory technology company June 15 2026 |
| 7 | 07:36:34 | Exa Search | Search | Google Intel Tensor Processing Unit 3 million chips deal TPU 2028 announcement |
| 8 | 07:36:58 | Exa Search | Search | robotics humanoid funding round announcement June 15 16 2026 series |
| 9 | 07:36:59 | Exa Search | Search | chip startup funding Series A Series B AI semiconductor June 15 2026 |
| 10 | 07:36:59 | Exa Search | Search | Samsung Google Neuralink foundry AI chip Icefish I/O die memory |
| 11 | 07:37:18 | Exa Fetch | Fetch | https://www.wired.com/story/doj-lawyers-argue-xai-vital-national-security-naacp-lawsuit/ · https://9to5google.com/2026/06/15/google-announces-one-point-five-billion-dollar-data-center-expansion/ |
| 12 | 07:37:22 | Exa Search | Search | DOJ xAI gas turbines NAACP lawsuit national security dismiss filing date June 2026 |
| 13 | 07:37:22 | Exa Fetch | Fetch | https://9to5google.com/2026/06/15/google-announces-one-point-five-billion-dollar-data-center-expansion/ |

_11 searches, 2 fetches._

### Cluster: world  (session ade33025)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:36:04 | Exa Search | Search | Iran war aftermath ceasefire Strait Hormuz June 16 2026 |
| 2 | 07:36:05 | Exa Search | Search | Ukraine Russia war development June 16 2026 attack |
| 3 | 07:36:06 | Exa Search | Search | FDA drug approval June 15 2026 clinical trial biotech |
| 4 | 07:36:07 | Exa Search | Search | central bank rate decision June 16 2026 inflation |
| 5 | 07:36:08 | Exa Search | Search | SpaceX launch June 15 2026 mission satellite Starship |
| 6 | 07:36:16 | Exa Search | Search | G7 summit June 2026 Canada leaders meeting |
| 7 | 07:36:17 | Exa Search | Search | climate extreme weather event June 15 16 2026 wildfire flood |
| 8 | 07:36:17 | Exa Search | Search | US economic data retail sales industrial production June 16 2026 |

_8 searches, 0 fetches._

---

## 2026-06-17

### Cluster: ai  (session 2da6e0c4)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 08:17:20 | Exa Search | Search | SpaceX acquires Cursor $60 billion all-stock deal June 2026 |
| 2 | 08:17:22 | Exa Search | Search | Z.ai GLM-5.2 release flagship open weights MIT license 1M context June 16 2026 |
| 3 | 08:17:23 | Exa Search | Search | Odyssey world models $310 million Amazon AWS Trainium Series funding 2026 |
| 4 | 08:17:23 | Exa Search | Search | CuspAI $400 million Bezos materials science generative AI Cambridge UK round |
| 5 | 08:17:29 | Exa Search | Search | Sensor Tower ChatGPT market share below 50 Gemini Claude assistant report June 2026 |
| 6 | 08:17:30 | Exa Search | Search | Anthropic G7 UK carve-out Mythos 5 export ban Trump administration June 16 |
| 7 | 08:17:31 | Exa Search | Search | Junyang Lin new AI lab former Qwen Alibaba lead funding raise valuation Tencent |
| 8 | 08:17:32 | Exa Search | Search | Bland AI voice $50 million Series C Dell Technologies Capital June 2026 |

_8 searches, 0 fetches._

### Cluster: hw  (session 4f362da6)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 08:17:04 | Exa Search | Search | humanoid robot Figure Tesla Optimus Unitree announcement June 16 2026 |
| 2 | 08:17:04 | Exa Search | Search | Samsung chip foundry orders BYD Google AMD Nikkei June 2026 |
| 3 | 08:17:05 | Exa Search | Search | Kazakhstan Firebird Nvidia data center 10 billion deal June 2026 |
| 4 | 08:17:06 | Exa Search | Search | Snap Specs AR glasses launch price preorder $2195 June 16 2026 |
| 5 | 08:17:07 | Exa Search | Search | Qualcomm Snapdragon Reality Elite XR chipset Xreal Aura AWE 2026 |
| 6 | 08:17:15 | Exa Search | Search | Microsoft Surface Pro Laptop Snapdragon X2 launch price June 16 2026 |
| 7 | 08:17:16 | Exa Search | Search | Huawei chip logic stacking advance Financial Times June 2026 |
| 8 | 08:17:17 | Exa Search | Search | Odyssey world models $310M Amazon Trainium AWS funding round |
| 9 | 08:17:18 | Exa Search | Search | data center funding $58 billion 2026 YTD Dealogic Financial Times |
| 10 | 08:17:19 | Exa Search | Search | Apple AirPods camera 2027 iPhone foldable 20 Pro Gurman June 16 2026 |

_10 searches, 0 fetches._

### Cluster: world  (session a8253eca)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 08:17:12 | Exa Search | Search | Iran Israel war ceasefire diplomatic update June 16 2026 |
| 2 | 08:17:13 | Exa Search | Search | G7 summit Evian France outcomes statement Iran June 16 2026 |
| 3 | 08:17:14 | Exa Search | Search | Trump administration AI companies government equity stakes sovereign wealth fund Lutnick |
| 4 | 08:17:15 | Exa Search | Search | FDA drug approval biotech clinical trial June 16 2026 |
| 5 | 08:17:15 | Exa Search | Search | Binance EU MiCA license rejected Greece June 2026 |
| 6 | 08:17:27 | Exa Search | Search | Ukraine Russia war strike news June 16 2026 |
| 7 | 08:17:29 | Exa Search | Search | SpaceX stock surge market cap Amazon June 16 2026 IPO public |
| 8 | 08:17:29 | Exa Search | Search | oil price brent crude Strait of Hormuz reopen June 16 2026 |
| 9 | 08:17:30 | Exa Search | Search | Amazon Odyssey AI world models $310M Series funding round June 16 2026 |
| 10 | 08:17:31 | Exa Search | Search | Federal Reserve rate decision economic data June 16 2026 |

_10 searches, 0 fetches._

---

## 2026-06-18

### Cluster: ai  (session 1726a751)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:59:00 | Exa Search | Search | Noam Shazeer joins OpenAI lead architecture research June 2026 |
| 2 | 07:59:01 | Exa Search | Search | Baseten $1.5 billion funding round AI inference $13 billion valuation |
| 3 | 07:59:02 | Exa Search | Search | Nvidia ENPIRE agent framework robot self-improvement coding agents |
| 4 | 07:59:03 | Exa Search | Search | AWS Continuum AWS Context AI agents New York summit Amazon 2026 |
| 5 | 07:59:04 | Exa Search | Search | Bernie Sanders 50% AI stock tax sovereign wealth fund legislation 2026 |

_5 searches, 0 fetches._

### Cluster: hw  (session 1e6c8002)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:58:35 | Exa Search | Search | Intel Apple chip manufacturing deal Trump announcement June 17 2026 |
| 2 | 07:58:37 | Exa Search | Search | Tim Cook Apple price increase memory chip shortage AI June 18 2026 |
| 3 | 07:58:40 | Exa Search | Search | Nvidia ENPIRE robot self-improvement framework agent harness |
| 4 | 07:58:40 | Exa Search | Search | robotics humanoid startup funding round June 17 2026 |
| 5 | 07:58:40 | Exa Search | Search | data center power deal nuclear gigawatt announcement June 2026 |
| 6 | 07:58:49 | Exa Search | Search | Bank of Korea AI chipmaker bonus inflation warning June 2026 SK Hynix Samsung |
| 7 | 07:58:50 | Exa Search | Search | TSMC foundry capacity HBM Samsung order June 17 2026 |
| 8 | 07:58:51 | Exa Search | Search | chip startup Series funding raised June 17 2026 semiconductor |
| 9 | 07:58:52 | Exa Search | Search | Allbirds Smartbird AI pivot AWS CEO data center June 17 2026 |
| 10 | 07:58:53 | Exa Search | Search | data center construction announcement gigawatt June 17 18 2026 Texas |

_10 searches, 0 fetches._

### Cluster: world  (session 602058df)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:58:43 | Exa Search | Search | FDA drug approval clinical trial result June 17 2026 |
| 2 | 07:58:44 | Exa Search | Search | SpaceX launch satellite mission June 17 2026 |
| 3 | 07:58:45 | Exa Search | Search | central bank rate decision inflation report June 17 18 2026 |
| 4 | 07:58:46 | Exa Search | Search | Bernie Sanders AI stock tax sovereign wealth fund proposal |
| 5 | 07:58:47 | Exa Search | Search | Intel Apple chip design deal stock surge Trump announcement |
| 6 | 07:59:28 | Exa Search | Search | Frontier Anthropic $915 million carbon removal credits Stripe Google announcement |
| 7 | 07:59:29 | Exa Search | Search | Blackstone Medallia Thoma Bravo deal June 2026 |
| 8 | 07:59:30 | Exa Search | Search | Bank of Japan interest rate decision June 16 17 2026 hike |

_8 searches, 0 fetches._

---

## 2026-06-19

### Cluster: ai  (session 6f9411cc)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:53:41 | Exa Search | Search | GLM-5.2 open weights model Artificial Analysis Intelligence Index leading |
| 2 | 07:53:42 | Exa Search | Search | General Intuition $300M Series Bezos spatial reasoning AI agents valuation |
| 3 | 07:53:43 | Exa Search | Search | Meta Crusoe 1.6 GW data center Texas Missouri compute deal |
| 4 | 07:53:44 | Exa Search | Search | Amazon Trainium chip sell third party data centers Peter DeSantis |
| 5 | 07:53:45 | Exa Search | Search | Google Anthropic TPU New York data center $3.2 billion Nvidia playbook |
| 6 | 07:53:46 | Exa Search | Search | Anthropic Mythos Preview Project Glasswing 200 firms access preserved US order |
| 7 | 07:53:47 | Exa Search | Search | Dean Ball OpenAI Strategic Futures team frontier policy |

_7 searches, 0 fetches._

### Cluster: hw  (session 502317ed)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:52:29 | Exa Search | Search | humanoid robotics Figure Tesla Optimus Unitree funding announcement June 18 2026 |
| 2 | 07:52:29 | Exa Search | Search | data center nuclear power deal hyperscaler announcement June 18 2026 |
| 3 | 07:52:30 | Exa Search | Search | Nvidia AMD TSMC Samsung chip announcement June 18 2026 |
| 4 | 07:52:31 | Exa Search | Search | chip startup robotics funding round June 18 2026 announcement |
| 5 | 07:52:32 | Exa Search | Search | Amazon Trainium third party sale Peter DeSantis Bloomberg June 2026 |
| 6 | 07:53:19 | Exa Fetch | Fetch | https://www.tweaktown.com/news/112239/amd-google-tesla-and-groq-turn-to-samsung-foundry-as-tsmc-runs-out-of-capacity/index.html · https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/ · https://siliconangle.com/2026/06/17/robotic-teleoperation-data-startup-xdof-launches-70m-funding/ |
| 7 | 07:53:20 | Exa Search | Search | Intel Seok-Hee Lee EVP foundry SK Hynix CEO Naga Chandrasekaran announcement |
| 8 | 07:53:22 | Exa Search | Search | Meta Crusoe 1.6 GW Texas Missouri data center deal Bloomberg June 18 2026 |
| 9 | 07:53:22 | Exa Search | Search | ASML Lutnick China EUV machine Trump administration export controls June 2026 |
| 10 | 07:53:23 | Exa Search | Search | Google Nvidia playbook TPU data center New York Anthropic $3.2 billion |

_9 searches, 1 fetch._

### Cluster: world  (session 43aa197d)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:52:39 | Exa Search | Search | SpaceX $20 billion bond sale debt offering refinance bridge loan IPO June 2026 |
| 2 | 07:52:40 | Exa Search | Search | ASML China EUV machine export concern Lutnick US Commerce Secretary June 18 2026 |
| 3 | 07:52:41 | Exa Search | Search | Jio Platforms India IPO filing Ambani draft papers June 19 2026 |
| 4 | 07:52:43 | Exa Search | Search | Accenture acquires Dragos runZero NetRise cybersecurity deal $4.18 billion June 2026 |
| 5 | 07:52:43 | Exa Search | Search | Waymo recall 4000 robotaxis highway construction zones June 18 2026 |
| 6 | 07:52:52 | Exa Search | Search | India Telegram ban VPN surge ProtonVPN registrations exam paper leak June 17 2026 |
| 7 | 07:52:53 | Exa Search | Search | Apple Brazil App Store alternative marketplaces CADE settlement commission June 18 2026 |
| 8 | 07:52:54 | Exa Search | Search | US Iran nuclear deal interim agreement risk sentiment markets June 18 2026 |
| 9 | 07:52:55 | Exa Search | Search | oil prices Iran sanctions ceasefire markets June 18 2026 Brent WTI crude |

_9 searches, 0 fetches._

---

## 2026-06-22

### Cluster: ai  (session 81290654)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:11:29 | Exa Search | Search | Samsung ChatGPT Enterprise Codex OpenAI deployment Korea June 22 2026 |
| 2 | 07:11:30 | Exa Search | Search | Getty Images OpenAI licensing deal ChatGPT search announcement June 2026 |
| 3 | 07:11:31 | Exa Search | Search | Anthropic AI risk language Financial Times analysis export ban 2026 |
| 4 | 07:11:32 | Exa Search | Search | Tencent Xiaowei AI assistant WeChat WeLM DeepSeek launch June 2026 |
| 5 | 07:11:33 | Exa Search | Search | Aether AI causal world models seed funding $20M physical AI startup robotics |
| 6 | 07:11:55 | Exa Search | Search | Bain Capital private equity AI coding tools recreate software due diligence June 2026 |
| 7 | 07:11:56 | Exa Search | Search | Coowa embodied AI robotics Hong Kong IPO $3B valuation SoftBank June 2026 |
| 8 | 07:11:57 | Exa Search | Search | Satya Nadella Microsoft AI giants economy interview low-cost models June 21 2026 |
| 9 | 07:11:58 | Exa Search | Search | defense tech AI startup funding PitchBook 2026 $12 billion battlefield drones |
| 10 | 07:12:21 | Exa Search | Search | Humble Robotics autonomous freight truck cabless $24M Series A California June 2026 |
| 11 | 07:12:21 | Exa Search | Search | "Sarah Polcz" Bernie Sanders AI sovereign wealth fund proposal The Information June 2026 |
| 12 | 07:12:21 | Exa Search | Search | AI model release benchmark frontier lab announcement June 21 22 2026 |

_12 searches, 0 fetches._

### Cluster: hw  (session 00653208)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:12:01 | Exa Search | Search | SK Hynix overtakes Samsung Electronics largest South Korea market cap June 22 2026 |
| 2 | 07:12:02 | Exa Search | Search | China export controls MP Materials Teal Drones Anduril procurement ban June 2026 |
| 3 | 07:12:03 | Exa Search | Search | Coowa embodied AI robotics SoftBank Hong Kong IPO $3 billion valuation |
| 4 | 07:12:04 | Exa Search | Search | Aether AI causal world models physical AI $20 million seed MPCi June 2026 |
| 5 | 07:12:05 | Exa Search | Search | Morgan Stanley data center developers leveraged loans $15 billion 2026 |

_5 searches, 0 fetches._

### Cluster: world  (session a818a94e)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 07:11:37 | Exa Search | Search | China export controls US companies MP Materials Teal Drones Anduril sanctions procurement ban June 21 2026 |
| 2 | 07:11:38 | Exa Search | Search | defense tech startups funding 2026 PitchBook 12 billion drones battlefield AI venture capital |
| 3 | 07:11:39 | Exa Search | Search | WiseTech Richard White Australian federal police investigation sex trafficking shares fall June 22 2026 |
| 4 | 07:11:41 | Exa Search | Search | SK Hynix Samsung most valuable company Korea June 22 2026 1.4 trillion Kospi memory |
| 5 | 07:11:42 | Exa Search | Search | oil prices Brent WTI June 21 2026 Iran Strait of Hormuz post-war markets |
| 6 | 07:11:54 | Exa Search | Search | space launch satellite SpaceX Starship rocket June 21 2026 mission |
| 7 | 07:11:55 | Exa Search | Search | FDA approval clinical trial biotech drug June 21 2026 announcement |
| 8 | 07:11:56 | Exa Search | Search | climate heatwave extreme weather record June 21 2026 |
| 9 | 07:11:57 | Exa Search | Search | Anduril Israel operations expansion local manager June 2026 |
| 10 | 07:11:58 | Exa Search | Search | Trump Iran threat strike Hezbollah Lebanon ceasefire June 21 2026 |

_10 searches, 0 fetches._

---

## 2026-06-24

### Cluster: ai  (session 0efdac3d)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 08:01:35 | Exa Search | Search | new AI model release or benchmark results announced June 23 2026 frontier lab OpenAI Anthropic Google DeepMind |
| 2 | 08:01:36 | Exa Search | Search | AI in science drug discovery protein folding math proof breakthrough announced June 23 2026 |
| 3 | 08:01:36 | Exa Search | Search | AI startup funding round Series A B C raised June 23 2026 agent infrastructure |
| 4 | 08:02:35 | Exa Search | Search | Menlo Ventures raises $3 billion AI funds largest ever Anthropic stake June 2026 |
| 5 | 08:02:36 | Exa Search | Search | Anthropic Claude Tag agentic AI coworker Slack launch beta Team Enterprise June 23 2026 |
| 6 | 08:03:48 | Exa Fetch | Fetch | https://mistral.ai/news/ocr-4/ · https://venturebeat.com/technology/enterprise-grade-ai-image-generation-in-2-seconds-is-here-krea-2-raw-and-turbo-available-as-open-weights-under-custom-license |

_5 searches, 1 fetch._

### Cluster: hw  (session 74dfae47)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 08:01:40 | Exa Search | Search | data center power deal nuclear gigawatt announced AI compute |
| 2 | 08:01:41 | Exa Search | Search | humanoid robot Tesla Optimus Figure Unitree announcement new model |
| 3 | 08:01:42 | Exa Search | Search | Agility Robotics SPAC merger $2.5 billion Michael Klein Digit humanoid public |
| 4 | 08:01:43 | Exa Search | Search | xLight EUV laser startup raising $350 million Bain Capital Boardman Bay |
| 5 | 08:01:43 | Exa Search | Search | Qualcomm ByteDance custom chip design services Alphawave talks |
| 6 | 08:02:03 | Exa Search | Search | Cerebras first quarterly earnings revenue $193 million net loss gross margin guidance |
| 7 | 08:02:04 | Exa Search | Search | Nvidia AI chip black market prices doubled China smuggling DGX B300 export crackdown |
| 8 | 08:02:05 | Exa Search | Search | SK Hynix US Nasdaq listing raise $29.4 billion ADR new shares July 10 |
| 9 | 08:02:06 | Exa Search | Search | Hadrian AI factories space defense parts funding $1 billion $7.5 billion valuation |
| 10 | 08:02:54 | Exa Search | Search | Agility Robotics SPAC Michael Klein ticker AGLT public listing Digit Amazon |

_10 searches, 0 fetches._

### Cluster: world  (session aa557f3f)
| # | Time (UTC-3) | Tool | Type | Query / URL |
|---|---|---|---|---|
| 1 | 08:01:26 | Exa Search | Search | US Iran nuclear deal Switzerland talks developments June 23 2026 geopolitics Middle East |
| 2 | 08:01:26 | Exa Search | Search | central bank interest rate decision June 23 2026 economy inflation oil prices |
| 3 | 08:01:27 | Exa Search | Search | FDA drug approval clinical trial results June 23 2026 biotech phase 3 |
| 4 | 08:01:28 | Exa Search | Search | rocket launch space mission June 23 2026 SpaceX NASA satellite |
| 5 | 08:01:29 | Exa Search | Search | defense military deal weapons contract June 23 2026 NATO procurement |
| 6 | 08:03:53 | Exa Search | Search | FCC mid-band spectrum auction raises $3.5 billion replace Chinese telecom equipment rip and replace June 2026 |
| 7 | 08:03:54 | Exa Search | Search | Alibaba sues US Defense Department Pentagon blacklist Chinese military companies lawsuit June 2026 |
| 8 | 08:03:54 | Exa Search | Search | France orders 5000 Harmattan AI military drones armed forces ministry June 2026 |

_8 searches, 0 fetches._
