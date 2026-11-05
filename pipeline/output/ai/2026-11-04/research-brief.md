# Research — News Cluster

Search for news **events that occurred** between **2026-11-03 10:00 BRT** and **2026-11-04 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-11-03 10:00 BRT to 2026-11-04 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-11-04
**Research window:** 2026-11-03 10:00 BRT → 2026-11-04 10:00 BRT

**Previous edition headlines (2026-11-03 — skip unless genuinely new development):**
- anthropic-s1a-rsi-threshold-imminent: Anthropic's amended S-1 says future models may 'imminently' meet its AI-accelerated R&D threshold
- anthropic-s1a-q3-financials-valuation-1-5t: Anthropic S-1/A: Q3 revenue ~$17B, $895B compute commitments; IPO investors push ~$1.5T valuation
- weight-space-programming-gpt6-astra-edits-qwen: MIT researchers: GPT-6 Astra edited 0.016% of a Qwen model's weights, raising math score 7.9% to 48.1%
- salesforce-acquires-cresta-2-7b: Salesforce agrees to buy voice-AI contact center startup Cresta, reportedly for $2.7B
- china-ndrc-ai-lifecycle-safety-standards: China's planner says it will speed AI legislation and lifecycle safety standards for model makers
- trajectory-45m-series-a-sequoia-post-training: Trajectory raises $45M Series A led by Sequoia at $300M valuation for no-code model post-training
- openai-merges-chatgpt-chat-work-shared-token-pool: OpenAI to merge ChatGPT's Chat and Work tabs; ChatGPT and Codex to share one usage allowance
- nvidia-cloud-clients-51-percent-non-chinese: FT: Nvidia tells cloud clients at least 51% of their compute must go to non-Chinese customers
- hbm-smuggling-huawei-ascend-960dt: Smugglers move Samsung and SK Hynix HBM into China via a loophole; Huawei's 960DT leans on it
- samsung-taylor-fab2-hbm-base-dies-amd-nvidia: Samsung to make HBM base dies for AMD and Nvidia at its second Taylor, Texas fab, report says
- agility-robotics-spac-approved-nasdaq-aglt: Churchill Capital XI holders approve $2.5B Agility Robotics SPAC; trading as AGLT set for Nov. 5
- tutor-intelligence-75m-series-b-a16z: Warehouse-robot maker Tutor Intelligence raises $75M Series B led by a16z
- drax-brookfield-radiant-yorkshire-ai-data-center: Drax, Brookfield and Radiant plan a GW-scale AI data center at Drax Power Station, up to £20B
- apple-memory-costs-unprecedented-inventory-154: Apple's Ternus calls memory prices 'unprecedented' as inventory jumps 154% and margins guided lower
- us-strikes-iran-qeshm-island-eve-of-midterms: US strikes Iran's Qeshm Island in Hormuz on eve of midterms as Brent posts biggest drop since July
- russia-massive-strike-ukraine-energy-abu-dhabi-talks: Russia hits Ukraine's grid with 59 cruise and 17 ballistic missiles as US sets Abu Dhabi talks
- rba-hikes-cash-rate-4-85-eighteen-year-high: Australia's central bank hikes to 4.85%, an 18-year high, in split 6-3 vote
- ncsc-annual-review-ai-cyber-china-russia-2028: UK's NCSC: China, Russia will routinely use AI cyberattacks for geopolitical goals by 2028
- suse-cuts-10-percent-workforce-citing-ai: SUSE to cut about 10% of its 1,900 staff, saying AI is 'fundamentally shifting' software work
- mercado-bitcoin-hack-46-million: Brazil's largest crypto exchange Mercado Bitcoin halts withdrawals after $46M breach
- wall-street-tech-rotation-oracle-gold-nov-2: Nasdaq falls 1.1% as investors keep rotating out of tech; Dow rises and gold gains 1.8%

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 46 stories

1. Democratic gubernatorial wins from Texas and Georgia to Ohio and Pennsylvania are set to expose 50% of AI data center proposals to more scrutiny and pushback
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-04/ai-data-center-boom-is-set-for-upheaval-after-us-election-rout
   Data center developers seeking to build dozens of sprawling artificial intelligence campuses across Texas were already dealing …
   > @elonmusk: Data centers in space looking pretty appealing right now
   > @annmarie: In Texas, roughly 13 gigawatts of data center capacity — enough to power roughly 10 million homes at any given moment — is immediately exposed by Hinojosa's win, Gordon Johnson of GLJ Research said in
   > @adamkovac: Pro-Innovation House Democrats — candidates endorsed by @sliccardo's Innovation for Good PAC — have won 39 out of 40 races called so far. The new Congress is going to have a strong bench of pro-innova
   > @reprobertgarcia: LAWYER UP.
   > @edmarkey: They are going to need to plant new forests for all of the subpoenas we'll be printing.
   Also: 404 Media, CNBC, Wccftech, Reuters, CoinDesk, Implicator.ai

