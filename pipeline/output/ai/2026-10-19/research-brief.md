# Research — News Cluster

Search for news **events that occurred** between **2026-10-15 10:00 BRT** and **2026-10-19 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

Your output will be merged with other clusters into the final research file.

## Cluster boundaries (de-confliction)

You are **one of three** parallel clusters — **ai**, **hw**, **world** — merged
into one file afterward. So two clusters don't spend a slot on the same story,
each contested story type has a single owner. Research your own beat; when a
story sits on a boundary, defer to the owner below and **do not spend a slot on a
story a sibling owns** — even a strong one.

| Contested story type | Owner |
|---|---|
| Models & AI-app/software capabilities; AI-lab / AI-software funding rounds | **ai** |
| Silicon, chips, accelerators — **even when announced by an AI lab** (e.g. an inference chip) | **hw** |
| Robots / humanoid hardware | **hw** |
| Hardware-company financing — IPOs, ADR listings, SPACs, raises, M&A (chipmakers, robotics, data-center/compute infra, energy-for-compute) | **hw** |
| Semiconductor export controls (ASML/EUV, sanctions) | **hw** |
| Geopolitics, military/defense, macro & central banks, markets, biotech/pharma, health policy, space, climate/energy | **world** |
| Non-tech funding / IPOs / M&A / SPACs (any company that isn't an AI or hardware company) | **world** |

Apply the column for **your** cluster (named in your system prompt). The other
columns are off-limits — a sibling has them covered.

## Rules

- Up to 7 stories. Fewer is fine if the news day is thin for your cluster.
- Every URL must come from a search result or fetched page. Never invent URLs.
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-15 10:00 BRT to 2026-10-19 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
- **Sourcing — a rehash has no primary source.** Anchor each story on a **primary source** (company/government release, filing, the principal's own post) or a **tier-1 outlet**. If the only coverage is thin aggregators or SEO trade blogs with no primary or tier-1 confirmation, treat that as a red flag the item is a rehash of old news, not a fresh event — find a primary/tier-1 source or skip it. Never let a lone aggregator write-up be the sole basis for a story.
- Every fact in `key_facts` must come from a **listed source** — one that appears in the story's `sources` array. No background knowledge, no facts from pages you visited but didn't cite. If you found a fact via a tweet, search snippet, or secondary article, add that URL to `sources`.
- `headline` and `key_facts` in English.
- The previous edition's headlines are listed at the end of this prompt. Skip stories already covered unless there's a genuinely new development.

## Tools

| Tool | Use for |
|---|---|
| `exa_search` | Best for dated news. Use single-topic queries — multi-topic loses focus. Set `startPublishedDate`/`endPublishedDate` for date scoping. Pass `contents: {text: true}` to get full article text inline — avoids a separate fetch. |
| `exa_get_contents` | Fetch full text from URLs you already have (e.g. from tweets, press releases, or a source you want to read in full). Pass an array of URLs. |
| `bash` with `bird search "query"` | X/Twitter. Use specific terms or `from:` queries — broad queries return noise. |
| `bash` with `bird read <url>` | Fetch full tweet text. |

**Do NOT fetch these domains** (blocked/paywalled — use `exa_search` snippets instead):
reuters.com, bloomberg.com, axios.com, cnbc.com, politico.eu, seekingalpha.com, businessinsider.com, wired.com, business-standard.com, datacenterdynamics.com, etnownews.com, archynewsy.com, wccftech.com, openai.com, cybernews.com, coindesk.com, appleinsider.com, aninews.in


## Workflow

1. Check the previous edition headlines at the end of this prompt.
2. **Landscape scan**: Review the Techmeme scan, then run 5 searches to fill gaps. Stop searching.
3. **Pick your 7 stories.** From what you found, choose 7. This is your final list — do not add stories after this point.
4. **Fetch only where needed**: For stories where search snippets lack exact numbers or quotes, fetch the source. Most stories won't need this.
5. Write the JSON output file.

## Output

Write to the file path given below. Format:

```json
{
  "stories": [
    {
      "id": "kebab-case-slug",
      "headline": "Factual headline under 100 chars",
      "key_facts": [
        {
          "fact": "Specific claim with numbers/names/dates",
          "source_url": "https://...",
          "excerpt": "Supporting detail from the source (search snippets are fine)"
        }
      ],
      "sources": [
        {
          "url": "https://...",
          "outlet": "Reuters",
          "title": "Article headline",
          "published_at": "YYYY-MM-DD",
          "image_url": "",
          "type": "news_article"
        }
      ],
      "category": ["technology"],
      "entities": {
        "organizations": [],
        "people": [],
        "places": []
      }
    }
  ]
}
```

**Story fields**: `id` (unique kebab slug), `headline` (<100 chars), `key_facts` (3-8 sourced facts, each with `source_url` pointing to a listed source and `excerpt` with the supporting text), `sources`, `category` (1-3 from: technology, science, world, economy, finance, business, politics, brazil, sports, entertainment), `entities` ({organizations, people, places} — named entities from sources only).

**Source fields**: `url`, `outlet`, `title` (tweets: "Tweet by @handle: [first 80 chars]"), `published_at` (YYYY-MM-DD, fallback today), `image_url` ("" if unavailable), `type` (news_article|tweet|blog_post|paper|press_release|video|government_filing).

---

**Date:** 2026-10-19
**Research window:** 2026-10-15 10:00 BRT → 2026-10-19 10:00 BRT

**Previous edition headlines (2026-10-15 — skip unless genuinely new development):**
- anthropic-q3-revenue-16-8b-profitable-pre-ipo: Anthropic tells investors Q3 revenue hit $16.8B and it was profitable ahead of IPO
- eight-states-sue-openai-ftc-subpoenas-openai-anthropic: Eight US states sue OpenAI over ChatGPT harms as FTC subpoenas OpenAI and Anthropic
- metr-loss-of-control-assessment-proposal: METR proposes independent assessments of whether AI labs could lose control of internal agents
- spacexsi-grok-voice-3: SpaceXSI launches Grok Voice 3.0, topping Artificial Analysis speech-to-speech index
- gemini-4-argon-science-results-epoch-eci: DeepMind touts Gemini 4 Argon science results; Epoch ranks it just behind Opus 5.5 and GPT-6 Astra
- bofa-1000-contractors-mythos-flaws: Bank of America hired 1,000 contractors to patch flaws exposed by AI models like Mythos
- apple-intelligence-china-december-ios-27-3: Apple plans to launch Apple Intelligence in China in December, without Siri AI
- tsmc-q3-2026-record-profit-44pct-growth-new-3nm-fab: TSMC posts sixth straight record profit, lifts 2026 growth to ~44% and adds a 3nm fab in Tainan
- tsmc-terafab-talks-texas-must-run-fab: TSMC confirms Terafab talks and Texas scouting, but says any fab 'has got to be run by TSMC'
- bytedance-mediatek-data-center-asic-talks: ByteDance nears deal to buy custom data-center AI chips from MediaTek
- sk-hynix-solidigm-us-fab-tied-to-dalian-export-license: SK Hynix ties new US NAND factory to US approval for more chip-tool exports to its China fab
- idc-smartphone-shipments-record-22pct-drop-memory-crisis: Global smartphone shipments fall a record 22% in Q3 as AI-driven memory crunch bites, IDC says
- senators-question-meta-rd-tax-credits-ai-data-centers: Democratic senators press Meta over billions in R&D tax credits claimed on AI data centers
- mueon-65m-series-a-cubelets-3d-compute: Mueon raises $65M Series A led by Maverick Silicon for 3D compute-memory 'Cubelets'
- hormuz-two-container-ships-sink-iran-attacks: Two cargo ships sink in Strait of Hormuz as Iran escalates attacks on shipping
- musk-starshield-limits-us-military-zelenskyy-betrayed: Musk says US military decides Starshield limits as Zelenskyy says he feels betrayed by Trump
- kospi-crash-ai-rout-ppi-6-3-percent: Kospi crashes 7.6% with circuit breaker as AI rout spreads; US wholesale inflation hits 6.3%
- citizen-lab-adfection-discover-tech-spyware-ads: Citizen Lab: Israeli ad firm Discover-Tech delivered zero-click spyware through targeted ads
- anduril-tender-offer-90b-valuation: Defense startup Anduril opens $1.3B employee tender at about $90B valuation
- fda-anktiva-papillary-bladder-cancer-approval: FDA expands ImmunityBio's Anktiva to papillary-only bladder cancer via new evidence approach
- jio-platforms-ipo-3-2b-108b-valuation: Jio Platforms sets $3.2B IPO, India's largest, at up to $108B valuation

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 36 stories

1. Elon Musk says “I will give one of my SpaceX shares to every kid in America” in 2027, a gift worth ~$10.5B, after Anthropic committed 5% of its shares to APBF
   Kai Nicol-Schwarz / CNBC — https://www.cnbc.com/2026/10/19/elon-musk-spacex-shares-giveaway-kids.html
   Choose CNBC as your preferred source on Google and never miss a moment from the most trusted name in business news.
   > @elonmusk: Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many.
   > @shakeelhashim: They are, though it is very sad that the money just goes to Americans — what about the rest of the world?
   > @johnarnold: 530A accounts ("Trump Accounts") are a great solution for many ultra-wealthy Americans who are philanthropically inclined, do not want a foundation staff, do want to give while living, and haven't bee
   > @kimmonismus: Giving one SpaceX share to every child in the US would mean donating roughly 72 million shares, about 1.12% of Musk's reported holdings. At $146.03 per share, that would be worth approximately $10.5 b
   > @rmac18: Also worth noting that Musk has a history of making philanthropic pledges and not following through. In 2018, he pledged to “fund fixing the water in any house in Flint that has water contamination ab
   Also: RTÉ, TechCrunch, Associated Press, Wall Street Journal, WPXI-TV, Variety, RedState, Dexerto, +26 more

2. Anthropic commits 5% of its shares to the Anthropic Public Benefit Fund, for a total of ~20% with co-founder and staff pledges, plus 2% per 50% valuation rise
   Anthropic — https://www.anthropic.com/news/public-benefit-fund
   Today, we're committing a portion of Anthropic's shares to the Anthropic Public Benefit Fund, a new entity with a structure that increases the stake as the company grows.
   > @elonmusk: @AnthropicAI I recommend giving the shares directly to the public
   > @iterintellectus: the beginning of universal basic income
   > @elonmusk: @AnthropicAI This is what I will be doing
   > @edzitron: ? What the fuck does that mean? Is this legally binding or just some sort of key jingling for headlines
   > @edzitron: How many stories are we going to get from these ai companies that do not answer fundamentally important questions like “how?” Or “what does that mean?” Unbelievable
   Also: BBC, Associated Press, Wall Street Journal, PCMag, Semafor, Bloomberg, The Guardian, TechCrunch, +28 more

3. A look at Anthropic's opaque, five-member Long-Term Benefit Trust, where members own no Anthropic equity but hold enormous sway by appointing most of its board
   Theo Francis / Wall Street Journal — https://www.wsj.com/tech/ai/anthropic-ipo-private-trust-188f41f7?st=RtdGHg&reflink=desktopwebshare_permalink
   AI company has shared few details on the dynamics of the five-person trust empowered to shape its board and block major moves
   Also: 24/7 Wall St.

4. Researcher: a Chinese-speaking hacker used AI agents to target 1,200+ websites and breach 100+ entities, like Deere and SharkNinja, spending ~$5,000 in tokens
   Raphael Satter / Reuters — https://www.reuters.com/legal/government/how-one-hacker-used-ai-agents-few-thousand-dollars-break-into-scores-sites-2026-10-19/
   Over the past couple of weeks, a cybersecurity researcher watched as a Chinese-speaking hacker broke into websites belonging …
   > @hesamation: and yes, there's literally an open source agent framework for hacking now called Cairn. the defense needs to pick up the pace full report: https://norforge.com/...
   > @hesamation: Chinese hackers used DeepSeek + Claude Code to breach 100+ companies. but forgot to put passwords on their own agent dashboards. so researchers found 20 exposed dashboards and could literally watch th
   > @uk_daniel_card: I guess people haven't heard about tools before 🤣
   > @mooncat_is: Just a few days ago I saw a post saying “if deepseek is as good as the original mythos, why haven't we seen large scale AI cyber crime yet???”
   > @rgb_lights: Transition from vulpocalypse to breachpocalypse is here. IR firms are saturated & turning away work. Now one hacker unleashed AI agents on 1,200+ websites, compromising 100+ for ~$5,000 in tokens. $50
   Also: NorForge, MadRobot, The Verge, Metacurity, Unite.AI

5. Google DeepMind says four Gemini 4 Argon agents beat Minecraft without any human help in 27 hours and 14 minutes, costing $1,620 at Argon's planned 2027 price
   Matthias Bastian / The Decoder — https://the-decoder.com/four-gemini-4-argon-agents-beat-minecraft-without-any-human-help/
   The Google Deepmind team dropped the agents into a randomly generated world without assigning roles, strategies, or game-specific tools.
   > @maxencefaldor: A team of Gemini 4 Argon agents beats Minecraft
   > @googledeepmind: Four Gemini 4 Argon agents beat Minecraft from scratch in 27 hours. Operating in a sandbox using only code and text, they wrote 2,783 programs, divided up jobs over chat, shared notes, and debugged er
   > @robertarail: Four Gemini 4 Argon agents teamed up in Minecraft to defeat the Ender Dragon in 27 hours, writing every move as code and coordinating in the game's chat. Great work led by @maxencefaldor with Satinder
   > @adonis_singh: I take everything bad I said about Argon, this is really cool
   > @emollick: The paper on how a team of Gemini 4 agents beat Minecraft is worth a look. It is accessible example (partially because it is AI written) of spontaneous coordination among agents to accomplish a compli
   Also: Google DeepMind, Engadget, IGN

6. Sam Altman's World debuts a World ID verification suite for banks, bundling tools for verifying human and agent identities, its first industry-specific offering
   Zack Abrams / The Block — https://www.theblock.co/news/ecosystems/2026-10-18-world-launches-world-id-suite-banks-418869
   The identity project co-founded by OpenAI CEO Sam Altman named Bain Capital and VanEck Funds among its design partners …
   > @worldnetwork: In 2024, an employee at engineering firm Arup transferred $25.6 million after joining a video call where every other participant was a deepfake. Since then, AI has advanced significantly and is making
   > @bitpaine: crazy how elliptic curve cryptography is about to suffer an imminent collapse from ai and ai-accelerated quantum but the guy best positioned to know whether this is a major concern (Sam Altman) is bac
   > @nazo_ku: Can World beat the fake AI agents scaling globally to snatch everything of value and even leak national secrets? [embedded post]
   > @world_id: World ID is having a moment
   Also: Decrypt, Fortune, crypto.news, CryptoPotato, Biometric Update, CoinGape, The Indian Express, PYMNTS.com, +2 more

7. AI chip startup Tenstorrent raised a $1.5B Series E led by Trace Capital and Innovation X at a $6.2B valuation, up from $2.6B after raising $700M in 2024
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-19/ai-chip-startup-tenstorrent-raises-funds-at-6-2-billion-value
   AI chip startup Tenstorrent Inc., after attracting takeover interest earlier this year, has raised $1.5 billion from investors …
   Also: Tenstorrent, BetaKit, AI Insider, Reuters, DatacenterDynamics, SiliconANGLE, Capital Brief, Quartz

8. CyberSN: US cybersecurity job postings fell 26.4% YoY to a four-year low of 235,786 roles from January to September; AI security engineer demand soared 268.3%
   Kevin Townsend / SecurityWeek — https://www.securityweek.com/us-cybersecurity-job-postings-fall-26-as-ai-security-engineer-demand-soars/
   CyberSN's Cybersecurity Jobs Report provides visibility into the US cybersecurity job market. It's a mixed bag.
   Also: CyberSN, RuntimeWire, Help Net Security

9. Sources: Nscale faces investor pushback over its ~$30B IPO valuation, with some urging a lower $16B-to-$19B valuation, as Microsoft exits a UK data center deal
   Bailey Lipschultz / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-18/ai-cloud-firm-nscale-faces-investor-pushback-over-ipo-valuation
   Nscale Ltd. is facing opposition to the valuation target it's pursuing in its initial public offering, according to people familiar …
   > @edzitron: Dead as disco
   Also: The Decoder, DatacenterDynamics, Quartz, Yahoo Finance, The Information, Implicator.ai, PYMNTS.com, Crypto Briefing

10. Sources: two industry execs expect 7-10 of hundreds of neoclouds to survive, as Nvidia supports them with easier credit terms, site finding, and $20B in leases
   Phoebe Liu / The Information — https://www.theinformation.com/articles/neocloud-shakeout-looms-nvidia-lot-lose
   > @highyieldharry: Easiest analogy for the Neoclouds are that they're the WeWork of the AI cycle.
   Also: Reuters, 24/7 Wall St., CNBC, The Crypto Basic, Quartz, Sydney Morning Herald, Motley Fool

11. Analysis: companies are set for a massive acceleration of 50GW+ in data center capacity additions in 2027; 24GW+ across 40 campuses are in the advanced stages
   Jeremie Eliahou Ontiveros / SemiAnalysis — https://newsletter.semianalysis.com/p/datacenters-2027-the-year-of-acceleration
   60GW Under Construction, SemiAnalysis Leading Indicators, 1.3T of Lease Contracts Signed YTD, The Shortage Could Move to Chips
   > @jordannanos: Our forecasts are too aggressive according to @altcap Don't believe your lyin' eyes
   > @semianalysis_: Datacenters 2027: The Year of Acceleration, +50GW in a Single Year 60GW Under Construction, SemiAnalysis Leading Indicators, 1.3T of Lease Contracts Signed YTD, The Shortage Could Move to Chips https:
   > @mayabarkin: @altcap and others called our +43GW of global datacenter capacity (ex China) for 2027 too aggressive, so we went back through every site we track. We came out higher, at +50GW. The satellite images sp
   Also: CNBC, Klement on Investing

12. Analysis: 11K+ accounts on X, Bluesky, Discord, Telegram, and others made nearly 25K posts to unmask a Cornell sexual assault accuser, after she named seven men
   New York Times — https://www.nytimes.com/2026/10/16/nyregion/cornell-jane-doe-internet-doxing.html?unlocked_article_code=1.JVE.fW7d.sMnfJ3J11YO7&smid=url-share
   After a former student named seven men in a lawsuit saying they had sexually assaulted her, a movement gained steam online to reveal her identity.
   > @rmac18: Over the last few weeks there's been a lot of whether this platform is back. In that time, this platform has also become the central place where people have congregated to dox a woman who accused seve
   Also: ZeroHedge News, Financial Times

13. Tel Aviv-based doubleAI releases a code execution model for improving GPU and CPU performance; doubleAI raised $220M, using ~50% to buy 1,000 Nvidia B300 chips
   Belle Lin / Wall Street Journal — https://www.wsj.com/cio-journal/nvidia-backed-startup-doubleai-launches-model-to-pare-cost-of-compute-b780f215?st=Xj19EK&reflink=desktopwebshare_permalink
   DoubleAI, a startup based in Tel Aviv, is set to debut what it calls a new category of artificial intelligence that can help companies lower their computing costs.
   Also: Quartz, CTech

14. Deutsche Telekom, Orange, Telefónica, and Vodafone agree to explore a joint bid to offer “direct-to-device” satellite service in Europe, challenging Starlink
   Financial Times — https://www.ft.com/content/555bbf91-4c38-43ce-94b6-90f7fc04e82c
   Deutsche Telekom, Orange, Telefónica and Vodafone to explore joint bid for spectrum to provide mobile satellite coverage
   Also: Quartz, RCR Wireless, Advanced Television, Telecompaper

15. Microsoft unveils new security tools in its 365 E7 bundle and Project Perception system to treat AI agents as potential insider threats via risk assessments
   Todd Bishop / GeekWire — https://www.geekwire.com/2026/microsoft-unveils-tools-to-monitor-and-corral-rogue-ai-agents/
   Microsoft is coming out with new security tools that treat AI agents as potential insider threats, continuously assessing their risk …
   > @skupor: Another good example (following on the heels of the @nvidia release a few weeks back) of the industry using software to address potential security concerns around SI. This is the familiar pattern we'v
   > @satyanadella: I recently wrote about why we need to treat models as insider risks, with security controls sitting outside the model itself. Today, we're putting that principle into practice by expanding Project Per
   Also: Microsoft, Sky News, Microsoft Security Blog, Microsoft Security on YouTube, Unite.AI, Sky News on YouTube, The Chosun Daily

16. Character.AI's Chapter 11 court filings indicate a two-part deal with Disney to transfer talent and tech while insulating Disney from mounting legal liabilities
   Maddy Varner / Wired — https://www.wired.com/story/disney-asked-characterai-to-go-bankrupt-for-a-get-out-of-lawsuits-card/
   The entertainment giant hopes to get trust and safety tech, among other IP, from a startup whose chatbots dozens …
   > @douglaslfarrar: In their bankruptcy filings Character AI disclosed that the FTC opened an investigation into them under Chair Khan, only for it to be closed by the Trump-Vance FTC. No justice for the parents of child
   Also: Tech Times, Quartz, Business Today

17. How Democrats, who polls predict will flip at least one chamber of Congress in the midterm elections, are preparing to aggressively scrutinize the AI industry
   Lauren Feiner / The Verge — https://www.theverge.com/policy/1013113/democrats-ai-midterms
   At a moment when voters are fearful of AI, Democrats are finding their footing. … Democrats could win back control of Congress this November …

18. Sources: HomeView units sat in warehouses for months; Apple plans a November 6 store reset, likely for new Macs; iPhone Duo preorder mess could boost the 18 Pro
   Mark Gurman / Bloomberg — https://www.bloomberg.com/news/newsletters/2026-10-18/apple-homeview-with-robotic-arm-new-mac-ipad-mini-nov-6-release-iphone-duo?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MjMzMjI1NywiZXhwIjoxNzkyOTM3MDU3LCJhcnRpY2xlSWQiOiJUTjNXODFLR1pBSjQwMCIsImJjb25uZWN0SWQiOiJDNEVEQ0FFMUZBMDU0MEJFQTI0QTlGMjExQzFFOTA4MCJ9.SXy771LY1gAlXt2MmZODtLQ3lEquvyiefNIH-i7IZHQ
   Also: The company is planning Nov. 6 retail store reset, indicating potential Mac release date.
   > @raywongy: This is so fascinating. @markgurman says that finished HomeViews have been “sitting boxed up in warehouses for the better part of a year.”
   > @mgsiegler: John Ternus needs to hire a supply chain expert ASAP. Might I suggest Tim Cook...
   > @jim_gresham: Duo pre order was a TOTAL SHIT SHOW. I was online in the store at 8am and shipping was already Nov 2. Tried to set an in store pickup and the stores couldn't be selected because it “isn't available to
   > @markgurman: Apple very clearly launched the iPhone Duo prematurely based on the supply available just to get it to market earlier. I believe they knew they wouldn't have a reasonable amount of supply until Novemb
   > @markgurman: Apple's iPhone Duo preorders were an absolute disaster. That may help the iPhone 18 Pro. More in Power On: https://www.bloomberg.com/...
   Also: 9to5Mac, Stratechery, Macworld, 9to5Mac, PCMag, SamMobile, Cult of Mac, The Shortcut, +21 more

19. Q&A with Nvidia's Vera team on agentic AI driving CPU demands and forcing CPU design priority back to single-threaded performance over core counts, and more
   Wccftech — https://wccftech.com/exclusive-nvidia-vera-team-says-chiplet-designs-sacrificed-single-threaded-performance-for-core-counts-and-agentic-ai-is-now-forcing-a-reversal/
   NVIDIA's Vera CPU heralds a redefinition of computing architecture from a traditional, task-isolated paradigm to an orchestrated …
   Also: Digital Trends

20. How the data center industry courts kids amid a backlash: 11+ firms and groups hosting field trips since 2025, flag kits and cards for first graders, and more
   Caroline Haskins / Wired — https://www.wired.com/story/data-center-industry-is-trying-to-woo-kids/
   Amid a wave of backlash, some industry-friendly groups are employing creative and time-tested strategies to woo the youth.
   Also: Columbian

21. Source: Anthropic is preparing a model with superior intuition and reasoning that can discern unstated intentions and is better at thinking outside of the box
    — https://www.theinformation.com/articles/anthropic-readies-model-reads-users-intentions-better

22. Vinted faces an influx of listings suspected of containing stolen goods following widespread French riots, which targeted Sephora, Louis Vuitton, and Burberry
   Yazhou Sun / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-19/vinted-faces-influx-of-suspected-looted-goods-after-french-riots
   Also: Telegraph, IGN

23. Survey: the chatbot gender adoption gap among US adults has closed since 2024, though men are more likely to use them daily; ChatGPT has identical use rates
   Pew Research Center — https://www.pewresearch.org/short-reads/2026/10/16/the-gender-gap-in-ai/
   Also: Music Ally

24. Foxconn agrees to acquire a 50% stake in Mitsubishi's automotive components unit for ~$727M; Mitsubishi will provide autonomous tech for Foxconn's EV platforms
   Reed Stevenson / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-19/foxconn-buys-727-million-stake-in-mitsubishi-electric-unit-that-makes-ev-parts
   Also: Nikkei Asia, Automotive World, Dow Jones Newswires, Taipei Times, DigiTimes

25. A profile of Alona Katz, chief of Brooklyn DA's Virtual Currency Unit, who recently led an operation that seized and disrupted over 240 crypto fraud websites
   Bloomberg — https://www.bloomberg.com/news/features/2026-10-17/how-a-brooklyn-crypto-cop-cracked-a-global-scam-network?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MjI5NDg2MSwiZXhwIjoxNzkyODk5NjYxLCJhcnRpY2xlSWQiOiJUTjIxS09LSVVQUzQwMCIsImJjb25uZWN0SWQiOiIwNEFGQkMxQkYyMTA0NUVEODg3MzQxQkQwQzIyNzRBMCJ9.TJtB0IVDmFtu-rsX1kq0V9O0320Ah0eRWmDK4POOkFE
   > @apompliano: This article about law enforcement and regulators working to take down crypto scams highlights the intricate cat-and-mouse game being played for years. @pattersonscott & team did a great job explainin
   > @business: Crypto scams cost Americans more than $11 billion last year. From a cramped Brooklyn office decorated with cat posters, prosecutor Alona Katz is finding new ways to fight the global networks behind th

26. AI's ability to forecast extreme weather faces a major test in the coming months amid a historic El Niño, as some scientists question the tech's accuracy
   Financial Times — https://www.ft.com/content/60bffbe3-f7aa-4813-b657-a31087e7b116?accessToken=zwAAAaFPPIA3kc9gv_vj96pIE9O2V6MQh-exFg.MEUCIQC302L7LYN0b4H7cc56Qhao045gUhnaQ5lY3hVqofsapwIgMamrT5GOqYwTANyeaAe4bKrPLm98_aPRWRc0jHYm4pk&sharetype=gift&token=47f0afa3-f0b0-49cc-8bef-ffb2288a135f
   Also: Wall Street Journal, Sky News

27. Survey of 94 economists: 54% expect AI's gains to spread across the G20 over the next decade, not just the US and China; 32 see African countries falling behind
   Financial Times — https://www.ft.com/content/c6aeb3a1-1874-4947-8ffc-4d993301244a

28. Stripe Link data shows agentic transactions increased by 38x and volume of payments by 20x in September, with retail leading in both, and a ~$100 average spend
   Alex Konrad / Upstarts Media — https://www.upstartsmedia.com/p/data-stripe-link-how-ai-assistants-spend
   > @alexrkonrad: DATA: Are AI assistants launching a new era of agentic commerce? @danhilltech, head of consumer product at @stripe, thinks so. I spoke to him for exclusive intel on how 70+ assistants currently use @l
   Also: The Decoder

29. Abby Care, which runs an AI-powered platform that trains and certifies family members as paid caregivers, raised an $82M Series C led by Transformation Capital
   Allie Garfinkle / Fortune — https://fortune.com/2026/10/15/startup-abby-care-raises-82-million-to-turn-family-members-into-paid-caregivers/
   > @alfred_lin: We invested in Abby Care because we need better home-based care options. All of us have felt the pain of how long it can take to get care at a medical facility. That pain is even worse for those who n
   Also: Abby Care, Inc, The SaaS News

30. Allium: stablecoin payments rose 45% YoY to $482B YTD through September 30, with transactions up 71% to 1.04B, while circulating supply grew just 0.4% to ~$305B
   Krisztian Sandor / CoinDesk — https://www.coindesk.com/business/2026/10/18/stablecoin-supply-stalls-but-payments-jump-45-as-visa-mastercard-and-stripe-connect-crypto-to-cash
   Also: Forkast, Bitcoin Insider, Times of India, Crypto Briefing

31. Intel unveils its GPU D-series for data centers, featuring up to 480GB of LPDDR5X memory, an unusually large capacity to support demanding inference workloads
   Efosa Udinmwen / TechRadar — https://www.techradar.com/pro/behold-intel-plans-a-480gb-gpu-a-video-card-with-more-memory-than-the-average-laptop-ssd-has-storage-but-of-course-its-for-ai-and-curiously-it-will-use-lppdr5x-not-even-gddr7
   Also: Intel, Digit

32. China's GDP grew 4.5% YoY in Q3, up from Q2's three-year-low growth rate of 4.3% but below Q1's 5%, as AI-driven exports helped offset weak domestic spending
   Osmond Chia / BBC — https://www.bbc.com/news/articles/cm5yn098xz8lo
   Also: CNN, Quartz, The Straits Times, The Guardian, Associated Press, Al Jazeera, The Asia Business Daily, Financial Times, +3 more

33. Analysis: 795 accounts funded by ADI Predictstreet's own fee-collecting wallet drove 99% of the FIFA-partnered prediction market's activity since late August
   Wall Street Journal — https://www.wsj.com/finance/nearly-all-volume-on-fifa-linked-prediction-market-is-circular-trading-549393f3?st=Mc7RQM&reflink=desktopwebshare_permalink

34. Europe's three biggest industrial companies are cashing in on the AI boom, as Schneider and Siemens expand further into software, while ABB focuses on equipment
   Aaron Kirchfeld / Financial Times — https://www.ft.com/content/5d45d66f-fd31-4263-b52f-54d9d88baa63

35. Stand Insurance, which uses digital twins of homes to price wildfire risk and insures $10B+ of property, raised a $70M Series C at a $1B valuation led by Saga
   Nick Lichtenberg / Fortune — https://fortune.com/2026/10/15/stand-insurance-wildfire-unicorn-raises-70-million-1-billion-valuation/
   > @superpobe: @Techmeme a billion valuation for a 70m raise seems steep
   > @huevatoi: @Techmeme digital twins for wildfire risk sounds like a smart pricing edge
   > @jasonxmueller: It's been a blast building @standinsurance alongside @danpres — we are actively setting the new standard for how to best protect and underwrite property. https://fortune.com/...
   > @ryan_falvey: Congrats to @danpres and the team @standinsurance on the latest fundraising milestone! We were proud to have been one of the first checks backing Dan's vision of AI and insurance, just a little over 2
   Also: FinTech Global, Ventureburn, ReinsuranceNe.ws, FinSMEs, The SaaS News

36. Sources: Nvidia asked Samsung, SK Hynix, and Micron to use TSMC's 3nm process to produce NVHBM memory base dies; Samsung agreed, its first use of TSMC for HBM
   Kyu-Seok Shim / Reuters — https://www.reuters.com/world/asia-pacific/samsung-use-tsmc-technology-nvidias-next-generation-memory-chips-seoul-newspaper-2026-10-18/
   > @nano_arun: “Samsung to use TSMC technology for Nvidia's next-generation memory chips, Seoul newspaper reports” When the times are crazy, interesting things happen https://www.reuters.com/...
   Also: The Information, Seoul Economic Daily, Tech Monitor, Electronics Weekly, Tech Times, SamMobile, SammyGuru, Wccftech, +2 more
