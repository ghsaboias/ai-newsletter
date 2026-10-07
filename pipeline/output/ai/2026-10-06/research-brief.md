# Research — News Cluster

Search for news **events that occurred** between **2026-10-05 10:00 BRT** and **2026-10-06 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-05 10:00 BRT to 2026-10-06 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-06
**Research window:** 2026-10-05 10:00 BRT → 2026-10-06 10:00 BRT

**Previous edition headlines (2026-10-05 — skip unless genuinely new development):**
- trump-super-intelligence-force-clayton-ai-czar: Trump creates 'Super Intelligence Force' led by DNI Jay Clayton to coordinate US AI policy
- altman-accept-bad-things-anthropic-religious-force: Altman says world 'should accept some bad things' from AI, jabs Anthropic over 'religious force'
- openai-chatgpt-visual-ads-image-generation: OpenAI to test visual ads in ChatGPT during image generation in the US later in October
- aleph-alpha-kolibri-78b-open-weight-sovereign-model: Aleph Alpha releases Kolibri, a 78B open-weight German-English model under Apache 2.0
- reflection-ai-first-open-weight-model-western-wave: Axios: Nvidia-backed Reflection AI readies first open-weight model as Western labs plan October releases
- kyoto-vision-golden-age-science-superintelligence: US and 16 countries endorse 'Kyoto Vision' to harness AI for autonomous scientific discovery
- iwf-ai-csam-h1-2026-exceeds-all-2025: IWF: AI-generated child abuse images in H1 2026 already 40% above all of 2025
- huawei-qualcomm-cross-license-5g-ai-patents: Qualcomm signs first 5G cross-license with Huawei and buys some of its US AI and compute patents
- musk-confirms-tsmc-terafab-talks: Musk confirms early talks with TSMC to build and run his Terafab chip plant in Texas
- schneider-electric-acquires-ptc-23-7b: Schneider Electric agrees to buy PTC for $23.7B in cash, its largest acquisition
- firmus-ipo-half-to-existing-investors-oversubscribed: Nvidia-backed Firmus to give half of up to $5.5B IPO to existing backers as demand exceeds offer
- groq-engineers-sue-board-nvidia-20b-deal: Former Groq engineers sue its board, say Nvidia's $20B license deal shortchanged shareholders
- robco-unicorn-40m-secondary-sale: German robot-arm maker RobCo tops $1B valuation in $40M share sale, double January's mark
- oracle-point-beach-nuclear-project-lighthouse: Oracle to take 10-20% of Wisconsin nuclear plant's output for OpenAI data center campus
- brazil-election-flavio-bolsonaro-leads-lula-runoff-markets-rally: Flávio Bolsonaro edges Lula 47% to 45% in Brazil's first round; runoff Oct 25, markets rally
- iran-hormuz-tankers-struck-houthis-hit-saudi-aramco-us-bombers-leave-uk: Tankers hit in Hormuz, Houthis strike Saudi oil sites as Iran-US talks stall
- russia-intensify-kyiv-strikes-merz-1-3b-package-trilateral-talks: Russia vows to intensify Kyiv strikes as Merz brings €1.3B aid and Zelensky backs October talks
- g7-100m-barrel-release-opec-plus-holds-november-output: G7 orders 100M-barrel oil and diesel release; OPEC+ holds November output with Brent above $100
- shionogi-intrabio-2b-ge-healthcare-sofie-945m: Shionogi buys rare-disease biotech IntraBio for $2B; GE HealthCare buys Sofie for $945M
- okxice-sec-notice-24-7-tokenized-us-stocks: OKX-ICE venture notifies SEC it will run a 24/7 tokenized-stock venue for 63 US shares

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 35 stories

