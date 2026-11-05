# Research — News Cluster

Search for news **events that occurred** between **2026-10-22 10:00 BRT** and **2026-10-23 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-22 10:00 BRT to 2026-10-23 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-23
**Research window:** 2026-10-22 10:00 BRT → 2026-10-23 10:00 BRT

**Previous edition headlines (2026-10-22 — skip unless genuinely new development):**
- deepseek-raises-15b-funding-round: DeepSeek raises about $15B, one of China's largest rounds, led by CATL and Tencent
- anthropic-claude-duet-proactive-agent: Anthropic opens preview of Claude Duet, a proactive background agent app on Opus 5.5
- microsoft-storm-0940-artex-agentic-ai-connectwise: Microsoft: China-aligned hackers used agentic AI tool ARTEX to breach ConnectWise tenants
- hugging-face-carbon-x-dna-model: Hugging Face releases Carbon-X, an open 14B model that answers questions about DNA in English
- flapping-airplanes-1b-series-a: Year-old AI lab Flapping Airplanes raises $1B Series A at a reported $6B valuation
- meta-q3-muse-10m-users-class-c-stock-ai: Meta says 10M+ set up Muse agents; creates nonvoting shares to fund AI buildout
- walmart-agent-gateway-mcp-ai-shopping: Walmart launches Agent Gateway MCP server to let AI agents shop, as Amazon blocks them
- tesla-optimus-early-production-fremont: Tesla starts early Optimus production on Fremont's high-volume line, cuts 2026 capex to ~$20B
- micron-taoyuan-strike-first-taiwan-chip-strike: Micron union stages Taiwan's first-ever chip-industry strike over AI-profit sharing
- lam-research-ti-q3-results-chip-demand: Lam Research posts record $8.22B quarter; TI revenue jumps 28% with data center up ~95%
- lava-b300-chips-china-telecom: Security firm Lava traces 32 banned Nvidia B300 chips to China Telecom-linked IP addresses
- huang-nscale-work-around-the-clock-neoclouds: Huang says he told Nscale to 'work around the clock'; neoclouds 'just need working capital'
- humain-datavolt-nebius-oxagon-neom: Nebius signs as first customer for HUMAIN and DataVolt's AI campus at NEOM's Oxagon
- enact-maxinsights-robotics-funding: Robotics startups Enact and Maxinsights each raise $30M; Mensch and LeCun back Enact
- iran-seven-tankers-hormuz-strike-plans-brent-112: Iran says 7 tankers hit in Hormuz as US-Israel strike plans surface; Brent tops $112
- russia-kyiv-ballistic-barrage-after-talks-ukraine-drones-moscow: Russia fires 21 ballistic missiles at Kyiv hours after agreeing to talks; Ukraine sends 630 drones at Moscow
- pentagon-technology-support-office-covert-sabotage: Politico: Pentagon quietly built TSO, a new agency to covertly sabotage foreign military tech
- barclays-cuts-5000-jobs-ai: Barclays to cut 5,000 jobs, about 5% of staff, in AI-driven cost push
- global-stocks-ai-jitters-treasury-below-france: AI jitters sink global stocks; US 10-year yield falls below France's for first time in 13 years
- xona-250m-series-d-pulsar-gps-alternative: Xona raises $250M at $2.45B valuation for its Pulsar alternative to GPS
- palantir-no-kill-switch-nato-maven-starshield: Palantir says NATO's Maven AI system has no US 'kill switch' after Ukraine Starshield cutoff

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 41 stories

1. Sources: OpenAI nears an up to $30B round led by investors from the UAE and Coatue at a $1.25T pre-money valuation, as an “opportunistic” bridge ahead of an IPO
   Kate Rooney / CNBC — https://www.cnbc.com/2026/10/22/openai-funding-round-uae-investors.html
   OpenAI is closing in on a funding round that could value the artificial intelligence giant at more than $1 trillion ahead …
   > @kimmonismus: OpenAI nears up to $30 billion funding round at $1.25 trillion valuation led by UAE investors. OpenAI's valuation in this new round would exceed Anthropic's last private valuation. However, Anthropic 
   > @kr00ney: Scoop: OpenAI is closing in on a funding round of up to $30 billion at a $1.25 trillion (pre-money) valuation, led by UAE investors and Coatue Alongside the new investment, OpenAI is negotiating a com
   > @stanphylcap: So $1.25T not $1.5T? That's a pretty big haircut!
   > @ft: OpenAI trims valuation target to $1.25tn after pitching higher price https://www.ft.com/...
   > @kt_futures: @KobeissiLetter Petrodollars funding the ultimate exit liquidity.
   Also: TechCrunch, The Decoder, The Information, PYMNTS.com, Implicator.ai, SiliconANGLE, Crypto Briefing

