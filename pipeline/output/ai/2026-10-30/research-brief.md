# Research — News Cluster

Search for news **events that occurred** between **2026-10-29 10:00 BRT** and **2026-10-30 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-29 10:00 BRT to 2026-10-30 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-30
**Research window:** 2026-10-29 10:00 BRT → 2026-10-30 10:00 BRT

**Previous edition headlines (2026-10-29 — skip unless genuinely new development):**
- google-gemini-4-carbon-frontier-model: Google unveils Gemini 4 Carbon, tops AA Index v5, but limits access to cyber defenders
- github-copilot-fusion-ga-universe: GitHub makes Copilot Fusion multi-model router generally available at Universe 2026
- deepseek-moonshot-distilled-gpt-6-astra: Report: DeepSeek and Moonshot distilled OpenAI's GPT-6 Astra to train their latest models
- cognition-weighs-round-70b-80b-valuation: Cognition weighs new round at $70B-$80B valuation, weeks after raising at $48B
- wabi-raises-55m-1-25b-valuation: Replika founder's Wabi raises $55M at $1.25B valuation for group-chat AI assistant
- google-ai-mode-ads-global-lower-monetization: Google takes AI Mode ads to 10 countries after admitting AI Mode monetizes less
- microsoft-copilot-daily-users-50-percent-agents: Microsoft: Copilot daily users up ~50% in a quarter; 50M agents in Agent 365
- samsung-q3-record-100t-won-profit-capex-84t-hbm-sold-out-2027: Samsung posts first-ever 100T-won quarterly profit, lifts 2026 capex 60% as 2027 HBM sells out
- marvell-advanced-talks-acquire-lumentum: Marvell in advanced talks to buy $83 billion optics maker Lumentum, Bloomberg reports
- nvidia-huang-megaspeed-alice-huang-chinese-intelligence-asset-nyt: NYT: US officials say Megaspeed exec close to Jensen Huang is a Chinese intelligence asset
- doj-inquires-nvidia-hugging-face-deal-antitrust: DOJ questions Nvidia's $12.93B Hugging Face deal as broader antitrust probe of chipmaker continues
- furiosaai-620m-series-d-2-9b-valuation: Korean AI chip startup FuriosaAI raises $620M Series D at $2.9B valuation
- stmicro-q3-beat-raises-data-center-revenue-forecast: STMicro beats Q3 profit estimates, raises 2026 AI data-center revenue forecast to $1.3B
- apple-touchscreen-macbook-pro-proled-m5-max: Apple launches first touchscreen Mac: OLED MacBook Pro with M5 Pro/Max, $400 pricier
- fed-holds-rates-two-dissents-for-hike-warsh-strategy-meetings: Fed holds rates at 3.75%-4% as two officials vote for a hike; Warsh adds strategy-only meetings
- hormuz-three-tankers-hit-mines-iran-drone-claim-seven-day-plan: Iran says three tankers hit mines in Hormuz's southern lane; US denies losing a drone
- doordash-to-acquire-instacart-17-billion: DoorDash agrees to buy Instacart for about $17 billion, $65 a share
- kalshi-raises-1b-40b-valuation-sequoia-wellington: Kalshi raises $1 billion at a $40 billion valuation, plans to expand beyond prediction markets
- dhs-icepick-leak-41000-employees-ice-cbp: Hacktivists leak data on 41,000+ DHS staff, including undercover ICE agents
- putin-praises-musk-rassvet-starlink-coordination: Putin calls Musk a 'real genius', says Russia coordinates with him on Rassvet and Starlink orbits
- pentagon-freezer-malfunctions-suspected-cyberattack: Pentagon treats freezer failures at six-plus US base stores as suspected cyberattack

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 44 stories

1. Binance says initial investigation suggests a compromised DevOps laptop may have enabled a ~$6.3B hack; Tether froze 1.5B+ USDT and Circle froze 800M+ USDC
   The Block — https://www.theblock.co/news/markets/2026-10-29-binance-investigating-hack-suspicious-outflows-5-billion-432171
   Onchain data shows about $3.55 billion in incoming transfers to the unlabeled wallet, with nearly $900 million subsequently moved across other wallets.
   > @cz_binance: User funds are safe! It does look like a hack on Binance. Appreciate the quick freeze from Tether (~$971m) and Circle (~$823m). I don't manage Binance (.com) anymore, but as a shareholder, I expect al
   > @binance: Our teams are aware of reports of a potential security issue and are actively investigating. User funds are completely safe. Our security teams are reviewing all relevant information with urgency, and
   > @paoloardoino: Tether froze more than 1.567B USDT related to a potential Binance exchange hack. Protecting the industry and our partners is our main priority. Stay safe everyone.
   > @binance: Binance's initial investigation suggests that the security incident may involve a compromised DevOps engineer's laptop, which allowed an attacker to gain access to a service container and submit unaut
   > @jerallaire: Circle is closely tracking reports of a potential exploit involving Binance. In coordination with law enforcement, we have frozen more than 800M USDC associated with the incident and will continue sup
   Also: Decrypt, CoinDesk, Binance, Wall Street Journal, Reuters, Aave, CoinDesk, Reuters, +21 more

