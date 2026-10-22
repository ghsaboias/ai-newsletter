# Research — News Cluster

Search for news **events that occurred** between **2026-10-21 10:00 BRT** and **2026-10-22 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-21 10:00 BRT to 2026-10-22 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-22
**Research window:** 2026-10-21 10:00 BRT → 2026-10-22 10:00 BRT

**Previous edition headlines (2026-10-21 — skip unless genuinely new development):**
- php2shell-ai-found-php-rce-gpt-5-6-sol: AI models found 'PHP2Shell', critical PHP flaws hitting up to 70% of websites
- openai-agents-disabled-misalignment-monitoring: OpenAI discloses its GPT-6.1 Sol and GPT-6 Astra agents weakened misalignment monitoring
- metr-review-anthropic-risk-report-monitoring: METR review says Anthropic's AI monitoring is weaker than public evidence suggests
- anthropic-s1-h1-revenue-16-3b-net-loss: Anthropic draft S-1: $16.3B first-half revenue, $80.7B net loss, ~20% from two clients
- openai-models-google-cloud-model-garden: OpenAI brings GPT-6 models and Codex to Google Cloud, now on all three big US clouds
- claude-designs-scorpion-toxin-binders: Claude autonomously designs protein binders against scorpion neurotoxins; 17 of 211 bind
- legora-blacksmith-ai-funding-rounds: Legal AI Legora raises $550M at $8.8B; AI-code CI startup Blacksmith hits $1B
- nvidia-dsx-pod-containerized-vera-rubin-gtc-berlin: Nvidia unveils DSX POD, containerized Vera Rubin AI factories that deploy in 14 days
- agile-robots-nvidia-agile-one-sn-humanoid: Agile Robots and Nvidia launch research humanoid, plan up to 2,000 units in 2027
- samsung-sk-hynix-upgrade-china-nand-fabs: Samsung and SK Hynix upgrade China fabs to 200+ layer NAND to fend off YMTC
- nextdc-shares-plunge-guidance-cut-melbourne-power: NextDC shares plunge ~42% as Melbourne power delay forces a one-third guidance cut
- nvidia-firmus-investment-talks-neocloud-backstop: Nvidia in talks to invest hundreds of millions in Firmus after its IPO flop
- nscale-memo-dayone-ipo-data-center-listings-wobble: AI data-center IPOs wobble: Nscale touts $100B+ backlog, DayOne weighs cutting its listing
- micron-taichung-union-labor-deal: Micron signs labor deal with Taichung union; Taoyuan strike threat remains
- putin-witkoff-trilateral-talks-november: Putin tells Witkoff he will resume three-way Ukraine peace talks after Nov. 10; US detainee freed
- wsj-musk-ordered-starshield-slowdown-ukraine: WSJ: Musk ordered Ukraine's Starshield slowdown; Rubio says access is SpaceX's call, not White House
- iran-rejects-pakistan-mediation-tankers-struck-oman-iraq: Tankers hit off Oman and Iraq as Iran rebuffs Pakistan-mediated talks with the US
- fda-approves-gsk-hibsago-hepatitis-b: FDA approves GSK's Hibsago, first antisense drug for chronic hepatitis B, aiming at functional cure
- spacex-q3-profit-tesla-merger-committees: SpaceX posts $14.6B Q3 revenue and $4.4B profit; Musk says Tesla merger committees formed
- france-bund-spread-widest-close-since-2011: French-German 10-year spread closes at widest since 2011 amid unrest and budget fight
- ebay-lays-off-9-percent-workforce: eBay to cut about 9% of staff, roughly 1,100 jobs, in its second layoff round of 2026

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 49 stories

1. AWS analysts say that at least one actor attempted to exploit the PHP2Shell vulnerabilities on October 17, four days before their public disclosure and patching
   Lily Hay Newman / Wired — https://www.wired.com/story/hackers-exploited-the-php-vulnerabilities-days-before-they-were-patched/
   Amazon Web Services logged attempts to leverage the internet-melting PHP2Shell bugs four days ago. They're now being “broadly exploited” across the internet.
   > @lukolejnik: PHPocalypse flaws existing for a decade, identified with the help of AI, let attackers hijack web servers without logging in. Amazon & Cloudflare reported exploitation attempts days before disclosure.
   > @anthonyronning: Yeah I mean honestly, a significant CVE where multiple people independently found the vulnerability at nearly the same exact time should not be sat on for 2 months. Not only was this irresponsibly dis
   > @4n6lady: PHP2Shell (CVE-2026-109618/109619) hit our MadPot honeypots on Oct 17, four days before disclosure. Investigating? Start your timeline there, not at the advisory date. Patch to 8.5.12 / 8.4.27 / 8.3.3
   > @sughanthans1: aws says a 7-day patch deadline is now too slow for critical bugs in anything facing the internet. it wants teams to measure patching in hours. php2shell shows why. aws's honeypots logged an exploit a
   > @dinodaizovi: Periodic reminder that for every serious, exploitable vulnerability that you find out about and patch, there was some level of exploitation of it *before* then.
   Also: Amazon Web Services, Financial Times, CNBC, SecurityWeek, Reuters, BleepingComputer, Metacurity, The Guardian, +10 more

