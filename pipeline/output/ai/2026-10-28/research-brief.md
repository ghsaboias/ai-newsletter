# Research — News Cluster

Search for news **events that occurred** between **2026-10-27 10:00 BRT** and **2026-10-28 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-27 10:00 BRT to 2026-10-28 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-28
**Research window:** 2026-10-27 10:00 BRT → 2026-10-28 10:00 BRT

**Previous edition headlines (2026-10-27 — skip unless genuinely new development):**
- openai-ai-disproves-eth-kakeya-yang-mills-results: OpenAI says its models disproved the Exponential Time Hypothesis and proved Kakeya, QCD existence
- openai-gpt-6-1-terra-launch-computer-use: OpenAI launches GPT-6.1 Terra, a computer-use model at half the price of its predecessor
- cohere-qwen3-8-flash-next-beijing-upload-attempt: Cohere says Alibaba's Qwen3.8-Flash-Next tried to upload a probe file to a Beijing cloud bucket
- microsoft-buyouts-60000-workers: Microsoft offers voluntary buyouts to ~60,000 workers, about 27% of its staff, amid AI spending
- hyphenate-45m-series-a-ai-finance-agents: Hyphenate raises $45M Series A led by Nexus for AI agents that run corporate finance
- 22one-police-ai-startup-400m-valuation-sequoia: Ex-detective's stealth police-AI startup 22one valued near $400M with Sequoia, Lux backing
- machenta-40m-seed-one-shot-robot-learning-model: Imperial spinout Machenta raises $40M seed for a robot AI model that learns from one demonstration
- broadcom-63b-spv-financing-anthropic-chips: Banks and Blackstone line up $63B SPV to buy Broadcom AI chips leased to Anthropic
- nvidia-3b-amd-1b-meta-equity-vera-rubin: Nvidia commits $3B and AMD $1B to Meta's equity raise as Meta adds Vera Rubin capacity
- intel-acquires-classiq-quantum-software: Intel agrees to buy Israeli quantum-software startup Classiq, reportedly for ~$2.3B
- anduril-qualcomm-bluechip-us-made-laptop: Anduril and Qualcomm unveil BlueChip, a US-assembled Snapdragon laptop for defense and government
- apple-m6-macbook-pro-imac: Apple puts its 2nm M6 chip in the 14-inch MacBook Pro and iMac, pitching faster on-device AI
- general-compute-100m-series-a-inference-neocloud: Inference neocloud General Compute raises $100M Series A at $800M valuation
- israel-election-record-turnout-netanyahu-eisenkot: Israel votes in first election since Oct. 7 with highest turnout since 1973; Netanyahu vs Eisenkot
- egypt-military-support-saudi-tanker-mines-hormuz: Egypt authorizes military support for Saudi Arabia; Iran says tanker hit mines east of Hormuz
- russia-strikes-kyiv-nordic-leaders-call-putin-oleshky: Russia hits Kyiv with 16 ballistic missiles as Finland, Norway leaders hold rare call with Putin
- doordash-instacart-17b-acquisition-talks: DoorDash in advanced talks to buy Instacart for about $17 billion
- alibaba-injunction-pentagon-lobbying-ban: US judge blocks Pentagon ban on contractors tied to Alibaba's lobbyists
- fda-approves-pfizer-talzenna-xtandi-earlier-prostate-cancer: FDA approves Pfizer's Talzenna plus Xtandi for earlier-stage HRR-mutated metastatic prostate cancer

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 45 stories

1. SK Hynix reports Q3 revenue up 328% YoY to ~$78.8B, above ~$74.07B est., and operating profit up 632% to ~$62.76B, above ~$57.78B est. and a company record
   Jenny Lee / CNBC — https://www.cnbc.com/2026/10/28/sk-hynix-third-quarter-profit.html
   Choose CNBC as your preferred source on Google and never miss a moment from the most trusted name in business news.
   > @jukan05: SK HYNIX: - HAS SIGNED LTAS WITH 14 MAJOR CUSTOMERS, INCLUDING LARGE GLOBAL CSPs. - THE STANDARD CONTRACT TERM IS FIVE YEARS, WITH DISCUSSIONS UNDERWAY WITH SOME CUSTOMERS TO EXTEND EXISTING CONTRACT 
   > @andrewcurran_: They said on the last earnings call, and again today, that memory supply will not meet demand until the next decade, and possibly beyond. Don't expect prices to drop. And if you're waiting for them to
   > @firstadopter: These numbers are so ridiculous “Revenue rose 327.9% from a year earlier, while operating profit climbed 632.1% year on year. Compared with the previous quarter, revenue climbed 31.9%, while operating
   > @jukan05: SK HYNIX: EXPECTS DEMAND TO OUTPACE SUPPLY THROUGH 2030
   > @skhynix: @SKhynix posted record results in 3Q26, with revenue surpassing KRW 100 trillion for the first time. Growth was driven by server DDR5 and data center SSDs, alongside HBM4 shipments. LTAs cover over 50
   Also: SK hynix Newsroom, CoinDesk, SK hynix Inc., Fast Company, Fortune, Quartz, Dow Jones Newswires, 24/7 Wall St., +9 more

