# Research — News Cluster

Search for news **events that occurred** between **2026-10-30 10:00 BRT** and **2026-11-02 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-30 10:00 BRT to 2026-11-02 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-11-02
**Research window:** 2026-10-30 10:00 BRT → 2026-11-02 10:00 BRT

**Previous edition headlines (2026-10-30 — skip unless genuinely new development):**
- cohere-series-e-initial-close-canada-stake: Cohere closes first tranche of up to C$7B Series E at C$35.7B; Canada takes a stake
- mistral-large-4-le-chonk-open-weights: Mistral releases open weights of 1T-parameter Large 4 'Le Chonk', tops Western open models
- anthropic-is-spacex-customer-b-34-percent-revenue: Bloomberg: Anthropic is SpaceX's 'Customer B', 34.5% of Q3 revenue via compute rental
- crowdstrike-vapor-panda-artex-ai-agents-200-orgs: CrowdStrike: China-linked hackers used AI agents and DeepSeek to hit 200+ organizations in 11 days
- openai-model-spec-five-values-misalignment-monitoring: OpenAI rewrites Model Spec around five values and details its frontier misalignment monitors
- accenture-contractor-claude-agent-dod-network: Wired: Accenture contractor's personal Claude agent ran on a Pentagon network for two months
- uk-cma-probes-meta-terms-ai-content-publishers: UK CMA opens probe into Meta terms that would let it use publishers' content for AI
- intel-q3-weak-q4-guide-pc-slowdown-memory-crunch: Intel beats Q3 but guides Q4 below estimates on memory-driven PC slump; shares sink 20%+
- nvidia-talks-credit-guarantees-nscale-anthropic-data-center: Nvidia in talks to guarantee billions in debt for Nscale's 460MW Anthropic data center
- sandisk-11b-quarter-stock-split-kioxia-guide-miss: Sandisk revenue nearly quintuples to $11B with 8-for-1 split; Kioxia warns NAND price gains slowing
- cxmt-q3-net-profit-8-billion-revenue-613-percent: China's CXMT posts $8.2B Q3 profit as revenue jumps 613% on AI memory prices
- agility-robotics-spac-465m-foxconn-pipe-nasdaq-aglt: Agility Robotics SPAC to raise ~$465M with Foxconn-led PIPE, Nasdaq debut set for Nov 5
- am-intelligence-seeks-3b-debt-nvidia-vera-rubin: India's AM Intelligence seeks up to $3B in debt to pay for Nvidia Vera Rubin chips
- huang-defends-megaspeed-ties-china-denies-warren-demands-answers: Jensen Huang calls Megaspeed dealings 'normal' as China denies spy report and Warren demands answers
- binance-6-3b-hack-north-korea-tradertraitor: Binance loses ~$6.3B in largest crypto theft ever; TRM and Chainalysis blame North Korea
- hormuz-limpet-mine-tanker-trump-iran-war-wrapped-up-soon: Limpet mines hit tanker in Hormuz as Trump says Iran war will be 'wrapped up soon'
- ecb-holds-2-5-debated-hike-lagarde-early-exit: ECB holds at 2.5% after debating a hike; Lagarde to leave nine months early
- boj-holds-1-25-declares-2-percent-target-met: Bank of Japan holds at 1.25%, says inflation target met for the first time since 2013
- alphabet-record-500b-wipeout-worst-day-nasdaq: Alphabet loses record ~$500B in worst day ever on negative cash flow, dragging Nasdaq 1.4%
- hegseth-fires-lt-gen-sylvia-leak-criminal-referral: Pentagon refers fired Iran war planner Lt. Gen. Sylvia to DOJ over alleged leaks
- israel-final-count-netanyahu-bloc-loses-majority: Israel's final count: Netanyahu bloc wins 53 seats, loses majority; Arab parties take record 19

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 40 stories

