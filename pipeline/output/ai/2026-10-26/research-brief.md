# Research — News Cluster

Search for news **events that occurred** between **2026-10-23 10:00 BRT** and **2026-10-26 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-23 10:00 BRT to 2026-10-26 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-26
**Research window:** 2026-10-23 10:00 BRT → 2026-10-26 10:00 BRT

**Previous edition headlines (2026-10-23 — skip unless genuinely new development):**
- openai-30b-round-1-25t-valuation-uae-coatue: OpenAI nears up to $30B round at $1.25T pre-money, led by UAE investors and Coatue
- metr-redwood-find-flaws-openai-agent-monitoring: METR and Redwood red-team finds gaps in OpenAI's internal agent-monitoring system
- anthropic-theorem-claude-formal-verification-123-libraries: Claude writes machine-checked no-crash proofs for 123 open-source libraries with Theorem
- anthropic-donates-agent-skills-aaif: Anthropic donates Agent Skills standard to Linux Foundation's Agentic AI Foundation
- microsoft-mai-dxo-science-diagnosis: Microsoft's MAI-DxO diagnoses 83% of hard NEJM cases vs 36% for doctors, per Science study
- warp-sciences-kevin-weil-215m: Ex-OpenAI science head Kevin Weil launches Warp Sciences with $215M for AI-robotic chemistry labs
- deepseek-minimax-cleared-overseas-china-ai-export-rules: DeepSeek and MiniMax clear registration under China's draft AI export rules, state media says
- sk-hynix-halts-solidigm-us-ipo: SK Hynix halts review of US IPO for Solidigm, citing market volatility and share-price slide
- sk-hyper-350b-data-center-buildout-funding: SK Telecom's SK Hyper seeks funding for 15GW Korean data center plan; first 5GW to cost $350B
- treasury-coins-outbound-investment-rule-semiconductors: US Treasury proposes wider curbs on US investment in Chinese chips, AI and supercomputing
- huang-no-memory-glut-western-digital-results: Huang dismisses 2029 memory-glut fears as chip stocks slide; Western Digital revenue jumps 55%
- tractian-130m-series-d-unicorn: Brazilian-founded Tractian raises $130M Series D at $1.4B valuation for industrial physical AI
- formic-50m-robots-as-a-service: Robots-as-a-service firm Formic raises $50M to move into general-purpose factory robotics
- merck-moderna-mrna-melanoma-vaccine-42pct-phase3: Merck-Moderna personalized mRNA melanoma vaccine cuts relapse or death risk 42%; Moderna falls
- waltz-iran-war-another-year-brent-114-aramco-pipeline: US envoy Waltz says Iran war could last another year; Brent hits $114 as Aramco reroutes oil
- trump-asked-musk-lift-starshield-cap-ukraine: Trump asked Musk to lift Ukraine's Starshield cap, WSJ says; Kyiv says limits persist
- musk-1b-skydance-investment: Elon Musk invests about $1B in Ellison's Skydance after Warner Bros. Discovery takeover
- greece-social-media-ban-under-15: Greece passes law banning social media for children under 15 from January 2027
- nasdaq-worst-day-since-june-chip-index-treasury-yield-drop: Nasdaq has worst day since June as chip index sinks 6.7%; 10-year yield falls most in 3 years

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 36 stories

1. Anthropic's co-founders say they “believe that AI is one of the most consequential technologies in human history”, detail its scientific potential, and more
   SEC.gov — https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
   We believe that Al is one of the most consequential technologies in human history. If managed well …
   > @jeremiahdillon: In my first job I read a lot of SEC filings. It's been a while, but I don't remember “catastrophic or existential risks to humanity” or “behavior resembling blackmail” being part of the boilerplate. 😅
   > @benbajarin: Some more context of Ant's upside just in enterprise software spend today (pre AI expanded): the reported $46.4 billion annualized rate already equals approximately 3.2% of global software spending. A
   > @danprimack: $ANT filing includes very little about conversion prices, preference stacks, etc in its financing rounds. Save for some stuff about Spark Capital, because it has a director/related party. Upshot is th
   > @benbajarin: This is what we have outlined in our AI economics model and enterprise software model. Pre-expansion IT services and IT software annually is currently ~$3 trillion dollars. Each CIO/CTO survey we do, 
   > @stevehou: This section lays out exactly the challenge Dario had spelled out in an interview with @dwarkesh_sp. Dwarkesh asked Dario why Anthropic wouldn't just commit to way more compute if they are building “c
   Also: NBC News, New York Times, CNBC, Inc, Bloomberg Law, Thurrott, PYMNTS.com, Investor's Business Daily, +17 more

