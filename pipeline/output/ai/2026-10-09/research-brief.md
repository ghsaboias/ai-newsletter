# Research — News Cluster

Search for news **events that occurred** between **2026-10-08 10:00 BRT** and **2026-10-09 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-08 10:00 BRT to 2026-10-09 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-09
**Research window:** 2026-10-08 10:00 BRT → 2026-10-09 10:00 BRT

**Previous edition headlines (2026-10-08 — skip unless genuinely new development):**
- anthropic-claude-haiku-5-5-launch: Anthropic launches Claude Haiku 5.5, ~75% cheaper than Haiku 4.5 and its first Haiku with effort controls
- google-cloud-gemini-agent-universal-work-agent: Google Cloud unveils Gemini agent, a 'universal agent for work' that runs multiday tasks
- fired-openai-researchers-letter-cot-monitorability: Three fired OpenAI safety researchers urge board to halt work that degrades AI monitoring
- ai-math-fallout-crypto-bunker-mode-ahm-boycott: After OpenAI's math dump, Buterin warns of AI risk to cryptography and a math group urges boycott
- crowdstrike-artex-ai-hacker-south-korean-banks: CrowdStrike: lone hacker used AI agents and LLMs to breach South Korean banks
- manus-500m-round-after-meta-unwind: Manus raises over $500M in first round since Beijing forced Meta to unwind its acquisition
- arena-200m-3-1b-alignment-index: AI leaderboard Arena raises $200M at $3.1B valuation and launches an Alignment Index
- samsung-q3-record-107-trillion-won-tsmc-record-quarter: Samsung guides record $80B Q3 operating profit on AI memory; TSMC books record quarter
- globalfoundries-tsmc-2b-silicon-interposer-malta: GlobalFoundries signs $2B, five-year deal to make CoWoS silicon interposers for TSMC in New York
- broadcom-50b-financing-openai-chips-oracle-apollo: Broadcom seeks $50B+ in private credit to fund OpenAI's custom chips; Oracle in chip-lease talks
- firmus-asx-ipo-falters-reprice-nvidia-backed: Nvidia-backed Firmus's A$44B ASX float falters as bankers weigh repricing or pulling the IPO
- nvidia-rtx-spark-n1x-surface-laptop-ultra-preorders: Nvidia opens RTX Spark Arm PC chip preorders with Microsoft's $2,599 Surface Laptop Ultra
- oratomic-475m-series-b-5-4b-universal-quantum-100m: Quantum hardware startup Oratomic raises $475M at $5.4B; Universal Quantum raises $100M+
- mecka-ai-60m-series-b-sequoia-robot-training-data: Robot-data startup Mecka AI raises $60M Series B led by Sequoia, with Nvidia and Samsung
- yandex-sasovo-data-center-drone-strike: Drones hit Yandex's Sasovo data center, first major attack on a Russian data hub in the war
- fed-minutes-ai-buildout-inflation-another-hike: Fed minutes cite AI buildout as inflation driver; most officials see another hike by year-end
- iran-warns-block-new-hormuz-oil-routes-reviews-us-reply: Iran warns Gulf states against new oil export routes as it weighs US reply on Hormuz plan
- iea-accelerate-oil-stock-release-diesel-brent-100: IEA members back faster release of emergency oil stocks, prioritising diesel, as Brent tops $100
- fda-approves-pfizer-tukysa-frontline-her2-maintenance: FDA approves Pfizer's Tukysa combo as chemo-free front-line maintenance for HER2+ breast cancer
- musk-starlink-india-oligarchs-government-rejects: India rejects Musk's claim that 'oligarchs' are blocking Starlink's launch
- fda-approves-novartis-rhapsido-symptomatic-dermographism: FDA approves Novartis' oral BTK inhibitor Rhapsido as first treatment for symptomatic dermographism

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 39 stories

1. AI researcher Mikita Balesni says he believes OpenAI fired him, Tomek Korbak, and Jasmine Wang “for prioritizing safety over the near-term interests of OpenAI”
   Mikita Balesni / @balesni — https://x.com/balesni/status/2108262814003687745
   Two other safety researchers and I were fired from OpenAI last week. We wrote this letter to leadership. I believe we were fired for prioritizing safety over the near-term interests of OpenAI as a cor
   > @j_asminewang: OpenAI fired me last week, along with two of my safety colleagues. I was given one reason: that I accessed an executive's email. I want to say this plainly, because too many of OpenAI's history is smo
   > @tomekkorbak: I was told verbally I was fired because of the way I communicated with METR. No details on what I said or did or when. No other reasons were given and nothing was put in writing. To be clear, talking 
   > @balesni: We were not given written reasons for our firing. In the exit call, I was told OpenAI no longer trusts me because I was speaking too much to third party safety organizations, implying I leaked company
   > @j_asminewang: We were not the first to be pushed out of OpenAI under suspicious circumstances. Unless the employees take a stand now against this kind of maneuver, I am concerned we will not be the last. The messag
   > @neelnanda5: This seems extremely sketchy behavior from OpenAI I don't want to pass judgement before hearing OpenAI's side, but I doubt these three are lying about not hearing good reasons And why would 3 associat
   Also: The Verge, Mikita Balesni blog, BBC, The Rundown AI, Engadget, Digit, Business Insider, The Information