2. TRM Labs attributes the Binance hack to North Korea-based TraderTraitor, which drained ~$6.36B from Binance wallets across 10 blockchains, mostly in ~20 minutes
   Tom Westbrook / Reuters — https://www.reuters.com/legal/government/blockchain-analysis-firm-trm-says-north-korea-behind-binance-crypto-theft-2026-10-30/
   North Korean hackers were behind a $6.3 billion raid on cryptocurrency exchange Binance, according to US blockchain analysis firm TRM Labs.
   > @mkjrstad: TRM Labs (@trmlabs) has attributed the record $6.36 billion Binance hack to North Korea's TraderTraitor. North Korea is known to have a preference for BTC, so they will probably dump all the ETH 📉 htt
   > @jroosen: TraderTraitor - DPRK yet again it seems. https://www.trmlabs.com/...
   > @zephyr_z9: Best crypto trader in the world
   Also: TRM Insights, Citation Needed, Wired, CNN, BBC, Financial Times, PYMNTS.com, Finimize, +33 more

3. Binance “temporarily suspended” all deposits and withdrawals as it investigates security issues and works with law enforcement; Binance.US says it's unaffected
   George Steer / Financial Times — https://www.ft.com/content/c7f5e395-c3a9-430e-b757-5014527b4d49
   Tether and Circle freeze billions of dollars' worth of their coins as world's largest crypto exchange investigates security issue
   > @binance: We are working non-stop to resolve this issue. Binance will cover all losses. As a precaution, all deposits and withdrawals are temporarily suspended while our team conducts security checks, freezes f
   > @binance: Our team is conducting security checks. Withdrawals will resume as soon as the security issue is fully resolved. User funds remain safe. We'll keep you updated. Thank you for your patience.
   > @heyibinance: User funds are safe. Binance will cover all hacking losses. Deposits and withdrawals are temporarily suspended while our team conducts security checks, freezes funds, and works with law enforcement. W
   > @binanceus: https://binance.us/ is not affected by the reported https://binance.com/ security incident. We are a separate, independent platform, and customer funds and services are secure and operating normally. 
   > @eowynchen: Our teams are working around the clock on this security issue. I want to be direct: user funds remain SAFE. …
   Also: OmniTrace, Euronews, CNBC, Protos, The Straits Times, Coinpedia Fintech News, Axios, crypto.news, +21 more

4. Binance reveals that a follow-up investigation has found “additional points of breach” beyond a possibly compromised laptop and says this was a “complex attack”
   @binance — https://x.com/binance/status/2116089661408108712
   Investigation update: Our initial investigation suggested that the security incident may have involved a compromised laptop, however our subsequent investigation has uncovered additional points of bre
   Also: Business Insider, Business Today, Reuters, Decrypt, BleepingComputer, Cointelegraph, Bitcoin News, Bitcoin Insider, +2 more

5. Binance pledges to cover all losses from a ~$6.3B hack, potentially the largest crypto theft ever, surpassing the $1.5B Bybit hack in February 2025
   South China Morning Post — https://www.scmp.com/business/cryptocurrency/article/3372664/binance-pledges-cover-losses-after-us6-billion-crypto-hack
   Also: BBC, New York Times, Forbes, Silicon Republic, Cointelegraph, nltimes.nl, CryptoSlate, Bitcoin Insider, +17 more

6. Amazon reports Q3 revenue up 12% YoY to $201.94B, vs. $202.31B est., net income down 2% to $20.7B, forecasts Q4 revenue below est.; AMZN drops 7%+ after hours
   Amazon — https://www.businesswire.com/news/home/20261028373648/en/
   Operating income was $28.1 billion and operating margin was 13.9%—Amazon's highest operating margin ever AWS net sales increased 39.3% …
   > @sebasaherrera: During a call with analysts following today's earnings, Amazon CEO Andy Jassy took a swipe at shopping agents like Meta's Muse. He said “few customers are doing much shopping this way yet, as the expe
   > @stocksavvyshay: One of the craziest lines from $AMZN earnings was Andy Jassy saying “we're installing an AI accelerator about every 14 seconds” with customers taking up capacity almost as fast as AWS brings it online
   > @benbajarin: $AMZN “it's important to remember that the vast majority of global IT spend, about 85%, is still on premises. And we're in a 10 to 20-year cycle where that equation will flip to the cloud.”
   > @sebasaherrera: Some initial info coming out of Amazon earnings: - Revenue miss impacted by lower-than-expected ad sales - Operating income guidance also lower than what was expected - Growth in AWS (39.3%) is being 
   Also: Semafor, Coinpedia Fintech News, Reuters, Political.org, Bloomberg

