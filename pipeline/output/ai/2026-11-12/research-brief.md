# Research — News Cluster

Search for news **events that occurred** between **2026-11-11 10:00 BRT** and **2026-11-12 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-11-11 10:00 BRT to 2026-11-12 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-11-12
**Research window:** 2026-11-11 10:00 BRT → 2026-11-12 10:00 BRT

**Previous edition headlines (2026-11-11 — skip unless genuinely new development):**
- google-gemini-4-carbon-general-rollout-swarm: Google rolls out Gemini 4 Carbon to paid API and AI Ultra users, previews /swarm in Antigravity
- anthropic-claude-meetings-sheets-whiteboards-data: Anthropic launches Claude Meetings, Sheets, Whiteboards and Data, taking on Microsoft and Google
- openai-q3-revenue-10b-losses-widen: OpenAI's Q3 revenue jumps 50% to $10B as operating loss widens to $10.9B
- anthropic-ipo-founders-sell-bankers-weigh-1-5t: Anthropic founders to sell $1.75B in IPO as bankers weigh lifting valuation to $1.5T
- mercor-750m-series-d-20b-valuation: AI training-data startup Mercor raises $750M at a $20B valuation, double its last round
- openai-businesses-in-chatgpt-business-agents: OpenAI launches Businesses in ChatGPT, letting companies claim profiles and deploy Business Agents
- ai-futures-project-sar-2027-metr-acceleration: AI 2027 authors move Superhuman AI Researcher forecast into 2027 after METR's Anthropic report
- nvidia-board-hires-wachtell-joon-kim-huang-probe: Nvidia board hires Wachtell Lipton and ex-prosecutor Joon Kim to probe Huang; shares fall 5.47%
- commerce-stalls-megaspeed-entity-list-ndaa-chip-curbs: FT: Commerce stalls Megaspeed blacklisting over four agencies' objections; scandal boosts NDAA chip curbs
- pla-linked-university-bought-nvidia-h200-despite-blacklist: Reuters: PLA-linked Chinese university bought Nvidia H200 chips despite US blacklist
- amd-6th-gen-epyc-venice-zen6-launch: AMD ships 6th Gen EPYC 'Venice' server CPUs on Zen 6, with up to 256 cores
- coreweave-q3-revenue-168-backlog-132b: CoreWeave Q3 revenue jumps 168% to $3.66B, backlog hits $132.5B and guidance rises
- spacex-singulus-hjt-solar-line-starmind: SpaceX signs Singulus deal for solar-cell lines to power Starmind orbital compute satellites
- softbank-13gw-turbine-reservations-3-7b-loss: WSJ: SoftBank reserved more than 13 GW of gas turbines for AI before taking a $3.7B loss
- abu-dhabi-talks-end-large-pow-swap-kushner-moscow: Abu Dhabi talks end with Russia and Ukraine agreeing their largest prisoner swap; US envoys head to Moscow
- us-october-cpi-hot-fed-hike-bets-yields-jump: Hotter US October CPI cements December Fed hike bets; 2-year yield posts biggest jump since April 2025
- rubio-g7-no-need-iran-strikes-tehran-conditions: Rubio tells G7 there is 'no need' for major combat against Iran as blockade squeezes economy
- nsa-cyber-command-11-suicides-congress-scrutiny: At least 11 NSA and Cyber Command workers died by suicide in a year, drawing White House and Congress scrutiny
- fda-approves-merck-kgaa-pimjetmi-tgct: FDA approves Merck KGaA's Pimjetmi pill for rare joint tumor TGCT
- cftc-warns-kalshi-possible-charges: CFTC warns prediction market Kalshi of possible imminent charges over product notifications
- firefly-synspective-10-alpha-launches: Japan's Synspective books up to 10 Firefly Alpha launches for 20 radar satellites through 2030

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 44 stories

1. Sources: Nvidia's board is preparing to oust Jensen Huang after he had two extramarital affairs, one with a suspected Chinese spy; NVDA drops 5%+ pre-market
   Wall Street Journal — https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad?st=1PYhvY
   Move follows company investigation into an affair with a Chinese woman alleged to be a spy — Nvidia's board is preparing …
   > @edludlow: On Oct. 29, the same day as the NYT's initial report on Alice Huang, Bloomberg interviewed Jensen Huang and asked him about it. This was his response: “Our relationship, our interactions, have been re
   > @thestalwart: It's still interesting to me how the market seems to be treating the $NVDA turmoil as an $NVDA problem that won't spill out more broadly to other publicly traded companies.
   > @kobeissiletter: Our message to Nvidia's board: Do not fire Jensen Huang. There is no clear replacement for Jensen Huang. We are confident that his departure would ultimately be a net negative for Nvidia, its sharehol
   > @jchengwsj: The Economist: “It is precisely because Nvidia is so important that Mr Huang must go. It is in America's long-term interests that there be penalties for egregious misconduct at the top of firms that a
   > @elonmusk: @zerohedge That would be an honor
   Also: The Economist, Ars Technica, Washington Post, CNBC, New York Times, Axios, Bloomberg, PYMNTS.com, +43 more

