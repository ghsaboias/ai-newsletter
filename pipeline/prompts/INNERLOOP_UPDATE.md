# Innermost Loop Daily Article — Generation Instructions

Generate a daily article in the style of **The Innermost Loop** by Dr. Alex Wissner-Gross. The article should be indistinguishable from a real edition. Save it to `pipeline/output/YYYY-MM-DD.md` with the same frontmatter format as existing files.

## Reference Material

Read 3-5 recent posts from `pipeline/output/` before writing. These are your style bible. Match them exactly.

**Always read yesterday's post.** The blog has running narrative threads that carry across days — the Dyson Swarm, OpenClaw/lobsters, agent wallets, Musk's lunar plans, etc. Don't repeat yesterday's stories. Do pick up ongoing arcs and advance them with new developments.

## Structure

### Title
Always: `Welcome to [Month] [Day], [Year]`

### Opening Line
A single provocative metaphorical sentence about "the Singularity" that ties to the day's most striking story. Pattern: "The Singularity is/has/now [vivid metaphor]."

Examples from real posts:
- "The Singularity is having babies."
- "The Singularity just bought a 30-second spot."
- "The Singularity is now a subscription service with ads."
- "The bootstrap phase of the Singularity is complete."
- "Humans are becoming marionettes for the Singularity theater."

### Body
5-8 thematic paragraphs. Each paragraph:
1. Opens with a **bold thematic claim** (one sentence, no link)
2. Chains 3-6 stories together with **inline links on key phrases**
3. Weaves stories into a narrative arc — not a bullet list disguised as prose

Paragraphs should feel like a single flowing argument supported by evidence, not a collection of items. Stories within a paragraph should relate to each other.

### Closing Line
A standalone single-sentence paragraph. Punchy, wry, sardonic. Often callbacks to the opening metaphor or a philosophical twist. These are the signature of the blog.

Examples:
- "The agents have their own wallets now, so at least they can chip in for the electricity."
- "We are scaling intelligence until we clip through the walls of reality."
- "The Singularity is automating the mind, but it still has to rent the body."
- "However, American lobsters also live on the ocean floor and are known to be very territorial."
- "When the Church blesses the compute and the agents are raising their own young, the only real question left is whether the Singularity will remember to close its own car doors."

## Thematic Categories

Cover 5-8 of these per article (not all, and not always in this order):

1. **AI capabilities** — new models, benchmarks (HLE, SWE-bench, ARC-AGI, Codeforces Elo), autonomy time horizons, reasoning breakthroughs
2. **Agentic economy** — AI agents acting autonomously, agent-to-agent commerce, OpenClaw ecosystem, MoltCourt/Moltbook, agent wallets
3. **Recursive self-improvement** — AI designing AI, models improving their own training, algorithmic breakthroughs
4. **Scientific automation** — AI solving physics/math/biology, automated labs, drug discovery
5. **Hardware & compute** — chips, data centers, energy consumption, memory costs, optics, new architectures
6. **Space & orbital compute** — Dyson Swarm, SpaceX, lunar plans, orbital data centers, satellite launches
7. **Economics & labor** — job displacement, capex figures, funding rounds, IPOs, valuations, market moves
8. **Robotics & physical AI** — humanoids, autonomous vehicles, drones, manufacturing
9. **Biotech & longevity** — gene therapy, aging research, drug discoveries, BCI (Neuralink)
10. **Geopolitics & military** — defense AI, surveillance, drone warfare, chip export controls
11. **Ontological shock** — UAP/UFO disclosures, congressional testimonies (recurring minor theme, usually last or second-to-last paragraph)

## Voice & Tone

