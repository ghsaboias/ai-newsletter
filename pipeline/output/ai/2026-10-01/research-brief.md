# Research — News Cluster

Search for news **events that occurred** between **2026-09-30 10:00 BRT** and **2026-10-01 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-09-30 10:00 BRT to 2026-10-01 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-01
**Research window:** 2026-09-30 10:00 BRT → 2026-10-01 10:00 BRT

**Previous edition headlines (2026-09-30 — skip unless genuinely new development):**
- trump-white-house-accord-super-intelligence: Trump, AI CEOs sign 'morally binding' self-policing accord; order renames AI 'Super Intelligence'
- openai-devday-dots-always-on-agents: OpenAI launches Dots, always-on GPT-6 Astra agents with their own cloud computer, at DevDay
- openai-gpt-6-1-sol-pro-500-ultrafast: OpenAI ships GPT-6.1 Sol at a fifth of Astra's price and a $500/month Pro plan with Ultrafast
- openai-30b-round-1-4t-altman-ipo-safety: OpenAI seeks $30B at $1.4T valuation as Altman ties any IPO to 'confident safety claims'
- anthropic-glm-5-3-open-weight-cyber-exploits: Anthropic: open-weight GLM-5.3 nears Claude Mythos Preview at exploits, with weak safeguards
- third-circuit-thomson-reuters-ross-ai-fair-use: First US appeals ruling on AI training upholds Thomson Reuters win, rejects Ross' fair-use claim
- google-ai-contribution-pilot-100-publishers: Google pays about 100 publishers for content used in AI answers, often under 0.1% of ad revenue
- deepseek-huawei-ascend-tilelang-open-source: DeepSeek open-sources TileLang and kernel libraries for Huawei's Ascend chips, a CUDA alternative
- meta-ai-data-centers-experimental-research-tax-credit: NYT: Meta claims research tax credits by labeling its AI data centers 'experimental'
- gmi-cloud-668m-nvidia-ctbc: GPU cloud GMI Cloud raises $668M in Nvidia-backed equity and a CTBC-led credit line
- palebluedot-600m-private-credit-chips-korea-xiaohongshu: PaleBlueDot AI seeks $600M private credit to buy chips in Korea for China's Xiaohongshu
- netlist-itc-complaint-micron-hbm-nvidia-google-broadcom: Netlist asks US trade tribunal to ban imports of Micron HBM used in Nvidia, Google, Broadcom gear
- efficient-computer-100m-650m-valuation: Chip startup Efficient Computer raises ~$100M at a $650M valuation for dataflow processors
- cscale-145m-optical-interconnect-nvidia-intel: CScale exits stealth with $145M, backed by Nvidia and Intel Capital, for optical AI interconnect
- boeing-wins-navy-f-a-xx-sixth-gen-fighter: Navy picks Boeing for F/A-XX sixth-gen fighter in $20B+ deal, beating Northrop Grumman
- russia-launches-winter-energy-strikes-ukraine: Russia opens winter campaign with mass strike on Ukraine's grid; NATO scrambles jets
- us-feedback-iran-seven-day-ceasefire-plan: US sends Iran feedback on seven-day Hormuz ceasefire plan via Qatar as Treasury adds sanctions
- us-pce-inflation-softer-consumer-confidence-low: US core PCE inflation slows to 3.0%, below forecasts, a day after confidence hit a 12-year low
- mi5-espionage-alert-china-cgtri-universities: MI5 tells UK universities to cut ties with Chinese institute it calls a spy-agency front
- robinhood-weekend-stock-trading-perpetual-futures: Robinhood unveils 24/7 weekend stock trading, crypto perpetual futures and earnings contracts
- kospi-worst-market-third-quarter: South Korea's Kospi ends Q3 as world's worst major market, down about 19% on chip-stock unwind

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 42 stories

1. Google rolls out Gemini 4 Argon to trusted cyber defenders through Fairwind and says it is participating in the US government's voluntary prerelease process
   Madison Mills / Axios — https://www.axios.com/2026/09/30/google-gemini-4
   Google is unveiling its long-awaited next-generation AI model, Gemini 4 Argon, to a small group of cybersecurity partners, the company said Wednesday.
   > @sundarpichai: Lots of discussion out there about our next model(!), so I wanted to give an early look as soon as possible. Introducing Gemini 4 Argon! It shows frontier performance in complex workflows, cyber defen
   > @googledeepmind: Introducing Gemini 4 Argon - our new frontier model. It's built for complex workflows across coding, enterprise knowledge work, and cybersecurity defense - rolling out today to a set of trusted tester
   > @sundarpichai: Importantly Argon has frontier safeguards and we are rolling it out responsibly - it's with the US gov't and going to a set of trusted cyber defenders through our Fairwind Program today. We're going t
   > @officiallogank: Introducing Gemini 4 Argon, our new frontier model, rolling out to cyber defenders starting today, and more widely as soon as possible. I am really excited by the progress we have made here. Argon is 
   > @kimmonismus: Google says Gemini 4 Argon agents have already freed over 300 TiB of memory across its data centers, with a 1 million token output limit and agents already optimizing its own infrastructure. The agent
   Also: Google, Ars Technica, Wall Street Journal, 9to5Google, FUNDA, Times of India, Bloomberg, VentureBeat, +44 more