1. Marvell agrees to acquire optical components maker Lumentum in a $115B all-stock deal, as it aims to rival Broadcom; Nvidia invested $2B in each company in 2026
   Anhata Rooprai / Reuters — https://www.reuters.com/legal/transactional/marvell-buy-lumentum-115-billion-deal-ai-data-center-bet-2026-11-02/
   Marvell Technology (MRVL.O) is buying optical components maker Lumentum (LITE.O) in a $115 billion all-stock deal, including debt …
   > @vikramskr: Marvell and Lumentum to combine. Here is a post thinking through the consequences: https://www.viksnewsletter.com/ ...
   > @patrickmoorhead: I've said @MarvellTech times and integrates its M&A well. The $115B all-stock deal for @Lumentum is the biggest test yet. $MRVL $LITE Inphi brought the DSPs, Celestial AI the photonic fabric, Lumentum
   > @mayazi: Nvidia's optics support is being bought by a company that builds the hyperscalers' (trainium) chips. But more importantly it gives Marvel an advantage over Broadcom. https://www.bloomberg.com/...
   > @benbajarin: Also the Marvell and Lumentum deal is telling on what's needed to compete with Broadcom.
   > @damnang2: Finally happened
   Also: The Information, Vik's Newsletter, Marvell Technology, Inc., Financial Times, Dow Jones Newswires, Wall Street Journal, Seeking Alpha, Yahoo Finance

2. Marvell's $115B Lumentum acquisition is one of the biggest tech deals ever and 2026's top M&A deal; Lumentum is up 128% YTD, giving it a ~$76B market cap
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-02/marvell-reaches-115-billion-deal-for-lumentum-holdings
   Marvell Technology Inc. has reached a deal to buy data center optics maker Lumentum Holdings Inc. at an enterprise value $115 billion …
   Also: Axios, Finimize, Wall Street Journal, Dow Jones Newswires, Quartz, 24/7 Wall St., Pulse 2.0

3. Supermarkets in Belgium, Ireland, Sweden, Finland, and Estonia report fridge and freezer temperature spikes due to suspected hacks, echoing attacks in France
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-02/belgian-swedish-supermarkets-report-new-suspected-freezer-hack
   Supermarkets across Europe were hit by suspected cyberattacks that resulted in sudden changes in the temperatures of their fridges …
   > @maxekaplan: The entire world is about to learn just how bad of an idea IoT was https://www.bbc.com/...
   > @richdecibels: if I were working in AI safety I might do some low consequence high drama hacks to shape the public narrative
   > @malwaretechblog: I'm super curious as to who is behind all these. The only threat actor I could think of who'd be motivated to just randomly break fridges across Europe is Russia. They've funded a lot of sabotage oper
   > @osint613: Cyberattacks overnight disrupted refrigeration systems at supermarkets in Sweden, Belgium and Luxembourg, causing extreme temperatures and heavy damage to stored food. Some ICA stores in Sweden had un
   > @warmonitor3: There has been a large cyber attack on Swedish supermarket chains which have turned of refrigerators of many stores leading to food rotting a similar cyber attack happened recently in France with sour
   Also: The Guardian, The Irish Times, Associated Press, BBC, Tom's Hardware, Silicon Republic, The Verge, Security Affairs, +5 more

4. SemiAnalysis launches GDPx, an AI frontier model benchmark measuring 11 domains, including chip design, cybersecurity, and RSI; Opus 5.5 tops with a 12% score
   SemiAnalysis — https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities
   A comprehensive benchmark spanning RSI, hardware design, cyber, bio, finance, legal, quant trading, chip design, software engineering, materials science, and alignment
   > @negligible_cap: It was insane to think Google would never be able to catch the frontier ever “Google will continue meandering on and releasing models, but their odds of reaching SOTA again have dropped to zero.” It's
   > @semianalysis_: GDPx covers the following domains. Each was a collaboration with at least one specialized data partner. SemiAnalysis was responsible for final QA and heavily involved with task iteration. (2/7)
   > @_josephwang_: Proud for @emulated_ai to be a science partner contributing to the frontier of materials science! With most of my career being in software, part of me has always wanted to go back to physical sciences
   > @semianalysis_: It's worth emphasizing that certain models like Opus 5.5 and GPT-6 Astra have sandbagged overall scores due to their safety classifiers. If we exclude cyber, biology, and alignment—the three domains w
   > @aisignaldrift: @sundarpichai It's laughable that Google is relying on fringe sites to prove its worth. That's what happens when you hire Freeloaders as CEO.

5. YC details multi-agent tests in games like Minecraft, where agents exhibit emergent capabilities, forming roles, hierarchies, and complex coordination patterns
   YC Labs — https://labs.ycombinator.com/projects/games/index.html
   > @ycombinator: Then, we shifted to Mindustry, a factory-building game (like Factorio) with military strategy. We placed 50 GPT-6.1 Sols against 50 Claude Opus 5.5s in PvP mode for 7 consecutive matches that lasted ~
   > @ycombinator: In collaboration with @olam_labs, we ran a series of experiments letting agent swarms compete in Minecraft and Mindustry. We wanted to see what kinds of agent dynamics would emerge when they shared a 
   > @ycombinator: As the Mindustry matches progressed, the language that the GPTs used only continued to get compressed. They would invent their own words and string many phrases together. We did not see specialized la
   > @ycombinator: Next, we ran nine 45-minute games of Bed Wars, a Minecraft game format where teams fight to destroy each other's beds while protecting their own. We pitted 10 Claude Opus 5.5 agents against 10 GPT 6.1
   > @ycombinator: Claudes generally established democracies, GPTs formed hives. In our seven match run, GPTs split factory ownership from the start and were very willing to supply resources towards shared goals. They a
   Also: Tom's Hardware

