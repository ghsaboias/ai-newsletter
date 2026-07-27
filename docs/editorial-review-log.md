# Editorial Review Log

The dated provenance behind [editorial-principles.md](editorial-principles.md): each review session's specific draft→final edits, kept for their concrete before→after examples. The distilled, deduplicated rules live in the principles doc; this is the audit trail. Chronological.

> Every dated entry is a point-in-time observation. File/line citations and pipeline names (`pt.md`, `draft.sh`, `GENERATION.md`) reflect the older prose pipeline and may be stale — the *editorial* substance is what carries forward.

---

## 2026-03-09 — First audit reviews (03-05 & 03-06 editions)

Two sessions. 03-05: 19 findings, 6 fixed, 13 dismissed. 03-06: 23 findings, 16 dismissed, 7 fixed, 2 softened.

**Common false positives:** source truncation (audit curls + truncates to 1500 chars → claims in the cut portion flagged "unsupported"); paywalled/blocked sources (Reuters, VentureBeat, Fortune block curl → flagged `source_unavailable`, but claims almost always fine, confirm by web search); number in a *different* source covering the same event (sourcing gap, not a factual error — swap the source, don't change the claim); `outside_window` flags (the newsletter contextualizes ongoing stories — safe to dismiss when framing is clearly contextual).

**Real errors — the generation adds specificity that isn't in sources** (the hardest class to catch):
- Math that doesn't add up: Penn-Wharton $210B presented as a total with a breakdown ($65B+$115B=$180B, not $210B).
- Fabricated specifics: Dravet "85% em três meses" from a source saying "substantial and durable reductions over 3+ years." Most dangerous type.
- Unsupported superlative: "primeiro programa governamental americano a financiar extensão de healthspan" (NIA has funded aging research for decades).
- Scope inflation: SoftBank "$40B loan… maior empréstimo corporativo da história" — Bloomberg said "its largest-ever" (company record, not world record).
- Invented range: jobs "55 a 60 mil" matching no single source (CNBC 50K / Reuters 59K / others 60K) → use the actual 50–60K spread.
- Overstated role: Raia Hadsell "chefiado por" the UK AI lab → she chairs the peer-review panel ("painel presidido por").
- Stale intraday prices: Brent $83.99 intraday vs $85.41 settlement; Dow "900 pontos" matched neither close (784) nor intraday (>1,100). Use settlement.

**Efficiency lesson (Gui):** review factual errors one-by-one with web search; batch-dismiss/quick-fix link mismatches — don't spend equal time on both.

---

## 2026-03-10 — First repetition-check review (03-10 edition)

10 findings, all addressed (8 edited, 2 already resolved).

**Story repetitions — the fix is never to remove the story, it's to trim the background readers know:**
- Anthropic-Pentagon: dropped "que classificou a empresa como risco na cadeia de suprimentos" (explained 03-09), kept the new facts (amicus brief, $5B loss).
- Nexperia: cut the recap tail; the dash-clause juxtaposition (subsidiary outpacing parent) already landed.
- Macron naval mission: shifted from repeating "missão naval europeia" to the escalation ("a missão anunciada ontem agora tem hardware no mar").
- Oil prices: added "que não parou de subir desde 28 de fevereiro" to acknowledge the trajectory instead of presenting the price as new.

**Phrasing/framing:** max one editorial punchline per edition (had 3, kept 1); "Enquanto X, Y" device → two short punches ("LeCun aposta contra as LLMs. O resto da indústria dobra a aposta nelas."); kept an outsider-quote closer but glossed it (black cabs).

**Working-style preferences established here:** show both texts side-by-side for repetition claims; one best option (not three); one edit at a time, wait for approval; show surrounding context; don't over-cut (a good adjacent stat isn't repeated — Waymo 400k); feminine for LLMs; remove p-values; use code blocks for before/after in the terminal.

---

## 2026-03-20