2. Texas elects Democrats for governor and the US Senate for the first time in decades, creating uncertainty for its booming AI data center sector and Elon Musk
   Nick Wingfield / The Information — https://www.theinformation.com/briefings/stunning-democrat-victories-texas-bring-uncertainty-data-centers-musk
   Texas elected Democrats for governor and the U.S. Senate for the first time in decades, creating potential uncertainty …
   > @nprinskeep: Elon Musk moved from California to Texas in order to live in a red state, and wakes up this morning in what looks (for the moment) like a blue state.
   > @energy_tidbits: Here is Texas Governor-elect Gina Hinojosa's clear data center stance.
   > @beffjezos: Time for an executive order to ban TikTok Time to take back the psychological warfare playing field
   > @intheassembly: Almost nobody is connecting these two stories. Texas just elected a Democratic senator and governor. Texas is also where roughly 20% of America's data centers are supposed to get built. James Talarico
   > @annaeconomist: Why Texas really matters. It's set to overtake Virginia as the dominant states for data center. And much of the projects still in early stage (which means, they can be stopped). h/t Derrick Flakoll (B
   Also: Barron's Online, Reuters, Bloomberg, Semafor, Bisnow, Coinpedia Fintech News

3. Democrat James Talarico defeats Ken Paxton to win Texas' first Democratic Senate seat in 30+ years; Elon Musk spent $47M+ backing Paxton and attacked Talarico
   Stephanie Findlay / Financial Times — https://www.ft.com/content/b2d07a1f-dfa6-449b-a598-1db51951d6f6
   Billionaire had ploughed $47mn into bankrolling Republican Ken Paxton's campaign while fuelling conspiracy theories about his opponent
   > @elonmusk: Guess my election-interfering space lasers didn't work this time 🤷‍♂️
   > @harryjsisson: Elon Musk spent hundreds of millions trying to buy the Texas Senate seat and LOST. Talarico beat him AND Paxton. L BOZO😭🥀
   > @rshivshankar: Money doesn't make you boss, Elon. It's the people. ELON MUSK: THE BIGGEST LOSER OF THE U.S. MIDTERMS? Elon Musk suggested that Oligarchs rule countries becuse they have money. But the mid-terms showe
   > @gator_gum: The James Talarico win is absolutely inspiring. He had to endure daily attacks. Lies. Misinformation... Musk spent hundreds of millions, and posted lie after lie. They absolutely attacked him in a dis
   > @wrbolen: Elon Musk and Joe Rogan moved to Texas to escape liberal California and inadvertently turned Texas blue for the first time in 30 years 😂
   Also: Business Insider, International Business Times, Capital Brief, Wall Street Journal, Axios

4. Democrats' US midterms victory is a win for hyperscalers and AI labs, a mixed bag for Nvidia, an advantage to China, and may make space data centers attractive
   Ben Thompson / Stratechery — https://stratechery.com/2026/ai-on-the-ballot/
   Data Centers were on the ballot, and they lost in a major way; what does it mean if American opposition to building is permanent?
   > @stevehou: To the extent that AI has been an arms race that nobody among the hyperscalers/megacap tech cos dares to slow much less stop even as investors turned skittish/unpersuaded of the capex, being forced to
   > @brandonjcarl: If I had to summarize things: - The largest growth engine of the economy now faces more friction - Retail leverage and exposure very high in semiconductors; does not benefit from this - Installed comp
   > @bradrcarson: So the results are all in. Data center moratoria (various flavors) went 43-1. All hyperscalers must now converge on Harwood, North Dakota, the one outlier. Find out what's in the water or in the air. 
   > @danprimack: Gonna be interesting to see how many SV folks have principles and how many are just front-runners. Betting hard on the latter.
   > @anecdotal: These seem right, especially data centers in space (far down the road) and general upsides for consumers. Optimistic. @stratechery https://stratechery.com/...

5. NBC exit poll: 56% said AI and data centers had been a “crucial or a major factor” in their Congress votes, as Democratic candidates pledged to halt development
   Financial Times — https://www.ft.com/content/badd6af9-88b7-47b7-b1c2-067814e70fb5
   Gubernatorial wins in Texas, Georgia and Ohio and local ballot measures show depth of discontent with Trump-backed infrastructure spree
   > @thestalwart: Blueskywave. Those of us on here, across the board, were out of touch. I see no other conclusion.
   > @theobertram: The big losers: Trump and datacentres. 56% of US voters said AI and datacentres were a factor in how they vote. Of the 34 specific measures across the US to restrict or allow local datacentres, voters
   > @daniel_271828: This is the lowest salience AI will ever be in an election
   > @rob_flaherty: Post your L's, king
   > @jayshooster: I am so confused that tech industry groups are sharing stats like these as evidence that AI is not a big deal with voters. This is a huge deal! And everyone can see this is only going to grow by 2028.
   Also: DatacenterDynamics, NBC News, Reuters, The Decoder, The San Francisco Standard

6. US voters in 29+ jurisdictions overwhelmingly pass data center bans or restrictions; S&P says 145+ US projects were delayed or canceled through early August
    — https://www.washingtonpost.com/technology/2026/11/04/voters-pass-over-20-ballot-measures-ban-or-restrict-data-centers/
   They passed a string of local bans and elected gubernatorial and Senate candidates pledging tougher regulation. — SummaryLoading...
   > @carlquintanilla: WAPO: “.. Voters in at least 29 jurisdictions across the country passed bans or restrictions on data centers Tuesday, reflecting the widespread public revulsion to the facilities ..” @washingtonpost h
   > @mollytaft: the texas data center implications are truly insane for the industry. if i was a data center developer i would not feel very good right now
   Also: Capacity

