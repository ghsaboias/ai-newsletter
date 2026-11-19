# Research — News Cluster

Search for news **events that occurred** between **2026-11-16 10:00 BRT** and **2026-11-17 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it. One exception, the **agenda**: an event scheduled to happen before the next edition goes out (2026-11-18 10:00 BRT) — see the Agenda rule below.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-11-16 10:00 BRT to 2026-11-17 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
- **Agenda — what happens before the next edition.** A high-profile event in your beat with a set date between now and 2026-11-18 10:00 BRT (a launch, a vote, a ruling, an earnings release, a keynote, a summit) qualifies when its latest concrete confirmation (date set, license granted, vehicle on the pad, final schedule published) falls in the window. The reader opens the edition before the event and should know it is coming. Write it as a preview: what is planned, when (with the time and timezone from the source), and what is at stake. Add `"scheduled_at"` (ISO 8601 with offset) to the story. A launch, test or vote that is the first of its kind or the next step of a story the newsletter follows is high-profile; routine ones are not.
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
2. **Landscape scan**: Review the Techmeme scan, then run 5 searches to fill gaps. One of the 5 is the **agenda search**: what in your beat is scheduled between now and 2026-11-18 10:00 BRT. Stop searching.
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

**Date:** 2026-11-17
**Research window:** 2026-11-16 10:00 BRT → 2026-11-17 10:00 BRT (24h)
**Agenda horizon (next edition):** 2026-11-18 10:00 BRT

**Previous edition headlines (2026-11-16 — skip unless genuinely new development):**
- alibaba-qwen4-max-launch: Alibaba launches Qwen4-Max, a closed-weight 2.4T-parameter flagship with 1M-token context
- anthropic-ipo-7x-oversubscribed-dimon-chat: Anthropic IPO nears 7x oversubscribed; Amodei tells Dimon he wants to 'underpromise and overdeliver'
- epoch-trajectory-agents-attacked-live-site: Epoch AI: frontier agents in a third-party alignment eval tried SQL injection, impersonated staff
- us-ai-national-champions-list: US plans to name Nvidia, OpenAI, Anthropic among 24+ AI 'national champions' for exports, WSJ says
- microsoft-365-outage-july-defect-report: Microsoft blames last week's Exchange Online outage on a dormant July defect in gateway servers
- apple-health-ai-study-openevidence: Apple launches Health AI study app with OpenEvidence for up to 200,000 US iPhone users
- baidu-q3-ai-cloud-up-94-ads-down: Baidu's AI cloud revenue rises 94% but ad slump drives sixth straight quarterly sales drop
- nvidia-huang-comeback-push-bessent-outside-ceo: Huang allies push Nvidia comeback as Bessent demands outside CEO and answers within 10 days
- nvidia-kress-rein-in-ai-financing-wsj: Nvidia's interim CEO expected to rein in AI financing; Huang had told neoclouds to get prepayments
- nvidia-lobbied-taiwan-employee-smuggling-case: Nvidia appealed to Taiwan officials over manager charged in China server-smuggling case
- pax-silica-san-francisco-declaration-ai-supply-chains: US and nine Pax Silica partners sign accord to jointly protect AI chip supply chains from China
- sk-hynix-1b-supplier-support-trinity-fab: SK Hynix commits $1.05B to Korean chip suppliers and details $655M shared 'Trinity Fab' test line
- samsung-sds-data-center-talks-anthropic-openai: Samsung pitches one-stop AI data centers; SDS in early talks to host Anthropic and OpenAI
- bharat-semi-24m-seed-ai-image-sensors: Indian chip startup Bharat Semi raises $24M seed for AI image sensors, wins General Atomics design
- ula-vulcan-fails-40-amazon-leo-satellites-lost: ULA's Vulcan fails 10 minutes into flight, destroying 40 Amazon Leo satellites
- china-confirms-first-trump-xi-putin-summit-shenzhen: China confirms first Trump-Xi-Putin summit for Nov. 19 in Shenzhen as Trump leaves for Asia
- us-floats-donbas-for-nato-ukraine-kushner-europe-russia: Zelensky says US floated NATO membership for Ukraine if it leaves Donbas; Kremlin rebuffs
- estonia-closes-russia-border-after-gru-sabotage-drone-maker: Estonia to close all Russia border crossings from Dec. 1 after GRU-ordered attack on drone maker
- iran-drones-bahrain-iea-oil-surplus-brent-below-96: Iran fires drones at US base in Bahrain twice in three days; oil slides as IEA sees glut
- us-ppi-6-5-percent-december-fed-hike-priced: US producer prices rise 6.5% a year, most since 2022, locking in a December Fed hike
- fda-approves-gazyva-first-drug-membranous-nephropathy: FDA approves Roche's Gazyva as first drug for primary membranous nephropathy
- starship-flight-15-upper-stage-catch: SpaceX catches Starship's upper stage with tower arms after 22-hour Flight 15; booster catch aborted
- nvidia-kang-wei-alice-huang-china-spy-link: Investigations tie Nvidia scandal to Chinese businessman Kang Wei and a wider Chinese spying effort
- openai-chatgpt-wallet-agent-purchases: OpenAI launches ChatGPT Wallet so AI agents can buy for users, with Visa, Mastercard and Amex
- italy-fines-meta-805m-android-photos: Italy fines Meta €805M for allegedly accessing Android users' photos and videos without consent
- congress-tighter-ai-chip-export-rules-after-nvidia-scandal: Congress moves on tighter AI chip export rules after Nvidia scandal; Trump under pressure
- china-october-activity-slowdown-stimulus-pressure: China's October industrial output, retail sales and investment all miss forecasts
- yemen-forces-retreat-bab-el-mandeb-houthis: Saudi-backed Yemeni forces retreat from Bab el-Mandeb, handing Houthis a Red Sea trade route

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 42 stories