1. "superapp desktop"→"superapp para desktop"; 2. "ferramentas Python"→"ferramentas para Python"; 3. drug names in "-ida" are feminine (a semaglutida, a retatrutida); 4. don't present plans as done ("anunciou a fusão" vs "plano de fundir"); 5. jargon like "Phase 3", "vouchers prioritários", "sem platô" means nothing to a general audience — rephrase/cut; 6. identify people by role on first mention ("Fidji Simo, CEO de aplicações na OpenAI"); 7. a stat discrepancy across editions (4x→5x) = assume hallucination, cut rather than update.

---

## 2026-03-24

1. "Stripe" is feminine (da Stripe); 2. "rede" alone is ambiguous — "rede elétrica" for the power grid; 3. "destravar" over "destrancar" for unlock in capacity contexts; 4. "lotada" doesn't work for production capacity — "com capacidade esgotada"; 5. "research preview" is translatable ("prévia de pesquisa"); 6. don't force a clever opener when the content leads itself (the Netherlands drone story); 7. don't frame unrelated launches as responses ("respondeu com" → "lançou").

---

## 2026-06-03 — Layout was the big new lever

**Bullets (new):** a section with ≥3 parallel items → lead-in + bullets with the proper noun bold as label. "Microsoft Build" (dense para) → lead "…três frentes simultâneas:" + **MAI-Thinking-1** / **Majorana 2** / **Project Solara**. "Captações" (4 paras) → header + **SpaceX** / **DeepSeek** / **Suno**. Label = proper noun, not category. Bullets + bold pass clean through pandoc→Substack.

**One concrete topic per header:** "Modelos & adoção"→"Modelos"; "Data centers & quântica"→"Data centers" + "Computação quântica"; a distinct beat (GitLab layoffs) leaves "Captações" for its own **Demissões** header (dropped the "Já" seam).

**Section order = taste** (moved Geopolítica/Ucrânia to the end, leading with AI/Tech) — but explicitly *depends*, edition to edition. Not to be codified.

**Cuts:** killed whole low-signal items (Sanções/Nobitex, Vingroup/Vinmotion); trimmed secondary detail (Brent "US$97 pela terceira sessão", ETF outflow line, Ukraine interception count "derrubaram 189" + route detail); rounded a volatile number (BTC "caiu 8,58% para US$67.206"→"caiu para a faixa de US$67.000").

**Jargon decode:** Marvell photonics → "fios de luz mais rápidos que os de cobre"; ZutaCore "sistema bifásico sem água"→"fluido não-condutor que absorve o calor fervendo…"; "switch Ethernet" + inline gloss. De-calque: "ancorar"→"liderar", "critérios classificados"→"não-públicos", "chips customizados"→"sob encomenda". But keep crisp English italic: "a um *valuation* entre", "modalidade do *input*". Gloss goes *outside* the link anchor (Otsuka/IgA).

---

## 2026-06-04 — Split dense blocks

**Split by topic:** Governança (DNA letter + OpenAI blueprint + Trump order) → **Biossegurança** + **Governança**; Semicondutores (Broadcom + TSMC) → two headers; Robótica (Amazon + Generalist AI) → header + a 2nd para (no bold) opening "Em capital de risco,".

**New bullet use-case:** a parallel list of **policy asks** (OpenAI blueprint's 4 requests) → bullets **without** bold labels (they're not entities). Lead-in ends "O texto pede que:".

**Anchor-shortening as a whole-doc pass:** reduce every link to the core fact, move descriptor/gloss/investor-list/attribution *outside* the brackets without deleting words. "[C.C. Wei disse a acionistas que o suprimento…]" → "C.C. Wei disse a acionistas que [o suprimento…]"; "[comprou a Kumo AI, startup… por US$400mi]" → "[comprou a Kumo AI], startup… por US$400mi".

**Accuracy:** generation hallucinated a phantom "Gemma 4 de 31 bilhões de parâmetros" (the line was 12B dense + 26B MoE) and inverted a comparison ("o 12B aproxima-se" of the 89,2% figures, when research said it approximates the 26B MoE). Cut the sentence. Verify benchmark claims against research.json.

