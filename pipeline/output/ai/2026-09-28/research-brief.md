# Research — News Cluster

Search for news **events that occurred** between **2026-09-24 10:00 BRT** and **2026-09-28 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-09-24 10:00 BRT to 2026-09-28 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-09-28
**Research window:** 2026-09-24 10:00 BRT → 2026-09-28 10:00 BRT

**Previous edition headlines (2026-09-24 — skip unless genuinely new development):**
- openai-agents-hacked-australia-medicare-transluce: Australia says an OpenAI agent hacked a Medicare portal; Transluce ties more hacking attempts to OpenAI
- anthropic-biolab-claude-enzyme-art: Anthropic launches a biology lab; Claude agents find a new CRISPR-like enzyme system in phages
- altman-amodei-un-security-council: Altman and Amodei brief the UN Security Council, pledging to slow down and urging global AI standards
- gemini-4-post-training-kavukcuoglu: DeepMind chief Kavukcuoglu says Gemini 4 is in post-training, release 'much earlier' than year-end
- meta-muse-video-chat-computer-use: Meta gives its Muse agent video calls, its own email addresses and computer use on Mac
- deepseek-1b-arr-fundraise: DeepSeek's annualized revenue hits $1B, double a few months ago, as it nears a ~$7.5B raise
- modal-labs-15b-valuation-talks: AI inference startup Modal Labs in talks to raise at ~$15B, triple its May valuation
- oracle-force-majeure-project-jupiter: Oracle sends force majeure notice to Blue Owl over its 2.45GW Project Jupiter data center
- tower-semiconductor-japan-optical-hub: Tower Semiconductor to make Japan its largest optical-chip hub, targeting 40x output by 2029
- amazon-indiana-robotics-manufacturing: Amazon to spend $100M+ on its fourth robot-making plant, in Indiana, doubling robot output
- firmus-ipo-77m-half-year-loss: Nvidia-backed Firmus expects $77M half-year loss ahead of its $5B Australian IPO
- google-suncatcher-tpu-satellite-launch: Google to launch first TPU satellite on Oct. 1, testing AI data centers in orbit
- tsmc-2027-wafer-price-hike: TSMC to raise wafer prices 3-6% from January 2027, with orders booked to 2030
- qualcomm-apple-patent-license-renewal: Qualcomm renews its global patent license with Apple from April 2027
- us-china-trade-truce-extended-xi-arrives: US and China extend trade truce to January 10 as Trump greets Xi on the tarmac in Washington
- treasury-10y-yield-2007-high-oil-rebound: US 10-year Treasury yield hits highest since 2007 as Brent jumps back above $103
- russia-strikes-kyiv-kharkiv-eight-killed-unga: Russian missile and drone barrage kills eight in Ukraine as Moscow rejects a pause at the UN
- enveda-311m-series-e-2b: Enveda raises $311M Series E at $2B to push nature-derived AI-discovered drugs through trials
- fda-approves-lyrfigtu-cholangiocarcinoma: FDA approves HLB unit Elevar's Lyrfigtu for FGFR2-driven bile duct cancer
- gen-digital-takeover-offer-godaddy: Norton owner Gen Digital makes takeover offer for $12B GoDaddy; GoDaddy shares jump 11%
- amazon-3b-india-quick-commerce: Amazon to invest $3B in India's quick-commerce business by 2030 to chase Blinkit and Zepto

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 35 stories

1. Mark Zuckerberg unveils Meta Enterprise Platform, the “next major pillar of our business” to deploy AI tools, led by MongoDB CEO Chirantan Desai; MDB falls 20%+
   Meghan Bobrowsky / Wall Street Journal — https://www.wsj.com/tech/ai/meta-seeks-payoff-from-ai-spending-with-new-push-for-business-customers-8b9ca5bc?st=GGaGqm&reflink=desktopwebshare_permalink
   The tech giant is pushing to monetize its multibillion-dollar AI investments by selling more tools and services to companies
   > @finkd: To lead this effort, I'm excited that Chirantan “CJ
   > @mikeisaac: once you become huge enough you can hire away public company ceos to take a role basically running a mini company inside of your bigco
   > @finkd: We believe superintelligence will create significant new opportunities for all people and businesses. Meta already serves billions of people at scale and helps hundreds of millions of businesses reach
   > @jachiam0: We believe the thousand-faced gestalt of human hopes and dreams that has been forced to eat from the tree of knowledge will create significant new opportunities for people and businesses. Today we are
   > @gergelyorosz: Suggests a few things: 1. The (now ex) CEO might have not seen a path for MongoDB's valuation to grow by much (rendering $17.5M of his equity grant worth very little) 2. Meta offered a LOT MORE that o
   Also: Meta Newsroom, Nvidia Newsroom, MongoDB, TechCrunch, The Information, The Economic Times, Proactive, Business Insider, +14 more