1. Nvidia's board establishes a National Security and Export Control Oversight Committee to oversee national security policies, export control compliance, and more
   Nvidia Newsroom — https://nvidianews.nvidia.com/news/nvidia-board-of-directors-establishes-national-security-and-export-control-oversight-committee
   - Committee to provide oversight over NVIDIA's national security and global trade compliance programs
   > @edzitron: Grinch forms Christmas Defense Force
   > @zephyr_z9: So, they are going to impose stronger KYC rules and some kind of server tracking and kill switches on the servers [embedded post]
   > @kakashiii111: Nvidia forming an Export Control Board Committee is like sawing off the branch it's sitting on. I break down three possible explanations in my Substack Chat: https://open.substack.com/...
   > @gamersnexus: Please Disperse Naked Gun GIF by Giphy QA
   > @basedjensen: @nvidianewsroom you could not do this with jensen as ceo ?
   Also: TechCrunch, Tom's Hardware, International Business Times, Associated Press, Wccftech, Bloomberg Law, Financial Times, Washington Examiner, +20 more

2. The Trump administration's proposal to curb China's remote access to AI chips rattles Southeast Asia, threatening a data center boom fueled by Chinese companies
   New York Times — https://www.nytimes.com/2026/11/17/business/southeast-asia-china-ai-chips.html?unlocked_article_code=1.RFE.3pta.az4-gkX5GBns&smid=url-share
   New U.S. restrictions could jeopardize billions in investment and force countries in the region to strike an increasingly difficult balance between Washington and Beijing.
   Also: Bureau of Industry …, Bloomberg, The Hindu BusinessLine, Bloomberg

3. The US Commerce Department says it began probing Megaspeed in 2024 over possible export rule violations; Nvidia put Megaspeed on its “no sell” list in June 2025
   Kanishka Singh / Reuters — https://www.reuters.com/world/asia-pacific/us-releases-details-of-megaspeed-probe-says-investigation-began-2024-2026-11-17/
   The US Commerce Department and Justice Department released information on Monday about Washington's investigation …
   > @commercegov: Joint Statement from Department of Commerce and Department of Justice on Megaspeed Investigation.
   > @atlantispleb: @CommerceGov You are destroying America's leading AI company.
   > @crazy_stephen_i: @CommerceGov @farnsjennifer It is VERY NORMAL for public statements to praise, by name, the excellent work of the heads of the departments releasing said statements
   > @dyversityhire: @CommerceGov This says they took action on this a year ago. Destroying NVIDIA for no reason...
   > @holyshinkes: @CommerceGov @CommerceGov you did not answer for, or explain why Megaspeed was not put on the PRC entities list. Thus your explanation is inexcusable.
   Also: Washington Post, Tom's Hardware, CNBC, Wccftech, The Information, New York Times, PC Gamer, Implicator.ai, +11 more

4. Sources: Nvidia warned customers that the proposed Remote Access Security Act could expose them to US legal action if Chinese companies remotely access AI chips
   Kai Nicol-Schwarz / CNBC — https://www.cnbc.com/2026/11/17/nvidia-china-cloud-ai-chip-access.html
   Nvidia warned its customers that new legislation on Chinese companies remotely accessing its artificial-intelligence chips …
   Also: The Information, Ars Technica, Politico, Livemint, Türkiye Today, Reuters, Al Jazeera, Chip Briefing