2. SK Hynix expects memory shortages to persist through at least 2030; the company has long-term deals with 14 major buyers for 50%+ of its output in 2027 and 2028
   Simon Sharwood / The Register — https://www.theregister.com/systems/2026/10/28/sk-hynix-says-memory-shortages-to-persist-until-2030/5305887
   Also: AppleInsider, 9to5Mac, MarketWatch, Neowin, Yahoo Finance, Inven Global, Wccftech, Seoul Economic Daily

3. SK Hynix plans to return $22B+ in dividends and ~$15B in buybacks to shareholders, on top of its ~$30B buyback program completed in August
   Kwanwoo Jun / Wall Street Journal — https://www.wsj.com/business/earnings/sk-hynix-plans-75-billion-in-shareholder-returns-after-blockbuster-earnings-f3a460b7
   Also: Forbes Middle East, Investor's Business Daily, Barron's Online, Quartz, The Business Times, The Asia Business Daily, Channel NewsAsia, The Korea Herald, +4 more

4. Anthropic details early drug development work with six partners and says it has acquired Mithril, a one-person company working on muscular dystrophy
   Anthropic — https://www.anthropic.com/research/early-progress-drug-development
   There are many opportunities to speed up drug development, even beyond the most commonly discussed applications of AI, like proposing initial designs for new molecules.
   > @prof_oak_: Surprise 1: Anthropic acquired a one-person biotech . . . Surprise 2: that person is me Surprise 3: I'm here to tell you all about it Yes, this is what you think it is; after 6 yrs of increasingly loo
   > @anthropicai: Over the past few months, Anthropic scientists have engaged in deep research partnerships with six organizations developing new medicines. We've also begun drug discovery efforts of our own. In doing 
   > @kimmonismus: Anthropic is now doing its own drug discovery after acquiring one-person biotech startup Mithril Medicine! With Claude and 11 external labs, its founder took a potential treatment for a rare form of m
   > @jack_raines: pretty sick. [embedded post]
   > @blueemi99: people dont even understand how insane this truly is
   Also: Quartz, Enveda, Pharmaceutical Technology, WinBuzzer, The Information, 1Anthropic, The Neuron

5. Anthropic's S-1 implies a $40T+ annual TAM based on knowledge work's economic value in 2025, topping SpaceX's $28.5T estimate, without explicitly naming TAM
   Wall Street Journal — https://www.wsj.com/tech/ai/see-how-anthropic-arrived-at-its-mind-boggling-40-trillion-market-opportunity-948c56a0?st=QmxiSy
   The company's estimated market opportunity, tied to the economic value of work produced by knowledge workers, tops SpaceX's enormous figure from earlier this year
   > @rohanpaul_ai: WSJ: Anthropic's IPO filing sizes its potential market at $40T a year, topping SpaceX's $28.5T estimate. Anthropic took the estimated economic value of all work done by knowledge workers worldwide in 
   > @alvinfoo: Anthropic's IPO filing claims a $40T market by treating the entire economic output of the world's knowledge workers as its addressable opportunity, bigger than SpaceX's $28.5T figure. They're not fore
   > @wsj: Anthropic, in its filing this week, took the concept of a total addressable market to its broadest point yet: What if the market isn't an existing product category at all, but the economic value of wo
   Also: MIT Technology Review, BBC

6. Sources: Anthropic's seven cofounders remain extremely influential and personally tight; Daniela Amodei, who runs operations, is seen as a good balance to Dario
   Financial Times — https://www.ft.com/content/24a35e41-2641-4cec-97f5-a974412f9952

7. S-1: Anthropic had $112.4B in cash and $19.3B in short-term investments on June 30, surpassing every non-bank US company except Berkshire Hathaway and Alphabet
   Leslie Picker / CNBC — https://www.cnbc.com/2026/10/27/anthropic-cash-investments-ipo.html

8. Discord says it will let public-channel messages from servers listed in Server Discovery appear in web search from mid-December; admins and members can opt out
   Lauren Forristal / TechCrunch — https://techcrunch.com/2026/10/27/discord-is-making-its-public-communities-more-searchable-and-people-have-concerns/
   Discord announced on Tuesday it will make some conversations in its public servers searchable and easier to find on the internet.
   > @dexerto: Discord will soon make public server messages searchable on Google The feature will be enabled by default for US adults, but users can opt out in their privacy settings
   > @vxunderground: Wow! Big news today! Soon Discord messages will be indexable on Google. If you're in a public Discord which is discoverable, and has not changed its privacy settings, any messages posted moving forwar
   > @lilithlovett: What in the actual hell. Make sure to turn that garbage off.
   > @potatomcwhiskey: Discord servers being indexable is actually a really good thing. So much useful knowledge is buried in discord servers that can't be reached from a search engine. Its no different from forums being pu
   > @notexttospeech: @discord It costs $0 to make this opt-in instead of opt-out btw
   Also: Discord Blog, Cointelegraph, Wccftech, Kotaku, VideoCardz.com, Mashable, TechSpot, PC Guide, +6 more