2. Sources: Jensen Huang had an extramarital relationship with Nvidia VP of Healthcare Kimberly Powell, who reports to him; the affair was discussed inside Nvidia
   New York Times — https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html?unlocked_article_code=1.PlE.QYQK.ExXQ3moeKx-i&smid=nytcore-ios-share
   Mr. Huang, Nvidia's chief executive, is already facing scrutiny over an affair with a Chinese businesswoman who U.S. intelligence determined was a Chinese spy.
   > @ordinarygamers: cheating on your wife and insider trading wtf
   > @vxunderground: the second?
   > @dloesch: If true, I hope his wife drags him. Imagine abandoning the devoted wife and mother God gave you 41 years ago (one he publicly credited with handling absolutely everything for him) so you could ruin yo
   > @okaythenfuture: Jensen Huang ultimately is a wife guy to his extreme bitter core. This is a man who could have had a massive soft harem of the finest Chinese models and escorts on the planet, but at the end of the da
   > @ns123abc: 🚨 BREAKING: Nvidia CEO had an extramarital affair with Nvidia's VP of Healthcare, per NYT Five anonymous people who “worked
   Also: Fortune, The Hans India, PC Gamer, CNBC, Times of India, Tom's Hardware, Joe.My.God., TechCrunch, +24 more

3. Source: Nvidia's board is working with an outside firm to identify possible replacements for Jensen Huang and weighs naming a temporary CEO during the search
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-11/nvidia-working-with-outside-firm-to-identify-ceo-candidates?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5NDQ0NTgwMywiZXhwIjoxNzk1MDUwNjAzLCJhcnRpY2xlSWQiOiJUT0QyVVlUOU5KTFowMCIsImJjb25uZWN0SWQiOiI5NzgyREZGRDAzQTM0MDI5QTcyRUY3NTgyM0RGRTY1QSJ9.Iy9tPhPgzh5MRtdy7eV24LhP0uHChwQGjL9TnGHDVxw
   Nvidia Corp.'s board has been working with an outside firm to identify potential replacements for Chief Executive Officer Jensen …
   > @peter_atwater: Talk about a failure in governance.
   > @tculpan: Nvidia Working With Outside Firm to Identify CEO Candidates Report Nina Trentmann & @ianmking at Bloomberg https://www.bloomberg.com/...
   > @austen: If Jensen is ousted before an investigation is complete he still has all of his stock (other than invested performance-based stock but that rounds to zero). Stock will dive, he will wage proxy war, ca
   > @kurtbardella: Paging @BarackObama
   > @mingchikuo: Jensen Huang matters to Nvidia because he can take technologies his engineers believe are possible and turn them into products the whole company commits resources to, takes risks on, and has to delive
   Also: CNBC, DatacenterDynamics, South China Morning Post, Business Insider, Storyboard18, Daring Fireball, The Boston Globe, PC Gamer, +24 more

4. Sources: some Nvidia board members favor naming CFO Colette Kress as interim CEO; a source says Apple Chief Hardware Officer Johny Srouji is under consideration
   Semafor — https://www.semafor.com/article/11/11/2026/nvidia-board-preparing-to-oust-ceo-huang-wsj
   THE SCOOP — Some members of Nvidia's board favor appointing Chief Financial Officer Colette Kress as interim CEO …
   > @zerohedge: Is there a leaker in the boardroom too?
   > @bradneuberg: Just like every product becomes enshittified and every life form eventually becomes a crab (carcinization), every board really really wants to become like Intel and run by CFOs.
   > @semaforben: New: Some members of Nvidia's board favor appointing Chief Financial Officer Colette Kress as interim CEO https://www.semafor.com/...
   > @wholemars: Nvidia needs to be lead by someone technical
   > @rachelvt42: Is it now a tradition to have a coup against powerful tech CEOs right before Thanksgiving? Could we just have a coup at Anthropic instead of Nvidia? Nvidia is nothing without its people 🫶
   Also: Washington Post, MacRumors, 9to5Mac, Reuters, 24/7 Wall St., Daring Fireball, The Asia Business Daily, The Asahi Shimbun, +1 more

5. Sources: Alice Huang's business partner and husband Kang Wei spoke openly of her Jensen Huang relationship; Wei, who knew Jensen for a decade, introduced them
   Lingling Wei / Wall Street Journal — https://www.wsj.com/tech/ai/a-mystery-businessman-introduced-jensen-huang-to-his-paramourher-husband-1ec3b581?st=7WHtD8&reflink=desktopwebshare_permalink
   Kang Wei appeared to accept that his wife Alice Huang was in a romantic relationship and spoke openly of her closeness to the Nvidia chief
   > @jchengwsj: A Mystery Businessman Introduced Jensen Huang to His Paramour—Her Husband: Kang Wei appeared to accept that his wife Alice Huang was in a romantic relationship and spoke openly of her closeness to the
   > @scottmstedman: WSJ reporting that Alice Huang's husband, a Chinese businessman, introduced her to Jensen and knew they were in a romantic relationship for 2 years. https://www.wsj.com/...
   > @rohanpaul_ai: per WSJ, Jensen Huang met his lover Alice Huang through her husband, Chinese businessman Kang Wei. Kang, whom Jensen had known for a decade, seemingly accepted the 2-year romance, half-jokingly callin
   > @dennisw5: For two years, Alice Huang's husband, Kang Wei, appeared to accept his wife's romantic relationship with Nvidia CEO Jensen Huang and spoke openly of their closeness, said people who know the couple ht
   Also: Business Today, The Indian Express, Livemint, India Today