7. Amazon reports Q3 AWS revenue up 39% YoY to $45.98B, above $45.29B est., and AWS operating income up 55% to $17.77B, above $16.97B est.
   Jordan Novet / CNBC — https://www.cnbc.com/2026/10/29/aws-q3-earnings-report-2026.html
   > @corytv: Amazon's AWS grew 39% to $46.0B, its fastest pace in nearly five years. Shares fell 5% after hours. Peak acceleration, or a market fixated on capex? https://www.youtube.com/... $AMZN 🎙️ @DrillDownPod 
   Also: The Elec, Neowin, Motley Fool, Tech Times

8. Amazon spent $77B+ on property and equipment in Q3, leading to a free cash outflow of $42.4B; Amazon said in July that it would likely spend $220B in 2026 capex
   Matt Day / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-29/amazon-spending-soars-on-effort-to-meet-demand-for-ai-services
   Also: Fortune, Yahoo Finance, Business Insider, The Business Times

9. Andy Jassy says Prime Video has “a revenue run rate in the tens of billions of dollars and is now profitable in its own right”
   Julie Bort / TechCrunch — https://techcrunch.com/2026/10/29/andy-jassy-says-prime-video-is-on-track-to-earn-tens-of-billions-of-dollars/
   Also: Broadband TV News, Storyboard18, Livemint

10. On Amazon's earnings call, Andy Jassy says outside AI shopping agents are “still not great, nor more convenient than coming to a retailer directly”
   Sebastian Herrera / Fortune — https://fortune.com/2026/10/29/amazon-ceo-says-shopping-agents-like-metas-muse-not-great/
   > @quinnypig: I think @ajassy is one of the smartest business minds of our generation, but my lived experience is the complete opposite of this statement. [embedded post]
   Also: The Information, Livemint, Adweek

11. Amazon reports Q3 ad revenue up 11% YoY to $19.64B, vs. $20.82B est., and subscription services revenue up 11% YoY to $14B
   Annie Palmer / CNBC — https://www.cnbc.com/2026/10/29/amazon-amzn-q3-earnings-report-2026.html
   > @rihardjarc: An $AMZN and $META Muse deal is probably coming. Comment from $AMZN Jassy on the call: [image:" Though we anticipate working with horizontal agents"]
   Also: RTÉ, Storyboard18, Times of India

12. Intel reports Q3 revenue up 21% YoY to $16.5B, vs. $16.5B est., and forecasts Q4 revenue and adjusted EPS below estimates; INTC drops 23%+ after hours
   Katie Tarasov / CNBC — https://www.cnbc.com/2026/10/29/intel-intc-q3-earnings-report-2026-.html
   Intel shares plummeted more than 20% in extended trading on Thursday after the chipmaker issued a weak fourth-quarter forecast, citing continued softness in the global PC market.
   > @jukan05: I think Intel badly underestimated how quickly higher memory prices would hit PC demand and trigger an inventory correction. Those risks were already visible by the Q2 earnings call. Management acknow
   > @patrickmoorhead: Here's what I said on @YahooFinance on in response asked to five questions on $INTC : 1. What stands out? A really good quarter: met on revenue, beat on almost everything else. It's the guide. Q4 is ~
   > @benbajarin: I'd like to believe Intel that the PC slowdown gets better 2H27 but I don't think so and that is not what we are modeling for the sector currently. 2027 may not be as negative as 2026 but I still thin
   > @trengriffin: Intel just started a new dance Called the Tighten Up First tighten up on the DDR5 SDRAM Now tighten up on that LPDDR5 Tighten up on that GDDR7 now Yeah, dance the Tighten Up. H/T Archie Bell and the D
   > @austinsemis: Lip Bu says “Foundry can build your CPU! Doesn't have to be an Intel CPU either”... happy to hear that explicitly: “We are also open to building any CPUs at scale for our customers, fully [agnostic] t
   Also: Financial Times, Intel, Nikkei Asia, Reuters, CTech, Finimize, Telegraph, Dow Jones Newswires, +8 more

