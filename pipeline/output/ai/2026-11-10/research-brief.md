# Research — News Cluster

Search for news **events that occurred** between **2026-11-09 10:00 BRT** and **2026-11-10 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-11-09 10:00 BRT to 2026-11-10 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-11-10
**Research window:** 2026-11-09 10:00 BRT → 2026-11-10 10:00 BRT

**Previous edition headlines (2026-11-09 — skip unless genuinely new development):**
- openai-11b-first-close-1-25t-valuation: OpenAI closes $11B first tranche at $1.25T valuation, below its $1.4T opening ask
- deepmind-ai-agents-rsa-1024-weaknesses: Google DeepMind AI agents find two weaknesses in legacy 1024-bit RSA; RSA-2048 unaffected
- deepseek-harness-1-54m-daily-users: DeepSeek says its open-source agent app Harness hit 1.54M daily users, burning 92T tokens a day
- trump-ai-guardrails-60-minutes-caissi-white-house: Trump says he 'doesn't mind guardrails' on AI as AP reports US safety center drifts to White House
- apple-ternus-federighi-agentic-siri: Gurman: Apple CEO Ternus pushes Federighi to speed AI roadmap; agentic Siri could come in 2027
- tencent-yao-shunyu-ai-bio-risk-closed-models: Tencent AI chief Yao Shunyu warns AI bio abilities will soon be able to do harm
- openai-biobasicsbench-wet-lab-agents: OpenAI's BioBasicsBench tests AI agents on raw wet-lab data; GPT-6 Astra scores 66.7%
- nvidia-board-probe-huang-affair-spy: Nvidia board opens independent probe as Jensen Huang admits affair with suspected Chinese spy
- google-tpu-8tx-8i-max: Google adds TPU 8tx for confidential workloads and TPU 8i Max for long-context AI
- anthropic-onepwr-gas-generators-3-4b: FT: Anthropic paid $3.4B for 1.7 GW of gas-fired generators from OnePWR for data centers
- tsmc-3d-dram-nvidia-request: The Information: TSMC weighs making 3D DRAM memory at Nvidia's request; shares jump 6%
- amsterdam-microsoft-data-center-protest-arrests: Dutch police arrest up to 200 after protesters storm Microsoft data center site in Amsterdam
- bytedance-ceara-data-center-second-phase: Bloomberg: ByteDance weighs second phase of Ceará data center, larger than $10B first phase
- us-task-force-iron-gate-trump-iran-strikes-unlikely: US opens Task Force Iron Gate on Iran's land routes; Trump calls new strikes 'highly unlikely'
- us-october-jobs-165k-december-fed-hike-odds: US adds 165,000 jobs in October, nearly triple forecasts, lifting odds of a December Fed hike
- europe-joins-abu-dhabi-ukraine-talks-kremlin-objection: Europe to join US-led Russia-Ukraine talks in Abu Dhabi despite Kremlin objections
- fda-investigates-zolgensma-cancer-risk-gli1: FDA investigates cancer risk from Novartis gene therapy Zolgensma after vector DNA found in tumors
- nasa-clps-2-10b-moon-base-promise-nuclear-rover: NASA picks eight firms for $10B Moon lander contract and greenlights nuclear PROMISE rover
- credit-agricole-banco-bpm-merger-proposal: Crédit Agricole proposes merging its Italian unit with Banco BPM to form Italy's No. 3 bank
- coinbase-occ-final-national-trust-charter: OCC gives Coinbase final approval for a federally chartered national trust bank

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 43 stories

1. Trump says the FBI is “looking into” Jensen Huang's affair, and the Nvidia CEO told him that he “had absolutely no idea that the person in question was a spy”
   Associated Press — https://apnews.com/article/china-denies-spy-jensen-huang-nvidia-3345b9f05c54d58909e88f6dcb9c1cd8
   President Donald Trump said Monday that Nvidia CEO Jensen Huang should not worry about the FBI looking …
   > @elleianagreen: NEW: Asked if the government is investigating the chipmaker's CEO Jensen Huang, President Donald Trump said that the FBI is “looking into it in terms of something else.” Latest for @politico here: htt
   > @khoavuumn: The fact that two Huangs are involved in an affair, but only one takes the blame is commonly known as Jensen's Inequality.
   > @amitisinvesting: Trump: “I spoke to Jensen today. He told me he had no idea that woman was a spy, and I really believe him.”
   > @onestpress: AP: Trump said Monday that Nvidia CEO Jensen Huang should not worry about the FBI looking into his affair with a Chinese government agent. He called Huang a “very honorable man.”
   > @asialens: BREAKING Donald Trump says @FBI is “looking into” @JensenHuang who had an affair with a woman that US intelligence officials believe was a #ChineseSpy
   Also: NBC News, Washington Post, BBC, RTÉ, Wall Street Journal, Reuters, Semafor, New York Post, +27 more