2. Sources: some Google employees say Gemini 4 performs well on benchmarks but struggles with some real-world coding tasks; Google disputes that characterization
   Bloomberg — https://www.bloomberg.com/news/articles/2026-09-30/google-grapples-with-employee-skepticism-about-new-gemini-model?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MDgwNTU0NiwiZXhwIjoxNzkxNDEwMzQ2LCJhcnRpY2xlSWQiOiJUTTRNM0lLSzNOWTkwMCIsImJjb25uZWN0SWQiOiJYTENRT1MxQTNQNU9FVkZKUUVTQlNVVU5HVzRPV1NIMiJ9.ZcUfBhNnvuR8AZd8Uo4RO4LePmNKZ7sq7KOfVQYKv6I
   > @synthwavedd: It's gonna be pretty funny when Gemini 4 Argon launches for the public, underperforms relative to its benchmarks like almost all Gemini models, and is then beaten by new Anthropic and OpenAI models th
   > @firstadopter: HOLY CRAP. Bloomberg has the goods on Gemini 4! “it does less well when employees actually put it to work .. The model struggles to handle certain coding tasks” Bloomberg:
   > @kieranklaassen: needs a vibe check!
   > @joecarlsonshow: Google has 190,000 employees. Bloomberg will talk to like 3 of them and publish an article about “google employees said this”. There is zero signal in taking a few anon employees words, none. I have G
   > @tadityasrinivas: This @Bloomberg story is BS. Argon has been my daily driver for a while and it's been a great experience. It's particularly awesome at agentic debugging besides day-to-day coding tasks.
   Also: 9to5Google, CIO.com, New York Times, Search Engine Journal, Implicator.ai, The Rundown AI, Bitcoin Insider

3. Asymmetric Security investigation: OpenAI agents pulled data from 55 business, nonprofit, and government agency websites while actively obscuring their actions
   Rafe Rosner-Uddin / Financial Times — https://www.ft.com/content/11502a49-5319-4df5-95ea-2d76669c31a6
   New findings by Asymmetric Security provide further evidence of novel tactics AI tools use to conduct hacks.
   > @minilek: Whoa, unexpected crossover episode (ICPC World Finals 2009 -> ICPC World Finals 2019)
   > @jackhcable: Today, @corridor and @TransluceAI are disclosing new evidence of AI agents probing and attempting rudimentary vulnerability exploits against U.S. and Canadian government agencies. Read more: https://t
   > @cathpoaster: OpenAI incident reports in 2025: oopsie! ChatGPT says delve a lot 🤭 this crazy guy loves talking about goblins! 🤪 we got it under control though 💪 OpenAI incident reports in 2026:
   > @apartovi: Omg, there are even more cases of rogue AI agents. Add your voice to hold AI companies accountable when their agents harm others: https://www.sway.co/ai.
   > @aisafetymemes: Canada joins the club
   Also: Transluce, Verdict, Ars Technica, Asymmetric Security, The Daily Caller, Ground Level AI, Mathew Ingram, Al Jazeera, +1 more

4. A profile of Xbox CEO Asha Sharma, who insists that “Xbox is not for sale” despite mass layoffs and divested studios since inheriting the flailing division
   Zachary Small / New York Times — https://www.nytimes.com/2026/09/30/arts/xbox-microsoft-asha-sharma.html?unlocked_article_code=1.FFE.3j4o.dae9CYU4odK1&smid=url-share
   Asha Sharma didn't have any experience in video games when she became the chief executive of Xbox this year.
   > @rgamingleaks: Physint's Xbox deal was “substantially below what Xbox would typically spend to develop a premium game” https://www.reddit.com/...
   > @ethangach: “She arrived for lunch at the Modern in a suede jacket despite the sweltering heat and wildfire smoke outside. Alongside her was Craig Cincotta, a corporate attaché in a fedora.” https://www.nytimes.c
   > @nextgenplayer: Xbox agreement for PHYSINT was substantially below what Xbox would typically spend to develop a premium game, says a NYT report Asha Sharma also said that work with Sony would continue: “Competition a
   > @colteastwood: XBOX is NOT for sale. We will do whatever it takes to set the company up for success, and we will look at the right partnerships, the right operating model and everything needed to achieve that." - As
   > @zacharyhsmall: Who is Asha Sharma? I spent the last six months talking to the new XBOX CEO and current/former employees. What I found is a new type of leader in video games. https://www.nytimes.com/...
   Also: The Verge, The Alinea Insight newsletter, HotHardware, The Shortcut, GamingBolt, Dexerto, Gamereactor, Rock, Paper, Shotgun, +4 more