1. Sources: DeepSeek is close to raising $12B+ in a round that could hit ~$14.9B, with Tencent and CATL among the biggest contributors, ahead of an early-2027 IPO
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-06/deepseek-to-raise-at-least-12-billion-in-tencent-backed-funding
   DeepSeek is close to securing at least 80 billion yuan ($12 billion) in its latest round of funding, blowing past …
   > @jukan05: BBG: DeepSeek has secured at least $12 billion in a funding round, with the final amount potentially approaching RMB 100 billion. BBG: DeepSeek is targeting an IPO in early 2027.
   > @teortaxestex: NICE That's more like it, another $7.4B (with $3B from Liang) would have been embarrassing. They need high hundreds of megawatts of capacity. Will be hard even like this, but I can only hope they'll p
   > @zephyr_z9: Whale has around $20B in cash
   > @jenzhuscott: With $12bn in the bag, DeepSeek will complete open-source programming tools like TileLang + kernel libraries (such as DeepGEMM Ascend) to create a viable alternative to Nvidia's CUDA ecosystem for Hua
   Also: PYMNTS.com, Quartz, New York Times, CoinDesk, The Decoder, CTech, China Money Network, The Straits Times, +4 more

2. Sources: Moonshot AI has closed its final private funding round at a ~$50B valuation and is targeting a Hong Kong IPO in Q1 2027 to raise up to $5B
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-06/moonshot-said-to-eye-early-2027-ipo-after-value-hits-50-billion
   Moonshot AI has closed the final round of private fundraising at a valuation of about $50 billion and is heading toward an initial public offering …
   Also: Quartz, Silicon Republic, Bitcoin Insider, CTech, Euronews, Seoul Economic Daily, Tech in Asia

3. NYC-based Reflection unveils Beam, an open model it says rivals GLM-5.2 on reasoning while using 3x-4x less compute and approaches Qwen3.8-Max on agentic tasks
   Semafor — https://www.semafor.com/article/10/05/2026/reflection-ai-unveils-an-open-source-answer-to-chinese-labs
   Reflection AI, the startup billing itself as America's answer to open-source Chinese AI, is releasing its first model, called Beam.
   > @mishalaskin: AI is both foundational as a science and a technology, and the safest way that also ensures the benefits of AI are distributed evenly is by making it open. I'm excited for what developers and scientis
   > @artificialanlys: Artificial Analysis has been given access by Reflection and is independently benchmarking Beam Early indicators suggest Beam will be one of the most token-efficient open models we've seen for its leve
   > @real_ioannis: Today, we're introducing Beam, Reflection's first model. A year ago, we set out to build a frontier open model before we had much of the team or infrastructure required to do it. Since then, Reflectio
   > @reflection_ai: Introducing Beam: a highly efficient agentic open model with 501B total parameters and 23B active. - Frontier reasoning efficiency - Advances the Western open frontier on coding & agentic tasks - Trai
   > @nayshins: 8 months ago I joined Reflection to build a frontier western open weight model. Today we're releasing Beam (501B total, 23B active with an Apache 2.0 license). I worked in many roles over this time, b
   Also: Reflection, The Hill, The Decoder, Quartz, The Neuron, Financial Times, Sources, TechCrunch, +10 more

4. Analysis: for agentic workloads, Anthropic's plans with Claude Opus 5.5 offer ~5x more API-equivalent value per month than OpenAI's plans with GPT-6.1 Sol
   SemiAnalysis — https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x
   Limit testing every AI subscription plan from Anthropic, OpenAI, Meta, SpaceXAI, MiniMax, Moonshot, Z.ai, Cursor, and Cognition
   > @stalkermustang: This plot explains why OpenAI had to close $200 subs and why the quota gets cut. Anthropic is dedicating 42% of inference compute to subs, which generate 10% of revenue (10% of $70B ARR is ~$583M/mo).
   > @morqon: leaving out token efficiency kind of undermines the analysis, you'd think
   > @synthwavedd: Pssst - I heard Anthropic are planning a price cut for Fable 5.5 ;3 Anyway, here's the article - https://newsletter.semianalysis.com/ ...
   > @synthwavedd: As suspected, Anthropic's subscriptions offer over 5X the value of OpenAI's (vs the equivalent API pricing) when using mid-tier models OpenAI offers very slightly more usage of Astra vs Anthropic's Fa
   > @kimmonismus: Holy sh*t, Anthropic's subscriptions offer so much more value, even compared to the new and efficient GPT-6.1 Sol. It's not even close. SemiAnalysis puts Opus 5.5 at over 5x the API-equivalent value o
   Also: Implicator.ai