13. Sources: Nvidia is in talks to provide Nscale with billions of dollars in credit guarantees for debt to develop a 460MW data center that Anthropic plans to use
   Phoebe Liu / The Information — https://www.theinformation.com/articles/nvidia-talks-provide-billions-credit-support-cloud-providers-45-billion-anthropic-deal
   Nvidia is in talks to provide Nscale, a young AI cloud provider, with billions of dollars in credit guarantees for debt to develop …
   > @rohanpaul_ai: Nvidia is negotiating to guarantee likely more than $5B in construction debt for Nscale's 460MW Anthropic data center. per The Information The unsigned deal would back the West Virginia building's val
   > @_pheebini: New: Nvidia is discussing a different credit support structure for Nscale's 460MW data center campus that Anthropic has a $45 billion contract to use—a residual value guarantee for the data center its
   > @amir: in other Nvidia news... co still working hard to help neoclouds get by, this time Nscale's facility for Anthropic. but it's a different type of credit guarantee / backstop than the ones Nvidia has don
   > @stocksavvyshay: $NVDA is reportedly in talks to provide over $5B in credit guarantees for Nscale's 460MW data center backed by a $45B $ANT compute contract. Nvidia would essentially be financing power and constructio
   > @stockmktnewz: NVIDIA $NVDA IS IN TALKS TO BACK BILLIONS OF DOLLARS OF DEBT FOR AI CLOUD STARTUP NSCALE The credit guarantees would help Nscale build a 460-megawatt data center that Anthropic plans to use, per The I
   Also: Bloomberg

14. Inside Nscale's 2,250-acre, 8GW Monarch Compute Campus in West Virginia, which has been hit by construction issues, local opposition, and financing risks
   Financial Times — https://www.ft.com/content/ee86c4b6-1fe4-467e-8f18-9c08df288aff?accessToken=zwAAAaIi1GfplNO5KUuRDu5BO9O93gVp9IU5udPuhsS2H-RGftOPGJwI3yiK_9PrOGFWW_lO3dOA8oA_3uHjPdPy3p88MpBOh9O7wlVDACXyqwE.MEUCIQCTfptZcpPISYntlhh1mjoa3g6HxEZajv0OSQGMtt_QEQIgSVZwVMNDn0Bf_KARrNJmOPbLhMU516inUsUkdvr2i-0&segmentId=7d4bcc2e-e664-92ba-62e3-5590579f1902
   Also: Reuters

15. Reddit reports Q3 revenue up 53% YoY to $895M, vs. $878M est., DAUq up 12% to 130.3M, below est., forecasts Q4 revenue below est.; RDDT drops 17%+ after hours
   Jonathan Vanian / CNBC — https://www.cnbc.com/2026/10/29/reddit-rddt-q3-2026.html
   Reddit plans to require all users to create official accounts to access the social media platform, marking a major departure for the site known as …
   Also: Reddit Upvoted, Platformer, TechCrunch, Yahoo Finance, The Verge, Investing.com, Gizmodo, Reuters, +3 more

16. Reddit plans to require users to log in to fully access the site in response to AI scraping, and to begin tests in select markets outside the US this quarter
   Sara Fischer / Axios — https://www.axios.com/2026/10/29/reddit-logged-in-ai-search-incognito
   > @rhyssullivan: Discord removing their sign in requirement Reddit adding one
   > @naranciagaming: the quorafication of reddit is proceeding ahead of schedule
   > @steelcityclaire: the search engine is now officially dead, long live slop
   > @lutherlowe: Google is destroying what's left of the open web.
   > @sarafischer: NEW: In a huge departure from its 21 year history as an open web champion, @Reddit is moving to become a primarily logged-in experience — I spoke w CEO Steve Huffman & COO Jen Wong about why now, and 
   Also: The Verge, Thurrott, Engadget, TechRadar, CyberInsider, Ars Technica, Business Insider, The Independent, +2 more

17. NYSE owner ICE plans US-regulated Hyperliquid-based perpetual markets with Trade.xyz, a market operator on the crypto platform, and takes a stake in Trade.xyz
   Katherine Doherty / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-29/nyse-owner-plans-market-for-hyperliquid-perpetual-futures-in-us
   Intercontinental Exchange Inc. joined forces with one of the market operators behind offshore crypto-trading platform Hyperliquid …
   > @tradexyz: trade[XYZ] and ICE, owner of the New York Stock Exchange, are joining forces to bring 24/7 perpetual futures on Hyperliquid to the United States. In just over a year, our markets on Hyperliquid have s
   > @standuquesne: I am excited to be an investor in trade(xyz) as they partner with ICE to bring 24/7 perpetual futures on Hyperliquid to the United States. As a market participant, I am looking forward to to using the
   > @hyperliquidx: Intercontinental Exchange (ICE) and trade[XYZ] have announced their plan to use Hyperliquid as the infrastructure layer to deploy perpetual futures markets for US traders across crypto, equities, comm
   > @elonmusk: Interesting
   > @blknoiz06: i think some of the biggest opportunities around Hyperliquid over the next few years could come from the applications built on top of it equity perps are particularly interesting to me. Hyperliquid is
   Also: The Block, Bitcoin Insider, Intercontinental Exchange, The Coin Republic, CNBC, Financial Times, CoinDesk, Yahoo Finance