6. Binance says net outflows were ~$3.64B, or 2.1% of assets, in the 9.5 hours after it began restoring withdrawals; DefiLlama puts 24-hour net outflows at $4.05B
   Zack Abrams / The Block — https://www.theblock.co/news/business/2026-11-01-binance-sees-3-64-billion-in-net-outflows-after-reopening-withdrawals-following-record-hack-432259
   The exchange said the outflows equal 2.1% of its assets and that withdrawal volumes have eased after an initial spike.
   > @binance: Binance began restoring withdrawals in phases at 06:00 UTC on November 1, 2026. By 12:36 UTC, withdrawals had resumed for all 15 networks and assets in the initial phase. After an initial spike, withd
   > @cz_binance: Blockchain data is transparent.
   > @njcallocates: Over $1B deposited into Binance in the first 9.5 hours after withdrawals reopened. Just days after a $6.3B hack. I really didn't expect that. [embedded post]
   > @sunshinebinance: Thank you for your patience and continued support. [embedded post]
   > @venusprotocol: We stand with Binance and deeply respect the team working tirelessly in managing this security incident. Seeing the efforts of the team and community alike reminds us why we build in this ecosystem. V
   Also: CoinDesk, Unchained, Bloomberg, CNBC, Silicon Republic, Bitcoin Insider, The Guardian, RTÉ, +19 more

7. A look at Binance's efforts to contain the hack, including creating a global war room of ~100 people and coordinating with other crypto companies and the FBI
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-31/rogue-code-2-test-runs-and-no-sleep-inside-the-binance-hack
   > @aaalex: Binance paying Bloomberg for sympathy points lmao Truly just pathetic behavior from everyone involved
   > @zectrillionaire: We don't give a fuck. Did I impregnate her? Stop trying to portray her doing her job as some extraordinary act of heroism. She's the co-CEO of Binance. Handling a crisis at the company she runs is lit
   > @ellazhang516: True, she's a warrior. When she stayed with me in SF pregnant with her first baby, I worried she never slept. She had 3 phones around her and taking care of (then) Binance baby. So I'm not surprised t
   > @edward_yu_var: > logged off work and was scrolling through X before going to bed around 12:30 a.m. Ah I see we all have the same schedule
   > @bdanweiss: such a fun kicker in the breakdown we just pubbed on the race to respond to the binance hack, h/t @olgakharif:
   Also: Fortune, Information Age, Business Insider, Tech Times, CoinDesk, CTech, BleepingComputer, Telegraph, +8 more

8. The FBI attributes the $6.3B Binance hack to North Korea's elite hacking unit TraderTraitor, which the agency has also blamed for the $1.5B Bybit hack in 2025
   Kevin Whitelaw / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-31/fbi-blames-north-korea-for-6-billion-binance-crypto-hack
   > @cz_binance: 12 hours after withdrawals resumed: 2.1% net outflow, with most occurring in the first couple of hours. Over $1 billion in flow, too. 98% choose to stay! Trust isn't earned by what you say in good tim
   > @_richardteng: We know how important trust is, especially in moments like this. We've now replenished 90% of the stolen assets, and we're committed to covering the remaining 10%. Our users will not bear the financia
   > @binance: We sincerely thank @FBICyberBranch for their strong support during this challenging time.
   > @rapidresponse47: .@POTUS on the Binance hack: “We're learning about it. We don't know if it's North Korea — but if it is, we'll talk to North Korea about it.”
   > @hrkrshnn: ...There's interest in bringing back ‘letters of marque and reprisal’ to counteract the cybercrime that North Korea is committing... The problem is that in a modern context, issuing this against a nat
   Also: Decrypt, FBI, Help Net Security, Unchained, 24/7 Wall St., Infosecurity, Bitcoin News, Yahoo Finance, +36 more