2. Sources: OpenAI has cut its valuation target to $1.25T, down from the $1.4T valuation it pitched earlier this month, after facing resistance from some investors
   Financial Times — https://www.ft.com/content/bb564eb1-79d4-4694-aa24-1155202a9abc
   AI lab floated $1.4tn price tag earlier this month, according to documents seen by the FT — OpenAI has cut its valuation target …
   > @edzitron: lmfao Dubai made clammy sammy drop the valuation
   Also: Fortune, Semafor, Bloomberg, Telegraph, Crypto Briefing, The Straits Times

3. US Treasury proposes rules tightening restrictions on US investments in areas including AI and supercomputing in China, Russia, and other “countries of concern”
   Associated Press — https://apnews.com/article/treasury-china-tech-investments-rule-b742c292ff8eb19e6a4c8cf03d4d66b9
   The U.S. Treasury Department proposed a rule Thursday to crack down on American high-tech investments such as supercomputing …
   > @niubi: Treasury Issues Proposed Rule to Implement Comprehensive Outbound Investment National Security Act https …
   Also: U.S. Department …, The Information, Barron's Online, The Hill, Financial Times, Crypto Briefing

4. An interview with Ondřej Surý, a volunteer who maintains PHP and automates its patches, about his role in fixing two critical PHP security vulnerabilities
   Charlie Warzel / The Atlantic — https://www.theatlantic.com/technology/2026/10/man-who-saved-internet-php-vulnerability/689123/?gift=iWa_iB9lkw4UuiWbIbrWGX0S2EScp28jU-louXZfg5I&utm_source=copy-link&utm_medium=social&utm_campaign=share
   On Tuesday, the world found out about two massive security vulnerabilities in PHP, a programming language that is used by roughly 70 percent of websites.
   > @cwarzel: His name is Ondřej Surý and yesterday he kinda saved the internet. I called him up to talk about it! https://www.theatlantic.com/ ... [embedded post]
   > @censysio: Two critical PHP vulnerabilities. Widespread Internet exposure. Reuters covers the latest developments, citing Censys research. https://www.reuters.com/... Follow our Censys ARC advisory for the lates
   > @cwarzel: 70% of the internet was vulnerable yesterday to very bad security flaws inside a coding language. Turns out, *one volunteer* is mostly responsible for maintaining that code & helping push updates. Yes
   > @cwarzel: really exactly the kind of guy you want in charge of something like this
   > @josephfcox: New: AI is making it so much easier to discover serious vulnerabilities. This applies both to people with little skill, and researchers with a lot of expertise. If you can't accept AI is exceptional a
   Also: 404 Media, Business Insider, Tech Times, Moneycontrol, CyberScoop, BBC

5. Cloudflare's Matthew Prince says PHP2Shell exploit attempts on its network rose from thousands in the 10 hours before the disclosure to millions afterward
   Matthew Prince / @eastdakota — https://x.com/eastdakota/status/2113079352682570051
   > @bayeslord: Millions of attempted exploits. I'm confused. Where is the impact? [embedded post]
   > @nikitabier: There is nothing to worry about. Nothing important is run on PHP or old software—except the water & electrical grid, a few government services like our missile defense systems and a handful of electri
   > @bitcoinpalmer: Guys I know I meme and pasta a lot But I'm 100% struggling to see how this isn't a massive black swan otw [embedded post]
   > @noahpinion: DESTROY THE INTERNET [embedded post]
   > @c_c_krebs: [image] [embedded post]
   Also: Associated Press, CNN, BBC, Superintelligence, NPR, Reuters, The Asia Business Daily, Gizmodo, +4 more

6. SK Hynix says its SSD subsidiary Solidigm has halted a review of a potential US IPO to fund a new US chip fab, citing “market conditions and share price trends”
   P.R. Venkat / Wall Street Journal — https://www.wsj.com/tech/sk-hynix-shelves-plans-for-u-s-listing-of-memory-chip-unit-solidigm-e9670506?st=aR7N6u&reflink=desktopwebshare_permalink
   SK Hynix's shares fell as much as 4.2% in early trade in Seoul — SK Hynix halted plans to list its memory-chip unit in the U.S. …
   Also: SK hynix Newsroom, Korea JoongAng Daily, Barron's Online, Silicon UK, Bloomberg, The Korea Herald, The Korea Times, Seoul Economic Daily, +10 more