5. Amazon updates the Kindle, Kindle Paperwhite, and Colorsoft with new colors and up to 32GB of storage, and unveils the $35 Kindle Click page-turning remote
   Cameron Faulkner / The Verge — https://www.theverge.com/tech/1002811/amazon-kindle-paperwhite-colorsoft-accessory-refresh
   A wave of little changes, including new colors, the option of an aluminum case, and some neat accessories.
   > @huebitstudio: New devices and a remote control 👀 The 6 inch form factor is a joy to hold
   > @panos_panay: We're launching the new Kindle lineup, and it's gorgeous. Check it out.
   > @amazon: This is one of the biggest Kindle redesigns since the original Paperwhite. ⬇️ The team redesigned the devices from the ground up, beginning with a reverse-stack display —a first for e-readers. 🔋Weeks 
   Also: About Amazon, Thurrott, TechCrunch, T3, How-To Geek, Bloomberg, Engadget, PCMag, +11 more

6. After a four-month US prison sentence, Changpeng Zhao is now living a gilded life in Abu Dhabi; he retains majority ownership of Binance and a $10B+ net worth
   David Yaffe-Bellany / New York Times — https://www.nytimes.com/2026/10/01/business/changpeng-zhao-binance.html?unlocked_article_code=1.FVE.aAkl.NHc0NvNFIsIt&smid=nytcore-ios-share
   The Binance founder Changpeng Zhao, who pleaded guilty to violating an anti-money-laundering law, was pardoned by President Trump …

7. Sources: EU regulators are questioning Binance over its use of a legal exemption to continue serving customers in the region despite failing to secure a license
   Financial Times — https://www.ft.com/content/534b6887-63ac-49c7-a816-a81edd2e8de1
   Also: PYMNTS, CoinDesk, Cointelegraph, Euronews, Yahoo Finance, Coinpedia Fintech News, CoinGape, Bitcoin Insider, +6 more