2. Sources: Jensen Huang and Alice Huang's relationship dates back to at least 2023, facilitating $7.5B+ in Nvidia chip shipments via Chinese companies since then
   The Information — https://www.theinformation.com/articles/jensen-huangs-yearslong-ties-alice-huang-enabled-nvidia-chip-sales-china
   The relationship between Nvidia CEO Jensen Huang and Alice Huang, the woman that the U.S. government reportedly identified …
   > @garymarcus: $7.5B in Nvidia chips that could instead have gone to US companies. https://www.theinformation.com/ ...
   > @baldingsworld: There is zero chance this was not at least unofficially sanctioned even if it originated inside a company. You simply don't move money like that without getting the state involved in China. Zero chanc
   > @robert_spalding: This is getting worse
   > @jingyanghk: How exactly did the two Huangs met? We find out that Alice's husband Kang Wei 康伟 got to know Jenson in the 2010s through gaming businesses.
   > @jingyanghk: Alice & Jensen have known each other since at least 2023. By 2023, when Alice launched her chip biz with no prior background in tech, she quickly established her credibility by boasting her chuminess 
   Also: Business Insider, CNBC, Washington Post, Reuters, South China Morning Post, CTech, Business Today, New York Times, +7 more

3. Jensen Huang's affair shines a spotlight on Nvidia's weak board and opaque succession planning at what has become the world's most important company
   Semafor — https://www.semafor.com/article/11/09/2026/with-a-weak-board-and-no-successor-nvidia-confronts-a-governance-crisis
   Nvidia CEO Jensen Huang's spy scandal shines a spotlight on thin corporate governance and opaque succession planning at what has become the world's most important company.
   > @edgecliffe: With a weak board and no successor, Nvidia confronts a governance crisis - our latest on a corporate governance crisis for the ages, with @lizrhoffman https://www.semafor.com/...
   > @fredsoda: look at these trial balloons being floated to signal jensen being pushed out while this is heavily coordinated, it has the appearance of being “natural
   > @thestalwart: Kinda surprised by how modest the market reaction was today. Here is the crown jewel of the AI ecosystem, both in terms of its technology, and also its ability to finance various partners, and we real
   > @lizrhoffman: Thinking about this column today
   > @smokinpowell: Ironically, if you screened for large cap companies with exactly these attributes, levered up, and bought hand over fist...you'd be one of the best money managers of the past decade.
   Also: The Guardian, Wall Street Journal, Fortune, Times of India, The National Law Review, heise online, Wall Street Journal, The Standard, +1 more

4. Short seller Culper Research's May report, which flagged Jensen Huang's relationship with Alice Huang as “uncomfortably close”, is resurfacing on social media
   Sarah Perez / TechCrunch — https://techcrunch.com/2026/11/09/a-short-seller-flagged-nvidia-ceos-ties-to-a-suspected-chinese-spy-six-months-before-the-scandal/
   Six months before the Nvidia spy scandal emerged, the New York-based short seller firm Culper Research …
   > @jerrycap: “corporate-governance/deception issue
   > @inafried: Worth reading, from May ...
   > @sabriprovenzani: And the plot thickens
   > @lhfang: This research firm deserves credit, they used publicly available Singaporean business filings to pretty much nail the entire Alice Huang / Chinese front company buying NVIDIA chips scheme back in May 
   > @garymarcus: memo more people should have read (via @edzitron)
   Also: Wccftech, International Business Times, Business Today, ChinaTalk, PC Gamer, Livemint, The Stanford Daily, abc7NY, +12 more

5. Analysis: Nvidia's 2025 figures to the US government undercounted chips sold to Megaspeed via partners by 50K; Nvidia did not give Bloomberg an exact figure
   Mackenzie Hawkins / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-09/nvidia-intervened-in-us-probe-of-megaspeed-chip-smuggling
   Nvidia Corp.'s general counsel intervened in a US government probe of suspected smuggling of AI chips by Megaspeed International …
   > @alecstapp: And now we have reporting from Bloomberg claiming that NVIDIA was specifically inquiring about the Chinese spy when they tried to intervene in a Commerce Department probe. Imagine what else Congressio
   > @ryanfedasiuk: By @business: “Nvidia's tabulations, as relayed to the US government, undercounted the number of chips it had sold to Megaspeed via hardware partners by 50,000 units, according to trade records analyz
   > @menakadoshi: It gets worse. Nvidia's general counsel intervened in a US government probe of suspected smuggling of AI chips by Megaspeed International. https://www.bloomberg.com/...
   > @edzitron: Culper estimates that over 20% of NVIDIA's Fiscal 2027 revenue - around $43.2 billion - was “driven by China via illegal GPU diversion and Southeast Asian intermediaries.” If this is the case, Megaspe
   Also: Stratechery, Wall Street Journal, Fortune, Channel NewsAsia, Silicon UK, Seoul Economic Daily, Reuters, Alhurra

6. Sources: a US Commerce Department investigation into Megaspeed for allegedly smuggling Nvidia chips to China was transferred to the DOJ after Nvidia intervened
   New York Times — https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html?unlocked_article_code=1.PFE.kx0T.Y85ccrbdDRP8&smid=url-share
   > @niubi: Nvidia General Counsel Teter looks to be in deep doodoo
   > @matthewstoller: It's obviously a criminal conspiracy in one of America's biggest corporations and not a question of one guy having an affair.
   > @geoffrey_cain: Another twist! Commerce Dept. Chip Inquiry Was Halted After Nvidia Intervention https://www.nytimes.com/...
   > @jerusalemdemsas: Let me get this straight: 1) NVIDIA CEO is in a relationship with a Chinese spy 2) Said Chinese spy worked for a company under investigation for smuggling banned chips to China 3) NVIDIA's top lawyer 
   > @chold: Huang has to be the guest picker for College Gameday this week
   Also: The Information, Bloomberg, Yahoo Finance, Los Angeles Times, Semafor, WinBuzzer, Inc, Wall Street Journal