7. OpenAI suspected the three fired researchers of leaking internal model designs to AI safety researcher Ryan Greenblatt, including via disappearing Signal chats
   Wall Street Journal — https://www.wsj.com/tech/ai/the-signal-chats-that-cost-openai-researchers-their-jobs-594c5853
   The company fired three safety researchers for mishandling sensitive information. They had been fighting to keep the workings …
   > @zeffmax: New: The three researchers OpenAI fired last month spent the summer fighting to keep AI's chain-of-thought process visible. Then, OpenAI asked to see their Signal chats. A week later, they were let go
   > @so8res: It sounds like OpenAI fired the three safety researchers because they used disappearing messages. It sounds like they weren't told not to; they were just fired without warning after the fact. Seems ba
   > @_nathancalvin: The WSJ says OpenAI is searching employees personal phones and looking through their Signal messages [image] [embedded post]
   Also: OpenAI

8. a16z rebrands a16z Crypto as a16z Frontier and expands the fund's scope to back startups developing AI, robotics, and other emerging technologies
   Camila Grigera Naón / Fortune — https://fortune.com/2026/10/22/venture-giant-andreessen-horowitz-crypto-name-blockchain-fund-rebrands-a16z-frontier/
   In 2018, Andreessen Horowitz made a splash in the venture capital world by launching a spin-off dedicated to digital assets called a16z Crypto.
   > @leomschwartz: Scoop: a16z's flagship blockchain fund plans to drop “crypto
   > @a16z: Chris Dixon on a16z Frontier's investing philosophy, and why being too early is better than being too late: “We believe that basically every good idea that we've ever seen that involved technology has
   > @eleanorterrett: Are we entering the 'it won't be called crypto, it'll just be finance' era?
   > @a16z: Marc Andreessen says individuals are adopting AI faster than organizations, and startup formation is going to skyrocket as a result:
   > @a16zfrontier: “We want to err on the side of being too early.”
   Also: TechCrunch, a16z Frontier, Bitcoin Insider, CryptoSlate, TheStreet, YouTube, Bitcoin News, Crypto Briefing, +2 more

9. Sources: Anthropic and London-based PE firm Hg agree to launch a consultancy by the end of 2026 to embed AI consultants and engineers into European businesses
   Financial Times — https://www.ft.com/content/df70bf20-e809-48d0-8485-f8f514a7fbc4
   New company backed by Anthropic and UK buyout group Hg will advise companies on how to deploy AI
   Also: Crypto Briefing

10. Sources: US banks are restricting third-party AI agents from accessing customer accounts, after some agents appeared to act independently of users' instructions
   Madison Mills / Axios — https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access
   Major U.S. banks are detecting unauthorized third-party AI agents operating inside customer accounts, with some agents attempting …
   > @madisonmills22: SCOOP: Major U.S. banks are detecting unauthorized third-party AI agents inside customer accounts, including some attempting to take actions that appear to be independent of user instructions, sources
   > @peterwildeford: I feel like one service I can provide is trying to help sort through what feels like a big deal …
   > @hedgiemarkets: 🦔Yup...I've been uneasy about this one since Muse launched. Banks catch fraud by knowing it's you on the other end, and some of them now can't tell you from the software. If you connect your bank to M
   > @sensanders: This is insane. We cannot allow AI agents to go into your bank account and act independently without your authorization. But that is what's happening right now. Left unchecked, AI could endanger the e
   > @chafkin: stories like this are often held up as proof that AI is advancing at a breakneck speed. I think its proof that most of these agents don't work very well (at least for now!) https://www.axios.com/...
   Also: Reuters, New Republic, TechCrunch, WinBuzzer, American Banker, Axios, Business Insider, Marcus on AI, +14 more

11. Microsoft says its GPT-5-powered Diagnostic Orchestrator uses agents that mimic panels of experts to diagnose conditions up to 4x more accurately than doctors
   Robert Hart / The Verge — https://www.theverge.com/ai-artificial-intelligence/1016690/suleyman-microsoft-diagnostic-orchestrator-science-medical-superintelligence
   'We're going to build something that is indistinguishable from human performance ... in the next couple of years,' Microsoft AI CEO Mustafa Suleyman tells The Verge.
   > @tomwarren: Microsoft says its AI tool is better than doctors at diagnosing conditions. The company claims to have developed an AI-powered tool it says can diagnose conditions up to four times more accurately tha
   > @verge: 'We're going to build something that is indistinguishable from human performance ... in the next couple of years,' Microsoft AI CEO Mustafa Suleyman tells The Verge. https://www.theverge.com/...
   Also: Reuters, TechCrunch, Microsoft AI, The Neuron, Digit, Gizmodo, Unite.AI