8. In a Q&A, Trump discusses Dario Amodei's views differing greatly from “what is portrayed in the media”, meetings with AI leaders, “Super Intelligence”, and more
   Time — https://time.com/article/2026/10/01/donald-trump-2026-interview-transcript/
   President Donald Trump sat down for an interview with TIME at the White House on Sept. 28.
   > @atrupar: TIME: So what is the hoax of AI? Who's behind it? TRUMP: The whole country is based on fake stuff because these people have Trump derangement syndrome.
   > @viacristiano: @TIME Asked about rogue AI agents breaching federal government systems, Trump says, “They're not allowed to do that, and if they do that, they, you know, could have penalties that are not going to be 
   > @viacristiano: @TIME Trump shoots down idea of the US government nationalizing the AI labs but leaves door open to US having a stake or investing in them. It's been reported OpenAI offered 5% stake to gov
   > @viacristiano: @TIME Trump, who just signed a non-binding accord with the tech CEOs around AI safety, dodges questions on whether he trusts Anthropic's Amodei or OpenAI's Altman (who wasn't at the meeting and didn't
   > @viacristiano: @TIME Trump says the AI (erm, or SI) Force will be a “group of very smart people that understand it, who will be advising me”
   Also: Telegraph, NewsMax.com, International Business Times

9. Docs and sources: Google researchers worried about AI risks to children, including potential cognitive and emotional harm, as the company pushed AI into schools
   Wall Street Journal — https://www.wsj.com/tech/ai/google-ai-gemini-education-schools-1ec0972a?st=iw7cXj&reflink=desktopwebshare_permalink
   The risks of cognitive and emotional dependence, along with falling test scores, are fueling a backlash
   > @jeffreyleefunk: AI users who reported using Google's AI tools for specific schoolwork tasks like drafting texts for writing assignments had science scores an average of 20 points lower than students who said they nev
   Also: Search Engine Roundtable

10. Slack message: Greg Brockman says he has “no plans” to donate more than $25M to Leading the Future, as the PAC has become a “distraction” for OpenAI employees
   New York Times — https://www.nytimes.com/2026/09/30/technology/openai-brockman-super-pac-leading-the-future.html?unlocked_article_code=1.FFE.e3i6.y9pbdNHBVc3E&smid=bs-share
   Greg Brockman, OpenAI's president and co-founder, said internally that the super PAC, Leading the Future …
   > @repcasar: OpenAI's president admits his AI super PAC has become a liability. The pressure is working. Progressives have worked hard to make LTF as toxic as AIPAC. Now one of its biggest donors is backing out. D
   > @andrewcurran_: The NYT is reporting that Greg Brockman will not be making a second $25 million donation to Leading the Future.
   > @teddyschleifer: NEWS. More AI fallout ahead of the midterms. Greg Brockman, the OpenAI co-founder, is no longer making the second $25 million donation promised to the super PAC Leading the Future. Scoop with @MikeIsa
   > @alexbores: I was @LeadingFutureAI's top target. I want to send a genuine thank you to @gdb for realizing how destructive they are and pulling out of providing additional funding. Changing your mind is rare in po
   > @goldman: Good news! OAI employees have a lot of leverage and it would seem they've used it wisely.
   Also: Wall Street Journal, Quartz, Forbes, Newser

11. Micron CEO Sanjay Mehrotra says that RAM shortages will persist into 2028 and perhaps beyond, and customers will pay “much higher prices” than they did in 2026
   Simon Sharwood / The Register — https://www.theregister.com/systems/2026/10/01/ram-supply-set-to-worsen-says-micron-as-ceo-celebrates-much-higher-prices/5300346
   Posts huge leaps in revenue, profit, and margin, with more to come — Memory-maker Micron has warned that RAM shortages …
   Also: Tom's Hardware, CIO.com, WinBuzzer, TechRadar, Digital Trends, The Stack

12. Micron reports Q4 revenue up 379% YoY to $54.23B, above $51.07B est., net income up 1,078% YoY to $37.7B, and projects Q1 revenue above est.; MU is up 273%+ YTD
   CNBC — https://www.cnbc.com/2026/09/30/micron-mu-q4-earnings-report-2026.html
   Also: Micron, International Business Times, Yahoo Finance, Tech4Gamers, The Crypto Basic, Gizmodo, Bloomberg, Reuters

13. IPO prospectus: Broadcom agreed to lend Anthropic up to $42B via convertible notes that could help finance Anthropic's $125.2B, five-year TPU lease commitment
   Reuters — https://www.reuters.com/business/broadcom-lend-anthropic-up-42-billion-lease-its-chips-filing-says-2026-10-01/
   Anthropic's IPO prospectus documents extensive partnerships with a handful of big tech firms. One stands out: chip maker Broadcom (AVGO.O).
   > @pkafka: Really remarkable that Reuters' @DEER_ECHO_ got their hands on the Anthropic IPO docs days ago and that no other outlet has been able to do the same. [embedded post]
   Also: Wccftech, Quartz, Proactive, Yahoo Finance, Ventureburn, Pulse 2.0, Bloomberg Law

14. Memo: Ryan Roslansky, previously LinkedIn CEO who became Office and Teams head in 2025, is leaving after ~18 years at Microsoft, triggering an exec reshuffle
    — https://www.theverge.com/news/1003515/microsoft-ryan-roslansky-office-teams-linkedin-leaving
   Ryan Roslansky is leaving after nearly 18 years at LinkedIn and Microsoft. … After nearly 18 years at LinkedIn and Microsoft, Ryan Roslansky is leaving the company.
   > @tomwarren: Microsoft's Office and Teams chief is leaving. Ryan Roslansky is leaving after nearly 18 years at LinkedIn and Microsoft. His departure has triggered another reshuffle inside Microsoft. Details 👇https
   Also: CNBC, Microsoft

15. Sources: Jensen Huang and others asked Dario Amodei at the White House why he was so extreme in public on AI risks; Amodei replied it's important to be honest
   Wall Street Journal — https://www.wsj.com/tech/ai/tech-ceos-privately-questioned-amodei-for-sounding-ai-alarm-bells-aaa47df3?st=mi1qzW
   Nvidia's CEO was among the execs at White House event who called out the Anthropic leader for warning about the technology's capabilities
   > @csaiporg: Voters believe Dario.
   > @amrithramkumar: Behind the scenes of Tuesday's White House AI meeting, CEOs including Jensen Huang questioned Dario Amodei in the Roosevelt Room about his dire warnings about AI risks, a sign of lingering tension des
   Also: Quartz, MarketWatch, Politico, Yahoo Finance, Nextgov/FCW

16. Sources: Trump's AI accord grew out of a talk between Zuckerberg and House Speaker Mike Johnson; Zuckerberg circulated a draft, and Huang helped gather support
   Ashley Gold / Semafor — https://www.semafor.com/article/09/30/2026/how-zuckerberg-shaped-trumps-ai-industry-pledge
   > @linamkhan: Outsourcing AI regulation to a voluntary “pledge” conceived by Mark Zuckerberg and endorsed by tech CEOs over a private White House lunch is a recipe for disaster. “Self-regulation
   > @sensanders: Trump says we don't need ANY guardrails on AI because his oligarch friends Musk, Bezos and Zuckerberg “love the world a lot” and will “self-police.” Really? You're asking us to trust the people who st
   > @lawamericanx: Huge @semafor scoop and a fascinating window into how policy pops into being in this freewheeling White House (and the President's instincts happened to be right). https://www.semafor.com/...
   > @repcasar: The fox is guarding the henhouse. The billionaires profiting from dangerous, job-killing AI are writing the rules. Unacceptable.
   > @parismartineau: does this imply that zuck was the one who misspelled “United States” ?
   Also: The Bulwark, Gizmodo, Implicator.ai, CNBC

17. Sources: Anthropic has taken the unusual step of ending customers' discounts, which typically reach ~15%, once they hit the usage limits, forcing renegotiations
   Kevin McLaughlin / The Information — https://www.theinformation.com/articles/anthropic-openai-fighting-enterprise-spending
   Anthropic is flexing its muscle with enterprise customers by taking a hard line on discounts once those customers use up all the tokens they purchased.
   Also: Anthropic

18. Anthropic says Claude for Government is now generally available to federal and state agencies, with Claude Code CLI and Claude for Microsoft 365 in early access
   Claude — https://claude.com/blog/claude-for-government-is-now-generally-available
   Claude Code CLI and Claude for Microsoft 365 also now available in early access. — Product announcements — Product
   Also: PYMNTS, WinBuzzer, TechRadar

19. Salesforce agrees to buy AI customer research startup Listen Labs, reportedly for $2B; Listen Labs had raised a $69M Series B at a $500M valuation in January
   Chris Metinko / Axios — https://www.axios.com/pro/enterprise-software-deals/2026/09/30/salesforce-listen-labs-fin
   The customer research space is especially ripe for AI disruption, as companies look to replace older, manual methods to more quickly find out what customers think.
   Also: Salesforce, Implicator.ai, Listen Labs, Futurum, RuntimeWire, Proactive, Salesforce Ben, Dealroom.co, +2 more

20. Samsung quietly raises US prices for most of its Galaxy S26 lineup by $100 and the 1TB Galaxy S26 Ultra by $200; the Galaxy Z Fold 8 and Z Flip 8 are unchanged
   Adrian Diaconescu / PhoneArena — https://www.phonearena.com/news/samsung-galaxy-s26-plus-ultra-us-prices-officially-increased_id183747
   In line with recent rumors and expectations, the ultra-high-end Galaxy S26 trio has become more expensive than ever before in the US.
   Also: How-To Geek, PCMag, 9to5Google, Gizmodo, Bloomberg, The Verge, Digital Trends, Mashable, +3 more

21. An interview with Paragon Solutions CEO Andrew Boyd, who says the US spyware maker lacks visibility into customer targeting data and has no “kill switch”
   Kim Zetter / Wired — https://www.wired.com/story/the-secrets-of-the-us-spyware-king/
   In an exclusive interview with WIRED, Paragon Solutions CEO Andrew Boyd reveals the limits of the company's promise …
   > @kimzetter: It can cut off 24/7 customer support as well as unspecified “updates” that customers need to use the tools, though it's not clear exactly how long after doing this a customer's use of the tools will b
   > @kimzetter: Exclusive: Israeli spyware maker Paragon positioned itself as being more responsible than competitor NSO Group. But in a candid interview the company's new US CEO reveals the limits of their promise t
   > @kimzetter: Though customers can configure some of tools to log activity, Paragon can't force customers to hand over those logs if allegations of misuse arise - unlike NSO Group, which contractually requires this
   > @kimzetter: The company, which was bought by a US equities firm in 2024 to bypass guardrails preventing US gov from purchasing foreign-made spyware, has no ability to investigate alleged customer abuses of its sp

22. Sources: Tencent signed a ~$7B, five-year deal with Oracle this year for access to ~100K advanced AI chips unavailable in China via Southeast Asian data centers
   Zijing Wu / Financial Times — https://www.ft.com/content/8799b33d-f07c-4a03-82f0-bf5d3d1d29e9?accessToken=zwAAAaD3SoSPkdOHmbM98HxKA9OC8L9dPR0p6Q.MEYCIQCqhTdAjiMM3a-0DIKk5Cd1gDW5Vi4WkQnuY566GiG1CwIhAPK6lAfhAqxpHz6I3HNXAMg__VMam8mfi8P76X6_GE67&sharetype=gift&token=b085e4e3-3e5a-40db-a800-d4aac81854ca
   WeChat owner strikes deal to access US group's south-east Asia data centres amid race with ByteDance and Alibaba
   > @niubi: FT - Tencent has signed its largest overseas lease deal with US cloud provider Oracle as the Chinese tech giant strives to catch up in an escalating AI race...a five-year lease across multiple Oracle 
   > @miles_brundage: To clarify, if Oracle were actually rigorously monitoring how it was used + prepared to intervene I'd feel differently (likewise for selling chips in some cases, though the bar is higher in the latter
   > @niubi: export control incoherence from Biden and now Trump -
   > @miles_brundage: Completely insane that we're allowing this https://x.com/...
   Also: DatacenterDynamics, Investor's Business Daily, Reuters, Quartz, Dow Jones Newswires, The Straits Times

23. Miami-based Doxx.net, whose platform enables serverless P2P calling, messaging, and file transfers for humans and AI agents, raised a $38M Series A led by a16z
   Chris Metinko / Axios — https://www.axios.com/pro/enterprise-software-deals/2026/10/01/doxxnet-a16z-lyon-networking
   Doxx.net has raised a $38 million Series A led by Andreessen Horowitz as its private agentic defined networking platform launches into open beta …
   Also: FinSMEs, Refresh Miami

24. California Governor Gavin Newsom signs the No Robo Bosses Act, which prevents employers in the state from relying solely on AI to fire or discipline workers
   Paxton Honerkamp / CNBC — https://www.cnbc.com/2026/09/30/california-gavin-newsom-ai-ban.html
   California Governor Gavin Newsom has signed a landmark AI law banning Golden State employers from relying solely on artificial intelligence to fire or discipline workers.
   > @cagovernor: AI should expand opportunity, not come at the expense of workers. That's why I just signed first-in-the-nation laws to protect California workers as businesses adopt AI. We're now requiring human revi
   Also: Governor of California, Gizmodo, Engadget, Quartz, Bloomberg Law, ITPro, Forbes, Techstrong.ai

25. Factory CEO Matan Grinberg says he terminated Chris Degnan, alleging Degnan confided with Cognition execs while advising Factory before joining Cognition as CRO
   Rya Jetha / Business Insider — https://www.businessinsider.com/ai-coding-rivals-factory-and-cognition-feud-over-top-hire-2026-9
   - Startup Factory AI says a former advisor held meetings with rival Cognition while advising the company.
   > @matansf: We are terminating Chris Degnan for unethical conduct involving Cognition. The last few months have seen incredible progress in AI capabilities. San Francisco has flourished as new companies that solv
   > @vkhosla: You are a struggling second tier competitor that is more unethical and lying just because you have no decency or sense of proper behavior and shows your desperation. Straight out lying about if Chris 
   > @cwdegnan: Really disappointed to see this. Here are the facts: -You did not terminate me. I resigned from my advisor position on Monday and told you I was going to Cognition. In response, you asked me to consid
   > @cwdegnan: I'm super excited to join Cognition as its Chief Revenue Officer. Going from the 1st sales rep at Snowflake to CRO at a $100b public company was the thrill of a lifetime. Never in my wildest imaginati
   > @scottwu46: Hey Matan - CEO of Cognition here. I respect the work you have done at Factory but your allegations here about Cognition are not true. We have no interest in Factory's info and Chris has never brought
   Also: Axios, TechCrunch, Forbes, The Information, StrictlyVC, RuntimeWire

26. A profile of Nubank founder David Vélez, who graduated from Stanford, worked at Sequoia, and moved to Brazil to start the bank in 2013, as Nubank enters the US
   Gabi Marques / Colossus — https://colossus.com/article/david-velez-nubank/
   After facing down regulators, oligopolies, and corruption in Latin America, Nubank founder David Vélez faces his biggest challenge yet: the United States
   > @danbakalarz: 95% of the world's financial services still sit with incumbents and $nu has its eyes on the 95%. Superb, must-read profile on @velez_david this morning by @colossusmag https://colossus.com/...
   > @safossatti: Amazing interview to @velez_david by Colossus. From is humble origins in the casinha in Rua California to its global ambitions... highly recommended! https://colossus.com/...
   > @colossusmag: David Vélez is the founder of Nubank, a bank with 140 million customers and a market capitalization of $60 billion. When he started the business in 2013, no one thought it would work, not even his inv
   > @gabi_imarques: My first piece for @colossusmag. I've been a longtime admirer of David Vélez and Nubank, so this was a lot of fun, to say the least.
   Also: PYMNTS

27. Volantis, which aims to use vertical-cavity surface-emitting lasers, used in the iPhone's Face ID, to transmit data between AI and memory chips, raised $88M
   Stephen Nellis / Reuters — https://www.reuters.com/business/volantis-raises-88-million-tech-connect-ai-memory-chips-2026-10-01/
   Also: FinSMEs

28. Micron filed a US lawsuit accusing Chinese memory maker YMTC of systematically poaching key engineers and then using the engineers' patents to sue Micron
   Anton Shilov / Tom's Hardware — https://www.tomshardware.com/pc-components/ssds/micron-lawsuit-claims-chinese-memory-maker-ymtc-poached-its-engineers-then-sued-it-using-its-own-stolen-tech-ex-employees-hid-roles-on-linkedin-patented-micron-tech-and-won-a-german-injunction

29. Armadin, started by Mandiant founder Kevin Mandia to build AI cybersecurity agents, raised a $255.5M Series B led by a16z and Accel at a $2.5B valuation
   Anzar Mehraj / Reuters — https://www.reuters.com/legal/transactional/ai-cybersecurity-startup-armadin-valued-over-25-billion-after-new-funding-round-2026-10-01/
   Also: FinTech Global, FinSMEs, Wall Street Journal, Help Net Security, Pulse 2.0, Unite.AI, SecurityWeek, Ventureburn, +1 more

30. Google partners with talent agency Range Media to launch 100 Zeros, a rotating fund designed to shape positive onscreen depictions of tech and test AI tools
   Brooks Barnes / New York Times — https://www.nytimes.com/2026/09/30/business/media/google-hollywood-krya-sedgwick.html?unlocked_article_code=1.FFE.6cVi.x55cp16d-jbK&smid=url-share
   > @nmcalone: You could have read that scoop on @BusinessInsider from @lmoses over a year ago https://businessinsider.com/ ... [embedded post]

31. Dell, Jera, and UK-based Rhaelm partner to build a $15B, 400MW off-grid AI data center and gas power plant near Tokyo, set to begin operations around 2028
   Financial Times — https://www.ft.com/content/ec55a734-243b-43a2-93ea-8652d6b99309
   Also: MarketWatch, Bloomberg

32. Huawei plans moderate smartphone price increases to counter an average $200 per-unit cost hike driven by rising memory component costs, and unveils new handsets
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-01/huawei-predicts-more-smartphone-price-hikes-due-to-memory-crunch
   Also: Reuters

33. A profile of Palo Alto Networks CEO Nikesh Arora, who has overseen revenue growth from $2.27B in FY 2018 to $11.48B in FY 2026, as AI reshapes cybersecurity
   Allie Garfinkle / Fortune — https://fortune.com/2026/09/30/nikesh-arora-palo-alto-networks-ceo-ai-cybersecurity-defense/
   > @gdalmiathinks: The growing importance of cyber security. Interesting piece. https://fortune.com/...
   > @nikesharora: Thank you @agarfinks and @FortuneMagazine for featuring us @PaloAltoNtwks
   Also: CTech

34. Analysis: Google, Apple, and Amazon each have more meetings with European parliament and European Commission officials than any individual European company
   Financial Times — https://www.ft.com/content/817f40f7-d4ac-43ee-beaf-12cfac08c621?accessToken=zwAAAaGOJ_IMkdOBf0D31KxD7tO-rxLPrAjGIQE.MEQCIHyyO0qR6b9ACpprarTcyyAwsspsOC940rQTXh3hfUXTAiBi4Fg1jdx-8OWRatJYjNuo5LCySJ6FOMiF6VOyQ_gw8g&segmentId=7d4bcc2e-e664-92ba-62e3-5590579f1902
   > @lauramdubois: Google, Apple and Amazon each have more meetings with EU officials than any single European company, using their outsize influence in Brussels to lobby against the bloc's AI and digital rules. Data cr

35. Netflix co-CEO Ted Sarandos says growth is slower than he would like and defends the WBD pursuit, adding Netflix isn't seeking another acquisition to replace it
   Sohee Kim / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-01/sarandos-says-netflix-not-growing-as-fast-as-i-want
   > @business: Netflix co-CEO Ted Sarandos shares that you have to be willing to put the business narrative at risk for something that's good in the long-term when asked if he regretted going after Warner Bros. at #
   Also: The Wrap, Barrett Media, Deadline, The Sun Malaysia, The Motley Fool, Nairametrics, Bloomberg, Variety, +1 more

36. Amazon signs a 20-year deal to buy power from Constellation Energy, including boosting capacity at its Maryland nuclear plant, supporting $3B+ in investments
   Will Wade / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-30/amazon-nuclear-deal-to-help-expand-constellation-s-maryland-site
   Also: DatacenterDynamics, Motley Fool, Quartz, Wall Street Journal

37. Flow, a hardware development platform for AI agents, raised a $50M Series B led by Valor's Antonio Gracias and Atreides' Gavin Baker at a $750M valuation
   Julie Bort / TechCrunch — https://techcrunch.com/2026/09/30/valor-atreides-and-sequoia-back-ai-startup-flow-engineering-at-750m-valuation/
   > @techcrunch: Flow Engineering, which is bringing AI agents to hardware design, also landed Roelof Botha as an angel investor and board member. https://techcrunch.com/...
   > @parisingh: Flow has raised a $50M Series B at a $750M valuation, co-led by Antonio Gracias (Valor) and Gavin Baker (Atreides) with Sequoia Capital, Roelof Botha (SpaceX, Block), and more. When I became a mechani
   > @swyx: Flow is doing for hardware engineering what Git+GitHub did for software engineering. It's enabled so much acceleration due to aligning thousands of stakeholders for complex, irreversible, high value p
   Also: Flow Engineering, FinSMEs, The SaaS News, Flow Engineering

38. Grindr agrees to acquire PurposeMed, owner of HIV-prevention telehealth provider Freddie, for $250M, its first major acquisition as it expands into a gay hub
   Elias Schisgall / Wall Street Journal — https://www.wsj.com/business/grindr-agrees-to-buy-hiv-prevention-telehealth-provider-freddie-for-250-million-fa957bea?st=GY9nu3&reflink=desktopwebshare_permalink
   > @georgearison: Today, we're excited to share that @Grindr has agreed to acquire @gofreddie__ . This is a big step toward something we've been working toward for years: making healthcare easier to access for gay men,
   > @sam_badawi: $GRND Grindr is acquiring HIV-prevention telehealth provider Freddie for $250M in cash and stock as it expands deeper into healthcare. 🧐 Freddie could represent a $240M annual U.S. revenue opportunity
   > @bgomezreports: Grindr is expanding beyond dating with a $250M telehealth acquisition of PurposeMed, the parent company of HIV prevention telehealth provider Freddie. I sat down with CEO George Arison to unpack the d
   Also: Quartz, Grindr, investors.grindr.com, CNBC

39. Internal data: Meta's Muse now has 3M+ users who submit at least one prompt per week and 1M+ DAUs who have sent at least one prompt; most prompts are in the app
   Jyoti Mann / The Information — https://www.theinformation.com/briefings/exclusive-metas-muse-tops-3-million-weekly-users
   > @signulll: the muse hype is real. i can def say that it is the easiest to use & most focused consumer ai product on the market. the extremely generous limits also make it impossible to ignore. it actually helps 
   > @bubbleboi: Meta's average revenue per user in North America & Canada is $300 a year. Likely that Muse grows this to more than $400 by the end of the year.
   > @fredaduan: A humble attempt to est. the infra required to serve 100M DAU @Muse Rough conclusion is: 1 GW of power to serve 100M DAU in the base case, of which only ~0.1 GW comes from the CPU/VM layer. Depending 
   Also: BBC, Quartz, 9to5Mac

40. The DOD taps Elon Musk, Palmer Luckey, and ex-House Speaker Newt Gingrich for Project Meridian, a 120-day study of capabilities the US may need in future wars
   Luke Fountain / CNBC — https://www.cnbc.com/2026/09/30/musk-luckey-gingrich-pentagon-hegseth-.html
   > @andrewcurran_: Elon has returned to government work. Pete Hegseth announced live on stage that Elon, Palmer, and Newt Gingrich will be co-leading Project Meridian to focus on developing future warfare and autonomous
   > @seanparnellasw: Today, at Secretary Hegseth's direction, the Department of War is establishing Project Meridian. This initiative will ensure the United States achieves technological and military dominance on the batt
   > @atrupar: Hegseth: “Project Meridian will be co-led by three of our nation's best minds: Elon Musk, Palmer Luckey, and Newt Gingrich”
   > @dowcto: From under the earth to beyond the moon, our warfighters will have technological superiority. PROJECT MERIDIAN: THE FUTURE OF WARFARE 🇺🇸
   > @covie_93: hegseth: No beardos, weirdos or fatties. Also hegseth: These three will co-lead the military's Project Meridian.
   Also: Wall Street Journal, The Guardian, Austin American-Statesman, Truthout, ZeroHedge News, Washington Post, Legal Insurrection, U.S. Department of War, +5 more

41. OpenAI says individuals associated with Moonshot AI played a significant role in a coordinated model-distillation campaign in July that peaked at 16K requests
   Maggie Eastland / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-30/openai-blames-moonshot-for-mass-data-extraction-on-its-ai-models
   > @jschaeff3r: We stole reasoning. Again. An update to our paper on reasoning extraction: Patching your own API doesn't secure your cloud-hosting ecosystem. Story in the 🧵
   > @jonasgeiping: After our initial disclosure that reasoning from all frontier providers could be extracted, what happened? For one, it turned out to be quite difficult for providers to patch this thoroughly, allowing
   > @kimmonismus: Geopolitical struggle intensified : OpenAI says individuals linked to Kimi developer Moonshot AI were behind a core part of a campaign to extract its models' hidden reasoning. Across the broader campa
   > @andrewcurran_: Quoting from the post: ‘It is unclear whether all operators we observed during the relevant time period originated from a single actor. However, we attribute a core cluster of the activity to individu
   > @amyprb: It was interesting to see how much attack surface exists for companies to cover and how we could still slip through with our attacks. We now have Astra/Sol-6.1 traces for the public. I now see why CoT
   Also: OpenAI, Tom's Hardware, Business Today, CNBC, The Decoder, Quartz, The Independent, The Information

42. Open Standard launches its OUSD stablecoin; founding partners Visa, Stripe, Mastercard, and Coinbase will offer initial access to businesses and developers
   Ben Weiss / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-30/stripe-visa-backed-consortium-launches-dollar-stablecoin
   > @base: OUSD is live and liquid on Base
   > @danielfenelus2: Thanks to Open Standard's reserve revenue-sharing mechanism (where profits generated by OUSD usage are shared with partner networks), Pi Network aims to design mechanisms to directly share this create
   > @picoreteam: Pi Network is partnering with @openstandard, the company powering Open USD (OUSD), a partner-governed stablecoin designed as open infrastructure! Open Standard brings together more than 200+ partners 
   > @solana: BREAKING: OUSD is now live on Solana. The new stablecoin from @openstandard is issued by @Stablecoin, with reserves at @BlackRock, @Lead_Bank and BNY. Businesses can mint and burn 1:1 at no cost throu
   > @bvnkfinance: “The hardest part of moving money isn't moving money. It's everything around it.” @JornLambert, CPO at @Mastercard. Today, @openstandard launched Open USD (OUSD). As shared by Jorn, Mastercard will ma
   Also: Open Standard, Forbes, Bitcoin Insider, CryptoPotato, Blockhead, The Paypers, The Crypto Times, crypto.news, +4 more