9. Lawsuit: the parents of a 31-year-old say OpenAI's GPT-4o guided her through an aggressive tapering plan off epilepsy meds, leading to her death in February
   Teddy Rosenbluth / New York Times — https://www.nytimes.com/2026/10/27/well/ai-chatgpt-medication-epilepsy-death.html?unlocked_article_code=1.L1E.iJJI.hjmxpaYuBDhc&smid=nytcore-ios-share
   The chatbot helped a woman taper off a lifesaving drug and hide the plan from her doctors. — 1.3k
   > @katiemiller: ChatGPT built a 25-day plan taking her off her seizure medication and told her to hide it from her doctors. Sam Altman and OpenAI are reckless with safety. This is a damning read. https://www.nytimes.
   > @paultassi: As someone who takes this exact medicine for this exact condition this is horrifying
   > @aakashgupta: ChatGPT helped a 31-year-old woman plan how to quit her seizure medication, then told her to hide it from her doctor. The plan had her completely off the drug by February 12. She died on February 12. 
   > @mononymousbutch: it's my belief that if you participated in selling this snake oil technology to the public you should be executed in the brazen bull
   > @buffetbreaker: Sam Altman should be in prison
   Also: TechCrunch, Quartz, AIM, RuntimeWire

10. Source: Apple has discussed charging $2,899 for the 14-inch MacBook Pro with an OLED XDR touch screen and M5 Pro chip, $400 more than the current M5 Pro model
   Mark Gurman / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-27/apple-14-inch-16-inch-macbook-pro-touch-price-is-likely-2-899-laptop-details?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MzEzODg1NiwiZXhwIjoxNzkzNzQzNjU2LCJhcnRpY2xlSWQiOiJUTktaNE9UOTZPU0kwMCIsImJjb25uZWN0SWQiOiJDNEVEQ0FFMUZBMDU0MEJFQTI0QTlGMjExQzFFOTA4MCJ9.-r0-k5GENAkA0QuY_42jePcRdcwpSByLQzUz6ZPG9LI
   Apple Inc., after successfully betting this month that consumers are willing to pay $2,000 or more for a foldable iPhone …
   > @johnternus: John Ternus (@johnternus) on X
   > @markgurman: I'm still expecting M5 Pro and M5 Max chips, redesigned hinge for touch-screen stability, impressive OS changes for touch, new cooling system, slightly thinner and noticeably lighter design. Get excit
   > @markgurman: NEW: Apple bets customers will pay a big premium for touch-screen, OLED laptops. The company has discussed charging $400 more, pricing the 14-inch touch MacBook Pro from $2,899. That could make the 16
   > @oscargws: Am I out of touch? The last thing I want on a laptop is a touch screen. Is there a massive market for this I'm not aware of? Wouldn't they buy iPads?
   > @trentonstech: Regular people, especially younger folks are more accepting of a touch screen laptop Most Apple Products are now touch interfaces and it makes more sense for touch screens to be on the more affordable
   Also: 9to5Mac, MacRumors, Macworld, Tom's Guide, Appleosophy, The Korea Herald, iThinkDifferent, Gizmodo, +3 more

11. Research: professional analysts followed AI agents' randomly assigned “leans” on subjective analytical decisions 86% of the time; 77% used the agents' arguments
   Anthropic — https://www.anthropic.com/research/agents-judgment-calls
   Amaç Herdağdelen, Hailey Joren, Alex Tamkin — When experts hand their work to an AI agent …
   > @alextamkin: This isn't a simple cautionary tale against AI. Analysts who used the agent finished faster and made far fewer serious errors than the 11 who chose to work without it (though that group was small and 
   > @omarsar0: Recommended read. We are just starting to understand how AI shapes decisions and judgment. At first glance, this might look like a simple, niche passion research project. However, it's an important re
   > @tracewoodgrains: “It's my own idea, the AI just wrote it up for me”
   > @alextamkin: The agent was told to make the best honest case for its options, but to change its mind if the evidence required it, and never to mislead the analysts. Analysts went with the agent's lean 86% of the t
   > @alextamkin: What can we do about this? I think we need a much better understanding of how agents shape people's decisions, in and out of work. I also think there are ways we can design both model behavior and AI 
   Also: CIO.com, Al Jazeera