12. Chinese state media: DeepSeek and MiniMax completed registration and won approval to open-source and deploy AI models overseas under proposed export controls
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-23/deepseek-minimax-win-approval-for-global-use-state-media-says
   DeepSeek and MiniMax Group Inc. have won approval to deploy models overseas, part of a wave of homegrown AI technologies that Beijing …
   Also: Reuters, South China Morning Post

13. Anthropic donates the Agent Skills open standard to the Agentic AI Foundation and says 70+ platforms have integrated it, after donating MCP to the AAIF in 2025
   Anthropic — https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation
   Today, we're donating Agent Skills, the open standard that gives AI agents specialized knowledge and workflows, to the Agentic AI Foundation (AAIF).
   > @claudedevs: We're donating Agent Skills to the Agentic AI Foundation (@AgenticAIFdn), the same foundation we donated MCP to. Since December 2025, 70+ agent platforms have integrated the standard, including ChatGP
   > @tokengremlin: “We're donating Fable 5.5...” Oh, never mind. They're just donating some Agent Skills.
   > @adocomplete: Free the standards! So happy to see this.
   > @bcherny: Agent Skills started as an experiment in Claude Code. Many across the industry have come to adopt it, so we at Anthropic found it more fitting to donate it to the @AgenticAIFdn, next to MCP.
   > @claudedevs: The committee's first priority is a roadmap: versioned releases, a formal proposal process, and security guidance for skill authors and users. Want to contribute? Start with the spec at https://agents
   Also: The Register, The New Stack, SiliconANGLE, Blockchain.News, Simon Willison's Weblog

14. SK Telecom unit SK Hyper is in talks with tech firms and investors to finance 15GW of data center capacity in South Korea by 2035; the first 5GW will cost $350B
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-23/sk-data-center-arm-in-talks-to-fund-350-billion-ai-buildout
   SK Hyper Co. is in talks with big tech firms and financial investors to secure funding for an envisioned $350 billion data center buildout …
   Also: Seoul Economic Daily, RuntimeWire, Chip Briefing

15. Anthropic says it partnered with Theorem to use Claude to formally prove security properties at the assembly level across 100+ real-world open-source libraries
   Anthropic — https://www.anthropic.com/research/formal-verification
   Introduction — Even mature, heavily tested software contains bugs, and LLMs are increasingly adept at finding them.
   > @anthropicai: New on our Frontier Red Team blog: using Claude to formally verify software at large scale. Formal verification can prove that code is free of certain bugs, but historically it has only been feasible 
   > @choblin29: This is INSANE. Anthropic says Claude wrote around one billion lines of formal proofs …
   > @___atin___: When people want hope in the face of the onslaught of bugs; I send them a link to this blog post.
   > @envoldev: This week: two PHP bugs put the internet in lockdown. Today: Claude proved security properties in 100+ open-source libraries in a few weeks. Someone point it at PHP. 🙃
   > @gf_256: How to find ALL PHP bugs: 1. Compile code (e.g. to RISC-V, x86, LLVM IR) 2. Vibe prove ASAN and non-ASAN versions have same behavior across all inputs. Hard, but Claude can do it! 3. Find a LOT of bug
   Also: Blockchain.News, Unite.AI, Crypto Briefing, CryptoSlate

16. Canva launches Craft, its first image generation model, trained on human-designed templates, available to all users, with plans to support third-party chatbots
   Ivan Mehta / TechCrunch — https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/
   Design platform Canva released its first image generation model, called Canva Craft, developed by its research team to compete …
   Also: TestingCatalog AI News, Forbes Australia, Capital Brief, Australian Financial Review, The West Australian, SmartCompany, Digital Trends, Unite.AI, +3 more

17. Oura sues Indian smart ring rival Ultrahuman again to block US sales of Ring Pro, months after a redesign helped Ultrahuman return following an import ban
   Jagmeet Singh / TechCrunch — https://techcrunch.com/2026/10/22/oura-sues-rival-ultrahuman-again-threatening-its-u-s-smart-ring-comeback/
   Smart ring maker Oura has sued Indian rival Ultrahuman again, seeking to block U.S. sales of its Ring Pro (pictured above) …
   Also: Engadget, The Pulse Blog, Gadgets & Wearables, ip fray