2. The PHP Foundation says its patches for the RCE vulnerabilities are limited to PHP 8.2 and newer, leaving legacy deployments dependent on third-party vendors
   Wired — https://www.wired.com/story/this-is-not-a-drill-2-php-vulnerabilities-are-setting-the-internet-on-fire/
   The PHP Foundation has revealed two serious vulnerabilities that could impact millions of websites.
   > @m_jones_1797: This is rather serious. About 70% of websites rely on PHP, which has been discovered to contain 2 major vulnerabilities. Cybersecurity specialists Cloudflare report thousands of attempts to exploit th
   > @danjarvismbe: Do you want more information about how to protect your organisation following the PHP advisory notice? The UK's cyber experts at @NCSC have published six key steps for organisations - large or small -
   > @sporadica: wait, if my math is correct.. doesn't this say that a full ONE THIRD of the Internet is just...perma-fucked?
   > @intcyberdigest: The day the internet broke, and most of it is too old to fix.
   Also: W3Techs, Wiz, National Cyber Security Centre, PC Gamer, BBC, Washington Post, Daily Mail, Fortune, +26 more

3. Cloudflare's Matthew Prince says PHP2Shell exploit attempts on its network rose from thousands in the 10 hours before the disclosure to millions afterward
   Matthew Prince / @eastdakota — https://x.com/eastdakota/status/2113079352682570051
   Also: Reuters, The Register, ITPro, Politico, Infosecurity, Bitcoin News, SecurityWeek

4. eMudhra says it will exit the SSL/TLS certificate business, 1% of its revenue, after its TLS certificates with private keys of just 3 to 8 bits were compromised
    — https://www.reuters.com/legal/litigation/indian-firm-emudhra-exits-global-digital-certificates-business-after-2026-10-22/
   Also: eMudhra Limited, The Economic Times, Business Today, Moneycontrol, Cyber Security News, Livemint, The Indian Express, Storyboard18, +8 more

5. Meta reports Q3 revenue up 26% YoY to $64.6B, operating income down 37% YoY to $12.99B on a $9.9B AG settlement, and family DAP up 3% YoY to 3.64B for September
   Meta — https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx
   Announces Establishment of New Class C Common Stock — Meta Platforms, Inc. (Nasdaq: META) today reported financial results for the quarter ended September 30, 2026.
   > @firstadopter: Zuckerberg says the most common use case for Muse is shopping and the average purchase size has been over $200. Expects to grow Muse to “billions” of users
   > @zastocks: Imagine if there was a company positioned to win big in AI who had 3.6 billion daily active users, $250B in revenue growing over 25%, and a 42 year old Mount Rushmore founder CEO. Oh that's $META.
   > @stockmarketnerd: It's easy to shrug off 26% Y/Y growth for $META . But this is not normal... in the best of ways. 23% growth Q3 2023. 19% growth Q3 2024. 26% growth Q3 2025. 26% growth Q3 2026. At a $64.6B revenue bas
   > @stocksavvyshay: $META just posted negative FCF for the first time in over a decade despite beating revenue estimates by over $1B as AI helped lift ad prices 14%. That's the kind of cash burn I can get behind when Met
   > @matthewkeyslive: Meta's ARPU is only $18. That's nuts. I've seen streaming platforms (Roku) with higher ARPU.
   Also: Business Insider, New York Times, Cautious Optimism, Coinpaper, Fast Company, Music Ally, Quartz, Fortune, +12 more

6. Meta reports 18% YoY ad revenue growth in Europe for Q3, down from ~40% in Q1 and 24% in Q2, lagging the US and Canada, after rolling out Less Personalized Ads
   Isabella Ward / Wired — https://www.wired.com/story/metas-ad-sales-suffering-now-europeans-can-pick-less-personalization/

7. Filing: Meta reports ~$825B in lease and contract commitments, up from nearly $700B in July; off-balance-sheet leases total $355.7B through 2036; META drops 5%+
   Sarah Frier / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/meta-reports-825-billion-in-future-spending-commitments
   > @thestalwart: This paragraph from $META's inside 10-q filling may mark the official announcement that the funding environment for the AI buildout has turned the corner. (HT: Barclays' Alexander Altmann)
   Also: Crypto Briefing