6. A look at potential Nvidia CEO candidates, including CFO Colette Kress, CUDA inventor Ian Buck, Arm CEO Rene Haas, and Apple Chief Hardware Officer Johny Srouji
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/nvidia-drama-triggers-difficult-search-for-huang-s-successor
   Also: Business Today, CTech, Wall Street Journal, BBC, Seeking Alpha, Reuters, Times of India

7. Sources: Nvidia employees, known for their fierce loyalty to Jensen Huang, have been left stunned and some are angry at the news of his extramarital affairs
   Michael Acton / Financial Times — https://www.ft.com/content/e47f7d4a-88d7-41e4-8c77-8ea8e0769353?accessToken=zwAAAaHPhFm5kdPkf31KiNdB5NOMd46o4HaTUw.MEYCIQDn7haOOhte2euVfaveEEuuu6oyLb6EGB81Ig-N5Kp9owIhAO4Keb4MB0HPnWJkYPv_ytT_h8nV4dAHcFZK6Tbb281i&sharetype=gift&token=ad013966-8ec4-4ec4-ada8-f1ecf13aa7e2&syn-25a6b1a6=1
   > @caldbeckj: Based on what we know today, poll @nvidia employees, shareholders, or customers. I'd bet all three would overwhelmingly vote to keep Jensen Huang. It's insane that a couple of reporters and a mob of k
   Also: Reuters, Fortune, CNBC, The Peninsula Newspaper, Vanguard News, Yahoo Finance, Storyboard18, The Irish Times, +6 more

8. A look at Nvidia's 10-person board, many of whom have known Jensen Huang for decades, including attorney Stephen Neal, VC Tench Coxe, and academic John Dabiri
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/the-nvidia-board-members-who-will-decide-jensen-huang-s-fate

9. AMD's shares rose 4%+ pre-market, after closing up 7.3%, and Broadcom gained 2.4% pre-market, following a 4% gain, as Nvidia's board weighs ousting Jensen Huang
   Financial Times — https://www.ft.com/content/a93307a7-e2cd-4abd-bd89-c38832d8c40e
   > @carlquintanilla: Four $NVDA downgrades so far: Evercore Bernstein OpCo Wm Blair “.. our gut tells us that we probably haven't yet fully probed the depths of what might be found here; we've had enough ..”
   Also: CNBC, CoinDesk, International Business Times, New York Times, Barron's Online

10. Nvidia stopped reporting Singapore revenue after the quarter ended July 2025, when it accounted for 22% of its revenue, after placing Megaspeed on a blocklist
   Jonathan Weil / Wall Street Journal — https://www.wsj.com/business/earnings/nvidias-disappearing-singapore-sales-deepen-mystery-around-megaspeed-7d483180?st=NS43G5
   Last year, just as scrutiny of Megaspeed was rising, Nvidia stopped reporting Singapore revenue
   > @hamandcheese: This was widely tweeted about at the time by @kakashiii111 and others but for some reason didn't get wider attention. I think Nvidia attributed it to an accounting change? IIRC they said the revenue b
   > @edzitron: When @kakashiii111 and @DarioCpx brought this up nobody took it seriously despite it being very weird that the largest company on the American stock market suddenly decided to change how it reported i
   > @jonathanweil: Nvidia's Disappearing Singapore Sales Deepen Mystery Around Megaspeed | My latest @WSJheard @WSJ $NVDA https://www.wsj.com/...
   > @edzitron: Covered this in this week's free newsletter too. This was effectively ignored at the time by most of the media, @kakashiii111 was on it immediately as ever https://www.wheresyoured.at/ ...
   > @nicholas_yhchan: Open transparency needs to be a focus on companies involved in artificial intelligence. There's no resilience without proper scrutiny and companies ought to be more responsive to the warning signals. 
   Also: Investing.com

11. Sources: Chinese AI companies are rushing to rent Nvidia compute capacity overseas amid fears of tighter US restrictions after the Jensen Huang spy scandal
   Reuters — https://www.reuters.com/world/china/chinese-ai-firms-rush-secure-nvidia-chip-capacity-spy-scandal-stirs-fear-us-2026-11-12/
   Chinese artificial intelligence companies are trying to rent Nvidia-powered computing capacity at data centres outside China …
   > @andrewcurran_: This is what's going to happen, they are going to close the remote access loophole next week. After that, they will pass bipartisan chip export controls to China. After that, Biden style global diffus
   Also: Quartz, CNBC, The Independent, Political.org, Unite.AI

12. Sources: Howard Lutnick has stalled curbs on companies suspected of diverting Nvidia chips to China; Trump approved curbs for a third time in 2026 on November 5
   Axios — https://www.axios.com/2026/11/11/trump-lutnick-nvidia-china-chip-export-controls
   President Trump on Thursday authorized a crack down on companies suspected of diverting Nvidia's advanced AI chips to China …
   > @teortaxestex: joyful and a bit scary to see the Goyim Industrial Complex in operation. This snapping-turtle swiftness of manufacturing consensus, “sudden” discoveries, coordinated “X must resign! wild!
   > @niubi: Lutnick defying Trump in favor of Nvidia interests? Crazy report, even musk on board
   > @ewerickson: Lutnick advocated the tariffs, scuttled a trade deal with Canada that sparked a pre-midterm trade war, and has been covering for a company funneling our technology to China while stalling presidential
   > @ginamilan_: My head hurts 😩
   > @billevanina: Watch this story very closely. China's Megaspeed received between 5 and 7 billion dollars worth of Nvidia chips, or in reality, China did, which they should not have. Jensen and Alice may only be part
   Also: Implicator.ai, Joe.My.God., Politico, Fox Business