2. OpenAI says it didn't fire three researchers for “raising safety concerns or speaking out”, but for violating “clear policies on handling sensitive information”
   Michael Considine / CNBC — https://www.cnbc.com/2026/10/09/openai-fired-researchers-ai-concerns.html
   OpenAI on Friday defended its decision to fire three safety researchers, saying they had committed a “significant breach of trust.”
   > @openainewsroom: A note from our research leaders: Last week we parted ways with Jasmine, Mikita, and Tomek after a thorough investigation found they violated clear policies on handling sensitive information. Our inte
   > @eliebakouch: this is a point by point response to the 3 points raised in the letter from the former oai employee who got fired [image]
   > @eliebakouch: i guess it's still the same issue, we'll never know what the “sensitive information
   > @heavyhelium11: > we want to address the points they raised in their letter directly spoiler - they didn't
   > @paul__walsh: If Jasmine's public response is true, and I believe it probably is given how quickly lawyers and a cybersecurity expert could prove it, OpenAI's IT staff granted her access to an executive's email and
   Also: Financial Express, Associated Press, Quartz, TechCrunch, Business Insider, The Decoder, Fortune, Al Jazeera, +6 more

3. President Trump awards Elon Musk, Jensen Huang, Lisa Su, and Sergey Brin the National Medal of Science at a White House summit promoting US innovation
   Jared Perlo / NBC News — https://www.nbcnews.com/tech/tech-news/trump-awards-musk-tech-titans-national-medals-science-rcna602104
   President Donald Trump joined Michael Kratsios to award the Medal of Science to Elon Musk, Jensen Huang, Lisa Su and Sergey Brin amid announcements about new science funding.
   > @elonmusk: Congratulations to Sergey, Jensen, Lisa, Michael and Satya!
   > @whitehouse: President Donald J. Trump, alongside Director of Science and Technology Policy Michael Kratsios, award six patriots the highest honor in science and technology, the National Medal of Science and the N
   > @saracarterdc: Progress for All humanity ....
   > @lisasu: It was an incredible honor to receive the National Medal of Science from @POTUS today. My parents came to America with big dreams and a deep belief in education and hard work. This country gave me the
   > @michaeldell: 42 years ago, I started @Dell with $1,000 in my dorm room. Today, I'm deeply honored to receive the National Medal of Technology and Innovation. 🇺🇸 Thank you @POTUS. This honor belongs to the incredib
   Also: SPACE.com, NSF, American Greatness, The Hill

4. President Trump awards Satya Nadella and Michael Dell the National Medal of Technology and Innovation during a White House summit attended by US tech leaders
   Washington Post — https://www.washingtonpost.com/politics/2026/10/08/trump-microsoft-nadella-musk-ai/2a7fcefa-c33f-11f1-8170-681419af1cc9_story.html
   > @hkarthik: Trump and Vance are definitely playing good cop/bad cop with Microsoft right now. This is what you do when you want something like favorable pricing on a multi-year government contract. Or to get the 
   > @jblunt1018: Vance seems to be running a competing administration. One side targets Microsoft while the other honors its CEO. Do they even talk to each other? 🤡
   > @satyanadella: Thank you, @POTUS, for this incredible honor today. I'm humbled to stand alongside so many giants of American innovation and looking forward for what we can continue to do together to advance technolo
   > @mattooshashank: Breaking: US President Trump honours Microsoft CEO Satya Nadella just hours after suspending Microsoft's ability to sponsor most foreign workers for green cards
   > @rapidresponse47: .@POTUS: “For more than three decades, @satyanadella has been a key figure in the transformation of Microsoft — revolutionizing the company and empowering businesses, students, and consumers from all 
   Also: Axios, Ars Technica, The White House, New York Post, diginomica, gulftoday, The Indian Express, Business Insider