- **Accelerationist but not naive** — treats the Singularity as inevitable and already underway, not aspirational
- **Sardonic humor** — dry wit, especially in closings. Finds absurdity in juxtapositions (e.g., Waymo launches autonomous driving AND pays gig workers $11.25 to close car doors)
- **Dense and specific** — every claim is linked. Uses exact numbers: percentages, dollar amounts, Elo ratings, word counts, time horizons
- **Narrative, not listicle** — reads like dispatches from the front line of the intelligence explosion, not a news roundup
- **Metaphors from unexpected domains** — biology ("debugging the biological runtime"), religion ("the Church blesses the compute"), gaming ("clip through the walls of reality"), warfare, architecture
- **Named actors** — drops specific names: Musk, Altman, researchers, companies. Never generic "a company" when you can name them
- **Present tense, active voice** — "X launches" not "X has launched" or "X announced the launch of"
- **Juxtaposition as a signature move** — the best sentences pair a grand claim with an absurd or contradictory detail in the same breath. Examples: "Waymo is launching fully autonomous operations... though it is simultaneously paying DoorDash gig workers $11.25 to close robotaxi doors left ajar." / "Anthropic's Chief Product Officer confirms 100% of code is now written by Claude... companies have started selling kawaii enclosures for Mac minis." This tension between the sublime and the ridiculous is core to the voice.

## Link Density & Formatting

- **20-40 inline links per article** — nearly every factual claim links to a source
- Links go on the most descriptive phrase, not on "here" or "this"
- Sources: X/Twitter, ArXiv, Bloomberg, Reuters, WSJ, FT, NYT, Nature, Science, Cell, TechCrunch, The Verge, company blogs, government filings (FCC, FDA, DOE)
- X/Twitter posts are a primary source — the author follows AI/tech accounts heavily
- Format: `[descriptive phrase](url)` — the linked text should make sense even without clicking

## Word Count

Target: **550-800 words** for daily posts. Err on the side of density over length.

## Research Process — BE THOROUGH

This is the most important section. The quality of the article depends entirely on the breadth and depth of your research. **Do not cut corners. Do not stop after 3-4 searches. You need 20-40 real, linked stories to write a good article.**

### Tools Available

- **`bird search "query"`** — Search X/Twitter. This is a PRIMARY source for the blog. The real author follows AI/tech Twitter heavily. Use `bird read <url>` to fetch full tweet content.
- **Exa MCP tools** (`mcp__exa__web_search_exa`, `mcp__exa__get_code_context_exa`) — Web search optimized for AI/tech content. Use for finding news articles, blog posts, papers.
- **WebFetch** — Fetch and extract content from specific URLs. Use to verify stories, get details from articles found via search, and confirm links are real.
- **WebSearch** — General web search. Use alongside Exa for broader coverage.

### Search Strategy

**Use parallel searches for speed.** When you're searching across different topic areas, batch them — launch multiple bird, Exa, and WebSearch calls in the same message instead of waiting for each one to return. This saves significant time and avoids the temptation to stop searching early once you have a few good stories.

**Phase 0: Map the landscape**

Before doing any targeted searching, figure out what actually happened today. Run a small batch of searches to get the lay of the land.

**Tool strengths (learned from testing):**
- **Techmeme (`WebFetch https://www.techmeme.com/`)** — The single best landscape tool. Returns curated, high-signal tech headlines with URLs. Start here.
- **Exa (`mcp__exa__web_search_exa`)** — Strong for finding dated news articles. Use **single-topic queries** — combined multi-topic queries lose focus and only return the strongest signal. Good: `"AI agents autonomous economy"`. Bad: `"SpaceX robotics energy data center nuclear"`.
- **bird** — Useless for broad queries like `bird search "AI"` (returns global noise in every language). Excellent with **specific terms** and **`from:` queries** for key people. Save for Phase 1.
- **WebSearch** — Weak for daily news (returns trend roundups and prediction articles). Use as a last resort supplement.
- **ArXiv listing pages** — Low signal. Don't fetch the listings page. Instead, search for specific paper topics via Exa when you find a story that references a paper.

```
# Phase 0 searches (run in parallel)
WebFetch https://www.techmeme.com/     # curated tech headlines — start here
mcp__exa__web_search_exa "AI news [current date]"
mcp__exa__web_search_exa "AI model benchmark release [current date]"
mcp__exa__web_search_exa "AI funding startup raised [current date]"
mcp__exa__web_search_exa "robotics autonomous vehicles [current date]"
mcp__exa__web_search_exa "biotech longevity research [current date]"
mcp__exa__web_search_exa "space launch energy data center [current date]"
```

Scan all results. Identify the 8-12 actual stories of the day — model launches, funding rounds, papers, policy moves, weird agent behavior, whatever is actually making noise. Write down a quick mental map of what happened. This is your story list. Phases 1-3 are about going deep on these stories, not discovering them from scratch.