7. Democrats running on AI regulation and anti-data center platforms won key races, including Sherrod Brown in Ohio, as leadership signals aggressive AI oversight
   Politico — https://www.politico.com/news/2026/11/04/dems-made-big-tech-a-foil-and-they-couldnt-stop-winning-01148450
   > @sherrodbrown: Thank you, Ohio. Let's get to work.
   > @christopherhale: JD Vance's former Senate seat is now held by Sherrod Brown.
   > @brendanpedersen: The crypto super PAC network Fairshake couldn't kill Brown again and the industry didn't bother to spend a dollar helping any other Senate Democrats this cycle. The industry's agenda is dead in the Se
   > @skeptrune: how the ceos about to be moving when aoc is president
   > @signulll: some facts from tonight. woke is not only back but it will be bigger than ever before. 1. georgia: keisha lance bottoms defeated billionaire rick jackson, becoming america's first black woman governor
   Also: Axios, International Business Times, Unchained, Motley Fool, Reuters

8. Elon Musk's preferred US midterm candidates, including Ken Paxton and Vivek Ramaswamy, lost almost everywhere; Musk spent ~$446M, a record for a non-candidate
   Calder Mchugh / Politico — https://www.politico.eu/article/elon-musk-dealt-major-blow-in-midterm-elections-2026/
   > @rmac18: Though we'll need to adjust those net worth estimates now. Tesla is down 4.5% in premarket trading and SpaceX down 5% while other tech stocks and wider market are doing ok. Investors signaling that th
   > @finestyew: Elon is a dead man walking btw (metaphorically ofc). The Starlink stunt he pulled in Ukraine really pushed even the most moderate Democrat over the edge. They're baying for his blood rn.
   > @yahatetwoseeit: Tesla Boy ain't tweeted in like 6 hours I know you see this shit dickhead
   > @sbg1: Just thinking about the remarkable fact that Elon Musk will have dropped nearly a half a billion dollars on this election with no return... wow.
   > @rmac18: Musk spending about $500 million says something about US politics and perhaps more about wealth inequality. $500 million represents .06% of his current $900 billion net worth. His net worth went up $2
   Also: Politico, Reuters, New York Times, Forbes, CNBC, Washington Post

9. Ohio voters approved data center bans or restrictions in 14+ municipalities across 21 ballot measures, adding to the 125 local moratoriums already in the state
   Sasha Rogelberg / Fortune — https://fortune.com/2026/11/04/ohio-data-center-ballot-measures-midterm-elections/
   > @annaeconomist: In tomorrow's midterm races we have our eyes on the gubernatorial races. Just 10 states have 70% of the data center pipelines (per our BNEF colleagues), and several of their governors are up for reele
   > @matthew_sigel: In Ohio (OH), where polls closed at 7:30pm ET, watch Mahoning county, a rust belt county with a long Democratic history which has moved to the right over the last decade after the closing of the Lords
   > @zerohedge: Ohio has 21 local data center votes, 16 would ban or cap. Ohio is home to what will be the world's biggest data center (if it is ever completed): SB Energy's 8GW project
   > @factpostnews: Ohio voters speak out about the importance of data center issues while voting
   > @matthew_sigel: Loudon County is the one to watch in VA. Not only the largest concentration of data centers anywhere in USA, but also an early reporter with the count should be substantially complete by 8pm ET. Given
   Also: Yahoo News, Journal-News

10. Sources: Oracle has scrapped a ~$7B, five-year deal to lease as many as 100K advanced AI chips to Tencent after bowing to pressure from the Trump administration
   Financial Times — https://www.ft.com/content/c5a6a738-cd78-4a8e-a814-57a7473ebb9c
   Intervention comes amid growing tension for US AI infrastructure groups doing business with Chinese tech giants.
   > @ns123abc: BREAKING: Oracle just CANCELED its $7 billion AI deal with Tencent it has begun
   > @rohanpaul_ai: Oracle has scrapped a $7B lease giving Tencent up to 100K advanced AI chips after US objections. The 5-year contract, Tencent's largest overseas lease, would have supplied chips unavailable in China f
   > @kakashiii111: There are a few questions from this: 1. Why all of a sudden Trump put pressure on this, while from the very beginning he turned a blind eye to what was happening with Chinese customers and Nvidia GPUs
   > @jwupacific: China tried to rent 100,000 American AI chips through a U.S. company. The deal just collapsed. Oracle just canceled a $7 billion deal that would have given Tencent access to advanced AI chips through 
   > @tanarrowz: $ORCL is a major supplier to ByteDance in Asia with multiple data centres in Malaysia. The company also hosted US customer data for the Chinese group's social media platform TikTok b4 being part of a 
   Also: Bloomberg, Reuters, Investing.com, Seeking Alpha, Reuters

11. Tencent releases its Hy4 open-weight foundation model, which it says joins the top tier of Chinese open-weight AI for the first time, and plans a Flash version
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-04/tencent-declares-latest-ai-model-ranks-among-china-s-best
   Tencent Holdings Ltd. released a foundation model Wednesday that it said joins the top tier of Chinese open-weight AI systems for the first time.
   > @thepandaily: @Techmeme In Tencent's blind finance eval with 213 professionals across 579 real tasks, Hy4 scored 3.04, ahead of DeepSeek V4.1 Flash at 2.97 and Kimi K3.1 Pro and GLM-5.3 at 2.68. A cheaper Flash ver
   > @yonglongt: Guess folks still love high-performing open-weight models 👀 We are taking a cautious approach to release the weights. Give it a spin and let us know what you think!
   > @shunyuyao12: Proud of what we've achieved under a year! Priortize security, usefulness, human evals, and generalization. Favorite part of mine is the bottom line of the plot 😂
   > @tencenthunyuan: Introducing Hy4
   > @jumperz: wild, HY4 is out and it's looking really good.. here's where it really good at > finance research: #1 among open models in Tencent's evaluations > game dev: +19.1% improvement, trained for Unity, Unre
   Also: Reuters, hy.tencent.ai, Nikkei Asia, South China Morning Post