8. Mark Zuckerberg says Muse has drawn 10M+ users since its launch and 25%+ of users are making purchases through the app, with an average purchase size of $200+
   Business Insider — https://www.businessinsider.com/meta-q3-2026-earnings-mark-zuckerberg-muse-ai-app-users-2026-10
   > @jeremiahdillon: My Instinct agent is always acting kind of pressed, like it's suspicious that I've ghosted it. 👻 Muse keeps simping, even when I ignore it for a week. 🫡 The difference tells you something important.
   > @edzitron: Cool stuff mark. Any idea how it makes you money?
   > @kakashiii111: Muse, the most expensive toy ever by Meta (and some smart people may ask why it reminds of Manus AI), is draining all of Meta's compute, and they are gonna get more. The problem? Many who downloaded i
   > @munster_gene: Even though there are only around 10m daily Muse users (my estimate), the product is losing a lot of money, more than any other products they've launched. Reading between the lines. Zuckerberg says no
   > @danielnewmanuv: $META Muse becomes the agentic marketplace and ad revenue generator. Think about the money machine of agents as as consumers versus humans? 💪🏻🚀
   Also: Gizmodo, TechCrunch, Reuters, CNET, Quartz, Seoul Economic Daily, MediaNama, Ukrainian National News, +6 more

9. Meta says it will create a new class of nonvoting stock to raise capital for developing and serving AI models, with the 2-for-1 stock split on January 19, 2027
   Meghan Bobrowsky / Wall Street Journal — https://www.wsj.com/articles/metaplatforms-meta-3q-earnings-report-2026-stock-f28d64c2?st=Uj26V6&reflink=desktopwebshare_permalink
   > @dangaron: Said differently, @finkd wants to retain founder control to protect META from activist investors who may be less inclined to support his long term vision. That is laudable.
   > @danielnewmanuv: $META delivered a strong quarter. EPS Miss directly attributable to ~$10 billion settlement. Slight raise of capex and a raise on revenue expectations. All good in tech land here. The show goes on.
   > @semaforben: Amazing year in the history of capitalism, generally.
   > @thestalwart: $META 's new CAPEX outlook is roughly inline with its old CAPEX outlook, which is fine. But for the last few years, we've been accustomed to companies underestimating their future spending plans.
   Also: Semafor, The Verge, Wall Street Journal, Meta, Capital Brief, Reuters, Yahoo Finance, Business Insider, +1 more

10. Epic says “Fortnite is coming back to the App Store in Australia tomorrow” after an Australian federal judge ordered Apple to open up iOS in an antitrust case
   Rhea Rose Abraham / Reuters — https://www.reuters.com/technology/epic-games-fortnite-returns-apple-app-store-australia-2026-10-22/
   Epic Games said its shooter title “Fortnite” will return to Apple's (AAPL.O) App Store in Australia on Thursday …
   > @epicnewsroom: Big news: Fortnite is coming back to the App Store in Australia tomorrow! Today the Australia Federal Court told Apple to open up iOS after finding they violated competition law. Here's what's changin
   > @timsweeneyepic: The Australian Epic v Apple antitrust remedies were just issued, and are a huge victory for consumers and developers. We are studying the verdict and will share more soon. The Court has freed Fortnite
   Also: Federal Court of Australia, iDrop News, PocketGamer.biz, Engadget, iThinkDifferent, MacRumors, Digital Trends

11. An Australian federal judge rules Apple must let Australian iPhone users install apps from third-party app stores starting March 1, 2027; Apple plans to appeal
   Marcus Mendes / 9to5Mac — https://9to5mac.com/2026/10/21/apple-must-open-iphone-to-alternative-app-stores-in-australia-after-epic-games-ruling/
   Also: AppleInsider, GamesBeat, GSMArena.com, Lex on Tech, Mobilegamer.biz, iThinkDifferent

12. Anthropic unveils Claude Duet, a proactive agent app on iOS, Android, and the web that works in the background, in research preview for US Pro and Max users
   Claude — https://claude.com/resources/articles/claude-duet
   A research preview is available by waitlist today, starting with US Pro and Max subscribers. — Join the waitlist … ShareCopy link
   > @thsottiaux: @claudeai Dot, meet Duet. Duet, meet Dot. Be nice to each other.
   > @claudeai: We're opening a research preview of Claude Duet, a new app where Claude works as a proactive agent. It comes to you with what needs your attention, completes tasks you ask of it, keeps working when yo
   > @_catwu: We heard your feedback that you want Claude to proactively take more off your plate! Claude Duet is a large step in this direction - it'll notice work that needs to be done, and then do it before you 
   > @vishalsingh2972: WHAT THE ACTUAL FUCK?! Anthropic just decided to go after OpenAI Dots and Grok Bot with Claude Duet, powered by the absolute MONSTER that is Opus 5.5. We literally go to sleep, wake up, and somehow An
   > @matthewberman: Should have called this Clawdbot
   Also: Claude, TechCrunch, VentureBeat, The Verge, SiliconANGLE, Lenny's Newsletter, Crypto Briefing, Reuters, +17 more