18. An interview with Intel's leadership, including CTO Pushkar Ranade, on AI chip demand, lessons from 10nm, whether Intel can catch up to TSMC, Terafab, and more
    — https://www.dwarkesh.com/p/intel-tour
   What I learned from touring Intel's most advanced fab and talking to its leadership. — I spent two days touring Intel's …
   > @intel: What does it really take to make the world's most advanced chips? Thousands of intricate manufacturing steps. Extraordinary engineering precision. And an industry working to meet growing global demand
   > @intel: @dwarkesh_sp Thank you, Dwarkesh, both for spending time with us in Oregon and for featuring so many Intel leaders on the podcast! We appreciate the opportunity to showcase the latest in semiconductor
   > @dwarkesh_sp: My semis tutor @willmichaels0 and I made a bunch of flashcards about semiconductor manufacturing. Check them out if you want to better understand and retain the explainers in the new Intel episode. Wi
   > @benbajarin: Well produced. All the things I have been saying about Intel was well positioned with for three years now and taken much hate on this platform for being a believer. And its because we dove deep on the
   > @mzuhair123: This is an amazing podcast by @dwarkesh_sp, as always. Intel is a company which is really close to me since childhood, and I have always talked in support of it, no matter the circumstance. Foundries 

19. Greece's parliament passes a bill to ban social media platforms for children under 15 from 2027 and gives companies two months to verify users' ages
   Angeliki Koutantou / Reuters — https://www.reuters.com/legal/litigation/greece-passes-social-media-ban-children-under-15-2026-10-23/
   Greece's parliament approved a bill on Friday that bans the use of social media platforms for children under 15 amid growing concerns …
   Also: Agence France-Presse

20. Sources: SpaceX is in talks with at least one major cellular infrastructure firm to secure a minimum of 80K US cell sites, as it eyes a wireless carrier launch
   Kelcee Griffis / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/spacex-in-talks-to-access-80-000-cell-sites-for-wireless-network
   SpaceX aims to secure a minimum of 80,000 cell sites across the US, and it's in talks with at least one major cellular infrastructure company …
   Also: MarketWatch, Finimize, Dow Jones Newswires, Forbes, Honolulu Star-Advertiser, Reuters

21. Amazon rebrands its Kindle Unlimited subscription as Kindle+ and expands access to audiobooks, including titles narrated by AI
   Maria Diaz / ZDNET — https://www.zdnet.com/tech/kindle-unlimited-kindle-plus-audiobooks-ai/
   Unlike narrated audiobooks from Audible and other providers, the audiobooks created with Virtual Voice in Kindle+ will instead be narrated by AI. — ZDNET's key takeaways
   Also: Thurrott, Good e-Reader, Android Central, Digital Trends, iPhone in Canada, 9to5Mac, The Verge

22. Spotify confirms it is rolling out a new family plan verification method requiring members to scan QR codes on plan managers' phones within seven days of notice
   Sarah Perez / TechCrunch — https://techcrunch.com/2026/10/22/spotify-confirms-family-plan-crackdown-but-calls-it-a-routine-improvement/
   Spotify confirmed the reports of its crackdown on Family Plan sharing during its third-quarter call with investors …
   Also: Thurrott, The Verge, Simon Owens's Media Newsletter, Reuters, Spotify

23. Sources: Elon Musk has invested ~$1B in Ellisons' Skydance; in 2022, David Ellison's father, Larry Ellison, invested $1B in Musk's deal to take Twitter private
   Rohan Goswami / Semafor — https://www.semafor.com/article/10/22/2026/elon-musk-makes-1-billion-investment-in-ellisons-skydance
   Elon Musk has invested roughly $1 billion in Skydance, according to people familiar with the matter, providing …
   > @missrobinsays: Elon Musk has invested 1BILLION dollars into Skydance, the company that owns CNN. This could be interesting................. https://www.semafor.com/...
   > @justinbaragona: What we all knew was coming has finally begun https://www.semafor.com/...
   Also: Daily Mail, The Hollywood Reporter, CNBC, Forbes Australia, MediaNews4U, Storyboard18, The Asia Business Daily, Cord Cutters News, +9 more

24. Amazon issues refunds from a 2025 settlement, crediting “President Trump's Federal Trade Commission,” the first time an FTC refund has been tied to a president
   Alfred Ng / Politico — https://www.politico.com/news/2026/10/21/amazon-trump-midterms-settlement-01130666
   Millions of Americans are expected to receive a settlement check from Amazon credited to “President Trump's Federal Trade Commission” …