12. Sources: Alibaba, Tencent, ByteDance, and other Chinese AI companies ordered 6M Nvidia RTX Pro 5500 chips worth $70B, but expect only ~1% within four months
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-04/nvidia-china-clients-to-get-1-of-70-billion-rtx-chips-ordered
   Also: Tom's Hardware, Seeking Alpha, Seoul Economic Daily

13. Apple opens Siri AI to all developers, letting any app on iOS 27.3 beta and other 27.3 OS betas bring its content and actions into Siri AI by using App Intents
   Apple Developer — https://developer.apple.com/news/?id=gdk2umrf
   Starting today with the iOS 27.3, iPadOS 27.3, macOS 27.3, and visionOS 27.3 betas, a new Developer Preview enables any developer …
   > @viticci: These are some of the actual skills Apple is using for Siri AI in iOS 27.3 - there's a skill to teach Siri how to select and insert text in Notes - they made a skill to tell Siri about file types supp
   > @johnvoorhees: This is a big deal folks. It promises to open up Siri AI much wider, so it can do a lot more.
   > @dancunderwood: For those who missed it, at WWDC we gave a session on how to think through security for your app with these kinds of integrations - now is a great time to watch it if you haven't yet! https://develope
   > @viticci: The expanded Siri AI is actually a bigger deal - from Apple: “Today's preview allows any app to bring its content and actions directly into Siri AI by using App Intents” So Apple is moving away from s
   > @mattcassinelli: The best Siri AI news is hidden in the documentation - she can accept values in the request! Currently, you must ask with a specific phrase and following up with an answer. Soon, you can make a single
   Also: MacRumors, The Verge, Macworld, The Hindu, Tom's Guide, 9to5Mac, The Apple Post, PPC Land, +3 more

14. Apple launches iOS 27.3 beta, adding Apple Intelligence in China with an Alibaba-powered content filter, and watchOS 27.3 beta, with Siri Recap and Live Rewind
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-03/apple-releases-ios-27-3-beta-with-watch-ai-listening-tools-health-app-china-ai?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MzczMDU5MCwiZXhwIjoxNzk0MzM1MzkwLCJhcnRpY2xlSWQiOiJUTlhWQTJOM04wOUowMCIsImJjb25uZWN0SWQiOiJDNEVEQ0FFMUZBMDU0MEJFQTI0QTlGMjExQzFFOTA4MCJ9.7fxypbPrSvvjnL8axvz4558x4pLkCOGmDrxk0Q0E3l0
   Apple Inc. rolled out the first developer beta versions of iOS 27.3 and watchOS 27.3 on Tuesday, putting new features …
   > @aaronp613: iOS 27.3 beta 1 adds Reachability on iPhone Duo
   > @parkerortolani: this is a great update, not necessary imo, but will help a bit
   > @mweinbach: There are a ton of little Duo usability tweaks in iOS 27.3 around keyboard, noticed a new in iMessage, probably more. Lots of shifting around UI elements to show more content
   > @markgurman: The betas also include Reachability on the iPhone Duo, the new Duo StandBy Mode on non Duos, and support for Siri Mode in Camera and Visual Intelligence with Apple Pencil in iPadOS.
   > @rsgnl: iOS 27.3 beta 1 adds vertical tabs to Safari. This extends to iPadOS 27.3 and macOS 27.3.
   Also: Apple Support, Apple, Gizmodo, 9to5Mac, 9to5Mac, 9to5Mac, 9to5Mac, MacRumors, +18 more

15. Google says AI tools for K-12 students will be off by default in 2027; schools that block AI entirely will lose Search, as “Search and AI are deeply integrated”
   New York Times — https://www.nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html?unlocked_article_code=1.NlE.VMKr.Cr-g-C6phyfH&smid=url-share
   Google is making it easier to restrict its A.I. tools for students. But schools that block A.I. entirely will lose student access to Google's search engine.
   > @nycmayor: Google is trying to use its monopoly power to force AI into our public schools. No corporation should have the power to dictate how we teach our children. Our public schools exist to serve students, n
   > @sensanders: President Trump claimed that AI oligarchs could regulate themselves because they “love our country.” Now, Google is threatening schools... That's not love. That's extortion. PAUSE AI NOW.
   > @linamkhan: Google is using its search monopoly to coerce schools into adopting AI. This highlights the danger of allowing an unregulated monopolist to control an essential service. Multiple courts have found Goo
   > @lilyraynyc: “They can turn ON one, two or three of these services individually” is quite different than how the @nytimes framed it in their article headline 🫠
   > @senblumenthal: Google is once again prioritizing profits over people—this time blocking schools from using Google Search unless they opt into their A.I. overview. Clearly, the Tech Giant is more concerned with forci
   Also: Google, Washington Post, The Verge, The Guardian, Mercury News, Financial Express, Bloomberg, Neowin, +19 more

