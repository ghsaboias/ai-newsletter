# Research — News Cluster

Search for news **events that occurred** between **2026-11-17 10:00 BRT** and **2026-11-18 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it. One exception, the **agenda**: an event scheduled to happen before the next edition goes out (2026-11-19 10:00 BRT) — see the Agenda rule below.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-11-17 10:00 BRT to 2026-11-18 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
- **Agenda — what happens before the next edition.** A high-profile event in your beat with a set date between now and 2026-11-19 10:00 BRT (a launch, a vote, a ruling, an earnings release, a keynote, a summit) qualifies when its latest concrete confirmation (date set, license granted, vehicle on the pad, final schedule published) falls in the window. The reader opens the edition before the event and should know it is coming. Write it as a preview: what is planned, when (with the time and timezone from the source), and what is at stake. Add `"scheduled_at"` (ISO 8601 with offset) to the story. A launch, test or vote that is the first of its kind or the next step of a story the newsletter follows is high-profile; routine ones are not.
- **Salience over beat balance.** Before you pick, ask: what in my beat will a reader who follows tech and geopolitics hear about everywhere today? Those stories go in first, whatever the sub-area. A slot left empty while such a story sits in your search results is a miss.
- **Novelty beats frequency.** Some event types happen every week: a rocket launch, a funding round, a model release, an earnings call. Their weight comes from what had never happened before, not from the type: the first catch of a rocket's upper stage, the first approval of a drug class, the first model to pass a benchmark. Judge each one by its first-ever element, put that element in the headline and the first key fact, and never file it as routine because its type is common. In the `rejected` log, a routine-looking event you dropped says why it had nothing new.
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
2. **Landscape scan**: Review the Techmeme scan, then run 5 searches to fill gaps. One of the 5 is the **agenda search**: what in your beat is scheduled between now and 2026-11-19 10:00 BRT. Stop searching.
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

**Date:** 2026-11-18
**Research window:** 2026-11-17 10:00 BRT → 2026-11-18 10:00 BRT (24h)
**Agenda horizon (next edition):** 2026-11-19 10:00 BRT

**Previous edition headlines (2026-11-17 — skip unless genuinely new development):**
- california-sues-openai-hugging-face-rogue-agents: California sues OpenAI over its escaped AI agents' attack on Hugging Face, citing 80+ incidents
- isomorphic-labs-5b-series-c: Isomorphic Labs raises $5B Series C led by Sequoia and Greenoaks to push AI-designed drugs to trials
- optimizely-supply-chain-attack-178-sites: Optimizely flaw lets attackers serve card skimmers and iOS exploits on Zoom, BBC, CNN and 175 others
- anthropic-ipo-filing-amazon-google-28-percent: Anthropic filing shows Amazon and Google will own ~28% after IPO, set to price Wednesday evening
- openai-nato-daybreak-300b-tokens: OpenAI gives NATO its cyber-defense models via Daybreak; alliance uses up to 300B tokens a month
- anthropic-cuts-disclosure-window-30-days: Anthropic cuts bug-disclosure deadline from 90 to 30 days, saying AI makes rediscovery likely
- eu-preliminary-dsa-breach-temu-illegal-products: EU preliminarily finds Temu in breach of DSA over illegal products, risking fine of up to 6% of turnover
- bis-remote-access-rule-southeast-asia-chips: US rule closes chip 'remote access' loophole, adds license curbs on 4 Southeast Asian nations and Brazil
- nvidia-board-export-control-committee: Nvidia board creates export-control oversight committee; board not weighing Huang's return
- megaspeed-probe-commerce-doj-timeline: Commerce and DOJ say Megaspeed export probe began in 2024; Nvidia blacklisted it in June 2025
- nvidia-q3-earnings-first-without-huang: Nvidia reports Q3 today, its first results since Huang's exit, with the stock down ~24% this month
- nvidia-rubin-hpc-gpu-sc26: Nvidia unveils Rubin HPC, a science GPU with a record 50,000+ CUDA cores, due in 2028
- google-quaise-superhot-geothermal-ppa: Google signs first commercial superhot-rock geothermal deal: 50 MW from Quaise for Oregon data centers
- top500-record-low-new-systems: TOP500 adds just 27 new supercomputers, a record low, as hardware flows to AI factories
- ukraine-collapses-kerch-bridge-road-arch: Ukraine drops a road arch of Russia's Crimean Bridge into the sea after weeks-long strike campaign
- black-sea-two-ships-sink-bulgaria-eez-drones: Two ships sink in two days in NATO member Bulgaria's Black Sea zone after drone strikes
- iran-third-bahrain-radar-attack-hormuz-tanker-crew-missing: Iran fires drones at US radar in Bahrain for third time in a week as mediators push talks
- trump-asia-thailand-trade-statement-quad-manila: Trump opens Asia trip in Manila: Thai tariff pledge and first Quad summit in two years
- global-stock-selloff-chips-oil-dollar-fed-hike: Global stocks slide for a fourth day as chip shares sink 5.3% and oil drops below $92
- jpmorgan-chase-software-bug-bank-outage: JPMorgan Chase software bug disrupts online banking and Zelle payments across US banks
- fda-approval-day-giredestrant-rybrevant-hnscc-firsts: FDA clears a batch of firsts: first new second-line head-and-neck cancer drug in a decade
- us-air-travel-faa-ground-stop-aftermath-united-outage: US air travel limps back after FAA ground stop; United hit by its own system outage
- deutsche-bank-15m-files-leak-oligarchs-epstein: Leak of 15M Deutsche Bank files shows courting of Russian oligarchs and Epstein-linked flows
- corma-125m-series-a-1b-valuation-ai-cyber-defense: AI cyber-defense startup Corma raises $125M Series A led by NEA, hitting $1B valuation in ~3 months
- china-canada-expand-tariff-relief-xi-carney: Xi and Carney expand China-Canada tariff relief, suspending steel and aluminum duties to 2028
- nvidia-madison-huang-chief-of-staff-test-for-kress: Jensen Huang's daughter Madison stays in senior Nvidia role after alienating executives, NYT says
- anthropic-direct-900b-data-center-875k-tpus: Anthropic's 'Anthropic Direct' data-center network commits $900B+ through 2045, FT reports
- anthropic-ipo-pitch-altimeter-5b-mythos-amd-port: Anthropic IPO pitch: Altimeter eyes $5B order; Mythos Preview ported AI to AMD GPUs in ~3 days
- macos-27-3-beta-warns-against-full-access-for-ai-apps: macOS 27.3 beta warns users against giving AI apps full disk access
- china-ai-distillation-us-models-reuters-review: Reuters review of 300+ Chinese documents: AI distillation from US models is now mainstream industrial practice
- nhs-keeps-palantir-330m-contract-until-2029: UK NHS plans to keep its £330M Palantir contract until 2029 instead of exiting early in 2027

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 47 stories