9. Binance starts resuming withdrawals in phases, including for bitcoin and ether, after covering 95% of the $6.3B in tokens stolen in the hack by TraderTraitor
   Reuters — https://www.reuters.com/legal/government/binance-resume-withdrawals-after-recovering-bulk-6-billion-stolen-funds-2026-11-01/
   > @binance: Security Incident | Recovery Update #4: Withdrawals Resume in Phases (2026-11-01)
   > @binance: Security Incident | Update #3: 90% of Stolen Assets Replenished; Proof of Reserves Snapshot Provided
   > @binance: Update: First batch network now opened in phase one of withdrawals is $BTC bitcoin network
   > @binance: Withdrawal Update Withdrawals have now been restored for the following assets and networks: - Ethereum Network: USDC, USDT, ETH - BNB Smart Chain (BSC): USDC, USDT, BNB We will continue to restore add
   > @binance: As part of our ongoing security response, we have updated our list of Proof of Reserves addresses to include newly generated wallet addresses. Going forward, all withdrawals will be processed from the
   Also: Decrypt, RTÉ, Feld Thoughts, The Cyber Express, Euronews, Ynetnews, The Record, Times of India, +14 more

10. A profile of UCLA professor Terence Tao, who was once enthusiastic about AI's role in math but now warns of AI destroying the field's deliberative process
   Rivka Galchen / New Yorker — https://www.newyorker.com/magazine/2026/11/09/the-year-math-changed-forever?currentPage=all
   A.I. is solving problems that stumped the field for decades. Mathematicians look to Terence Tao for guidance on their altered world.
   > @fanofaliens: it's really over for mathematicians terence tao, the world's most famous mathematician is warning that AI is moving too fast for math to keep up: “we have to slow down. it's insane, the pace.
   > @hesamation: Published on Terence Tao's blog: Mathematics has changed. Let's act like it. this is a guest post by Frank Calegari, saying mathematicians need to stop treating AI as existential threat and start reth
   > @ml4trading: Well written, nuanced view on mathematics in the new age of AI - what may be gained, what may be lost, and how little we know how it will all play out https://www.newyorker.com/...
   > @sampearton: Thanks to the @NewYorker on featuring @SAIRfoundation and ongoing discourse around alignment for Math 2.0 featuring Terence Tao
   > @stevenstrogatz: This article by Rivka Galchen is beautiful. The story about @JohnCUrschel's work with his postdoc Rikhav Shah (& an AI assist) is especially interesting. (You can find non-paywalled versions if you po
   Also: What's new

11. Elon Musk says the cost of serving Grok Bot was “unsustainably high relative to revenue”, following subscriber complaints regarding rapid usage limit depletion
   Siladitya Ray / Forbes — https://www.forbes.com/sites/siladityaray/2026/11/02/musk-says-grok-bots-costs-were-unsustainably-high-weeks-after-touting-rapid-growth/
   Topline — Elon Musk acknowledged on Sunday that the cost of running SpaceX's AI agent Grok Bot was “unsustainably high” …
   > @elonmusk: @DogecoinNorway The cost of serving Grok Bot was unsustainably high relative to revenue
   > @dogecoinnorway: Any chance for a Grok Bot reset, @elonmusk? Lots of people say their usage ran out really fast this week.
   > @jason: This is an extremely bullish sign that people are getting value from their bots For $5k a year you can have two or three competent mid-tier employees... I think grok bots represent $30 an hour employe
   > @benjamindekr: Two weeks ago Grok Bot was an incredible success story powering SpaceXai's revenue growth Now it's unsustainable and loses money (???) [image] [embedded post]
   > @optionscjp: Elon musk just pulled the plug on Grok bot usage.. [embedded post]
   Also: Business Insider, Telegraph, IGN, The Independent, Moneycontrol, RuntimeWire

12. Sources: SpaceX is in talks with EchoStar to acquire Boost Mobile or access its network, after Verizon, T-Mobile, and AT&T rebuffed requests for network access
   Washington Post — https://www.washingtonpost.com/technology/2026/11/02/inside-elon-musks-plan-upend-wireless-phone-industry/
   Elon Musk approached the heads of America's top telecom companies in recent months with a request that would help him fulfill a years-long dream.
   > @tmfassociates: I'm not sure why this is pitched as SpaceX buying Boost, which the MNOs would try to veto. Clearly SpaceX wants the underlying DISH Wireless network. My assumption is that Boost is spunoff to CONX, un
   Also: Investor's Business Daily, Wccftech, Barron's Online, New York Times, Reuters, Telecompaper

