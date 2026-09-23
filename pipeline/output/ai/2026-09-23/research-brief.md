# Research — News Cluster

Search for news **events that occurred** between **2026-09-22 10:00 BRT** and **2026-09-23 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-09-22 10:00 BRT to 2026-09-23 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-09-23
**Research window:** 2026-09-22 10:00 BRT → 2026-09-23 10:00 BRT

**Previous edition headlines (2026-09-22 — skip unless genuinely new development):**
- anthropic-claude-opus-5-5: Anthropic launches Claude Opus 5.5: Fable 5.1-level performance at 40% lower cost to run
- xiaomi-mimo-v2-6-top-open-weights: Xiaomi's MiMo-V2.6 Pro becomes the top open-weight model, under an MIT licence
- alibaba-qwen-rsi-10-trillion-parameters: Alibaba plans a 5T-10T parameter Qwen model and says Qwen3.8-Max improved itself for a month
- snorkel-ai-350m-training-data: Snorkel AI raises $350M at a $3.5B valuation as labs bid up complex training data
- shopify-meta-muse-agentic-checkout: Shopify opens every store to Meta's Muse agent, letting it check out with Shop Pay
- meta-muse-mac-zero-day: Zero-day let any local code hijack Meta's Muse on macOS; Meta shipped a hotfix in hours
- china-cac-probes-deepseek-moonshot-anthropic: China's internet regulator probes DeepSeek and Moonshot over data routed to Anthropic's Claude
- alibaba-zhenwu-v900-20gw-roadmap: Alibaba unveils Zhenwu V900 AI chip and a 20 GW compute target for 2032
- boston-dynamics-atlas-metaplant-training-center: Boston Dynamics opens Atlas training center inside Hyundai's Georgia Metaplant
- cognex-acquires-realsense: Cognex buys Intel spinout RealSense for $500M in cash to enter robot perception
- ligent-hong-kong-ipo-debut: Hisense-backed optical chipmaker Ligent raises $723M and pops 19% in Hong Kong debut
- google-georgia-power-nuclear-uprate: Google pays a premium to fund nuclear uprates at Vogtle and Hatch, adding 96 MW
- kairos-samsung-ct-investment: Samsung C&T to put up to $100M into Kairos Power's reactor for Google
- verda-189m-series-b-unicorn: Finland's Verda raises $189M, becoming Europe's newest AI-cloud unicorn
- us-denmark-greenland-arctic-security-pact: Trump signs Arctic security pact with Denmark and Greenland, pledging two new US bases
- iran-offers-reopen-hormuz-seven-days: Iran offers to reopen the Strait of Hormuz in seven days if the US lifts its port blockade
- brent-falls-below-100-hormuz-tanker-attacks: Brent slides below $100 as Saudi Gulf loadings surge — even as two more tankers are hit in Hormuz
- united-russia-wins-first-wartime-duma-election: United Russia takes 57.5% in Russia's first wartime Duma election, held under record drone attack
- binance-100m-circle-stake-usdc-deal: Binance buys a $100M stake in Circle and signs a five-year deal to push USDC in emerging markets
- boehringer-envisagenics-rna-splicing-deal: Boehringer Ingelheim commits up to $1B to Envisagenics' RNA-splicing cancer targets
- nigeria-cbn-cuts-rate-350bp: Nigeria's central bank cuts rates 350bp to 23%, breaking with a hawkish turn elsewhere

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 46 stories