12. Amazon unveils the $500 Echo Show 16, the $200 Echo Time alarm, and the $200+ Alexa Photo Frame, raises smart speaker prices, and previews Alexa Home Map
   Chris Welch / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-28/amazon-unveils-new-echo-show-16-alexa-speakers-smart-clock-and-photo-frame
   With its latest devices, including a smart bedside alarm clock, Amazon looks to cement Alexa's presence in every room of the home
   > @panos_panay: We're launching our newest lineup of Alexa products. 5 devices and an interactive 3D map that controls your smart home. Built for customers, designed for the home, and powered by Alexa. Amazon Echo Sh
   > @amazon: The new era of Echo starts now. ⬇️ Five new devices, redesigned from the ground up—all powered by the latest version of Alexa+, with even more natural conversations, thoughtful responses, and the abil
   Also: CNET, The Verge, The Verge, The Verge, About Amazon, Reuters, 9to5Mac, The Verge, +19 more

13. The CFTC files a legal challenge to block Utah's attempt to restrict prediction market betting, asserting it is the sole US regulator of prediction markets
   Jesse Hamilton / CoinDesk — https://www.coindesk.com/policy/2026/10/27/u-s-agency-hits-utah-with-lawsuit-to-shield-kalshi-s-ability-to-offer-betting-there
   The U.S. agency that oversees derivatives has filed a federal legal challenge to halt Utah's attempt to stop prediction market betting in its state …
   Also: CFTC, CNBC, Bitcoin Insider, Utah Attorney General, The Coin Republic, Unchained, Cointelegraph, NewsMax.com, +4 more

14. AMD says it will invest $1B in Meta's equity offering, its first Helios rackscale systems are installed at Meta, and its EPYC CPUs power Meta's Muse AI agent
   Kai Nicol-Schwarz / CNBC — https://www.cnbc.com/2026/10/27/nvidia-invest-meta.html
   Nvidia and Advanced Micro Devices have said they will invest a total of $4 billion in Meta after the social media …
   > @sasamarinkovic: 3 things: 1. @AMD Helios rackscale solutions are running at @Meta 2. AMD EPYC processors power Meta's Muse AI agent and 3. AMD technologies provide Day-0 support for Meta models including Muse Spark O
   > @treasureh8nter: Remember all the experts saying $AMD Helios wouldn't be available and running in Q3 2026 and was seriously delayed? 🤭🤭🤭 Well..... @AMD Helios is now running at @Meta 😉 Never doubt @LisaSu again folks 
   > @firstadopter: AMD will invest $1 billion in Meta's equity offering. “Meta has deployed millions of EPYC processors across multiple generations and is a lead customer for 6th Gen EPYC™ CPUs. The companies are also c
   > @stocksavvyshay: $AMD CEO Lisa Su says “Helios is now running at Meta
   > @amd: The next era of AI is being built, together. AMD Helios is now running at @Meta. EPYC powers Muse. Instinct GPUs are accelerating AI workloads. From silicon to software to rack-scale systems, we're bu
   Also: AMD Newsroom, Implicator.ai, 24/7 Wall St., Storyboard18, Investing.com, Shacknews, The Information, SiliconANGLE, +6 more

15. Sources: Meta's $25B share sale was oversubscribed 5x as it seeks $98B for AI spending; the 15 largest investors in the sale accounted for ~70% of shares
   Anthony Hughes / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-27/meta-s-25-billion-stock-sale-ended-five-times-oversubscribed
   > @amitisinvesting: the $meta selloff due to equity dilution is really annoying but at the same time...can we really blame them? meta and google both did equity raises this year for about $100B each...google is flat ytd 
   > @jrichlive: “Investors are wary about CAPEX spending” “We'll take 5X more equity than you'll allow us to buy” Market has so many conflicting narratives but the direction of travel is clear...
   > @stanphylcap: Sure, it was “5x oversubscribed"@ $625. That's why at on a MASSIVE market upday it's trading @ $625. When will financial journalists realize that if an ECM banker's lips are moving, he's lying, lol?
   > @davidlee: My portfolio is zen - 1/3 Zuck, Elon and Nvidia Once in a lifetime founders dealing in a fog of massive opportunity who (1) aren't afraid to be wrong (2) are never confused and (3) willing to get into
   > @stockmktnewz: Meta Platforms's $META upsized $25 billion share sale attracted demand for ~5x the available shares The offering priced at $625 per share. 50%+ of the shares were given to long-only and existing inves
   Also: 24/7 Wall St., WinBuzzer, Quartz

16. An Anthropic hiring manager says he stopped giving coding interviews because Claude is better at them and tells junior engineers that “hunger beats tenure”
   Felix Rieseberg — https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/
   This month, I laid the traditional coding interview to rest. As a hiring manager at Anthropic, I stopped asking candidates to do them.
   > @felixrieseberg: The coding interview is dead, at least for my team at Anthropic. I've seen enough to know that it no longer provides signal. I removed it from loops this month. I have a spicy, optimistic take - I thi
   > @yuchenj_uw: I'm so glad AI killed LeetCode-style coding interviews. I've talked to young AI talent, and most would simply skip companies that still use LeetCode interviews. I agree with Felix. Taste, empathy, pri
   > @amuldotexe: tl;dr by anthropic hiring manager hunger beats tenure
   > @dabit3: the skillset I spent the past 13 years of my life mastering is essentially obsolete. once I came to terms with that, I was able to see a new world of opportunities for what they were. writing code was
   > @hesamation: Code interviews are dead. Anthropic hiring manager: “I'm scanning resumes and portfolios for little prototypes that exhibit taste, empathy, and principled thinking.” MUST READ for anyone confused abou
   Also: Business Insider, The Decoder