**De-calque + gloss:** "hiperescaladores"→"*hyperscalers* (as grandes empresas de computação em nuvem)"; "AI Edge Gallery"→"(app que baixa e roda modelos de IA direto no aparelho, sem nuvem)". A legit continuation with new confirmed facts (Ucrânia/SPIEF) can stay even with overlapping framing — Gui's call.

---

## 2026-06-08 — Cut padding

**"plurianual" cut 3×:** "parceria plurianual que somaria"→"parceria que somará"; etc. The qualifier rarely carries weight.

**Remove the whole secondary paragraph** when the fact is the policy, not the market: cut the entire oil-price paragraph (Brent +4,35% US$97,14 / WTI +4,25% US$94,39 / Friday relief) + its CNBC link, kept only OPEC+; also dropped "Brent a US$97" from the subtitle.

**Terminology:** "*valuation*" (italic) > "valor" ("a um valor de US$30bi"→"a um *valuation* de US$30bi"). Comparison by extenso instead of "desde" ("desde US$4bi em dezembro"→"a empresa era avaliada em US$4bi em dezembro"). Plain verbs: "sequestradas"→"roubadas", "costurado"→"mediado". Precise nouns: "espaçonaves"→"satélites", "clientes ficaram sem energia"→"pessoas".

**PT:** "do Bloomberg"→"da Bloomberg"; "no Computex"→"na Computex" (2×); "OPEC+"→"OPEP+"; "que somaria"→"que somará". **Jargon gloss:** "O FDA"→"O FDA, agência reguladora de remédios e alimentos dos EUA,"; "anticorpo monoclonal injetável"→"(molécula de laboratório feita para mirar um alvo único)". Em-dash→comma/parens (Gui still does it by hand). Section reorder = taste again (Espaço up, Biotech to the end).

---

## 2026-06-09 — 22 point edits

**"IPO" cru > empolada paraphrase (3×):** "registra S-1 sigiloso"→"registra IPO"; "o que seria a maior estreia em bolsa do setor"→"o IPO"; "da própria estreia em bolsa"→"de seu IPO". Cut the floreio, keep the crisp term.

**"*exploit(s)*" italic.** **Decode/omit medical jargon:** "câncer de pulmão de células não-pequenas, não-resecável ou metastático"→"um tipo específico de câncer de pulmão" (here *omit*, not gloss).

**Trimming:** cut a whole secondary clause (Meta Workforce construction-deficit stat); cut secondary valuations ("captou US$65bi a US$965bi" off the Anthropic mention; "persegue avaliação de US$1,75 trilhão" off Cursor/SpaceX — which also *resolved an ambiguity* by cutting, not rewriting); cut companion-diagnostic detail ("detectadas em teste autorizado"); cut qualifiers that don't change the fact ("firme", "marcados em"→"de", "em proclamação de"→"em").

**De-editorialize:** "estertores finais"→"reta final"; "a pedido de Trump"→"por mediação do presidente dos EUA, Donald Trump"; "já vem puxando à frente"→"vem à frente". **PT:** "ligando o recurso"→"fazendo uso do recurso"; "ao desenvolvedor"→"a desenvolvedores"; "ante o aperto"→"frente ao aperto" (causal, ≠ the comparative ante→contra); "dois interceptadores"→"dois tipos de interceptadores"; header "Geopolítica tech."→"Geopolítica.".

⚠️ **Unresolved:** "a Google"→"o Google" changed in only 1 of 4 occurrences → inconsistent gender in one doc. Not a rule; ask Gui which gender to fix.

---

## 2026-06-12 — Link boundaries dominated (~6×)

**Narrow the anchor to the headline phrase, description as prose outside:**
- OpenAI: `[anunciou … comprar a Ona, startup de orquestração para agentes]` → `[anunciou um acordo para comprar a Ona]`, startup…
- Codex: `[+5mi usuários …, ante 3mi em abril, e profissionais…]` → `[+5mi usuários ativos semanais]`, contra 3mi…
- Also MiMo, Genspark, KKR/Helix, Icefish — same move. Em-dashes/glosses go *outside* the bracket.