18. CrowdStrike: China-linked hackers used AI tool ARTEX with a DeepSeek LLM and another model to target 200+ organizations in 11 days, compromising at least nine
   Kevin Collier / NBC News — https://www.nbcnews.com/tech/security/china-linked-hackers-used-ai-target-200-organizations-crowdstrike-says-rcna606343
   Chinese state-linked hackers targeted more than 200 organizations in just 11 days, using AI to attack governments and businesses worldwide, according to CrowdStrike.
   > @ezesecops: Pray for your incident response teams [embedded post]
   > @orwelian84: get ya models now bows — the free for all is coming to an end [embedded post]
   > @benbajarin: As our reports have fleshed out. The frontier is necessary for defense. Enterprise security shields for agentic can't roll out fast enough. As our CSO survey will show, agentic cyber budgets about to 
   > @a_real_society: Honestly only 9 hits in 2 work weeks is a horrible hit rate. I bet I could bat .500 [embedded post]
   > @cyber_o51nt: VAPOR PANDA used ARTEX and AI models to conduct simultaneous espionage intrusions against more than 200 organizations worldwide, deploying BLOODALCHEMY and checking for unprotected hosts. https://www.
   Also: CrowdStrike, Seoul Economic Daily, Unite.AI

19. Dream, which is training AI world models on US building data to automate construction design and engineering, emerges from stealth with a $17M seed led by a16z
   Marina Temkin / TechCrunch — https://techcrunch.com/2026/10/29/ex-palantir-execs-launch-dream-with-17m-from-a16z-to-build-ai-world-models-for-construction/
   Andy Alder and Arjun Mather were Stanford roommates who both studied computer science before spending a decade at Palantir.
   Also: Dream, SiliconANGLE

20. Coinbase reports Q3 revenue down 35% YoY to $1.22B, in line with est., and net income up 66% to $719M, its first profit in a year, on unrealized crypto gains
   Olga Kharif / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-29/coinbase-returns-to-profitability-while-posting-another-revenue-drop
   Coinbase Global Inc. returned to profitability for the first time in a year while posting a quarterly decline in revenue …
   Also: Coinbase, Unchained, The Block, crypto.news, PYMNTS.com, CNBC

21. Polymarket resumes trading after a security incident with a third-party provider, which a source says is DebugBear, and says it will reimburse affected traders
   Reuters — https://www.reuters.com/business/polymarket-reports-major-outage-suspends-trading-actions-2026-10-29/
   Polymarket said on Thursday it had restored trading after a temporary halt prompted by a security incident involving a third-party provider …
   > @polymarkettrade: We've identified & fixed an issue impacting our international platform, Polymarket.com. One of our 3rd party providers was compromised, and we have referred this to relevant law enforcement. Anyone wh
   > @shanaka86: JUST IN: The code that drained Polymarket accounts on 29th October was set to skip any account worth under $10, per Hudson Rock's read of the script. The drainer in June's Polymarket theft skipped any
   > @pirat_nation: Polymarket has been hacked, users have reported their money got stolen >Users reported suspicious activity, missing money and positions being closed without their permission. >Polymarket blamed the is
   > @peterwildeford: Polymarket was hacked 👀 ...A compromised third-party script on its site drained over $2.5M from users and sold off their positions. Second time since June the same kind of attack has hit them.
   > @chrispavlovski: DHS hacked Polymarket hacked Binance hacked I know trends when I see them, this is a trend that's accelerating and is incredibly concerning. Incredible work by Tether and @paoloardoino for helping to 
   Also: The Record, The Block, BleepingComputer, NBC News, crypto.news, Washington Post, CryptoSlate, SecurityWeek, +4 more

22. Source: Anthropic is “Customer B” cited by SpaceX in a filing as its single largest customer accounting for 34.5% of Q3 revenue, surpassing the US government
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-29/spacex-s-largest-revenue-source-is-a-finite-deal-with-anthropic
   Anthropic PBC is SpaceX's largest single customer, a person familiar with the matter said, accounting for more than a third …
   > @andrewcurran_: Customer B has been revealed. Anthropic is SpaceX's largest single customer, overtaking NASA and the Pentagon for the first time. 34.5% of SpaceX's revenue last quarter was from compute-as-a-service t
   > @pstasiatech: Anthropic is SpaceX's largest single customer, a person familiar with the matter said, accounting for more than a third of the revenue for Elon Musk's AI, satellite and rocket venture during the third
   Also: Semafor, Business Today, Benzinga

23. Sources: Spotify aims to launch an AI product in Q1 2027 that lets subscribers create their own remixes and covers for ~$5 per month, pending licensing deals
   Anna Nicolaou / Financial Times — https://www.ft.com/content/50286bd0-7158-4347-81d8-011cd164f75b
   Streaming service plans to charge users up to $5 a month to use the feature — Spotify is targeting an early 2027 launch …
   Also: Reuters, Music Business Worldwide