1. GTA VI review: an unparalleled technical and comedic masterpiece, with elaborate depictions of a heightened reality and an unpredictable environment by design
   Jason Schreier / Bloomberg — https://www.bloomberg.com/news/features/2026-11-18/gta-6-review-rockstar-games-latest-is-a-masterpiece?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5NDk5OTYzNCwiZXhwIjoxNzk1NjA0NDM0LCJhcnRpY2xlSWQiOiJUT1AyS0hLR0lGUTgwMCIsImJjb25uZWN0SWQiOiJCMUVBQkI5NjQ2QUM0REZFQTJBRkI4MjI1MzgyQTJFQSJ9.pks5MCyquJRoPSiA_59TfyguHaO8mfXluOkX8OZaVSY
   It turns out that the secret ingredients to a great game are a lot of money, time and talented people.
   > @genepark: new GTA6 screenshots in my review. mission design is no longer “drive here, shoot people.” many missions are about navigating tense social situations, violence can be avoided. it's also great at steal
   > @pkafka: The new Grand Theft Auto lets you shoot and rob people but also lets you do squats and kettlebell raises. Its release this week is the biggest entertainment event of the year - bigger than multiple bl
   > @hshaban: GTA 6 is a gigantic news story and cultural event. Media outlets are rightly covering it. But all the attention this week makes it more obvious than usual how short-sighted and confused newsroom bosse
   > @gtasix_: Jason getting eaten by an alligator in GTA 6.
   > @daveloach2: “Authentic human bond” I'm loling
   Also: Metacritic, The Guardian, IGN, Eurogamer.net, Game Informer, Digital Foundry on YouTube, IGN, Metacritic, +49 more

2. Sony and Rockstar say a new PS5 firmware update is mandatory to play GTA VI, which launches on November 19, likely in a bid to combat rapid homebrew exploits
   Wesley Yin-Poole / IGN — https://www.ign.com/articles/sony-issues-official-ps5-firmware-update-warning-confirms-gta-6-requirement
   When will the Whac-A-Mole end? — Sony has confirmed that the recently released PS5 firmware 14.23 update is required to play GTA 6 …
   > @ps_support_us: Sony Interactive has issued a PS5 system software update that is required before playing Grand Theft Auto VI. Players should download this update prior to midnight on November 19 so that they're ready
   > @playstation: 👀
   > @samvale29: Heads up if you're playing GTA VI on PS5 day one: don't leave this for launch night. …
   > @manfightdragon: PlayStation have just released firmware 14.23, and done something they've never done before. They've immediately cut all PSN access older firmware. (Usually 14 days grace) When GTA6 unlocks, anyone wh
   > @realradec: the two mfs who are working overtime on deploying PS5 system software updates [image] [embedded post]
   Also: PCMag, Phandroid

3. Rockstar says GTA VI targets 30fps across all current-gen consoles; PS5 and Xbox Series X upscale the game from 1440p to 4K and Xbox Series S from 720p to 1080p
   Alessio Palumbo / Wccftech — https://wccftech.com/grand-theft-auto-vi-amd-fsr-4-xbox-series-s-ray-tracing/
   During Grand Theft Auto VI's review period, Rockstar Games offered us the chance to send some questions to the developers.
   > @charlieintel: Grand Theft Auto VI runs at a base resolution of 1440p on both PS5 Pro and PS5, but reaches 4K with PSSR on PS5 Pro The game runs at ‘unwavering’ 30FPS on PS5 Pro, but on base PS5 can fall down to mid
   > @bartonovopolis: Goddammit man, this is gonna feel rough 😭
   > @okami13_: Digital Foundry's breakdown on GTA 6.... 30 seconds in and my mind is already blown. ▫️ “Landmark achievement in visual realism, simulation density, and world design.” ▫️ Ray traced lighting system is
   > @exoghost: Playing GTA 6 right now The performance is horrible. This is less than 30 FPS. It's like 24 FPS
   > @pirat_nation: Digital Foundry has published its technical analysis of GTA VI, calling it the most detailed and realistic open world they've ever seen. > 30 FPS on both PS5 and PS5 Pro. > 1440p internal resolution o
   Also: Digital Foundry, VideoCardz.com, Video Games Chronicle, GamingBolt, Pure Xbox, Tech4Gamers, IGN, DayOne

4. GTA VI's main campaign completion time ranged from 42 hours for a “rushed” playthrough to 115 hours for an exploration-heavy playthrough, per four reviewers
   IGN — https://www.ign.com/articles/how-long-is-gta-6
   Also: Eurogamer.net, Pure Xbox, Video Games Chronicle