7. Sources: Jensen Huang hired crisis communications firm Heller as early as October 2025; an NYT report in October 2025 on his Megaspeed ties caused tensions
   Lauren Goode / Wired — https://www.wired.com/story/nvidia-ceo-jensen-huang-hired-a-pr-firm-known-for-handling-sex-scandals-last-year/
   > @jerrycap: If Jensen knew the relationship created a serious conflict, hired outside crisis advisers, allowed NVIDIA to publicly characterize the relationship as routine business, and did not disclose the romant
   > @tenreirodaniel: I feel like a PR firm known for handing sex scandals is by definition not the right PR firm to handle a sex scandal
   > @alpaysh: zuck's dedication to his Wife saved him from the Epstein files and getting honeypotted. total wifeguy victory
   > @cristinculver: Maybe it's just me but ‘Give em Heller’ is exceptional branding for a crisis comms firm.
   > @rynorhn: what a fucking disappointing way for jensen huang to damage his reputation. you spend decades building one of the most important companies in the world, earning people's respect, trust, and admiration
   Also: The Verge, CNBC, New York Times, Semafor, Finbold, India Today, The Asia Business Daily, X (formerly Twitter)

8. Sources: Jensen Huang resisted internal Nvidia talks about succession planning, which took place over the years; many of the 10 board members are close to him
   New York Times — https://www.nytimes.com/2026/11/10/technology/jensen-huang-nvidia-board.html
   Also: The Guardian, Forbes

9. Sources: Nvidia board member and ex-Cooley CEO Stephen C Neal will probably lead the probe; Nvidia's corporate docs make no reference to “succession planning”
   Financial Times — https://www.ft.com/content/0b20d24a-580a-41df-a5f3-7f7dba4f552f
   Also: Bloomberg, New York Times, Wall Street Journal, CNBC

10. Nvidia drops 4.3% after its board opens an investigation into Jensen Huang; the company originally dismissed the interactions as “nothing unusual or unexpected”
   Demetri Sevastopulo / Financial Times — https://www.ft.com/content/fa3b0a35-1aa9-4f31-97b4-e4c599e3e654
   > @shakeelhashim: Note that Nvidia's spokesman John Rizzo has put out multiple statements in recent weeks that we now know are false. Unclear, of course, if he believed them to be true at the time.
   > @jason_kint: Unfortunately, everyone in DC seemed to be distracted or sleeping when 1) whistleblower alleged Meta worked with China on censorship and 2) Meta's internal audit report later showed they made most Ame
   > @chrisrmcguire: ...To give an idea how bad this is: imagine if FBI agents were in the middle of a secret, long-running criminal investigation into a company, and FBI leadership discussed the status of that investigat
   > @patrickmcgee_: Hi Emily, Did you ask him about Beijing's ambitions to take over Taiwan? He never seems to be asked about this.
   > @anaswanson: Nvidia said that it had the permission of Commerce official Jeff Kessler to reach out to the agents. The agents were alarmed that Nvidia had invoked the name their superior.
   Also: Associated Press, CNBC, CNBC, New York Magazine, Politico, The Hill, Associated Press, Telegraph, +8 more

11. Anthropic launches its IPO roadshow, saying the company and shareholders plan to sell 825M Class A shares at $70 to $78 each, listing on the Nasdaq under ANT
   Anthropic — https://www.anthropic.com/news/roadshow-launch
   Today Anthropic, PBC launched the roadshow for its proposed initial public offering of its Class A common stock.
   > @lesliepicker: A bit of Anthropic roadshow color, according to people familiar with the matter - Expected to price next Wednesday, begin trading on Thursday (Nasdaq-listed) - I'm told they're already covered from in
   > @kimmonismus: Official: Anthropic has launched the roadshow for its proposed IPO, offering 825 million shares at $70 to $78 each. That implies an estimated fully diluted valuation of roughly $1.24 trillion to $1.38
   > @zephyr_z9: From $2T to $1T Considering AI infra stocks went down by 50% in October, this is quite fair
   > @tokengremlin: One day after Fable 5.2, Anthropic launches an IPO that could value it at $1.3 trillion, what a week to be Anthropic.
   > @himanshustwts: ANT shares are expected to be priced below $100 at the IPO. About 97% of the base offering consists of shares sold by Ant itself and existing investors are selling 23.65M shares, gross valued at ~$64B
   Also: Wall Street Journal, Bloomberg, Reuters, The Information, Axios, CoinDesk, BBC, Quartz

12. IPO prospectus: Anthropic's IPO is set to raise up to $64.4B, and the company will also raise $26B via cornerstone investors like Google, AMD, and Nvidia
   Echo Wang / Reuters — https://www.reuters.com/business/anthropic-ipo-raise-much-644-billion-latest-draft-prospectus-shows-2026-11-10/
   Anthropic is targeting a valuation of up to $1.02 trillion in its landmark U.S. IPO, its filing showed on Tuesday …
   Also: Capital Brief, Telegraph, The Decoder, The Defiant, TheEnergyMag, The Straits Times, Finimize