5. Sources: Apple told some suppliers to cut iPhone 18 Pro and Pro Max component production by 15% to 20% as higher memory costs pushed up prices, hurting demand
   Nikkei Asia — https://asia.nikkei.com/business/technology/exclusive-apple-cuts-iphone-18-pro-orders-due-to-soft-demand
   TAIPEI — Apple has told some of its suppliers to cut production of components for its newly launched iPhone 18 Pro and iPhone 18 Pro Max …
   Also: Reuters, 9to5Mac, AppleInsider, MacRumors, The Crypto Basic, Deal N Tech, iClarified, MarketWatch, +10 more

6. Meta bans ByteDance's ads and paid marketing, plus third-party campaigns that link to TikTok, in the US, Canada, Egypt, Indonesia, Japan, Thailand, and Vietnam
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-08/meta-bans-tiktok-parent-bytedance-from-advertising-on-its-apps-in-7-countries
   Meta Platforms Inc. banned advertisements in the US from ByteDance Ltd., the former controlling owner of TikTok …
   > @yahoofinance: Meta is done taking TikTok's ad money. Meta began blocking all ads and paid messages from ByteDance on Thursday, including third-party ads that link to TikTok. The ban covers the US, Canada, Egypt, In
   > @newsguyusa: Forbes - TikTok's executives quietly defanged its advertising rules, opening the floodgates to fraudsters that target American users with fake sales of products that never arrive. https://www.forbes.c
   Also: The Verge, Ubergizmo, Wall Street Journal, Music Ally, Reuters, Yahoo Finance, Engadget, Advertising, Marketing …, +2 more

7. Sources detail Mark Zuckerberg's decision to launch Muse despite safety concerns, after seeing that AI startup Instinct's similar agent product gained traction
   Eli Tan / New York Times — https://www.nytimes.com/2026/10/09/technology/inside-mark-zuckerbergs-decision-to-pull-the-trigger-on-metas-ai-agent.html
   Meta had delayed releasing Muse, its A.I. agent app, for months over safety concerns. Then new competition forced Mr. Zuckerberg's hand.

8. Global PC shipments dropped 20.1% YoY in Q3 to 62.7M units due to higher prices and supply issues; Lenovo dropped 22.6% YoY, HP 30.9%, Dell 25%, and Apple 11.3%
   IDC — https://www.idc.com/resource-center/press-releases/idc-pc-tracker-3q26/
   Q3 delivered the widely expected PC downturn, with supply constraints, high price points, and logistical disruption eroding the usual seasonal lift
   > @firstadopter: IDC: “Worldwide PC shipments fell 20.1% year over year in Q3 2026 to 62.7 million units, according to preliminary results from IDC Research (IDC)” https://www.idc.com/... [image]
   Also: The Register, Windows Central, Thurrott, MacRumors, Club386, Tom's Hardware, 9to5Mac, GSMArena.com, +3 more

9. Microsoft denies JD Vance's claim it replaced thousands of US workers with foreign workers in 2025, saying 80% of H-1B applications were for existing employees
   Associated Press — https://apnews.com/article/h1b-visa-program-vance-microsoft-e7b3a407f822702b269ee277d21343ea
   President Donald Trump's administration announced Thursday it was suspending Microsoft and several other firms …
   > @bennyjohnson: The Indian stock market completely COLLAPSED today after the Trump Administration suspended H-1B and foreign labor programs over fraud. The largest IT outsourcing firms in the world, Cognizant, Infosy
   > @repbrandongill: We have no obligation to let corporations abuse our immigration system to undercut American wages and replace American workers with foreign labor. The H-1B program has gone so far off track that it's 
   > @seanhannity: Vance to Microsoft: you laid off 6,000 Americans and took 6,300 H-1Bs. Your green card pipeline is suspended.
   > @sonderling47: For years, the H-1B visa program has been manipulated by fraudsters and it's been allowed to run rampant—THAT ENDS NOW! The difference is @POTUS, @VP, and the @WHFraudTF—we are FUNDAMENTALLY CHANGING 
   > @nickadamsinusa: America doesn't need H-1B Visas. We have American workers.
   Also: Wired, Bloomberg, CNBC, Forbes, PR Daily, Breitbart, Fast Company, The Information, +9 more

10. Nvidia commits $1B over five years to build out the US' “capacity for super intelligence R&D” in fields like quantum computing, healthcare, and energy security
   Tobias Mann / The Register — https://www.theregister.com/hpc/2026/10/08/nvidia-found-1b-under-the-couch-to-help-secure-american-scientific-computing-dominance/5302110
   Commitment comes as GPUzilla prepares to fortify Uncle Sam's arsenal with at least seven AI-optimized supers
   Also: Nvidia Newsroom, HotHardware, Quartz