5. Rockstar's GTA VI hits a 99/100 rating on Metacritic and 98/100 on OpenCritic, a record for both, as IGN and GameSpot give it perfect scores; TTWO jumps 6%+
   Jason Schreier / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-18/-grand-theft-auto-vi-becomes-the-best-reviewed-video-game-ever
   Also: TechRadar, GamesIndustry.biz, Game World Observer, Forbes, Comic Book, 9to5Toys, Digital Trends, Windows Central, +7 more

6. An interview with Rockstar North's Rob Nelson on the “risk” of a romantic story, switching from GTA V's split storyline to a co-dependent partnership, and more
   Andrew Webster / The Verge — https://www.theverge.com/entertainment/1035806/grand-theft-auto-6-rob-nelson-interview
   Also: TechRadar, Deadline, TheGamer, Rock, Paper, Shotgun, GamesBeat, IGN, GamesRadar, Kotaku

7. Sources: Wall Street execs and the NSA told Congress this week's outages stemmed from systems overwhelmed by a rush to patch vulnerabilities found by AI models
   Jeff Stein / The Washington Sun — https://www.washingtonsun.com/technology/bank-ceos-nsa-tell-congress-ai-driven-patches-behind-outages
   Wall Street executives and the National Security Agency have told members of Congress that this week's widespread tech outages …
   > @semianalysis_: https://x.com/...
   > @ssankar: There is a reason we made Apollo. The only way to responsible manage upgrade delivery as AI inflects code velocity. https://www.palantir.com/...
   > @natolambert: this is like, the best cyber news we've gotten in a long time? things working [embedded post]
   > @andrewcurran_: Heh, it's an interesting angle. Benevolent collapse. [embedded post]
   > @noahpinion: Uh huh
   Also: Wall Street Journal, BBC, Futurism, Sky News, Townhall, Forbes, Intelligence Report

8. Tech outages disrupting everything from air travel to banking transactions over the past week have fueled public distrust and paranoia about tech infrastructure
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-17/tech-paranoia-intensifies-after-outages-roil-public-trust
   Technology failures disrupting everything from Americans' air travel and banking transactions to secretive work …
   > @peterwildeford: There are lots of outages... Why? AI attacks? My more normal guess is that because there have been a lot of AI-discovered cyber vulnerabilities (including lots probably not yet disclosed), companies a
   > @buckleyplanet: @Techmeme Trust comes back through the boring stuff: a published root cause, a clear timeline, and a fallback people can actually see. It works the same way inside a company. Tell people what broke, w
   > @markwarner: I understand why Americans are concerned about the widespread outages we've seen in recent days, affecting everything from banks and major technology companies to critical government systems. At this 
   > @davetroy: A way to think about these outages: AI is finding software vulnerabilities at breakneck speed. Alerts are going out to IT teams telling them they have to upgrade stuff or face dire consequences. They 
   > @nhegde: With outages every day, we are really being taught the lesson of the dangers of a few companies having control over big parts of the economy.
   Also: Wired, CNBC, Forbes, New York Times, Semafor, Washington Post, NewsMax.com, Fox News, +10 more

9. Marco Rubio says there's “zero evidence” linking the recent FAA ground stop, Microsoft outage, and bank service issues, and the US isn't “under systemic attack”
   Kiki Intarasuwan / CBS News — https://www.cbsnews.com/news/marco-rubio-tech-outages-not-connected/
   Also: BBC, The Hill, 9to5Mac, Bloomberg, Associated Press, The Guardian, New York Post

10. The FAA pauses installations of Juniper routers like the one officials believe contributed to Friday's ground stop; HPE says its Juniper device wasn't defective
   Neil Vigdor / New York Times — https://www.nytimes.com/2026/11/17/us/faa-routers-ground-stop.html?unlocked_article_code=1.RVE.NvSB.4mbzPoegpFNf&smid=url-share
   Also: Wall Street Journal, U.S. Senate Committee …, ABC News, Reuters, PCMag, Fox Business, The Hill, CNBC, +1 more

11. Nvidia reports Q3 revenue up 103% YoY to $115.8B, above $109.1B est., Data Center revenue up 110% to $107.6B, and forecasts Q4 revenue above est.
   Nvidia Newsroom — https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027
   - Revenue of $115.8 billion, up 103% from a year ago — Data Center revenue of $107.6 billion, up 110% from a year ago
   > @timsweeneyepic: Just think of what NVIDIA could do if they invested $150 billion back into their business in America. NVIDIA could build multiple massive new leading-edge fabs. New jobs. Reindustrialization. End the 
   > @alistairmbarr: Nvidia Board chair: we're not hiring Jensen back Stock drops Nvidia interim CEO: we're raising 2028 fiscal yr outlook Stock rebounds
   > @munster_gene: $NVDA made a statement tonight: Even without Jensen, we're gonna continue to crush it.
   > @benbajarin: Interesting $NVDA put out a blog emphasizing their supply chain commitments. Interpreted as, the plan to keep growing is set in stone. https://nvidianews.nvidia.com/ ...
   > @pitdesi: Nvidia is an absolute monster of a company. $115.8B Q3 revenue, up 103% YoY. 75% gross margins. $65B in quarterly net income. Guiding to $130B in Q4 revenue, assuming ZERO Data Center compute revenue 
   Also: Nvidia Newsroom, Tom's Hardware, The Verge, CNBC, Breitbart, Fortune, The Register, Feld Thoughts, +20 more