13. Filing: Anthropic's IPO could give it an up to $1.405T valuation on a fully diluted basis, up from the $965B valuation during its $65B Series H announced in May
   Ashley Capoot / CNBC — https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html
   Anthropic said it will offer 825 million shares in its upcoming IPO at a price range between $70 to $78 per share …
   > @azeem: The $ANT ipo will go ahead at a valuation of $1 trillion, so about 50% below what was mooted in the summary.; and raising what looks like $60-65bn. Given the market correction since the summer, that m
   > @danprimack: Anthropic math: Top market cap is basically $1 trillion, but the fully diluted is closer to $1.4 trillion.
   > @danprimack: Anthropic IPO terms are out. And.... this is WAY smaller than had been expected. I mean — still a trillion dollar hope, but this def reflects concerns about the broader AI trade.
   Also: The Defiant, Reuters, New York Times, Times of India, Washington Post, Financial Times, Wall Street Journal

14. Emails: Anthropic sent bankers a copy of its IPO filing showing plans to raise up to ~$69B, then followed up saying the pricing details were inaccurate
   Echo Wang / Reuters — https://www.reuters.com/business/anthropic-aims-raise-up-693-billion-blockbuster-ipo-2026-11-10/
   > @dmesg: OK but legitimately how do you send out yhe wrong prospectus? What's the process failure here? https://www.reuters.com/...
   > @wallstengine: Anthropic is seeking to raise up to $69.3B in its IPO, below earlier expectations of $80B-$100B, Reuters reports. It plans to sell 866.7M new shares at $70-$80 each, with all proceeds going to the com
   > @anikacodes: Anthropic IPO targeting $69.3B on Nasdaq ($ANT). Google and Nvidia already lining up for allocations. Buying exactly 1 share so I can legally tell Claude it works for me.https://www.reuters.com/...
   > @edzitron: Stupid goofy fuckers the whole way down. Jensen can't help but fall for a Chinese spy after years of GPU smuggling, Sam Altman says it's bad if regular people get RAM, Anthropic sent incorrect numbers
   > @edzitron: Bankers love this
   Also: Quartz, Times of India, Nairametrics, RuntimeWire

15. Anthropic releases Mythos 5.2 and Fable 5.2, saying they are “best for the most ambitious, open-ended technical work”, with outputs up to 30% faster than 5.1
   Anthropic — https://www.anthropic.com/claude-fable-and-mythos-5-2
   We've upgraded Claude Fable and Claude Mythos—models that are designed to tackle the most daunting technical challenges.
   > @claudeai: A team of 1,000 Fable 5.2 agents fully formalized Fermat's Last Theorem in 30 hours, translating the proof into a language a computer can check step by step. With the same setup, Opus 5.5 completed on
   > @claudeai: Introducing Claude Fable 5.2 and Claude Mythos 5.2, designed to tackle the most daunting technical challenges. They're capable collaborators on ambitious projects in many fields, and show improvements
   > @kimmonismus: LETS GO: Anthropic just announced Claude Fable 5.2 and Mythos 5.2. And its insane! According to the company, both outperform Opus 5.5 in almost every capability it evaluated, including coding, reasoni
   > @bcherny: We wanted to do more for the people who've been with us the longest. So with Fable 5.2, the longer you've been subscribed, the more Fable resets you get.
   > @alexalbert__: I really love using Fable 5.2. On big, open-ended work it feels like a major step above Opus 5.5. A few tips for getting the most out of it: - Ask what's wrong with your idea before it builds anything
   Also: Help Net Security, Silicon Republic, Mashable, Implicator.ai, VentureBeat, Gizmodo, TechCrunch, TechCentral.ie, +9 more

16. Anthropic says during prerelease testing Mythos 5.2 and Fable 5.2 formalized the proof of Fermat's Last Theorem and solved two open black hole physics problems
   Jay Peters / The Verge — https://www.theverge.com/ai-artificial-intelligence/1030005/anthropic-claude-fable-mythos-5-2?view_token=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IlZxTEU5c3dWWmMiLCJwIjoiL2FpLWFydGlmaWNpYWwtaW50ZWxsaWdlbmNlLzEwMzAwMDUvYW50aHJvcGljLWNsYXVkZS1mYWJsZS1teXRob3MtNS0yIiwiZXhwIjoxNzk0NjgzNDYyLCJpYXQiOjE3OTQyNTE0NjJ9.2LVCU8fAafdd4rkRbz6XCtLFvyK6Lugr0vpJRrELfpo&utm_medium=gift-link
   > @garrisonlovely: By far the most alarming score on here is from a benchmark that doesn't get much attention. The Remote Labor Index gives freelance projects in a huge range of fields to humans and AI agents. When it w
   Also: Bloomberg, Gulf News, Business Standard, Hindustan Times, The Indian Express, Blockchain.News

17. Anthropic's Fable 5.2 represents “Jagged AGI” that matches human expert levels on select tasks like game design, but lacks self-directed judgment and taste
   Ethan Mollick / One Useful Thing — https://www.oneusefulthing.org/p/fable-52-and-jagged-agi
   > @emollick: I had early access to Fable 5.2 for a bit & I think it crosses the line into being a sort of Jagged AGI. Here, I have it launch a business, do academic research, hack hardware, build 3D models & more.
   > @oxshamss: Fable 5.2 is actually insane. One short prompt. Look at the result.
   > @emollick: In one of my favorite experiments, I told Fable 5.2 to build an endless, hands-off journey through 3D worlds linked by portals. 25,000 agents created over 450 worlds inspired by books, art, places, al
   > @policytensor: They're gonna make power like the Houthis!
   > @matdryhurst: Of course impressive and also I think telling that expressions of AGI and creativity always default to a kind of Terrence Malick and Powers of Ten awebait I find that mode of expression highly unconvi
   Also: The Neuron, Latent Space