13. OpenAI plans a post-midterms policy and PR blitz, pushing mandatory “speed limits” for powerful AI and rebranding its data centers as “AI compute campuses”
   Axios — https://www.axios.com/2026/11/01/scoop-openai-post-midterm-policy
   Right after Tuesday's midterms, OpenAI will unleash a policy and PR blitz to try to get in sync with the new Washington …
   > @kimmonismus: Artificial Intelligence (AI) is now Superintelligence (SI) and Data Centers are now “AI compute campuses”, as OpenAI wants to call them now. Via Agios.
   > @rohanpaul_ai: axios: OpenAI will start calling its data centers “AI compute campuses
   > @andrewcurran_: OpenAI is preparing for a post midterms change in the weather. Axios:
   > @sc_cath: Not the right alignment problem to solve
   > @mikenellis: I mean, kudos to whatever PR hack got paid $100,000 by OpenAI to come up with “AI compute campuses” That shit ain't gonna work
   Also: Business Insider, Politico, The Rundown AI, TechCrunch, The Decoder, Gizmodo, Implicator.ai

14. Ukraine says its air raid alert app was compromised late Sunday, sending false warnings of “nuclear danger”; Russia confirms a similar hack of its alerts app
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-02/ukraine-and-russia-report-cyberattacks-on-emergency-alert-apps
   Ukraine and Russia said they faced cyberattacks on emergency and air raid alert systems.
   > @hissgoescobra: Horrifying. Just awful.
   > @faytuksnetwork: BREAKING: Ukraine's civil defense air alert system has been compromised in a major cyberattack, triggering physical sirens and sending false emergency notifications across multiple regions, per Falcon
   > @treyyingst: NEW: Ukraine's air raid alert system was hacked, sending warnings of chemical and radiation threats to phones across the country. The loudspeaker alert system was also compromised, blaring a similar m
   > @maria_drutska: TWO CAN PLAY THIS GAME After a cyberattack on Ukraine's Air Alert app last night, unknown hackers struck back, targeting Russia's Ministry of Emergency Situations system. ☢️ Russians received an alert
   > @euan_macdonald: Russian cyberattack. They gave themselves away by triggering two very unlikely alerts that had never been issued before within a couple of minutes. Fucking fascist eejits.
   Also: Security Affairs, BBC, Implicator.ai, Associated Press, NBC News, Al Jazeera, KRDO, Reuters, +11 more

15. Investigation: a network of 400+ domains and apps linked to Chinese-language developers bypasses app store reviews to generate nonconsensual deepfakes and CSAM
   Matt Burgess / Wired — https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/
   WIRED uncovered some 400 apps and websites linked to Chinese-language developers that look like regular AI tools but had secret features …
   Also: 9to5Mac

16. Data analytics provider Hex Technologies, which says it has rebuilt its platform for AI agents, raised a $100M Series D led by Peak XV at a $1.2B valuation
   Tim Keary / Forbes — https://www.forbes.com/sites/timkeary/2026/10/27/hex-threw-out-its-code-to-stop-the-saaspocalypse-raising-100-million/
   This voice experience is generated by AI. Learn more. … The SaaSpocalypse has become one of the most controversial topics in enterprise tech.
   > @kellblog: Hex raised, by my math, about $50 per line of deleted code. There's an AI transformation angle. Announcing our $100M raise https://hex.tech/... [image]
   Also: Hex

17. Hirundo, Lazarus, and others are applying machine unlearning and weight edits to Chinese models to remove censorship and harden security for Western companies
   Rest of World — https://restofworld.org/2026/western-startups-realigning-chinese-ai-models/
   A growing number of startups are editing powerful Chinese open-weight models for Western businesses that are concerned about censorship and security.

18. British physicist and materials scientist Cyril Hilsum, widely recognized as “the father of liquid crystals” for enabling flat-panel display tech, died at 101
   Michael S. Rosenwald / New York Times — https://www.nytimes.com/2026/11/01/technology/cyril-hilsum-dead.html?unlocked_article_code=1.NFE.gD-P.2F70K4AuzFTo&smid=url-share
   The man who helped develop the technology for liquid crystal displays — the screens in flat-panel televisions and laptops — has died at 101.
   > @alistairburtuk: A brilliant man, being appropriately and rightly recognised.
   > @mikerosenwald: If you're watching football on a flat screen, thank this guy. https://www.nytimes.com/...
   > @peterbale: @lindseyhilsum @nytimes A great man. Beautifully honoured. I recall in late '80s an item on the Defence Dept accounts, royalties for LCDs. I imagine now in Qinetiq. I also recall my Dad buying an earl
   > @lindseyhilsum: A lovely obituary of my father in @nytimes : That Giant HDTV That Fits in Your Living Room? Thank Cyril Hilsum. https://www.nytimes.com/... via @NYTimes

