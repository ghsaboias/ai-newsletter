# Editorial Principles

The distilled, deduplicated voice/writing spec for the AI/Tech newsletter (PT-BR). These are the patterns Gui applies by hand in review, folded back so future drafts need fewer corrections — v2 roadmap task #6 ("draft voice = zero human corrections") calls this trail *the spec*.

This file is the **actionable rules**. The dated provenance — each edition's specific before→after edits — lives in [editorial-review-log.md](editorial-review-log.md). The repo `CLAUDE.md` carries the 9 canonical numbered "Editorial Principles"; this expands them with the accumulated detail.

> Voice in one line: **neutral, dense, factual. Show, don't tell. Cut anything that doesn't carry the news.**

---

## 1. PT-BR language quality

**De-calque, but keep crisp English terms.** The tension resolves cleanly: a bad PT calque of an English term reads *worse* than the original → keep the English (italic) + gloss once. A common PT word exists and is clearer → use PT.
- **Keep English (italic), gloss once:** *valuation*, *hyperscalers*, *exploit(s)*, *post-money*, *yield*, *stealth* (out of "modo furtivo"), *marketplace*, *cap table*, *input*. Also consecrated terms that need no italic: framework, wafers, IPO (prefer the crisp "IPO" over empolada paraphrases like "o que seria a maior estreia em bolsa").
- **Use PT (the calque confuses):** "compute" → computação/processamento; "in-house" → próprios; "target" → alvo; "market cap" → valor de mercado; "keynote" → apresentação; "blueprint/toolkit/reference platform" → keep the English term + short gloss rather than "projetos de fluxo"/"projeto-referência"; "command and control/C2" → keep, don't invent "comando-e-controle"; "die" → chip; "firmas" → empresas; "lista negra" → "lista de empresas sancionadas"; "chips customizados" → "chips sob encomenda".
- **"coding" ≠ "codificação".** In tech context "coding" = **programação** (or desenvolvimento). "Codificação" is *encoding*. See the always-apply lexical substitutions below.