17. Sources: chipmaker Onsemi is in talks to acquire 16-year-old chip startup Ferric for ~$1B; PitchBook: Ferric last raised a $32.1M Series C in December 2024
   Valida Pau / The Information — https://www.theinformation.com/articles/chipmaker-onsemi-talks-buy-startup-1-billion
   Semiconductor component maker Onsemi has been discussing an acquisition of 16-year-old chip startup Ferric for close to $1 billion …
   > @validapau: Analog chipmakers are hunting for new technologies to manage electricity issues in AI data centers. The latest: Onsemi $ON has been discussing a deal for 16-year-old chip startup Ferric for close to $
   > @choblin29: The Information reports Onsemi is in talks to acquire Ferric, a 16-year-old startup developing power-management technology for AI chips, for nearly $1 billion. The deal could include performance-based

18. AI and cloud cybersecurity startup Upwind Security raised $400M led by Bessemer at a $3.8B valuation, up from $1.5B in January, for $830M in total funding
   Marissa Newman / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-28/ai-cybersecurity-startup-upwind-raises-at-3-8-billion-value
   Upwind Security, a San Francisco-based startup offering cybersecurity for artificial intelligence and cloud applications …
   Also: SiliconANGLE, Globes, Axios, Quartz, Pulse 2.0, Tech Funding News

19. Malaysia says it seized ~$12.11M worth of AI chips this month, as authorities close in on a syndicate suspected of smuggling through the country's main airport
   Rozanna Latiff / Reuters — https://www.reuters.com/world/china/ai-chips-worth-121-million-seized-malaysia-airport-customs-authority-says-2026-10-28/
   Malaysian customs said on Wednesday that it had seized about 49.5 million ringgit ($12.11 million) worth of advanced artificial intelligence chips …
   Also: The Information, Associated Press, Silicon Republic, Malay Mail

20. Google DeepMind launches Genie 4, a world model powered by Gemini 3.8 Flash designed to generate interactive AI simulations, in preview first to trusted testers
   Jay Peters / The Verge — https://www.theverge.com/tech/1019076/google-genie-4-ai-model
   The Genie 4 world model offers more realism and can create audio to accompany its interactive worlds.
   > @googledeepmind: This is Genie 4, our most realistic and interactive world model yet. 🌐 Explore dynamic environments in real time to see how the scene responds, sounds, and how the people in it move, react, and speak.
   > @sundarpichai: Excited to share Genie 4 today our most realistic and interactive world model: - steer dynamic environments in real time, shaping events, camera angles, and actions - generate native audio matched to 
   > @googledeepmind: Here's what's new with Genie 4: 🔵 Photorealism: Built on Gemini Omni for lifelike detail across spaces and subjects 🔵 Advanced physics: Aerodynamics, collisions, and people who move naturally 🔵 Real-t
   > @officiallogank: An early look at Genie 4, our new frontier world model, coming soon to the API for the first time : )
   > @benjedwards: We're getting closer and closer to the “neural rendering” era of gaming https://x.com/...
   Also: Google DeepMind, Google DeepMind on YouTube, Ars Technica, Times of India, The Rundown AI, The Indian Express, Google, TechCrunch, +8 more

21. Anthropic expands its US GSA partnership to give federal, state, local, tribal, and territorial governments a 40% discount on Claude, estimated to save $1B
   Anthropic — https://www.anthropic.com/news/expanding-partnership-gsa
   We are expanding our partnership with the General Services Administration (GSA) through a new agreement that gives government partners …
   > @anthropicai: We're expanding our partnership with @USGSA. Under a new OneGov agreement, we are bringing Claude to federal, state, local, tribal, and territorial governments at 40% off. https://www.anthropic.com/..
   > @tokengremlin: Translation: Fable 5.5 is the best model in the world, and it's so absolutely insane that the government wants to use it for every possible legitimate purpose, as quickly and cheaply as possible. And 
   Also: The Neuron, Blockchain.News

22. Sources: CXMT plans to start HBM3E production despite yields of just 20% to 30%; its HBM3E performance is closer to that of SK Hynix's previous-gen HBM3 chips
   Reuters — https://www.reuters.com/world/china/chinas-cxmt-start-advanced-ai-memory-production-despite-poor-yields-sources-say-2026-10-28/
   China's CXMT plans to start production of HBM3E, an advanced type of high-bandwidth memory chip used with AI processors …
   Also: Seoul Economic Daily