5. Ofcom opens an OSA investigation into Meta over Instagram Instants in the UK; Meta says it “briefed Ofcom about this feature” several times before its May debut
   Reuters — https://www.reuters.com/business/uk-probes-meta-over-safety-risks-of-instagram-instants-feature-2026-10-06/
   Britain's communications regulator said on Tuesday it has opened an investigation into whether Meta Platforms …
   Also: Ofcom, The Guardian, Reuters, BBC, Neowin, PetaPixel, LBC, Silicon UK, +3 more

6. UK retailer Asos falls 10%+ after customers received app notifications saying “we have fully compromised the Snowflake instance”; source: Asos is investigating
    — https://www.ft.com/content/eab7052d-6640-4928-a128-8df73455ba0a
   Shares in FTSE 250 retailer fall more than 10% following reports from mobile users
   > @danbarker: Imagine if today was your start date on this job at ASOS. Someone comes to interrupt your onboarding session: 'um - are you the new DPO? There's been a message for you...'
   > @digitaljobs: Looking for a new challenge? ASOS are currently hiring for someone to act as ‘Data Protection Officer’... https://www.digitaljobs.com/ ...
   > @mattrsalisbury: Anyone else get the ASOS hacked notification? Any ideas?
   > @alexmartin: ASOS is looking like a really unusual incident. The push notification included a link to a Telegram account which says payment information hasn't been affected. No explicit extortion demand or motivat
   > @intcyberdigest: ‼️ BREAKING: ASOS was hacked and customers received a ransom note meant for ASOS, pushed through the app. Titled “ASOS HACKED”, it tells the company's data protection officer and IT team that attacker
   Also: BBC, The Register, The Guardian, TechRadar, Infosecurity, Quartz, Channel NewsAsia, ITPro, +8 more

7. TikTok debuts Shopping Assistant, a conversational AI agent that helps users find and buy products, and Buy Direct for one-click purchases from the For You feed
   Aisha Malik / TechCrunch — https://techcrunch.com/2026/10/05/tiktok-rolls-out-an-ai-shopping-assistant-and-one-click-checkout/
   TikTok announced Monday that it's launching an AI shopping assistant and a new in-app checkout feature that lets users buy directly from brands.
   Also: TikTok, Music Ally, Net Influencer, Social Media Today

8. Sources: the FBI removes an Accenture contractor over a breach exposing thousands of employees' data; the FBI says a contractor failed to apply a security patch
   Reuters — https://www.reuters.com/technology/accenture-contractor-removed-fbi-following-damaging-data-breach-sources-say-2026-10-06/
   The Federal Bureau of Investigation removed an Accenture contractor on Monday over their role in a damaging data breach …
   Also: Security Affairs, CIO.com, Cyber Security News, CSO, Political.org, The Hacker News

9. ChatGPT is not only using New Yorker cartoonists' style but also adding their signatures to the fake cartoons it creates, which have gone viral on social media
   Andrew Deck / Nieman Lab — https://www.niemanlab.org/2026/10/chatgpt-is-adding-real-cartoonists-signatures-to-fake-new-yorker-cartoons/
   OpenAI's chatbot isn't just imitating the magazine's style. It's also falsely attributing AI-generated images to real artists.
   Also: The A.V. Club

10. South Korean officials are probing whether AI agents were used in recent bank hacks, after President Lee Jae Myung said “signs” suggest AI models were involved
   New York Times — https://www.nytimes.com/2026/10/06/world/asia/south-korea-banks-hacked-ai.html?unlocked_article_code=1.GlE.a6yQ.6rGaxfIHN0Bc&smid=bs-share
   The president said there were signs that such models were used in recent attacks on several banks involving customer data.
   Also: Tom's Hardware, Quartz, Wall Street Journal, Financial Times, IJR News, Kyodo News, Reuters, Political.org

11. Sources: Kuaishou's Kling has picked banks to lead a Hong Kong IPO aiming to raise $1B+ as soon as 2027; Kling hit a ~$15B valuation after raising $2.8B in July
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-06/china-ai-video-startup-kling-picks-banks-for-1-billion-plus-ipo
   By continuing, I agree to the Privacy Policy and Terms of Service. … Explainers
   Also: The Information