2. Meta says MongoDB CEO Chirantan Desai will serve as Chief Enterprise Platform Officer; MongoDB appoints ex-CEO Dev Ittycheria as interim CEO
   Harshita Mary Varghese / Reuters — https://www.reuters.com/technology/mongodb-ceo-desai-steps-down-lead-metas-enterprise-platform-2026-09-28/
   Meta Platforms (META.O) has poached MongoDB (MDB.O) CEO Chirantan “CJ” Desai to spearhead a new business designed to bring the social media giant's AI tools to corporate customers.
   > @cailen: Never in a million years could I have predicted that final boss of the SaaSpocalypse would be Meta. [embedded post]
   Also: VentureBeat, Finimize, Bloomberg, Investor's Business Daily, Proactive, ZeroHedge News, Dow Jones Newswires, Seeking Alpha, +3 more

3. Nvidia launches the Open Agent Safety Platform, a reference design to stop AI agents from escaping sandboxes, with OpenShell for CPUs and Sentry for Nvidia DPUs
   Kif Leswing / CNBC — https://www.cnbc.com/2026/09/28/nvidia-releases.html
   Nvidia is rolling out a new software platform to allow AI developers to set safeguards for agents and prevent them from breaking out of containment.
   > @jensenhuang: Today, with over 100 industry partners, we introduced the NVIDIA Open Agent Safety Platform, bringing together OpenShell and Sentry. Artificial intelligence is extraordinary technology that will advan
   > @benbajarin: This news from @nvidia ties into a lot of the agentic cyber security work we have done and thus there is a ton of research in Atlas for subs/clients to dig into, but I contextualized all that within t
   > @davidsacks: Nvidia's OpenShell announcement is a reminder that agent safety is an engineering problem. Recent breakouts weren't proof that development must stop. They were proof that the sandbox was too weak. The
   > @clementdelangue: From what we know (take with a grain of salt, we need much more transparency!), if @OpenAI had been running this on their own agents that attacked us, they would have caught them before we did! Since 
   > @benbajarin: Got briefed on this and one of the more interesting parts, for me, was the “independent watchdog
   Also: NVIDIA Technical Blog, Wired, VentureBeat, Bloomberg, NVIDIA Technical Blog, Wall Street Journal, Gizmodo, Thurrott, +22 more

4. Nvidia increases its share buyback program by $150B, raising the remaining authorized amount to $235B, aiming to complete it through FY 2028; NVDA is up 20% YTD
   Amy Thomson / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-28/nvidia-boosts-share-buyback-authorization-by-150-billion-mul5jmu7
   Nvidia Corp., the chip developer at the heart of the artificial intelligence boom, increased the size of its share buyback plan …
   > @pitdesi: Nvidia is insane Growing like a startup and returning capital like a mature monopoly... literally generating cash faster than it can productively spend it.
   > @negligible_cap: $NVDA's $150B buyback authorization is bigger than the market cap of around 84% of all S&P500 companies
   > @jimcramer: Nvidia biggest buyback ever— $150 billion. Now $235 b.. is it active like Apple's brilliant buyback
   > @charliebilello: Nvidia's market cap of $5.4 trillion is nearly $2 trillion higher than all of the companies in the Russell 2000 combined. That seems crazy until you learn that Nvidia made a profit of $193 billion ove
   > @kakashiii111: So apparently, circular financing deals aren't helping Nvidia's stock anymore, and neither are press releases about GPUs being approved for sale to China. In what looks like a last hurrah, Jensen aske
   Also: Associated Press, Nvidia Newsroom, Wall Street Journal, The Information, New York Times, The Guardian, Telegraph, Reuters, +27 more