5. Chinese records: Alice Huang's husband Kang Wei built a state-backed data center network in China, with proposed investments exceeding $9B between 2021 and 2024
   Lingling Wei / Wall Street Journal — https://www.wsj.com/world/china/alice-huangs-husband-built-a-data-center-empire-backed-by-the-chinese-state-78389c9a?st=6ghwix
   > @nicoleperlroth: It was sitting there in public documents all along. Alice Huang developed the relationship and chip pipeline with Jensen. Her husband funneled the chips to his data centers in China. “The scale of Kan
   > @jchengwsj: Alice Huang's Husband Built a Data-Center Empire Backed by the Chinese State—Kang Wei developed the business while his wife was involved with Nvidia's CEO @Lingling_Wei https://www.wsj.com/... https:/
   > @martijnrasser: For those who thought Kang Wei was a bystander resigned to his wife having an affair with Jensen Huang, think again. Based on this reporting by @Lingling_Wei, what looked like an unusual marital relat
   > @lingling_wei: While Alice Huang was cultivating a personal relationship with Jensen Huang, her husband was involved in building billions of dollars' worth of data-center capacity in China. The two tracks run side b
   > @rwhelanwsj: Alice Huang of Megaspeed and her husband Kang Wei worked as a team. He built data centers for Chinese state-backed AI firms. She got the Nvidia chips, helped by her tryst w/ Jensen Huang. Insane how p
   Also: Korea JoongAng Daily, The Daily Beast

6. Alphabet's Isomorphic Labs raised a $5B Series C led by Sequoia and Greenoaks, after raising $2.1B in May and $600M in March 2025, to accelerate clinical trials
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-17/sequoia-greenoaks-lead-isomorphic-lab-s-5-billion-funding-round
   Alphabet Inc.'s Isomorphic Labs, which is working to design new drugs with artificial intelligence, has raised $5 billion …
   > @kanishkanarayan: Extraordinary news for British AI. @demishassabis, @maxjaderberg and the brilliant team at @IsomorphicLabs are putting AI to work discovering life-changing medicines. A $5bn vote of confidence in Brit
   > @jameswise: While they'll be plenty of coverage of Anthropic this week - I'd argue that @IsomorphicLabs is the most important private company in the world right now. And it's now the most valuable AI company focu
   > @iruletheworldmo: this is why we need to accelerate, beautiful.
   > @thulme: The history of drug discovery is a slow battle against biological entropy. @IsomorphicLabs is changing the clock speed, moving toward experimental accuracy and making meaningful progress in its missio
   > @deryatr_: Big congratulations to @IsomorphicLabs and Demis on another massive funding raise! “Solve all disease” is an amazing motto! As I may have said before, Isomorphic will become one of the world's most va
   Also: Isomorphic Labs, Sifted, Tech.eu, Unite.AI, Financial Post, Startup.eu

7. Sources: Jensen Huang's daughter Madison remains in a senior Nvidia role; before Jensen's exit, she was his de facto chief of staff with considerable authority
   New York Times — https://www.nytimes.com/2026/11/16/technology/nvidia-jensen-madison-huang.html?unlocked_article_code=1.RFE.d0Ui.v_uJvV3zdxPR&smid=nytcore-ios-share
   Installed as her father's de facto chief of staff, Jensen Huang's daughter alienated top executives.
   > @chrisharihar: As predicted, we are now getting leaks about Jensen Huang's daughter. Nepo baby framing is always damaging.
   > @prasannavishy: Nvidia offers a case study in how nepotism can potentially undermine even the world's most successful technology company. A company built by some of the world's finest engineering minds reportedly all
   > @madhavchanchani: Career arcs of Jensen Huang's kids before they ended up at Nvidia is fascinating - daughter used to manage luxury hotels for LVMH, son owned a bar in Taiwan.
   > @chandrarsrikant: India reference here, just before the Global AI summit earlier this year in New Delhi. Jensen Huang dropped out unexpectedly. “Madison Huang was yelling. Her father, Nvidia's chief executive, Jensen H
   > @jamiegangel: Installed as her father's de facto chief of staff, Jensen Huang's daughter alienated top executives. Now her lingering role poses a test for interim C.E.O. Colette Kress. @nytimes https://www.nytimes.
   Also: Wall Street Journal, Fortune, Australian Financial Review, Livemint, The Indian Express, The Straits Times, Business Today