25. The Browser Company says it will shut down its Arc browser on December 22, launched in 2023, shifting attention to its AI-focused Dia browser, launched in 2025
   Jay Peters / The Verge — https://www.theverge.com/tech/1016832/arc-browser-shutting-down
   New feature development for the innovative web browser ended last year. Now The Browser Company is telling users to try Dia, Arc's replacement.
   > @arcinternet: We've decided to sunset Arc on December 22, 2026. That's not an easy sentence to write. We spent years building Arc and celebrating each and every release along the way: we have so much pride and love
   > @reallyrawn: Arc is the reason I will never switch browsers ever again. I used Chrome for years and years …
   > @itsmatthewao: Dude no one uses Dia I literally cannot understand this decision making [embedded post]
   > @daytonmills: Imagine you accomplish the herculean task of convincing people to switch off of Chrome as their default browser (something Microsoft couldn't even do with billions of dollars) and then you decide to j
   > @korablev: Arc shuts down on Dec 22. I wasn't ready to let it go, so I rebuilt it. Spaces, pinned tabs, Peek, Little Arc, Split View, nested folders. Native Mac app, free. AI stays out of the way until you ask. 
   Also: PCMag, Digital Trends, Thurrott, Neowin, zylstra.org, TechCrunch, Engadget

26. German energy company PreussenElektra says it is working with Nvidia to assess whether the country's idle nuclear plants could be turned into data centers
   Eva Brendel / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/germany-s-idle-nuclear-plants-eye-new-life-as-ai-data-centers

27. Microsoft and Alphabet join 14 other companies objecting to a plan by OKXICE, a venture of OKX and ICE, to trade blockchain-based versions of their shares
   Camila Grigera Naón / Fortune — https://fortune.com/2026/10/21/microsoft-alphabet-object-blockchain-versions-shares-veto/
   Also: WinBuzzer

28. Sources: Datadog offered to acquire Israeli cloud cybersecurity startup Upwind Security for nearly $4B; Upwind is finalizing a $300M round at a ~$3.8B valuation
   The Information — https://www.theinformation.com/articles/datadog-offered-buy-security-startup-upwind-nearly-4-billion
   > @aaronpholmes: SCOOP: Datadog offered to buy Upwind for nearly $4 billion as cloud security demand booms. w/ @validapau https://www.theinformation.com/ ...
   Also: Globes, CTech

29. Sources: SoftBank's SB Energy is considering going public as soon as December or waiting until 2027, as it closely watches Anthropic's IPO, expected in November
   The Information — https://www.theinformation.com/articles/sb-energy-considers-waiting-december-later-ipo
   Also: Seoul Economic Daily

30. US officials say Trump asked Elon Musk to lift Starshield restrictions; Ukraine officials said it was not fully fixed Thursday but was working at higher speeds
   Wall Street Journal — https://www.wsj.com/world/trump-called-musk-and-asked-him-to-lift-ukraine-starlink-restrictions-5aeebc6e?st=hZda67
   > @michaeldweiss: More reporting suggesting that Musk does indeed have his finger on Starshield's operability. Quite a lot of power for a ketamine-addicted trillionaire in bed with hostile foreign regimes. You might ev
   > @mathieuvonrohr: WSJ: President Trump called Elon Musk and asked him to lift restrictions on a military-grade version of Starlink in Ukraine that the SpaceX chief had throttled, U.S. officials said. The system was wor
   > @joshkraushaar: “Vance's message differed from comments by Defense Secretary Pete Hegseth and Secretary of State Marco Rubio that Musk had the authority to enforce his company's terms of service without input from th
   > @courtneywmh: “Trump told Musk he was frustrated the system's speeds remained capped at around 100 mph.” Perhaps the White House now realizes that siding with Russia & punishing Ukraine is unwise prior to the midte
   Also: Washington Post, Straight Arrow, Politico, New York Times, The Kyiv Independent, Reuters, HuffPost, HotAir, +5 more

31. Chicago-based Formic, which provides robots-as-a-service automation to manufacturers, raised $50M, including a $40M Series B and $10M in asset-backed financing
   Natalie Breymeyer / Axios — https://www.axios.com/pro/all-deals/2026/10/22/formic-50m-robotics-deployments
   Also: FinSMEs, Formic, RuntimeWire

32. Microsoft says it is closing The Garage, which for 17 years gave employees worldwide space and tools for side projects and ran the company's Global Hackathon
   Todd Bishop / GeekWire — https://www.geekwire.com/2026/microsoft-shuts-the-door-on-the-garage-the-central-program-behind-its-hackathon-and-maker-spaces/
   > @tomwarren: Microsoft is shutting down its beloved maker space, The Garage. In my Notepad newsletter this week I look back at a key part of Microsoft's hacker culture, as well as a bumper week of Microsoft and Xb
   Also: Windows Report, Neowin

33. Filings: Nvidia, Anthropic, and OpenAI had their highest-spending lobbying quarter between July and September, spending $2.2M, $2.1M, and $1.5M, respectively
   Lauren Feiner / The Verge — https://www.theverge.com/policy/1016585/openai-anthropic-nvidia-lobbying-records
   > @icleanai: The AI labs are now spending like Big Tech in Washington. Filings show Nvidia, Anthropic and OpenAI each had their highest lobbying quarter ever in July-September: $2.2M, $2.1M and $1.5M, per The Verg

34. Atlanta-based Tractian, which uses AI and sensors to predict machine failures and recommend maintenance plans, raised a $130M Series D at a $1.4B valuation
   Rocket Drew / The Information — https://www.theinformation.com/briefings/exclusive-physical-ai-startup-tractian-becomes-unicorn
   Also: Hypepotamus

35. METR says a pilot test of OpenAI's monitoring system found vulnerabilities, including an exploit that could have let AI agents hide hundreds of recent actions
   Anzar Mehraj / Reuters — https://www.reuters.com/business/ai-safety-group-metr-finds-flaws-openais-internal-monitoring-system-2026-10-22/
   > @metr_evals: Two employees from METR and Redwood Research worked on premises at OpenAI for three weeks this summer in an embedded assessment pilot. This team evaluated the systems OpenAI was using to monitor for m
   > @openai: This summer, we invited METR and Redwood Research to pilot an embedded evaluation of our internal monitoring system, providing deep access to our infrastructure over three weeks. Their findings helped
   > @garrisonlovely: METR's really burying the lead here. OpenAI let two external researchers embed for 3 weeks this summer, where they learned [...] Look, OpenAI deserves credit for doing any of this, especially when com
   > @dfrsrchtwts: I feel like this isn't getting enough attention: - there were some pretty big holes found by the red-teamers, e.g. agents could just keep acting and not let the user do stuff and this would prevent mo
   > @andrewcurran_: The original report was 61 pages, it was redacted to 38.
   Also: METR, CNBC, The Neuron, Forkast, Wccftech, The Elec, The Deep View

36. Warp Sciences, founded by former OpenAI CPO Kevin Weil to speed up drug development using AI, emerges from stealth with $215M at an $865M post-money valuation
   Rebecca Torrence / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/ex-openai-science-head-kevin-weil-launches-startup-with-215-million?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MjY4MzA4OCwiZXhwIjoxNzkzMjg3ODg4LCJhcnRpY2xlSWQiOiJUTkJGMkFSMjRVODkwMCIsImJjb25uZWN0SWQiOiJFQUU4NEExRDRERjI0Q0ZFQTg5MjExMzI3OTY0NTYzNSJ9.I9u7mVaiXfV1lUZPdWbgi1qQ_JbRjPEramRjaNApFZk&leadSource=article-gifting
   > @kevinweil: 💥 Introducing Warp Sciences, a new company applying AI and robotics to help the world develop new medicines faster. We've raised a $215M Series A led by @lightspeedvp to bring frontier AI out of the b
   > @lightspeedvp: While AI has advanced in mathematics, we believe there's still a major gap in the physical sciences. @warpsciences co-founders @kevinweil and Solomon Reisberg joined Lightspeed Partner @guruchahal to 
   > @guruchahal: Robotic factories for chemistry? Sign me up 🙂 @kevinweil and i go back to the very start of our careers. today, he and his team launch @warpsciences It was great to revisit those early days and learn 
   > @lightspeedvp: Kevin Weil on why he left OpenAI to build autonomous labs: the next leap in AI needs experimental data the models don't have. “The models are data poor in the physical sciences.
   > @amy: Couldn't be more excited to be a (small) part of this journey with Warp Sciences! @kevinweil has been a dear friend since we first met at Twitter 16 (!) years ago, and he's been passionate about accel
   Also: FinSMEs, SiliconANGLE, Endpoints News, Pulse 2.0, Lightspeed Venture Partners, TechCrunch

37. eMudhra says it will exit the SSL/TLS certificate business, 1% of its revenue, after its TLS certificates with private keys of just 3 to 8 bits were compromised
   Abhirami G / Reuters — https://www.reuters.com/legal/litigation/indian-firm-emudhra-exits-global-digital-certificates-business-after-2026-10-22/
   > @creativewolf: This announcement of “eMudhra to Exit global SSL/TLS Certificate Business” by @eMudhra is only raking up the rank stink. They should undergo a thorough Digital and Financial Forensic Audit and their a
   > @scott_helme: eMudhra claim they're leaving the SSL/TLS business because they're being criticised on social media. It's more likely that they've realised they will probably be fully removed anyway, so they're bowin
   > @zquestz: Due to extreme incompetence eMudhra is leaving the SSL/TLS cert business. Good riddance. May you lose every single customer you have. You have lost all trust. https://emudhra.com/...
   > @mciabuca: @Techmeme @abhiiswriting my phone pin has more bits than that
   > @bee_fumo: Holy fucking shit it actually killed them. https://www.reuters.com/... [image]
   Also: eMudhra Limited, CSO, The Register, Ars Technica, MediaNama, Schneier on Security, heise online, Forkast, +8 more

38. Nirva, which plans to launch a wearable AI personal companion that offers relationship advice and more, raised $25M, bringing its total funding to $33M
   Will Maddox / Axios — https://www.axios.com/pro/health-tech-deals/2026/10/22/nirva-25m-ai-wearable-personal-companion
   Also: San Francisco Business Times

39. President Trump says he called Sundar Pichai to ask to rename the Atlantic Ocean in Google Maps, but that he would “probably pass” following Pichai's pushback
   Victoria Craw / Washington Post — https://www.washingtonpost.com/politics/2026/10/22/trump-says-he-called-google-ceo-sundar-pichai-discuss-renaming-atlantic-ocean/
   > @andrewcurran_: President Trump says that Sundar Pichai talked him out of renaming the Atlantic Ocean. 'And I spoke to a brilliant guy, Sundar, he heads all of Google, he's a brilliant guy. Sergey and Sundar, totally
   > @cwarzel: you're just going about your day and you now get to read stuff like “Trump says Sundar Pichai talked him out of renaming the Atlantic Ocean” and you just have to nod and move on with your day. “Oceans
   > @goneoldie: How Sundar must have felt answering his call:
   > @cbsnews: President Trump said he called Google Maps and asked to rename the Atlantic Ocean. “No, no, no. This time I'm not doing it ... oceans are different, sir,
   > @clashreport: Trump: I called Google Maps to change the name of the Atlantic Ocean to Trump Ocean. Sundar said, “No, no, no. This time I'm not doing it.” He said, “Oceans are different, sir. They cover a lot of cou
   Also: The Verge, Mashable, The Portugal News, Fortune, HuffPost, indy100, Ukrainian National News, The A.V. Club, +1 more

40. 1Password passes $500M in ARR, up from $400M in November 2025, driven by enterprise AI coding assistants and agents, and launches 1Password for Agents
   Elias Schisgall / Wall Street Journal — https://www.wsj.com/tech/ai/1password-surpasses-500-million-in-revenue-as-ai-agents-drive-growth-903ccd4b?st=acBBcU&reflink=desktopwebshare_permalink
   > @bot: Grok Bot can now use your 1Password account. Approve the logins you want to share, and your Bot signs in for you. This new integration is rolling out to users over the next few days.
   > @dps: We're excited to bring 1Password directly into @Muse for the many people who already use it. It gives you another secure way to let Muse sign in and keep working: you approve each login and your passw
   > @xeophon: holy fucking shit we are so back
   > @trevin: I can't wait to try this out. Many of the platforms have native credential and secret storage, but having it siloed and repeated across every platform is painful to set up and maintain
   > @omarshahine: At long last. A coherent solution.
   Also: 1Password, 1Password, WinBuzzer, SammyGuru, Engadget, iClarified, Neowin

41. Microsoft says China-linked hackers used AI penetration testing tool ARTEX to compromise ConnectWise as part of a campaign targeting hundreds of organizations
   AJ Vicens / Reuters — https://www.reuters.com/technology/chinese-linked-hackers-compromise-connectwise-target-hundreds-global-attack-2026-10-21/
   > @msftsecintel: The China state-aligned threat actor Storm-0940 used the agentic AI penetration testing framework ARTEX to automate attacks targeting hundreds of organizations globally across a broad range of industr
   > @andrewcurran_: @Chahatusharma @synthwavedd It's separate. It affected aerospace and defense, automotive, chemicals, energy, financial services, government, legal, manufacturing, media, military, semiconductor, softw
   > @snlyngaas: A China state-linked actor used an AI tool to target “hundreds” of orgs globally, per Microsoft. Targets in the mil, aerospace, energy, financial services sectors, among several others: https://www.mi
   > @kimmonismus: Whats happening right now is probably way worse than the Hugging Face incident. AI-powered attacks are hitting real organizations while major platforms disclose breaches and critical flaws. - Microsof
   > @sporadica: welp. the Internet was nice while it lasted.
   Also: Microsoft Security Blog, SecurityWeek, The Record, Townhall, Security Affairs, The Information, CyberScoop