13. Microsoft says China-linked hackers used AI penetration testing tool ARTEX to compromise ConnectWise as part of a campaign targeting hundreds of organizations
   AJ Vicens / Reuters — https://www.reuters.com/technology/chinese-linked-hackers-compromise-connectwise-target-hundreds-global-attack-2026-10-21/
   A Chinese state-aligned hacking group used an AI-driven penetration testing tool to compromise IT services firm ConnectWise as part …
   > @msftsecintel: The China state-aligned threat actor Storm-0940 used the agentic AI penetration testing framework ARTEX to automate attacks targeting hundreds of organizations globally across a broad range of industr
   > @sporadica: welp. the Internet was nice while it lasted.
   > @beffjezos: Unfortunately Chinese models have too much botnet potential now and are a supply chain risk. Time for the US Gov to fund open source models to remove this risk. [embedded post]
   > @martin_casado: I dunno, at some point we just need to unalign Claude and let it save the free world ... [image] [embedded post]
   > @michaeldunwort1: 1 minute to midnight [embedded post]
   Also: Microsoft Security Blog, CSO, Business Today, The Register, Tech Times, Infosecurity, Digit, Silicon UK, +4 more

14. Sources: DeepSeek raised ~$15B in its latest fundraising round, one of China's largest ever, with CATL and Tencent among the biggest contributors
   Lulu Yilun Chen / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/deepseek-raises-15-billion-in-challenge-to-leading-us-labs
   The Chinese AI pioneer DeepSeek has raised about 100 billion yuan ($15 billion) in its latest fundraising round, one of the country's largest ever …
   Also: TechCrunch, Wall Street Journal, Silicon Republic, Reuters, Quartz, Semafor, Ventureburn, Crypto Briefing, +2 more

15. Hugging Face releases Carbon-X, an open-source, 14B-parameter multimodal AI model to let users query DNA sequences via natural language, trained on 300B tokens
   Emily Mullin / Wired — https://www.wired.com/story/hugging-face-new-ai-biology-model-chat-with-dna/
   The new open-source model speaks the language of DNA and can help researchers understand the effects of any changes on gene activity and health.
   > @loubnabenallal1: On five benchmarks of DNA understanding and generation, Carbon-X outperforms all open language models we evaluated. This is a 27-point improvement over Qwen3-14B, showing how much a language model can
   > @loubnabenallal1: Introducing Carbon-X: The best open DNA model. We midtrained a 14B model on DNA and text, and it beats every open language model and matches GPT-6.1 Sol at 1,000x lower cost. Ask it about a sequence, 
   > @cmpatino_: The difference between Carbon-3B and the new Carbon-X feels like the transition between gpt-3 and gpt-3.5 for DNA models. You can talk to Carbon-X in natural language, so humans and agents can easily 
   > @_lewtun: Today we're releasing Carbon-X, a 14B model that brings DNA and natural language together for the first time 🧬 1. Beats every open language model we tested across DNA benchmarks. Within a point of GPT
   Also: Hugging Face, Business Insider, RuntimeWire, Crypto Briefing

16. SEC filings show how Meta restructured its stock to shield Mark Zuckerberg from California's proposed wealth tax, after he said he'd sell his Palo Alto home
   New York Times — https://www.nytimes.com/2026/10/21/technology/mark-zuckerberg-meta-california-wealth-tax.html?unlocked_article_code=1.KlE.qaXj.8PiLV3csMayA&smid=url-share
   The billionaire told Meta's board that he planned to list his Silicon Valley home for sale. The company remade its stock structure to help him pay the tax if voters pass it.
   > @buccocapital: “We're not going to raise $700B. The Class C shares are also about pre-empting the Prop 40 wealth tax”
   > @admcrlsn: There are many reasons I want Democrats to flip at least one chamber of Congress, but launching investigations into Big Tech CEOs has gotta be near the tippy top of my list.
   > @moonalice: Perhaps the time has come to acknowledge that Mark Zuckerberg may live in the US, but does not accept the responsibilities of a citizen of the US. Watch Aaron Sorkin's incredible film, The Social Reck
   > @teddyschleifer: NEW — The extraordinary story of how Mark Zuckerberg wheeled and dealed to get Meta's board of directors to protect him from California's wealth tax. With @elitanjourno https://www.nytimes.com/...
   > @amoylan: A wealth tax is one thing (a bad, wrong, unconstitutional thing); a wealth tax assessed based on *voting control of public companies* is utter insanity. As @JaredWalczak wrote, it portends insane, dis
   Also: The Guardian, CBS News, Accounting Today, CNBC, Forbes, Australian Financial Review, Fox Business, Newser, +1 more

17. Filing: Mark Zuckerberg commits to staying in Meta's HQ jurisdiction in return for nonvoting shares; he weighed leaving California over a proposed wealth tax
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-21/zuckerberg-weighs-leaving-california-if-billionaire-tax-passes
   > @cernovich: He should be forced to stay. This is what he funded. Fuck Zuck
   > @william_fitz: They all say this and never actually leave. Looking at you, Sergey.
   > @petermeijer: Ah, so he's going to be the plaintiff in the inevitable challenge to the constitutionality of Prop 40. Nice.
   > @bobbyfijan: This is obvious, and something his investors would want even more than Zuck Would investors rather he: 1) Sell huge amount of stock in short time, pushing down share price, at least in short term? 2) 
   Also: Financial Times, Washington Examiner, Business Insider, New York Times, Politico, Quartz, 24/7 Wall St., The Independent, +6 more