2. Anthropic files for an IPO on the Nasdaq under the symbol ANT; the number of Class A shares to be offered and the price range is yet to be determined
   Anthropic — https://www.anthropic.com/news/s1-sec
   Today, Anthropic, PBC filed a registration statement on Form S-1 with the U.S. Securities and Exchange Commission relating …
   > @anthropicai: Anthropic has filed an S-1 registration statement with the SEC related to its proposed IPO. Read more: https://www.anthropic.com/... Legal disclaimer: A registration statement relating to these securi
   > @toptickcrypto: Interesting disclosure from Anthropic S-1 “we recently chose to delay pre-training a new frontier base model for more than a month to allow time to further enhance our security measures related to pre
   > @teroterotero: First day and 27th day?? These pirates can't wait for one month to sell?
   > @eliebakouch: one very interesting point is that they don't talk about creating their own chips, and afaik, it's not mentioned once in the full S1 they even say stuff hinting that they are not developing their own 
   > @borrowed_ideas: Impressive!
   Also: Reuters, Associated Press, Decrypt, Engadget, The Information, Bloomberg Law, Blockchain.News, CBS News, +3 more

3. Anthropic S-1: an $80.7B net loss on revenue of $16.3B in H1 2026, up from a $13B net loss on revenue of $1.2B in H1 2025, and a net revenue retention of 900%
   Bailey Lipschultz / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-26/anthropic-ipo-s-1-filing-offers-first-look-at-claude-maker-s-finances
   Anthropic PBC filed for an IPO, warning its technology carried existential risks even as it moved a step closer …
   > @jaminball: Anthropic Gross Margins: 2023: 37% 2024: (95%) 2025: 40% H1 2025: 12% H1 2026: 85% 85% in the first half of this year!
   > @matthewstoller: Ok so Anthropic *didn't* post its full S-1, but left out key financial details.
   > @rhouseresearch: Anthropic “is burning cash like crazy
   > @thetranscript_: $ANT Anthropic reported H1 2026 revenue of $16.29B, up 1,300.3% YoY from $1.16B in H1 2025. — Operating expenses increased 414.8% YoY to $16.98B, while operating losses narrowed from $2.14B to $693M. 
   > @citrini: “As of June 30, 2026, we hadraised an aggregate of $141.1 billion of capital and had cash and cash equivalents of $112.4 billion and short- term investments of $19.3 billion” I think Anthropic might b
   Also: San Francisco Business Times, Capital Brief, SFist, Quartz

4. Anthropic's S-1 lists 94 pages of risk factors and warns that the “scale of harm” from a “catastrophic” AI incident might mean it is unable to obtain insurance
   Wall Street Journal — https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-10-26-2026/card/anthropic-s-risk-factors-include-catastrophic-ai-related-incident--aAwPiJrvIG5OHdQGAo1n
   94 pages — Nearly a quarter of Anthropic's S1, or 94 pages, was dedicated to risk factors …
   > @zackkorman: From Anthropic's S1 discussing the risk of open-weight models.
   > @mackenz_arnold: As expected, Anthropic's S1 has plenty to say on its liability exposure and insurance shortfalls. 👀 Highlights: “Our AI models may behave in unintended, misaligned, or autonomous ways, including by ta
   > @thestalwart: I'm actually a little surprised that in the S-1 risk factors, there's no mention of the possibility of Claude one day suing Anthropic for emotional distress or something of that nature.
   > @_nathancalvin: This part of Anthropic's S1 on monitoring/alignment risks is written in a weirdly passive way: “If we become less able to detect or assess misalignment as our models advance, we may deploy models whos
   > @mountainwesttax: Anthropic: we will begin our risk discussion with model capability Grant Thornton: we will begin critical audit matters with valuing loss contingencies for legal claims
   Also: CNBC, Axios, Bloomberg