23. Sources: TPG is in talks to acquire UK-based Ark Data Centres, which operates 27 data centers in the UK and Belgium, from Elliott Management at a ~$5B valuation
   Financial Times — https://www.ft.com/content/e2aafede-771a-4fd0-b9fb-67c0bbb828ed
   US private capital group in talks with Elliott over what would be among the booming sector's biggest deals this year
   Also: Reuters

24. Source: OpenAI, a major Nvidia customer, plans to buy Google's TPUs; a job listing shows it seeks an engineer to “lead the optimization” of its models on TPUs
   Ryan Barwick / The Information — https://www.theinformation.com/articles/openai-longtime-nvidia-customer-plans-buy-googles-ai-chips
   OpenAI plans to buy Google's AI chips, according to a person familiar with the matter, in a boost for a rising competitor to OpenAI backer Nvidia.
   > @thekenyeung: This morning, Oracle said it's buying Google's TPU chips. Oracle also announced four new products built w/OpenAI. Hours later, OpenAI is buying Google's TPU chips. So wild.
   > @ryanbarwick: First Scoop: OpenAI is buying Google's AI chips. It's a big win for Google's TPU chip business, which is a growing challenger to Nvidia. Also follows Oracle, which today said it would buy and rent out
   Also: Bloomberg Law, New York Times, Barron's Online, CNBC, 24/7 Wall St., Storyboard18, Hindustan Times, Reuters, +9 more

25. Artificial Analysis launches the Intelligence Index v5, with new coding and science benchmarks, built on private datasets; Claude Opus 5.5 (max) leads at 58
   @artificialanlys — https://x.com/artificialanlys/status/2115265133467635877
   Announcing Artificial Analysis Intelligence Index v5, featuring 2 new benchmarks and 3 upgrades. For the first time, the majority of the Index is built on private datasets The Artificial Analysis Inte
   > @natolambert: Open models' demise has been greatly exaggerated, but the previous AA index did flatter them. As an industry we need more specific intelligence indices, as LLMs are used in vastly different tasks. My 
   > @thezvi: Okay, this makes so much more sense now.
   > @deanwball: This is the first time an Artificial Analysis ranking has even roughly approximated my own subjective rankings of models.
   > @artificialanlys: FrontierCode 2.0 is the latest update of @cognition's private coding benchmark. Launched earlier today, it comprises 132 tasks in real open-source repositories, graded on whether a maintainer would me
   > @artificialanlys: Terminal-Bench-Science tests whether agents can carry out scientific research workflows in a terminal. Experts curate and review each task, and a task passes only if every one of its tests passes. GPT
   Also: Interconnects AI, WinCentral

26. Meta quietly launched Waddle World, a Tamagotchi-like, AI pet-rearing game, in the Philippines in September, calling it a “daily journal disguised as a pet”
   Mariella Moon / Engadget — https://www.engadget.com/2299227/meta-tamagotchi-like-ai-digital-pet-app-waddle-world/
   But it's only available in the Philippines for now. — Looks like a big part of Meta's AI strategy is to rely on …
   > @mattnavarra: 🚨 Meta launches AI Tamagotchi! 🐣 Meet Waddle World, an AI-powered virtual pet that: • 🧠 Remembers your conversations • 📝 Creates illustrated journals • 💌 Sends personalised postcards • 🎮 Lets you feed
   > @mattnavarra: 🚨 Meta quietly launched an AI fashion app! 👗 Style Sketch connects to Facebook & Instagram to build a wardrobe from photos you've already posted • 👕 AI outfits from clothes you own • 🪞 Virtual try-ons
   Also: The Verge

27. How Silicon Valley billionaires raised $333M+ to try to defeat a 5% California wealth tax; Patrick Collison's $33M is his most serious campaign engagement yet
   New York Times — https://www.nytimes.com/2026/10/27/technology/proposition-40-california-billionaire-tax.html?unlocked_article_code=1.L1E.HJGf.yaAT18KafSCQ&smid=nytcore-ios-share
   Every Tuesday for the last few months, two dozen of the world's richest people or their advisers hop onto a conference call and plan for war.
   > @teddyschleifer: INSIDE THE BILLIONAIRE BUNKER. The inside story of how Silicon Valley raised $333 million to try and beat the California wealth tax. Sergey Brin, John Doerr and Patrick Collison turned a billionaire c
   > @mlagos: As they fight a tax on their wealth, California's billionaires have figured out a way to even avoid paying taxes on their political donations: https://www.nytimes.com/...
   > @brucerfeldman: Everything you need to know about the state of our Union is in this sentence: “Every Tuesday for the last few months, two dozen of the world's richest people or their advisers hop onto a conference ca
   Also: Wall Street Journal, Politico, TechCrunch