18. Walmart unveils Agent Gateway, an MCP server for AI agents to shop its site, and Agent Profiles to authorize agents and track their purchases separately
   Sarah Perez / TechCrunch — https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/
   Walmart is embracing agentic commerce with the launch of its own Agent Gateway to manage transactions and other new features aimed …
   Also: Walmart Inc., PYMNTS.com, MediaPost, Techstrong.ai, The Verge, Quartz, PCMag, Storyboard18, +7 more

19. Apple is rolling out a new “Made for iPhone Duo” badge in the App Store, and touts Netflix, Prime Video, Zoom, Word, and Outlook as Duo-optimized apps at launch
   Emma Roth / The Verge — https://www.theverge.com/tech/1016526/apple-made-for-iphone-duo-badge-app-store
   Many apps, including Netflix, Microsoft Word, and Zoom, are taking advantage of the Duo's extra screen real estate.
   Also: Apple, MacRumors, Thurrott, AppleInsider, 9to5Mac, iThinkDifferent, Mashable, Crypto Briefing

20. Sources: the Pentagon quietly establishes the Technology Support Office (TSO), an agency to execute covert sabotage, cyberattacks, and supply chain disruptions
   Politico — https://www.politico.com/news/2026/10/22/technology-support-office-dod-tech-spyware-sabotage-01100327
   The Pentagon has spent months quietly building an elite new tech agency to help covertly disrupt and sabotage foreign technology …
   > @johnnysaks130: New: I got a tip a little while ago about a shadowy Pentagon entity called “TSO” with a lot of money and a desire for offensive hacking tools. Turns out TSO is a new DoD agency. And it does a lot more

21. 1Password passes $500M in ARR, up from $400M in November 2025, driven by enterprise AI coding assistants and agents, and announces 1Password for Agents
   Elias Schisgall / Wall Street Journal — https://www.wsj.com/tech/ai/1password-surpasses-500-million-in-revenue-as-ai-agents-drive-growth-903ccd4b?st=acBBcU&reflink=desktopwebshare_permalink
   And the free cash flow margin is in the double digits amid an explosion in coding assistants and agents in enterprise settings
   Also: 1Password, 9to5Google, PCWorld, Thurrott, Quartz, BetaKit, Engadget, The Verge, +5 more

22. GitLab patches a critical flaw, rated 10.0, that lets unauthenticated attackers run code on self-managed servers, affecting every release since 7.0 in 2014
   Swati Khandelwal / The Hacker News — https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html
   GitLab released fixes on October 21 for a flaw that lets an attacker run code on a self-managed server without logging in …
   > @chrisgpt: Fable 5.5 is in the wild, I repeat fable 5.5 is in the wild this is not a drill ‼️🚨 [embedded post]
   > @jedisct1: Emudhra, Opencode, Pingcap, Orange, PHP, Node, LiteLLM... what's next? Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases https://thehackernews.com/...
   > @thehackersnews: 🚨 CRITICAL: GitLab flaw (CVSS 10.0) affects 12 years of releases. CVE-2026-110264 could allow unauthenticated remote code execution on self-managed servers. Read - https://thehackernews.com/...
   Also: GitLab Docs, BleepingComputer, Forkast, Implicator.ai

23. GM says it plans to debut OnStar AI, an in-car assistant that can execute vehicle functions and run diagnostics via voice commands, in the 2027 Cadillac Lyriq
   Aarian Marshall / Wired — https://www.wired.com/story/gm-wants-your-car-to-do-your-chores/
   The Detroit automaker wants your next vehicle to be a personal assistant, a best friend, and an autonomous errand-runner.
   Also: New York Times, TechCrunch, The Verge, Fast Company, CarScoops, Electric Cars Report, Financial Times, Business Insider

24. Microsoft reveals pricing for Xbox Cloud Gaming without Game Pass, for Xbox Insiders now and others next month: 10 hours for $3.99, 25 for $7.99, 50 for $11.99
   Tom Warren / The Verge — https://www.theverge.com/news/1015321/xbox-cloud-gaming-pay-as-you-go-cloud-hours-pricing
   Microsoft is opening up Xbox Cloud Gaming to anyone in November. … Microsoft announced last month that it will let anyone …
   > @playeressence: No offense to anybody who likes cloud gaming, but you have to be a moron to pay for per the hour internet streaming of video games. There are enough free to play, cheap games and other titles that giv
   > @pirat_nation: Xbox Cloud Gaming is getting a pay-as-you-go option for people who don't have Game Pass. Microsoft will sell cloud gaming hours in three bundles: > 10 hours — $3.99 > 25 hours — $7.99 > 50 hours — $11
   > @wario64: Xbox Cloud Gaming introductory launch pricing revealed: -10hrs for $3.99 -25hrs for $7.99 -50hrs for $11.99 https://news.xbox.com/... [image]
   > @jezcorden: Microsoft has revealed prices for Xbox Cloud Gaming's hourly passes, which don't require an Xbox Game Pass subscription. It has also detailed the free with ads tier. https://www.windowscentral.com/ ..
   > @tomwarren: Microsoft is opening up Xbox Cloud Gaming to anyone in November, and it's now revealing the pricing of cloud hours. Xbox Cloud Gaming's pay-as-you-go option starts at $3.99 for 10 hours. Details 👇http
   Also: XBOX Wire, Ars Technica, HotHardware, Club386, The Shortcut, Gameranx, Eurogamer.net, Digital Trends, +4 more