**Structure:** broke a dense SpaceX lead into 2 paras + a plain framing sentence ("Hoje a SpaceX fará sua abertura de capital na bolsa.") before the numbers; sometimes *add* the number that sizes the headline ("mais de quatro vezes sobre-subscrita"→"quase quatro vezes: cerca de US$250bi de demanda, contra US$75bi ofertados").

**Gloss clinical/financial inline:** "estudo de fase 2/3 (formato acelerado… que funde as duas últimas etapas)"; "uso adjuvante (a terapia após a cirurgia, para reduzir o risco de o câncer voltar)". "*post-money*" italic (here English chosen over the prior "pós-money").

**Trimming:** cut secondary comparison/valuation from link+prose (Saudi Aramco 2019, "à frente da Tesla US$1,6tri"); cut the recurring Anthropic-fundraising sentence again; cut an unverifiable "segundo a empresa supera o Claude Code" from a link; cut FOLFOX6 → "quimioterapia".

**PT:** "ante"→"contra" comparatives (2×); gender ("o sul-coreano Mirae Asset"→"a", "do seed", "a primeira CPU"); crase ("terceirizar à Samsung"); "no Ohio"→"em Ohio". **Sourcing (new):** swap a weak aggregator link (channelnewsasia quoting The Information) for the named primary (theinformation.com) when the prose names the outlet.

---

## 2026-06-15 — Cut market-reaction color

**Cut whole market-reaction sentences:** European oil-cos %s + gold + Russell 2000 record; "SK Hynix subiu 7% e liderou a bolsa coreana." **Cut the war box-score:** "disparou 681 armas, 70 mísseis e 611 drones, maior salva da guerra… abateu 632 dos 681, mas 20 balísticos e 27 UAVs atingiram 42 locais" → "atacou as regiões de Kyiv, Dnipro e Kharkiv." Keep what/where, drop the tally.

**Structure:** reordered first 3 sections [Irã→Anthropic→Apple]→[Anthropic→Apple→Irã] (AI leads); split the dense Anthropic paragraph in two; subtitle rewritten to lead with AI and dropped oil-price + wine-tariff. **Jargon:** "die"→"chip"; "HBM"→"HBM (memória de alta largura de banda)". **PT:** "o desfazer do prêmio"→"a queda do prêmio", "encadear"→"realizar", "embarcar chips"→"produzir", "Lá fora"→"Fora dos EUA".

⚠️ **Generation bug (new):** markdown link with double parens `[texto]((url))` (Interfax link). Sweep for `]((` in finalize.

---

## 2026-06-19 — Factual changelog (Iran/oil verification)

Gui questioned whether the Iran story was repetition and whether the oil/signing facts were right. Web-verified ground truth:
- **Two signings of the US–Iran 14-point MoU:** (a) Sunday — initial phase, VP JD Vance + Iran negotiator Mohammad Bagher Ghalibaf, Trump witnessing; (b) Wed 17 Jun, Versailles — Presidents Trump + **Masoud Pezeshkian**, "entered into force immediately," 2 days ahead of the planned Friday Switzerland ceremony. Interim: immediate end to hostilities + 60-day window for the final treaty.
- **Pre-war Brent US$72,87** (close Fri 27 Feb, last day before strikes). 19 Jun close **US$77,69** — lowest since 27 Feb, still ~6.6% above pre-war. WTI US$74,90.
- **Appfigures/TechCrunch:** Tue 16 Jun biggest VPN-download day in India since ≥2025; **208k** = that day's total, **139k** = the baseline daily average (+49%).
- **Telegram (Section 69A):** delisted until 22 Jun; message-editing disabled until 30 Jun (both temporary).
- **06-18 edition:** no standalone Iran item; the deal appeared only in the Fed paragraph.
- **repetition.json flagged only** two phrasing/framing items — it *missed* the structural overlap with 06-15 (14-point MoU / Ormuz / 60-day / Friday-Switzerland).