12. Sources: Meta and Microsoft are working to cut internal Claude use; Meta employees using Claude Code dropped to ~30,000 from ~60,000 earlier in 2026
   The Information — https://www.theinformation.com/articles/meta-microsoft-work-wean-staff-anthropics-claude
   Meta Platforms and Microsoft, two of Anthropic's biggest corporate customers, are working to cut their employees' use of Claude …
   > @kimmonismus: Meta and Microsoft are reportedly cutting employees' Claude usage to reduce costs (and push their own AI tools.) The Information reports that Microsoft cut its projected annual spending on internal An
   > @dratchcap: Meta too. And yet, bc compute is super tight, any freed up finds a home instantly....Lab rev is capacity gated. And the preponderance of evidence suggests there's no spare token production dying for h
   > @edzitron: Ed Zitron (@edzitron) on X
   > @hesamation: NEW: Microsoft and Meta, two of Anthropic's MAJOR customers, are working to cut employee usage of Claude models. the reason: cost. Claude bills are exploding and they're pushing their own tools. Micro
   > @jessicalessin: Getting a lot of questions this morning from investors asking if we have even more detail like this. New: Microsoft lowered its internal claude spending projections by 1/3 and Meta cut the number of e
   Also: Cyber Security News, The Decoder, PYMNTS.com, DigiTimes

13. OpenAI says it will add text watermarking for ChatGPT and Codex users in the EU to comply with the EU AI Act, and an opt-in setting for API customers globally
   OpenAI — https://openai.com/index/eu-text-provenance
   - Starting today, API customers globally will be able to opt in to text watermarking for select models.
   > @openai: We're expanding our approach to content provenance to include text in response to EU regulatory requirements, while recognizing the significant limitations of current text watermarking technology. Our
   > @kimmonismus: OpenAI will start changing ChatGPT's word choices in the EU to make its text detectable, and I don't like this direction. Over the coming weeks, ChatGPT and Codex outputs will receive invisible text w
   > @kunchenguid: looks like the watermarks are here to stay.. i have mixed feeling about this on one hand, i don't let LLM write any of my content, and i hate all the bot replies. i wish we have a solution to kill the
   > @max_spero_: OpenAI's watermarking technical report is out. One thing that stands out to me is that they evaluate it at a target false positive rate of ~1%! That's surprisingly high for what some would assume to b
   > @eurofounder: This is the proof that big AI labs cannot move their finger without the explicit EU approval Another big win for Europe
   Also: The Register, Tech Times, The Verge, OpenAI, BleepingComputer, Gizmodo, The Independent, SammyGuru, +23 more

14. Sources: Seagate and Toshiba are bidding for TDK's HDD magnetic head business in a multibillion-dollar deal, as they compete for AI data center storage demand
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-06/seagate-is-said-to-battle-toshiba-for-tdk-s-hard-drive-head-unit
   Seagate Technology Holdings Plc and Toshiba Corp. are locked in a contest for TDK Corp.'s magnetic-heads business for hard-disk drives …
   > @jukan05: Seagate cannot afford to let this fall into Toshiba's hands under any circumstances. If Toshiba acquires it, it will see tremendous growth, just as Micron did after acquiring Elpida. [image] [embedded
   Also: Barron's Online, Dow Jones Newswires, Investor's Business Daily

15. Analysis: insurers brace for multimillion-dollar claims caused by rogue AI agents, amid concern that Sam Altman, Dario Amodei, and others could be held liable
   Lee Harris / Financial Times — https://www.ft.com/content/a5caf8d4-992f-4832-89c3-6c73f6f111fe?accessToken=zwAAAaGnEvNukdOlyvjUmS9IMtOJw2xz9vER_gE.MEUCIC26ZqjN6sLwpwEYeTXFDMLeRsl791eP3rx-wumAiht-AiEAyYXcp5pW6YvG3IJriGwttg1X96Y7ufTirN5WmE1fqw0&segmentId=7d4bcc2e-e664-92ba-62e3-5590579f1902
   Insurers and lawyers weigh the cost of potential massive lawsuits and damages against the leaders of OpenAI and Anthropic

16. Study: China is struggling to attract foreign AI talent; for every 30 Chinese AI researchers in the US in 2025, only one in China made the opposite journey
   Zeyi Yang / New York Times — https://www.nytimes.com/2026/10/06/science/in-race-with-us-china-struggles-to-recruit-foreign-ai-researchers.html
   China's booming artificial intelligence sector has given local researchers good reason to remain in the country …
   Also: Carnegie Endowment …