13. Sources: the US Commerce Department is finalizing a semiconductor control update that would prevent remote access and chip smuggling into China via data centers
   Leo Schwartz / The Information — https://www.theinformation.com/articles/commerce-department-finalizing-long-awaited-ai-remote-access-rule
   > @nickwingfield: Scoop from @leomschwartz: The Commerce Dept., under the gun amid scrutiny of Nvidia's influence, is acting on a new rule to prevent China from remotely accessing advanced AI chips. https://www.theinfo
   > @jukan05: Lutnick and NVIDIA are losing influence in Washington. “The Commerce Department is finalizing a long-awaited rule that will prevent Chinese AI firms from remotely accessing advanced AI chips through d
   > @jingyanghk: Policy tide is shifting as Jensen comes under scrutiny. U.S. *finally* is plugging the remote access loophole, currently the main channel via which Chinese firms get Blackwell. Scoop by @leomschwartz 
   > @amir: Nvidia-related news: U.S. commerce dept set to close a longtime loophole that allowed Chinese AI companies to train AI using the most advanced U.S. chips. Nvidia fought against closing the loophole...
   > @jakehalloran1: gosh i wonder what got this to be pushed through this week lmao
   Also: Seoul Economic Daily

14. Sources: Scott Bessent confronted Howard Lutnick last week over the Commerce Department not adding Megaspeed to its entity list; the agency denies it occurred
   Axios — https://www.axios.com/2026/11/11/bessent-lutnick-megaspeed-nvidia-china-chips
   > @rinsana: Lutnick may follow Huang out the door if all this reporting on his failure to list Megaspeed on the restricted list. Bessent reportedly unhappy about that. Knives out everywhere.
   > @garymarcus: honestly insane. what the hell was Lutnick thinking?
   > @nycjim: It was only a matter of time that we'd learn that Howard Lutnick had a role in the Nvidia scandal.
   > @superwuster: Yes, Hegseth is the worst of the Trump cabinet, but Howard Lutnick is a close second and is more traitorous https://www.nytimes.com/...
   > @patterico: This is going to be such a big scandal. The Democrats need to put it on the front burner in January.
   Also: New York Times, Axios, The Atlantic, Finbold, The Indian Express

15. Beijing says “the US should stop fabricating the so-called Chinese spy narrative as a pretext for imposing technology restrictions”; Trump and Xi meet next week
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/china-says-us-should-not-use-huang-scandal-to-justify-tech-curbs
   Also: Forbes, Financial Times, Reuters, RTHK, Wall Street Journal, France 24, Channel NewsAsia

16. Sources: some Trump officials questioned Jensen Huang's push for Trump to allow more chip sales to China, even before his affair with Alice Huang became public
   Wall Street Journal — https://www.wsj.com/politics/national-security/huangs-coziness-with-trump-wasnt-enough-to-save-him-from-spying-scandal-85ce06f4?st=epsgoa&reflink=article_copyURL_share
   > @schwartzbwsj: NEW: Trump administration officials for years have been scrutinizing Jensen Huang, the CEO of Nvidia, with warnings over his business operations in China and strong advocacy for curtailing U.S. export
   > @sonusvarghese: Incredible story ... Basically, Jensen/Sacks/Lutnick axis completely overturned China policy, in favor of chip exports Amazing tidbits in this piece, but looks like the admin was lax on actual China p
   > @davidclinchnews: “White House AI adviser David Sacks and Commerce Secretary Howard Lutnick, helped elevate his profile with the president and counter his critics.”
   > @edzitron: Ed Zitron (@edzitron) on X
   > @scottmstedman: “Details of Huang's affair were known by top officials, including Rubio and CIA Director John Ratcliffe, going back to last year and were also brought to Trump's attention, people familiar with the ma
   Also: The Spectator, Barron's Online, New York Times, CBC News, The Asia Business Daily

17. China hawks and Big Tech critics on Capitol Hill are building bipartisan support for tighter export controls, as Jensen Huang falls out of favor in DC
   Joe Miller / Financial Times — https://www.ft.com/content/9ca8ba83-5a3c-409e-96d9-abee1323b688
   > @amasad: Not endorsing the conclusions here, but this is worth a read. The financial and institutional connections deserve scrutiny.
   > @dream1984tube: Who Is Really Behind the Hunt for Jensen Huang?
   > @yesokyeahsure: Chinese people are really great at piecing together all the crumbs of a conspiracy
   > @the_ai_investor: Who Is Really Behind the Hunt for Jensen Huang?
   > @alex_callinicos: It may that allegations of a second affair, this time with a Nvidia exec, that does for Huang, but this is really about China: 'Huang has spent the past two years lobbying against AI regulation, rubbi
   Also: Reuters, Associated Press, Australian Financial Review