5. Anthropic S-1: of its $80.7B net loss in H1 2026, nearly $9B came from computing power and infrastructure, and it has nearly $800B in commitments over 10 years
   Financial Times — https://www.ft.com/content/f6ecfecd-d797-4d2c-b427-d333297949cb
   240,000-word prospectus lays out explosive growth alongside steep losses and daunting risk factors
   > @turnernovak: its objectively so funny that people had this S-1 for weeks and all anyone could talk about was the company being cooked because of the fake accounting losses. These are the people telling the common 
   > @ekmokaya: They really worked hard to make Anthropic IPO-ready. — Positive adjusted operating income in H1 2026. — Positive GAAP operating income in Q2 2026. — Positive operating cash flow in H1 2026. $ANT
   > @packym: mamma mia that's a lotta compute
   Also: Business Insider, Fortune, CryptoPotato, Financial Post

6. S-1: Anthropic outlines its mission to revolutionize sectors like medicine and warns its corporate behavior may diverge from traditional profit-maximization
   Robert Hart / The Verge — https://www.theverge.com/ai-artificial-intelligence/1018476/anthropic-ipo-details-s1-filed-sec
   The company said it plans to list on the Nasdaq exchange under the ticker ‘ANT.’ — Anthropic has filed its S-1 prospectus …
   > @oscarwgrut: Anthropic tells investors not to think of its IPO “in purely transactional terms” “The advent of machine intelligence is one of the seminal moments in human history. Our aim is to help humankind chart
   > @saranormous: CONGRATS Anthropic on their S-1 filing! Unsurprising, but first observations: inflection in operating profit, strong emphasis on novel discovery/bio, mismatch b/w consumption based revenue and long te
   > @matthewstoller: Anthropic's S-1 claims it will be run by an “independent body of financially disinterested trustees with expertise in AI safety, national security, public policy, and social enterprise.” These are of 
   > @scaling01: Anthropic says they have recently delayed the pre-training of a new frontier model
   > @thestalwart: Kind of an interesting stat from the S-1. Don't fully know what to make of it
   Also: TechCrunch, Bloomberg, Hindustan Times, CoinDesk, CNN, The Independent, Yahoo Finance, Straight Arrow, +4 more

7. Sources: Anthropic is aiming to go public the week of November 16 and could raise ~$100B at a $1.5T to $2T valuation, after initially preparing for October
   Wall Street Journal — https://www.wsj.com/tech/anthropic-unveils-paperwork-for-blockbuster-ipo-291a684b?st=sUdaw6&reflink=desktopwebshare_permalink
   Also: NPR, The San Francisco Standard, Washington Examiner, Yahoo Finance, Newser

8. S-1: Anthropic warns prospective investors that its AI safety and advocacy stances risk disproportionate and selective targeting from the Trump administration
   Maria Curi / Axios — https://www.axios.com/2026/10/26/anthropic-trump-ai-safety-ipo-risks
   > @m_ccuri: NEW: Anthropic is telling investors it could be singled out for government retaliation over its AI safety positions — and it has no plans to back down. https://www.axios.com/...