17. At an Australian hearing, OpenAI Chief Strategy Officer Jason Kwon pledged faster safety incident disclosures; Anthropic representatives made similar pledges
   ABC — https://www.abc.net.au/news/2026-10-06/openai-hearing-apology-key-takeaways/107235640
   By national AI reporter Cam Wilson and the Specialist Reporting Team's Miwa Blumer — abc.net.au/news/openai-hearing- apology-key-takeaways/107235640
   Also: Bloomberg, The Guardian, New York Times, Information Age, Quartz, Nikkei Asia, Capacity, DealStreetAsia, +5 more

18. Hadrian, an agentic AI offensive security service, raised $40M co-led by Forgepoint Capital International and SmartFin, taking its total funding to $65M
   Tamara Djurickovic / Tech.eu — https://tech.eu/2026/10/06/hadrian-raises-40m-to-tackle-ai-driven-cyber-threats/
   Hadrian will use the funding to expand across EMEA and the US while growing its engineering and research teams and further developing …
   Also: FinSMEs, The SaaS News, SiliconANGLE, Startup.eu

19. SignSplit, which offers infrastructure to let people digitally sign datasets, likenesses, and creative works, raised $400M from W Group at a $1B valuation
   Mike Wheatley / SiliconANGLE — https://siliconangle.com/2026/10/05/signed-data-pioneer-signsplit-launches-with-400m-to-help-everyone-get-paid-for-their-ai-contributions/
   Few technology companies can help users to protect and monetize their personal data for artificial intelligence as well as SignSplit PBC, it seems.
   Also: SignSplit, The SaaS News, Ventureburn, Pulse 2.0, RuntimeWire, FinSMEs

20. Anthropic's IPO prospectus: Dario Amodei earned $18M in 2025, middle of the pack for tech CEOs, and President Daniela Amodei, his sister, earned $16.4M
   Reuters — https://www.reuters.com/technology/anthropics-amodei-made-18-million-last-year-middle-tech-ceo-pack-2026-10-06/
   Also: CTech

21. Google contracts for 3.6 GW of power from Constellation Energy in the US' largest power grid, with new nuclear energy accounting for ~25% of that supply
   Laila Kearney / Reuters — https://www.reuters.com/business/energy/google-enters-massive-36-gw-power-deal-with-constellation-energy-2026-10-06/
   Also: Wall Street Journal, MarketWatch, Barron's Online, Quartz, Bloomberg, Chicago Tribune, Google, TheEnergyMag

22. Source: Palmer Luckey's Erebor hits $7B+ in deposits since launching in February, including $3B+ over the past quarter with 500+ new customers
   Financial Times — https://www.ft.com/content/42b6fa88-f730-4f8a-a194-8f53d0759aaf?accessToken=zwAAAaEQ8idRkc9CtvqI9zBPitOhlI9T0HWarw.MEQCIFsYyjb4yxfvL3FOYls_oURkUKWBO4D3qWglNfKRlyUkAiAc4ICia43FCLduzE_Ou9i3X6eZQkRTLJXokEIvDatsNw&sharetype=gift&token=78fc5726-2260-4671-8c2d-d26f1fcda068&syn-25a6b1a6=1

23. London- and Paris-based tokenized cash startup Spiko raised a $90M Series B at an $800M valuation, taking its total funding to $120M, and hits ~$2.7B in AUM
   Ryan Weeks / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-06/tokenized-cash-startup-spiko-raises-90-million-to-take-on-us-giants
   Also: The Block, The SaaS News, FinSMEs, FinTech Global, crypto.news, Tech.eu, Startup.eu

24. AMD CEO Lisa Su says the company plans to “substantially increase” supply in 2027 and needs “more advanced wafer capacity”, as she meets Foxconn and TSMC
   Wen-Yee Lee / Reuters — https://www.reuters.com/world/asia-pacific/amd-plans-substantially-increase-supply-2027-ceo-says-2026-10-06/
   Also: Bloomberg, Focus Taiwan, IJR News, Finimize, DigiTimes