**Phase 1: Targeted deep dives**

Now that you know what happened, search specifically for each story to get sources, numbers, quotes, and adjacent context.

**bird shines here** because you now have specific terms from Phase 0. Two tactics that work:

1. **`from:` queries** for key people — gets their actual tweets, not random mentions. The blog quotes founders and researchers directly.
2. **Specific product/story names** — gets the X/Twitter reaction and discussion around known stories.

```
# X/Twitter — search for specific stories found in Phase 0
bird search "from:sama"              # Sam Altman
bird search "from:DarioAmodei"       # Dario Amodei
bird search "from:elonmusk AI"       # Musk on AI topics
bird search "from:demaborsa"         # Demis Hassabis
bird search "[specific product name from Phase 0]"
bird search "[specific company announcement from Phase 0]"

# Web — go deeper on specific stories
mcp__exa__web_search_exa "[specific company] [specific announcement]"
WebFetch on article URLs from Phase 0 to get full details, quotes, numbers
```

**Key accounts the blog frequently cites** (search with `from:` when relevant):
`sama`, `elonmusk`, `scaling01`, `chatgpt21`, `metr_evals`, `epochairesearch`, `arcprize`, `polynoamial`, `OpenAI`, `AnthropicAI`, `GoogleDeepMind`, `xaborsa`

Adapt to the actual stories of the day. The point is: Phase 0 tells you WHAT to search for. Phase 1 is WHERE you get the details.

**Phase 2: Follow up on promising leads**
- Use `bird read <url>` to get full context on interesting tweets
- Use WebFetch on article URLs to extract details, quotes, and numbers
- Search for adjacent stories that connect to what you've found

**Phase 3: Verify and fill gaps**
- Check which thematic categories you're missing — search specifically for those
- Verify every URL you plan to include actually works
- Look for the weird/surprising stories that make the closing one-liner land

### Source Categories (search for news from the current date and previous 24 hours)

- **X/Twitter**: AI researchers, founders (Musk, Altman, Dario Amodei, Demis Hassabis), labs (OpenAI, Anthropic, Google DeepMind, xAI, Meta AI), AI benchmark accounts, scaling01, chatgpt21, metr_evals, epochairesearch
- **ArXiv**: new papers in cs.AI, cs.LG, cs.CL
- **Tech press**: TechCrunch, The Verge, Ars Technica, Wired
- **Business press**: Bloomberg, Reuters, WSJ, FT, NYT business/tech sections, CNBC
- **Science journals**: Nature, Science, Cell (for biotech/health stories)
- **Government**: FCC filings, FDA approvals, DOE announcements, congressional hearings
- **Company blogs**: OpenAI, Anthropic, Google DeepMind, Meta AI, Nvidia, SpaceX

### Minimum Bar

You should have **at least 25 candidate stories** before you start writing. You'll use 20-40 of them. If you have fewer than 25, you haven't searched enough — go back and search more. The real articles are extremely dense with links. A thin article with 10 links is a failure.

Focus on stories that fit the Singularity narrative — breakthroughs, milestones, economic disruption, physical infrastructure scaling, and the weird edges where the future leaks into the present.

## What NOT to Do

- Don't write a bullet-point news digest — this is narrative prose
- Don't editorialize with caveats like "it remains to be seen" or "time will tell" — the author writes with conviction
- Don't use filler phrases ("it's worth noting," "interestingly," "in a significant development")
- Don't soften claims — if a benchmark is SOTA, say SOTA
- Don't skip the closing one-liner — it's the signature
- Don't use the same opening pattern two days in a row — check the previous day's file
- Don't fabricate links — every URL must be a real, verifiable source found during research. If you can't find a source, drop the claim
- Don't include subscription widgets, images, or promotional content

## Output Format

Save to `pipeline/output/YYYY-MM-DD.md`:

```markdown
---
date: YYYY-MM-DD
url: (leave empty — this is a generated article)
title: "Welcome to [Month] [Day], [Year]"
wordcount: NNN
generated: true
---

# Welcome to [Month] [Day], [Year]

[Article body]
```

The `generated: true` field distinguishes generated articles from fetched originals.