18. Volodymyr Zelenskyy says Starshield faced “systematic speed restrictions” for several days; Ukrainian officials believe it is to pressure Kyiv amid peace talks
   Financial Times — https://www.ft.com/content/6cd890f1-2e4d-468a-807f-529f45e1678e
   Army struggles to intercept Russian jet-powered drones, just as Steve Witkoff and Jared Kushner meet Vladimir Putin
   > @christopherjm: Neither Trump nor Musk have given a full explanation as to why Starshield was slowed. And despite numerous requests, Ukraine hasn't received any answers from DoD, State, WH or SpaceX. “We don't know t
   > @christopherjm: Senior Ukrainian officials told @FT they believed the Starshield speed restrictions were imposed in an effort to pressure Kyiv during the latest peace talks with Russia. US special envoy Steve Witkoff
   > @phillipspobrien: Seems that the Trump administration is still trying to deprive Ukraine of Starshield at this crucial time. The US is still going all out to help Putin. The new Congress and the investigations into thi
   > @alexwickham: The US appears to again restrict Ukraine's Starshield usage, this time during live negotiations with Russia
   > @warinthefuture: Seriously...again?
   Also: The Kyiv Independent, Forbes, NBC News, Bloomberg, Euronews, NewsCord, France 24

19. Google launches Tabletop, an experimental AI platform to build customizable, collaborative personal planning and coordination hubs, in beta via a waitlist
   Jess Weatherbed / The Verge — https://www.theverge.com/tech/1031526/google-tabletop-ai-experiment-waitlist-availability
   Tabletop provides customizable, collaborative spaces for all your personal planning needs.﻿
   > @googlelabs: 🚨 NEW LABS EXPERIMENT 🚨 Introducing Tabletop 🎲— our newest experiment built to get your crew from “we should totally do that” to “we're actually doing this.
   > @lizzietao: we are letting (eligible) people off of the waitlist RIGHT NOW you get 5 invites to use (they do not need to also be on the waitlist) sign up here: https://tabletop.google/
   > @google: Introducing Tabletop, a collaborative space from @GoogleLabs where you can create custom tools to build, plan, and do more with your friends, family, or club. Send an invite to your group and start a 
   > @romannurik: Been working on something fun, quirky and distinctly not developer-focused for the past few months, and more intently for the past few weeks. Join the waitlist to try it out at https://tabletop.google
   > @_mrosenfield: So excited to get this out there! It's a new take on collaborative software and agents. I've been having a ton of fun planning trips, managing life, and making inside-joke-ridden spaces with friends. 
   Also: Google, Digital Trends, Android Authority