16. Following backlash against its education updates, Google says schools can choose to enable Gemini, Gemini Notebook, and Search individually
   Isabel O'Brien / CNBC — https://www.cnbc.com/2026/11/03/google-responds-to-outrage-over-removing-search-in-schools-that-ban-ai.html
   > @newsfromgoogle: We want to clarify what we announced today about our education services. Today's announcements give schools more choice, not less. Here's what we announced: - Gemini, Gemini Notebook, and Search will 
   > @ednewtonrex: @NewsFromGoogle But if they turn on Search, they get AI Mode in Search, right? In other words, they can't turn off AI without losing Search. Which is exactly what the press has been reporting, and exa
   > @mikeisaac: google doing a bit of damage control from the uproar today but this is interesting to me childless man question: is it common to ban search in classrooms? the way “AI guided learning” is described see
   > @jason_kint: Google and Meta have the same PR spin. It's getting tiring. I read the below as hiding the ball. Like with training on publishers' intellectual property, Google appears to be bundling AI Overviews and
   > @thenextcorner: That was fast. It looks like Google is backtracking their closure of search if you schools don't opt in for Gemini tools. I still wonder how much of our kids work will be used for training data if Gem
   Also: Search Engine Roundtable, CNET, Education Week, The Information

17. Canva says it is restructuring, impacting 1,271 jobs, or 22% of its staff, across layoffs and relocations, as it merges its product, growth, and platform teams
   David Swan / The Age — https://www.theage.com.au/technology/canva-unveils-mass-job-cuts-in-hardest-moment-of-its-history-20261104-p61b62.html
   Canva will cut more than 1000 jobs in a major restructure in response to slowing growth at the design giant.
   > @markdistef: Canva's terms for departing employees are both exceedingly generous and a window into modern tech: * Six months salary * A year healthcare * A year of LinkedIn premium * A $10k grant to start a busine
   > @hameonline: Extremely sad day for Aussie tech. Canva should be a reminder that you should strike when the iron is hot and not rest on your backside. I'm confident that many wonderful engineers will be unshackled 
   > @forgebitz: watch canva get bending spooned
   > @p_remarks: I promise you if AI capex spending rolls, the entire economy is going to roll. Staples will get rolled. Lots of healthcare will too. Will be few hiding spots.
   > @cargoshortdad64: Canva is a mom and pop shop that accidentally grew too big that they now have to participate in the AI arms race and they're talking about cutesy design templates while we're witnessing the birth of d
   Also: Canva, CTech, Bloomberg, TechCrunch, Silicon Republic, Windows Report, The Information, Forbes Middle East, +13 more

18. AMD reports Q3 revenue up 45% YoY to $13.38B, above $13.09B est., Data Center revenue up 97% to $8.5B, and forecasts Q4 revenue above est.; AMD jumps 7%+
   Katie Tarasov / CNBC — https://www.cnbc.com/2026/11/03/amd-amd-q3-earnings-report-2026-.html
   Advanced Micro Devices reported third-quarter earnings on Tuesday that beat Wall Street's expectations, with revenue jump 45% …
   > @patrickmoorhead: $AMD Q3: BEAT and raise, it's up sharply after hours: the market is paying for the $17B guide. Stellar execution; the pundits were wrong. The numbers: -Revenue $13.38B, +45% YoY, vs $13.08B consensus:
   > @stocksavvyshay: It took $AMD all of 2023 to generate $6.5B in data center revenue and it just did $8.5B in a single quarter 🤯
   > @stockmktnewz: AMD CEO Lisa Su said that more than 10 Million people tried $META's Muse Agent in the first 6 weeks
   > @realnickmugalli: HOLY SHIT! $AMD just guided its December quarter to $17bn of revenue. $INTC guided its entire company to $15-16bn last week for comparison. A few years ago AMD was the scrappy underdog fighting for sc
   > @wallstengine: $AMD says Anthropic, Meta, Microsoft, OpenAI, and Oracle are now running workloads on its first Helios AI racks. Data center revenue nearly doubled to a record $8.5 billion, helping total revenue clim
   Also: Advanced Micro Devices, VideoCardz.com, Bloomberg, Reuters, Bloomberg, Wall Street Journal, ServeTheHome, Seoul Economic Daily, +1 more

19. AMD projects ~$17B in Q4 revenue, above Intel's $15B to $16B projection, potentially overtaking Intel as the largest x86 processor vendor for the first time
   Simon Sharwood / The Register — https://www.theregister.com/systems/2026/11/04/amd-on-track-to-overtake-intel-as-biggest-x86-outfit/5307448
   Also: DatacenterDynamics, Tom's Hardware, Seeking Alpha, The Verge, Morningstar, Zacks Investment Research

20. OpenAI acquires developer tools startup Pierre Computer for an undisclosed amount and plans to integrate Pierre's Code Storage feature directly into Codex
   Madison Mills / Axios — https://www.axios.com/2026/11/04/openai-pierre-computer-github
   OpenAI will acquire Pierre Computer, a developer tools startup whose technology is already embedded in Codex, the company told Axios exclusively.
   Also: Unite.AI

21. Anthropic releases FlashProve, an open-source prototype that cryptographically verifies an AI response came from a given model, not one that a router swapped in
   Anthropic — https://www.anthropic.com/research/provable-inference
   Roy Rinberg (Anthropic), Alex Allain (Anthropic); Alessandro Chiesa (EPFL, StarkWare), Miranda Christ (MIT, RESI), Rahul Dalal …
   > @akitainuasa: Verifiable Inference will be one of the most important security technologies of the century. We're not there yet but were making progress https://www.anthropic.com/...
   > @gakonst: a lot of reasons to be excited for the new anthropic work but the one im the most excited to shout out is @transmissions11 in the coauthors! we had the privilege of working together at @paradigm a few
   > @jaminball: Provable inference is coming. A very real commercial use case for zero knowledge proofs is forming! “Recently commercial efforts have reached impressive numbers, with Attestable proving Gemma 4 31B at
   > @succinctlabs: Huge congrats to Succinct's Rahul Dalal, one of the cryptographers behind FlashProve, @AnthropicAI's provable inference system built on zkSNARKs. Why: Today, AI runs on a “just trust me
   > @dcbuilder: ZKML is now mainstream I guess. How time flies since we did some of the first experiments on ZKML at World in 2022. https://www.anthropic.com/...
   Also: TechCrunch, Help Net Security