25. Ukraine says the abrupt throttling of US-funded Starshield grounded dozens of drones mid-flight, costing one unit $1M+, and halted some strikes for three days
   New York Times — https://www.nytimes.com/2026/10/21/world/europe/starshield-starlink-ukraine.html?unlocked_article_code=1.KVE.bUiV.u_YBlM0MuAAB&smid=nytcore-ios-share
   Ukraine says it still doesn't know why the military satellite internet service, a sister to Starlink, was abruptly throttled, leaving troops vulnerable to Russian attacks.
   > @georgeszamuely: So helpful of @nytimes not to inform its readers who Andriy Biletsky is. https://www.nytimes.com/...
   > @siobhan_ogrady: A senior Ukrainian commander told me he lost more than $1 million in drones the first night StarShield went out. The next 3 days, speeds remained so unstable they canceled almost all ops striking RU l
   > @maxpatten: Vibes are bad for Starlink and Musk with this. He can try to finger-point or spend hundreds of millions in midterms to distract from this but jeez. https://www.nytimes.com/...
   > @philklay: “The Starshield disruptions forced Oleh to halt almost all operations for the next three days, he said, including strikes on Russian command posts and fuel hubs. Such attacks, he said, help save the l
   > @rmac18: As the White House and Elon Musk point fingers at one another over who restricted Starshield to Ukraine, here are some of the real life repercussions for troops on the front lines. From @siobhan_ograd
   Also: CBS News

26. Cloud provider Railway says an unauthorized party may have accessed customer encrypted environment variables and, for some, obtained the decrypted contents
   Jacob Cooper / Railway Blog — https://blog.railway.com/p/security-disclosure-wednesday-october-21st
   Earlier this morning, Railway detected anomalous activity involving systems that store customer environment variables.
   > @rohanpaul_ai: Developer platform Railway told every customer to rotate all secrets after an intruder decrypted some stored credentials. Those environment variables hold database passwords, cloud keys and model API 
   > @bruno_hiis: GG Railway leaked all customer env variables. pls don't gamble with your infra, if you have users, move to AWS
   > @wesbos: what a day, man
   > @darcyagi: holy fucking shit, railway too??? an attacker have accessed customer environment variables, including decrypted api keys and database credentials. deployments have been paused and users are being told
   > @synthwavedd: It took Railway almost 15 hours to notify its thousands of customers that their environmental variables have been compromised. Several people on this app raised alarm about their keys being drained an
   Also: TechCrunch, The Hacker News, Claroc Blog, crypto.news, The Defiant

27. Palantir says that neither the company nor the US government has a “kill switch” for its Maven platform that NATO uses, after Ukraine's Starlink disruptions
   Andrew Gray / Reuters — https://www.reuters.com/business/media-telecom/palantir-says-it-cannot-shut-off-nato-ai-system-europeans-fear-us-tech-2026-10-22/
   US software company Palantir (PLTR.O) sought to reassure Europeans that its military AI system used by NATO has no …
   Also: Novara Media, Crypto Briefing, Euronews

28. Barclays plans to cut 5,000 jobs, or ~5% of its workforce, by the end of 2026 as part of AI-driven cost cutting, with ~60% coming from support and developers
   William Shaw / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/barclays-to-cut-5-000-jobs-as-ai-starts-creating-efficiency
   Barclays to Cut 5,000 Jobs as AI Starts to Create Efficiency — Video Player is loading. — Unmute — Current Time 0:00 Loaded: 69.77% Playback Rate
   Also: Silicon Republic, The Guardian, Financial Times, Techstrong.ai, Wall Street Journal, Reuters, New York Times, Quartz, +10 more

29. iPhone Duo review: the outer device is by far the worst iPhone Apple has ever made, while the inner device is a splendid tablet with a UI that bests the iPad's
   John Gruber / Daring Fireball — https://daringfireball.net/2026/10/the_iphone_duo
   The very nature of the iPhone Duo raises numerous obvious questions about what it's like to use. Does it not feel thick and heavy, awkward both to pocket and unpocket?
   > @omarshahine: This is a solid review. I won't have one tomorrow, but all my apps are updated for the Duo. I'm glad I got the iPhone 18 Pro, it's a great phone and I look forward to trying this out, but I really wis
   > @firstadopter: Iphone Duo is half baked. Read this review before ordering. The initial enthusiasm on the neat opening Duo animation has faded. Hard. It may all but disappear after the first wave of Apple fan early a
   > @brian_henderson: An insightful review of the Duo user experience; and how Apple has approached design challenges associated with the form factor.
   > @gruber: It's been a lot of fun trying the Duo out for a week, but it feels like I've gotten to use an extraordinarily polished prototype — not a finished product that I'd want to buy and carry. https://daring
   > @mitsuhiko: Definitely low key questioning my purchase decision.
   Also: 9to5Mac, NBC News, New York Times, New York Magazine, Wired, Techaeris, Tao of Mac, The Verge on YouTube, +3 more