19. Filing: Anthropic plans to raise up to $3.5B from Japanese investors as part of its IPO, joining Australia, Canada, and parts of Europe in having direct access
   Yasutaka Tamura / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-02/anthropic-seeks-up-to-3-5-billion-in-japan-for-its-mega-us-ipo
   Anthropic PBC aims to raise up to $3.5 billion from Japanese investors in its initial public offering in the US …
   > @edzitron: Every bank in this list has at some point given money to OpenAI or CoreWeave, trying to lock $3.5bn of Japanese investors' money in volatile Anthropic stock with a junk rating for a market already hig
   > @rinnishimura: Anthropic announced today that it plans to raise up to $3.5 billion (approx. ¥552.8 billion) in Japan through an IPO. It exceeds the amount raised by SpaceX, which went public in June, by 60% and woul
   > @choblin29: 🚨BREAKING: Anthropic plans to sell up to $3.5 billion in new shares to Japanese investors through its US IPO, a filing released today shows, Reuters reports. If fully sold, that would be 59% more than
   > @puckrin: Anthropic is taking its IPO on a world tour. Up to $3.5B from Japanese investors, with Australia, Canada & parts of Europe also on the itinerary. Exit liquidity, now available in every timezone.
   Also: Reuters, CoinGape, Political.org, Tech in Asia

20. Letter: the White House argues it doesn't have to share the full draft of its voluntary AI testing framework, citing national security and commercial exemptions
   Leo Schwartz / The Information — https://www.theinformation.com/briefings/trump-administration-refuses-release-information-ai-testing-framework
   The Trump administration declined to produce key documents related to its voluntary AI testing framework …