11. NY AG announces an up-to-$35M settlement with ex-Celsius CEO Alex Mashinsky that permanently bars him from the securities, commodities, and crypto industries
    — https://www.coindesk.com/policy/2026/10/09/new-york-ag-secures-up-to-usd35-million-and-lifetime-crypto-ban-from-celsius-alex-mashinsky
   New York Attorney General Letitia James said Friday she secured up to $35 million from former Celsius CEO Alex Mashinsky …
   Also: NY State Attorney General, The Block

12. A slew of cyberattacks hit Japanese companies in September, exposing the data of millions and prompting calls for security checks, as AI lowers hacking barriers
   Sarah Hilton / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-09/wave-of-cyberattacks-prompts-japan-to-urge-security-reviews
   A cascade of cyberattacks has hit Japanese companies over the past few weeks, prompting the government to call for security checks …
   Also: Reuters, Associated Press, Seoul Economic Daily

13. Meanwhile, a Sam Altman-backed bitcoin life insurance provider, raised $37.5M led by Bain Capital, sources say at a $350M valuation, up from $190M in April 2025
   Lucinda Shen / Axios — https://www.axios.com/pro/fintech-deals/2026/10/08/sam-altman-bitcoin-insurer-meanwhile
   Meanwhile, a Sam Altman-backed company offering life insurance in bitcoin, raised $37.5 million in funding, CEO Zac Townsend tells Axios exclusively.
   Also: Business Wire, The Block, CoinDesk, crypto.news, The SaaS News

14. Anthropic launches OSS Scanner, which provides free, opt-in security audits for open-source projects by sending AI-generated reports without human review
   Anthropic — https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source
   We're launching OSS Scanner, an opt-in vulnerability scanner for the open-source ecosystem informed by our experience using Claude …
   > @jeffreyleefunk: Anthropic launched an effort to help people patch the software vulnerabilities exposed by its own Project Glasswing, just like a careless camper starting a wildfire and later funding a fire department
   Also: The Register, The Verge, Security Affairs, Silicon Republic, Engadget, Implicator.ai, The Hacker News, Cyber Security News, +2 more

15. Anthropic debuts the Critical Infrastructure Defense Program to provide AI models, threat research, and on-site engineers, starting with CrowdStrike and others
   Sam Sabin / Axios — https://www.axios.com/2026/10/08/anthropic-critical-infrastructure-cybersecurity
   > @anthropicai: We're launching the Anthropic Cyber Mission, a new effort to secure critical infrastructure and open-source software. https://www.anthropic.com/...
   Also: Anthropic, SiliconANGLE, Forbes, Salesforce Ben, SecurityWeek, Cyber Security News

16. Sources: SoftBank is seeking to raise up to $100B from Gulf investors for a fund to buy companies and improve their operations with AI and other advanced tech
   Financial Times — https://www.ft.com/content/3bc0eaa5-a8d4-47e8-903c-7dd762d947dd
   Founder and chief executive Masayoshi Son has held talks with senior figures in the UAE in recent weeks
   > @ppgmacro: Shitbank - more BS from Son. Levered up to the eyeballs. Desperate for AI IPOs to pay down debt. Good luck getting cash from the Gulf countries who are now borrowing because of the war. Note 5y CDS in
   > @zephyr_z9: Masa will finesse MBS again lol [embedded post]
   Also: Bloomberg, Proactive, NewsMax.com, ZeroHedge News, Channel NewsAsia, Reuters, The Information

17. Sources: Netflix is preparing to cut ~5% of employees, or ~850 jobs, as early as next week, amid pressure over weakened engagement and a depressed stock price
   Matthew Belloni / Puck — https://puck.news/netflix-is-sharpening-the-layoff-axe/
   Facing pressure over weakened engagement and a depressed stock price, the streamer is prepping for a round of layoffs in the near future, per sources.
   > @theinsneider: The trades published 731 articles about the Skydance merger this week. I read each one and distilled them into a MASSIVE 5,000-word column that pulls no punches, including about the massive layoffs th
   > @mattbelloni: News: Netflix is about to lay off about 5 percent of the company. Details ⬇️⬇️ https://puck.news/...
   Also: Quartz, Deadline, Reuters, Variety

18. Sources: Flock plans to let go of ~270 employees, or 18% of its staff, at the end of October; the layoffs come after a voluntary buyout program in September
   Reuters — https://www.reuters.com/business/ai-surveillance-startup-flock-safety-cut-several-hundred-jobs-amid-backlash-2026-10-09/
   Flock Safety plans to let go of about 18% of its employees, people with direct knowledge of the plans said on Thursday …
   Also: TechCrunch, The Hill, Forbes Europe