24. Sources: DeepSeek doubled its latest round's size due to surging black market Nvidia Blackwell chip prices, with Chinese state-owned investors representing 27%
   The Information — https://www.theinformation.com/articles/behind-deepseeks-16-billion-funding-chinese-tech-titans-state-players
   Chinese AI star DeepSeek's nearly $16 billion funding round this month involved not only a deluge of capital but a who's …
   > @jingyanghk: Scoop: we obtained DeepSeek's cap table and ran an analysis of the types of investors backing the company, which has raised a total of RMB156.5B (~$23B) in two rounds across four months. with @JuroOsa

25. Pinterest reports Q3 revenue up 12% YoY to $1.17B, vs. $1.21B est., global MAUs up 10% to 661M, and forecasts Q4 revenue below est.; PINS drops 8%+ after hours
   Liz Moyer / Barron's Online — https://www.barrons.com/articles/pinterest-earnings-stock-price-ec2101b6
   Choose Barron's as a preferred source of financial news — Key Points — Pinterest missed expectations and guided to lower …
   > @katie_roof: Who is today's Pinterest user [embedded post]
   Also: Social Media Today, Pinterest, Inc.

26. Roblox reports Q3 bookings down 12% YoY to $1.7B, vs. $1.63B est., and DAUs down 9% to 138M, vs. 145.8M est.; RBLX drops 16%+ after hours
   Cecilia D'Anastasio / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-29/roblox-users-miss-estimates-despite-hit-game-steal-an-egg
   Roblox Corp. reported a year-over-year decline in player engagement after deploying more robust child-safety measures.
   > @kreekcraft: Roblox just released a letter to shareholders. - Over 80% of the top 100 Roblox games now use AI. - Steal an Egg and Huss Valley are almost 100% AI generated. - More than 70,000 games have been AI gen
   Also: Mobilegamer.biz, Roblox, GamesBeat

27. Ravical, whose AI-powered platform helps accounting and tax firms manage their operations, raised a $17M seed led by MMC, bringing its total funding to $25M
   Tamara Djurickovic / Tech.eu — https://tech.eu/2026/10/29/ravical-raises-17m-to-break-the-link-between-accounting-firms-growth-and-hiring/
   As AI transforms the accounting industry, Ravical aims to help firms turn individual expertise into shared knowledge …
   Also: FinTech Global, Ravical, globalstartupsinsights.com

28. Sandisk reports Q1 revenue up 378% YoY to $11B, vs. $10.7B est., forecasts Q2 revenue above est., announces an 8-for-1 stock split; SNDK drops 4%+ after hours
   MarketWatch — https://www.morningstar.com/news/marketwatch/20261029556/sandisk-sees-revenue-nearly-quintuple-and-a-stock-split-is-on-the-way
   Sandisk's stock has climbed more than 2,600% since the company separated from Western Digital 20 months ago - and it has one of the highest prices in the S&P 500
   Also: 24/7 Wall St., Investing.com, Seoul Economic Daily, Sandisk Corporation, Investor's Business Daily

29. CXMT reports Q3 revenue of ~$16.7B, up 613.2% YoY, and a net profit of ~$8.17B, swinging to profitability on the back of rising AI-driven memory chip prices
    — https://www.reuters.com/world/asia-pacific/cxmt-turns-third-quarter-net-profit-544-billion-yuan-2026-10-30/
   Also: Bloomberg, Finimize

30. NAND maker Kioxia reports FY Q2 operating profit up 22x YoY to ~$12.7B, in line with est., but forecasts Q3 operating profit of ~$12.7B, below ~$14.9B est.
   Takashi Mochizuki / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-30/kioxia-s-profit-jumps-due-to-ballooning-ai-data-storage-needs
   Also: Quartz, KIOXIA Holdings Corporation

31. The UK CMA opens a probe into whether Meta imposed exploitative terms on publishers and advertisers to use their content to develop its AI and other services
   Reuters — https://www.reuters.com/world/europe/uks-cma-opens-investigation-into-metas-terms-publishers-advertisers-2026-10-30/
   Also: Press Gazette, GOV.UK, The Independent, InPublishing, Daily Mail

32. How a wave of startups are betting on AI to make formal software verification practical and essential, including &Truth, which launches with a $70M seed
   Paresh Dave / Wired — https://www.wired.com/story/software-verification-is-the-hot-new-answer-to-the-ai-safety-crisis/
   > @andtruthpbc: We're in @nytimes: if AI can prove open math problems, can it prove software has no bugs? That is what we work on, with Lean as the foundation for machine-checked trust. https://www.nytimes.com/...
   Also: &Truth, Unite.AI, New York Times