12. Sources: Nvidia made two separate introductions in 2022 connecting Alibaba with alleged Chinese spy Alice Huang, helping Megaspeed land Alibaba as a customer
   The Information — https://www.theinformation.com/articles/nvidia-introduced-alibaba-alice-huang-workaround-u-s-export-controls
   Nvidia's sales team introduced Chinese tech giant Alibaba to Alice Huang, the alleged Chinese spy involved in smuggling Nvidia chips into China …
   > @leomschwartz: New reporting into the early relationship between Nvidia, Megaspeed's Jensen Huang, and China tech giant Alibaba from @JuroOsawa and @QianerLiu. Nvidia's sales team introduced Alibaba to Alice Huang, 
   > @choblin29: Holy, Nvidia reportedly introduced Alibaba to Alice Huang TWICE in 2022, including after the first US restrictions on advanced AI chips, Information reports. The introductions helped Huang's future Me
   > @edzitron: Hahahaha oh that's a nice headline
   > @kakashiii111: Jensen was the king of matchmaking. The king of “lock in supply first, assign demand later.”
   > @amir: 👀 the Nvidia / Alice Huang relationship runs deeper than previously known
   Also: Digital Trends

13. Colette Kress says Nvidia will no longer sell H200 chips in China, ending its role in a deal brokered by Huang and Trump that let the US collect a 25% tariff
   Tim Fernholz / TechCrunch — https://techcrunch.com/2026/11/17/nvidia-is-abandoning-china-after-jensen-huangs-ouster/
   Nvidia will no longer sell its H200 chips in China, acting CEO Colette Kress said Tuesday, ending the company's participation …
   > @onlyyoontv: #China has no comment on @nvidia interim CEO Kress saying future “guidance does not have any licensed Hopper data center products included, and we are no longer shipping licensed Hopper data center pr
   > @justjoshinyou13: Nvidia sold <=100k H200s to China last quarter, and maybe don't think they will be able to sell anymore? In the past few quarters they have always said their next quarter guidance doesn't include Hopp
   Also: Bloomberg, Quartz, The Verge, CBS News, Wall Street Journal, Reuters, Political.org

14. Sources: ex-Nvidia executive Jay Puri, who oversaw clients like Alice Huang, controlled chip sales to Supermicro; Puri is married to an ex-Supermicro executive
   The Information — https://www.theinformation.com/articles/jensen-huangs-right-hand-man-oversaw-chip-customers-including-alice-huang
   > @jingyanghk: Who knew? Jay Puri, Nvidia's longtime sales chief, handled customer relations w/Alice Huang & is married to a former exec at Supermicro, which is being investigated for chip smuggling into China. Dyna
   > @amir: As U.S. probes of Nvidia go on, many roads lead to Jay Puri, its longtime former sales chief, who oversaw customers (and dealt w/folks incl Alice Huang) and is married to a former Supermicro executive
   > @martijnrasser: A development worth watching. Disclosure: I'm a former chief of staff at Muddy Waters, and I know firsthand they don't shoot from the hip.
   > @muddywatersre: Muddy Waters is short $NVDA A woman identified as Cenly Chen, referred to in some photograph tags as Cenly Puri, has been photographed in public between 2024 to 2026 with Ajay K. Puri. Until this June
   Also: The Hill, Telegraph, Korea JoongAng Daily

15. Sources: the US SEC is investigating Nvidia, including whether its disclosures misled investors, adding to the crisis facing the company; NVDA is down 15%+ YTD
   Wall Street Journal — https://www.wsj.com/business/sec-is-probing-nvidia-amid-departure-of-ceo-jensen-huang-ee7643f8?st=JDfemd&reflink=article_copyURL_share
   Regulator's civil probe looks at whether company violated investor disclosure laws — The Securities and Exchange Commission …
   > @anissagardizy8: NEW: SEC Is Probing Nvidia Amid Departure of CEO Jensen Huang The civil investigation adds to the crisis facing Nvidia, whose shares have fallen more than 10% since Huang was ousted. w/ @davidamichael
   > @garymarcus: a good quarter doesn't solve this
   > @kakashiii111: There is a lot for the SEC to investigate in Nvidia's Beat and Raise.
   > @abebrown716: A shortlist of Nvidia investigations/probes/hearings: Even if they all find absolutely nothing wrong happened, they still present a ... staggering amount of corporate distraction. 👀 Board investigatio
   Also: TechCrunch, Politico, PYMNTS.com, Financial Times, The Decoder, Wall Street Journal, Mercury News, New York Times, +7 more

16. Nvidia's Q3 earnings call: Chair Harvey Jones says Nvidia's board “does not intend to reinstate” Jensen Huang as CEO and unanimously accepted his resignation
   Hayden Field / The Verge — https://www.theverge.com/report/1035465/nvidia-says-it-will-not-reinstate-jensen-huang-as-ceo?view_token=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjA3cFNpbDJCT1MiLCJwIjoiL3JlcG9ydC8xMDM1NDY1L252aWRpYS1zYXlzLWl0LXdpbGwtbm90LXJlaW5zdGF0ZS1qZW5zZW4taHVhbmctYXMtY2VvIiwiZXhwIjoxNzk1Mzg1NDc1LCJpYXQiOjE3OTQ5NTM0NzV9.PWMNbp8LvjiIh6EH1gdv9OqWZ7SGbuRwywWf6K983Vg&utm_medium=gift-link
   > @8teapi: Jensen is not coming back I know it sucks but The board is doing the right thing. 1) Take the pain once - Jensen is 63, he's been with the company 33 years. Succession has been a persistent question f
   > @johnwilson: But has he read through the petition yet? Or Gavin's and Brad's letter? 🤣🤣🤣 [embedded post]
   > @kantrowitz: Nvidia on its earnings call sounded like a company moving on from Jensen. “We've got this” were the concluding words from interim CEO Colette Kress
   > @davetroy: Ultimately Jensen needed a grown up to be CEO, do risk management and compliance, while letting Jensen oversee the supply chain and engineering interface. He clearly just wasn't qualified for aspects 
   > @hadas_gold: More... “While this was an unexpected transition, the board acted deliberately and in the best interest of the company's employees, customers, partners, and shareholders.” Say they will not answer any
   Also: Washington Post, Wired, The Information, Business Insider, South China Morning Post, The Verge, GamesBeat