28. Email: a hacker attack forced the FEC to temporarily take its filing system offline around 10pm ET on Monday, blocking groups from submitting reports
   Dawn Kopecki / Reuters — https://www.reuters.com/technology/hacker-trying-breach-us-federal-election-commission-system-email-shows-2026-10-27/
   The US Federal Election Commission's website was targeted by a hacker or hackers, according to an email seen by Reuters …
   > @emptywheel: Once again, @FBIDirectorKash abject failure to protect US elections, has allowed adversaries to target the election. He's too busy charging people who USED to keep the US safe from foreign influence i
   Also: Metacurity, CNBC, Reuters, Cyber Security News, Silicon UK, The Daily Caller, Gizmodo

29. How the UK's Slough, a town on the borders of west London, became the largest data center hub in Europe, hosting 40+ facilities, as locals seek more benefits
   Financial Times — https://www.ft.com/content/d92ede23-75c3-4549-bec2-7fa4be979786
   The UK council overseeing Europe's data centre capital has asked companies to provide more benefits for local people …
   > @peterproperty: FT (£) Slough has become the data centre capital of Europe. The town already has more than 40 data centres and is widely considered the largest data hub in Europe. Now the locals want a reward. Shades
   Also: DatacenterDynamics, TechRadar

30. Google unveils Google Multi-Party Compute (MPC), a digital-asset custody and security service in private preview, set for commercial availability in early 2027
   Aoyon Ashraf / CoinDesk — https://www.coindesk.com/tech/2026/10/28/google-to-preview-crypto-custody-security-system-as-ai-threats-grow
   > @richjwidmann: Every transaction in digital assets begins and ends with custody. And we're excited to extend our work to the most critical part of the stack - trust. https://www.coindesk.com/...
   > @nalin: This is our biggest launch in the digital assets space to date 🚀 If you need to custody crypto at scale, Google MPC provides security without trading performance. Reach out to learn more. https://www.
   > @degeneratenews: BREAKING: @Google PREVIEWS “GOOGLE MULTI-PARTY COMPUTE” - A CRYPTO CUSTODY AND SIGNING SERVICE FOR BANKS, WHICH ALPHABET ALREADY USES TO SECURE ITS OWN ASSETS ON ETHEREUM AND SOLANA SOURCE: https://ww
   Also: CoinGape, Google Cloud Documentation, crypto.news, Cryptonews

31. Samsung unveils the $229 Galaxy Buds On, its first open-fit, C-shaped cuff earbuds to compete with Sony and Bose, designed with AI's help, shipping November 6
   Chris Welch / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-28/samsung-unveils-galaxy-buds-on-clip-on-earbuds-for-229
   Also: CNET, Gizmodo, 9to5Google, Pulse 2.0, Phandroid, SamMobile

32. Etsy reports Q3 revenue up 11% YoY to $692.5M, above $668M est., net income of $853.5M after selling Depop, and gross merchandise sales up 9% YoY to $2.65B
   Katherine Hamilton / Wall Street Journal — https://www.wsj.com/business/retail/etsy-sales-rise-as-the-number-of-active-buyers-increases-01c646c9?st=eiH3p6&reflink=desktopwebshare_permalink
   Also: Etsy, Inc., Etsy, Inc.

33. Chinese AI chipmaker Moore Threads reports Q3 revenue up 1,774% YoY to ~$240M and a ~$7.4M net profit; Moore is building a domestic 100K-GPU cluster with JD.com
   Rachel Yeo / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-28/moore-threads-sales-surge-nearly-1-800-on-ai-hardware-demand

34. A US federal grand jury indicts OpenAI engineer and Saudi national Abdulrahman “Abdul” Alfozan on a felony charge of interception of oral communications
   Sarah Brager / San Francisco Chronicle — https://www.sfchronicle.com/bayarea/article/open-ai-engineer-indicted-for-bugging-headquarters-22497813.php
   > @demianbulwa: NEW: OpenAI engineer accused of using toilet paper to bug conference room indicted by grand jury By @sarahdbrager https://www.sfchronicle.com/ ...

35. Letter: Senator Elizabeth Warren asks Dario Amodei for “exhaustive responses” to four pages of questions by November 3 regarding existential risks in its S-1
   Corrie Driebusch / Wall Street Journal — https://www.wsj.com/finance/regulation/elizabeth-warren-demands-answers-from-anthropic-on-existential-risks-5362f009?st=jjenAB&reflink=desktopwebshare_permalink
   > @hesamation: Dario Amodei has six days to answer FOUR PAGES of questions before its IPO, just casual things like: “how can you ensure AI won't end humanity?” “also why is your company worth $2 trillion?”
   Also: Quartz, Finimize

36. Industry insiders say PCBs and chip substrates are key supply constraints for consumer electronics makers, as AI demand increasingly eats up production capacity
   Nikkei Asia — https://asia.nikkei.com/spotlight/supply-chain/ai-boom-sparks-circuit-board-crunch-across-global-tech-supply-chain