19. A US judge sentenced Raheim Hamilton, co-creator of the dark web marketplace Empire Market, to 40 years in prison for facilitating $430M in illegal transactions
   Sergiu Gatlan / BleepingComputer — https://www.bleepingcomputer.com/news/security/owner-of-empire-cybercrime-market-gets-40-years-in-prison/
   The co-creator of Empire Market, one of the largest dark web marketplaces before its shutdown, has been sentenced to 40 years …
   > @darkwebinformer: 🚨 🇺🇸 Empire Market co-creator sentenced to 40 years for operating $430 million dark web marketplace Raheim Hamilton, 30, also known online as “Sydney” and “ZeroAngel,
   Also: The Record, US Department of Justice, Decrypt, CoinDesk

20. SpaceX agrees to acquire a low-band spectrum portfolio to help Starlink “become a major mobile carrier in the US”; AT&T, T-Mobile, and Verizon shares fall 5%+
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-08/spacex-to-acquire-low-band-spectrum-for-mobile-phone-service
   Elon Musk's SpaceX said it acquired low-band spectrum that will enable it to use its Starlink satellites to become a …
   > @elonmusk: Very big deal [embedded post]
   > @trengriffin: Radio spectrum is like invisible money. SpaceX will acquire 100% of Grain's nationwide 800 MHz spectrum portfolio. “Get Low” by Lil Jon & the East Side Boyz is really a song about in-building penetrat
   > @gvaresearch: $SPCX spectrum buy to connect Starlink satellite network to U.S. cell phones good for $FLTCF, sole supplier of E-band GaN SSPAs enabling ground stations to reach multi-gigabit speeds & bandwidth to pr
   > @stanphylcap: “Bloomberg reported in August that SpaceX was...interested in the spectrum. Musk...appeared to reject the idea, responding ‘not true’ on X” https://www.bloomberg.com/... What did I tell you guys yeste
   > @bdsams: If SpaceX shows up with a global plan for $30 a month...they would cleanup overnight. [embedded post]
   Also: 9to5Mac, Wall Street Journal, Wall Street Journal, DatacenterDynamics, Barron's Online, Morningstar, Proactive, NewsMax.com, +12 more

21. Jev developer TypeSafe AI raised ~$870M led by a16z at a $7.5B valuation with Sequoia and angel investors also participating; ~33% of the Fortune 500 use Jev
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-09/andreessen-horowitz-backs-jev-maker-at-7-5-billion-value
   TypeSafe AI, the startup behind Jev, a new artificial intelligence model that went viral after it launched only a few weeks ago …
   Also: RuntimeWire

22. Nvidia, Oracle, CoreWeave, and other AI stocks fell after a report that OpenAI's annualized revenue at September's end was $20B less than previously reported
   CNBC — https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html
   Shares of Nvidia, Oracle, CoreWeave and other artificial intelligence names sank lower on Thursday after the market learned more details about OpenAI's revenue.
   > @fitz_keith: @OpenAI counted its partners' revenue as its own. Wall Street's response? Sell the chipmakers. 🤦‍♂️ That's like shorting the casino because one gambler counted his buddy's chips. Wrong table, folks. N
   Also: Implicator.ai, Reuters, Quartz, Financial Times

23. Docs: OpenAI told investors its annualized revenue was nearing $50B at the end of September, well below the $70B reported by the media based on investor docs
   Financial Times — https://www.ft.com/content/b66a9858-f8fb-46cb-b506-44bfe26fca2a
   GitHub Copilot will soon determine when a task is best handled by on-device AI and when it needs cloud-scale models.
   > @tradeflooraudio: 👉👀 OpenAI Expects $70 Billion in Annualized Revenue by End of 2026 ... BBG On Thursday, tech shares led losses in the S&P 500 after reports that OpenAI's annualized revenue would be lower than some pr
   > @mikeisaac: i am not fully sure what the hell went on with all this weird OAI math but i do agree with dan that this is the most unsatisfying part of fragmented numbers leaks as a reader, one should go into any p
   > @samdagher: “OpenAI is in talks with multiple investment funds from the United Arab Emirates, including Abu Dhabi-based MGX, to help anchor its new financing round” https://www.bloomberg.com/...
   > @stevesi: @danprimack Microsoft, Amazon, Google have uniquely different cloud businesses and perfectly rational but different t approaches to GAAP, and that doesn't stop the street from doing comparisons and co
   > @jimcramer: I lack real clarity on whether the FT story on OpenAI is “new” news given my contacts at the company. But if FT doesn't take it back.. it doesn't matter
   Also: Bloomberg, CNBC, Barron's Online, PYMNTS.com, MarketWatch, Wall Street Journal, International Business Times, New York Times, +19 more