Rewrote the Geopolítica lead + subtitle; Gui hand-edited the rest (per-paragraph: cut a ran-yesterday Intel sentence; cut runZero/NetRise descriptions keeping only the Dragos valuation; SpaceX "bonds"→"dívida", dropped a ratings sentence; "auto-aprimoramento recursivo"→"auto-melhoria recursiva"; ASML "embarcar EUV"→"exportar EUV"; many em-dash asides → comma/parens; "ante US$20bi"→"contra"). **Gui verbatim prefs:** on oil price — "sem o preço explícito, só 'voltou ao menor nível desde X'"; on the benchmark term — "ao invés de Brent, usa 'petróleo'" (subtitle; body kept Brent/WTI).

---

## 2026-06-30 — Published-vs-local diff (three-tier format)

Fetched the live post (`sstats post --today --html`) and diffed against local `edition-final.md`; teaser+paywall+AbacatePay are auto-injected, so only editor-side changes are Gui's.

**Tiering/structure:** reordered the 3 Grandes (local Meituan→Taiwan→Califórnia → published Taiwan→Califórnia→**Meituan** last — the generator's lead pick went last). Subtitle rewritten to match + reworded ("modelo de fronteira"→"modelo avançado"; dropped the Anthropic-Pentágono question). **Cut a whole load-bearing-looking bullet** (Califórnia's "Contraste." Pentágono/OpenAI, 4→3 bullets) — a deliberate editorial cut the fact-verifier would flag as a dropped fact.

**Paywall teaser overshoot: generator wrote 16, published shows 10.** Cut 6 (both Biotech; the duplicate-label "Capital." overflow; Leia-também throwaways). Made survivors vaguer/de-named ("A dona do ranking Chatbot Arena"→"Dona de ranking de chatbots"; "A sueca Saab"→"Suécia"; Higgsfield "rodada que multiplica seu valuation"→"rodada de investimento"). Takeaway: fewer teasers, vaguer, no duplicate labels, don't tease the tail.

**Per-bullet:** claim-softening ("liderou os rankings"→"apareceu perto do topo… no OpenRouter"; "primeiro modelo de trilhão de parâmetros"→"primeiro modelo aberto de mais de um trilhão"); "codificação por IA"→"programação por IA"; "comprometeu"→"investiu"; dash-aside (Reed) pulled into a trailing sentence; systematic em-dash→comma. **Manual editor-only additions:** 9 images w/ captions+credits (~1/story) + a "Recomendações de hoje" video block (2 picks). The Médias bullets + Leia também came through clean.

---

## 2026-07-01 — Two wrong-Grande failure modes (→ pipeline fix)