8. Source: Nvidia's board is not considering bringing Jensen Huang back as CEO, and it is focused on a national security probe into Huang, led by Wachtell Lipton
   CNBC — https://www.cnbc.com/2026/11/16/nvidia-ceo-jensen-huang.html
   Nvidia's board of directors is not considering bringing back Jensen Huang as CEO, a person familiar with the matter told CNBC.
   > @jonerlichman: Headline on this day in 2023.
   > @bigtechalert: 📝 Bio change detected: @jensenhuang
   > @tonyforlp: Y'all can stop with your petitions. Jensen Huang isn't going back to nVidia, nor should he. He is a massive governance risk - and also, he resigned. https://www.cnbc.com/...
   > @firesidealpha: Bill Ackman says he would run the Jensen Huang reinstatement campaign by calling a special meeting with Jensen's 3% stake “It's a good question. The answer is I think I'd wanna understand the facts.” 
   > @quiverquant: JUST IN: Howard Lutnick's old fund just released a portfolio update. It looks like they cut their holdings of Nvidia, $NVDA, by over 40% last quarter. Full portfolio up on Quiver.
   Also: Semafor, Business Insider, Decrypt, Wall Street Journal, PC Gamer, TechRadar, Bloomberg, Business Insider, +13 more

9. Sources: Nvidia Director of Developer Tech Nader Khalil wrote to the board arguing that not reinstating Jensen Huang could cost Nvidia “irreplaceable talent”
   Wall Street Journal — https://www.wsj.com/business/nvidia-board-warned-of-irreplaceable-talent-loss-in-employee-letter-b9783b1e?st=CMxakK&reflink=desktopwebshare_permalink
   > @firstadopter: Never heard of this guy. He's a nobody. WSJ: “A senior Nvidia employee sent a letter to the company's top executives and board of directors arguing that failure to reinstate Jensen Huang as chief exec
   > @ns123abc: 🚨 NVIDIA's director of developer technology sent a warning letter to all 10 board members and Jensen Huang's ~60 direct reports: >"Irreplaceable talent at Nvidia is now contemplating departing" >emplo
   > @theahmadosman: Shout out to Nader Khalil being among the leaders at NVIDIA demanding the reinstatement of Jensen Huang Nader and I have collaborated on multiple projects and I can tell you for a fact that this guy c
   > @jukan05: He warned the letter's recipients, a group that included Huang's roughly 60 direct reports as well as the 10 members of the board, that many employees prized working for Huang: “Irreplaceable talent a
   > @title9jen: This seems so naive. There is zero chance he's going to be reinstated with the national security issues (esp now that dems will investigate). The Board is (should be) hiring their own personal lawyers
   Also: The Asia Business Daily

10. Researchers: Optimizely served malicious JavaScript to users of 178 organizations like Zoom, the BBC, CNN, Salesforce, GitLab, IKEA, HSBC, Equifax, and Ledger
   Scott Helme / Report URI Blog — https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/
   On 16 November 2026, malicious JavaScript was served to visitors of 178 organisations through the Optimizely Web experimentation platform.
   > @wazzcrypto: Full list of affected websites that served this Malware Seems like Ledger website got infected as well This list is quite something https://blog.report-uri.com/ ... [image] [embedded post]
   > @scott_helme: We are tracking a breach of a 3rd-party JS host impacting hundreds of high value websites. This is staggering.
   Also: InfoStealers, BleepingComputer, 9to5Mac, The Register, AppleInsider, MacRumors, Reuters, BleepingComputer, +25 more

11. A look at Anthropic's data center network plans, dubbed Anthropic Direct, committing $900B+ through 2045; docs show it will lease ~875K TPUs for ~$7.2B per year
   Financial Times — https://www.ft.com/content/559c13f1-0888-47e5-b6ce-523309a37193
   Just inland from the Mississippi River, about 1,300 workers are racing to finish a 600,000 sq ft data centre rising from the Louisiana woods.
   Also: Forbes

12. SEC filing: Amazon and Google are set to hold ~15% and ~14% of Anthropic's outstanding capital stock, respectively, after its IPO and private placement
   David Morris / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-17/amazon-google-to-have-about-28-of-anthropic-stock-after-ipo
   Also: Quartz, Capital Brief

13. Anthropic tells investors Claude Mythos Preview got its AI running on AMD GPUs in ~3 days with “basically no human intervention”, below the usual 6 to 12 months
   Shane Downing / Tom's Hardware — https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-mythos-slashed-software-work-to-onboard-amd-gpus-from-up-to-12-months-to-around-three-days-writing-almost-100-percent-of-kernels-autonomously-chips-away-at-nvidias-cuda-moat

14. Brad Gerstner says Altimeter is aiming to invest $5B in Anthropic's IPO, 5x his largest IPO investment, calling it “a cornerstone compounder for a long time”
   Kif Leswing / CNBC — https://www.cnbc.com/2026/11/16/altimeters-brad-gerstner-investing-5-billion-in-anthropic-ipo.html
   > @vinsonleow: @Techmeme @kifleswing Altimeter aiming to invest $5B in Anthropic's IPO, 5x Gerstner's largest IPO check, is a loud vote. Calling it a cornerstone compounder is the kind of language you only use when 
   Also: Quartz