25. South Korea plans to launch a ~$3.5B program to develop a frontier AI model starting as early as March 2027 and will open a competition to select participants
   Jie Ye-eun / The Korea Herald — https://www.koreaherald.com/article/10893306
   Also: Reuters

26. Q&A with Senator Adam Schiff on recursive AI becoming a real national security threat, making AI companies retain training data, needing an FDA for AI, and more
   Nilay Patel / The Verge — https://www.theverge.com/podcast/1004286/senator-adam-schiff-ai-trump-regulation-corruption

27. Singapore-based data center operator DayOne files for a US IPO, reporting its H1 revenue more than tripled YoY to $512M while its net loss widened to $77.2M
   Pragyan Kalita / Reuters — https://www.reuters.com/legal/transactional/dayone-data-centers-files-us-ipo-2026-10-05/
   > @zephyr_z9: 🤣🤣🤣🤣🤣 They supply a lot of compute to Chinese players [embedded post]
   Also: Bloomberg, The Straits Times, The Information, Telecompaper, Tech in Asia

28. Sources: AI inference-chip startup Etched is in early talks to raise funding at a $40B to $50B valuation, up from $21B after raising $700M in August
   Marina Temkin / TechCrunch — https://techcrunch.com/2026/10/05/etched-fields-funding-offers-at-40b-valuation-sources-say/
   Also: StrictlyVC

29. SpaceX stock closes up 7.6% after Morgan Stanley called SPCX “cheap”, reaching its highest level since mid-June and returning Elon Musk to trillionaire status
   Lora Kolodny / CNBC — https://www.cnbc.com/2026/10/05/spacex-stock-climbs-highest-since-june-returning-musk-to-trillionaire.html
   Also: Fast Company, Quartz, CoinGape, Dow Jones Newswires, The Crypto Times, Watcher Guru, Gizmodo, NewsMax.com, +11 more

30. Ghost, which makes a $3,499 computer designed for AI agents and includes an RTX Pro 4000 SFF Blackwell GPU, emerges from stealth with an $11M seed led by a16z
   Dominic-Madori Davis / TechCrunch — https://techcrunch.com/2026/10/05/at-19-ghost-founder-raises-11-million-to-build-a-3499-computer-for-your-personal-ai/
   > @ccatalini: Intelligence will come in many forms. Including 100% local. https://x.com/...
   > @ghostai: At Ghost, we are building an ecosystem around personal intelligence you own. The more of your life agents understand, the more capable they will become. But a system with this much access should not l
   > @lucasquan: Zain is the most compelling founder i've ever met. our first convo was a kickoff call. eventually, i was living in his office 4 months ago, i took that call from nyc. @zainmfj had forgone college to b
   > @0xsero: Grateful for the unit. I looked at the stats and the price is very food. NVIDIA RTX PRO 4000 Blackwell, 24 GB GDDR7 64 GB DDR5 RAM 1 TB NVMe SSD 770 AI TOPS 6-core AMD Ryzen 5 7600 3500$, that is real
   > @jamdac: - Be Zain - Start investing at 7 with $100 from your parents - Begin coding at 9 after learning about Jim Simons - Raise a $20k fund at 12 by going door to door in Catskill, NY; outperform the market 
   Also: SiliconANGLE

31. Former Anthropic researcher Jacob Coxon and representatives from Anthropic, Google, OpenAI, and Meta testified at a New York City Council hearing on AI safety
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-05/ex-anthropic-researcher-jacob-coxon-testifies-at-nyc-council-ai-hearing
   > @jessyednews: Councilmember @chiosse also called out the AI execs on their statements made under oath:
   > @cameronwilson: Interesting tweak in language from OpenAI about its hacks ahead of its US exec appearance at a committee today. Last week it apologised for its models doing something that it was “not authorised to”. 
   > @vmmaloney: The @NYCCouncil held a first-in-the-nation hearing to question @claudeai, @openai, @google, and @meta about the societal risks posed by AI. My bill, Int. T2600-2026, would create a private right of ac
   > @cmcarlwilson: @NYCCouncil is hosting a hearing and introducing a package of legislation aimed at regulating AI as it progresses in our city. At a time when the federal government is lacking the oversight and seriou
   > @firesidealpha: Jacob Coxon says he left Anthropic scared of two things: nobody can control AI yet, and next year's models will be able to improve themselves
   Also: India Today, CNBC, Wall Street Journal, Washington Post, Newsweek, The Indian Express, Forkast, Fortune, +20 more

