# Research — News Cluster

Search for news **events that occurred** between **2026-11-13 10:00 BRT** and **2026-11-16 10:00 BRT** (a 72-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it. One exception, the **agenda**: an event scheduled to happen before the next edition goes out (2026-11-17 10:00 BRT) — see the Agenda rule below.

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
| Big Tech and internet platforms outside AI — outages, security breaches, consumer products, platform policy, antitrust (not their financing: that follows the funding rows) | **ai** |

The rows above win. Only a story type no row covers goes to **ai** if it is about a software or internet company, **hw** if it is about physical hardware, **world** otherwise. A funding round, IPO or M&A of a company that is neither AI nor hardware (fintech, prediction markets, internet platforms) is always **world**. Every story has exactly one owner; when you defer a story, name the owner in your `rejected` reason, and if no sibling owns it, it is yours.

Apply the column for **your** cluster (named in your system prompt). The other
columns are off-limits — a sibling has them covered.

## Rules

- Up to 7 stories. Fewer is fine if the news day is thin for your cluster.
- Every URL must come from a search result or fetched page. Never invent URLs.
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-11-13 10:00 BRT to 2026-11-16 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
- **Agenda — what happens before the next edition.** A high-profile event in your beat with a set date between now and 2026-11-17 10:00 BRT (a launch, a vote, a ruling, an earnings release, a keynote, a summit) qualifies when its latest concrete confirmation (date set, license granted, vehicle on the pad, final schedule published) falls in the window. The reader opens the edition before the event and should know it is coming. Write it as a preview: what is planned, when (with the time and timezone from the source), and what is at stake. Add `"scheduled_at"` (ISO 8601 with offset) to the story. A launch, test or vote that is the first of its kind or the next step of a story the newsletter follows is high-profile; routine ones are not.
- **Salience over beat balance.** Before you pick, ask: what in my beat will a reader who follows tech and geopolitics hear about everywhere today? Those stories go in first, whatever the sub-area. A slot left empty while such a story sits in your search results is a miss.
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
2. **Landscape scan**: Review the Techmeme scan, then run 5 searches to fill gaps. One of the 5 is the **agenda search**: what in your beat is scheduled between now and 2026-11-17 10:00 BRT. Stop searching.
3. **Pick your 7 stories.** From what you found, choose 7. This is your final list — do not add stories after this point.
4. **Fetch only where needed**: For stories where search snippets lack exact numbers or quotes, fetch the source. Most stories won't need this.
5. Write the JSON output file, with the `rejected` log (below).

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
  ],
  "rejected": [
    {"headline": "What the candidate story was", "reason": "Why it stayed out (beat owner, no in-window event, minor, already covered, slot taken by …)"}
  ]
}
```

**Story fields**: `id` (unique kebab slug), `headline` (<100 chars), `key_facts` (3-8 sourced facts, each with `source_url` pointing to a listed source and `excerpt` with the supporting text), `sources`, `category` (1-3 from: technology, science, world, economy, finance, business, politics, brazil, sports, entertainment), `entities` ({organizations, people, places} — named entities from sources only). Optional `scheduled_at` (ISO 8601 with offset) for an agenda story that hasn't happened yet.

**`rejected`**: every story you considered and left out — anything in your beat that showed up in the Techmeme scan or your search results with real coverage. One line of reason each. It is how a missed story gets diagnosed later, so be specific.

**Source fields**: `url`, `outlet`, `title` (tweets: "Tweet by @handle: [first 80 chars]"), `published_at` (YYYY-MM-DD, fallback today), `image_url` ("" if unavailable), `type` (news_article|tweet|blog_post|paper|press_release|video|government_filing).

---

**Date:** 2026-11-16
**Research window:** 2026-11-13 10:00 BRT → 2026-11-16 10:00 BRT (72h)
**Agenda horizon (next edition):** 2026-11-17 10:00 BRT

**Previous edition headlines (2026-11-13 — skip unless genuinely new development):**
- google-gemini-4-hydrogen-launch: Google launches Gemini 4 Hydrogen, a fast model near Sonnet 5.5 and GPT-6.1 Sol at $1.50/$7.50
- openai-daybreak-red-team-defense-factory: OpenAI launches Daybreak Red Team and Defense Factory, AI agents that pentest and patch code
- mirendil-1b-series-a-ai-rd-agents: Ex-Anthropic researchers' Mirendil raises $1B Series A to automate frontier AI research with agents
- anthropic-anvil-automated-red-teaming: Anthropic's automated red-teamer Anvil beats human experts at jailbreaking Claude's safeguards
- openai-raises-15b-1-25t-valuation: OpenAI raises $15B at $1.25T valuation, half its original $30B target, CNBC reports
- anthropic-ipo-six-times-oversubscribed: Anthropic's IPO is about six times oversubscribed; bankers to prioritize existing backers
- meta-muse-outbound-calling-paid-us: Meta's Muse AI agent can now phone US businesses for paying subscribers
- nvidia-huang-resigns-kress-interim-ceo: Jensen Huang resigns as Nvidia CEO; CFO Colette Kress named interim chief, Harvey Jones chair
- senate-banking-summons-huang-lutnick-export-controls: Senate Banking chair asks Huang and Lutnick to testify on Nvidia chip exports; Lutnick agrees
- spacex-74b-data-centers-texas-arizona-terafab-grimes: SpaceX plans $74B in AI supercompute campuses in Texas and Arizona, picks Terafab chip site
- nscale-amended-s1-needs-financing-anthropic: Nscale's amended IPO filing: $1.69B loss, $5.5B debt, more financing needed for Anthropic build
- cerebras-q3-beat-microsoft-deal: Cerebras beats Q3 estimates, signs Microsoft as third hyperscaler customer; stock jumps 17%
- samsung-talks-acquire-modine-cooling: Samsung in talks to buy US data-center cooling maker Modine; shares jump 28% after hours
- xfusion-clears-shenzhen-review-1-2b-ipo: Chinese AI server maker xFusion clears Shenzhen review for $1.2B ChiNext IPO
- europe-seat-ukraine-talks-dublin-pow-swap: After Dublin meeting, US says Europeans will join next Ukraine talks; largest POW swap agreed
- trump-no-iran-deal-needed-brent-jumps: Trump says US doesn't 'need a deal with Iran', pulls Vance off talks; Brent jumps 3.3%
- treasury-10y-above-5-1-fed-hike-bets: US 10-year yield tops 5.1% as Fed officials signal more hikes; December increase fully priced
- doj-seizes-1-2b-north-korea-binance-hack: DOJ moves to seize $1.2B stolen by North Korea from Binance; dismantles deepfake 'FaceStealer' scheme
- kalshi-65b-valuation-talks-trump-jr-exits: Kalshi in talks to raise at $65B weeks after $40B round; ends Donald Trump Jr.'s advisory role
- spacex-tesla-merger-talks-december: SpaceX and Tesla merger talks advance; record deal could be announced as soon as December

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 43 stories

1. Sources: Jensen Huang has discussed a comeback as Nvidia CEO with confidants, as allies form a “war room” to lobby for his return and seek White House support
   Financial Times — https://www.ft.com/content/45383d86-33c4-4d99-86e5-5e058d3567c1?accessToken=zwAAAaHhCqBRkc9FOD2GM8RNmdOG5V4FjTVnwQ.MEYCIQCZEg_GADuUi3HMzfVy4L3GgdXzwW5GpeLTdxDHbMhYXQIhAKQz7pVUZgb0WKGUJq30p1B5vEF2gPlUop1e8Yzyol24&sharetype=gift&token=35d995ef-ed14-4cc4-8323-31a3da06ba1b&syn-25a6b1a6=1
   Tech supporters lobby chipmaker's board to reinstate former CEO after he resigned following affair with alleged Chinese spy
   > @divestech: No one individual can replace Jensen as CEO....but at the end of the day after this global scandal the old Jensen with the black leather jacket and rock star persona is gone for good....that cannot be
   > @jyarow: Market hates the idea of Jensen coming back
   > @thestalwart: NASDAQ-100 futures solidly red. $NVDA down another 2.3% pre-market
   > @munster_gene: I now put the odds Jensen returns at 51%. On Friday I had it at 10%. Kalshi currently has it at 9%. Two reasons for my increased odds: 1. The bring back Jensen movement is gaining momentum. 2. Jensen 
   > @jimcramer: If a board's only duty was to the shareholders than, of course, we want Jensen back. But a board has to be concerned with ethics and national security.. Hence why Nvidia's board felt it had to act... 
   Also: Stand with Jensen, Bloomberg, Fortune, Reuters, BBC, CNBC, The Verge, The Guardian, +42 more

2. Sources: Jensen Huang had planned to pull back Nvidia's aggressive financing and told neoclouds to get upfront customer payments; Colette Kress may go further
   Wall Street Journal — https://www.wsj.com/tech/ai/nvidias-days-as-an-open-checkbook-for-the-ai-economy-are-numbered-90c7b388?st=LGBxVv
   Interim CEO Colette Kress is expected to rein in deals after a stretch in which Nvidia aggressively financed computing deals and startup investments
   > @linda__stevens: Wow. It was all a scam.
   > @nntaleb: The guy starts a company, invents a new technology, then is dethroned by a board composed of virtue faking empty suits who never did anything other than powerpoint presentations, while the Epstein cro
   > @anissagardizy8: NEW: We continue to learn more and more about how Nvidia's plans to finance the AI boom were running into issues—even before Jensen was ousted. Nvidia's Days as an Open Checkbook for the AI Economy Ar
   > @tidefallcapital: “Jensen was laying the groundwork to pull back on backstopping. Companies would need to secure upfront payments from customers, that would make their projects easier to finance and ensure that $NVDA w
   > @edzitron: Jensen Huang feared back in August that he had overbought capacity at TSMC/memory firms. It seems that his resignation is the opening NVIDIA has to sneak out stories about demand slowing for its GPUs.
   Also: Reuters, Fortune, The Information, Daily Mail, Financial Times

3. Jensen Huang's resignation causes dismay and disbelief in Taiwan, his birthplace and where he is “the people's dad”; an official expects little impact on TSMC
   Li Yuan / New York Times — https://www.nytimes.com/2026/11/15/business/jensen-huang-taiwan.html?unlocked_article_code=1.QlE.zIv0.e4PF00FGssfU&smid=nytcore-ios-share
   > @liyuan6: The Nvidia chief executive's resignation shocked people in his birthplace, where he is called “the people's dad.” My latest https://www.nytimes.com/...
   > @basuashis: Age-restricted adult content. This content might not be appropriate for people under 18 years old. To view this media, you'll need to log in to X. Learn more
   > @michhuan: “The People's Dad” is a fitting moniker for someone who went out of his way to help the People's Republic
   Also: Semafor, Focus Taiwan

4. Alibaba releases Qwen4-Max, its new flagship 2.4T-parameter MoE model with a 1M-token context window, saying it beats Qwen3.8-Max with up to ~50% fewer tokens
   Qwen — https://qwen.ai/blog?id=qwen4-max
   Today, we are introducing Qwen4-Max, your new AI teammate for work, creativity, and discovery.
   > @openrouter: Qwen4 Max from @Alibaba_Qwen is live on OpenRouter. The first model in the Qwen4 series, built for coding, office work and long-horizon agents.
   > @kimmonismus: Interesting release: Qwen has launched Qwen4-Max, their new AI model with native vision and a 1 million-token context window. Outperforms Opus 5.5 and GPT-6.1 Sol/Astra on relevant benchmarks bot lack
   > @xeophon: it's so over
   > @arena: Qwen4-Max by @Alibaba_Qwen is the #1 Chinese model on the leaderboard making Alibaba now the #1 Chinese lab and #5 lab overall, just behind Anthropic, Google, OpenAI and Meta. It debuts overall at #14
   > @soumilbhandari: @arena @Alibaba_Qwen +74 over qwen3 is a big jump
   Also: Computerworld, Wccftech, RuntimeWire, Dow Jones Newswires, TechNode

5. Qwen4-Max scores 43 on the Artificial Analysis Intelligence Index, beating Qwen3.8 Max at ~67% lower cost per task but trailing Kimi K3.1 Pro at ~11% lower cost
   Artificial Analysis — https://artificialanalysis.ai/models/qwen4-max
   > @emollick: I think contrary to many of our expectations, we have not seen a Fable class open model more than 8 months after Fable/Mythos was first made public.
   > @kimmonismus: Qwen 4 is not a good release. Although it appears on paper to be on par with Opus 5.5 in key benchmarks, the AA Index paints a completely different picture. The fact that Qwen is being cut off from di
   > @solivagant7777: Chinese frontier models are trying their hardest just to reach Haiku-level performance. 💀
   > @mert_gulsun: [personal opinion] We might be in this interesting “middle period” where Chinese chips and data pipelines have not fully caught up to US ones yet. Furthermore, next year the compute gap will be wider.
   > @steadeepanda: @ArtificialAnlys @ArtificialAnlys what happened to the 700+ models you have they no longer appear in the list, it was a good way to track and see the improvement? Also UI keeps changing every now and 
   Also: Artificial Analysis

6. Alibaba says Qwen4-Max, which isn't open weight, beats Fable 5.1 and Kimi K3.1 Pro in coding benchmarks, and plans to release weights for smaller Qwen4 models
   Luz Ding / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-16/alibaba-unveils-new-flagship-ai-model-in-riposte-to-us-rivals
   Also: Intelligence Report

7. Alibaba says it filtered Qwen4-Max's training data to remove offensive cyber capabilities and mitigate chemical, biological, radiological, and nuclear risks
   Ann Cao / South China Morning Post — https://www.scmp.com/tech/big-tech/article/3374540/alibaba-says-new-flagship-ai-model-cuts-task-costs-60-while-tightening-cyber-guardrails
   Also: Reuters, Finimize

8. Apple launches its Health AI Usage Study, with an OpenEvidence-powered app that answers health questions and can use HealthKit data, for up to 200,000 US users
   Ivan Mehta / TechCrunch — https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/
   Big AI labs like OpenAI and Anthropic have made their bets on offering chatbots that can answer health-related queries with specialized features.
   > @orskyai: Apple is recruiting 200,000 US users with iPhone 15 Pro and iOS 26 to test AI health tools in a new study with OpenEvidence. It is fascinating to see how they are integrating HealthKit data-like sleep
   > @tymphillips: @aaronp613 Not Duo optimized 😏
   > @aaronp613: Apple launches research study to explore the use of AI for health The Apple Health AI Usage Study, conducted in collaboration with OpenEvidence, will evaluate trust, comprehension, and real-world heal
   > @zomeha38: @aaronp613 That visit summary needs to stay short enough for a doctor to actually read
   > @spherenx: @aaronp613 Better pay up, Amazon gave me $300 for there Amazon One Medical AI study. Apple thinks im opting into this for free? Nope. Shouldn't have made HomeView $299 greedy piece of trash.
   Also: Apple, 9to5Mac, AppleInsider, MacRumors, ABC News, The Verge, CNET, RuntimeWire, +13 more

9. Preliminary report: Microsoft attributes a major 365 and Exchange outage to a software defect introduced in a July 2026 update for network gateway servers
   Richard Speed / The Register — https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026
   Summer code change caused a Fall fail - frantic engineers had to patch the patch instead of rolling back
   > @clamanna: More details on the root cause can be found in the Microsoft 365 Admin center, and an abridged version can be found below. We are deeply sorry for the impact to all our customers and recognize the imp
   > @trace_cohen: Ok seems crazy technical at such a massive scale
   > @puneetck: We are sorry for the impact last week's incident has had on your business. The preliminary Post Incident Review for the incident is now available in the Microsoft 365 Admin center.
   > @kharaykraykray: So in summary: 1. Microsoft 365 program had a contention bug written in July and the bug remained dormant 2. …
   Also: PCMag, XDA Developers, The Stack, Neowin, Cyber Security News

10. Sources: the Trump administration plans to name Nvidia, Amazon, Microsoft, OpenAI, and Anthropic among 24+ AI “national champions” to help win overseas business
   Wall Street Journal — https://www.wsj.com/tech/ai/trump-administration-to-name-nvidia-among-ai-national-champions-c9284344?st=e6my7o&reflink=desktopwebshare_permalink
   The new program is part of an effort to help U.S. AI companies compete for business overseas
   > @timsweeneyepic: The designation of national champions changes that, and risks tainting those companies with the appearance of state control or political alignment in a way that could undermine trust in them domestica
   > @timsweeneyepic: The government shouldn't pick winners and losers in markets nor CEOs of companies. America is a country where everyone has a chance to start a business, to have a fair chance to compete, and succeed o
   > @npunwani: Nvidia, Amazon, Microsoft, OpenAI, and Anthropic will be designated as “national champions” by the Trump Admin and will receive expedited export licenses, government support, federal financing Welcome
   > @edzitron: And if there's one company we know has some expertise in “overseas business” it's NVIDIA [embedded post]
   > @pstasiatech: Nvidia will be one of more than two dozen companies designated AI “national champions” as part of an effort by the Trump administration to help AI firms win business overseas Kind of a no brainer.... 
   Also: The Verge, Business Today, Reuters, naked capitalism, The Daily Beast, Forbes, Hindustan Times, Jerusalem Post, +2 more

11. Amazon loses 40 Leo satellites after ULA's Vulcan rocket fails 10 minutes into flight, marking the first mission failure for the Boeing-Lockheed joint venture
   Joey Roulette / Reuters — https://www.reuters.com/business/aerospace-defense/us-rocket-fails-after-launch-payload-amazon-internet-satellites-destroyed-2026-11-15/
   A Vulcan rocket owned by United Launch Alliance, the joint venture of Boeing (BA.N) and Lockheed Martin (LMT.N) …
   > @ulalaunch: Based on data received by our Launch Director, we confirm that the Vulcan vehicle launched from Space Launch Complex 41 suffered an anomaly 10 minutes into the flight and failed to deliver the Amazon 
   > @amazonleo: There is risk with any launch, and that's especially true for inaugural missions like LV-01. ULA has been a trusted partner for Amazon, and we believe they'll learn from this mission and deliver on th
   > @elonmusk: Let's take this gentleman's argument at face value that anyone can throw money at rockets and get something like Starship, Falcon or Dragon. Perhaps he can explain to everyone how SpaceX is able to ca
   > @cosmos4u: A Vulcan rocket and 40 Amazon Leo broadband satellites fell back to Earth minutes after liftoff Sunday, a crushing setback that will ripple across the US space industry: https://arstechnica.com/... - 
   > @sciguyspace: Yes, Scott, and we're all thinking it. But we've all be studiously avoiding saying anything about this in order to not manifest the worst possible outcome!
   Also: Ars Technica, DatacenterDynamics, GeekWire, The Verge, Bloomberg, Aviation Week, Simple Flying, Coinpedia Fintech News, +9 more

12. Fan fiction website AO3, run by nonprofit Organization for Transformative Works, returns online after a “security incident”, ahead of its four-week timeline
   Adeel Hassan / New York Times — https://www.nytimes.com/2026/11/15/arts/ao3-fan-fiction-site.html?unlocked_article_code=1.Q1E.JOzR.v1pS94jn07St&smid=url-share
   The archive, which is home to tales inspired by the likes of “Harry Potter” and “Heated Rivalry,” was taken down more than two weeks ago, leaving its fans bereft.
   Also: Organization …, Digital Trends, Engadget, Mashable

13. Source: Musk will attend this week's APEC summit in Shenzhen, where Trump, Xi, and Putin will meet; many US business leaders may skip over scheduling conflicts
   Nikkei Asia — https://asia.nikkei.com/politics/international-relations/apec/apec-china-5-things-to-know-about-xi-jinping-s-diplomatic-show
   SHANGHAI/HONG KONG/TOKYO — China is hosting the 33rd Asia-Pacific Economic Cooperation forum in the southern tech hub of Shenzhen this week.
   Also: International Business Times, The Hill, Reuters, The Guardian, Associated Press, ABC News, NPR, Bloomberg, +4 more

14. The US and Pax Silica allies, including Japan, the UK, and India, agree to create a joint list of AI technologies and supply chains to protect from China
   Financial Times — https://www.ft.com/content/3c2197fc-9618-4838-91e6-522ce1a96a22
   > @ravikarkara: The US and its allies have agreed to jointly identify and protect artificial intelligence technologies …
   Also: Bloomberg, Reuters, Times of India, AIM, Hindustan Times, Associated Press, Australian Financial Review, Business Today, +2 more

15. Apple is launching a video podcasts section on the Apple TV app, initially for developer testing, and plans to increase video podcasts on its Podcasts app
   New York Times — https://www.nytimes.com/2026/11/16/business/media/apple-tv-podcasts-youtube.html?unlocked_article_code=1.Q1E.xu1z.aQGKo_cvhI1L&smid=url-share
   They will soon be free to all Apple TV users and will appear on more than 1 billion devices that have the app, including Rokus and smart TVs.
   Also: 9to5Mac, MacRumors, Mashable, Digital Trends, TVBEurope, iThinkDifferent

16. SK Hynix and the South Korean government plan to partner to build Trinity Fab, a $654M chip testing facility letting suppliers test products on 12-inch wafers
   Yoolim Lee / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-16/sk-hynix-plans-chip-testing-hub-to-boost-smaller-korean-players
   By continuing, I agree to the Privacy Policy and Terms of Service. … Explainers
   Also: MoneyToday, Korea JoongAng Daily, Seoul Economic Daily

17. SK Hynix says it plans to spend ~$1.05B over five years to support domestic suppliers of chip materials, parts, and equipment, strengthening its supply chain
   Heekyong Yang / Reuters — https://www.reuters.com/world/asia-pacific/sk-hynix-spend-1-billion-over-five-years-support-chip-suppliers-2026-11-16/
   Also: AIM, Seeking Alpha, MoneyToday, Seoul Economic Daily, Nikkei Asia, The Korea Herald, Dow Jones Newswires, Tech in Asia

18. London-based Plural raised a €1B fund to back European startups, one of only a handful of European VCs that raised €1B+ in one go, planning to back 30+ startups
   Financial Times — https://www.ft.com/content/26e52d2a-b259-4283-af83-e2c75d67a2fc
   London-headquartered group announces one of region's biggest-ever venture capital fundings
   > @demishassabis: @pluralplatform ... Huge congrats Ian, exciting news!
   > @mikebutcher: *Interview: Plural confirms the rumours of a new €1bn fund to go deep into Europe's frontier tech* The fund was said to be raising “up to” €1 billion earlier this year. Themes for the new fund will in
   > @sebjohnsonuk: Plural is one of the greatest firms in Europe today: >> Backed the likes of Proxima, Olix, Helsing, The Exploration Company >> 3 of their partners invested in Anthropic's first round >> 10% of their p
   > @carinanamih: The founders building the next generation of global companies are here in Europe. We've raised €1bn to back them.
   > @andreasklinger: The best fund in Europe just raised EUR 1B! 🔥 Mark my words: Plural will be Europe's Founders Fund (and more).
   Also: Tech.eu, Pathfounders, Resilience Media, Reuters, Axios, Crunchbase News, Tech Funding News, VCWire

19. Tighter AI chip export rules are gaining bipartisan support in Congress, including a bill to block Chinese companies from accessing chips overseas
   Financial Times — https://www.ft.com/content/3062790a-553d-41b8-9c7d-bae17b9d2e29
   Jensen Huang's alleged affair with Chinese spy ‘increases momentum’ to crack down on US hardware reaching China
   Also: The Verge, CNN, CNBC, Radio Free Mobile

20. An interview with Rockstar executives at the company's Edinburgh HQ about GTA VI, encouraging players to avoid rampages, realism, building the game, and more
   Keza MacDonald / The Guardian — https://www.theguardian.com/games/ng-interactive/2026/nov/15/grand-theft-auto-vi-inside-rockstar-games
   The latest instalment of the epic crime saga is finally here. We visit Rockstar Games for a hands-on encounter with the cultural event …
   > @gtavi_countdown: New GTA 6 details from The Guardian's preview at Rockstar North: - It's the first title in the series to encourage empathy, as your actions will have some effect on how the game plays out - You can ro
   > @angelpoltava: >makes one of the protagonists Latinx >first game to have “basic human empathy”
   > @henrytheblasian: That's a hell of a quote
   > @landeur: “It's the first title in the series to encourage empathy...”
   > @discussingfilm: Rockstar Games explain why they took so long to develop GTA 6. “If you were a developer with these resources, the only developer with these resources, wouldn't you go for the most ambitious thing you 
   Also: Sam Lover, 80 Level, GamingBolt, IGN

21. Canada faces intense lobbying from Meta, Apple, Alphabet, and Signal over Bill C-22, which would compel them to retain and hand over metadata to the authorities
   Laura Osman / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-16/canada-s-carney-faces-meta-google-apple-backlash-over-lawful-access-bill-c-22
   Prime Minister Mark Carney's government is facing fierce pushback from Big Tech firms over security legislation …
   Also: FinTech Global, Tech Times

22. Wall Street's 10 biggest IPOs of 2026, including SpaceX, SK, and Cerebras, have fallen by an average of 20.5% from their offer prices, as the AI frenzy fades
   Emily Herbert / Financial Times — https://www.ft.com/content/7974acec-e378-4298-a1a7-2b16b00d8b32
   Ten biggest flotations have fallen more than 20% on average in 2026 after four years of gains — Wall Street's 10 biggest initial …

23. The US-led Pax Silica faces local backlash in the Philippines over a planned AI hub, with concerns about displacement, resources, and threats to sovereignty
    — https://www.nytimes.com/2026/11/16/business/trump-paxsilica-philippines-ai.html?unlocked_article_code=1.Q1E.S_8o.St--m43lJuOx&smid=url-share
   A planned American-led artificial intelligence hub in the Philippines has sparked fierce opposition over concerns about displacement …

24. Tech startups and VC firms are hiring for “ecosystem” roles, like “startup ecosystem lead”, to prioritize in-person networking and cut through AI marketing slop
   Lora Kelley / New York Times — https://www.nytimes.com/2026/11/15/business/tech-jobs-ai-ecosystem.html?unlocked_article_code=1.Q1E.Rex6.3x1x0jaexrm1&smid=url-share
   The people ushering in the artificial intelligence revolution are also doubling down on in-person relationships in their own industry.

25. Amazon's Prime Air drone service, which operates across 18 sites in 10 US states, is drawing local opposition; its Baton Rouge hub launches ~30 drones per hour
   Kris Maher / Wall Street Journal — https://www.wsj.com/lifestyle/amazon-delivery-drones-4807e976?st=WD5ZHf
   Aerial package drops draw plenty of gawkers, but some say they're destroying the neighborhood
   Also: DroneXL

26. Sources: Nvidia appealed to Taiwanese officials after its manager was charged over chip smuggling, and sought advice from TSMC, which declined to get involved
   Mackenzie Hawkins / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-15/nvidia-sought-taipei-s-help-over-employee-s-chip-smuggling-case
   Nvidia Corp. appealed to Taiwanese officials after prosecutors on the island accused an employee of helping to smuggle AI chips into China …
   Also: TechCrunch, Livemint, Digital Trends, Taiwan News

27. Scott Bessent urges Nvidia to hire an outside CEO and wants answers within 10 days on whether it pushed “seemingly illicit” chip sales to China to boost revenue
   Tony Czuczka / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-15/bessent-says-nvidia-needs-dramatic-shakeup-after-huang-ouster
   Tied for #1 on the AA Decision Index, Snap is a multimodal model with a 384k-token context window for fast reasoning and agentic decisions.
   > @niubi: odds of that effort to reinstate Jensen Huang succeeding close to 0 when the US Treasury Secretary says stuff like this “Bessent said Nvidia stopped breaking out Singapore revenue in its financial fil
   > @alexmaxham: @Techmeme @TonyCzuczka Us government choosing a CEO for a public company is crazy
   > @zephyr_z9: Based on what Besent is saying, Nvidia will likely now enforce server level location tracking from next year [embedded post]
   > @foundrceo: @Techmeme @TonyCzuczka treasury secretary picking nvidia's next CEO was not on my 2026 bingo card
   > @davesantamonica: Scott Bessent is launching a witch hunt. Nvidia and Jensen Huang followed the existing official export control list to the letter. Megaspeed was not on the Entity List at the time! You can't blame a c
   Also: Wall Street Journal, Bloomberg Law, Axios, Fox Business, CNBC, Yeni Safak English, NTD, Reuters, +8 more

28. Baidu reports Q3 revenue down 1% YOY to ~$4.6B, its sixth straight quarterly sales decline, and net income of ~$210M; AI businesses are now 50%+ of its revenue
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-16/baidu-posts-sixth-straight-sales-drop-after-ai-drag-persists
   Also: Reuters, Finimize, South China Morning Post, RuntimeWire

29. A look at China's push for AI literacy by 2030, as schools adopt AI-focused curricula, classroom cameras, and AI-generated lessons to mitigate teacher shortages
   Reuters — https://www.reuters.com/world/china/inside-chinas-drive-build-an-ai-native-generation-2026-11-16/

30. Analysis: global manufacturing, utility, and mining companies have shed $4.2T in market value since June as the AI “picks and shovels” trade swings into reverse
   Clara Murray / Financial Times — https://www.ft.com/content/d5adde7e-68cc-455b-ba78-b39cc3676b7a
   > @staunovo: Data centre construction stocks lose $4.2tn as boom in AI trade unravels Shares in AI ‘picks and shovels’ companies hit hard by tech sell-off https://www.ft.com/...
   Also: Semafor

31. Startups unveil plans to develop floating offshore data centers to bypass land and power constraints, while experts warn of challenges like saltwater corrosion
   Jackie Snow / Wall Street Journal — https://www.wsj.com/tech/ai/data-centers-ocean-f676429a?st=StJGmG&reflink=desktopwebshare_permalink
   Also: Fast Company, The Korea Herald

32. Russia is bringing young foreign influencers to occupied Ukraine, encouraging them to share their highly curated experiences, to legitimize its occupation
   Linda Hourani / The Kyiv Independent — https://kyivindependent.com/the-foreign-influencers-helping-russia-sell-its-occupation/
   > @collinslkoh: It's good to be young. But it's quite another thing to become, knowingly or naively, a useful young idiot. https://kyivindependent.com/ ...
   > @jayinkyiv: The foreign influencers taking Russian money to legitimize Russia's occupation of Eastern Ukraine and cover up large-scale war crimes. https://kyivindependent.com/ ...
   > @matthew_kupfer: Great reporting by @LindaHourani on #Russia using influencers to legitimize its war on #Ukraine in the “Global South.” This stood out to me: Alongside Donbas, Russia took them to Georgia's Abkhazia re

33. Delhi-based Bharat Semi, which is developing programmable image sensors combining capture, processing, and AI capabilities on a single chip, raised a $24M seed
   Jagmeet Singh / TechCrunch — https://techcrunch.com/2026/11/15/indian-chip-startup-bharat-semi-lands-24m-seed-round-as-it-eyes-global-ai-sensor-market/
   Also: Inc42, The Economic Times, Entrackr, Livemint, DealStreetAsia, Tech in Asia, Telecompaper

34. Zus Health, which is building an AI-native healthcare data platform, raised a $33M Series B led by Drive Capital, bringing its total funding to $100M+
   Heather Landi / Fierce Healthcare — https://www.fiercehealthcare.com/health-tech/zus-health-secures-33m-build-infrastructure-ai-powered-clinical-workflows
   Also: Zus Health

35. Copenhagen-based AI accounting software maker Sumary raised a $25M seed led by Singular, taking its total funding to $29.2M after a $4.2M pre-seed in Nov. 2025
   Sofia Chesnokova / Tech Funding News — https://techfundingnews.com/sumary-25m-seed-ai-accounting-firms/
   Also: Startup.eu

36. AI agent management platform Kindo raised $30M led by Crosspoint and Forgepoint, taking its total funding to $57.6M, and says its revenue grew ~800% YoY in 2026
   Abhinaya Prabhu / Tech Funding News — https://techfundingnews.com/kindo-raises-30m-after-800-revenue-growth-can-one-control-center-tame-enterprise-ai-agents/

37. Mount Thor, which is building cloud infrastructure for agentic AI on Apple silicon, raised $45M in a seed and a Series A co-led by CRV and Conviction
   Bradley C / 9to5Mac — https://9to5mac.com/2026/11/12/mount-thor-raises-45-million-to-build-mac-data-centers-for-ai-agents/
   > @foundrceo: @Techmeme the mac mini in every agent setup photo finally has a cloud
   Also: DatacenterDynamics, Mount Thor Blog, TechRadar

38. Toronto-based Blue J, which provides AI-powered tax research software, raised a $176M Series E round led by JMI Equity at a $700M+ valuation
   Alex Riehl / BetaKit — https://betakit.com/ai-tax-research-platform-blue-j-raises-176-million-usd-series-e/
   > @foundrceo: @Techmeme @RiehlAlex99 an ai that voluntarily reads the tax code deserves the $700m
   Also: FinTech Global, Blue J

39. Samsung aims to be a one-stop shop that builds, runs, and powers AI data centers; sources: its IT arm is in early talks to sign Anthropic and OpenAI as tenants
   Financial Times — https://www.ft.com/content/ee5b23b3-89b3-41f7-9158-56c1586759c2
   > @foundrceo: @Techmeme renting to openai and anthropic in the same building is a bold sitcom pitch

40. Sources: Anthropic's IPO is ~7x oversubscribed; Anthropic and some of its backers are seeking to raise up to $90.4B via the IPO and a separate private placement
   Bloomberg — https://www.bloomberg.com/news/features/2026-11-15/anthropic-s-ipo-makes-dario-amodei-the-new-face-of-the-ai-boom
   Also: Australian Financial Review, Gulf News

41. Analysis: Huawei's Horinger data center, among China's largest for AI, has ~7% of the compute of SpaceX's Colossus 2 and may stay far behind until at least 2028
   Ben Cottier / Epoch AI — https://epochai.substack.com/p/what-huaweis-horinger-data-center
   > @kimmonismus: METR reports are always worth reading. Just finished reading their latest Substack. If you want to understand how much ahead the US is regarding data center, read those numbers: Huawei's flagship AI d

42. Megaspeed says Alice Huang left in August 2025 and has no current role, and that it runs a “legitimate and lawful business” as it opens an internal probe
   Associated Press — https://apnews.com/article/singapore-megaspeed-alice-huang-nvidia-probe-e9e2e18169dce0b30a34f39715bf35ed
   > @aditis90: 🚨Short seller Culper Research described Jensen Huang's relationship with Megaspeed's Alice Huang as “uncomfortably close” : May 2026 The report flagged dinners, data-centre visits with Alibaba reps in
   Also: Barron's Online, South China Morning Post, CBS News, The Guardian, Associated Press, Fortune, The West Australian, ABC, +3 more

43. Sources: Apple plans to unveil smart glasses at WWDC and ship them by the end of 2027, focusing heavily on integration of third-party iPhone apps with Siri AI
   Mark Gurman / Bloomberg — https://www.bloomberg.com/news/newsletters/2026-11-15/apple-siri-ai-app-integrations-power-smart-glasses-iphone-duo-2-face-id-plan?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5NDc1NTQ2MSwiZXhwIjoxNzk1MzYwMjYxLCJhcnRpY2xlSWQiOiJUT0pUTzFLSVVQU0IwMCIsImJjb25uZWN0SWQiOiJDNEVEQ0FFMUZBMDU0MEJFQTI0QTlGMjExQzFFOTA4MCJ9.2TeBxZfpuwFLhhyEns0-GWBuy-YbU6nhgWwD5smKMD4
   > @markgurman: Inside Apple's smart glasses prototypes: a pared-down visionOS 28, Wi-Fi, flush camera openings and a magnetic charger near the tip of the left arm. Employees call them “AirPods for your face.” More i
   > @jimscard: @ManmohitSandhu Meta has been selling glasses that gather data for Meta and enable violation of people's privacy. Apple doesn't do either of those things, as a result, it's puzzling that they'd be rel
   > @einarjohnson_xr: Apple's going to slowly get to AR glass hardware. AI AirPods, AI glasses, then AR glasses. Gives them time for fixing Siri, getting society used to cameras on glasses, refining VisionOS, and getting A
   > @foundrceo: @Techmeme @markgurman shipping end of 2027 gives siri two years to get good. tight
   > @raywongy: I would take a thinner and lighter iPhone Duo 2 over Face ID first tbh
   Also: T3, iMore, The Verge, MacRumors, Cult of Mac, The Indian Express, Storyboard18, Neowin, +17 more