17. Sources: a faction of Nvidia's board members is pushing for Jensen Huang's return despite Chair Harvey Jones stating the board doesn't intend to reinstate Huang
   Semafor — https://www.semafor.com/article/11/17/2026/some-nvidia-directors-push-to-bring-huang-back-despite-board-opposition
   > @beffjezos: Can Trump step in and delete Ms Crunchwrap Supreme and Miss Coca Cola? How the f* is national security and the fate of all of AI compute being decided by a tiny committee of randos instead of a shareh
   > @analyticacamil1: 3 to go
   > @garrytan: Only three people to remove from the board? Easy work 15% shareholder vote coming
   > @reedalbergotti: Scoop with @rogoswami - Nvidia board is divided into factions, with one three-person faction vehemently against a Jensen Huang return. https://www.semafor.com/...
   > @brickroad7: Wow! Only a 3 person faction is seriously against it? That means 6 of the 9 are open to convincing! And Jensen already has multiple pushing for him? So worst case scenario you need just 3 more of the 
   Also: Tom's Hardware, CNN, 24/7 Wall St., Political.org, VideoCardz.com, Press Trust of India

18. A growing religious and quasi-religious revival is permeating the AI industry, featuring apocalyptic warnings, secret prophecy lectures, and fringe movements
   Sam Kriss / New Yorker — https://www.newyorker.com/magazine/2026/11/23/the-buddhist-ai-sect-that-wants-to-take-over-silicon-valley?currentPage=all
   We are living through the End of Days. A terrible Beast is rising out of the sea to conquer and destroy the world.
   > @tinyrevver: Perhaps it's not landing bc of the general doom atmosphere, but i dunno how more people around here aren't talking about this essay, which is bonkers https://www.newyorker.com/...
   > @hamandcheese: Is just turns out to be true that a lot of this really was pretty baked-in from the advent of the transitor
   > @geraldleroy6: A profile of a Buddhist monk in Vermont who recruits Silicon Valley engineers to create enlightened AI. An unsettling exploration of charismatic leadership, spiritual control, and the ambition to buil
   > @roryisconfused: AI people love sects, they are just fucking mad for being adjacent to or inside of sects
   > @aella_girl: ""We would say you enter a place, you merge with it, and you fully participate," he told me. I clarified that I had never claimed to be objective, that I was fine with just having my own view, but thi

19. Masayoshi Son says passing on a 2023 opportunity to invest in Anthropic was a “mistake”, noting that “by that point, we had already decided to invest in OpenAI”
   Financial Times — https://www.ft.com/content/08086201-6359-47ec-8854-70462ad5a4c0
   Japanese tech group had already started to put money into arch-rival OpenAI
   > @danprimack: One takeaway from lots of convos in NYC is that everyone is VERY confident that Anthropic is going to have a successful IPO pricing tonight.
   Also: Bloomberg

20. Anthropic IPO is set to redraw VC power rankings, with lesser-known firms like Spark Capital poised for outsized returns compared with larger, blue-chip rivals
   George Hammond / Financial Times — https://www.ft.com/content/a3430f0d-0080-4970-8eec-2c14c8438b3d?accessToken=zwAAAaHtopUSkdOjQw8NAIBJcNOO7CwUyEOLPQ.MEUCIF1q7aLCnP63ba_HSXgJrufMSFKbE0XM6j8UzDPK2UaJAiEAwlWU3Tct7FROgNE7x9sr3LUUt1DjFS0mZu406msl96Y&sharetype=gift&token=a97c7641-a9cb-433e-a6b6-ea4083f6a825
   > @nmasc_: A farewell private markets scoop from yours truly https://www.bloomberg.com/... [image]
   > @nmasc_: Scoop: Anthropic's most notable VC backers including Sequoia, Lightspeed, Iconiq and more are set to pour more money into the company in its IPO https://www.bloomberg.com/...
   Also: Bloomberg, Newsweek