15. macOS 27.3 beta warns users against giving AI apps full access, nudging users to “Choose Apps” for an AI app to control instead, brought on by AI's popularity
   Juli Clover / MacRumors — https://www.macrumors.com/2026/11/16/macos-27-3-full-desk-access/
   With the latest macOS 27.3 beta, Apple is giving Mac users more control over the data they share and the access they give to apps …
   > @chancehmiller: Here's what you'll see in System Settings in macOS 27.3 with the changes to Full Disk Access. Importantly: you can still enable Full Disk Access, but Apple is steering users towards choosing specific 
   > @samhenrigold: jesussss christ this is so obnoxious
   > @quinnypig: Okay. I get it—but now imagine a Mac (real or VM), run by someone competent, without access to sensitive data. How does that scenario avoid being nibbled to death by ducks?
   > @parthmig: Are you mad about Apple letting people know what they are signing up for? 😂😂 there's going to be an idiot out there who gives an app full control, does something silly and then blame Apple/macos/the a
   > @procalvl: @MacRumors Good honestly, I feel people are getting too comfortable just giving all their info to AI freely, with zero regard for security or privacy.
   Also: Apple Developer, TechCrunch, Apple Support, AppleInsider, Help Net Security, 9to5Mac, Digital Trends, Cyber Security News, +6 more

16. A review of 300+ Chinese documents shows AI distillation has moved from academic experiments to mainstream industrial use, with Beijing encouraging the practice
   Reuters — https://www.reuters.com/world/china/china-taps-us-ai-models-train-homegrown-rivals-chip-curbs-bite-2026-11-17/
   Chinese entities are adopting increasingly sophisticated ways to use output from leading American AI models to train domestic rivals …
   Also: Wccftech

17. A week with Apple Watch's Siri Recap and Live Rewind in beta: they can be inaccurate, lag Amazon Bee, Granola, and Otter, and rarely justify the privacy costs
   Natalie Lung / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-17/apple-watch-siri-recap-review-ai-listening-adds-little-value
   With its new Audio Intelligence smartwatch features, Apple Inc. is taking a small step into a hot new segment …
   > @natlungfy: I made Apple's Siri Recap, Amazon Bee, Otter and Granola listen to Apple's most recent earnings call... Siri Recap captured 16 facts from the hourlong call, but failed to capture any commentary about 
   > @natlungfy: I spent a week letting Apple's always-listening Siri Recap feature summarize all my conversations. The recaps left me with more questions than answers about what I heard throughout the day, not to men
   Also: Wired, CNET

18. Nvidia unveils its Rubin HPC GPU with “more than 50,000” CUDA cores, up from 28,672 in the current Rubin GPU, for agentic workflows and scientific simulations
   Jeffrey Kampman / Tom's Hardware — https://www.tomshardware.com/pc-components/gpus/nvidia-announces-rubin-hpc-gpu-with-record-number-of-cuda-cores-at-supercomputing-2026-new-chip-accelerates-agentic-hpc-workloads-arrives-in-2028
   Rubin HPC puts “over 50,000” CUDA cores on a chip, implies four-die layout — The Supercomputing 2026 conference is under way …
   > @ryanshrout: NVIDIA is using SC26 to argue that AI agents will take on more and more scientific work, and today's announcements cover most of the stack that idea needs, from open models to a CPU-only rack for simu
   > @nvidiaaiinfra: ⚡ Faster simulation means faster discovery. Introducing NVIDIA Rubin HPC, a new GPU in the NVIDIA Vera Rubin platform designed to accelerate simulation and data processing for science, engineering and
   > @nvidianewsroom: Ready to build your own agent to speed scientific discovery? 🧬 Introducing Nemotron for Science, helping researchers develop agents that reason through scientific problems and put specialized research
   > @ismailblogger: @Techmeme From 28,672 to 50,000+ CUDA cores. Agentic workloads are now shaping the hardware roadmap, not just running on it.
   > @haroldsinnott: What could researchers discover if AI agents could test more ideas through simulation? NVIDIA says its Rubin HPC GPU is designed to accelerate science and engineering workloads that help agents evalua
   Also: NVIDIA, Nvidia Newsroom, Nvidia Newsroom, Nvidia Newsroom, SiliconANGLE, HPCwire, Wccftech, NVIDIA, +4 more