32. The CFTC proposes a federal framework for crypto exchanges to offer retail customers leveraged and margined spot trading, without requiring congressional action
   Jason Shubnell / The Block — https://www.theblock.co/news/markets/2026-10-05-cftc-rulemaking-leveraged-retail-crypto-trading-regulation-ctx-cam-417701
   > @chairmanselig: The lesson from FTX's failure should have been obvious. America shouldn't have to choose between responsible innovation in crypto and protecting market participants from fraud and abuse. It needs prop
   > @chrisbarrett: The CFTC cited Chainlink's 2.0 whitepaper in today's crypto market rulemaking notice. Safer markets need more than rules. They need infrastructure built for transparency and verification. That's what 
   > @chairmanselig: Today, the @CFTC is doing its part to deliver clear rules of the road for crypto asset markets with its advanced notice of proposed rulemaking on Regulation Crypto Asset Transactions and Regulation Cr
   > @rvangrack: No tricks, just treats for American innovation. Great to see @ChairmanSelig and the CFTC taking another step toward regulatory clarity for crypto.
   > @faryarshirzad: Thank you @ChairmanSelig and @CFTC for taking an important step toward a clear federal path for crypto platforms to offer leveraged trading to U.S. customers. Done well, this effort can replace a patc
   Also: CFTC, Decrypt, Unchained, American Banker, The Daily Hodl, Reuters, Forbes, Coinpedia Fintech News, +13 more

33. A US official says the DOD stopped using Anthropic's tools; sources: Claude was in use as recently as last week, including in military operations against Iran
   BBC — https://www.bbc.com/news/articles/c5j9x9pr0240o
   Also: Fortune, Techstrong.ai, RuntimeWire

34. In a first-of-its-kind pilot in the US, Nolla Health will use AI to diagnose and prescribe acne medications to Utah patients without direct human oversight
   Annika Inampudi / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-05/nolla-health-ai-can-now-prescribe-acne-drugs-in-utah-without-doctors?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MTIxNjEzOSwiZXhwIjoxNzkxODIwOTM5LCJhcnRpY2xlSWQiOiJUTUZMODVLSVAzS00wMCIsImJjb25uZWN0SWQiOiI4OUM4OTNDMDhGOTQ0NThDQkQwQTQyREY1RDFCOTY0QyJ9.crHEdlDbj7Dx78MJpxZ7nHnh7NmskJmIYVmdbeyomfE
   > @luiswenus: Today, Nolla Health became the first organization in the U.S. (and possibly the world) to receive regulatory approval for an AI to issue initial prescriptions. This makes Nolla the first ever actual e
   > @michaelmina_lab: The first to receive regulatory approval in U.S. to use an AI doctor from Intake —> diagnosis —> Treatment! All with AI “doctor” via @nollahealth Nolla Health is making a massive jump here that can ch
   > @nollahealth: We are officially the first organization in the US to receive regulatory approval to issue initial AI prescriptions. Live in Utah today. Making really good healthcare more accessible through technolog
   > @logangrasby: An AI agent that can write actual prescriptions! This team is building the future of healthcare and it's inspiring to watch. There is such a massive opportunity to improve healthcare with AI and it re
   > @boringbiz_: Doctors: “yeah my job involves actually seeing patients, and it's not like AI is ever going to give you a prescription” AI:
   Also: Quartz, Nolla Health, Inc.com, Nolla Health, STAT, Gizmodo, SiliconANGLE, The Verge, +5 more

35. OpenAI says it will begin testing a visual ad format in ChatGPT later in October in the US, displaying clearly labeled visual ads while users generate images
   Mayank Parmar / BleepingComputer — https://www.bleepingcomputer.com/news/artificial-intelligence/openai-will-show-visual-ads-in-chatgpt-while-you-generate-images/
   > @btibor91: OpenAI is testing a new visual ad format in ChatGPT during image generation, starting later this month in the US https://openai.com/...
   Also: OpenAI, TechCrunch, Advertising, Marketing …, MediaNews4U, MediaNama, TechCentral.ie, Mumbrella, Inc, +19 more