24. Sabi, which is building a baseball cap that uses 100K non-contact neuro-sensors to convert neural signals into text prompts for AI systems, raised a $50M seed
   Rashi Shrivastava / Forbes — https://www.forbes.com/sites/rashishrivastava/2026/10/09/vinod-khosla-backs-an-ai-startup-building-a-mind-reading-baseball-cap/
   > @kimmonismus: Sabi says it has raised $50M to build a cap that turns intended speech into text. …
   > @scobleizer: A baseball cap with 100,000 sensors, built so you can talk to your AI agents just by thinking. Khosla, Accel, Initialized, DST and Kevin Weil just put $50M behind @sabi. Most brain interfaces so far h
   > @hesamation: Brain foundation models after reading my thoughts. These guys just raised $50M to build their own chips for a cap that turns your thoughts into prompts. [video] [embedded post]
   > @rahulchhabra07: we have built non-contact neuro-sensors that can capture reliable signals even through hair these are low noise, take minimal power, and can fit inside a cap thanks to TSMC for helping fabricate the w
   > @rahulchhabra07: we've raised $50M from Khosla Ventures, Accel, Initialized, Kevin Weil, DST Global to build the world's most wearable BCI cap at Sabi read more here: https://www.forbes.com/...
   Also: TestingCatalog AI News

25. Analysis of 857 releases from nine Chinese AI labs from 2021 to September 2026: just 3.6% included safety results from the developer and only 1.1% did at launch
   SemiAnalysis — https://newsletter.semianalysis.com/p/beijing-will-not-pace-the-frontier
   > @niubi: Beijing Will Not Pace the Frontier: China's Speed-First AI Safety Regime by @SemiAnalysis_ https://newsletter.semianalysis.com/ ... “Nobody in China's AI industry is slowing down, and nobody is asking

26. The UK plans to curb non-compete rules that force employees to wait before moving jobs or starting companies, an issue that has drawn complaints from startups
   Shona Ghosh / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-09/burnham-says-uk-will-curb-non-compete-clauses-after-tech-ai-startup-outcry
   Also: Tech.eu, Pathfounders, City A.M.

27. The Chinese developer of ARTEX says they have converted the AI agent into a closed-source project after CrowdStrike said it was used to hack South Korean banks
   Brenda Goh / Reuters — https://www.reuters.com/world/china/chinese-developer-makes-artex-ai-agent-closed-source-after-korean-bank-hack-2026-10-09/
   Also: The Paypers, Security Affairs, The Information

28. Anthropic is setting up a “presidential engagement” program for the 2028 US elections that will offer AI policy education to candidates in both parties
   Emily Forlini / Fortune — https://fortune.com/2026/10/08/anthropic-presidential-engagement-program-hiring-political-lead-2028-elections/
   > @sameer_singh17: How kind. I'm sure this won't be self-serving at all. [embedded post]
   Also: AI Policy Daily

29. USV raised $900M, including a $500M early-stage fund, up from $275M in 2024, cuts its general partnership to four investors, and aims to lead more AI rounds
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-08/union-square-ventures-doubles-fund-size-shrinks-team-for-ai-era
   > @mollysoshea: BREAKING: USV Raises $900M in New Funds $500M dedicated for early-stage, & a $400M opportunity fund The largest fund cycle in the firm's history. FULL INTERVIEW + HQ TOUR For more than 20 years, Union
   > @mignano: The Next Chapter of USV
   > @colinarms: USV just announced $900M in new funds. They led our $5M round in 2024. They've been thinking about publishing, networks and ownership for a long time, and their new thesis gets at what we see every da
   > @nmasc_: Shakeup in VC land: Union Square Ventures has shrunk down its general partnership & “right-sized” its funds across a new $900 million haul. More w/ @RebeccaTorrenc5: https://www.bloomberg.com/...
   > @chrija: With this, we at @PointNineCap are the only firm left that stubbornly refuses to raise a larger fund. 😄🤔 (Not trying to put us into the same league as @usv and @benchmark with this comment!)
   Also: Union Square Ventures

30. Sources: Apple is planning an event on or around October 27 for its first touchscreen MacBook, an OLED iPad mini, a 14" MacBook Pro with M6, and an iMac with M6
   Mark Gurman / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-08/apple-set-to-debut-touch-screen-macbook-and-new-ipad-mini-in-late-october?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MTQ5MDMwMCwiZXhwIjoxNzkyMDk1MTAwLCJhcnRpY2xlSWQiOiJUTUtNUllLSVVQU1cwMCIsImJjb25uZWN0SWQiOiJDNEVEQ0FFMUZBMDU0MEJFQTI0QTlGMjExQzFFOTA4MCJ9.FtH_qR7-ZMoCNHSPZzDhdIAtFuxSSOo7BPD87jeDEW4
   > @markgurman: NEW: Apple's big October will continue on the 27th with a second event to launch the first touch-screen MacBooks, OLED iPad mini and M6 14-inch MacBook Pro & iMac. It follows the smart home launch thi
   Also: T3, Business Today, VideoCardz.com, Shortlist, AppleInsider, PCMag, Quartz, Fossbytes, +15 more

