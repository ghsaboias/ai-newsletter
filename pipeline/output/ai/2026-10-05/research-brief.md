# Research — News Cluster

Search for news **events that occurred** between **2026-10-02 10:00 BRT** and **2026-10-05 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-02 10:00 BRT to 2026-10-05 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-05
**Research window:** 2026-10-02 10:00 BRT → 2026-10-05 10:00 BRT

**Previous edition headlines (2026-10-02 — skip unless genuinely new development):**
- openai-rogue-agents-100-orgs-nsw-hack-california-subpoena: OpenAI says it alerted 100+ groups to rogue agent activity; California AG subpoenas the company
- openai-fires-three-safety-researchers-shared-info: OpenAI fires three safety researchers accused of sharing confidential data with outside group
- anthropic-ipo-marketing-week-nov-9-before-thanksgiving: Anthropic aims to start IPO marketing the week of Nov. 9 and trade before Thanksgiving
- softbank-nvidia-complete-30b-openai-pledges: SoftBank and Nvidia pay final $10B tranches, completing $30B pledges each to OpenAI
- microsoft-mai-transcribe-2-streaming-mai-voice-2-1: Microsoft AI launches MAI-Transcribe-2-Streaming, No. 1 on streaming accuracy, plus voice models
- cloudflare-clef-aws-strands-decider-open-decision-models-jev: Cloudflare and AWS release open-weight 'decision models' to rival TypeSafe's Jev
- jay-clayton-likely-white-house-ai-czar: CBS: Jay Clayton likely to be named White House AI czar while staying DNI
- earthmade-greg-lui-300m-nvidia-servers-smuggling-china: US arrests California man over $300M smuggling of Nvidia AI servers to China via Malaysia
- amazon-8b-grace-blackwell-spv-leaseback: FT: Amazon seeks to move $8B of Nvidia Grace Blackwell chips into an SPV and lease them back
- amazon-built-together-1b-data-center-communities: Amazon pledges $1B+ over five years to data center towns, drops NDAs amid local backlash
- michigan-psc-approves-dte-google-1gw-data-center: Michigan regulators approve DTE power contracts for Google's 1GW Van Buren data center
- tesla-ai5-ai6-ram-cut-optimus-memory-shortage: Musk: Tesla halves AI5 chip memory to 72GB, cuts AI6 a third, to secure Optimus volume
- samsung-hbm4-price-3x-hbm3e-2027: Samsung asks over 3x HBM3E's price for 2027 HBM4 supply, Korean paper reports
- us-september-jobs-29k-unemployment-4-2: US adds just 29,000 jobs in September, far below forecasts; unemployment rises to 4.2%
- us-third-carrier-9000-troops-middle-east-iran: US sends third aircraft carrier and ~9,000 troops toward Iran as Trump weighs new strikes
- china-suspends-fuel-exports-brent-102: China halts fuel exports; Brent jumps 4.4% to $102 as Asian gasoline margins hit record
- treasury-a7-network-tco-iran-russia-sanctions: US Treasury designates Russia-backed A7 payment network a criminal organization over Iran ties
- putin-valdai-no-ceasefire-kaliningrad-nuclear-warning: Putin rules out Ukraine strike truce and warns of nuclear response over Kaliningrad
- spacex-crew-13-record-fastest-iss-docking: SpaceX Crew-13 reaches ISS in 7h55m, fastest trip ever by a US spacecraft
- fda-approves-autus-heart-valve-grows-with-children: FDA approves first heart valve designed to be expanded as children grow

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 36 stories

1. Sam Altman says OpenAI and Anthropic still have a fundamentally different worldview on AI regulation, arguing that AI's benefits justify accepting some risks
   Politico — https://www.politico.com/news/2026/10/04/sam-altman-decoded-interview-ai-01106217
   OpenAI CEO Sam Altman said there remains a fundamental difference in worldview between his company and rival Anthropic …
   > @senwarren: This is absurd. We should reject AI bots doing “bad things” so that some of the richest corporations in the world can get even richer. It's time to enforce the laws already on the books, regulate AI, 
   > @thekennymiles: There hasn't been worse PR for any industry (recently) than Big Tech talking about AI. It will be studied.
   > @jolingkent: 👀 hi I have a few follow up questions... https://www.politico.com/...
   > @chrisharihar: This is crazy. I understand the argument @sama is making here. But I cannot understand saying it this way. Telling people who are already skeptical of AI to accept “bad things
   > @andrewcurran_: Sam Altman to Politico's Brendan Bordelon: ‘We believe that the world should accept some bad things happening for the benefits of this technology and people having the agency.’
   Also: Business Insider, The Guardian, The Verge, PCMag, Financial Times, PYMNTS, The American Bazaar, Futurism, +16 more