22. Google says it expanded voluntary exit buyouts in June to employees across Canada, France, Germany, Japan, and Switzerland to manage costs amid huge AI spending
   Reuters — https://www.reuters.com/business/media-telecom/google-extends-voluntary-buyout-offers-employees-several-countries-2026-11-04/
   Alphabet's Google (GOOGL.O) has expanded employee buyout offers to several countries this year as it looks to rein …
   Also: CTech, Business Today, Storyboard18, Unite.AI, PPC Land, Livemint

23. Cat Wu, product lead for Claude Code and Cowork, says she has left Anthropic; Thariq Shihipar, who worked on Claude Code, announced his departure on October 24
   Stephen Council / Business Insider — https://www.businessinsider.com/claude-code-leader-cat-wu-exits-anthropic-before-big-ipo-2026-11
   - Cat Wu, who helped scale Claude Code into one of tech's most important products, has left Anthropic.
   > @trq212: I've left Anthropic after more than a year of working on Claude Code and seeing it scale larger than I ever imagined. I have really loved working at Ant and believe deeply in the mission, and most of 
   > @amorriscode: Yesterday was my last day at Anthropic. I created Claude Code on desktop because I believe everyone can be a builder. Every feature request and bug report we got from this community was a gift that im
   > @trace_cohen: $100M seed incoming
   > @_catwu: Friday was my last day at Anthropic. Two years ago, when Claude Code was a small internal tool, I asked it to build an RL env. I steered it for tens of hours but never manually wrote a line of code. I
   > @independenteco: Anthropic just lost one of its lead PMs Cat had a technical engineering background and will be hard to replace. There is now a trend of several high profile individuals leaving Anthropic before IPO. I
   Also: AIM

24. Revolut says it cut AI coding inference costs by ~90% in less than a year by making self-hosted GLM models its default over commercial tools like Claude Code
   Tobias Mann / The Register — https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345
   Revolut says that in less than a year it's managed to slash its AI coding inference costs by roughly 90 percent by making self-hosted models …
   > @guilleflorvs: BREAKING: Revolut moved ~2,000 engineers onto self-hosted GLM for coding and pushed Claude Code and Codex to the exception list. Per David Abitbol, who leads AI ops there: 56 Nvidia B200s, a blended 3
   > @guitaripod: Sam Altman' and Dario Amodei's worst nightmare. [embedded post]
   > @mattparlmer: I think the reason we haven't seen a huge uptick in router usage of open models is that after using GLM or similar near-frontier open models for a couple weeks the enterprises capable of pushing major
   > @quxiaoyin: At least wait until Anthropic IPOs. Be nice revolut [embedded post]
   > @tekbog: a lot of big companies have their own clusters, just like many have still their own servers …
   Also: Silicon Republic, TechRadar

25. Valve announces changes to Steam's review process, as a surge in game submissions pushes review times to “up to 12 business days”, instead of the usual 3-5 days
   Jay Peters / The Verge — https://www.theverge.com/games/1025722/valve-steam-game-increase-submissions
   Valve admits that it's now taking ‘up to 12 business days’ to game submissions.
   Also: Steam Community, GamesRadar, The Verge, Video Games Chronicle, Engadget, Digital Trends, PC Gamer, Kotaku

26. Industry experts warn that slow US power grid expansion could stifle its AI boom and give China an edge, as China builds power infrastructure faster
   Martha Muir / Financial Times — https://www.ft.com/content/20d5599f-8955-4184-a2a0-ac1296e400f3?accessToken=zwAAAaGlkx_5kc8g1VmfiVVBhNOioKwSluQA8w.MEQCIFK7Fdnkw1P8IFgW1-qvSdOM3zwT-zAi5iCOR69gDKeaAiA_kkJ1mI6J2nnKn1OyZSmVm-LcnHQeleuqnfqYmrcY9A&sharetype=gift&token=b4848b6e-823f-4d06-ad62-e40b39922426
   Why America is struggling to power the AI boom. The US is building electricity lines at a quarter the rate of a decade ago It took 13 years …

27. OpenAI hires Jill Hazelbaker, Uber's president and chief corporate affairs officer, as its new chief corporate affairs officer, reporting to Greg Brockman
   Mike Allen / Axios — https://www.axios.com/2026/11/03/jill-hazelbaker-openai-uber
   Jill Hazelbaker, Uber's president and chief corporate affairs officer, is moving to OpenAI in the new role of chief corporate affairs officer …
   > @mikeallen: 🚨🚨🚨 Jill Hazelbaker, one of Washington's best-known leaders, is jumping from @Uber to @OpenAI as chief corporate affairs officer She tells @axios it's a “chance to help shape how the world understands
   > @lexnfx: Hazelbaker will remain on the East Coast but “spend time” in SF, Fortune reports... OpenAI hires Uber President Jill Hazelbaker to lead communications, filling a critical role that was curiously vacan
   > @jemimacmcevoy: NEW: Uber's President Jill Hazelbaker is joining OpenAI as its chief corporate affairs officer, filling a role that has been empty since the start of the year. She will attempt to stabilize a team tha
   Also: OpenAI, Windows Report, MediaNews4U, Storyboard18, Fortune