**Always-apply lexical substitutions** (baked into `generator.md`'s "Léxico:" line as of 2026-07-02; still worth a check on the shipped edition):
- **codificação → programação** (and inflections: "codificação agêntica" → "programação agêntica", "modelos de codificação" → "modelos de programação").
- **ante → contra** — **only** the standalone preposition in a numeric/contrast comparison ("ante 3mi em abril" → "contra 3mi"). ⚠️ Whole-word only: never touch *antes, diante, mediante, importante, gigante*. And this is comparative-only — a *causal* "ante" ("ante o aperto americano") wants "frente ao", not "contra". Don't unify blindly.
- **modo furtivo → *stealth*** (italic): "saiu do modo furtivo" → "saiu do *stealth*" (Gui confirmed *stealth* over PT "sigilo", 2026-07-02).
- ⚠️ Whole-word/accented-form only. **Never rewrite URL slugs** — "codificação" is the accented prose form; a slug like `.../codificacao-agentica-...` is ASCII and rewriting it breaks the DJ link.

**Gender / preposition / crase concordância** (recurring correction — apply case by case):
- Gender: **a** Stripe, **a** Bloomberg, **a** assistente, **a** variante, **a** Google (⚠️ see the unresolved note below), IA avançad**a**, **as** LLMs / **nelas** (feminine for LLMs), **a** primeira CPU (fem), **o** seed (masc), sul-corean**a** Mirae Asset. Drug names in "-ida" are feminine: **a** semaglutida, **a** retatrutida.
- Preposition/crase: **na** Computex/Computex é feminina, **em** Ohio (not "no"), terceirizar **à** Samsung (crase), qualificou **como** (not "de").
- ⚠️ **Unresolved: "a Google" vs "o Google".** The 06-09 edition ended up inconsistent (changed one "a Google"→"o Google" but left "da Google", "A Google encomendou" feminine). **Not a rule** — ask Gui which gender to fix for "Google" when it comes up.

**Verb tenses.** Prefer simple past to compound/mais-que-perfeito ("já havia escapado"→"escapou"; "dissera"→"disse"; "já liderara"→"já liderou"). Present tense loose in a past narrative ("a guerra força")→past ("forçou"). Interrupted ongoing action → progressive ("estava sendo preparado", not "era preparado"). Condicional → futuro when the fact is firm ("que somaria"→"que somará").

**Numbers & currency.** Always **US$** not `$` (US$2 bilhões, US$46K). Spell out abbreviations in prose: `~$1T`→"aproximadamente 1 trilhão", 1M tokens→"1 milhão de tokens", "8 mil"→"8.000". Use **settlement** prices, not intraday. Round volatile numbers when the precision isn't the point ("caiu 8,58% para US$67.206"→"caiu para a faixa de US$67.000").

**Bad verbs / register.** "protocola"→"registra"; "despejou"→avoid; "colocou na rua"→awful; "sobretaxa"→"tarifa adicional"; "amargou um prejuízo"→neutral ("teve/registrou um prejuízo"); "sequestradas" (contas)→"roubadas"; "costurado por Washington"→"mediado". Tighten prolixity: "a alternativa a depender só da Nvidia"→"alternativa além da Nvidia".

**Crypto:** self-custodial wallets → **"carteira de auto-custódia"** (com hífen), never "wallet self-custodial"/"não-custodial". If explaining: "chaves privadas sob controle do usuário."

---

## 2. Naming & attribution

- **Identify people & companies on first mention.** "Suleyman"→"Mustafa Suleyman, CEO de IA da Microsoft e cofundador da DeepMind"; "Tower Semiconductor"→"fabricante israelense de chips". An unknown company always gets a one-clause description ("say what the company does"). A fund is "o fundo americano CRV", not "a americana CRV".
- **Identify foreign officials on first mention:** "Jaishankar"→"o chanceler indiano S. Jaishankar".
- **But do NOT gloss household names.** Anthropic, OpenAI, Google, DeepSeek dispensam aposição — a gloss on a recognizable name is noise that delays the lead. (Remove "A Anthropic, criadora do Claude," → "A Anthropic".)
- **Expand niche acronyms on first use:** ISW (Institute for the Study of War), FDA (agência reguladora de remédios e alimentos dos EUA). Well-known ones (ONU, EUA, OTAN) don't need it.
- **Normalize confusing place names:** "região de Leningrado"→"região de São Petersburgo" (the reader must map to the same place named elsewhere in the story).

---

## 3. Jargon: gloss once, decode don't calque

- **Gloss each term inline on the FIRST mention only** — never twice in the same doc.
- **Decode to the reader's language, not the paper's:** "sistema bifásico sem água"→"um fluido não-condutor que absorve o calor fervendo em contato com o próprio processador"; "anticorpos que tornam o paciente refratário aos tratamentos padrão"→"anticorpos que o corpo cria e que anulam o tratamento padrão". Put the *why*/plain meaning before the technical term.
- **Gloss vs omit — judgment call.** Sometimes glossing the clinical detail is right ("uso adjuvante (a terapia após a cirurgia, para reduzir o risco de o câncer voltar)"); sometimes the detail is pure noise and you **omit** it ("câncer de pulmão de células não-pequenas, não-resecável ou metastático"→"um tipo específico de câncer de pulmão"). The reader is tech-literate, not a clinician.
- Terms that have needed glosses: MoE, SPAC, DUV, FBA, RLHF, spread, HBM (memória de alta largura de banda), fase 2/3, switch Ethernet, confidential compute.
- **Don't gloss the same jargon the generation itself introduced** — half of some reviews is decoding calques the draft *created*. Fix that at generation.

---

## 4. Trimming — cut padding & secondary detail

The single most recurring lever. Default toward the trimmed form.

- **Cut qualifiers that don't change the fact:** "plurianual/plurianuais" (3× in one doc), "firme" (encomenda firme→encomenda), "marcados em fevereiro"→"de fevereiro", "em proclamação de setembro"→"em setembro", "modelos de fronteira com capacidades"→"modelos com capacidades". Same family as anchor-shortening.
- **Cut secondary market-reaction color — often whole sentences.** Oil-cos %s (Shell -4,5%, Equinor -5,9%…), gold, Russell 2000 records, "SK Hynix subiu 7%", ETF outflow tallies, Brent intraday moves. The fact is the deal/decision/product, not how the market reacted. Often the whole secondary paragraph goes (keep the OPEC+ quota, drop the price paragraph).
- **Cut war box-scores.** "disparou 681 armas, 70 mísseis e 611 drones, maior salva da guerra… abateu 632 dos 681" → just what/where ("atacou as regiões de Kyiv, Dnipro e Kharkiv"). Interception stats, weapon tallies, "largest of the war" framing = recurring noise on Russia-front stories.
- **The recurring Anthropic-fundraising cut.** "A Anthropic captou US$65bi… avaliação pós-money de US$965bi e arquivou pedido de IPO…" gets cut when the story is something else (the lease/1GW, the S-1). This exact sentence recurs and recurs — cut it.
- **Cut low-signal detail even when correct:** FOLFOX6→"quimioterapia", companion-diagnostic ("detectadas em teste autorizado"), the 2nd half of a two-part stat, specific interception routes, redundant openers.
- **Kill low-signal items whole, no guilt** (CLAUDE.md #9): a weak startup item (Reactor, Nobitex, Vingroup at US$12,75M) leaves entirely. But **don't over-cut** — a good stat adjacent to repeated content shouldn't get axed with it (Waymo's 400k rides wasn't repeated, just next to repeated content).
- **When an aposto creates ambiguity and the number is secondary, cut > rewrite.** (06-09: cutting SpaceX's "US$1,75 trilhão" valuation both trimmed and resolved a "que"-attachment ambiguity.)

---

## 5. Framing — no editorializing

- **No frase-moldura / "pigarro analítico."** Don't open a paragraph with an interpretive topic sentence that announces meaning before the facts ("A mudança reflete lições recentes de combate."). Signature: abstract subject (A mudança/O movimento/Esse cenário) + interpretive verb (reflete/revela/marca/sinaliza) + vague deep-sounding object. **Open with the fact itself** — it's the thesis, shown not told. When tempted to write a setup sentence, delete it and check what was lost (usually nothing).
- **No authoritative closing quote** as editorial punctuation ("Jensen Huang chamou de 'ponto de inflexão'"). Weave the quote into the sentence as a subordinate clause, or cut it.
- **Max one editorial punchline per edition** (short declarative closer). Had three ("esse é o nível de alerta", "a volatilidade é a mensagem") — keep the strongest, cut the rest.
- **Neutral verbs, de-dramatize.** "já vem puxando à frente"→"vem à frente"; "nos estertores finais"→"na reta final"; "a pedido de Trump"→"por mediação do presidente dos EUA, Donald Trump" ("a pedido" implies subordination; "mediação" is the real role). Soften superlatives the generation states flatly ("liderou os rankings"→"apareceu perto do topo").
- **No meta-references to the newsletter's own prior coverage** — never "nas últimas edições", "noticiado aqui", "como vimos". Continuity is implicit: convey it through angle/framing (lead with what's new, trim known background), not verbal callouts. (Acknowledging continuity as a *fact* — "Dois dias depois…" — is fine; it's the self-reference that's banned.)
- **Don't present plans as done:** "anunciou a fusão" vs "plano de fundir"; "aprovou investimento + planeja centro" = promise, not fact.
- **Don't frame unrelated launches as reactions** ("respondeu com"→"lançou"). **Don't editorialize political positions** as deficiencies (CLAUDE.md #2).

---

## 6. Structure & layout

- **≥3 parallel items → bullets, with the proper noun in bold as the label.** Lead-in sentence that introduces + bullets (or just header + bullets). The bullet body does **not** repeat the name (the label is the subject); the link anchor migrates from the name to the description. Label = proper noun, not category ("MAI-Thinking-1", not "Modelo próprio"). Bullets + `**bold**` pass cleanly through pandoc→Substack. A parallel list of **policy asks/items** (not entities) uses bullets **without** bold labels.
- **One concrete topic per header — kill composite "& " headers.** "Modelos & adoção"→"Modelos"; "Data centers & quântica"→two headers. If a cut leaves a paragraph with one topic, rename the header to match ("Fronteira"→"Computação quântica"). A distinct beat gets its own header (GitLab layoffs out of "Captações").
- **Split dense blocks that "breathe badly."** Divide a long single block into two even within one theme; cut the forced seam ("Na fabricação,", "Já a GitLab"). To keep one header over two paragraphs, open the 2nd paragraph (no bold) with a transition ("Em capital de risco,").
- **Salad paragraphs:** redistribute each unrelated item to the paragraph where it fits thematically. Stories live with their thematic neighbors (CLAUDE.md #8).
- **Lead with the strongest story.** The most dramatic/visual item rises to the top (right after the anchor), even if it breaks thematic grouping. Driver = story strength, not matching the subtitle's order.
- **Section order = TASTE, not a rule.** Gui reorders edition-to-edition by judgment (often leading with AI over geopolitics). **Do not codify** "geopolitics always last" anywhere. The generator's order is a starting point, not the contract.

---

## 7. Link boundaries

- **Narrow the anchor to the headline phrase, not the whole clause.** The link covers the citable/quantitative fact; the contextual description stays as prose *outside* the bracket. "`[anunciou … comprar a Ona, startup de orquestração para agentes]`" → "`[anunciou um acordo para comprar a Ona]`, startup de orquestração…". Glosses, em-dashes, investor lists, attributions all go outside the brackets. Only shift the bracket boundary — keep word order and punctuation.
- **Link to the named primary source.** If the prose says "segundo The Information", link The Information, not the aggregator that quoted it.
- **Don't give the link to an unverifiable "segundo a empresa" self-claim** — link the fact, not the boast.
- ⚠️ **Generation bug — watch for `]((`.** The generator has emitted double-paren markdown links `[texto]((url))` (breaks the link). Sweep for `]((` in finalize/review — pandoc/Substack won't fix it.

---

## 8. Opening line / subtitle

- **The opening line doubles as the Substack subtitle** (max ~180 chars). Use abbreviations to stay tight (US$2bi, 5GW).
- **Lead with the AI/tech story**, follow the edition's own order (lead first). Don't pack everything — cut the most tangential item (dropped: oil price detail, French-wine tariff).
- Open with a concrete image, not an abstract triple-noun inventory ("A corrida por X, Y e Z segue acelerando"). Avoid "enquanto" as the opening connector (overused).
- **Don't repeat a claim the body already makes** ("e supera a OpenAI" leaves the subtitle if "mais valiosa" is in the text). Cut intermediate steps that dilute a comparison (US$10bi → US$47bi, drop the middle US$30bi).
- **Don't repeat subtitle words in the first paragraph** (subtitle "libera" → paragraph "lançou").

---

## 9. Repetition & tiering (running stories)

- **Day 2+: brief-reference treatment** — don't re-explain premises readers know. **Day 4+ (e.g. Iran/Hormuz): cut context entirely.** Fold a recurring stat into a subordinate clause instead of a standalone premise-re-establishing sentence.
- **Don't re-report a price move as today's news.** If price barely moved, drop it — the event (IEA release, OPEC decision) is the story, not the price. Acknowledge a multi-day trajectory rather than presenting the level as new.
- **A legit continuation with genuinely new confirmed facts can stay** even with overlapping framing — that's Gui's call, not an automatic cut.
- **Tiering: Grandes are CAPPED AT 3, no fixed count.** The writer picks the number within the cap by the day's stories — usually 3, fewer (2 or 1) on a thin/repetitive day, **never more than 3**. Never pad to a number; never drop a real lead to fit a quota. (Was a hard "exatamente 3" gate; loosened 2026-07-01.)
- **No-re-lead rule.** A story whose core event already led as a Grande in the last ~5 editions demotes to Média — unless a genuinely new, *dated in-window* development leads instead (reframed). The generator now gets `RECENT_GRANDES` (last ~5 editions' `###` headlines) to check against.
- **Freshness = the event, not the article.** A fresh write-up of an old/known buildout does NOT qualify as a Grande. Name the dated in-window event or drop. An **aggregator-only** story with no primary/tier-1 source is a red flag → Média-max or a drop, not a Grande. (Both 2026-07-01 wrong-Grande errors — a repeated Korea megaproject and a stale ByteDance data-center rehash — trace to these.)
- **Roundup-article date trap:** a "45K layoffs in 2026" article dated today bundles events from weeks ago. Check individual event dates, not the article date.

---

## 10. Paywall teasers — must NOT give away the news

Vini's call (2026-07-07, Gui agreed): a teaser that names the subject + full action **is** the headline, so the free block gives no reason to click. Don't deliver 100% of the news above the cut.
- **Omit the protagonist's name.** "Tencent lança modelo…"→"Novo modelo de IA de código aberto que supera os melhores atuais." Swap the subject for a generic descriptor (nationality "chinês", category "uma empresa de data center nos EUA").
- A well-known **counterparty** may stay as bait if it doesn't identify the story ("…fecha acordo com a Anthropic").
- **Aggregate** same-category paid stories into one umbrella line (several fundings → "Principais rodadas de investimento em startups"). No duplicate category labels (don't ship three "Capital." lines).
- Prefer **noun-phrase fragments + `que…` relative clauses** over full subject+verb headlines. **Fewer teasers, deliberately vaguer.** Vagueness must stay accurate (no "fusão empresarial"→"fusão nuclear").
- **Don't tease the "Leia também" tail.** (Encoded in `paywall-teaser.md` rules #1/#3/#4; reversed the agent's earlier "allow proper nouns + subject+verb" rules.)

---

## 11. Standalone (non-newsletter) posts

Same neutral-voice instinct as the newsletter — strip flourish, stay literal (2026-06-24 Meta Arena post).
- **Title accurate to stage:** "Meta entra nos mercados de previsão com o Arena"→"Meta começa o desenvolvimento de um mercado de previsão" (in development, not launched). Drop the product-name hook from the title.
- **Cut editorializing appositives/qualifiers** ("vantagem que dinheiro de investidor não compra", "que hoje trava o setor").
- **Cut redundant contrast** ("A aposta é em pontos, não em dinheiro"→"A aposta é em pontos" — the next clause implies it).
- **No subtitle** on a short standalone post.

---

## 12. Mechanics — em-dashes

Em-dash (—, U+2014) → comma / colon / parentheses. This recurs **every** review — the `newsletter-no-dashes` skill covers the prose path, but the `generator`/`facts` agents still emit em-dashes into `edition.md`, so Gui still sweeps by hand.
- Aside → comma/parens: "por ano — a maior virada"→"por ano, a maior"; "Booking.com — tudo às vésperas do IPO."→"Booking.com (tudo às vésperas do IPO)."
- Introduces a list/explanation → colon: "confiabilidade — prédios ficaram fora do ar"→"confiabilidade: prédios…".
- ⚠️ An em-dash **inside a link's anchor text** survives the prose pass — move it outside the bracket. Also do a final mechanical pass for double spaces / inconsistent prepositions that manual edits leave behind.

---

## 13. Accuracy — the generation invents specifics

The most dangerous error class: the model adds authoritative-sounding specificity that isn't in sources — exact percentages, "first ever" superlatives, precise timeframes, phantom model sizes, inverted comparisons.
- **Verify every benchmark/number claim against `research.json`** (the fact + its excerpt). The generation once wrote "89,2% no AIME no modelo de 31 bilhões de parâmetros" — no such 31B model existed; and "o 12B aproxima-se desses resultados" when research said the 12B approximates the *26B MoE*. Distrust parameter counts and "aproxima-se de X." A benchmark horse-race claim usually gets cut anyway.
- Real error patterns caught in audits: math that doesn't add up (Penn-Wharton $210B breakdown ≠ $180B sum), fabricated percentages (Dravet "85% em três meses" from "substantial and durable over 3+ years"), scope inflation (company record → "maior da história"), invented ranges (jobs "55 a 60 mil" matching no single source), stale intraday prices.
- **Freshness audit focuses on the event window,** not fact-checking accuracy: reads the edition, checks `research.json` dates, web-searches as fallback. Background context supporting a fresh story is fine; an event presented as *news* must be in the window. `outside_window` and `source_unavailable` (paywalled Reuters/Bloomberg/Fortune blocking curl) flags are usually safe to dismiss with a quick web check.

---

## 14. Review process & working style

How Gui wants the review itself conducted:
- **Be proactive — don't ask "quer que eu reescreva?".** If you spot an issue or he flags one, go straight to the proposed rewrite. Save the question for genuinely ambiguous editorial calls with multiple valid directions.
- **One best option, not three.** Present the single best rewrite informed by the editorial voice. Multiple options only when asked.
- **One edit at a time.** Propose each individually in chat, wait for approval/tweak before applying — don't batch-apply. Expect him to tweak proposals; keep them clean and minimal.
- **Always show both versions** (current + rewrite), side by side, in **code blocks** (markdown link syntax mangles in the terminal). Show the full surrounding sentence/paragraph so he can judge the edit in place.
- **Efficiency:** review factual errors (wrong numbers, contradicted claims, fabrication) one-by-one with web search; batch-dismiss or quick-fix mere link mismatches (fact correct, source just doesn't contain it) — don't belabor them.
- **Feminine for LLMs:** "as LLMs", "nelas". **Remove p-values** and statistical-significance notation — noise for a general audience.