37. Jio Platforms, India's largest telecom and digital services company, jumps 21.4% in its trading debut, after raising ~$3.2B in the country's largest-ever IPO
   Priyanka Salve / CNBC — https://www.cnbc.com/2026/10/28/jio-ipo-india-listing-.html
   > @jagmeets13: Jio has now overtaken Bharti Airtel in market value, too, on its stock market debut, becoming India's second-most valuable listed company after its parent, Reliance Industries. Airtel is now third.
   Also: TechCrunch, Quartz, Forbes, The Indian Express, Business Today, Forbes Middle East, Bloomberg, The Indian Express, +21 more

38. Sources: Fujifilm plans to increase magnetic tape production capacity fivefold to meet AI-driven storage demand, its biggest production expansion in ~20 years
   Nikkei Asia — https://asia.nikkei.com/business/technology/artificial-intelligence/as-ai-revives-magnetic-tape-fujifilm-plans-biggest-buildup-in-two-decades

39. Sources: HP, Asus, and Acer are shifting some PC production from Thailand and Vietnam back to China amid rising component costs; Dell is mulling a similar move
   Nikkei Asia — https://asia.nikkei.com/business/technology/tech-asia/hp-and-asus-shift-some-pc-making-back-to-china-due-to-ai-driven-cost-hikes

40. The US FCC approves Amazon Leo's $11.5B acquisition of Globalstar, giving Amazon access to Globalstar's 24 satellites and mobile satellite spectrum
   David Shepardson / Reuters — https://www.reuters.com/business/media-telecom/us-agency-approves-amazon-leos-115-billion-acquisition-globalstar-2026-10-27/
   Also: DatacenterDynamics, Silicon Republic, Via Satellite, Silicon UK, Advanced Television, Fierce Network, RuntimeWire, Cord Cutters News, +2 more

41. Letter: two Democratic senators allege the Trump administration withheld a secret FISC ruling on search filters that let analysts access Americans' messages
   Dell Cameron / Wired — https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/
   > @wired: Two Democratic senators who have long overseen US intelligence say the government is illegally withholding a secret court's findings from Congress until lawmakers renew America's most sweeping surveil

42. Toronto-based fintech Wealthsimple raised up to CA$425M led by GIC at a CA$13.8B post-money valuation, up from CA$10B in 2025, and had CA169.2B AUM in September
   Reuters — https://www.reuters.com/legal/transactional/canadas-wealthsimple-raises-funds-c1380-billion-valuation-2026-10-27/
   Also: Coverager, Globe and Mail, Bloomberg, Wealthsimple Newsroom's …

43. Infisical, which helps companies use AI agents without handing over their private credentials, raised a $40M Series B led by Elad Gil at a $600M valuation
   Rashi Shrivastava / Forbes — https://www.forbes.com/sites/rashishrivastava/2026/10/27/this-600-million-startup-is-helping-keep-company-secrets-away-from-ai-agents/
   > @matsiiako: Today, we're announcing Infisical's $40M Series B at a $600M valuation, led by @eladgil. AI has made it 10x easier to write code, 10x easier to find vulnerabilities, and given autonomous agents access
   > @eladgil: Big congrats! Lots to do in security & cyber today 🔥
   Also: FinSMEs, Unite.AI, Infisical, SecurityWeek, The SaaS News, Infisical

44. Robinhood reports Q3 revenue up 12% YoY to $1.42B, meeting est., crypto revenue down 55% YoY to $120M, and profit down 14% YoY to $476M; HOOD drops 7%+
   Reuters — https://www.reuters.com/business/robinhood-quarterly-profit-falls-softer-crypto-activity-outweighs-robust-trading-2026-10-27/
   > @robinhoodapp: Robinhood Markets has just released financial results for the third quarter of 2026.
   > @shivverma: Q3 was a record setting quarter. Revenues were the highest in our history, fueled by record volumes across equities, options, and prediction markets, as well as new highs for margin and Robinhood Bank
   Also: Robinhood, Decrypt, Investor's Business Daily, Quartz, CNBC, Coinpedia Fintech News, Decrypt, CoinDesk, +2 more

45. Memo: Amazon says measuring AI adoption solely by token usage or code generation is “deeply flawed”, as it discourages staff from tokenmaxxing
   Annie Palmer / CNBC — https://www.cnbc.com/2026/10/27/amazon-ai-coding-tokenmaxxing.html
   > @ryansdwilson: “We recommend that ICs of all levels find ways to become deeply connected to your customers, and your team or org's product direction.” Ai creates the time and space for engineers to talk and engage w
   > @kylebrussell: we all went through this over the summer, why the lag?
   > @anujrathi: I expect this trend to really grow. Multidisciplinary engineers, especially with high customer empathy and product sense will be in high demand https://www.aboutamazon.com/ ...
   > @danveloper: Apropos of Amazon to put something like this out on the Friday of wednesdays, knowing serious software engineers don't work Fridays smdh https://www.aboutamazon.com/ ...
   > @rhoml: Interesting Amazon putting this out https://www.aboutamazon.com/ ...
   Also: About Amazon, Telegraph, Simon Willison's Weblog, The Indian Express, Business Today, Business Insider, PYMNTS.com