1. YouTube rolls out tools for microdramas, an AI storytelling assistant for script analysis, video A/B-testing, and more, as it battles Netflix over top creators
   Ben Fritz / Wall Street Journal — https://www.wsj.com/business/media/youtube-is-battling-netflix-over-top-talent-eebbf0cf?st=py6xAQ&reflink=desktopwebshare_permalink
   Google-owned platform rolling out better tools for digital producers that could help it keep more of their content exclusively
   > @unreal_dreamer: A lot of YouTube changes actually Lots I gotta look into and relearn Lots of good stuff though STILL no updates to YouTube livestreaming like moderation tools and lower livestream latency (ultra low s
   > @cerilysm: Welp, it was just a matter of time. Welcome to the Era of Content Creation AND Consumption dictated by AI. “Hey Youtube Studio, which thumbnail and hook brings more views?
   > @sam_badawi: YouTube is stepping up against with Netflix for top creators by rolling out better production tools, AI editing features, microdramas and live AI dubbing. Netflix $NFLX has been increasingly signing m
   > @mws: VIDEO A/B TESTING IS COMING TO YOUTUBE You can upload 3 versions of the SAME video Different hooks, different pacing, whatever you wanna test and YouTube tells you which one kept people hooked the lon
   > @teamyoutube: Hot off the presses from Made On 🔥some updates for Creators to look forward to: ✨ Shorts series, Live showdowns & more new ways to create and go live ✨New ways to partner with brands and grow your Sho
   Also: YouTube Official Blog, TechCrunch, TechCrunch, Big Technology, YouTube Official Blog, TechCrunch, Mashable, TechCrunch, +12 more

2. At its Made on YouTube event, YouTube unveils Custom Feeds, an LLM-powered feature that lets users generate and save tailored homepage video feeds, for US users
   Reece Rogers / Wired — https://www.wired.com/story/youtube-custom-feeds-let-you-steer-the-algorithm-without-breaking-it/
   In YouTube's latest update, viewers can tweak what the algorithm shows on their front page and curate it to a specific vibe.
   Also: YouTube Official Blog, TechCrunch, YouTube Official Blog, YouTube Official Blog, Bloomberg, YouTube Official Blog, YouTube Official Blog, Thurrott, +10 more

3. Google releases Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS, its “most expressive audio generation models yet”, with support for more than 100 languages
   Google — https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/
   Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS are our most expressive audio generation models yet.
   > @hume_ai: 3/ Gemini 3.8 Flash and Flash-Lite take the top two spots on Overall, at 0.92 and 0.91. Gemini 3.1 Flash, an older model, still leads Acting at 3.97, well clear of the 3.69 behind it.
   > @thedaryadesk: Forget the leaderboard wins. The real headline in Google's Gemini 3.8 TTS launch is that cloning a voice from a sample lasting 30 seconds is now a standard developer feature. Google's safeguard is a m
   > @steveruizok: I was invited to test Gemini 3.8 Flash TTS. This is currently my favorite model. The voice outputs from this model are extraordinary. I never really rated AI voice generation because of the uncannines
   > @karthik_rangan: I cant get over the fact that they explicitly added an active listening “mhm” feature. we really just built robots to pretend they care about what we are saying. Being able to direct it line by line l
   > @alisa_fortin: @Bangkok8ai Hello! You can definitely create and save your custom voice. You can use your own customer voice from an external source via our voice replication feature - you will be asked to verify tha
   Also: The Decoder, RuntimeWire, Unite.AI

4. Q&A with Jensen Huang on AI creating more jobs than it destroys, pushing back against AI doomerism, Chinese open models, the Hugging Face acquisition, and more
   Ezra Klein / New York Times — https://www.nytimes.com/2026/09/23/opinion/ezra-klein-podcast-jensen-huang.html?unlocked_article_code=1.DVE.XHWL.rvGLo4dRGLlK&smid=url-share
   This is an edited transcript of “The Ezra Klein Show.” You can listen to the episode wherever you get your podcasts.
   > @tedlieu: Oh
   > @hesamation: 🚨Jensen Huang just took a shot at OpenAI, Anthropic and AI doomers: “Nobody's building …
   > @edzitron: Jensen Huang calling to shut the labs down. Go off king
   > @themidasproj: Jensen Huang: “Now, if they say [that their models aren't safe] ... then I think the answer is that we have to shut the labs down.”
   > @garrisonlovely: pretty sensible tbh
   Also: The Ezra Klein Show on YouTube, The New Stack, Axios

5. Patreon co-founder Sam Yam says he is joining OpenAI to lead Creator Product, alongside Patreon's Head of Product Drew Rowny and Head of Engineering Shannon Ma
   Sam Yam / @samyamiam — https://x.com/samyamiam/status/2102503574492332141
   1/ I'm joining @OpenAI to lead Creator Product after over 13 years since starting @Patreon. Coming with me are my favorite crew Drew Rowny and Shannon Ma, Patreon's (now former) Head of Product and He
   > @openai: As part of our efforts to pace the frontier, we're committed to supporting independent assessments with deep levels of access across training, evaluation, and deployment. That access should enable thi
   > @joshconstine: Whoa, OpenAI just acquihired Patreon's co-founder/CTO plus it's heads of product and eng. Great for creators, and Jack will keep Patreon chugging, but also feels like a bit of coffin nail for the capi
   > @andrewneel: OpenAI is snatching up cofounders now 👀
   > @denk_tweets: sooo the patreon product hasn't evolved in a decade and now their head of product, head of engineering, and CTO just bailed 👉👈
   > @jgonzalezferrer: OpenAI hired former Patreon CTO to lead new products for Creators and Communities 😱
   Also: The Verge, Music Ally, WeRSM, The Decoder

6. Disney raises Disney+ and Hulu prices, the fourth price hike in as many years; the ad-free tiers will each cost $21.49/month, an increase of $2.50
   Rick Porter / The Hollywood Reporter — https://www.hollywoodreporter.com/business/business-news/disney-plus-hulu-price-increases-september-2026-1236708364/
   Subscribing to a bundle is now almost exactly half the price of individual plans for each streamer.
   > @justdaveyjustin: All this to watch nothing but remakes and subpar sequels to movies that didn't need them. A lazy corporation producing dogshit content and making you pay double for it.
   > @retrocvnty: I'm so glad I started collecting physical media
   > @canipack21: @THR Pushing ad free past twenty one dollars is how you move people to the ad tier without ever asking them to. The number to watch is not cancellations, it is how many downgrade instead, because thos
   > @rdd147: $DIS to hike streaming prices 13% as $AMZN Prime prepares announcement of up to 30% hike, and $SONY PlayStation 36% hike on streaming plans. No inflation. Sure.
   > @elafrost: @charlieINTEL Just a reminder that this shit launched at $7
   Also: Bloomberg, Finimize, 9to5Google, AppleInsider, 9to5Mac, Dexerto, Comic Book, TheDesk.net, +14 more

7. The US criticizes Australia's digital duty-of-care proposal, which has a provision that would require social media platforms to let users opt out of algorithms
   Angus Whitley / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-23/us-rebukes-australia-for-plan-to-target-social-media-algorithms
   The US government criticized Australia's plan to clamp down on social media algorithms and harmful content online …
   > @latikambourke: BREAKING Trump Administration warns it will treat as censorship ‘facilitating censorship’ Prime Minister Anthony Albanese's proposed crackdown on algorithms. Source: https://au.usembassy.gov/...
   > @drewpavlou: American patriots rescuing freedom in Australia
   > @matt_barrie: fafo
   > @albomp: Australia led the world with our social media ban for under-16s. And the world is following. Alongside @EmmanuelMacron and @sanchezcastejon we're now building a Coalition for Children's Rights and Pro
   > @senshenderson: Yes Anika, your digital duty of care bill is all about censoring online content. That's one of the reasons your draconian laws have been so condemned by the US Administration. @USEmbAustralia ➡️ https
   Also: BBC, ABC, U.S. Embassy & Consulates …, The Hill, Reclaim The Net, The Independent, The Guardian, Capital Brief, +1 more

8. Discord is rolling out its updated age-verification policy this week, sorting users into either the Adult or Teen group based on account age, activity, and more
   Anna Washenko / Engadget — https://www.engadget.com/2265924/discord-rolls-out-its-revised-age-verification-policy/
   It will offer several privacy-focused options for users who aren't automatically confirmed as adults.
   > @discord: An update on how we confirm your age group on Discord from @svishnevskiy. Read the full blog here: https://discord.com/...
   > @qfzeeph: “Guys they made it so you don't have to use the facial scan” ok but we shouldn't have to fucking do any of this there's literally no reason for any of this to be implemented at all except for corporat
   > @gyaruglow: Discord is pushing this age verification knowing the danger it could cause to people's privacy Are we gonna forget the 70K ID leaks now? Also adding a payment method for verification just gives hacker
   > @deephumor: Keep in mind that Discord is not legally mandated to implement age verification globally, they are just doing so because they want to harvest as much data as possible Handing this company ANY personal
   > @sxr123: Or, and stay with me here, you could just not do any of that. Let's do that. Let's just not do any of what you're proposing here and never talk about it again.
   Also: Discord, The Verge, TechCrunch, The American Bazaar, Biometric Update, GamesMarket, Digital Trends, PocketGamer.biz, +10 more

9. The UK CMA proposes rules requiring Google and Android OEMs to offer search choice screens on first use and via yearly prompts, new AI assistant rules, and more
   Steve Dent / Engadget — https://www.engadget.com/2266226/uk-competition-watchdog-wants-to-give-android-and-chrome-users-more-search-engine-choices/
   It would also require smartphone makers to give users a choice of AI assistants. — The UK's Competition and Markets Authority …
   > @cmagovuk: We have strengthened our proposals to make choosing your search provider on Android and Chrome easier and with a wider range of alternatives, including eligible AI services. We're now seeking your fee
   Also: GOV.UK, Light Reading, Search Engine Roundtable, Dow Jones Newswires, Telecompaper

10. At its Accelerate conference, Amazon says it is opening its seller tools to third-party AI agents, starting with Claude, in beta for US merchants
   Todd Bishop / GeekWire — https://www.geekwire.com/2026/amazon-opens-its-seller-tools-to-outside-ai-agents-starting-with-anthropics-claude/
   Amazon announced new AI tools for its independent sellers Wednesday, led by a plugin that lets them run their Amazon businesses from Anthropic's Claude or Amazon's own Quick assistant.
   > @aaron_harme: Amazon told third-party merchants they can check inventory, move prices, and edit listings from Anthropic's Claude without opening Seller Central, days after the same company blocked Meta's Muse shopp
   > @polarizinglit: This is a good example of a technofeudal take over ... You can't just start a business now on your own ... You need permission from a techlord to utilize their cloud infrastructure, shipping logistics
   > @stocksavvyshay: $AMZN is rolling out a Claude-powered Seller Assistant that can monitor and act on pricing, inventory, ads and compliance 24/7. Its already live for 90%+ of sellers globally with recommendations accep
   Also: About Amazon, Reuters, Unite.AI, PYMNTS

11. Sources and Nscale's US SEC filings: ByteDance accounted for nearly 75% of Nscale's sales in 2025 and used Nscale's facility in Norway to access Nvidia AI chips
   Financial Times — https://www.ft.com/content/d1090476-7be6-4bba-ae2a-f417499e820a
   Chinese tech giant was AI cloud provider's largest customer last year but is not prominently named in pitch to stock market investors
   > @hamish_low5: Loans from banks are currently bringing more demanding monitoring requirements on Chinese firms using restricted AI chips in the cloud than the US Government, which doesn't feel a particularly sustain
   > @tanarrowz: ByteDance used Nscale's cloud facility in Norway to access Nvidia chips that it would otherwise have been unable to buy in China, exploiting a loophole in US trade restrictions https://www.ft.com/... 
   > @azeem: Run-roh. [image] [embedded post]
   > @nathanbenaich: PLOT TWIST [embedded post]
   Also: Tom's Hardware, Cautious Optimism, Fortune, The Decoder

12. Gallup survey of 37 countries: in 34, positive AI sentiment outweighed the negative; 90%+ of people in China and 66%+ in Nigeria say AI will improve daily life
   Damien Cave / New York Times — https://www.nytimes.com/2026/09/23/world/ai-gallup-poll.html?unlocked_article_code=1.DVE.YqAd.JnPw-sQidvkd&smid=url-share
   A Gallup poll found that a majority of people surveyed across 37 countries said they were curious or excited about artificial intelligence, more than scared or worried.
   > @adrianweckler: AI usage daily, weekly, monthly (& never) — Gallup poll of 37 countries eg Ireland — 25% daily, 18% weekly, 13% monthly, 45% none)
   > @faizalhamssin: Meanwhile, in Asia, A.I. optimism is prevailing. “In China and Vietnam, more than 90% of people polled said they believed that A.I. would mostly make daily life better. In Nigeria, Israel and Singapor
   Also: TechCrunch, Spyglass, Gallup, Mashable, Techstrong.ai, 404 Media, NewsMax.com, Semafor

13. Survey: US public perception of data centers has sharply deteriorated since January, with 54% viewing them as bad for the environment, as local opposition rises
   Brian Kennedy / Pew Research Center — https://www.pewresearch.org/short-reads/2026/09/22/americans-views-of-data-centers-have-turned-more-negative/
   > @johngramlich: How Americans view data centers' impact on: The environment: 54% bad, 4% good Home energy costs: 50% bad, 4% good Local quality of life: 49% bad, 4% good Local jobs: 24% bad, 22% good Local tax revenu
   > @johngramlich: 60% of Americans say they'd be not too or not at all comfortable with a new data center operating in their area. Majorities in urban, suburban and rural areas express that view, as do majorities in bo
   Also: The Register, The Washington Sun

14. Pilgrim, whose device combines air sampling and genomic sequencing to detect biological threats, raised a $25M seed led by Buckley at a $150M valuation
   Kate Clark / Wall Street Journal — https://www.wsj.com/tech/ai/anthropic-leaders-back-startup-developing-system-to-detect-biological-threats-88ef9f0a?st=S5V7SX&reflink=desktopwebshare_permalink
   Pilgrim has raised $25 million and has developed a 50-pound device that detects biological threats — Two Anthropic leaders are investing …

15. Sources: China's SASAC, which oversees state-owned companies, is surveying the number of Broadcom switches in state-backed data centers amid a domestic AI drive
   Financial Times — https://www.ft.com/content/b97dde39-7813-4a51-8176-3699e2a468b1
   Survey comes amid drive to boost domestic players and reduce reliance on foreign AI infrastructure
   > @choblin29: 🚨EXCLUSIVE: China is scrutinizing Broadcom's grip on its AI data-center networks. A government survey found Broadcom switches make up as much as 90% of networking equipment at some state-owned compani
   > @rohanpaul_ai: FT: So much focus in China on hardware independence. Now its weighing curbs on Broadcom switches that may account for up to 90% of state-backed data-centre deployments. China's State-owned Assets Supe
   > @photoncap: - China conducting audit of $AVGO equipment amid domestic AI chip advancement efforts - Potential regulatory scrutiny tied to US export controls on advanced semiconductors - Move reflects broader tens
   > @rebel44cz: Many Western companies are also abandoning everything remotely related to Broadcom because of their criminally stupid way of handling VMware... So, please pick a different company we should be sorry a
   > @jukan05: China is pursuing full-stack hardware independence, including switches.
   Also: Reuters, Finimize

16. OpenAI says it will give its AI cyber defense system Daybreak and GPT-5.6 Sol to the Ukrainian government for free to help it protect civilian infrastructure
   Zoe Kleinman / BBC — https://www.bbc.com/news/articles/c90kly26d7pzo
   The tech giant OpenAI will share its AI cyber defence system Daybreak for free with the Ukraine government to help …
   Also: CyberScoop, OpenAI, Unite.AI, International Business Times

17. Seattle-based satellite startup Hubble, which is working to enable global Bluetooth connectivity, raised $200M at a $1.6B valuation, for $300M in total funding
   Sana Pashankar / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-23/startup-hubble-reaches-unicorn-status-for-space-based-bluetooth?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MDE2OTU3OSwiZXhwIjoxNzkwNzc0Mzc5LCJhcnRpY2xlSWQiOiJUTFFCTjFLSkg2VjQwMCIsImJjb25uZWN0SWQiOiJCRkI5RDA1ODU3NzI0QTVFQTU5ODA4NzhDRDQ4MjlEOCJ9.8JRkdEP29iEjh2rwiO1RybDDbGjxSApSNrNbb5htYBs&leadSource=article-gifting
   Satellite startup Hubble Network raised $200 million in a new funding round, taking the company's valuation to $1.6 billion …
   Also: SiliconANGLE, Hubble Network, GeekWire, FinSMEs

18. Anthropic and OpenEvidence partner to offer a specialized version of OpenEvidence's AI search tool for physicians in about 100 low- and middle-income countries
   Nancy Lapid / Reuters — https://www.reuters.com/legal/litigation/anthropic-openevidence-partner-bring-medical-ai-worldwide-2026-09-22/
   Artificial intelligence startup Anthropic and medical knowledge platform OpenEvidence are collaborating to bring AI-powered …
   Also: International Business Times, PYMNTS

19. Ema, which uses AI agents to automate corporate processes across HR, IT, and finance, raised a $77M Series B led by Creaegis, taking its total funding to $140M
   Jagmeet Singh / TechCrunch — https://techcrunch.com/2026/09/23/ema-raises-77m-as-ai-starts-eating-into-enterprise-software-and-services/
   Ema, a startup that uses teams of AI agents to automate corporate processes across HR, IT, and finance, has raised $77 million …
   Also: The Economic Times, FinTech Global, PYMNTS, FinSMEs, Times of India, SiliconANGLE, Forkast

20. A Facebook co-founder proposes creating an “Office of AI Supervision” to embed teams inside frontier AI labs, with a three-year term to avoid regulatory capture
   Chris Hughes / Financial Times — https://www.ft.com/content/58be9a1b-345c-4026-a738-989b72858c4f
   Both industries change rapidly and reach throughout the economy, requiring officials to weigh the benefits of innovation against risks
   > @alexeheath: we are at the ‘people who tried to regulate social media are back’ point of the cycle [embedded post]
   > @thestalwart: Piece in the FT from Facebook co-founder Chris Hughes arguing that the bank supervision model is the right template for AI regulation https://www.ft.com/...

21. Bessemer raised $5.75B, allocating $4B to growth-stage funding, including young companies raising large rounds at high valuations, and $1.75B for early-stage
   Natasha Mascarenhas / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-23/bessemer-raises-5-75-billion-in-new-funds-expands-growth-efforts
   Bessemer Venture Partners is set to announce $5.75 billion in fresh funding to support a broader shift towards more growth stage investments …
   > @bessemervp: New funds are here 🚀 $5.75 billion in new capital to continue the work in the AI era. Forged in steel. Building what's next: https://www.youtube.com/... [video]
   Also: CTech, Pulse 2.0, Bessemer Venture Partners on YouTube, Bessemer Venture Partners

22. Anthropic reported disrupting a Beijing-aligned operation to monitor religious leaders and diaspora communities, including a DC-based advocacy group for Tibet
   Richard Gere / Wall Street Journal — https://www.wsj.com/opinion/beijing-turns-ai-against-tibetans-worldwide-a95c6132?st=ybtPN4&reflink=desktopwebshare_permalink
   Anthropic uncovers a Beijing-aligned operation targeting my organization among other dissidents.

23. Qualcomm unveils the Snapdragon 8 Elite Gen 6 and 8 Elite Extreme Gen 6, both on TSMC's 2nm process, with two 5GHz prime cores and six 4GHz performance cores
   Axel Metz / TechRadar — https://www.techradar.com/phones/android/qualcomm-just-announced-the-snapdragon-8-elite-gen-6-and-8-elite-extreme-gen-6-for-next-gen-android-phones-heres-how-and-why-the-two-chipsets-differ-and-which-phones-could-be-supported
   Extreme by name, extreme by nature — Qualcomm has announced not one, but two new flagship mobile chipsets at its annual Snapdragon Summit …
   > @ryansmithat: 5GHz is not a barrier. It is a threshold. A barrier repels you. (I know that's QC's phrasing, not yours, Jim. But it's still a poor choice of words on their part)
   > @samirkhazaka: Turns out the Dimensity 9600 Pro is extreme. MediaTek announced support for up to 30B parameter MoE models a week ago. Qualcomm announced the same today on Snapdragon 8 Elite Extreme Gen 6.
   > @tekstrategist: @Qualcomm breaks the CPU 5GHz barrier with the Oryon cores in the new Snapdragon 8 Elite Gen 6 SoCs. #SnapdragonSummit
   > @moto: Revealing our most advanced smartphone yet at #SnapdragonSummit, motorola signature 27. Here's what to look forward to: - Our best camera system yet. - The only smartphone in the market to feature aud
   > @qualcomm: A new chapter of @Snapdragon mobile innovation begins today. More intelligence. More performance. More possibilities.
   Also: Qualcomm, 9to5Google, TechCrunch, Tech Advisor, The Verge, Wccftech, Tom's Guide, The Verge, +37 more

24. A profile of Noah Shinn, founder of AI assistant Instinct, who soft-launched it as an invite-only site for VCs and is reportedly fundraising at a $10B valuation
   Business Insider — https://www.businessinsider.com/noah-shinn-instinct-ai-competes-meta-muse-2026-9
   Noah Shinn was publishing influential AI research before he graduated from college. Now, at the ripe age of 23, he's taking on Mark Zuckerberg.
   > @businessinsider: Instinct's breakout has turned a college dropout into one of AI's hottest young founders and put his tiny startup in direct competition with another company started by a college dropout: Meta. Noah Sh

25. Sony Music becomes the first music company to join ARIAM, which advocates for responsible AI adoption in the creative industry and includes the NYT and Disney
   Corbin Bolies / Variety — https://variety.com/2026/music/news/sony-music-group-joins-ai-content-coalition-ariam-1236873137/
   Sony Music Group has joined the Alliance for Responsible Innovation in the Arts & Media (ARIAM), becoming the first music company …
   Also: Billboard, Music Ally, Music Business Worldwide

26. London-based AI life sciences startup Basecamp Research raised a $140M Series C led by S32, with participation from Anthropic, taking its total funding to $225M
   John Reynolds / Tech.eu — https://tech.eu/2026/09/23/anthropic-and-nvidia-back-basecamp-research-in-140m-series-c/
   Basecamp says it will use the funding to train a new generation of its AI models. — A UK life sciences startup using AI …
   Also: Reuters, Basecamp Research, FinSMEs, Unite.AI, Pulse 2.0, Endpoints News

27. Carnegie China: China passed the US as the top destination for elite AI talent in 2025, rising from 2022's 27.1% share to 40.6%; the US fell from 46.4% to 34.2%
   Claudia Chong / The Information — https://www.theinformation.com/briefings/china-leads-u-s-top-ai-talent-study-finds
   Chinese AI researchers have increasingly opted to stay and work in their home country, leading China to become the top destination …
   > @appendixzeroai: This might be the most interesting number in the whole report: 3,619 researchers followed a China → China → China path: Chinese undergrad, Chinese grad school, now working in China. China → US → US: 1
   > @appendixzeroai: But this isn't a story of the US suddenly losing its ability to attract talent. The US still has by far the largest net talent gain: +2,145 in Carnegie's sample. China is at -1,729. What changed is th
   > @hsu_steve: Carnegie report on NeurIPS 2025 authors and AI talent flow. US AI is heavily dependent on attracting talent from PRC. But PRC talent pool is larger than RoW combined. Largest pool of AI talent - capab
   > @appendixzeroai: Carnegie just dropped its new AI Talent Tracker and the shift since 2022 is pretty striking. Among the NeurIPS researchers in its sample, 57.4% did their undergrad in China, up from 46.3% in 2022. The
   > @appendixzeroai: China has now overtaken the US as the main place these researchers work. 2022: 🇺🇸 46.4% 🇨🇳 27.1% 2025: 🇨🇳 40.6% 🇺🇸 34.2% That's a massive shift in just three years. The old picture of China producing 

28. NADI, a new DARPA-like Dutch government agency, launches a €40M challenge to accelerate chip design with AI in collaboration with its German counterpart SPRIND
   Toby Sterling / Reuters — https://www.reuters.com/business/german-dutch-strategic-innovation-agencies-collaborate-ai-chip-design-2026-09-23/
   A new Dutch government agency set up to achieve strategic innovation will work with its German counterpart to pursue breakthroughs …
   Also: Tech.eu, Telecompaper

29. Six major banks, including BofA and Capital One, warn that increased autonomy for agentic commerce chatbots could lead to more scams, fraud, and disputes
   Ece Yildirim / Gizmodo — https://gizmodo.com/big-banks-say-theyre-uneasy-about-people-shopping-via-ai-agents-2000815443
   Agentic commerce could increase the amount of scams, fraud and disputes, the banks warn in a new report.

30. Portuguese surveillance drone maker Tekever raised $580M led by UC Investments at a $6.4B valuation, after securing a UK MOD contract worth £400M over 10 years
   Henrique Almeida / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-23/drone-maker-tekever-seeks-deals-after-new-round-s-first-close
   Tekever, a Portuguese developer of surveillance drones, is seeking acquisitions after the first close of a funding round that targets raising $580 million.
   Also: Reuters, FinSMEs, CNBC, Quartz, Financial Times, Resilience Media, Tech Funding News, Ventureburn

31. HypeAuditor: OpenAI doubled its sponsored Instagram posts promoting ChatGPT from 61 in June to 122 in July, rising again to 141 in August, as it seeks new users
   Business Insider — https://www.businessinsider.com/inside-open-ai-influencer-marketing-strategy-chatgpt-ads-sponsorships-instagram-2026-9
   Also: Rolling Stone, Inc.com, CyberInsider

32. Analysis: 30 Chinese tech stocks with the largest overseas revenue exposure returned 36% YTD, outperforming the 8% return from domestically dependent peers
   Bloomberg — https://www.bloomberg.com/news/articles/2026-09-22/china-s-ai-trade-favors-global-winners-over-local-champions
   Also: Zeekr Intelligent Technology …

33. Ofcom opens an investigation into Pornhub owner Aylo to determine whether it has complied with OSA requirements to prevent under-18s from accessing porn
   Reuters — https://www.reuters.com/technology/uk-media-regulator-investigates-pornhub-over-age-checks-2026-09-23/
   Also: Financial Times, The Verge, BBC, The Guardian, The Register, The Independent, Ofcom, Politico

34. Chinese chip foundry CanSemi, focused on automotive, industrial, and IoT chips, files for an IPO on Shenzhen stock exchange's ChiNext, seeking to raise ~$919M
   Sangmi Cha / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-23/cansemi-tech-joins-china-chip-ipo-wave-with-919-million-deal
   Also: Reuters

35. German publisher C.H.BECK takes a majority stake in Noxtua, which develops AI tech to research, analyze, and draft legal documents and raised a $100M+ Series C
   Cate Lawrence / Tech.eu — https://tech.eu/2026/09/23/noxtua-raises-more-than-eur100m-as-chbeck-takes-majority-stake-german-legaltech/
   Also: Artificial Lawyer, Noxtua, RuntimeWire, Startup.eu

36. Global AI glasses shipments, including display-less and AR and AI glasses, rose 263% YoY in H1 2026, driven by Meta and EssilorLuxottica's display-less lineup
   Counterpoint Research — https://counterpointresearch.com/en/insights/global-ai-glasses-shipments-surge-263-percent-yoy-with-display-less-ai-glasses
   > @craigweiss: i think I'm starting to see meta's vision: muse + meta glasses shit, they're going to be unstoppable
   Also: 9to5Mac, The Mac Observer

37. Go.AI, which offers on-premises AI hardware and software tools for regulated organizations like banks, raised an $85M Series A led by Updata Partners
   Ryan Lawler / Axios — https://www.axios.com/pro/fintech-deals/2026/09/22/go-ai-85m-series-a-bank-ai-appliances
   Also: Chicago Business Journal, The SaaS News, Go.AI, RuntimeWire

38. Alibaba says it plans to build its first cloud regions in Turkey, Finland, and the Netherlands over the next 12 months, amid escalating US-China AI tensions
   Bloomberg — https://www.bloomberg.com/news/articles/2026-09-23/alibaba-to-add-data-centers-in-europe-middle-east-in-ai-push
   Also: Quartz, Türkiye Today, Hello China Tech, South China Morning Post, Tech in Asia, Dow Jones Newswires

39. Xbox has become a shell of its former self, weighed down by job cuts and studio closures, as it focuses on franchises like Halo and reaching “a billion people”
   Andrew Webster / The Verge — https://www.theverge.com/games/998758/xbox-activision-blizzard
   > @realmrclutch: I was thinking this. Xbox games studios publishing has shrunk in favor of Bethesda, activision and blizzard finally admitting what even Xbox bots still refute till this day. That Xbox has been mid. An
   > @stephentotilo: Added a statement from Activision's president regarding Halo, says they've “begun assembling” a team for the next Halo.
   > @jezcorden: BREAKING: I guess that July rumor I had about Halo going under Activision wasn't so crazy after all. Activision is building a new team to build Halo games, Obsidian is going under Bethesda, and Ninja 
   > @tomwarren: Microsoft is laying off 268 Xbox staffers and Ninja Theory may close. Two deals to sell Ninja Theory fell through over the summer. Details 👇 https://www.theverge.com/...
   > @nintyprime: I feel for the 230 lost jobs at Halo Studios or whatever, but shifting the franchise to be under the arm of Activision and the powerhouse they have created in CoD is probably the best move Microsoft h
   Also: Kotaku, XBOX Wire, Game Developer, Wccftech, Eurogamer.net, Pure Xbox, The American Bazaar, Radio Times, +20 more

40. Sources: AI training data startup Micro1 raised $100M+ at a $4B valuation, up from $500M in September 2025; two frontier AI labs and xAI co-founders invested
   Anna Tong / Forbes — http://www.forbes.com/sites/annatong/2026/09/22/this-25-year-old-raised-over-100-million-for-his-ai-data-startup-at-a-4-billion-valuation/
   Also: Forbes Australia

41. Rabbit launches OS3, a cloud AI agent that connects to local apps and files on Windows, Mac, and Linux and works via web, Telegram, iMessage, or its R1 device
   Julian Chokkattu / Wired — https://www.wired.com/story/rabbit-r1-os3-jesse-lyu/
   > @cocktailpeanut: R1 users should be able to just chat with OS3 just like Jesse is doing, completely hands free, and with zero button pushing. Basically an always-on, portable Alexa/Google Home — Wake it up with a cust
   > @jesselyu: today we launch OS3 - our latest agent system that runs local on your devices, with a freedom of BYOK and model of your choice. watch the video and try it now at https://rabbit.tech/
   > @rabbit_hmi: bring your own API key. choose your models. add skills by pasting a URL. switch models without starting over. OS3 is live for everyone. our new website, FAQ and support guides are at https://rabbit.te
   > @rabbit_hmi: shared context across web, Telegram and r1. pair your phone to send tasks via SMS or iMessage. onboard at https://os3.rabbit.tech/ to route r1 queries through OS3. your rabbithole data comes with you;
   > @rabbit_hmi: give it the job, not instructions for every click. OS3 can research the web, work with your files and browser, and write and run code. connect up to 5 Mac, Windows or Linux computers with the rabbit a
   Also: SiliconANGLE, rabbit inc., Help Net Security, The Verge

42. Data security startup Cyera raised $400M from Goldman Sachs in a Series G extension, bringing its total funding since June 2025 to $1.94B
   James Rundle / Wall Street Journal — https://www.wsj.com/pro/cybersecurity/cyera-raises-400-million-from-goldman-in-extension-round-0643389c?st=YfcfGj&reflink=desktopwebshare_permalink
   Also: SiliconANGLE, CTech, WOWTALE, FinTech Global, BusinessWire

43. Microsoft says it will give DARPA on-site access to its latest quantum computing hardware, including the Majorana 2 chip, at its new Maryland research center
   Stephen Nellis / Reuters — https://www.reuters.com/business/microsoft-give-darpa-hands-on-access-to-quantum-system-new-maryland-site-2026-09-22/
   Also: The Quantum Insider, Microsoft Quantum, RuntimeWire, Quartz, Tech Times, The Quantum Insider, Constellation Research

44. Sources: Scott Bessent is emerging as a frontrunner for the AI czar position; other names include WH OSTP Director Michael Kratsios and OPM Director Scott Kupor
   Semafor — https://www.semafor.com/article/09/22/2026/bessent-eyed-for-trumps-ai-czar
   > @willmanidis: PetroDollar -> Mag7Dollar AI policy is monetary policy now. [embedded post]
   Also: Reuters, Politico, Bitcoin Insider, crypto.news, Cointelegraph, Seoul Economic Daily, Gizmodo

45. ShinyHunters claims it used an Oracle PeopleSoft zero-day to hack FBI-related services and steal employee and applicant data, and also defaced the FBI jobs site
   Joseph Cox / 404 Media — https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/
   > @darkwebinformer: ‼️ ShinyHunters has shared a message on their pay or leak portal to Director Brett Leatherman of the FBI Cyber Division and Director Kash Patel of the FBI:
   > @_nathancalvin: I feel like lots of people have been asking “where is all the hacking we were warned …
   > @vxunderground: fbi job portal defaced and compromised? oh yeah, it's a silly tuesday
   > @olganyc1211: And of course, no one will be held accountable for this dangerous breach. Certainly, not Kash Patel
   > @michaeldweiss: This is extremely bad.
   Also: Reuters, Breitbart, Politico, New York Times, HotHardware, TechCrunch, The Record, Associated Press, +25 more

46. Anthropic raises its five-hour usage limits by 20% on Pro, Max, and Team plans, and gives subscription users a rate limit reset
   David Gewirtz / ZDNET — https://www.zdnet.com/innovation/anthropic-claude-opus-5-5-fable-5-1-performance-costs-less/
   > @gabrielelpidio: Anthropic having seemingly more compute than OpenAI wasn't in my 2026 cards
   > @argofowl: anthropic is back we are getting the first ever BANKED RESET from anthropic (yes a claude banked reset is here) + increased 5h usage limits shots fired, big sexy shots
   > @kimmonismus: Let that sink for a moment: - Opus 5.5 costs 40% less compared to Opus 5 - performs at Fable 5.1 level - is 30% faster in output - and you get a banked reset on top of that. They chose war with OpenAI
   > @llmjunky: Anthropic is now offering banked resets. Thank you Tibo! 🤪
   > @bridgemindai: OPUS 5.5 BENCHMARKS JUST DROPPED. It beats Fable 5.1 and GPT 6 Astra across the board. Agentic coding, knowledge work, reasoning, computer use, visual recognition. Opus 5.5 leads every single one. At 
   Also: Anthropic, Claude, The Information, New York Times, MakeUseOf, Latent.Space, Seoul Economic Daily, Digit, +13 more