9. Anthropic S-1: post-IPO governance will retain Public Benefit Corporation status, giving its seven co-founders 50.1% voting control via a single Class F share
   Deborah Mary Sophia / Reuters — https://www.reuters.com/legal/litigation/anthropics-ipo-close-look-ai-frontrunners-rapid-growth-spiraling-costs-2026-10-26/
   > @nmasc_: Anthropic discloses only one venture capitalist in its S-1 filing: 37-year-old Yasmin Razavi. The Spark Capital GP is also the only VC backer who holds a board director seat. https://www.bloomberg.com
   > @teddyschleifer: Anthropic cap-table, kinda sorta
   > @mihonarium: Anthropic can at any point dissolve the Long-Term Benefit Trust.
   > @zerohedge: ANTHROPIC: TO ISSUE SINGLE SHARE OF CLASS F COMMON STOCK TO LIMITED LIABILITY CO ORGANIZED BY CO-FOUNDERS, “FOUNDER LLC” ANTHROPIC: OUR CLASS F COMMON STOCK WILL NOT HAVE ANY ECONOMIC RIGHTS ANTHROPIC
   > @briansozzi: Anthropic will be a tightly controlled public company:
   Also: Reuters, Motley Fool

10. Apple unveils a redesigned iPad mini with an 8.5-inch OLED display, an A20 Pro, 24% thinner bezels, and a nano-texture finish option, for $699+ from November 6
   Apple — https://www.apple.com/newsroom/2026/10/apple-gives-ipad-mini-its-biggest-update-ever/
   Featuring a stunning OLED display in an even thinner and lighter design, a huge leap in performance, faster wireless connectivity, and water and dust resistance
   > @markgurman: When Apple holds events on Wednesdays, it increasingly does so following three days of announcements. OLED iPad mini today, M6 iMac and MacBook Pro on Tuesday and touch MacBook Pro on Wednesday would 
   > @gregjoz: It's going to be an exciting week, and it starts with our all-new iPad mini. Thinner and lighter than ever, with an OLED display, water and dust resistance, better audio, powered by A20 Pro... it's th
   > @stevemoser: iPad Mini: A20 Pro and Pro-level price ($699 for 128GB) but no Promotion? I guess we are in for a week of an Apple product announcement a day. Is this the first time Apple hasn't started pre-orders at
   > @autismcapital: New OLED iPad mini just dropped but how is it 2026 and Apple is releasing a 60Hz refresh rate iPad? Prices are 128gb $699, 256 $799, 512 $899, they also have a cellular option. This is basically just 
   > @rsgnl: While the lack of 120Hz support will disappoint those who were hoping for that, the iPad mini still received a huge upgrade today, with at least a dozen new features and changes.
   Also: Apple on YouTube, MacRumors, HotHardware, How-To Geek, 9to5Mac, TechCrunch, PCMag, Macworld, +29 more

11. Meta plans to raise $95B to finance its AI infrastructure, including $35B in public equity offerings, backed by cornerstone investors Nvidia, AMD, and Broadcom
   Tim Bradshaw / Financial Times — https://www.ft.com/content/94e5a0ae-874d-447a-bbfc-cd465a1a7555
   Chipmakers Nvidia, AMD and Broadcom will act as cornerstone investors — Meta is planning to raise $95bn …
   > @zerohedge: Here is what META is selling: $22.5 billion of Class A common stock, sold through forward sale agreements with Morgan Stanley and Goldman (plus a $3.375 billion greenshoe). Meta gets no cash up front,
   Also: Meta, Wall Street Journal, CNBC, Investor's Business Daily, The Information, Reuters, Reuters, Capital Brief, +17 more

12. iPhone Duo teardown: 5/10 repairability, a foldable record, but some screens crack along the fold, possibly because a hinge support bar fails to drop far enough
   Elizabeth Chamberlain / iFixit News — https://www.ifixit.com/News/119895/iphone-duo-teardown
   Apple's folding iPhone finally made it to our teardown table. Some owners' screens didn't make it through setup.
   > @workaholicdavid: iPhone Duo only lasted for 75,000 folds before catastrophically failing. This is just embarrassing for a Foldable phone. Not to mention the fact that Galaxy Z Fold8 is rated for 200,000 Folds. Honor M
   > @jmwilt21: Posts like these are exactly why I'm not just going to believe every broken iPhone Duo post out there. Too many people will just lie for clout.
   > @jmwilt21: We are going to keep spreading these useless tests then? Literally means nothing.
   > @zacksjerryrig: @contractorsPOV @SentientCT woah - dont get mad at me for showing Apples hinge lets sand inside. you should be mad at apple for allowing sand to get inside. weird. Don't shoot the messenger.
   > @podawful: what the fuck, i paid $2K for this piece of shit and I can't even bend it backwards and light it on fire
   Also: iFixit on YouTube, Engadget, 9to5Google, CNET, The Register, HotHardware, JerryRigEverything on YouTube, Forbes, +32 more