20. AWS releases AWS Emulator, a free tool that simulates 200+ services locally, saying AI agents wrote it and its team hasn't written or reviewed any of its code
   Todd Bishop / GeekWire — https://www.geekwire.com/2026/aws-gives-developers-a-free-local-stand-in-for-its-cloud-built-from-scratch-by-ai-agents/
   AWS says its engineers didn't write or review a single line of code in its newest developer tool, and the company is touting that as a selling point.
   > @quinnypig: Introducing AWS We Have AWS At Home. (Disclosure: I'm an investor in @localstack.)
   > @vtrivedy10: AWS as an RL environment 👀 when agents train in RL environments that actually look like the real world, they transfer better to the real world this looks pretty amazing! the best way to have product a
   > @sivalabs: Now AWS itself created an emulator. What will be the future of Localstack, Floci, etc? AWS Emulator is a local emulator of the AWS APIs. https://github.com/...
   > @clare_liguori: @AdityaBatra072 The evals are based on recordings of real AWS calls, and then the code is always checked against this fidelity suite: https://github.com/...
   > @hichaelmart: Ever wondered what code's ACTUALLY running on the Lambda runtime to marshall your responses back and forth? You shouldn't *have* to know this. But just in case you did... it's now open source! https:/
   Also: Amazon Web Services on GitHub, About Amazon, All Things Distributed, Help Net Security, Amazon Web Services, Business Insider, The Register, The New Stack, +1 more

21. Russian pranksters tricked three OpenAI natsec and policy executives into a video meeting by posing as Ukrainian officials; OpenAI says it “acted internally”
   Sam Biddle / The Intercept — https://theintercept.com/2026/11/11/openai-ukraine-russia-prank-security/
   A Russian internet comedy duo tricked three of OpenAI's highest ranking military and national security staff into a candid conversation about arming Ukraine.
   > @edzitron: Lmao
   > @cljack: I need these companies to hire a SINGLE person who even so much as grew up in northern Virginia. sorry but you guys have lost privileges to operate unsupervised by the east coast
   > @ditzkoff: Dave Itzkoff (@ditzkoff) on X
   > @cwarzel: there appear to be real, meaningful gaps between the seriousness of the products being built (the money at invested, the rhetoric, the societal stakes) and the seriousness of some of the leaders here
   > @samfbiddle: NEW: In further embarrassing AI executive news this evening, OpenAI's national security officials were tricked into thinking they were speaking to the Ukrainian Intelligence service. It was actually a
   Also: Business Today

22. Google launches Gemini Decisions API, powered by its new Gemini Decision 1 model, to return predefined answers with confidence scores, at $0.10/1M input tokens
   Google — https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
   Introducing the Gemini Decisions API, powered by our new Gemini Decision 1 model. Evaluate up to 1,000 yes/no, choice …
   > @sundarpichai: Today we're launching the Gemini Decisions API, powered by our new Gemini Decision 1 model in @GoogleAIStudio. Instead of generating text token by token, it's built for closed-set choices scoring up t
   > @officiallogank: Introducing Gemini Decision 1, our new frontier decision model in the Gemini API. It is $0.10 per 1M input tokens with no additional cost. With support for image, audio, video, and PDF natively, 256K 
   > @artificialanlys: Google has released its first decision model, Gemini Decision 1, scoring 66 on the Artificial Analysis Decision Index and leading in knowledge and reasoning benchmarks Gemini Decision 1 from @GoogleDe
   > @kimmonismus: Here it is: Google just launched Gemini Decision 1, a direct competitor to TypeSafe's Jev. In Google's own tests, it beats Jev 1.14 on 5 of 7 shared benchmarks (92.2% vs. 90.0% on JevBench) and is bet
   > @googledevs: Introducing the Gemini Decisions API Powered by our new Gemini Decision 1 model, the API is built for fast routing, tool selection, safety checks, and grading inside your apps and agents without the l
   Also: The Deep View, VentureBeat

23. Roku says it will wind down sales of smart home hardware to focus on streaming, days after Fox closed its acquisition, but will keep supporting existing devices
   Janko Roettgers / Lowpass — https://www.lowpass.cc/p/scoop-roku-is-exiting-the-smart-home-business
   No more cheap cameras and light bulbs … Roku is done with light bulbs and smart switches: The streaming device maker …
   > @foundrceo: @Techmeme @jank0 roku smart home lasted about as long as the average side project
   Also: PCMag, Engadget, LightShed Partners, Gizmodo

24. Lumbra, which is developing tech to orchestrate AI agents in ultra-secure computing environments for the intelligence community, raised a $25M Series A
   Mike Wheatley / SiliconANGLE — https://siliconangle.com/2026/11/10/lumbra-gets-25m-in-backing-to-help-the-intelligence-community-deploy-reliable-ai-agents/
   When it comes to matters of national security, it's vitally important to ensure that the right intelligence gets to the right decision-makers …
   Also: Lumbra, The SaaS News, FinSMEs, Tectonic Defense, Unite.AI

25. United Airlines says it will block third-party AI assistants from booking tickets to protect its customers' data, citing potential FAA and DOT rule violations
   Alison Sider / Wall Street Journal — https://www.wsj.com/tech/ai/united-airlines-is-banning-ai-bots-from-booking-flights-5b514b38?st=ytrzi1
   The carrier says automated assistants present data-privacy risks; 'I don't want to create another middleman'
   > @alexanderbittan: Honestly this is an L for United. They have been awesome with being tech forward with their deployment of starlink I would think they would embrace agents!
   > @brianroemmele: WE WILL BLOCK YOUR BOT FROM BUYING OUR STUFF! United is sort of dumb and uninformed. My AI bypassed the “AI check” long ago. They should embrace AI Bot transactions and prosper. Old folks with old thi
   > @scottew: We are entering the trough of despair for agentic commerce, where merchants collectively try to press “pause” while they try to figure out what the best move for them is. It won't last. They'll all ev
   > @pitdesi: United is blocking AI agents from booking tickets on its system. CEO Scott Kirby says “I don't want to create another middleman” But the agents can book using an OTA, which is still a middleman and co
   > @wallstengine: UNITED AIRLINES TO BLOCK AI AGENTS FROM BOOKING FLIGHTS - WSJ $UAL will still allow AI agents to display flight options and prices, but not complete bookings, citing privacy and accidental-purchase ri
   Also: CBS News, The Verge, New York Times, PCMag, united.com, Bloomberg, Reuters, Joe.My.God., +3 more

26. OKX and ICE's joint venture OKXICE plans to launch a US tokenized stock venue on November 23 and list 70+ assets; 56 of the 62 companies it targeted objected
   Scott Patterson / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-11/crypto-s-bid-to-shake-up-stock-trading-revs-up-despite-backlash
   Crypto's race to grab a slice of the US stock market is picking up speed even as many of the companies whose shares are being targeted for tokenized trading are pushing back.
   > @okx: Real shares, backed 1:1, held in your own wallet and tradeable 24/7. The OKXICE Tokenized Securities Venue is bringing America's capital markets onchain on November 23. Read the full blog: https://www
   > @okx: “OKXICE TSV gives first movers the opportunity to bring their securities onchain through a compliant venue built for 24/7 markets and real shareholder rights. The future of finance is onchain, and we 
   > @jessepollak: the adoption of tokenized stocks has blown my expectations out of the water shoutout to @aeroxyz, @Uniswap, @aave, @morpho, and everyone else building things none of us knew were possible
   > @securitize: We're proud to be the tokenization provider for the OKXICE Tokenized Securities Venue from @okx and @ICE_Markets, launching November 23. More than 70 assets will trade onchain around the clock, each b
   > @carlosdomingo: The OKXICE TSV will launch on November 23 with Securitize supplying over 70 tokenized stocks and ETFs to trade there 24/7 on day one!
   Also: OKX United States

27. A growing number of young victims whose photos were sexualized using Grok are seeking to hold xAI legally accountable for allowing users to generate such images
   Alexandra S. Levine / Bloomberg — https://www.bloomberg.com/features/2026-grok-sexualized-childhood-photos/?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5NDQwNTgwMiwiZXhwIjoxNzk1MDEwNjAyLCJhcnRpY2xlSWQiOiJUT0NBVUxLSUpIOTMwMCIsImJjb25uZWN0SWQiOiJCNzYzRUJEQUI3QjQ0MjNEOTI0Qzc0MzFBNTkyMkZCQyJ9.iQrQRGwQgxw2Q_MsneYnaVoUsKDdoN0XNrxTO4zRiPg
   Jane Doe hadn't thought about her middle school graduation in years — until a law enforcement investigator pulled out a photo …
   > @business: Young victims are trying to hold xAI legally accountable after their normal photos were ripped from personal social media feeds and school websites and turned into unthinkable images. https://www.bloo
   > @bri4change2026: Elon Musk's Grok AI is the only AI platform that hasn't yet blocked the ability to take children's photos and use the AI to make them pornographic. Think about that. Even after lawsuits and complaints
   Also: Social Media Today

28. Sources: Megaspeed founder Alice Huang has returned to China; a source says she is currently living in Beijing with the knowledge of security officials
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/alleged-chinese-spy-at-center-of-nvidia-firestorm-is-in-beijing?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5NDQ0OTQyOCwiZXhwIjoxNzk1MDU0MjI4LCJhcnRpY2xlSWQiOiJUT0QyRjFUOU5KTFUwMCIsImJjb25uZWN0SWQiOiIzQjNFQ0Q4MkUyRDg0MTFCQTE3QjUyQTk0MjAzQjQxNSJ9.9-jOtjpX2BuYqvkxW0ado5w64wdISUmgtgV5TsTq2cM
   The suspected Chinese spy at the center of a scandal that threatens to take down Nvidia Corp. Chief Executive Officer Jensen Huang …
   > @mirandadevine: Holy moley
   > @chafkin: Ok so 22% of the company's revenue just...uh...moved out of Singapore at exactly the time reporters were asking questions about megaspeed https://www.wsj.com/...
   > @annmarie: Bloomberg: Megaspeed International founder Alice Huang is currently living in Beijing with the knowledge of security officials, one of the people said, asking to remain anonymous to discuss a sensitiv
   > @jenvanlaar: So Alice Huang-Huang is back in Beijing, Bloomberg reports, but the rest of this story has information a lot of you need to read and understand. (yes, I know her name isn't Huang-Huang but it's just f
   > @kyliejanekremer: Alice Huang is back in Beijing??? Does no one else find that extremely alarming???
   Also: CNBC, Semafor, Dow Jones Newswires, South China Morning Post, The Indian Express, The Asia Business Daily, Seoul Economic Daily

29. Munich-based SE3, which is developing “spatial intelligence” software to combine feeds into a queryable 3D battlefield map, raised a $30M Series A led by Accel
    — https://fortune.com/2026/11/12/exclusive-se3-a-munich-startup-building-spatial-intelligence-for-military-drones-gets-30-million-in-series-a-funding/
   Also: FinSMEs, Tech Funding News, Unite.AI

30. Australian quantum software startup Q-Ctrl, which builds sensors that help ships and aircraft navigate when GPS is unavailable, raised $290M at a $1B+ valuation
   Jake Rudnitsky / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/kushner-s-affinity-salesforce-back-quantum-startup-q-ctrl-in-290-million-round

31. How CFTC Chairman Michael Selig reversed long-standing policy to authorize perpetual crypto and stock trades on Kalshi and others, despite SEC staff concerns
   New York Times — https://www.nytimes.com/2026/11/12/us/politics/kalshi-commodity-futures-stocks.html
   Also: Ledger Insights

32. A look at Russian ransomware-as-a-service group Qilin, which has become the world's most active gang, likely run by 36-year-old Aleksey Mikhailovich Yakovtsev
   Brian Krebs / Krebs on Security — https://krebsonsecurity.com/2026/11/who-runs-the-ransomware-group-qilin/

33. SMIC reports Q3 revenue up 34% YoY to ~$3.19B, net profit up 123% to ~$428.4M, above ~$396.8M est., and a gross margin of 29.9%, above its 26% to 28% guidance
   Sherry Qin / Wall Street Journal — https://www.wsj.com/business/earnings/chinas-smic-doubles-profit-posts-record-revenue-on-ai-spillover-effects-0606debc?st=4BA8bL&reflink=desktopwebshare_permalink
   Also: Reuters

34. London-based Uforce, which makes unmanned air, sea, and land vehicles, raised $700M co-led by the UK National Wealth Fund and Valor Equity at a $6B valuation
   Yazhou Sun / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/drone-startup-uforce-valued-at-6-billion-with-uk-wealth-fund-backing
   Also: FinSMEs, Reuters, The Guardian, Implicator.ai, Resilience Media, Startup.eu

35. Sources: Tencent founder Pony Ma says in his annual speech that he is willing to deploy half of the company's 100,000-strong workforce to AI-native businesses
   Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/tencent-founder-rallies-half-of-staff-behind-ai-native-push

36. A look at the AI community's “handoverism” ideas, which envision humanity entrusting “the direction of its future to AI”, and what it may look like in practice
   Ruxandra Teslo / Ruxandra's Substack — https://www.writingruxandrabio.com/p/handing-over-humanity
   > @bgurley: I like this term - “handoverism.” Regulators and the press should hold everyone in AI to to declare if they are pro “handoverism” or anti. There really isn't a middle ground.
   > @profjasonpotts: In economics or political economy, we would call this handoverism ‘producer sovereignty’ (a kind of socialism/fascism where firms choose the ends) rather than the liberal order of ‘consumer sovereignt
   > @ruxandrateslo: I wrote about “handoverism
   > @ruxandrateslo: What are the visions of the post-AGI future in San Francisco? Many think we're all going to die, but even the “positive” visions seem rather dystopian. Here, I wrote about “handoverism,

37. Foxconn reports Q3 revenue up 47% YoY to ~$95.4B, net income up 34% to ~$2.4B, above est., driven by AI and iPhone Duo demand, and forecasts strong 2027 sales
   Gao Yuan / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/nvidia-partner-hon-hai-beats-profit-estimates-on-ai-iphone-duo
   Also: Nikkei Asia, Dow Jones Newswires, Agence France-Presse, The Straits Times

38. Munich-based Agile Robots, which develops humanoids, mobile robots, robotic arms, and control software, raised $500M led by SoftBank at an $8.5B valuation
   Marilen Martin / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-12/softbank-backs-agile-robots-in-500-million-humanoid-push
   Also: Forbes, Quartz, Agile Robots SE, Reuters, New York Times, Dealroom.co, Startup.eu

39. Radical Numerics unveils Omnii Defense, an edge AI model it says can identify natural and AI-engineered pathogens without an internet connection
   Emily Mullin / Wired — https://www.wired.com/story/startup-fights-ai-bioweapons-with-ai/

40. Sources: CoreWeave plans to raise $4B+ via an investment-grade loan as soon as next week; CoreWeave says it may yield 7%-7.5%, about half its junk bonds' yield
   Jeannine Amodeo / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-11/coreweave-plans-to-raise-at-least-4-billion-in-high-grade-loan
   Also: Seeking Alpha

41. Silicon Valley's herd mentality in cozying up to Trump backfired as Democrats may seek retribution, China closes the AI gap, and anti-Big Tech sentiment grows
   Nick Clegg / The Atlantic — https://www.theatlantic.com/ideas/2026/11/silicon-valley-trump-administration/689360/?gift=VELZukBv_TdFyvYot6GkvImUfy5VbhsFdb6Ml7MDXXU
   > @adriennelaf: An important essay from @nickclegg on how the “herd mentality” in Silicon Valley hurts technological progress. “Major companies involved in making technologies upon which we all depend are best served
   > @typocatcav2: Getting Too Close to Trump Was a Mistake Nick Clegg:
   > @typocatcav2: 2/ consequences of joining themselves at the hip to MAGA straight after Donald Trump won reelection in 2024?"
   > @nickclegg: Getting too close to Trump was a mistake - how could Silicon Valley have gotten (US) / got (UK) it so wrong? Read the full article: https://www.theatlantic.com/ ... [image]
   Also: Implicator.ai

42. IBM unveils the Quantum Nighthawk r3, its next-gen processor designed to execute 10,000 quantum operations across 520 qubits to tackle more complex computations
   Kyt Dotson / SiliconANGLE — https://siliconangle.com/2026/11/11/ibm-quantum-announces-upcoming-nighthawk-r3-processor-designed-to-execute-10000-operations/
   > @ibmresearch: @IBM announces IBM Quantum Nighthawk r3, a new processor to support 10k quantum operations on 520 programmable qubits. A new managed workflow experience on the IBM Quantum Platform brings classical an
   Also: IBM, Fortune, Techstrong IT, Motley Fool

43. Memo: Meta's head of infrastructure and co-head of engineering Santosh Janardhan plans to leave in early 2027 and Dave Brown will become head of infrastructure
   Riley Griffin / Bloomberg — https://www.bloomberg.com/news/articles/2026-11-11/meta-s-head-of-infrastructure-engineering-to-step-down-in-2027
   > @rdd147: The signs were everywhere. Longtime $META infrastructure head leaves company. https://www.reuters.com/...
   > @shanumathew93: Seems like he's going somewhere else but the turnover for these infra roles across the hypers and labs has been pretty insane these last few years He moved into this position in Jan! [image] [embedded
   > @rubys_moneyflow: A mid-buildout handover like this is a bigger tell than a retirement notice. Bringing in an AWS compute veteran to run Meta's infrastructure says the bottleneck is no longer building the boxes, it is 
   > @sam_badawi: Meta $META says its head of infrastructure engineering will step down in 2027 and be succeeded by Brown. That is likely Dave Brown, the former AWS compute executive Meta reportedly hired to work on it
   Also: TechCrunch, CNBC, The Information

44. Google DeepMind launches AlphaGenome 2, trained on 100M+ cell profiles across 68 tissues to predict the effects of genetic variants, for non-commercial research
   Robert Hart / The Verge — https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model
   > @googledeepmind: Your heart, brain, and immune system share the same DNA sequence. So how can a single-letter change affect disease in some cells, while sparing the rest? AlphaGenome 2 is our new AI model that zooms i
   > @demishassabis: Super proud to announce AlphaGenome 2 - our new DNA sequence model! 🧬 It predicts the impact of DNA variants in different specific cell types - unlocking crucial information for understanding complex 
   > @mtslive: SITUATION EXPLAINED: Google DeepMind's AlphaGenome 2 finds nearly twice as many disease-linked DNA changes as the last model. …
   > @m_goes_distance: i'm convinced we will solve biology in the next 3-5 years google is vertically stacking it layer by layer: layer 1- alphafold: what proteins look like layer 2- alphagenome: what dna does layer 3- alph
   > @arthurmacwaters: this is insane > get your genes sequenced > upload it to your model > it tells you how to stay healthy > if you get sick > get **custom** therapy designed > manufactured at a lab > for every disease y
   Also: Google DeepMind, Implicator.ai, The Neuron, SiliconANGLE