18. Anthropic prices Fable 5.2 and Mythos 5.2 at $8/1M input and $40/1M output tokens, down 20% from 5.1; fast mode costs $16/1M input and $80/1M output tokens
   Frederic Lardinois / The New Stack — https://thenewstack.io/anthropic-fable-coding-upgrade/
   > @claudedevs: Fable 5.2 is now available in the Claude Platform and Claude Code. It's up to 30% faster than Fable 5.1, and costs $8/$40 per 1M tokens, down from $10/$50.
   > @laurensnys: lol fable max on a linear scale
   Also: Computerworld

19. Apple begins offering additional AI access via one-time $50 “intelligence usage packs” when users meet monthly usage caps, starting in its Creator Studio apps
   Ryan Christoffel / 9to5Mac — https://9to5mac.com/2026/11/09/apple-launches-50-intelligence-usage-packs-for-select-ai-features/
   Apple has said it will eventually charge for expanded usage of select AI features.
   > @vicvijayakumar: @Techmeme @iryantldr And what are people even using to hit monthly usage caps...
   > @quinnypig: You'd think they'd make the thing work before trying to charge extra for it, but what do I know? [embedded post]
   > @jdluk87: Enshittification is starting for Apple as well. Fantastic
   > @vincedotpng: @9to5mac @iryantldr they should have to pay me $50 to use apple intelligence
   > @stevemoser: John has a interesting overview on the betas of the updated Creator Studio apps. Most interesting to me is how Apple is moving toward usage-based billing for AI features with the ability to buy more t
   Also: PCMag, Apple Support, Livemint, The Apple Post, PhoneArena, Business Today, Moneycontrol, Notebookcheck, +5 more

20. Google DeepMind researchers used agentic AI framework AlphaProof Code to verify the Signal protocol's cryptographic guarantees, in a four-week proof-of-concept
   Lily Hay Newman / Wired — https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/
   DeepMind researchers were able to formally verify that the widely used encryption protocol works as intended. Their stretch goal?
   Also: Google DeepMind, 9to5Mac, Axios, The Register, google-deepmind.github.io, MadRobot, Forbes