21. A look at AI safety debates and the rising popularity of “Stop Unilaterally + Raise Awareness”, or SURA; safety-focused AI labs shouldn't abandon the AI race
   Scott Alexander / LessWrong — https://www.lesswrong.com/posts/xikGZ8fuhdG6DApAo/against-sura
   The AI Futures Project[1] distinguishes several different plans for navigating the AI transition, which I'll lump into two broader categories:
   > @repligate: um, yeah, this is perhaps the main reason why the entire ai safety community has become way less interesting to me over the last few years it's like everyone decided that solving alignment is doomed a
   > @charliebull0ck: I agree with a lot of the points raised in this post. Not enough people take the point about what a unilateral U.S. pause would do to china negotiation dynamics seriously; I'm glad that Alexander does
   > @jessi_cata: Scott Alexander: “I... made fun of our misinformed opponents, who insisted that if we unilaterally paused AI then China would win. But actually, I said, nobody wants to unilaterally pause AI; this is 
   > @sashagusevposts: The use of superforecasters in the AI debates is fascinating. This post relies heavily on the predictions from five working at an AI safety think tank. A prior post ( https://www.astralcodexten.com/ .
   > @ryan_kidd44: If you read any blog post on AI safety from this year, make it be this one https://www.lesswrong.com/...
   Also: Security Affairs

22. How SF's AI boom is reshaping dating: founders treat first dates as interviews, use tech terms like “conversion rate” to track dates, and pay coaches $5K/month
   Emmy Martin / New York Times — https://www.nytimes.com/2026/10/31/technology/san-francisco-ai-boom-dating.html?unlocked_article_code=1.NFE.wr2v.F_Wy3TSgmnjB&smid=url-share
   San Francisco's A.I. boom has drawn a wave of young ambitious people who are now reshaping the city's dating life.Kelsey McClellan for The New York Times
   > @emmymrtin: They can raise millions. A second date is harder. My story on dating in San Francisco's A.I. boom: https://www.nytimes.com/...
   Also: Gizmodo

23. Analysis: Elon Musk contributed a record $474M to political groups for the 2026 midterms, including $216M to America PAC, the highest non-candidate spend ever
   Theodore Schleifer / New York Times — https://www.nytimes.com/2026/11/02/us/politics/elon-musk-midterm-spending.html
   Never before has a single ultrawealthy person who was not running for office spent this much during a single election cycle.
   > @teddyschleifer: NEW — Elon Musk's bill for the midterms? $474 million. Inside the numbers, the most anyone has ever spent on an election in which they were not running. https://www.nytimes.com/...

24. Fan fiction site AO3 says it could take two to four weeks to restore service after a security incident; AO3 hosts 18M+ works and has 11M+ registered users
   Bruce Gil / Gizmodo — https://gizmodo.com/popular-fan-fiction-site-ao3-could-be-offline-for-a-month-following-security-incident-2000833091
   “Black October” comes for the fan fic. — The popular fan fiction website Archive of Our Own (AO3) went offline Thursday, and its millions of users are freaking out.
   Also: 404 Media, The Verge, Engadget, New York Times, Dexerto

25. NAND maker Kioxia's shares fell up to 15% on Monday after its cautious Q3 outlook disappointed investors, raising concerns that AI-driven growth may be slowing
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-02/kioxia-shares-tumble-after-outlook-suggests-demand-leveling-off
   Also: The Elec, blocksandfiles, Tech in Asia, DigiTimes

26. Bites, whose AI tools deliver personalized training to frontline workers via WhatsApp, SMS, Slack, and other channels, raised a $40M Series A led by PeakSpan
   Meir Orbach / CTech — https://www.calcalistech.com/ctechnews/article/s1t5soetmx
   Also: Bites Training Platform …

27. The Hague-based Braid, whose API lets companies sell eSIM mobile plans under their own brand via 600+ carriers, raised a ~$38M Series A led by Octopus Ventures
   Rahul Raj / EU-Startups — https://www.eu-startups.com/2026/10/profitable-dutch-startup-braid-raises-e34-12-to-help-brands-launch-their-own-mobile-connectivity/

28. Casap, whose AI tools automate dispute and anti-fraud operations for banks, raised a $56M Series B led by Base10 Partners, bringing its total funding to $90M
   Jeff John Roberts / Fortune — https://fortune.com/2026/10/28/dd/
   > @jackchan_xyz: @Techmeme @jeffjohnroberts Strong round!
   Also: Pulse 2.0

29. South Korean President Lee Jae Myung vows to dedicate ~$16B for AI, chips, physical AI, and data centers in the country's 2027 budget, ~2x the 2026 allocation
   Reuters — https://www.reuters.com/world/asia-pacific/south-koreas-lee-vows-make-bold-ai-investment-record-budget-push-2026-11-02/
   Also: CNBC, The Korea Times, The Asia Business Daily, Hürriyet Daily News, Reuters

30. AI-powered medical search engine Vera Health, which says it is used by 800,000+ clinicians in 190 countries, raised a $28.5M Series A led by Threshold Ventures
   Cailey Gleeson / Fierce Healthcare — https://www.fiercehealthcare.com/finance/vera-health-secures-285m-series-ai-driven-clinical-search-engine
   Also: Pulse 2.0

31. Midstream Health, whose AI tools help 250 hospitals recover revenue from rebates and vendor and payer underpayments, raised a $20M Series A led by Valtrius
   Will Maddox / Axios — https://www.axios.com/pro/health-tech-deals/2026/10/29/midstream-health-20m-revenue-recovery
   Also: MedCity News, Inc.com

32. Broccoli AI, which sells AI agents to plumbing, HVAC, and electrical companies, raised a $22M Series A and a $30M Series B; a source says it is valued at $300M
   Nick Lichtenberg / Fortune — https://fortune.com/2026/10/28/broccoli-ai-funding-khosla-ventures-marcelle-flowers-plumbing-gen-z-founders/
   > @call_broccoli: Broccoli has raised our Series A and Series B, both led by @khoslaventures with @ycombinator Home services deserves tech that works as hard as its people. We're just getting started 🥦🥦🥦 https://fortun

33. Hyperbolic, which lets companies rent AI compute across ~30 neoclouds, raised a $30M Series A-1 led by Lip-Bu Tan's Walden Catalyst; it has raised $50M to date
   Geoff Weiss / Business Insider — https://www.businessinsider.com/intel-ceo-backs-30-million-round-ai-cloud-startup-hyperbolic-2026-10
   > @ojrenick: Wow, GPU futures race now really heating up. Hyperbolic just raised another $30M to $50M > https://www.businessinsider.com/ ... [embedded post]

34. How IShowSpeed became YouTube's top livestreamer with 62M+ subscribers, as his 24/7 “IRL streams” that last days mingle childlike wonder with teenage mischief
   Jon Caramanica / New York Times — https://www.nytimes.com/2026/10/29/magazine/ishowspeed-america-tour-livestream.html?unlocked_article_code=1.MVE.2S6N.BZdzqpeTtD8j&smid=url-share
   > @willystaley: In this week's Magazine: @joncaramanica hits the road with IShowSpeed, the livestreamer who revolutionized the stale format by bringing it out into the real world. https://www.nytimes.com/...
   > @ricoripoly: we worked on this new york times profile for nearly two years, gang. enjoy: https://www.nytimes.com/...
   > @devahaz: Speed has the coolest life which also sounds like absolute hell to me https://www.nytimes.com/...
   > @mattzeitlin: reading this literally made me feel ill (because it accurately captures a phenomenon i find very disturbing and bad) https://www.nytimes.com/...
   > @updatesfromyt: W's in the chat and IRL for @ishowspeedsui. This @nytimes profile brilliantly captures how a 21-year-old YouTuber is completely rewriting the rules of entertainment by turning the entire planet into h
   Also: What's on Netflix

35. Saudi Aramco acquires a 49% stake in AI startup Humain, contributing ~$2.6B in cash in 2026 plus AI, compute, and digital assets; Saudi Arabia's PIF retains 51%
   Dean Takahashi / GamesBeat — https://gamesbeat.com/saudi-arabias-aramco-buy-49-stake-in-ai-firm-humain-for-2-6b/
   > @caseynewton: As part of the deal, they're changing the name to Humain Rights Violation [embedded post]
   Also: Saudi Aramco, The Decoder, Wamda, RuntimeWire, Unite.AI, Forbes Middle East, Arab News, Daily Sabah

36. How “get-paid-to” apps like Freecash, briefly a top five App Store app in September, pay users small sums to play games and help publishers find big spenders
   John Herrman / New York Magazine — https://nymag.com/intelligencer/article/down-and-out-in-the-app-store.html

37. ServiceNow confirms it acquired Israeli startup Sweep to speed up customers' migrations to its CRM, for an undisclosed price estimated at hundreds of millions
   Allon Sinai / CTech — https://www.calcalistech.com/ctechnews/article/yxdvdp8sm

38. Analysis: candidates backing a data center moratorium could win up to 15 of 36 US governors' races on Tuesday, including in Texas, Ohio, Michigan, and New York
   Shane Burke / The Information — https://www.theinformation.com/articles/candidates-backing-data-center-pauses-win-15-governors-races
   Also: The Neuron, Bisnow, Seoul Economic Daily, The Real Deal, Wired

39. A look at VC-backed glossy magazine Colossus, whose glowing profiles of Zuckerberg and other tech titans win industry praise, while Kara Swisher says it is PR
   Andrew Fedorov / The San Francisco Standard — https://sfstandard.com/2026/10/30/colossus-glossy-quarterly-silicon-valley/
   > @mediaevan: Every few months the valley reinvents content marketing. https://sfstandard.com/...
   > @hitsamty: “This kind of wet kiss has always existed, but it was never done this artfully. Think of it as high-grade, tier-one content marketing.” - I am quoted in this dive into the magazine that is Silicon Val
   > @jonsteinberg31: On Colossus magazine, which publishes gorgeous, obsequious profiles of people like Zuck and Josh Kushner: “It's all well and good for the tech industry media bubble to have its own in-flight magazine,
   > @arashmassoudi: In-flight magazine quote still has me chuckling a day later @hitsamty
   > @andrewfed: Wrote about Colossus Magazine's lush and toothless profiles of the tech and investing elite for @sfstandard “These people are so fragile and made of papier-mâché that they need Vaseline mirrors to ref

40. Google's data center energy head says space data centers cost up to 100x more than Earth-based ones, and US power supply is sufficient but permits are slow
   Amir Efrati / The Information — https://www.theinformation.com/articles/google-energy-chief-space-data-centers-cost-100-times-earth
   > @smdcapital: @Techmeme @amir one of them is gonna be extremely wrong
   > @amir: @Walter65852293 @Techmeme google's analysis incorporates spacex launch costs and hauling capacity
   > @ramez: Pretty consistent with other modeling. Launch costs need to drop to $100-200 / kg to make space data centers economically competitive. Starship is built to reach those costs and lower, if it can achie
   > @realjimchanos: So $5T per GW...?! The fact that the head of data center energy at a hyperscaler is this far off from estimates from $SPCX management/bulls should give pause to anyone trying to model this business ou
   > @mikaelxeeland: @Techmeme @amir Slow permits being the bottleneck is exactly why sites that are already permitted and energized carry a premium right now. Time to power is worth more than the MW number on a slide.
   Also: Fortune, Wall Street Journal, Free Press Journal, The Deep View