28. India-based EloElo, whose Story TV microdrama app has 33M+ estimated active users, raised an $80M Series C led by Hornbill Capital and NBCU at a $500M valuation
   Ivan Mehta / TechCrunch — https://techcrunch.com/2026/11/03/indias-eloelo-nabs-80m-from-nbc-universal-to-bet-on-the-countrys-rising-microdrama-market/
   More than 118 million users watch microdramas every month as the serialized format has taken off in India.
   Also: EloElo Group, The Economic Times, Entrackr, Storyboard18, Moneycontrol, Variety

29. Pharmaceutical leaders are skeptical of claims that AI could cure most diseases within a decade; the US FDA has yet to clear any AI-designed biotech drugs
   Xavier Martinez / Wall Street Journal — https://www.wsj.com/tech/ai/silicon-valley-promises-ai-will-cure-disease-drugmaker-ceos-arent-buying-it-5218511c?st=sszirS&reflink=desktopwebshare_permalink
   No drug designed by artificial intelligence has won FDA clearance, and pharma leaders say biology is the obstacle
   > @ramez: People who work in pharma have a much more realistic view of what AI can and can't do in biology than many in the AI field. AI is only as smart as its data. Experimentation is the bio bottleneck. [emb

30. Binance says North Korean hackers stole $6.3B through a months-long scheme with fake LinkedIn job interviews and an ad campaign to deliver malicious software
   Jeff John Roberts / Fortune — https://fortune.com/2026/11/03/binance-hack-details-linkedin/
   Binance on Tuesday disclosed that North Korean hackers used a mix of social engineering and malicious software to pull off …
   > @binance: 29 October Binance Security Incident: Initial Findings and Response Update
   > @_richardteng: On 29 October, Binance was the target of one of the most sophisticated attacks the digital asset industry has ever seen. ~$6.34B in assets were impacted. We take full responsibility...No user bears th
   > @heyibinance: Throughout 2026, Binance's security team detected and prevented 57 suspected North Korea-linked cyber threat cases. These attempts reflect the persistent threat posed by state-sponsored actors targeti
   > @binance: Binance Co-CEO Richard Teng: “We now are operating, we are protecting every user, and we are extremely thankful for our users' confidence and trust
   > @alexinexxx: genuinely impressed by the level of sophistication of this hack. this is an entirely different league from those pathetic CVE exploits [image] [embedded post]
   Also: Reuters, Binance Blog, The Information, Washington Post, Help Net Security, CNBC, Reuters, Silicon Republic, +12 more

31. AI sales automation startup Nooks secures a $500M commitment from General Catalyst's CVF, which will take a share of the returns generated by the capital
    — https://www.reuters.com/business/finance/ai-sales-startup-nooks-secures-500-million-funding-expansion-2026-11-04/
   Also: Unite.AI

32. Uber reports Q3 revenue up 10% YoY to $14.8B, Gross Bookings up 20% to $59.8B, trips up 16% to 4B, and plans to scale its autonomous fleet to 2,000+ in 2027
    — https://www.ft.com/content/2fc1bfc2-4d16-4eb2-a8d4-eaef4f4571af
   Also: Uber, Wall Street Journal, Bloomberg

33. HP names former GSK CEO Emma Walmsley as its new CEO, effective January 4, permanently filling the role after HP's Enrique Lores departed in February 2026
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-04/hp-names-emma-walmsley-as-new-ceo-ending-monthlong-search
   Also: HP, Seeking Alpha, Reuters

34. Analysis: SpaceX revises its 2027 data center capacity target up to a record ~13GW, roughly equivalent to all of Google's capacity from 1999-2026 in 1.5 years
   SemiAnalysis — https://newsletter.semianalysis.com/p/elon-is-doing-it-again-spacex-will
   > @semianalysis_: Elon Is Doing It Again: SpaceX Will Be The World's Biggest AI Cloud Making 13GW in 1.5 Years A Reality https://newsletter.semianalysis.com/ ...
   > @trungtphan: SpaceX completing the build of 13GW from here through 2027 “would be the largest amount of datacenter capacity ever built by any one company in that timeframe, roughly equivalent to all of Google's da
   > @shaunmmaguire: Very interesting analysis...
   > @spcx100t: Now I am not the only one saying it. $SPCX will become world largest SI Cloud.
   > @0xdevshah: Sama - dram sitting idle on consumer computer is net negative Elon - here's a 13gw dyson sphere

35. Google plans to spend $15B across 2027 and 2028 to expand its data center and cloud infrastructure in Malaysia, including building new computing hubs
   Danial Azhar / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-04/google-to-spend-15-billion-in-malaysia-data-center-expansion
   Also: Wall Street Journal, Reuters, Jakarta Globe, Dow Jones Newswires, Malay Mail, Agence France-Presse

36. Legal shifts in Texas and Delaware leave Elon Musk's SpaceX-Tesla merger and Meta's new non-voting share plan better prepared to fend off shareholder lawsuits
   Financial Times — https://www.ft.com/content/e8d40d03-4d86-46ca-aab5-68f7ea69f364
   Also: Hindustan Times, Wall Street Journal, Business Insider, Motley Fool

37. A software engineer details how he went from merging eight to 20 pull requests per month to 200+ after joining AI-native creator startup Tano eight months ago
   Neil Kakkar / The Pragmatic Engineer — https://newsletter.pragmaticengineer.com/p/how-software-engineering-is-changing
   > @neilkakkar: 1/ I won @Pragmatic_Eng 's essay competition! The essay just went live: https://newsletter.pragmaticengineer.co m/ ... I write about how AI is changing software engineering, contrasting @posthog 's pr