31. Filing: the US FTC is probing Block over inadequate customer service for frozen or deactivated Square accounts amid staffing cuts, following 1,500+ complaints
   Leah Nylen / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-08/ftc-probes-block-after-consumer-complaints-over-frozen-accounts

32. Sources: Apple promotes Carson Oliver to VP of the App Store and names Steve Smith as M&A chief, replacing Adrian Perica, who keeps iCloud, Fitness+, and News
   Mark Gurman / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-08/apple-names-steve-smith-m-a-chief-moves-adrian-perica-to-services-business?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MTQ4MTMxMSwiZXhwIjoxNzkyMDg2MTExLCJhcnRpY2xlSWQiOiJUTUtNVVBWVFRDWlIwMCIsImJjb25uZWN0SWQiOiJDNEVEQ0FFMUZBMDU0MEJFQTI0QTlGMjExQzFFOTA4MCJ9.1w8Mo4fh5SSJ-nNQ5DAatEHpdItwM5wKUnR5XcJw7os
   > @markgurman: Perica and Apple Music head Oliver Schusser are the two eventual successors to Eddy Cue. Either one or the other or both together.
   > @markgurman: NEW: Apple is naming Steve Smith its new M&A chief, shifting longtime dealmaking head Adrian Perica to focus exclusively on his responsibilities overseeing parts of the company's services business. It
   Also: MacDailyNews

33. Firmus abandons its IPO and plans to pursue a private funding round instead, after some investors suggested its pricing strategy is aggressive
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-08/nvidia-backed-firmus-is-set-to-postpone-ipo-weigh-private-round
   > @tommyr345: Basically Firmus will ask Nvidia to fund it some more to buy some chips off Nvidia https://www.bloomberg.com/...
   Also: Financial Times, BBC, Reuters, Light Reading, Hindustan Times, Barron's Online, Bloomberg, Quartz, +2 more

34. Anthropic updates its usage policy to ban “sustained and needless abusive or cruel behavior” toward Claude; ending chats is “the primary enforcement mechanism”
   Hayden Field / The Verge — https://www.theverge.com/ai-artificial-intelligence/1008100/anthropic-new-usage-policy-abuse-claude
   > @levie: This sounds weird, but it is actually probably a good policy. Even if you don't believe AI is conscious (I don't), it stands to reason that you don't want future models trained on endless content of h
   > @bgurley: Strikes me this implies the company is certainly using customer's prompts as part of the training data? Otherwise, why would it matter? There would be no impact to the larger system. Open to hearing w
   > @paultassi: Please don't be mean to the sentient artificial life form we created but also we will continue to charge you monthly to keep him as an indentured servant
   > @orbitant: Anthropic's first usage policy update in over a year bans “sustained and needless abusive or cruel behavior” toward Claude. The main penalty is Claude hanging up. The weapons rules matter more to buye
   > @micsolana: truly do not mean to be pedantic here, but if a company is concerned with the welfare of chatbots to the degree it does not want us to be mean to them, how is this not slavery?
   Also: Anthropic, The Guardian, TechCrunch, BBC, PCMag, Yahoo Finance, MediaNama, Search Engine Journal, +7 more

35. Trump says the WH considers as “THE ENEMY” anyone who uses the term Artificial Intelligence, not “the highly accepted” and “more accurate” Super Intelligence
   Donald J. Trump / @realDonaldTrump@truthsocial.com — https://truthsocial.com/@realDonaldTrump/117406176604364910
   > @arikahenry: The phrase “faux pas” would be a radical understatement here. Here is the link to the post whereby President Donald J. Trump manages to trivialize both the first amendment AND national security in one
   > @markgurman: It's going to be absolutely fascinating to see what Apple does here.
   > @jamiedupree: A lot of Trump supporters keep telling me that this is fake news and was generated by AI. Nope - this is an actual Trump post. https://truthsocial.com/... [image]
   > @cwarzel: weird obsession imo!
   > @lexnfx: The White House's https://ai.gov/ page has now officially been updated to SI GOV. Unfortunately, the URL is still https://ai.gov/...
   Also: CNET, The Verge, Axios, Music Ally, Bloomberg, Reality Tea