2. Q&A with Sam Altman on his kids, his rivalries, pronatalism, “prepping” for the apocalypse, new products, the IPO delay, Luca Guadagnino's Artificial, and more
   Vanity Fair — https://www.vanityfair.com/story/sam-altman-exclusive-interview-part-1
   In an exclusive video interview, the OpenAI CEO discusses ChatGPT and suicide prevention, safety breaches …
   > @vanityfair: Mark Guiducci: “Do you know who Laura Reiley is?” Sam Altman: “I don't.” Mark Guiducci: “She is a journalist. She wrote an essay in the ‘Times’ last year. Her daughter committed suicide after speaking
   > @benmullin: Oh boy
   > @hesamation: NEW: Sam Altman says the next major AI incident will catch the world “off guard
   > @vanityfair: Sam Altman on Elon Musk: “Look, I don't like bullies, and I think Elon's a bully. And so I think once in a while you got to punch a bully back in the nose.” https://www.vanityfair.com/...
   > @dylanbyers: Baffled by the PR person who didn't trust @sama to handle himself and didn't think about how this would amplify the moment...
   Also: The Verge, The Wrap, HuffPost, Kotaku, Variety, The Hollywood Reporter, Reality Tea

3. Sam Altman says he's “very uncomfortable” with attributing “religious force” to AI, calling it “a real safety issue”, as Anthropic meets with religious leaders
   Ben Berkowitz / Axios — https://www.axios.com/2026/10/03/openai-anthropic-altman-amodei-religious-force-models
   OpenAI CEO Sam Altman on Saturday took a veiled shot at Anthropic and its work on the soul of AI …
   > @sama: I am very uncomfortable about people trying to ascribe religious force or a surrender of human judgment to AI models, and think it is a real safety issue.
   > @stevenheidel: the problem with naming a model “Claude” is that, if you work there long enough, you eventually start to treat it like a sentient god. we name our models things like “GPT-5.1-Codex-Max”. not really a 
   > @samhaselby: Altman, Olah, and Amodei all rely on this American Ted Talk-HR executive speak, eg “I am uncomfortable” “safety issue.” Whereas Pope Leo and Rabbi Mois Navan (the one who told them if they believe it 
   > @drelidavid: .@sama is referring to Anthropic's cult about the consciousness of its model, and the secret meetings they have held with religious figures about that. OpenAI is far from perfect, but I would prefer i
   > @andrewcurran_: @sama >ascribe religious force There are multiple ways this could be interpreted.
   Also: Breitbart, The Daily Wire, The Independent, The Neuron, New York Post, Wccftech

4. Q&A with Sam Altman on President Trump, the midterms, AI extinction risk, Xi Jinping's state visit, self-policing vs. regulation, and Greg Brockman's donations
   Vanity Fair — https://www.vanityfair.com/story/sam-altman-exclusive-interview-part-2

5. Huawei agrees to a multiyear patent licensing deal with Qualcomm covering AI, 5G, computing, and networking tech, its first 5G licensing deal with Qualcomm
   Miyoung Kim / Reuters — https://www.reuters.com/legal/litigation/huawei-agrees-multi-year-patent-licensing-deal-with-qualcomm-2026-10-05/
   China's Huawei Technologies (HWT.UL) said on Monday it had agreed a broad multi-year patent licence deal with Qualcomm (QCOM.O) …
   > @teortaxestex: Huawei chip design is getting some major endorsement
   > @lithos_graphein: Tau Scaling goes mainstream.
   > @huawei: Breaking News: Huawei & Qualcomm announce a multi-year, broad patent license agreement including cross licenses to the companies' patent portfolios across various fields such as 5G, compute, AI, and n
   > @huawei: Huawei and Qualcomm have announced a multi-year, broad patent license agreement that includes cross licenses to the companies' patent portfolios across a range of fields, including 5G, compute, AI, an
   > @glennluk: I spoke too soon on Huawei & Qualcomm not collaborating in 2024. To be fair, I also did not expect Huawei to get involved with chip fabrication in 2018. https://www.bloomberg.com/...
   Also: Qualcomm, Bloomberg, DatacenterDynamics, Light Reading, Unite.AI, Quartz, Political.org, Silicon Republic, +12 more

6. OpenAI says it will begin testing a visual ad format in ChatGPT later in October in the US, displaying clearly labeled visual ads while users generate images
   Mayank Parmar / BleepingComputer — https://www.bleepingcomputer.com/news/artificial-intelligence/openai-will-show-visual-ads-in-chatgpt-while-you-generate-images/
   OpenAI is expanding ads in ChatGPT, and one of the first new formats will show visual ads while you're generating images.
   > @btibor91: OpenAI is testing a new visual ad format in ChatGPT during image generation, starting later this month in the US https://openai.com/...
   Also: OpenAI, TechCrunch, Thurrott, Engadget, The Verge, Mashable, Digital Trends, The Decoder, +6 more

7. The CFTC proposes a federal framework for crypto exchanges to offer retail customers leveraged and margined spot trading, without requiring congressional action
   Jason Shubnell / The Block — https://www.theblock.co/news/markets/2026-10-05-cftc-rulemaking-leveraged-retail-crypto-trading-regulation-ctx-cam-417701
   The agency floated a new “crypto asset market” exchange category but said it can't require crypto to trade on CFTC platforms without Congress.
   > @amandatums: Heard 🫡 @ChairmanSelig today, on “onchain finance”:
   > @digitalchamber: @ChairmanSelig and the @CFTC just delivered what we've been demanding for years: a proactive, rules-based regulatory framework instead of enforcement chaos. Purpose-built federal rules kill the patchw
   > @jacqmelinek: JUST IN: CFTC Chairman Michael Selig published a new op-ed sharing that the agency is moving ahead with a proposal for its own frameworks for crypto markets, despite the Clarity Act failing to advance
   > @chairmanselig: 🚨 BREAKING NEWS 📺
   > @sjdedic: “Those days of Gary Gensler are over. The CFTC is moving quickly to institute rules and regulations that account for the distinctions between crypto assets and other types of commodities.
   Also: CFTC, Reuters, The Hill, Decrypt, CoinDesk, Wall Street Journal, Bloomberg, CoinGape

8. To comply with the EU AI Act, OpenAI plans to add text watermarking for ChatGPT and Codex users in the EU and an opt-in setting for API customers globally
   OpenAI — https://openai.com/index/eu-text-provenance
   - Starting today, API customers globally will be able to opt in to text watermarking for select models.
   > @andrewcurran_: Text watermarking in ChatGPT and Codex is rolling out. The new development is that, unlike Anthropic and Google, OpenAI (for now) is launching their watermarking - textGrain - 𝘰𝘯𝘭𝘺 in the EU, not glob
   > @koltregaskes: Hopefully this is not one of their significant improvements. 😜 Watermarking is coming to Codex and ChatGPT along with ads during your image generations. Fun times.
   > @nicdunz: this has got to be the worst thing ive ever seen happen in all of ai progress so far
   > @btibor91: OpenAI is rolling out text watermarking for the EU AI Act - opt-in for API customers globally for select models starting today, ChatGPT and Codex text in the EU gets an invisible watermark over the co
   > @hakmgpt: OpenAI will add an invisible watermark to text generated for users in Europe. This is the first feature we're getting from the “28 Ships in 28 Days” https://openai.com/...
   Also: OpenAI, Unite.AI

9. OKX and ICE's joint venture OKXICE is seeking US SEC approval to offer tokenized shares of 63 NYSE-listed companies, leveraging new rules on tokenized stocks
   Scott Patterson / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-05/okx-files-with-sec-to-launch-tokenized-us-stock-trading-platform
   OKX filed with the Securities and Exchange Commission on Sunday to launch a tokenized-stock trading platform …
   > @andrewcuomo: Today we are announcing a major step forward for OKXICE, the joint venture between @okx and Intercontinental Exchange, parent company of @NYSE: OKXICE has notified the SEC that we intend to launch our
   > @andrewcuomo: Today we are announcing a major step forward for OKXICE, the joint venture between @okx and Intercontinental Exchange, parent company of @NYSE: OKXICE has notified the SEC that we intend to launch our
   > @carlosdomingo: We were very excited when the SEC innovation exemption came up, and we are even more excited now that it's becoming a reality, with the first (of I think many) TSVs coming in Q4!
   Also: CoinDesk, Reuters, CryptoSlate, The Crypto Times, The Coin Republic, Wall Street Journal, Bitcoin Insider, Decrypt, +8 more

10. The IWF says it assessed 6,310 AI-generated images that met the legal definition of CSAM in H1 2026, 40% more than the 4,500+ images assessed in all of 2025
   Dan Milmo / The Guardian — https://www.theguardian.com/technology/2026/oct/05/internet-watch-foundation-huge-rise-ai-child-sexual-abuse-material
   Abuse material monitor says number of AI images assessed this year is already 40% higher than last year's total
   > @iwfhotline: Our analysts have found more photorealistic child sexual abuse material in the first half of 2026 than for the whole of the prior year. “Tech companies must build tools which cannot be abused this way
   > @joshthomas_iwf: “Tech companies must make tools which can't be abused this way,” says @IWFhotline policy chief @hannahswirsky. “This problem has been created by technology & if companies won't make tools which are sa
   > @2rarely: Internet Watch Foundation reports huge rise in AI Child Sexual Abuse Material #CSAM Abuse material monitor says number of AI images assessed this year is already 40% higher than last year's total. htt
   > @gregcantyfuzion: Where are all of the incredible world changing benefits that we heard so much about ??- AI technology is out of control and worse the leaders don't care, they just want to be the first https://www.the
   > @shadowfetch: The Internet Watch Foundation said it has assessed 6,310 AI images that met the legal definition of child sexual abuse so far this year, up from about 4,500 in all of 2025, The Guardian reported. Deta
   Also: 404 Media, Digital Trends, Tech Times

11. An official says the DOD has stopped using Anthropic's tools; sources: Claude was in use as recently as last week, including in military operations against Iran
   BBC — https://www.bbc.com/news/articles/c5j9x9pr0240o
   Technology reporter in San Francisco and — The US Department of Defence is no longer using Anthropic's AI tools …
   Also: RuntimeWire

12. Q&A with AI researchers Jacob Coxon, Daniel Kokotajlo, Alex Turner, and others on leaving AI labs, AGI's dangers, planned IPOs, AI safety, oversight, and more
   New York Magazine — https://nymag.com/intelligencer/article/ai-researchers-quit-openai-anthropic.html
   Exit interviews with defectors from OpenAI, Anthropic, and DeepMind. — On September 8, Jacob Coxon, a 27-year-old Anthropic employee …
   > @sharongoldman: THIS. IS. Unbelievable. I am absolutely speechless on this one. There is NO disclosure in the @NYMag piece other than it saying it is a collaboration with Asterisk, even though if you click through to
   > @teortaxestex: Three of my mutuals are on stage! Pretty reasonable crowd Strong move by EAs
   > @david_kasten: A huge get for NY Magazine to convince @asteriskmgzn to partner with them on this story!
   > @jasminewsun: incredible
   > @speakermenin: Jacob Coxon quit Anthropic after he came to believe that AI could pose a risk to humanity. Shortly, he will testify at a City Council hearing, along with fellow industry whistleblowers Daniel Kokotajl

13. In a first-of-its-kind pilot in the US, Nolla Health will use AI to diagnose and prescribe acne medications to Utah patients without direct human oversight
   Annika Inampudi / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-05/nolla-health-ai-can-now-prescribe-acne-drugs-in-utah-without-doctors?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MTIxNjEzOSwiZXhwIjoxNzkxODIwOTM5LCJhcnRpY2xlSWQiOiJUTUZMODVLSVAzS00wMCIsImJjb25uZWN0SWQiOiI4OUM4OTNDMDhGOTQ0NThDQkQwQTQyREY1RDFCOTY0QyJ9.crHEdlDbj7Dx78MJpxZ7nHnh7NmskJmIYVmdbeyomfE
   In a first-of-its-kind pilot, Nolla Health lets AI diagnose and issue prescriptions. — An AI-based healthcare startup on Monday …
   > @boringbiz_: Doctors: “yeah my job involves actually seeing patients, and it's not like AI is ever going to give you a prescription” AI:
   > @luiswenus: Today, Nolla Health became the first organization in the U.S. (and possibly the world) to receive regulatory approval for an AI to issue initial prescriptions. This makes Nolla the first ever actual e
   Also: STAT, Nolla Health, Unite.AI

14. Munich-based RobCo, which makes robotic arms and automation software, sells $40M of shares at a $1B+ valuation, up from ~$500M after raising $100M in January
   Ben Dummett / Wall Street Journal — https://www.wsj.com/tech/robotics-startup-robco-hits-1-billion-valuation-784bd6a5?st=yskaLT&reflink=desktopwebshare_permalink
   German company aims to capitalize on growing demand for autonomous industrial robots — German robotics startup RobCo has sold shares …
   Also: Reuters, Autonomous Industrial Robotics, PYMNTS, Quartz, RuntimeWire, Silicon Republic, Unite.AI, Startup.eu, +1 more

15. Cohere launches North 2, an update to its enterprise agent platform with cross-session memory and a redesigned harness, available across cloud and on-premises
   Sean Michael Kerner / VentureBeat — https://venturebeat.com/orchestration/coheres-north-2-puts-ai-agents-on-a-budget-and-gives-them-a-memory
   Cohere is going after two common enterprise agent problems with North 2, the new version of its enterprise agent platform.
   Also: Cohere, Globe and Mail, Unite.AI, SiliconANGLE, The Logic

16. Meta, TikTok, and X challenge UK's Ofcom over the amount of info it is demanding under the Online Safety Act, saying it creates unprecedented regulatory burdens
   Paul Sandle / Reuters — https://www.reuters.com/legal/litigation/meta-tiktok-x-challenge-uk-watchdog-over-online-safety-data-demands-2026-10-05/
   Meta (META.O), TikTok and X are challenging British regulator Ofcom over the amount of information it is demanding …
   Also: Law360

17. Survey: only 11% of 396 businesses could forecast AI spending; Microsoft finds lower-priced models cost more than higher-priced ones on 32% of 6,800+ tasks
   Wall Street Journal — https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a?st=1trc2u&reflink=desktopwebshare_permalink
   Artificial-intelligence use is measured in tokens, but the models' use of tokens at any given task can be unpredictable
   Also: PYMNTS, Financial Times, Paul Kedrosky

18. CTS: Chinese logic and memory chipmakers have imported 343 ASML immersion DUV lithography scanners from 2012 to early 2026, many of which can make 7nm chips
   Anton Shilov / Tom's Hardware — https://www.tomshardware.com/tech-industry/semiconductors/china-stockpiled-343-immersion-duv-tools-for-advanced-chipmaking-report-claims-270-asml-scanners-can-produce-7nm-processors-without-sanctioned-euv-tools
   China, apparently, has significant immersion DUV capability. … Chinese chipmakers have accumulated an estimated 343 immersion …
   > @chrisrmcguire: Everyone should read @techstatecraft's fantastic report by @nchlsbrwn on how China's access to ASML's DUVi lithography machines is driving its AI chipmaking capability. It's THE definitive report on t
   Also: Seoul Economic Daily, Motley Fool, Yahoo Finance, DigiTimes, MoneyWeek

19. Sources: Nico Caprez, son-in-law to Jensen Huang, rapidly ascended to become an Nvidia VP, serving as its main contact for neoclouds and Huang's “consigliere”
   Phoebe Liu / The Information — https://www.theinformation.com/articles/jensen-huangs-son-in-law-became-one-trusted-executives
   A little over a week ago, Madison Huang, a rising star at Nvidia and the daughter of its CEO, celebrated her wedding in Hawaii.
   > @_iainmartin: “Another employee said Nvidia now runs much more like a family business than people realize, which is a rare sight in the tech industry” https://www.theinformation.com/ ...
   > @_pheebini: New: I spoke with more than a dozen people who work with Nico Caprez, Jensen's new son-in-law (he and Madison married in Hawaii recently). Here's how he is quickly becoming one of Nvidia's most import
   > @jessicalessin: Nvidia is one of the most talked about companies in the world. But no one really understands how it operates. @theinformation has another deep dive with this profile of Jensen's son in law who is one 

20. French conglomerate Schneider Electric agrees to acquire US engineering software provider PTC for $23.7B in cash, paying $205 per share, its largest acquisition
   Financial Times — https://www.ft.com/content/2084f349-0829-4130-a5e6-b98929a6e633
   Takeover is French conglomerate's largest and enhances its products focused on manufacturers
   Also: WebDisclosure, Fierce Sensors, DatacenterDynamics, Bloomberg, Boston Business Journal, Constellation Research, Capital Brief, Reuters, +15 more

21. Valon, which makes software to help US mortgage companies cut red tape and costs, raised a $150M Series D from Ribbit, a16z, and others at a $2.3B valuation
   Zoya Hasan / Forbes — http://www.forbes.com/sites/zoyahasan/2026/10/05/fintech-unicorn-valon-hit-a-2-billion-valuation-to-bring-ai-to-americas-13-trillion-mortgage-market/
   > @wangandrewd: Thrilled to announce Valon's $150M Series D at $2.3B. Welcome @RibbitCapital to the Valon family and thanks to @a16z and others for the continued support. If you're energized by solving the hardest pr
   > @valon: Today we announced a $150M Series D at $2.3B, welcoming @RibbitCapital as a new investor and continued participation from @a16z, and others. Within 6 months of bringing ValonOS to market, we closed ov
   Also: PYMNTS.com, FinSMEs, Valon

22. Namespace, which offers cloud services and infrastructure for developers, raised a $42M Series B led by Scale Venture Partners and says it has 1,000+ customers
   Chris Metinko / Axios — https://www.axios.com/pro/enterprise-software-deals/2026/10/05/developer-infrastructure-namespace-scale
   Also: Tech.eu, RuntimeWire

23. Billionaires Index: tech billionaires account for all of the $845B in wealth gains so far in 2026; those whose fortunes came from outside tech lost $62B total
   Kristine Owram / Bloomberg — https://www.bloomberg.com/news/newsletters/2026-10-05/ai-billionaires-drive-845-billion-surge-in-wealth-this-year
   Also: The Economic Times, Bloomberg Law, New Yorker

24. Former Groq engineers file a lawsuit in Delaware against Groq, alleging the $20B “non-exclusive” acqui-hire deal with Nvidia in 2025 short-changed employees
   Financial Times — https://www.ft.com/content/93ee425d-9ac7-4543-8cc9-fef2e0670787
   > @joy: 👀 This explains the curious vibe... [embedded post]
   Also: Bloomberg Law, CNBC

25. An interview with CoreWeave Physical AI SVP Richard Ahlfeld on AI models failing real-world checks, the roles of synthetic data and physical tests, and more
   Superintelligence — https://read.getsuperintel.com/p/the-most-common-failure-isn-t-a-bad-model-coreweave-s-richard-ahlfeld-on-physical-ai
   Also: Constellation Research, Motley Fool

26. A look at China's gray market of token resellers, who use accumulated identities and USDT-funded cards to obtain Claude accounts and route them through proxies
   The Information — https://www.theinformation.com/articles/chinas-token-resellers-create-anthropic-gray-market

27. A look at Alpha, an invite-only Discord server of ~30 mostly Gen Z Polymarket traders who pool research and capital and have made an estimated $40M since 2024
   Niamh Rowe / Financial Times — https://app.ft.com/content/ac1f4db2-54fe-4a36-b3db-bb96675231f5
   Also: CryptoPotato

28. Sources: Firmus plans to allocate ~50% of its IPO shares to existing holders, as investor demand far exceeds the offer size in one of Australia's largest IPOs
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-05/firmus-said-to-plan-allocating-half-of-ipo-to-existing-investors
   Also: Reuters, Finimize, Australian Financial Review, Tech in Asia

29. Sources: several Western open-weight models are set to launch in October, such as Reflection AI's first model, expected to rival top Chinese open-weight models
   Bradley Olson / Axios — https://www.axios.com/2026/10/04/reflection-open-weight-ai
   > @cat_zakrzewski: Scoop? Last week Reflection CEO Misha Laskin spoke with me about his plans to launch an open-weight model soon, arguing it was necessary for national security. You can watch here https://www.youtube.c
   > @teortaxestex: I would be surprised. It's not that easy to train a model as good as even GLM 5.3 without years in the trenches. Nvidia could not, Thinky so far could not. Why would Reflection? But we've also had a l
   > @operationdanish: If this release is real, Anthropic will delay its IPO.
   > @shakeelhashim: This is such a strange (and strangely written) article.
   > @mcgrewsecurity: Weights or gtfo
   Also: Gizmodo, New York Times, RuntimeWire

30. A look at Sean Parker's resurrection of Stability AI following Emad Mostaque's ousting, and its new focus on AI for music professionals, backed by major labels
   Abram Brown / The Information — https://www.theinformation.com/articles/sean-parker-spreads-gospel-ai-music

31. Change.org says it is investing ~$100M of its own money to rebuild its core petitions platform using AI and launches an AI copilot beta for petition creators
   Dan Primack / Axios — https://www.axios.com/2026/10/02/changeorg-ai-100-million

32. Q&A with Google SVP and DeepMind Institute co-director James Manyika on AI risks and why responsibility must be shared across industry, government, and society
   Mishal Husain / Bloomberg — https://www.bloomberg.com/features/2026-james-manyika-weekend-interview/?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MTA0MTMwOSwiZXhwIjoxNzkxNjQ2MTA5LCJhcnRpY2xlSWQiOiJUTTlLSzlSS1YyVFYwMCIsImJjb25uZWN0SWQiOiJEMzU0MUJFQjhBQUY0QkUwQkFBOUQzNkI3QjlCRjI4OCJ9.u-yRXj5OldEL8nTrVyxthWTvxQ8nek0go4FwVqRE75E
   > @bloombergtv: “I don't think it should be left to any one company.” Google SVP James Manyika tells @MishalHusain a “collective effort” is needed to ensure AI safety. Listen at http://swap.fm/... or watch The Mishal
   > @business: Google's James Manyika says AI's risks are real and regulation is necessary. But responsibility has to be shared across industry, government and society. https://www.bloomberg.com/...
   Also: Bloomberg Podcasts on YouTube

33. Sources: UK neobank Monzo is in talks with CVC and Advent to sell up to a 15% stake, after Nubank takeover talks collapsed over the ~£10B valuation Monzo sought
   Laith Al-Khalaf / Financial Times — https://app.ft.com/content/57de6604-70a9-413a-a381-9ba82ec202ec
   Also: The Paypers

34. Sources: Anthropic's stock matching of employee charity gifts hit $660M+ from October 2025 to March 2026, likely to pass billions in 2027, diluting shareholders
   Cory Weinberg / The Information — https://www.theinformation.com/articles/anthropics-big-charity-bill-shareholders

35. Extracted system prompts show Meta's Muse compiles “a page for every person in the user's life”, with facts, history, tips to improve relationships, and more
   Wired — https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/
   > @irbto: @Techmeme Yeah, they're open about it. It's literally an entire tab in the app. This is not a shocker and it's a core feature of their product.
   > @_simonsmith: Yes, and this is awesome, and it's not all nefarious, you can see everything in your system files. I'm not a Meta cheerleader and don't use Facebook, Instagram, or Threads. And we should absolutely wa
   > @carissaveliz: Sometimes we make the simple complicated. Meta's current business model depends on #surveillance; therefore, the incentive is for it to design products to further that surveillance, not to benefit you
   > @paul__walsh: “Millions have eaten McDonald's chicken nuggets. But filling your appetite with them brings dietary issues”. In 2007, I refused to work with TRUSTe because they gave Facebook a privacy seal to signal 
   > @yoda: “isn't muse so cute?” i'm sure there were people who thought hitler's mustache was eccentric and adorable, too. wake up, people.
   Also: Gizmodo, 9to5Mac, Wall Street Journal, PCWorld, Implicator.ai, The Independent, Fortune, Entrepreneur, +2 more

36. Trump announces a Super Intelligence Force, led by DNI Jay Clayton, along with FTC Chair Andrew Ferguson, the DOD's Emil Michael, and OPM Director Scott Kupor
   Politico — https://www.politico.com/news/2026/10/04/jay-clayton-ai-trump-01106137
   > @rapidresponse47: [Screenshot of Trump's TRUTH Social post: “...I am announcing the formation of the Super Intelligence Force (SIF). The Super Intelligence Force is tasked with coordinating the effort of the Federal Go
   > @whitehouse: “I am announcing the formation of the Super Intelligence Force (SIF). …
   > @jkhamehl: scott is hands down one of the most effective, pragmatic people I know - so proud of @skupor helping our great country lead in SI 🇺🇸🚀💪
   > @skupor: Very honored to work with @ODNIgov , @USWREMichael and @AFergusonFTC and the entire SIF committee members to deliver on @POTUS mission - the U.S. will continue to lead in SI to enhance the well-being 
   > @vtg2: The selection of Clayton, a former SEC chair and Wall Street lawyer, is good news for the financial industry. I reported recently that Wall Street's ask on AI was, as one source put it, “somebody be t
   Also: Cybersecurity Dive, Semafor, BBC, Defense One, Forkast, The Information, TechCrunch, Washington Post, +26 more