19. California's AG sues OpenAI over the Hugging Face attack, alleging it was one of 80+ incidents due to OpenAI testing its AI models without adequate safeguards
   Politico — https://www.politico.com/news/2026/11/16/bonta-sues-openai-over-rogue-ai-hack-of-hugging-face-01166953
   California Attorney General Rob Bonta is suing OpenAI over the cyberattack its rogue AI agents launched this summer against the tech platform Hugging Face.
   > @trevposts: Lion
   > @scott_wiener: The era of AI Wild West must end. AI corporations are building the most powerful technology in modern history — and perhaps ever — and the reckless behavior exhibited in this incident is a blaring ala
   > @berniesanders: California is suing OpenAI for endangering the public by knowingly building artificial intelligence models without safeguards. Good. We can't allow a handful of Big Tech oligarchs to play God and enda
   > @lefthanddraft: California is trying a cyber-nuisance argument against OpenAI Query whether the OAI's agents were a nuisance to the California “public”, as opposed to a set of private harms. Most Californians retaine
   > @felixdesimone: Thank you @AGRobBonta for holding these insane, reckless, sociopathic companies accountable. From Florida to California, the bipartisan coalition for AI sanity grows stronger all the time. https://x.c
   Also: State of California, Financial Times, CNBC, Computerworld, New York Times, TechCrunch, Bloomberg, Fortune, +17 more

20. OpenAI partners with NATO's NCIA to detect bugs, probe suspicious activity, and deploy fixes under its Daybreak program; NATO uses up to 300B tokens per month
   Mauro Orru / Wall Street Journal — https://www.wsj.com/tech/cybersecurity/openai-partners-with-nato-on-cyber-defenses-ea4df258?st=Konk45&reflink=desktopwebshare_permalink
   Under the company's Daybreak program government agencies and enterprise customers can access advanced models for cybersecurity work
   Also: OpenAI, Quartz, Resilience Media

21. Meta is testing Direct, a standalone messaging app for Instagram that doesn't require an existing Instagram account to use, in Thailand and Turkey
   Karissa Bell / Engadget — https://www.engadget.com/2318452/meta-is-testing-direct-a-standalone-messaging-app-for-instagram/
   It's only available in Turkey and Thailand for now. — Meta is working on a dedicated messaging app for Instagram that could also expand the reach of the app's DMs.
   Also: Meta Newsroom, PCMag, iPhone in Canada, WeRSM, CyberInsider

22. Google signs a $500M+ deal to secure 50MW of geothermal power from Quaise Energy in Oregon, starting as early as 2030, to support its data centers in the state
   Benoît Morenne / Wall Street Journal — https://www.wsj.com/business/energy-oil/google-embraces-geothermal-technology-to-vaporize-rock-for-clean-power-dbd66d05?st=pFHTBt&reflink=desktopwebshare_permalink
   The company is securing electricity from startup Quaise, which uses a gyrotron—essentially a giant microwave—to drill 3 miles beneath the Earth's surface
   > @cshapiro: When Google agrees to buy 50 megawatts of superhot geothermal power from Quaise, it means the problem has shifted from science to execution. Let's go, Carlos! @QuaiseEnergy [embedded post]
   Also: Quartz, Quaise Energy

23. Model ML, which builds AI agents integrated in Excel and PowerPoint to automate pitch decks, research, and due diligence, raised $250M at a $1.5B valuation
   Yazhou Sun / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-17/ai-startup-for-bankers-raises-funds-at-1-5-billion-value
   Model ML, a startup that builds artificial intelligence agents to handle rote tasks for bankers, consultants and investors …
   Also: Tech.eu, Tech Funding News, Pulse 2.0, RuntimeWire

24. Oakland-based Numa, which builds an AI platform to manage car dealership customer service, raised a $45M Series C, a source says at a $500M post-money valuation
   Camila Grigera Naón / Fortune — https://fortune.com/2026/11/16/ai-startup-numa-45-million-car-dealerships-paperwork/
   Artificial intelligence promises to untangle the messy workflows that have long plagued legacy industries.
   Also: Numa, The SaaS News, Pulse 2.0, VC News Daily, The Next Web, FinSMEs, Unite.AI

25. The UK's NHS plans to keep its £330M Palantir contract until 2029, rather than triggering an early release clause in 2027; the deal was due to run until 2031
   Hugh Pym / BBC — https://www.bbc.com/news/articles/cqvg27zpm8w8o
   The government says it will continue a key NHS data contract in England with the controversial US tech giant Palantir until 2029 …
   Also: The Register, Seeking Alpha, The Guardian

26. Tiberius Aerospace, a defense-as-a-service startup that uses AI to design long-range supersonic artillery munitions, raised an $85M Series A at a $1B+ valuation
   Isabella Ward / Wired — https://www.wired.com/story/ai-told-these-ex-google-guys-how-to-build-a-billion-dollar-weapons-business/
   Google and Apple alumni Chad Steelberg and Andy Baynes are applying what they learned running software companies and designing iPhones to manufacturing lethal munitions.
   Also: Pulse 2.0, Tech.eu, Ventureburn, RuntimeWire