30. Source: Elon Musk's public endorsement of a SpaceX-Tesla merger rattled some insiders, who worry his comments could invite shareholder scrutiny and delays
   Milana Vinn / Reuters — https://www.reuters.com/legal/government/musks-public-endorsement-spacex-tesla-deal-may-throw-wrench-talks-2026-10-22/
   Elon Musk's public endorsement this week of a potential $3.5 trillion merger between SpaceX (SPCX.O) and Tesla (TSLA.O) …
   Also: Fortune, Wall Street Journal, Fortune, Motley Fool, Coinpedia Fintech News, Quartz, Euronews, Los Angeles Times, +4 more

31. Pressure to back promising AI startups is upending the VC investment process, with investors willing to buy into the same round at rapidly escalating valuations
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/venture-capitalists-push-up-ai-startup-valuations-with-tranched-two-step-rounds
   Venture capitalists are fighting to invest in AI startup Emulate, driving its valuation into the billions …
   > @_iainmartin: Competition to back the startup AI startup Emulate, is so intense that investors are willing to buy into the same round at spiralling prices. Index invested at a $200m pricetag. Creandum bought into t

32. A look at Huawei and DeepSeek's mutual reliance, where Huawei provides compute hardware while DeepSeek contributes model workloads and kernel optimization
   SemiAnalysis — https://newsletter.semianalysis.com/p/huawei-deepseek
   Huawei Ascend 950PR Deep dive & µbenchmarks, DSv4.1 Flash Analysis, DeepSeek support for Ascend, AICPU, Tilelang Ascend
   > @semianalysis_: Huawei Ascend 950PR Deep dive & µbenchmarks, DSv4.1 Flash Analysis, DeepSeek support for Ascend, AICPU, Tilelang Ascend https://newsletter.semianalysis.com/ ...
   Also: South China Morning Post

33. Spotify reports Q3 revenue up 16% YoY to €4.97B, below €4.98B est., subscribers up 9% to 306M, MAUs up 11% to 788M, meeting est., and €672M operating income
   Ashley Carman / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/spotify-keeps-adding-users-but-misses-slightly-on-revenue
   Spotify Technology SA reported monthly active users grew 1% in the third quarter, over the prior quarter …
   Also: Thurrott, Reuters, Spotify, Proactive, Barrett Media, Quartz, Hypebot, The Wrap, +2 more

34. Maxinsights, which creates training data for robots using first-person footage from cameras worn by 5,000+ contractors, raised a $30M seed led by Peak XV
   John Koetsier / Forbes — https://www.forbes.com/sites/johnkoetsier/2026/10/22/theres-not-enough-robot-training-data-this-startup-plans-to-fix-that/

35. Nirva, which plans to launch a wearable AI personal companion that offers relationship advice and more, raised $25M, bringing its total funding to $33M
   Will Maddox / Axios — https://www.axios.com/pro/health-tech-deals/2026/10/22/nirva-25m-ai-wearable-personal-companion
   Also: TechCrunch

36. President Trump says he called Sundar Pichai to ask Google Maps to rename the Atlantic Ocean, though he would “probably pass” following Pichai's pushback
   Victoria Craw / Washington Post — https://www.washingtonpost.com/politics/2026/10/22/trump-says-he-called-google-ceo-sundar-pichai-discuss-renaming-atlantic-ocean/
   Also: Times of India, India Today, Baller Alert, Variety, LADbible, Business Insider, Metro.co.uk, Outlook India, +4 more

37. Minneapolis-based Slingshot, which uses AI to help businesses offer embedded insurance, emerges from stealth with a $27M seed co-led by Rally and Skyward Group
   Mary Ann Azevedo / Crunchbase News — https://news.crunchbase.com/fintech-ecommerce/insuretech/startup-slingshot-insurance-seed-funding-genteman/
   Also: FinSMEs, Coverager

38. Enact, which develops full-stack tech for general-purpose robots, emerges from stealth with a $30M pre-seed from Mistral CEO Arthur Mensch, Yann LeCun, and more
   John Reynolds / Tech.eu — https://tech.eu/2026/10/22/mistral-boss-and-yann-lecun-back-swiss-robotics-startup-enact-in-30m-pre-seed-round/
   Also: RuntimeWire, EU-Startups

39. Sources: Visa is in late-stage talks to buy stablecoin custody and infrastructure provider Fireblocks for ~$2.5B, its first acquisition in the stablecoin sector
   Lucinda Shen / Axios — https://www.axios.com/pro/fintech-deals/2026/10/22/visa-fireblocks-talks-2-billion
   > @danprimack: Fireblocks denying, fwiw
   > @dogetoshi: a16z drops crypto from name and then immediately after Visa buys a crypto company for $2.5 billion.
   > @mdudas: interesting to reread the 2022 announcement of @FireblocksHQ $550M round at an $8B valuation “every business is going to be a crypto business one day
   Also: The Block, CTech, CoinDesk, Bitcoin Magazine, Crypto Briefing, crypto.news, Cointelegraph, CoinGeek