38. ITjuzi: Chinese embodied AI companies raised ~$13B across 322 deals in H1 2026, up 5x YoY, as robot makers shift focus from hardware to AI
   Reuters — https://www.reuters.com/world/china/chinas-robot-makers-have-mastered-moves-now-comes-race-brains-2026-11-01/
   > @thepandaily: ITjuzi's report shows how concentrated it is: the top 20 companies took 59% of the RMB 93.5B, led by X Square Robot's RMB 6.3B Series C. Angel rounds alone topped 100 deals, and Beijing led all cities
   Also: Bloomberg

39. Q&A with Simile CEO Joon Sung Park on claims that its digital twins predict human behavior with 85%+ accuracy, its goal of simulating all 8B people, and more
   Mario Gabriele / The Generalist — https://www.generalist.com/p/a-portrait-of-eight-billion-people

40. Meta raised $15B in a US dollar bond sale; sources: the offering drew as much as $58B in orders and is the biggest portion of a $20B+ cross-border bond offering
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-03/meta-kicks-off-debt-offering-in-push-to-fund-ai-investments
   > @beffjezos: Zuck/acc
   > @rohanpaul_ai: Meta raised $15B in bonds for AI build-out, and drew $58B in orders, about 3.9 times the deal size and in line with this year's major tech bond sales. Meta is projected to spend more than $740B on AI 
   > @unusual_whales: BREAKING: Meta is aiming to raise between $20 billion and $25 billion in a bond sale, per CNBC The sale is expected to be two-thirds U.S. dollars and one-third in Euros, according to people familiar w
   > @joemccann: 4x covered, still 90 bps wider than April
   > @ns123abc: BREAKING: META is raising another $25 billion in debt to fund AI infrastructure > S&P: your capex is unsustainable > meta: watch this The Zucc cannot be stopped.
   Also: Bloomberg, Reuters, CNBC, Dow Jones Newswires, Wall Street Journal, The Economic Times, Focus Taiwan, CoinGape, +4 more

41. California accepts $1.42B in US federal broadband funding, but challenges the Trump administration's demand that it stop enforcing state net neutrality rules
   Jon Brodkin / Ars Technica — https://arstechnica.com/tech-policy/2026/11/california-fights-preposterous-trump-admin-demand-to-scrap-state-broadband-laws/
   > @tedatpolicyband: .@CAgovernor Gavin Newsom takes the $1.4 billion from the BEAD program assigned by @NTIAgov, but his @californiapuc says it will not forfeit its authority to regulate retail broadband rates or to defe
   Also: American Prospect, KQED, CalMatters, Broadband Breakfast

42. Q&A with NYC Mayor Zohran Mamdani on new municipal AI policy measures, like an AI ban for some students, support for a one-year data center pause, and more
   Katie Drummond / Wired — https://www.wired.com/story/the-big-interview-podcast-nyc-mayor-zohran-mamdani/
   > @wired: “I have family members sending AI videos of me, to me, thinking that it's real.” Zohran Mamdani tells WIRED that he thinks AI is fueling a “crisis of faith” in reality. Read the full interview: https:
   > @noahshachtman: The legislation that @ZohranKMamdani is referencing? It's co-sponsored by a majority of the City Council. If @JulieMenin allows it to come up for a vote, it become law.
   > @nkulw: lmao what a smartass
   > @nataliekorach: “I think first they would do it in a WIRED interview” lol
   > @alexandermccoy4: .@NYCMayor @ZohranKMamdani in an interview with @WIRED:

43. Traversal, which provides AI agents for site reliability engineering, raised $120M co-led by Kleiner Perkins, Redpoint, and Khosla at a $1B valuation
   Rashi Shrivastava / Forbes — https://www.forbes.com/sites/the-prompt/2026/11/03/the-billion-dollar-business-of-fixing-what-ai-builds/
   Also: FinSMEs, Traversal, SiliconANGLE, WOWTALE

44. Super Micro reports Q1 revenue up 298% YoY to $19.95B, above $16.39B est., and forecasts Q2 revenue above estimates; SMCI jumps 7%+
   Reuters — https://www.reuters.com/business/super-micro-forecasts-quarterly-revenue-above-estimates-strong-ai-server-demand-2026-11-03/
   Also: Bloomberg, Supermicro, SiliconANGLE

45. Sources: Ubisoft and at least two other gaming companies offered to acquire Arkane Studios from Microsoft, which is exploring options before a December deadline
   Jason Schreier / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-03/xbox-s-arkane-studios-attracts-multiple-bidders-including-ubisoft?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MzczODc4NywiZXhwIjoxNzk0MzQzNTg3LCJhcnRpY2xlSWQiOiJUTlkxTDNWVFRDWk4wMCIsImJjb25uZWN0SWQiOiJCMUVBQkI5NjQ2QUM0REZFQTJBRkI4MjI1MzgyQTJFQSJ9.ix5loaB0Yf6oezkpCA7U-aWqZrr-beJQjpgNiY0OlJ8&leadSource=article-gifting
   Also: Wccftech, Eurogamer.net, Fortune, GamesIndustry.biz, Windows Report, Tech4Gamers

46. CrowdStrike debuts an AI kill switch in Falcon Guardian to stop internal AI agents that go rogue, and announces a Falcon Guardian integration with Claude Cowork
   Samantha Subin / CNBC — https://www.cnbc.com/2026/11/03/crowdstrike-ai-kill-switch-rogue-agents.html
   Also: CSO, CrowdStrike, CrowdStrike, The Indian Express, CrowdStrike