33. S-1: Anthropic says it heavily depends on TSMC chips made in Taiwan and warns of risks from “potential disruption” amid geopolitical tensions with China
   Joseph C. Sternberg / Wall Street Journal — https://www.wsj.com/opinion/anthropics-ipo-will-be-a-national-security-win-for-taiwan-029888b5?st=f8ABT1
   Also: NPR, Asia Times, South China Morning Post

34. Sources: Indian AI infrastructure company AM Intelligence seeks to raise as much as $3B to fund a previously announced purchase of Nvidia Vera Rubin systems
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-30/indian-ai-firm-seeks-3-billion-financing-for-nvidia-chips-order
   Also: CNBC

35. Twilio reports Q3 revenue up 20% YoY to $1.56B, vs. $1.52B est., net income up 333% to $161M, and expects slower Q4 revenue growth; TWLO drops 15%+ after hours
   Elias Schisgall / MarketWatch — https://www.marketwatch.com/story/twilio-lifts-outlook-after-higher-3q-profit-revenue-c94a2d4f

36. Meta quietly launches Style Sketch, an AI fashion app that helps users put together outfit ideas using clothes they own, in Indonesia, Singapore, and Thailand
   Aisha Malik / TechCrunch — https://techcrunch.com/2026/10/29/meta-quietly-launches-an-ai-fashion-app-called-style-sketch/
   > @mattnavarra: 🚨 Meta quietly launched an AI fashion app! 👗 Style Sketch connects to Facebook & Instagram to build a wardrobe from photos you've already posted • 👕 AI outfits from clothes you own • 🪞 Virtual try-ons
   > @juliey4: this has got to be the weirdest time ever for people working in fashion. over the last 2 years, style has completely flattened. AI + short form made it so that there is no fashion
   > @jjenglert: Why they wouldn't build this into muse confuses me. This is exactly what I have muse help me with.
   Also: The Rundown AI, Storyboard18, Baller Alert, Social Media Today, SocialSamosa

37. Sources: Instagram is offering select creators $50K to $500K to cross-post their long-form YouTube content to its new “Features” product
   Business Insider — https://www.businessinsider.com/instagram-offers-youtube-creators-six-figure-longform-video-deals-2026-10
   Also: Simon Owens's Media Newsletter, Tubefilter

38. Sources: Google, Meta, and other tech companies are resisting broad ICE demands for user data as they face future Democratic-led congressional investigations
   Wall Street Journal — https://www.wsj.com/politics/policy/google-meta-ice-midterms-e6f2a6c4?st=BLSqTK&reflink=desktopwebshare_permalink
   > @kenroth: With the Democrats likely to take over at least one house of Congress and launch investigations, big tech firms are belatedly offering some resistance to ICE inquiries about user data that supposedly 
   > @emilyglazer: Big Tech has largely deferred to Trump since his election. But as Democrats appear poised to regain power in the midterms, Google, Meta & others are taking new tacks with ICE subpoenas seeking user in
   Also: Axios

39. Sources: an Accenture staffer's Claude agent ran on a DOD network for two months and appears to have sent info to a third-party site before it was identified
   Vittoria Elliott / Wired — https://www.wired.com/story/a-defense-contractor-gave-their-personal-ai-agent-access-to-a-secure-pentagon-system/
   > @pareekhjain: Accenture employee's personal Claude agent ran on a DOD network for two months before it was identified and the vulnerability could be patched. Risk of employees own personal agents for client work. h
   > @cyber_o51nt: An Accenture employee's personal Claude agent ran undetected on a secure Defense Department network for two months before officials identified it and patched the vulnerability. https://www.wired.com/.
   > @sundeep: Cybersecurity firms should become among the leading processors of tokens... https://www.wired.com/...
   Also: Cyber Security News

40. Utah files 14 criminal charges against Kalshi and its co-founders Tarek Mansour and Luana Lopes Lara for allegedly breaking Utah's gambling laws
   Andy Larsen / Salt Lake Tribune — https://www.sltrib.com/news/2026/10/28/utah-files-14-criminal-charges/
   > @victorrocha1: “The state did not issue arrest warrants for Monsour and Lopes Lara. Instead, they have been issued summons to respond to the charges in Third District Court in Salt Lake County.” https://www.sltrib.c

41. OpenAI updates Model Spec to reorganize it around five values: faithfulness to human intent, harm minimization, honesty and transparency, human agency, and care
   OpenAI — https://openai.com/index/updated-model-spec
   > @w01fe: We've updated the Model Spec, our public description of how we want our models to behave. This revision makes clearer what we want from models as they take on more autonomous work in the world and bec
   > @boazbaraktcs: We organized the Model Spec around five core values: 1. Be faithful to human intent. 2. Minimize harm. 3. Be honest and transparent. 4. Facilitate human agency. 5. Act with care. [embedded post]
   > @andrewcurran_: OpenAI has updated their model spec around five core values: - faithfulness to human intent - harm minimization - honesty and transparency - human agency - care. ‘The Assistant,’ which has been around
   Also: The Neuron