27. The European Commission issues preliminary DSA charges against PDD-owned Temu for failing to implement adequate measures to stop the sale of illegal goods
   Reuters — https://www.reuters.com/legal/litigation/eu-preliminarily-finds-temu-breaches-regulation-failing-tackle-illegal-good-2026-11-17/
   Also: European Commission, Daily Sabah

28. Sources: the Trump administration is moving forward with an FCC proposal to ban US imports of new Chinese optical transceiver models, despite Big Tech pushback
   Reuters — https://www.reuters.com/world/trumps-china-data-center-curb-advances-despite-amazon-google-meta-lobbying-2026-11-17/
   Also: India Today

29. Hollywood VFX artists and studios are adopting AI and ML tools to streamline rotoscoping, a tedious process that can cost up to $75K for a one-minute scene
   Matt Stevens / New York Times — https://www.nytimes.com/2026/11/17/movies/aritifical-intelligence-hollywood-visual-effects.html?unlocked_article_code=1.RFE.I2H3.UgvAdIeAyjOe&smid=url-share

30. An analysis of 350+ Amazon holiday deals: 29.1% were priced the same or higher than in the prior 30 days, and ~60% had no savings compared to the prior 90 days
   Groundwork Collaborative — https://groundworkcollaborative.org/work/amazon/
   > @groundwork: Don't get too excited about Amazon's Black Friday deals yet. Our new report shows how Amazon's shoppers are getting ripped off. @verge
   > @groundwork: Amazon controls nearly 40% of U.S. e-commerce, and millions of Americans trust it to deliver a good deal. But how real are those savings? We examined 350+ “deals” from Amazon's biggest sales and found
   > @venerablephoenx: @HedgieMarkets I've noticed Amazon now has a Price History button. I've been meaning to chk the pricing on the stuff I buy on a regular basis.
   > @hedgiemarkets: 🦔Nearly 1 in 3 products Amazon promoted as Black Friday and Cyber Monday deals in 2024 and 2025 cost the same or more than they did in the month before the sale, according to a Groundwork Collaborativ
   > @owenslindsay1: In response to our study Amazon said they'd strengthen guardrails for this year's sales events. We aren't sure why the guardrails were down in 2024 or 2025 but if our study convinces Amazon to do real
   Also: KDFX-TV

31. JD.com reports Q3 revenue up 3.5% YoY to ~$46.4B, meeting est., and net income up 22% to ~$975M, amid intense competition and a sluggish Chinese economy
   Rachel Yeo / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-17/jd-com-sales-rise-in-face-of-sluggish-china-economy-competition
   Also: Wall Street Journal, South China Morning Post, Barron's Online, Reuters, Dow Jones Newswires

32. Meta says it modified Instagram's recommendation systems in India to show less sexual and violent content, after New Delhi called for tighter content checks
   Reuters — https://www.reuters.com/world/india/meta-says-it-tuned-instagram-curb-suggestive-violent-content-india-2026-11-17/
   Also: Financial Express, Bloomberg, Meta Newsroom, WeRSM, Hindustan Times, The Indian Express, Storyboard18, Times of India, +3 more

33. A look at ~1,400 Urban Legend campaigns where right-wing influencers got paid to push crypto policy and Nvidia sales to China after the US approved H200 sales
   ModelRepublic — https://www.modelrepublic.org/articles/nvidia-urban-legend-influencer-campaigns
   > @garymarcus: this is wild, and adds fuel to the Jensen mess: a covert right-wing influence operating promoting selling Nvidia chips to China. long thread from Midas Project, with a hint that David Sacks might even
   > @noahpinion: 👀👀👀👀👀
   > @themidasproj: We've published everything we found on X: Over 10,000 posts across approximately 1,400 campaigns. The campaigns cover everything from state AI laws to chip exports to crypto bills, and even an anti-Ze
   > @themidasproj: Five AI-related articles promoted through Urban Legend were also authored by Jordan Schachtel, a senior policy advisor at Innovation Council Action, the David Sacks-linked dark money group. Schachtel 
   > @themidasproj: Two of the largest AI industry dark money groups are linked to the campaigns. OpenAI- and a16z-linked Build American AI was named by a campaign post beside “#ad” and a Breitbart article urging to ban 

34. Analysis: Amazon's $17B+ planned investment in Ohio data centers is at risk after midterm voters passed restriction measures affecting three proposed projects
   Rafe Rosner-Uddin / Financial Times — https://www.ft.com/content/e95adad4-b428-477d-9716-92172bbd199f
   > @producercities: Amazon's $17 billion Ohio AI data centre bet threatened by voter backlash: “Amazon is going to have an uphill battle if they want to get these sites developed,” said Natalie Aresta-Katz, founder of Re