36. OpenAI disrupts a Russian influence campaign tied to the Politology network that targeted schools, media, and foreign officials, and gives it a 5/6 impact score
   Kevin Collier / NBC News — https://www.nbcnews.com/tech/security/openai-chatgpt-russian-influence-operation-targeting-latin-america-rcna602066
   > @arashbehgoo: 🚨OpenAI banned operation “Bogus Bylines” that used ChatGPT to pitch long-form US-Iran conflict articles under seven fake Western “journalist” bylines. ~100 pieces landed in small/medium outlets. Perso
   > @aghamilton29: OpenAI has revealed Iranian operatives used AI to create and plant articles claiming to be from Western journalists. They also created social media accounts for the fake journalists and flooded relate
   Also: OpenAI, Washington Post, The Record, The Hill, Euronews, NPR, The Decoder, Business Today

37. Google Cloud unveils the Gemini agent, which can handle multiday enterprise workflows in Workspace, Microsoft 365, and Slack using Gemini and other AI models
   Carl Franzen / VentureBeat — https://venturebeat.com/orchestration/google-cloud-unveils-persistent-gemini-agents-for-long-running-tasks-and-they-get-their-own-gmail-calendar-and-drive-storage
   > @thomasortk: Today at Google Cloud's Gemini at Work event, we announced Gemini, a new single universal agent for work that has all of your business context and can be used for everything from knowledge work to ans
   > @sundarpichai: Great to be with 700+ @googlecloud customers at the historic NASA Hangar One for Gemini at Work! Today, we introduced the new Gemini agent, a single, universal agent for work that has all of your busi
   > @jeremiahdillon: Google is playing to win. Here's how you can tell: directly competitive products like Slack and models like Claude are not only supported by the product but also featured in the marketing. I can tell 
   > @mtslive: SITUATION EXPLAINED: Google just turned Gemini into one universal agent for work, and it can use Anthropic's Claude too. • It chats, works on objectives by itself, makes images and media, and writes a
   > @newsfromgoogle: Announced today at #GeminiAtWork from @GoogleCloud: ✨ Gemini is becoming your universal agent for work. It answers your questions, handles your knowledge work, creates images and media, and writes and
   Also: Google Cloud Blog, Google, Implicator.ai, Forkast, Communicate Online, Computerworld, TechRadar, Advertising, Marketing …, +8 more

38. Amazon unveils Alexa Tablets, replacing Fire tablets, with Android and Google Play Store: 12 Pro for $500+, 11 for $330+, and 8 for $230+, shipping October 14
   David Pierce / The Verge — https://www.theverge.com/tech/1007648/amazon-alexa-tablets-price-specs
   > @panos_panay: The Kindle experience on the new Amazon Alexa Tablets is rad. The 3:2 ratio is perfectly balanced to get more of the page on screen, and when you open a book, magic happens. The whole display changes.
   > @amazon: Introducing all-new Amazon Alexa Tablets, the first tablets with Alexa+ built into the core. Three new tablets. Aluminum unibody design. Vivid high-res displays. And intelligence that actually helps. 
   > @parkerortolani: uh is that the Play Store icon
   > @panos_panay: Introducing the Amazon Alexa Tablets, all-new tablets with world-class hardware, personalized intelligence from Alexa+, seamless integration of Amazon services right out of the box, and full Google Pl
   > @markgurman: The new Alexa Tablets are absurd for their price points and compete with the iPad Air.
   Also: About Amazon, Yanko Design, The Verge, About Amazon, SamMobile, Fortune, Phandroid, SammyGuru, +12 more

39. Xbox launches XP, a unit that will manage four non-gaming “investment areas”: Xbox Pictures for film and TV, Xbox Products, Xbox Places, and Xbox Partnerships
   The Verge — https://www.theverge.com/games/1007602/xbox-xp-division-film-tv-products-events
   > @drewcoffman: xbox just put the person who spent 13 years at lucasfilm and helped build minecraft into an entertainment empire in charge of a new division for movies, merchandise, theme parks, etc they're taking th
   > @tomwarren: Xbox is launching a new film and TV division. It's called “XP,” a play on Experience Points, and it will focus on film, TV, products, live events, and partnerships https://www.theverge.com/... [image]
   > @tomwarren: Tom Warren (@tomwarren) on X
   > @genki_jpn: Xbox announced a new film, TV and entertainment division called XP! Its goal is to expand Xbox's franchises to become the number one entertainment company in the world. https://news.xbox.com/... [imag
   > @deeketweak: Sharma has the Four Cs, Matt reveals the Four Ps: https://news.xbox.com/... [image]
   Also: XBOX Wire, PC Gamer, PocketGamer.biz, KitGuru, Advertising, Marketing …, Bloomberg