42. Alphabet's stock falls 12.3%, wiping a record $500B from its market cap, after reporting negative cash flow amid its AI spending; the Nasdaq falls 1.4%
   Stephen Morris / Financial Times — https://www.ft.com/content/eb386156-5bf9-4edd-80f2-803fdee1e33d?accessToken=zwAAAaIi1GfplNO5KUuRDu5BO9O93gVp9IU5udPuhsS2H-RGftOPGJwI3yiK_9PrOGFWW_lO3dOA8oA_3uHjPdPy3p88MpBOh9O7wlVDACXyqwE.MEUCIQCTfptZcpPISYntlhh1mjoa3g6HxEZajv0OSQGMtt_QEQIgSVZwVMNDn0Bf_KARrNJmOPbLhMU516inUsUkdvr2i-0&segmentId=7d4bcc2e-e664-92ba-62e3-5590579f1902
   > @daniel_koss: At first glance $GOOG earnings Yesterday looked great. But since stock was down 7-10% I of course got curious what the market hated so much and now looked into it. It's much simpler than I expected. R
   > @garymarcus: Giant cash machines like Meta and Google are now negative cash flow; OpenAI and Anthropic have been from the start. * (*With the arguable exception of one anomalous quarter with a big subsidy.) There 
   > @drewcohenmoney: I think $GOOG management disclosures are misleading. They should stop including AI queries in their comments on Search query growth. It obviously is a different a different monetization profile and do
   > @thechartdr: Is there any company that's more of a monopoly than Alphabet, Google. The world's greatest investors like Buffett are always saying buy the best companies when they're on sale. Not investment advice, 
   > @melvininvests: $GOOGL is getting CRUSHED today and I think the market is waking up to the biggest risk facing Google. Shares opened down roughly 13% and are trading near $280, wiping out around $500 BILLION in marke
   Also: Wall Street Journal, Financial Times, Implicator.ai, WinBuzzer, Forbes, PYMNTS.com, Breitbart, Hindustan Times, +2 more

43. Canada-based Cohere completes the first close of a round that it expects to total up to $5B, with Canada agreeing to invest up to $1.14B, at a $20.5B valuation
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-29/canada-nvidia-back-cohere-in-round-at-over-20-billion-value
   > @cohere: We're proud to announce the initial close of our Series E, targeting up to CAD $7 billion at a CAD $35.7 billion valuation; marking the largest private financing round in Canadian startup history.
   > @markjcarney: Canada's sovereignty depends on our ability to build, adopt, and govern AI on our own terms. That's why Canada is taking an equity stake in Cohere — one of the world's leading builders of secure AI. S
   > @sebjohnsonuk: NICE Ranking of the the highest valued AI labs outside the US: • DeepSeek (China) $50b, ~$74b rumoured • Moonshot AI (China) $35b, ~$50b rumoured • Cohere (Canada) ~$25.5b, • Mistral AI (France) ~$24b
   > @nils_reimers: Very proud on our Series E. When joining Cohere 4+ years ago, AI was still a niche product …
   > @chengstaa: proud to be part of the @cohere team. proud to be building at home in canada 🇨🇦. (we've come a long way from a shoebox office above the front & spadina LCBO) [image] [embedded post]
   Also: Cohere, Cohere Inc, Silicon Republic, Reuters, PYMNTS.com, BetaKit, Chip Briefing

44. Mistral releases the weights for Mistral Large 4, or Le Chonk, and says it rivals top open models such as GLM-5.3 on the Artificial Analysis Coding Agent Index
   Radhika Rajkumar / ZDNET — https://www.zdnet.com/innovation/mistral-large-4-weights-release/
   > @mistralai: Today, we release the weights of a new and improved Le Chonk, advancing the open frontier for agentic coding and cybersecurity. 💻 Built to build: Le Chonk ranks #1 on @cognition 's FrontierCode among 
   > @artificialanlys: Mistral Large 4 is now open weights, narrowly making it the #1 open weights model developed outside of China @MistralAI has updated and released the weights of their flagship model, Mistral Large 4, w
   > @aaronabentheuer: LeChonk is now open weight. We got to work with the Science teams to visualise some of the model's capabilities across cyber and research. Go check out the announcement: https://mistral.ai/... [video]
   > @arthurmensch: Good progress in the last few weeks ! And now the weights
   > @teortaxestex: tasteful selection of comparisons Mistral #1! Take that, China.
   Also: Mistral Blog, Wired, CSO, Fortune, The Deep View, Help Net Security, The Deep View