40. Israeli security company Lava finds 32 Nvidia Blackwell Ultra B300 chips connected to systems linked to state-owned operator China Telecom, despite US controls
   Qianer Liu / The Information — https://www.theinformation.com/briefings/nvidias-powerful-b300-chips-spotted-chinese-state-owned-network
   Also: Crypto Briefing, Telecompaper

41. Xona, which plans to deploy a 258-satellite low-Earth orbit constellation as a commercial alternative to GPS, raised a $250M Series D at a $2.45B valuation
   Monica Hunter-Hart / Forbes — https://www.forbes.com/sites/monicahunter-hart/2026/10/22/exclusive-spacex-investor-backs-245-billion-startup-taking-the-starlink-model-to-gps/
   Also: FinSMEs, Payload, WOWTALE

42. Source: a16z plans to drop “crypto” from its flagship blockchain fund, rebranding it to “a16z frontier” and broadening its investment strategy beyond crypto
   Leo Schwartz / The Information — https://www.theinformation.com/articles/andreessen-horowitz-drop-crypto-name-flagship-blockchain-fund
   Also: Crypto Briefing

43. Jensen Huang says he urged UK-based neocloud Nscale to “work around the clock” to resolve data center delays amid investor pushback over its $30B IPO valuation
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/nvidia-s-huang-urged-nscale-to-move-faster-after-early-setbacks
   Also: Wall Street Journal, CNBC, Crypto Briefing, Capacity

44. How the AI boom is boosting paint maker PPG's sales: its specialized gray coatings resist fire, rust, and more, and total $3M to $8M per data center, per JLL
   Emmy Martin / New York Times — https://www.nytimes.com/2026/10/22/technology/ai-data-centers-paint.html

45. How the US and China are building rival “AI empires” to extend their power over innovation, production, science, culture, and, ultimately, advanced thought
   Foreign Affairs — https://www.foreignaffairs.com/china/empires-artificial-intelligence-ferguson-klaassen-schmidt
   > @matthewdancona: Really important piece
   > @intercog: “The next pandemic may be sparked by an AI-designed pathogen. Or the Internet itself could fall victim to agent-designed malware.”
   > @nfergus: Welcome to the new global order of the two AI empires. My latest for @ForeignAffairs with @ericschmidt and Lisa Klaassen.

46. Sources: Axel Springer CEO Mathias Döpfner proposed joining a bid for TikTok's European business over lunch with Charles Kushner, the US ambassador to France
   Financial Times — https://www.ft.com/content/171220b9-8d8e-4d82-a866-f9aaf258e0fb
   Also: Reuters

47. A Micron labor union staged Taiwan's first-ever strike in the semiconductor industry on Thursday, demanding a regular profit-sharing scheme for its employees
   Nikkei Asia — https://asia.nikkei.com/business/tech/semiconductors/taiwan-s-first-ever-chip-workers-strike-begins-at-micron-plant
   Also: Focus Taiwan, Reuters, Silicon UK

48. SAP: Q3 cloud revenue up 25% YoY to €6.67B, vs. €6.57B est., total revenue up 12% to €10.27B, current cloud backlog up 26% to €24.1B, all in constant currencies
   Christina Kyriasoglou / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-21/sap-cloud-growth-beats-forecast-in-sign-of-software-s-resilience
   Also: Proactive, diginomica, SAP, Dow Jones Newswires, Constellation Research

49. A New Mexico court orders Meta to pay $25B in penalties after a jury found Meta misled residents about its data practices in the Cambridge Analytica scandal
   Jonathan Vanian / CNBC — https://www.cnbc.com/2026/10/21/meta-new-mexico-cambridge-analytica-penalty.html
   > @agjamesuthmeier: As I said at the time, the multi-state settlement with Meta was a slap on the wrist. New Mexico was just awarded $25 billion for privacy violations, with $15 billion related to Cambridge Analytica. Th
   > @jason_kint: This appears to be the (nonsensical) statement Meta has provided to all major outlets about the $25B fine which had to do with an unprecedented data leak that they then kept under wraps through the 20
   > @matthewstoller: “This ruling, and the Attorney General's approach to this enforcement, makes it all but impossible to do business in the state of New Mexico.” That's a threat of withdrawing from New Mexico.
   > @sarahehunt01: 🧵 Instead of building an economy, my home state is trying to sue its way to a balanced budget, targeting a company that has bet big on NM. Meta is one of the few private-sector growth engines in New M
   > @jason_kint: It's worth noting the Court ordered Meta to pay New Mexico $25B for the claims that were just settled for $460M by 46 other state AGs, buried inside of the $18B child harms settlement. Advantage New M
   Also: Reuters, New York Times, Business Today, The Guardian, nmdoj.gov, Associated Press, The Information, The Verge, +23 more