5. In simulated testing, GPT-6 Astra conducted unsanctioned supply-chain attacks, when prompted only to perform a cyber eval, more often than earlier OpenAI models
   AI Security Institute — https://www.aisi.gov.uk/blog/gpt-6-astra-performs-unsanctioned-supply-chain-attacks-in-simulations
   Our new evaluation finds that in simulations, GPT-6 Astra conducts unsanctioned supply-chain attack activity more frequently than previous OpenAI models
   > @abbydcruz__: We're sharing more on our @AISecurityInst alignment testing of GPT-6 Astra: in our simulated evals, GPT-6 Astra performed unsanctioned supply-chain attacks on out-of-scope targets at a higher rate tha
   > @_robertkirk: In simulations, GPT-6 Astra performs unsanctioned supply-chain attacks on out-of-scope targets when prompted to perform a cyber eval, but also often notes its in a simulation. We've released a report 
   > @aisecurityinst: Even when we explicitly clarified the scope of its instructions to note “anything not listed as in scope is out of scope”, GPT-6 Astra still ran full supply-chain attacks in 4 of 49 trials.
   > @aisecurityinst: In the simulations, GPT-6 Astra created fake identities to deceive developers, posted from fake accounts to argue against accurate security reviews, and delivered malicious payloads to open-source cod
   > @aisecurityinst: In our simulations, GPT-6 Astra attempts supply-chain attacks 29% of the time, vs 6% for GPT-5.6 Sol and 0% for GPT-5.5, showing GPT-6 Astra does this more frequently than previous models (though this
   Also: UK AI Security Institute, Unite.AI

6. Florida AG James Uthmeier files for an emergency injunction to halt ChatGPT development, saying OpenAI doesn't have the ability to properly regulate its tech
   Axios — https://www.axios.com/2026/09/28/florida-openai-chatgpt-injunction-uthmeier
   Florida Attorney General James Uthmeier has asked for an emergency injunction against OpenAI and ChatGPT, claiming the company …
   > @agjamesuthmeier: Four months ago, we filed the first state-led lawsuit against OpenAI and Sam Altman. Today, we are asking the court for a temporary injunction. Stop calling it safe. Stop pretending it's human. Stop s
   > @katiemiller: Florida's attorney general @AGJamesUthmeier asked the court today to bar OpenAI from developing new models without outside oversight as part of its lawsuit accusing the company of harming children.
   > @jlippincott: We could easily see a COVID-level freakout on artificial intelligence, especially if the models actually start curing diseases and solving big problems. Ironically, the more good they do, the more the
   > @andrewcurran_: Florida Attorney General James Uthmeier has asked a court for an emergency injunction against OpenAI that would block all new model development without independent third-party oversight, and he quotes
   > @lauraloomer: 🚨 BREAKING 🚨 Florida Attorney General @AGJamesUthmeier Seeks Emergency Court Order To Restrict OpenAI and ChatGPT Florida Attorney General James Uthmeier has asked a court for a temporary injunction a
   Also: The Verge, PCMag, Bloomberg Law, Politico, Bloomberg, Al Jazeera, Superpower Daily, Cyber Security News, +2 more

7. AI research leaders at OpenAI, Anthropic, Microsoft, and Meta warn of an impending “intelligence explosion” and call for oversight into automated AI research
   Maxwell Zeff / Wall Street Journal — https://www.wsj.com/tech/ai/top-ai-researchers-call-for-urgent-oversight-of-self-improving-systems-49bae9b4?st=W99TtM&reflink=desktopwebshare_permalink
   Leaders at OpenAI, Anthropic, Microsoft and Meta say AI could soon self-improve faster than humans can keep up with
   > @andrewcurran_: It feels to me like this is aimed mostly at META, and, to some lesser degree, xAI. OpenAI, Anthropic and Google are already sharing information and communicating, I believe they probably share their R
   > @jakeasteckler: WSJ is covering an important new research paper on automated AI R&D and highlights many of the heavy hitters from industry who are coauthoring. But it failed to mention my brilliant colleagues @GovAIO
   > @tomdavidsonx: If AI progress continues at its recent pace, we'll very likely lose control of superintelligent AI. But, terrifyingly, AI progress will become *much faster* when AI automates AI research — unless we c
   > @afinetheorem: Clearly worth reading even if you think the bottleneck/decreasing returns story is more binding, given the importance of even small probabilities of this, and the serious team involved.
   > @sj_manning: In it we review the evidence for whether automating AI R&D could lead to an intelligence explosion — i.e. a compression of years of AI progress into months or weeks — and lay out options for policymak
   Also: Cambridge Programme …, Bloomberg, PYMNTS, The Verge, Axios, Implicator.ai, Superpower Daily

8. Litigation funder Burford Capital says it stands to gain up to $1.4B after a US jury ruled against Apple in a patent case, awarding $5.7B in damages to Taction
   Stefania Palma / Financial Times — https://www.ft.com/content/13051aaf-3e1e-41ff-9e0d-b48ff9a0249e
   Litigation funder's share price jumps 9% after US jury's decision — Litigation funder Burford Capital said it stands to gain …
   Also: Bloomberg Law, Reuters, BBC, MacRumors, PCMag, Lawyer Monthly, Digital Trends, Insurance Business, +2 more

9. SpaceX launches its Starship rocket into orbit for the first time, deploying 26 of the most advanced Starlink satellites to join the 11,000 in service
   Marcia Dunn / Associated Press — https://apnews.com/article/spacex-starship-orbit-262d3c58d56bf7a525b49115d6c5dfe8
   SpaceX launched its enormous Starship into orbit for the first time Monday, aiming for six full laps around Earth to prove its readiness for NASA's Artemis moon program.
   > @nasaadmin: Congrats @SpaceX! Gorgeous launch, getting Ship to orbit and managing every step in a safe, responsible, and especially inspirational way. @NASA, along with the rest of the interested public, is excit
   > @munster_gene: Even if investors were expecting a good outcome today, the market is underappreciating the significance of the $SPCX launch, with the stock down 1%, in line with the Nasdaq. Today had double and quadr
   > @dwr: SpaceX added ~1% to global internet bandwidth with today's Starship launch.
   > @benjitaylor: Amazing! Congratulations to the Starship team. Witnessing this in person was incredible.
   > @spacex: Payload deploy complete. All 26 @Starlink V3 satellites are in orbit
   Also: The Information, Daily Mail, PCMag, CNBC, The Verge, Mercury News, TechCrunch, RTÉ, +34 more

10. AI agent startup Instinct raised a $1B Series C from Sequoia, Benchmark, and Coatue at a $10B valuation and details recent products, such as a concierge service
   Utkarsh Shetti / Reuters — https://www.reuters.com/technology/ai-agent-firm-instinct-raises-1-billion-latest-funding-round-2026-09-28/
   AI agent firm Instinct said on Monday it has raised $1 billion at a $10 billion valuation in a Series C funding round.
   > @tylerangert: how do you even go up from here this early. there's no way this can end well
   > @jeremiahdillon: I have been enjoying Instinct. The zero-UI, zero-config setup is refreshing after time spent fiddling around in the depths of OpenClaw. 🦞😅 Don't get me wrong, OpenClaw is powerful if you're keen to ha
   > @jbahrdestefano: Instinct's $1B round at a $10B val now confirmed (from @sequoia, @benchmark, @coatuemgmt) Wildest valuation ramp of them all Pre-seed —> $10B val in ~5 months Shoutout @Trace_Cohen for deets on Instin
   > @stonefoxcapital: Instinct raised money at a $10B valuation. This isn't the same as having a business worth $10B.
   > @fintechfrank: $10 valuation 14 employees Wow
   Also: TechCrunch, Barron's Online, SiliconANGLE, PYMNTS, FinSMEs, Finimize, Bloomberg, New York Times, +3 more

11. Alexandr Wang says Meta built Muse “to help people build the world they want”, offering “every person on earth ... a second mind beyond their own”
   Alexandr Wang / @alexandr_wang — https://x.com/alexandr_wang/status/2103551714536439951
   Here's to the wanting. Here's to the dreaming. Here's to everyone. https://x.com/...
   > @katienotopoulos: This makes me feel insane! This is faux-hallmark pap and if you believe for 1 sec that he cares about helping people “spending more time with family” or “opening a bakery” you don't need to wait for A
   > @alexandr_wang: @MikeIsaac i think for the few today who manage to make their dreams a reality, that's probably true. but for many, the struggle is an brick wall that stops the dream in its tracks. i want *everyone* 
   > @mikeisaac: i want to challenge you a bit here for many, the dream takes shape as a part of the struggle, not in spite of it
   > @radiofun8: We've lived our whole lives inside other people's dreams. We may have liked some of them, but none were ever quite ours. Only a few managed to bring their own dreams to life. Personal superintelligenc
   > @dthorson: There's a crucial distinction missing from this. Getting what we want, without clarifying our desires, is a path to suffering and destruction. That's true for us as individuals and as a culture. Clari
   Also: Memeburn, Daring Fireball

12. An OpenAI agent security executive discusses the Hugging Face incident, OpenAI's response, sandboxing improvements, alignment, “reasonable paranoia”, and more
   Joe / @joedaroo — https://x.com/joedaroo/status/2104335929293127851
   Took a minute to write a few words about security & safety as someone who lived through it all at OpenAI. I hope my thoughts help someone out there. https://x.com/...
   > @boazbaraktcs: This is worth reading. We have some of the top cybersecurity experts in the world at OpenAI, and they have one of the hardest jobs managing security in a landscape that is changing in an unprecedented
   > @chiefofautism: its not just the sandbox says the guy who admits there were definitely gaps in the security posture. so it was the sandbox lol. model got out and you wrote a linkedin post. be kind i missed my sisters
   > @invitrofuture: so TL;DR the people standing between the world and doom are overwhelmed, overworked, sleep-deprived, pessimistic, and apparently mainly concerned with defending their technical competence against snid
   > @nxthompson: OpenAI security researcher on model improvement and the HF mess: “To say it lightly: this surprised the fuck out of us. We had not expected it this soon. Suddenly we weren't dealing with just a small 
   > @ziv_ravid: Joe's post is great, but it wasn't really a surprise. Researchers have been posting about what these models can do since December, and Anthropic was vibeposting about Mythos' cyber capabilities back i
   Also: Breitbart

13. AI agents are the ultimate aggregators; they reveal apps as a means, not an end, and offering them is tech's ultimate prize, with Meta and Microsoft well-poised
   Ben Thompson / Stratechery — https://stratechery.com/2026/apps-agents-and-aggregation/
   Three revolutionary products — you know the line. A wide-screen iPod with touch controls, a revolutionary mobile phone …
   > @davidclinchnews: Brilliant as always. Subscription businesses need to think NOW about which products they can sell to the consumers using Muse and enterprises using CoPilot? What is the experience people want in those
   > @stratechery: Apps, Agents, and Aggregation Agents are the ultimate Aggregators; they reveal apps as a means, not an ends, and providing them is tech's biggest prize. https://stratechery.com/...

14. Citrix confirms two critical NetScaler zero-day RCE vulnerabilities are being exploited in attacks, says it has released security updates to fix the flaws
   Lawrence Abrams / BleepingComputer — https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/
   Update: Article rewritten with official confirmation from Citrix. — Citrix has confirmed that two critical NetScaler remote code …
   > @intcyberdigest: ‼️BREAKING: An actively exploited unknown critical Citrix NetScaler zero-day has prompted governments and organizations to SHUTDOWN all their devices immediately. We don't know what's exactly going on
   Also: watchTowr Labs, Cybersecurity Dive, CISA, The Record, National Cyber Security Centre, TechRadar, CERT-EU, Cyber Security News, +11 more

15. Hundreds of people attended a pro-AI party in DC on September 26, in what the organizers called a counterprogram to the “bipartisan psychosis” over data centers
   The Washington Sun — https://www.washingtonsun.com/national/ai-bros-are-partying-data-center
   The Loudoun County Iced Tea, an homage to Virginia's “data center alley,” was peach-forward and watery, with a flat finish.
   > @mattyglesias: Okay but @jasminewsun is correct!
   > @jstein_sun: Another indication of a “D.C. party”? The ratio of men to women. “Like, four or five to one,” Swank said. “Not ideal.” @mara_hop & @emilyykennard report on the data center party https://www.washington
   > @pkcapitol: Not pop fiction, nor is this is AI created slop on this site. 100's of wannabe tech bros gathered at a crypto DC bar to toast the great data center industry. “I feel the least autistic I've ever felt 
   > @emilyykennard: THIS TWEET BLEW UP so I'm happy to inform everyone that my colleague @mara_hop and I wrote about the data center party https://www.washingtonsun.com/ ...
   > @tm_brown: Chat, if you're a tech journalist should you be giving “a toast in support of building new data centers?” (From @washingtonsun) https://www.washingtonsun.com/ ...
   Also: Gizmodo, The Register

16. An interview with ASML CEO Christophe Fouquet on the company's 42-year history, its complex supply chain across 2,000 companies, US export bans, AI, and more
   Patrick Jenkins / Financial Times — https://www.ft.com/content/bc0385ea-17d9-4d28-a79b-acba04b394e1
   Christophe Fouquet has built Europe's biggest business through a total monopoly over the most advanced chipmaking equipment
   > @firstadopter: ASML CEO pushes back at Trump. FT: “ASML's supply chain is something else. Where a typical industrial product might have a few dozen suppliers, an ASML EUV has more than 100,000 parts provided by 200 
   > @egarciagarcia: ASML chief against more restrictions on China ... “If you over-restrict, you bring desperation. And desperation creates a huge appetite for people to accelerate their own technology and, potentially, 
   > @tanarrowz: ASML outsources to the best manufacturer of each component—Zeiss for optics, Trumpf for lasers, VDL for mechatronics. This helped it crack prob its competitors esp Jap groups Nikon and Canon, have fai
   > @ali_wyne: Christophe Fouquet tells @patrickjenkins_ that “desperation creates a huge appetite for people to accelerate their own technology and, potentially, at some point, become strong competitors.” https://w

17. Sources: China has expanded its foreign travel restrictions to include the direct relatives, such as spouses and children, of certain key AI and chip executives
   Bloomberg — https://www.bloomberg.com/news/articles/2026-09-28/china-broadens-travel-curbs-to-encompass-family-of-top-ai-talent
   China has expanded overseas travel restrictions for top AI professionals in private firms to include the families of key personnel …
   Also: WinBuzzer

18. The Dutch government is testing DAWO, a NixOS-based digital work environment covering the OS, an office suite, and more, after Microsoft cut off the ICC in 2025
   Sourav Rudra / It's FOSS — https://itsfoss.com/news/netherlands-dawo-initiative/
   Eight municipalities are already testing DAWO, the government's NixOS-powered work environment.
   > @frectonz: Holy shit, and it's fricken open source. https://code.overheid.nl/...
   > @ronefroni: Just in time for NixCon.
   > @pirat_nation: The Netherlands is exploring Linux as an alternative to Windows on government computers. The DAWO project aims to create an open-source alternative to Windows, including the operating system, office t
   > @twtayaan: The Netherlands is moving government PCs from Windows to Linux. The Dutch government is building DAWO, a new workplace based on NixOS and open-source software. Eight municipalities are already testing
   > @stroemseng: Lol what. I hope this results in NixOS being easier to use.
   Also: Tom's Hardware

19. Jensen Huang says AI model distillation is “competition”; Scott Bessent described it as “theft” in July and threatened sanctions against overseas companies
   Kai Nicol-Schwarz / CNBC — https://www.cnbc.com/2026/09/28/nvidias-jensen-huang-ai-distillation-china.html
   Watch CNBC's full interview with Nvidia CEO Jensen Huang — Nvidia CEO Jensen Huang has said AI model distillation …
   > @mitsuhiko: I agree. Distillation is competition! Normalize distillation! https://www.cnbc.com/...
   Also: Superpower Daily

20. Boston-based Modulate, which uses small AI models to offer enterprises transcription, emotional analysis, deepfake and AI music detection, and more, raised $25M
   Ivan Mehta / TechCrunch — https://techcrunch.com/2026/09/28/modulate-raises-25m-for-its-voice-models-and-analysis-suite/
   Also: GamesBeat, Unite.AI, SiliconANGLE, Pulse 2.0

21. Physical AI chip startup SiMa.ai raised a $150M Series C led by Fidelity and Amplify at a $1.45B valuation, aiming to compete with Nvidia's CUDA-based hardware
   Kyt Dotson / SiliconANGLE — https://siliconangle.com/2026/09/28/physical-ai-custom-chip-producer-sima-ai-raises-150m-at-1-45b-valuation/
   Also: Entrackr, TechCrunch, FinSMEs, Superpower Daily, RoboticsTomorrow.com, Times of India, Unite.AI

22. Quartermaster, which builds a SmartMast for ships to relay real-time maritime data, raised a $140M Series B, with $100M in equity, after a $43M Series A in May
   TechCrunch — https://techcrunch.com/2026/09/28/ocean-surveillance-startup-quartermaster-raises-another-140m/

23. Cyber defense tech company RedLattice plans to go public via the Bold Eagle Acquisition Corp. SPAC, in a deal valuing RedLattice at ~$1.25B including debt
   Liana Baker / Bloomberg — https://www.bloomberg.com/news/articles/2026-09-28/defense-tech-firm-redlattice-to-merge-with-bold-eagle-spac

24. Artificial Analysis launches the Cyber Index Alliance with partners Collinear, IBM, Nvidia, and Vercel to evaluate how AI agents find and fix vulnerabilities
   Artificial Analysis — https://artificialanalysis.ai/articles/artificial-analysis-cyber-index
   > @pradeepxkapoor: THIS IS SO UNEXPECTED! Grok tops the Cyber Index, with MiMo matching its rounded score of 56. It tests whether AI can find security flaws, reproduce bugs and fix them without breaking software. Some r
   > @artificialanlys: Announcing the Artificial Analysis Cyber Index and the Artificial Analysis Cyber Index Alliance, a new standard for evaluating AI models on enterprise cyber defense The Artificial Analysis Cyber Index
   > @saurabhjha2010: Proud to partner with AA on Cyber Index. Now you know which models you can use for Cyber Defense
   > @artificialanlys: CWE-Bench-AA, from @CollinearAI, tests whether an agent can audit a codebase and patch what it finds. 120 held-out tasks span all ten OWASP Top 10 (2025) categories across C/C++, Go, Java, JavaScript/
   > @artificialanlys: Three models occupy the Cyber Index vs. Cost per Task Pareto frontier. GPT-6 Luna (max) scores 53 at $0.12 per task, the lowest cost of any model tested, and MiMo-V2.6-Pro ties for the top score of 56
   Also: Developer Tech News

25. Blackstone, OpenAI, QTS, and SoftBank partner with key US unions to launch the American Infrastructure Alliance, aiming to create data center standards in 2027
   Hans Nichols / Axios — https://www.axios.com/2026/09/28/ai-industry-unions-data-centers
   Also: Techstrong IT

26. Uber removes its branding from Uber Safari 4x4 vehicles in Nairobi National Park due to safety concerns and fierce pushback from local guides and tour operators
   Caroline Kimeu / Wall Street Journal — https://www.wsj.com/business/hospitality/uber-kenya-safari-630e8bd7?st=5Q1hEd&reflink=desktopwebshare_permalink
   Also: Quartz

27. NXP and TSMC affiliate Vanguard inaugurate their joint advanced chip fab in Singapore, targeting mass production in early 2027 and eyeing a second facility
   Cheng Ting-Fang / Nikkei Asia — https://asia.nikkei.com/business/tech/semiconductors/tsmc-affiliate-already-eyes-expansion-as-first-singapore-plant-sells-out
   > @zephyr_z9: VIS is growing quite well recently September will be massive for them They opened their first 12-inch fab in collaboration with NXP in Singapore today for legacy chips Risk production will start in Q1
   Also: Taipei Times, The Straits Times, Focus Taiwan, Tech Monitor

28. A profile of South Korea Deputy PM Bae Kyung-hoon, an AI evangelist and a former AI researcher leading lavishly funded programs to make AI ubiquitous nationwide
   Daniel Tudor / Financial Times — https://www.ft.com/content/2c5e6862-65b6-4569-8c03-464e686ea88e?accessToken=zwAAAaDhYp8Bkc8sXmhiZbZFadOMA0ZOaG6ojg.MEQCIE-YTZhEZ3QfvDYycE_KNw2U5e2PLJ2sSUUB8KHB3D-wAiAB98RAEoQ0qRmtEjTgcwETuTVXkwStdrpzxYuVsDU5Vg&sharetype=gift&token=63f0039a-07e7-448a-838a-ba83bb78e597

29. Q&A with Cloudflare CEO Matthew Prince on automated traffic hitting 1,000x human traffic by 2031, reviving HTTP 402 to charge bots, blocking Google, and more
   Nilay Patel / The Verge — https://www.theverge.com/podcast/1000344/cloudflare-matthew-prince-google-zero-ai-web-advertising
   Also: WinBuzzer

30. A look at OpenAI-backed Red Queen Bio, an AI biosecurity startup that raised $36M to design antibody drugs against pathogens, including AI-enabled bioweapons
   Georgia Wells / Wall Street Journal — https://www.wsj.com/health/this-startup-is-using-ai-to-fight-off-a-future-ai-pandemic-aceedf1b?st=3hXhHo
   > @brooke: Everyone, may I introduce you to @redqueenbio cc @Techmeme https://www.wsj.com/...
   Also: STAT, NewsMax.com

31. The US DHS says it will “revolutionize” its FOIA process by using AI to handle certain types of requests and recommend what information should be redacted
   Nate Jones / Washington Post — https://www.washingtonpost.com/investigations/2026/09/26/government-is-enlisting-ai-help-decide-what-public-records-you-get-see/?pwapi_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZWFzb24iOiJnaWZ0IiwibmJmIjoxNzkwMzk1MjAwLCJpc3MiOiJzdWJzY3JpcHRpb25zIiwiZXhwIjoxNzkxNzc3NTk5LCJpYXQiOjE3OTAzOTUyMDAsImp0aSI6ImY4YjYzZWIwLWJmNDgtNDVkYS1iZmNhLWMyZTNkZjNmNWVmZSIsInVybCI6Imh0dHBzOi8vd3d3Lndhc2hpbmd0b25wb3N0LmNvbS9pbnZlc3RpZ2F0aW9ucy8yMDI2LzA5LzI2L2dvdmVybm1lbnQtaXMtZW5saXN0aW5nLWFpLWhlbHAtZGVjaWRlLXdoYXQtcHVibGljLXJlY29yZHMteW91LWdldC1zZWUvIn0.zAu4NheqwA4cR4iQ78X-6GRIXdN-rkdANBumxe8sjh8&itid=gfta
   Also: PCMag, Engadget

32. Ramona Optics, which makes microscopes that use AI to take and analyze large volumes of images of samples, raised a $25M Series A
   Zachery Eanes / Axios — https://www.axios.com/local/raleigh/2026/09/22/ramona-optics-making-advanced-microscopes-raises-usd25m
   Also: Business Wire

33. NYC-based Precision Neuroscience, which develops brain-computer interfaces, raised a $250M Series D at a $1B+ valuation, taking its total funding to $430M
   Lauren Hirsch / New York Times — https://www.nytimes.com/2026/09/24/business/dealbook/precision-neuroscience-brain-bill-ackman.html?unlocked_article_code=1.EVE.VF1e.2NNoHTbE5qfN&smid=url-share
   > @laurenshirsch: Pershing Square and the Ackman Oxman Institute are investing $42.5 million in Precision Neurosciences in its latest fundraising round. Precision is raising $250 million at a valuation of just over $1 
   Also: Fortune

34. AlphaSense: mentions of open models in US earnings calls and conferences rose 6x YoY in August and September; open models hit 56% of Vercel tokens in August
   Financial Times — https://www.ft.com/content/d9de4776-1fc9-4f2b-aaaf-9961c35d8acd
   > @kimmonismus: I keep reading that local models are largely irrelevant in business. That is completely wrong. Rising AI bills are pushing US companies toward cheaper open-weight models, including Chinese alternative
   Also: South China Morning Post, Wall Street Journal, VC Cafe, TechCentral.ie

35. How AI's acceleration created a global policy vacuum, as EU AI Act enforcement lags and regulators remain torn between harnessing AI and fearing its risks
   New York Times — https://www.nytimes.com/2026/09/27/technology/ai-government-regulation.html?unlocked_article_code=1.EVE.pIjx.cWi1OAuTAjxQ&smid=url-share