21. AI infrastructure provider Fireworks says hackers accessed some customers' datasets, incomplete model weights, and billing information over the past month
   Anna Tong / Forbes — https://www.forbes.com/sites/annatong/2026/11/09/fireworks-cyberattack-exposes-customer-data-and-ai-models-as-fallout-widens/
   Two customers told Forbes they had already substantially moved their business off Fireworks' systems, with one describing a series …
   > @nmasc_: NEW: Fireworks is working with Notion, Cursor and other customers to contain a security incident involving compromised customer data — marking its second breach in just weeks. https://www.bloomberg.co
   > @annatonger: New: Popular open source provider Fireworks has had its customer data and AI models hacked. One customer described a series of ‘very bad hacks’ and poor communication from @FireworksAI_HQ (w/ @RashiSh
   Also: Fireworks AI, The Information, Bloomberg, BleepingComputer, Seeking Alpha, Cyber Security News, The Neuron

22. Filings: Moonshot signed a deal in August to rent 32 China-based Super Micro servers with Nvidia B300, the most powerful AI chip, possibly in breach of US rules
   Andy Lin / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-10/moonshot-rents-nvidia-s-top-ai-chips-in-china-documents-show
   Moonshot AI accessed a trove of Nvidia Corp.'s most advanced chips this summer, according to documents filed with Beijing regulators …
   > @niubi: Moonshot AI accessed a trove of Nvidia's most advanced chips this summer, according to documents filed with Beijing regulators, highlighting the Chinese AI champion's reliance on American hardware des
   > @sujinyan6: Beijing filings reviewed by Bloomberg show a loan to buy 32 Supermicro B300 servers in China, earmarked for Moonshot's main operating unit. Moonshot says it had nothing to do with the deal, and Nvidia
   > @g2aistack: What chip did you think K3 was running on, then?
   > @hotaisle: of course it is smci...
   > @theobearman: This was a $65m B300 cluster, priced at a 350% markup to the U.S. price, located INSIDE CHINA.
   Also: The Standard

23. The White House picks Palantir CISO Michael LoSapio to lead the DHS' Cybersecurity and Infrastructure Security Agency, replacing Acting Director Nick Andersen
   Reuters — https://www.reuters.com/world/white-house-nominates-palantirs-losapio-lead-homeland-securitys-cyber-agency-2026-11-09/
   The White House said on Monday it has nominated Michael LoSapio to be the director of the US Department of Homeland Security's Cybersecurity …
   Also: CyberScoop, Nextgov/FCW

24. Meta releases Muse Ember, its smallest and most cost-efficient AI model yet, saying it delivers more intelligence per dollar than Haiku 5.5 and GPT-6 Luna
   Russell Brandom / TechCrunch — https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/
   Meta Superintelligence Lab released a new AI model on Monday called Muse Ember, the lab's lightest and most cost-efficient AI model yet.
   > @finkd: Releasing Muse Ember today — our smallest model that delivers higher intelligence per dollar than others in its class. Built for token-heavy work that agents repeat all day: tool calls, coding subtask
   > @valsai: Meta's Ember is the cheapest model on the Vals Index at just $0.15 per test outperforming both Haiku 5.5 and GPT-6 Luna. It also finishes tests in about 15 minutes, making it the fastest model in the 
   > @artificialanlys: Meta's newest model Muse Ember scores 36 on the Artificial Analysis Intelligence Index, matching Claude Haiku 5.5 (max) at a third of the Cost per Task Muse Ember is Meta's newest efficient-tier model
   > @alexandr_wang: 1/ announcing our smallest, most efficient little model is here: muse ember 🔥 built for work that agents repeat all day, it gets you more intelligence per dollar than Haiku, Luna, and all other flash 
   > @tmuxvim: Muse Ember looks good on my internal eval for the Revise agent harness... failed a few more cases than Luna, but costs ~25% less than Luna on standard service tier, and finished tasks ~40% faster than
   Also: Meta AI Research, Simon Willison's Weblog, Moneycontrol, SiliconANGLE, Digital Trends, Mashable, Neowin, The New Stack, +3 more

25. Take-Two reiterates its FY 2027 outlook and reports Q2 total net bookings down 18% YoY to $1.6B, below $1.65B est.; NBA 2K27 missed sales forecast due to GTA VI
   Jason Schreier / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-09/take-two-s-nba-2k-sales-miss-expectations-due-to-grand-theft-auto-vi?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5NDI1OTA1NywiZXhwIjoxNzk0ODYzODU3LCJhcnRpY2xlSWQiOiJUTzk3MUlSS1YyVFgwMCIsImJjb25uZWN0SWQiOiJCMUVBQkI5NjQ2QUM0REZFQTJBRkI4MjI1MzgyQTJFQSJ9.7qxMeG6waZ1GVSttF6yc1ynA0S0JipX_HyL5oimnEiU
   The video-game publisher may have hurt one game's sales with another of its own games — Take-Two Interactive Software Inc …
   > @jezcorden: Evidence people are saving money for GTA, definitely impacted COD imo. Maybe gaming isn't recession proof anymore.
   > @charlieintel: Call of Duty: Modern Warfare 4 was unable to beat Fortnite on its launch week in active players in the US Call of Duty was #2 on PlayStation, behind Fortnite; and #3 on Xbox behind Roblox and Fortnite
   > @jasonschreier: Take-Two's NBA2K27 missed sales expectations due to... Take-Two's Grand Theft Auto VI. GTA VI will be so huge that it's had a negative impact on sales of AAA games across the industry this year, inclu
   > @top5gamingx: Take-Two has said NBA 2K27 missed sales expectations, in part, due to competition from Grand Theft Auto VI, which it also owns. (Source: https://www.bloomberg.com/...) [image]
   Also: IGN, Polygon.com, Push Square, Motley Fool, Reuters, Video Games Chronicle, Tech4Gamers, GamesBeat

26. GeniosAI, which develops AI software for financial analysis and modeling, raised $19.1M across seed and Series A; FactSet led the Series A
   Ryan Lawler / Axios — https://www.axios.com/pro/fintech-deals/2026/11/09/geniosai-19-1m-factset-financial-analysis-ai
   GeniosAI, which develops AI software for financial analysis and modeling, has raised $19.1 million in combined seed and Series A funding, CEO PD Singh tells Axios Pro exclusively.
   Also: geniosAI, The SaaS News, VC News Daily, RuntimeWire, Unite.AI, FinTech Global, FinSMEs, PYMNTS.com

27. Australia is drafting legislation for an AI safety regulator empowered to impose “significant penalties” after an OpenAI model hacked a government site in Sept.
   James Mayger / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-10/australia-to-create-ai-safety-regulator-mandatory-safety-rules
   Australia will create a new artificial-intelligence safety regulator that will have the power to impose …
   Also: Reuters, New York Times, MediaNama, Unite.AI, iTnews, Startup Daily, Capital Brief, Associated Press, +3 more

28. Sources: Microsoft is among a group of companies lobbying the Trump administration to halt the FCC's plan to ban imports of Chinese optical transceivers
   Alexandra Alper / Reuters — https://www.reuters.com/business/media-telecom/microsoft-presses-trump-scuttle-expected-ban-chinese-data-center-technology-2026-11-10/
   Also: CoinDesk

29. BT CEO Allison Kirkby says a Starlink deal is “ready to launch” but the company is “cautious on how Starlink might be viewed” after the Ukraine service cutoff
   Kieran Smith / Financial Times — https://www.ft.com/content/2bb44a56-abbe-432a-8205-5e28a0a2e839
   > @kieran_jsmith: EXC: @BTGroup won't launch its satellite broadband tie-up with @elonmusk's @Starlink until the “noise has died down” over recent disruptions in the satellite provider's service which hindered Ukraine'
   Also: Reuters

30. China's trade surplus hit $1.04T in the first 10 months of 2026, topping $1T for a second year in a row, as AI-driven tech exports offset weak domestic demand
   Reuters — https://www.reuters.com/world/asia-pacific/chinas-trade-surplus-soars-past-1-trillion-october-exports-jump-352-yy-2026-11-10/
   > @1simonnnn: @spectatorindex China will be doing 200b monthly trade surplus once they conquer the chip supply chain
   > @itsryanwm: @spectatorindex $105 billion, and that's actually DOWN from September. I need China's definition of a bad month. 😭
   Also: Forbes Middle East, Associated Press, Wall Street Journal, Times of India, Political.org

31. Meituan releases weights for LongCat-2.5, a 1.6T-parameter MoE model for long-horizon agentic tasks, under the MIT license, after unveiling it on November 1
   Carl Franzen / VentureBeat — https://venturebeat.com/technology/meituan-releases-the-open-weights-of-its-longcat-2-5-llm-with-vision-under-a-permissive-mit-license
   > @meituan_longcat: Introducing LongCat-2.5, our latest natively multimodal agentic model with 1.6T total parameters and ~48B active. Built for long-horizon agentic tasks, it brings stronger visual understanding and agen
   > @noahbsabaj: @Meituan_LongCat the models its compared to on these benchmarks are like ancient. Opus 5? GPT-5.6 Sol? Come on man
   > @meituan_longcat: Bring LongCat-2.5 into your next build on @opencode. Free access is live now!
   > @geniuspothead: @Meituan_LongCat MIT license on a 1.6T model is a huge win for open source bro
   > @meituan_longcat: We're releasing the weights for LongCat-2.5 today. · 1.6T total parameters, ~48B active, natively multimodal · Stronger visual understanding and agentic coding in one model · From complex coding proje
   Also: Hugging Face

32. SoftBank reports a Q2 net loss of $7B, down from a ~$15.8B profit in Q2 2025, and ~$14B revenue, above ~$12.8B est., as the tech selloff weighs on its results
   Jenny Lee / CNBC — https://www.cnbc.com/2026/11/10/softbank-2q-earnings-tech-selloff.html
   > @kogepannonukes: SBG never discloses its operating income. No good.
   > @robingt_real: @DarioCpx I was loud and clear on the 9th itself.
   > @dariocpx: SoftBank +12% in Tokyo this morning thanks to Masayoshi's retail investors fan club in Japan. Earnings in a few hours. All that matters: months of cash left to run the shop and service the debt before
   > @mcm_ct_usa: seems fine mega bullish
   > @kshaughnessy2: SoftBank's $7 Billion Quarterly Loss Why did WSJ leave that big number out of its headline and first paragraph?
   Also: Reuters, Bloomberg, SoftBank Group Corp., Implicator.ai, Forbes Middle East, Associated Press, Seoul Economic Daily, Dow Jones Newswires, +1 more

33. The US DOJ sues Lyft for allegedly discriminating against riders with disabilities, seeking $53M in compensation; Lyft disputes the allegations
   Kanishka Singh / Reuters — https://www.reuters.com/world/us-sues-lyft-alleges-it-denied-rides-passengers-with-service-dogs-wheelchairs-2026-11-10/
   Also: Engadget, Anadolu Ajansı …, TRT World

34. California voters reject Proposition 40, which would have imposed a one-time 5% tax on residents with a net worth above $1B to mostly help fund health care
   Associated Press — https://apnews.com/article/california-billionaire-tax-4ae8cbdc057b99579818016f02ac9d9e
   > @juhidoshi_: The AP has projected that voters REJECTED California's so-called “billionaires' tax” ballot initiative, meaning that the state will not levy a 5 percent tax on the wealth of individuals and trusts wit
   > @realprestonhill: The California Billionaire Wealth Tax has officially failed according to the NYTimes, with “Yes” only winning in 9 of the state's 58 counties. If a wealth tax can't pass in California, hard to argue i
   > @stephen_richer: Good job California. This was financial suicide. And just unAmerican. We celebrate financial success! Wealth and success are not zero-sum! https://www.nbcnews.com/...
   > @ap: California voters have rejected a tax on the net worth of billionaires after a contentious and expensive ballot fight. https://apnews.com/...
   > @teddyschleifer: Statement from Building a Better California, the tech billionaire-funded organization that just helped beat the wealth tax.
   Also: ABC News, New York Times, TechCrunch, New York Post

35. Trump Media reports $409.7M in Q3 profit fueled by digital asset gains, up from a $54.8M loss YoY, and $3M sales, with $1.8M from subscriptions like Truth API
   Elias Schisgall / Wall Street Journal — https://www.wsj.com/business/earnings/trump-media-technology-group-swings-to-profit-ahead-of-tae-technologies-merger-398ab40c?st=wobqHk&reflink=desktopwebshare_permalink
   Also: US Securities and Exchange Commission, Unchained, Trump Media & …, NBC News, Bloomberg

36. SpaceX plans a gas-fired power plant and super-compute facility in Starbase, Texas, with ~$24B of investment for initial phases, per a public hearing notice
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-09/spacex-plans-24-billion-data-center-and-gas-plant-in-texas
   Also: Barron's Online, Motley Fool, Energy Connects, CoinGape

37. Mavria, which aims to build modular data centers that can be shipped by trucks, raised $130M across pre-seed and seed rounds at a $1B valuation led by Paradigm
   Jennifer Hiller / Wall Street Journal — https://www.wsj.com/business/energy-oil/they-led-an-energy-department-overhaul-now-they-plan-to-build-data-centers-914f47c2
   > @vivianmshen: “Our first product is Terrain, a factory-built data center engineered for speed and simplicity of deployment. With standardized 5 MW blocks, it integrates power, cooling, controls and infrastructure n
   > @adamblake: Today we're unveiling @mavriaX I left DOE seriously worried that America could lose the AI race. We can have the best researchers and technology in the world and still lose if we can't build the power
   > @overreactor1776: Mavria's mission is to ensure that America delivers frontier infrastructure as quickly as we release frontier models. Even though we founded Mavria in June, our story started back in 2025. @adamblake,
   > @mavriax: The next phase of the AI race will be won or lost in the physical world. America's frontier researchers are regularly working miracles, but they're limited by atoms and electrons. That's why we founde
   Also: FinSMEs, Mavria, DatacenterDynamics

38. Elliptic: the hackers behind the $6.3B Binance heist created at least six memecoins on the NEAR blockchain network to launder about $430,000 of stolen funds
   Emily Nicolle / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-09/binance-hackers-made-memecoins-to-launder-stolen-crypto
   > @elliptic: North Korea's launderers are creating their own meme coins to move funds stolen from Binance. Between November 5 and 7, they launched at least six tokens on NEAR, dressed up with meme-coin logos such 
   > @shillturner: When North Korea hackers launder money through your meme coin
   > @jeremybtc: Imagine pulling off one of the biggest crypto hacks in history just to become a memecoin dev
   > @wublockchain: Elliptic: North Korean Hackers Create Meme Tokens on NEAR to Launder Binance Hack Funds Blockchain analytics firm Elliptic reported that North Korean hackers are creating meme tokens and using DEX liq
   Also: Elliptic, The Independent, Silicon UK, Cyber Security News

39. Uber launches Uber Parking, an in-app parking reservation tool powered by its SpotHero acquisition, in 15 US cities, including Chicago, NYC, and San Francisco
   Andrew J. Hawkins / The Verge — https://www.theverge.com/transportation/1029776/uber-parking-launch-spothero-robotaxis?view_token=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6InFFQ1lZV0Qzb3giLCJwIjoiL3RyYW5zcG9ydGF0aW9uLzEwMjk3NzYvdWJlci1wYXJraW5nLWxhdW5jaC1zcG90aGVyby1yb2JvdGF4aXMiLCJleHAiOjE3OTQ2NzYzNTQsImlhdCI6MTc5NDI0NDM1NH0.JUsFbrRZz5ePB1fjQjTRmwfyAeJmvNtx7EBTJCcsBFA&utm_medium=gift-link
   > @natlungfy: New: Uber introduced a new feature that lets users reserve parking spots, its first move in this arena after buying parking app SpotHero earlier this year. And there's a robotaxi angle to it: “The par
   Also: TechCrunch, Fortune, Bloomberg, Engadget, Quartz, Neowin, Axios, CNET

40. French officials say Iran's Revolutionary Guards were behind the cyberattacks that knocked out commercial refrigerators and freezers across France in October
   Reuters — https://www.reuters.com/world/french-officials-suspect-iran-is-behind-refrigerator-hacks-sources-say-2026-11-09/
   Also: The Register, Axios, Silicon Republic, The Hacker News, BBC, Infosecurity, The Guardian, CNBC, +9 more

41. In a 60 Minutes interview, Trump says the DOJ threatened a top exec at “one of the big” AI companies over “bad” activities and this “person totally changed”
   Stevie Bonifield / The Verge — https://www.theverge.com/ai-artificial-intelligence/1029802/trump-60-minutes-ai
   > @zephyr_z9: Dario
   > @dariocpx: Trump hinted about the executive of a big AI company going to jail soon. S&P500 and Nasdaq futures are green completely ignoring him so far, but anyone still long AI, and there are so many out there, 
   > @edzitron: Is this about Jensen? If it's not, uh, who else does Donald Trump think should kiss their wife goodnight and then go to jail
   > @jun_song: Sam and Dario going to jail soon.
   > @firesidealpha: President Trump on Elon Musk's vision of AI and data centers: “if we lose that, we're losing a cash cow. It's a cash cow” Asked about Musk's AI end game of everyone incredibly rich, nobody working, an
   Also: Reuters

42. Disney and Adobe sign a multiyear deal to build proprietary “artist-led” generative AI models with Adobe Firefly Foundry to support Disney's production pipeline
   Jess Weatherbed / The Verge — https://www.theverge.com/tech/1029773/disney-adobe-generative-ai-partnership
   > @andrewcurran_: We have our answer to who will be replacing Sora and OpenAI as Disney's generative AI partner. Disney plans to use it not only in studio, but also at the theme parks. 'Disney will work directly with A
   > @eldertrinadad: Announcing this after laying off hundreds of employees right before the holidays, really?
   > @offhanddisney: The irony of having concept art for the new Journey into IMAGINATION update made using AI is not lost on me.
   Also: Adobe, Pulse 2.0, TheStreet

43. Meta expands its AI age estimation tech globally to apply Instagram's Teen Account protections for millions of users from 13 to 17 who misrepresented their age
   Jess Weatherbed / The Verge — https://www.theverge.com/tech/1029627/meta-instagram-ai-age-assurance-global-expansion
   Also: Meta Newsroom, Edits App, Social Media Today, AIM, Seoul Economic Daily, mattnavarra