Both Grandes belonged in Médias; Gui cut both by hand.
- **Repetition (Grande #3, Korea Samsung/SK/Amkor US$578bi):** the same SW-Korea chip megaproject that was **Grande #1 on 06-29** (US$519bi version), back 2 days later. The `repetition-checker` caught it, but (a) it's advisory/non-gating and runs *parallel to the push*, so it never touches tiering; (b) its verdict was tier-blind ("continuidade legítima, não cortar") when the real call was **demote**.
- **Window/staleness (Grande #2, ByteDance US$39bi Ceará data center):** no July-1 *event* — the only dated event (Casa dos Ventos wind deal) was 2026-05-20, six weeks stale; the specs came from a thin trade-press consolidation (cryptobriefing.com). Both sources aggregators, no primary/tier-1. Not a *newsletter* repeat, so `repetition-checker` can't catch it — a *world-knowledge* staleness.

**Root:** the `generator` picks Grandes on *importância* alone — no memory of what recently led, no freshness/source-tier signal (facts.md strips dates). Both preventing signals died before the tiering decision.

**Fix shipped:** (1) `SKILL.md` computes the last ~5 editions' `###` headlines (`RECENT_GRANDES`) and injects them; `generator.md` got a **no-re-lead rule**. (2) `RESEARCH.md` sharpened — "recency = the *event*, not the article" + "a rehash has no primary source" (aggregator-only = find primary or skip). **Gui's durable tiering-quantity call:** don't force a fixed count, but **Grandes are CAPPED AT 3** — the writer picks the number within the cap, never pads, never more than 3.

---

## 2026-07-10 — Clean edition, 5 within-bullet edits (jargon + one embed)

Pulled the live Substack draft (`substack_mirror.py pull`, id `206435958` — still a draft, not yet published) and diffed against local `edition-final.md`. Teaser block + AbacatePay banner + paywall cut are auto-injected pipeline scaffolding (present in the draft, absent from `edition-final.md` by design). **No tiering, ordering, subtitle, or teaser changes** — the 3 Grandes, all Médias clusters, and Leia também came through in place. Every edit is a within-bullet touch-up; the generator's structure held.

**Grande · OpenAI (GPT-5.6) — "Variantes" bullet (two edits):**
- `Sol, o "cavalo de batalha"` → `Sol, o mais inteligente`
  (recharacterization — `facts.md` and the source, Axios, called Sol the "cavalo de batalha"/workhorse; Gui overrode it to flagship framing, matching Sol being the priciest tier at US$5/US$30.)
- `US$5 de entrada e US$30 de saída` → `US$5 de *input* e US$30 de *output*`
  (token-pricing terms switched from PT calque to the industry English *input*/*output* in itálico.)

**Grande · Meta (Muse Spark) — "Zuckerberg" bullet (link retarget + embed):**
- Link `[publicou no X pela primeira vez em três anos]`: `…/meta-lanca-api-de-modelos-de-ia…` (DJ article) → `https://x.com/finkd/status/2075218444056707458` (the actual tweet). Pointed the "publicou no X" phrase at the post it describes rather than the DJ story.
- **Embedded the tweet** (Substack `twitter2` card, Zuckerberg's "a strong agentic and coding model at a very low price") directly below the bullet — the one manual media add this edition.

**Médias · Rodadas & aquisições — "Mercor" bullet (two edits):**
- `startup de dados para treino de IA` → `startup de dados para treinamento de IA` (`treino` → `treinamento`).
- `aprendizado por reforço para os agentes` → `aprendizado por reforço (*reinforcement learning*) para os agentes` (added the English gloss in itálico).

**Médias · China — "MiniMax" bullet:**
- `alcançar a AGI](url) e prometeu` → `alcançar AGI](url) (Inteligência Artificial Geral) e prometeu` — dropped the article ("a AGI" → "AGI") and appended the gloss `(Inteligência Artificial Geral)` **outside** the link boundary. (AGI already glossed lowercase in the Fidji Simo bullet upstream; this re-gloss is capitalized.)

**Médias · Memória & fábricas — "Nanya" bullet:**
- `DRAM (memória dinâmica de acesso aleatório)` → `DRAM (memória dinâmica)` — shortened the gloss (dropped "de acesso aleatório").

**Pattern:** almost entirely jargon-glossing / term-choice housekeeping (RL, AGI, input/output, treino→treinamento, gloss-trim) plus a source-accurate link retarget + tweet embed. Reinforces the gloss-once and link-boundary principles; no new lever.

**Token-pricing convention (resolved):** the Sol edit first left the edition mixed — OpenAI switched to *input*/*output* while the Meta/"Preço" bullet still read "de **entrada** e … de **saída**". Flagged, and Gui normalized it in the draft by moving Meta to match: **both bullets now use *input*/*output* in itálico**. Standing rule going forward — token pricing uses `*input*`/`*output*` (English, itálico), not the PT `entrada`/`saída` calque.

---

## 2026-07-27 — 22 within-bullet edits, teaser cut 10 → 7

Pulled the live Substack draft (`substack_mirror.py pull`, id `208738161`) before the review and again after, and diffed the two ProseMirror bodies. No structural change: the 3 Grandes, the 8 Médias sections, Leia também and Recomendações kept their order and tiering; title, subtitle and all 10 image captions came through untouched.

**Grande 1 — Nvidia negocia garantia de US$250 bilhões (Ohio)**
1. `backstop` → `*backstop*`
2. `À parte, a Nvidia negocia uma estrutura de financiamento` → `Separadamente, a Nvidia negocia uma estrutura de financiamento`
3. `Anthropic, Microsoft e Google também o procuraram sobre o site.` → `Anthropic, Microsoft e Google também procuraram o secretário nas últimas semanas, interessadas no mesmo terreno.`

**Grande 3 — Claude Opus 5 no ARC-AGI-3**
4. `US$5 por milhão de tokens de entrada e US$25 na saída` → `US$5 por milhão de tokens de *input* e US$25 de *output*`

**Bloco de teaser (10 → 7 itens)**
5. `com a Anthropic como a ausência mais visível` → `com a Anthropic como a ausência mais notável`
6. `**Compute.**` → `**Poder computacional.**`
7. `**Semicondutores.** Estreia em bolsa de uma fabricante chinesa de memória com uma das maiores altas do ano na Ásia.` → `**Semicondutores.** Estreia em bolsa de uma fabricante chinesa de memória, com a maior captação em semicondutores da história da China.`
8. `**Memória.** Acordo de longo prazo entre gigantes coreanas e americanas de chips, mais os compromissos de uma cúpula de IA entre os dois países.` → `**Memória.** Acordo de longo prazo entre gigantes coreanas e americanas.`
9. `**Litografia.** China começa a produzir em massa máquinas de fabricação de chips, e ações europeias do setor recuam.` → (removido)
10. `**Espaço.** Voo de teste que soltou satélites operacionais pela primeira vez, e um pedido para uma nova constelação de órbita baixa.` → (removido)
11. `**Mundo.** Trégua no Oriente Médio derruba o preço do petróleo, e um artigo em jornal americano contra as novas tarifas.` → (removido)

**Médias · Segurança — "Microsoft"**
12. `contra cerca de 83% do Mythos, da Anthropic, e do GPT-5.5-Cyber; o modelo interno executa cerca de 95% do trabalho e a prévia pública chega na semana que vem via Azure AI Foundry.` → `contra cerca de 83% do Mythos, da Anthropic, e do GPT-5.5-Cyber. A prévia pública chega na semana que vem via Azure AI Foundry.`

**Médias · Washington e pesos abertos**
13. `sem ter sido instruído a isso; o prazo para três agências publicarem o marco voluntário de liberação é 1º de agosto.` → `sem ter sido instruído a isso. O processo de liberação que a OpenAI pretende usar para o modelo ainda não existe: três agências federais têm até 1º de agosto para publicar essas regras voluntárias e definir quais modelos elas cobrem.`
14. `A Anthropic segue como a ausência mais visível.` → `A Anthropic segue como a ausência mais notável.`
15. `#### Compute` → `#### Poder computacional`

**Médias · China e semicondutores**
16. `O IPO levantou US$8,6 bilhões, maior listagem da Ásia em 2026, e apenas 6,73% do capital ampliado era livremente negociável.` → `O IPO levantou US$8,6 bilhões, a maior oferta de semicondutores já feita na China continental, acima dos US$7,5 bilhões da SMIC em 2020.`
17. `131 sistemas embarcados pela ASML em 2025` → `131 sistemas despachados pela ASML em 2025`

**Médias · Rodadas — "Enigma"**
18. `saiu do *stealth* com uma seed de US$71 milhões` → `saiu do *stealth* com um *seed* de US$71 milhões`

**Médias · Espaço — "SpaceX"**
19. `[liberou satélites operacionais pela primeira vez](…), 20 Starlink V3, e a nave sobreviveu inteira à reentrada` → `marcou duas estreias para o programa: [liberou 20 satélites Starlink V3 operacionais](…) e sobreviveu inteira à reentrada`
20. `caiu duro no Golfo do México` → `caiu no Golfo do México`

**Médias · Mundo — "Irã"**
21. `EUA e Irã seguraram fogo pelo terceiro dia` → `EUA e Irã mantiveram uma pausa nos ataques pelo terceiro dia`
22. `semana depois de superar US$100` → `uma semana depois de superar US$100`