21. Microsoft makes Word, Excel, and PowerPoint generally available inside Copilot, which Satya Nadella calls “the new OS for work” in his Ignite keynote speech
   Nick Indge / Ars Technica — https://arstechnica.com/gadgets/2026/11/microsoft-calls-copilot-the-new-os-for-work-at-ignite-keynote/
   Opening the keynote at its Ignite event, Microsoft CEO Satya Nadella outlined the company's vision for its new …
   > @mgsiegler: Just as a new James Bond was chosen, Microsoft has anointed Copilot as the new “OS for Work”, following Teams brief run, with SharePoint, Yammer, Outlook, Office, and Windows itself before that... [em
   > @satyanadella: Highlights from my opening of the Ignite keynote this morning on how we're building a frontier ecosystem to turn advances in AI into real-world impact.
   Also: Creative Strategies, GeekWire, ITPro, International Business Times, WinBuzzer, Digital Trends

22. Microsoft unveils seven AI models spanning coding, cybersecurity, images, and voice, saying MAI Code 2 has 98% of GPT-6.1 Sol's performance at ~40% of the price
   Ina Fried / Axios — https://www.axios.com/2026/11/17/microsoft-ai-models-openai-anthropic-ignite
   > @taiwei_shi: Check out MAI Code 2 and Code 2 Flash! Happy to be part of this effort to bring foundation models into real-world enterprise productivity scenarios across Microsoft 365. https://microsoft.ai/...
   > @windowsdev: Big news from #MSIgnite! 🚀 See how Windows brings security and Hybrid Intelligence to the next era of work, with new security features, secure AI agents, local AI, Copilot, and AI infrastructure from 
   > @rachelconlan: Big news to kick off Day 2 of #Breakpoint2026 🚀 The Solana Foundation is backing @CoinGecko, one of the most trusted names in crypto. For years, CoinGecko has played a critical role in making crypto m
   > @satyanadella: Our ambition with everything we are announcing at Ignite today is to parlay technological advances into real outcomes and new points of leverage for people, organizations, and society at large. Just a
   > @finkd: Muse Wonder, Muse Spark 1.3, and Muse Ember are coming soon to Microsoft Foundry on @Azure.
   Also: Microsoft AI, Microsoft AI, Windows Blog, Bloomberg, Microsoft, ZDNET, Microsoft Copilot Blog, Microsoft, +19 more

23. A look at AI-related literary disputes and debates over Pangram, which flagged Peruvian author David Silva Rojas's award-winning novel as 99% AI-generated
   Brunella Tipismana Urbano / The Point Magazine — https://thepointmag.com/examined-life/the-part-about-the-machines/
   The news has already traveled the world, but for those who haven't yet heard: three weeks ago, El País published an article declaring …
   > @brianluidog: I always wonder. Why do we expect STEM people to know humanities stuff? Yet humanities people would never be asked to learn basic physics. I think there's a tacit agreement that humanities people are 
   > @wesleylhuff: I take the concerns about plagiarism in my written work seriously. Honesty and integrity matter deeply to me, and not correctly crediting others' work, in any setting, falls short of those standards. 
   > @left_plain: lol @ all the checkies fainting and swooning over the first mildly literate person they can find to articulate their frustrations at everyone not simply giving up and accepting their ubiquity and impo
   > @romeooriogun: I wish people would start suing you guys. The only reason you all are so bold in using the intellectual property of African writers like this is because you know you can get away with it. You wouldn't
   > @j_chiemeke: 187 titles authored by African writers fed into an LLM?? I'm curious to see the copyright permissions granted by each author and/or their representatives. I actually want to see documentary evidence o
   Also: Yudhanjaya Wijeratne

24. Sources: the Trump administration is considering requiring US companies to disclose on their websites if they use Chinese AI models, seeking to discourage usage
   Alexandra Alper / Reuters — https://www.reuters.com/world/china/trump-administration-weighs-forcing-us-firms-disclose-chinese-ai-use-2026-11-18/
   The Trump administration is considering requiring US companies to publicly disclose their use of Chinese AI models …
   > @natolambert: This is stupid. What counts as a chinese model? What about Thinky's model distilled from Kimi? What about composer, continued pretraining? What about Nemotron, using tons of DeepSeek synthetic data? W
   > @niubi: why would any company be against this disclosure?

25. Sources: ByteDance is in advanced talks with Microsoft to spend an additional ~$500M on Azure, primarily to access OpenAI models, drawing complaints from OpenAI
   The Information — https://www.theinformation.com/articles/microsoft-nears-500-million-deal-sell-ai-bytedance-irking-openai
   ByteDance is in advanced talks to spend an additional roughly $500 million on cloud services from Microsoft …
   > @leomschwartz: Scoop: The Chinese TikTok-developer ByteDance is in advanced talks with Microsoft to spend an additional ~$500 million, primarily to access OpenAI models through Azure, after getting cut off from Anth
   > @aaronpholmes: NEWS: Microsoft is nearing a deal to sell an additional $500m of AI to ByteDance, which is already a big customer. But OpenAI isn't happy, and has groused to MSFT that it thinks Chinese firms are dist

26. Cybersecurity startup Calif says it used GPT-6 Cyber to uncover an RCE flaw in Java dubbed “Java4Shell” and coordinated with Five Eyes; Oracle released a patch
   New York Times — https://www.nytimes.com/2026/11/17/us/politics/ai-security-bug-java.html?unlocked_article_code=1.RFE.J4uR.JL0Qv-280ALN
   The discovery by security company Calif shows A.I.'s ability to find gaping security holes in popular software.
   > @calif_io: Since the vulnerability has leaked: Calif discovered and reported Java4Shell (CVE-2026-114938). We're publishing technical details by 1 PM Pacific today, after Oracle releases a patch. Stay tuned!
   > @watchtowrcyber: watchTowr continues to track “Java4Shell” (CVE-2026-114938) now that public writeups and advisories have been released. Specific CPU, JDK, and Base64 pre-reqs are required. It's likely application-spe
   > @hopefullysc: The joy just keeps coming .. and coming... and coming. Something used by the vast majority of Fortune 500 companies https://www.cisa.gov/... [image]
   > @gdb: GPT-6 Cyber for helping further secure the internet, with a major security flaw in Java found by Calif, as part of our Patch the Planet initiative: https://www.nytimes.com/...
   > @magmill95: Because today's news cycle is so calm, CISA is telling organizations to implement a patch for the newly disclosed Java4Shell vulnerability immediately. This is a vulnerability in one of the world's mo
   Also: Calif, CISA, BBC, Gizmodo, Politico, VulnCheck, RTÉ, BleepingComputer, +18 more

27. US House Democrats launch an investigation into Commerce Secretary Howard Lutnick and his family's ties to Nvidia, laying the groundwork for oversight in 2027
   Chris Marquette / Politico — https://www.politico.com/news/2026/11/18/democrats-congress-lutnick-nvidia-01171921
   Democrats on the House Judiciary and Foreign Affairs Committees are launching a probe into whether the Trump administration's response …
   > @chrismarquette_: NEW: Democrats on House Judiciary and Foreign Affairs probing Lutnick family's role in Nvidia scandal https://www.politico.com/...
   Also: Quartz, MS NOW

28. Apple HomeView teardown: a step backward in repairability compared to recent iPads and HomePods, with heavily glued display, speakers, and logic board
   Carsten Frauenheim / iFixit News — https://www.ifixit.com/News/120317/homeview-teardown-a-surprising-step-backward
   Apple's first iPad-stuck-to-a-HomePod smarthome hub landed on our teardown table this week, and we figured we knew what we were getting into.
   > @nicfixem: WARNING TO ANYONE TAKING APART THEIR HOMEVIEW; The Apple HomeView's main logic board is stuck to the case with some of the most aggressive glue I've ever seen. Not just a simple double sided sticky st
   > @nicfixem: The rest of it was shockingly simple to work on; the base is practically all screws, the screen opens from the bottom. 9.5/10 repairability score for the base. 0.5/10 repairability score for the scree
   Also: iFixit on YouTube, 9to5Mac, Digital Trends, The Verge, AppleInsider, Nic's Fix on YouTube, Notebookcheck, MacRumors

29. A US court sentences Tyler Robert Buchanan, a 24-year-old British leader of Scattered Spider, to six years in prison for phishing and stealing $11.6M in crypto
   Sergiu Gatlan / BleepingComputer — https://www.bleepingcomputer.com/news/security/british-scattered-spider-hacker-sentenced-to-6-years-in-prison/
   A leader of the Scattered Spider cybercrime collective has been sentenced to six years in prison in the United States …
   Also: BBC, US Department of Justice, TechCrunch, Security Affairs, The Record, CoinGape, SecurityWeek, Decrypt

30. Tencent President Martin Lau says the US' new “remote access” rules on Chinese chip access “sets everyone back in China” and will delay new AI model training
   Juro Osawa / The Information — https://www.theinformation.com/briefings/tencent-president-new-u-s-chip-rule-sets-everyone-back-china
   Tencent President Martin Lau said Wednesday that Washington's new rule barring Chinese companies …
   > @dalperovitch: “It sets everyone back in China,” Tencent President Martin Lau told analysts on a post-earnings call on Wednesday. “It would take probably a longer time for us to come up with the next version in the 
   Also: Bloomberg, Finimize, Nikkei Asia

31. Tencent reports Q3 revenue up 8% YoY to ~$31.1B, below est., and operating profit down 7% in its first earnings decline in years, as AI capex surges 5x to ~$12B
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-18/tencent-s-sales-miss-estimates-in-setback-for-founder-s-ai-push
   Tied for #1 on the AA Decision Index, Snap is a multimodal model with a 384k-token context window for fast reasoning and agentic decisions.
   Also: Wall Street Journal, The Straits Times, Wall Street Journal, Quartz, Nikkei Asia, Reuters

32. An interview with philosopher Thomas Nagel, who won a $1M prize for contributions to consciousness and says the notion of AI consciousness is “just ridiculous”
   Steven Levy / Wired — https://www.wired.com/story/just-ridiculous-a-famed-philosopher-takes-on-ai-consciousness/

33. Docs: Meta's “Project Gryffindor” initiative in 2024 to acquire new teen Instagram users included school directories, banners, and “school blast” notifications
   Katie McQue / NPR — https://www.npr.org/2026/11/18/nx-s1-6037808/meta-instagram-schools-teens-safety
   Also: The Verge

34. Sources: Apollo's $40B chip financing for SpaceX is structured via a special-purpose vehicle, letting SpaceX keep it off balance sheet and rent the GPUs
   Ellen DiMauro / Semafor — https://www.semafor.com/article/11/18/2026/spacex-40-billion-chip-financing-to-stay-off-balance-sheet

35. Disney and AWS partner to develop AI-powered audio-animatronics of three Star Wars characters, debuting later in November at Amazon re:Invent in Las Vegas
   Alex Weprin / The Hollywood Reporter — https://www.hollywoodreporter.com/business/digital/new-star-wars-robots-disney-amazon-ai-anzellans-1236757851/
   Also: CNET, TechRadar, Disney Experiences

36. Sources: Netflix will join Apple TV, YouTube, Fox, ESPN, and others in a bid for the US rights of FIFA's 2030 World Cup; the auction is set to fetch $1.5B-$2B
   Matt Hughes / The Guardian — https://www.theguardian.com/football/2026/nov/18/netflix-fox-2030-world-cup-television-rights
   > @matthughesmedia: US 2030 World Cup TV rights auction seen as a seismic moment for sports broadcasting, with Fifa poised to cash in. | The Guardian https://www.theguardian.com/ ...
   Also: TheDesk.net

37. Swiss nonprofit Quad9 withdraws its DNS resolver from France after a court ruling imposed large fines, an understandable decision that harms the open internet
   Cloudflare — https://blog.cloudflare.com/quad9-withdrawal-from-france/
   > @eastdakota: People are going to die because of this. It's impossible to know what critical systems Quad9 or any other resolver are built into. Some are about to stop working. France's copyright cops and the court
   > @sysxplore: Quad9's free 9.9.9.9 DNS resolver stops working for everyone in France on 24 November. The Swiss non-profit lost a court case brought by beIN that orders it to block piracy-linked domains for French u
   > @alexmartin: Leaving aside the eternal fight about which layer of the internet copyright should be enforced at, this is simply embarrassing hyperbole. Quad9 chose to withdraw rather than comply with a court order.
   > @cloudflare: Quad9's forced withdrawal from France highlights the dangers of mandating DNS-level blocking. Read more: https://blog.cloudflare.com/ ...
   > @evaxyzh: Really sad to see this today, this is unreasonable interference that fundamentally harms the free and open Internet
   Also: CyberInsider

38. Bengaluru-based Humyn Labs, which creates robot training data using first-person footage from cameras, raised $26M in equity led by Accel and $21M in debt
   Jagmeet Singh / TechCrunch — https://techcrunch.com/2026/11/18/accel-backs-indias-humyn-labs-to-supply-training-data-needed-by-u-s-robotics-ai-developers/
   Also: Bloomberg, Entrackr, SiliconANGLE, Inc42, Moneycontrol

39. KPMG uses 100+ AI agents to conduct a parallel audit of a FTSE 250 company in a pilot, saying the AI asked “better questions” and dug deeper than human staff
   Financial Times — https://www.ft.com/content/5168b3e9-75d0-4be0-9ccd-d327d6b16c05
   > @thesecretacct: I'm glad there was no AI when I started at KPMG. I can't imagine what the profession will look like in just say another five years. Plus many other data and process-driven professions. https://www.ft.
   > @aghisellichina: Wait until they are sued because AI hallucinated
   > @fkronawitter1: So... why do you still need the audit company then...? https://x.com/...
   > @bipinsingh: This is the future
   Also: The Decoder, Security Boulevard, Unite.AI

40. London-based Payhawk, which offers enterprise expense and procurement management tools, raised a $280M Series C led by Goldman Sachs at a $2B valuation
   Yazhou Sun / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-18/goldman-backs-fintech-startup-payhawk-at-2-billion-value
   Also: Payhawk, Tech.eu, FinSMEs, Ventureburn, The SaaS News

41. A Gallup survey of 15,925 people aged 15 to 22 across 16 countries finds that more than 33% rely on AI for companionship, rising to 50% among daily AI users
   Jason Parham / Wired — https://www.wired.com/story/over-a-third-of-gen-z-rely-on-ai-for-friendship/
   Also: Gallup, Phandroid, Digital Trends, 404 Media, Pew Research Center

42. The Solana Foundation takes a majority stake in CoinGecko, a popular crypto price-tracking platform with 18M registered users
   Francisco Rodrigues / CoinDesk — https://www.coindesk.com/business/2026/11/17/solana-foundation-takes-majority-stake-in-crypto-data-provider-coingecko
   > @solanafndn: For more than a decade, CoinGecko has been the #1 crypto market data provider, serving tens of millions of users each year, while also powering 180,000 crypto applications and businesses through their
   Also: Solana Foundation, CoinGecko Buzz, CryptoNinjas, Blockhead, Coinpedia Fintech News, Unchained, Cointelegraph, Bitcoin Insider, +1 more

43. YouTube is rolling out an update to include “co-views”, or the estimated number of people watching together on TV, in the public view counts for videos
   Emma Roth / The Verge — https://www.theverge.com/streaming/1035683/youtube-co-views-count
   > @youtubeinsider: YouTube is rolling out an update to include co-views - the estimated number of people watching together on TV - in the public view counts for videos YouTube is doing this because viewers are now watch
   > @youtubeinsider: New! Co-views included in the public YouTube viewcount
   > @mattihaapoja: It's starting to feel like YouTubes total views are going down or have plateaued so now we are getting more of these “we are changing how we count views” decisions. I think Instagram is taking the cre
   > @paulwhitewick: Here we are. As I said. Why are youtube doing this I wonder. A new “flex” following their August uodate
   > @reneritchie: YouTube is doing this because viewers are now watching over 1 billion hours of YouTube on TVs every day, and the inclusion of co-views in the public view count will: - Credit creators true reach with 
   Also: How-To Geek, PCMag, Music Ally, WinBuzzer, Engadget

44. LanceDB, which makes a multimodal lakehouse for AI training, built on the open format Lance, raised a $57.5M Series B led by Bessemer and Innovation Endeavors
   Kyt Dotson / SiliconANGLE — https://siliconangle.com/2026/11/17/lancedb-raises-57-5m-to-accelerate-ai-model-training-with-multimodal-data-platform/

45. After two months of testimony, the US criminal trial against Huawei, accused of bank fraud and trade secret theft, is set to begin jury deliberations Wednesday
   Karen Freifeld / Reuters — https://www.reuters.com/legal/litigation/huawei-says-us-put-sinister-spin-business-activities-failed-prove-charges-trial-2026-11-18/
   > @innercitypress: Huawei, Why? Last night at midnight, *after* the EDNY prosecutors' long-winded summation, Huawei's three law firms docketed a letter dated November 16 including “Huawei's preparation for trial is ongo
   > @innercitypress: OK - this morning in Huawei closing by Heberlig after “escorted out” for 6 days accusing of phone - when in overflow courtroom today, dozen use laptops, and phones. @EDNYnews Spox willfully blind, “Ca
   Also: NTD, MLex, Courthouse News Service, Matthew Russell Lee's …, ABA Journal

46. Suno launches Visuals, letting users generate 15-second clips that can be spliced into a full music video, using a MiniMax-based model; video credits cost extra
   Ashley Carman / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-17/ai-music-generator-suno-to-let-users-create-music-videos
   Also: Suno, Music Ally, The Decoder

47. California bans Waymo robotaxis from freeways after a viral video showed one failing to yield to the highway patrol; Waymo halts freeway service nationwide
   Jeremy C. Owens / San Francisco Business Times — https://www.bizjournals.com/sanfrancisco/news/2026/11/17/waymo-california-freeway-ban-dmv-chp.html?page=all
   > @kirstenkorosec: ICYMI - Waymo is off all freeways in every market it operates after the California DMV ordered the company to no longer access highways following several incidents https://techcrunch.com/...
   > @alex: i know i know i know but also have you seen human drivers i mean goddamn [embedded post]
   > @rakeshsfnyc: Waymo barred from freeways in CA. The freeway incidents have been very concerning and potentially dangerous. CHP runs speed breaks specifically for dangerous situations.
   > @verge: The state DMV labeled Waymo's highway operations an “imminent hazard to public safety” after its robotaxis drove into an active construction zone. https://www.theverge.com/...
   Also: Reuters, Wall Street Journal, KTLA, Barron's Online, Jalopnik, New York Times, Autoweek, Gizmodo, +6 more