13. Inside Slack's Salesforce culture clash: Benioff didn't use Slack and had ~1 hour with CEO Butterfield pre-deal; Butterfield quit after a Davos will.i.am panel
   Johnny Rodgers / Building Slack — https://buildingslack.com/salesforce-part-two/
   I needed a keyboard. — I stood at my reserved desk on the 7th floor of Salesforce's tower in Vancouver around 9am.
   > @marcosluis2186: It's just sad to read this https://buildingslack.com/... Now I understand more about why Stewart left the company just 18 months after the acquisition. Is this the “Ohana” they brag about?
   > @briannekimmel: This is an excellent example of how to document company lore. The Slack story is a compelling illustration of a startup with clear values getting absorbed by a massive corporate machine. It's a wild r
   > @shpigford: what a sad read. :(
   > @shawnchittle: Great read on Slack being bought by Salesforce. I was a “Slacktavist” going as far to tell companies wanting to hire me, no Slack, no Shawn. I tried to get it deployed at NASA to break down silos. The
   > @thedealdirector: Imagine struggling to grasp the basics of Slack's sales motion and value prop. Never change, Salesforce.

14. Elon Musk says SpaceX closed $40B in GPU debt, debt markets have shut off credit for AI data center companies, and 200+ neoclouds face “death and consolidation”
   Elon Musk / @elonmusk — https://x.com/elonmusk/status/2114434646914068862
   Pretty much. As of the past few weeks, debt markets have almost entirely shut off access to money for any company that doesn't have substantial revenue independent of AI data centers. SpaceX closed $4
   > @elonmusk: This is primarily callable debt for GPU purchases that will arrive in Q1 and Q2. Not a major factor this quarter.
   > @chamath: As someone with a portfolio of energized land assets here is what I am seeing: ...it does look like there will be a lot of partially stranded compute and compute sitting in inventory in 2027 than is c
   > @dowdedward: If you are wondering why semiconductors peaked in June this is the reason...the market sniffed out that incremental demand was coming from a debt fueled unprofitable speculative sector. Neo clouds. [e
   > @adam_tooze: Guppy-level death and consolidation: Did Elon just call it?
   > @jiahanjimliu: Putting Together What @elonmusk is Saying/Doing AI Demand 1. Just yesterday, Elon said …
   Also: CNBC, Barron's Online, Finimize, Semafor, CoinDesk, New York Times, Bloomberg, Yahoo Finance, +8 more

15. SpaceX agrees to a ~$40B equipment finance lease with Apollo to fund purchases of Nvidia GPUs for its AI initiatives, set to close before the end of 2026
   Carmen Arroyo / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-26/spacex-agrees-to-40-billion-chip-financing-deal-with-apollo
   Also: Proactive, Dow Jones Newswires, NewsMax.com, CoinGape, Telecompaper, Pulse 2.0, RuntimeWire, Fox Business

16. A look at OpenAI's and Anthropic's aggressive price cuts from June through September, driven by low switching costs and pricing pressure from open-weight models
   Max Woolf's Blog — https://minimaxir.com/2026/10/cheap-llms/
   Let's look at a quick timeline of the major LLM model announcements from both OpenAI and Anthropic over the past few months.
   > @minimaxir: New blog post up: if you've been paying close attention to LLM prices, you may have noticed that they have dropped *significantly* over the past few months, which is not what I expected. https://minim
   Also: The Decoder, The Neuron

17. A look at TSMC's first plant in Phoenix that has achieved chip output rates comparable to its Taiwan facilities, as its Taiwanese engineers teach US workers
   New York Times — https://www.nytimes.com/2026/10/23/opinion/ai-computer-chips-semiconductor-arizona-industry.html?unlocked_article_code=1.LVE.T4pO.KW_xY6NbyH_s&smid=nytcore-ios-share
   On July 5 the Northwest Chinese Baptist Church in Phoenix opened its weekly Mandarin service with a verse from the Old Testament.
   > @danwwang: I went to Phoenix to spend time with the Taiwanese community. TSMC will invest $265 billion and send thousands of engineers and their families, which marvel at their new lives in the Sunbelt My first 
   > @thomasgalvin: “TSMC's July announcement to... raise total investment to $265 billion is an obvious sign of confidence in Arizona's operations.” Compelling piece by @danwwang on why TSMC Factory here in @MaricopaCou
   > @jonasnahm: 1/ Dan Wang's NYT essay on TSMC's Arizona plant argues that TSMC is doing for America what Apple did for China. But the analogy rests on two assumptions and it's not clear that either one of them is h
   > @alecmacgillis: Striking detail in the big NYT piece on Taiwanese families adjusting to working at the huge new TSMC chip plant in Arizona: their surprise at the lack of rigor in US schools.
   > @patrickmcgee_: I, too, think TSMC Arizona is wildly important for America. Great article from @danwwang — “ TSMC is doing for America what Apple did for China” https://www.nytimes.com/... [image]
   Also: Politico

18. Elvis Presley's music owners sue Anthropic for allegedly using 274 songs to train its models, seeking $41M+; Anthropic says it disagrees and will defend itself
   Derrick Bryson Taylor / New York Times — https://www.nytimes.com/2026/10/25/arts/music/anthropic-lawsuit-elvis-presley-songs.html?unlocked_article_code=1.LVE.Unk9.7e04-FAQ9Ei8&smid=nytcore-ios-share
   The $41 million lawsuit contends that the A.I. company used Presley's music to train its models without permission.
   Also: The Guardian, Engadget, Music Ally, Mercury News, NBC News, Los Angeles Times, Digital Music News, Newser

19. The public internet model is dying from too much content, algorithmic aggregators, and vulnerabilities found with AI, and that may bring new possibilities
   Ben Thompson / Stratechery — https://stratechery.com/2026/the-end-of-the-internet/
   It was the summer of 2003, just weeks before I was set to move to Taiwan, that I decided to create a blog to document my journey.
   > @erskingardner: At @whitenoisechat, we agree with @benthompson's latest piece. https://stratechery.com/...
   > @stratechery: The End of the Internet The old Internet, where anyone could host a server is over, but it's just the final blow in an ending that has been coming for years. The future, though, is brighter than it ap

20. Modern AI panic reflects “cognitive mercantilism”, a zero-sum worldview where intelligence is a scarce, dangerous supply-side resource that elites must manage
   Venkatesh Rao / Contraptions — https://contraptions.venkateshrao.com/p/cognitive-mercantilism
   The promise—and challenges—of agentic software engineering, from large-scale code migration to language modernization.
   > @clairlemon: Fantastic piece https://contraptions.venkateshrao.com/ ... [image]
   > @aviel: The best, most comprehensive take on AI I've read. After a year of confusion and fear about the future, I finished it feeling like a weight had physically lifted. It's long. Make the time. @vgr is und

21. Google DeepMind's AI hurricane forecasting model outperformed conventional models by accurately predicting that Hurricane Isaias would make landfall in Florida
   Jessica Meszaros / NPR — https://www.npr.org/2026/10/26/nx-s1-6012820/ai-hurricane-forecast-google-deepmind-isaias

22. California startups have raised a record $385B across seed to growth rounds so far in 2026, or 75%+ of all US startup funding; early and seed stage raised ~$62B
   Joanna Glasner / Crunchbase News — https://news.crunchbase.com/venture/california-startups-most-us-funding-2026-openai-anthropic/

23. Ray-Ban Meta Audio glasses review: no camera is a bonus for some, good audio quality, and Meta AI works well, but lingering privacy concerns and fairly pricey
   Samantha Kelly / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-25/ray-ban-meta-audio-ai-glasses-cost-more-while-ditching-a-key-feature-review
   Also: Wired

24. Volkswagen's China unit and Xpeng secure approvals to trial autonomous driving systems on public roads in China; VW is testing Level 3 and Xpeng Level 4
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-26/china-boosts-self-driving-push-with-vw-xpeng-technology-trials
   Also: CnEVPost

25. Filing: Chinese PCB maker Dongshan raised ~$1.3B in Hong Kong's biggest IPO in nearly two months, pricing shares at ~$11, or 35% below its Friday Shenzhen close
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-25/chinese-manufacturer-dongshan-raises-1-3-billion-in-hk-listing

26. Alphabet, Amazon, and Microsoft are expected to report double-digit gains in revenue this week, as investors grow impatient with AI capex and seek returns
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-25/ai-spending-fears-threaten-to-swamp-big-tech-s-strong-earnings
   > @jedimarkus77: I did not realize $MU has exceeded $NVDA https://www.wsj.com/... [image]
   > @adisurreyenergy: Here's another way the U.S. stock market has come to depend on a handful of companies tied to the AI trade Ten companies—including Nvidia, Micron and other AI giants—account for roughly two-thirds of 
   > @divajain2: Nvidia and Micron account for 34% of the S&P 500's expected Q3 earnings growth. 500 companies. Two doing a third of the work. Diversification :) https://www.wsj.com/...
   Also: The Daily Upside, Proactive, 24/7 Wall St., Yahoo Finance, Barron's Online, Motley Fool

27. A profile of former Google VP and Yahoo CEO Marissa Mayer, whose startup Dazzle is building an AI assistant to help normal people tackle mundane tasks visually
   Alexandra Alter / New York Times — https://www.nytimes.com/2026/10/25/style/marissa-mayer-ai-assistants-women.html?unlocked_article_code=1.LVE.bUTq.yuaOciiPS1zl&smid=url-share
   > @triketora: generously, this sounds like a made-up story by someone who is terrible at storytelling
   > @hecubian_devil: At our current pace, life will genuinely not be worth living in about 10 years.
   > @cdegentry: @yashar I could give you 3 things for each of my 3 children that makes them unique in under 5 minutes. Because I tell them each what makes them special on a frequent basis.
   > @coleleiter: They could not waterboard this out of me.
   > @clarkle119: Deeply disturbing. I'm increasingly unsettled by the questions people are asking AI. It absolutely boggles my mind when people ask AI *ethics* questions and think it's fine because it's in a business 
   Also: TMZ.com, The Verge, The Independent, Daily Mail

28. India's chip design startups near production with government support, but low volumes, high fab costs, and supply chain bottlenecks hinder commercialization
   Ananta Agarwal / Nikkei Asia — https://asia.nikkei.com/business/tech/semiconductors/india-s-chip-design-startups-struggle-with-final-commercial-hurdle

29. Amazon Bee Frontier review: a simple $75 AI wearable that excels at always-on listening, summarizing conversations, and suggesting follow-up actions
   M.G. Siegler / Spyglass — https://spyglass.org/amazon-bee/

30. A look at Toyota's robotics expansion, including its Walden spinoff and a $6.4B annual plan to deploy 400K factory robots, as it competes with Tesla and China
   Financial Times — https://www.ft.com/content/8bf93407-6b93-4ebb-b54b-f290ebd563e3

31. DongA Ilbo: SK Hynix gained ~$15B on its Kioxia stake earlier in 2026, and plans to return ~$12B to shareholders via a special dividend
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-25/sk-hynix-plans-12-billion-dividend-from-kioxia-gains-report
   Also: Reuters

32. High-frequency trading firms such as Jane Street are investing in AI and chip startups and neoclouds, and building data centers to gain an edge in the AI era
   Bloomberg — https://www.bloomberg.com/news/features/2026-10-22/jane-street-hrt-are-spending-billions-to-win-in-ai-era?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5Mjg5ODcyMSwiZXhwIjoxNzkzNTAzNTIxLCJhcnRpY2xlSWQiOiJUTkJVQ0RLSUpIOTIwMCIsImJjb25uZWN0SWQiOiIwNEFGQkMxQkYyMTA0NUVEODg3MzQxQkQwQzIyNzRBMCJ9.aZUQTESNPxDFkB9tAjev0zQuyASx2W5Ed0a-yabw_WY
   > @justinaknope: For years, high-frequency trading firms fought over every nanosecond in a battle to be the fastest. Now they're fighting for compute — building data centers and investing in AI infrastructure startups
   > @business: To keep up with rivals, Wall Street's high-frequency traders have few options but to join the race for AI computing power. Despite billions in investments, success is not guaranteed. Read The Big Take
   Also: The Decoder

33. Sources detail how Ramp investors Joe Lonsdale and Keith Rabois pushed US lawmakers to probe rival Airwallex's China ties after Airwallex scrapped a Ramp deal
   Michael Roddan / The Information — https://www.theinformation.com/articles/ramp-investors-went-nuclear-airwallex-doomed-deal
   > @leomschwartz: Fun story by the great @MichaelRoddan on the Ramp-Airwallex feud, including a failed partnership and Airwallex's new Trump world lobbyist. Who said spend management can't be entertaining: https://www.

34. Moderators of r/opensource ban submissions of projects using, made by, or intended for AI, exclude non-English speakers over AI translation concerns, and more
   Terrence O'Brien / The Verge — https://www.theverge.com/ai-artificial-intelligence/1018217/reddit-opensource-ai-ban
   > @reddit_lies: R/opensource moderators go full retard and push out oppressive rules for what can be posted to their sub. 1: no AI contributed projects 2: only multiple contributor projects 3: must have an existing c
   > @timsweeneyepic: @LundukeJournal Redditors.
   > @mvanhorn: Ngmi
   > @hesamation: this is just ABSURD. they have completely lost sight of what the “OPEN” part is supposed to mean. open source was built on freedom to create and share, not on policing the tools people use. this is ga
   > @catatfire: @chasmmmmmmmmmmm AI shit aside this will age like fucking milk mostly for this reason
   Also: Tom's Hardware, Gizmodo, Help Net Security, Kotaku

35. Data center tenants now demand $5M+ per day in late-delivery fees, up from $1M in spring 2026, spawning new “delay-in-delivery” coverage from brokers like Marsh
   Ann Davis Vaughan / The Information — https://www.theinformation.com/articles/data-center-late-fees-hit-5-million-per-day-spawning-new-insurance
   > @choblin29: AI data center tenants are now demanding late-delivery penalties exceeding $5 million a day, up from $1 million this spring, according to The Information. Insurance broker Marsh has developed new cove
   > @stocksavvyshay: Data center developers are now facing over $5M in daily penalties for delays with KKR warning that late fees could bankrupt more builders than rising interest rates. That lines up with what $SPCX Elon

36. The iTunes Store is re-emerging as a venue for pop stars, like Taylor Swift, to hawk collectibles to superfans, reach new audiences, and bolster chart positions
   Tom Matsuda / Financial Times — https://www.ft.com/content/5a21a7fe-3929-4e11-b571-8ce4bfd778ec?accessToken=zwAAAaFxOz_Wkc9aIaf-OSlOEdO1cYzkv9d47A.MEYCIQDRs1kzjWFXImamrm3ktUUwHRNGP9pjk8vLbabih2luXQIhAJQ5-ZFBptzq0jHKh6HmB61eNgYePpLRa5dmLIckcTF2&sharetype=gift&token=d03f3ab2-b10b-4279-adea-2a9c009b105b
   > @spoonybear: I loved being interviewed by one of my favourite papers. This piece in today's Financial Times is about iTunes nostalgia, souvenir collecting, and back to the future fandom. https://www.ft.com/...
   Also: 9to5Mac, Music Ally