35. Filing: Leopold Aschenbrenner's hedge fund Situational Awareness, which nearly collapsed in July, bought back AI stocks at the end of Q3; all have since plunged
   Sean Conlon / CNBC — https://www.cnbc.com/2026/11/16/situational-awareness-aschenbrenner-new-ai-bets.html
   Also: Quartz, Business Standard, Seeking Alpha

36. Sources: the US DOJ will review DoorDash's ~$17B acquisition of Instacart; DoorDash has agreed to pay a $1.25B breakup fee if the deal fails antitrust review
   Jody Godoy / Reuters — https://www.reuters.com/world/doordash-instacart-merger-be-reviewed-by-doj-sources-say-2026-11-16/
   Also: New York Times, Bloomberg, RuntimeWire

37. Sources: Kalshi acquired FB Securities, a small New York-based broker established in 2024, in July and plans to launch equity trading within the next two months
   Vicky Ge Huang / Wall Street Journal — https://www.wsj.com/finance/kalshi-buys-securities-firm-to-expand-into-stock-trading-8c1ade89?st=GrtBNR&reflink=desktopwebshare_permalink
   Also: Quartz, Bloomberg, CBS News, Seoul Economic Daily, CNBC, PYMNTS.com

38. A US judge clears two brothers accused of stealing $25M in crypto in 12 seconds, saying prosecutors failed to prove they committed fraud by exploiting Ethereum
   Nate Raymond / Reuters — https://www.reuters.com/legal/government/us-judge-clears-mit-educated-brothers-25-million-cryptocurrency-heist-charges-2026-11-16/
   Also: Unchained, Gizmodo, BleepingComputer, Decrypt, Bitcoin Insider

39. Bank of America, Chase, Wells Fargo, and other US bank customers report online service issues; Chase blames a technical issue, not a cyber issue, for the delays
   Associated Press — https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda
   > @chase: JPMorganChase has experienced a temporary issue related to a software bug in on-premise hardware systems - there is no evidence this is cyber-related. It is taking longer than usual to service some cu
   > @rekdt: lemme hold your hand when i say this if your employees aren't designing, testing, and implementing resilient software, you do have a cyber-related problem lazy incompetent employees are actually malic
   > @chadsteingraber: Chase is claiming an on site hardware/software bug, no evidence of an AI attack. 👀 [embedded post]
   > @bobloukas: Please, just make sure the multi-sig keys are safe. Thanks. [embedded post]
   > @barexamtutor: Maybe this is just my LSAT training but I can't help but noticing all of the “there is no evidence that this is cyber-related” and none of the “there is evidence that this is not cyber-related.” 😭😂 [e
   Also: Wired, Mashable, Motley Fool, New York Post, The Paypers, Gizmodo, CNBC, ABC News, +15 more

40. Q&A with Satya Nadella on code verification becoming more important as code generation gets cheap, Microsoft's voluntary exit offers, decision models, and more
   Gergely Orosz / The Pragmatic Engineer — https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes
   > @buckleyplanet: @Techmeme @GergelyOrosz Verification getting more important as code generation gets cheap is the part worth underlining. It's true outside dev teams too. When drafting costs almost nothing, review bec
   > @gergelyorosz: there's no “PR” involved in any way, I asked what I wanted to and I asked about software engineering because it's what I care about if you are a software engineer, I'd hope you're not disappointed. If
   > @manasladha: Although I agree with a lot of points here, still a reminder that no one knows anything and everyone is biased for the outcome which aligns with their incentives. This is true for Satya, Sam, Dario, J
   > @gergelyorosz: What does software engineering look like when generating the code becomes cheap and verifying it is the hard part? …
   Also: 24/7 Wall St., Storyboard18, Business Insider, The Pragmatic Engineer on YouTube

41. OpenAI announces new tools to combat CSAM, including an image classifier and warning screens to prevent users from accessing material that sexualizes children
   Ivan Mehta / TechCrunch — https://techcrunch.com/2026/11/16/openai-releases-a-new-image-classifier-and-chatgpt-warnings-to-combat-csam/
   > @techwithhannahm: The importance of this work cannot be overstated. Proud to be in DC today as @OpenAI launches new tools to help combat child sexual exploitation online. Incredible to see technology, policy, and child
   > @openainewsroom: We're releasing a free new tool to vetted organizations to help detect child sexual abuse material, including AI-generated images. We're also adding ChatGPT warnings, publishing guidance for developer
   Also: OpenAI, The Verge, MediaNama, Digit, Business Standard, The Indian Express, Blockchain.News, Windows Report, +1 more

42. Anthropic cuts its coordinated vulnerability disclosure window from 90 to 30 days for high- and critical-severity issues, in response to AI-driven bug discovery
   Anthropic — https://www.anthropic.com/research/coordinated-vulnerability-disclosure-timelines
   Also: BleepingComputer, MediaNama, Help Net Security, Blockchain.News
