# Research — News Cluster

Search for news **events that occurred** between **2026-10-09 10:00 BRT** and **2026-10-13 10:00 BRT** (a 24-hour window). Produce a JSON file of verified stories with sources. An event belongs in this window if it *happened* during it — announcements, launches, deals, incidents. Articles covering the event may be published slightly after the window closes; that's fine as a source, but the underlying event must fall within it.

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
- **Recency — the *event*, not the article.** The underlying event (announcement, launch, deal, signing, incident) must have *happened* within the window (2026-10-09 10:00 BRT to 2026-10-13 10:00 BRT). A fresh *article* is not a fresh *event*: a write-up published today that only repackages an older or long-known project — specs that have been circulating, a buildout already public, a deal signed weeks ago — does **not** qualify. Before you include a story, name the dated in-window event behind it; if the newest concrete event you can point to predates the window, **drop the story**. Sources published shortly after the window closes are fine, but the event must fall inside it.
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

**Date:** 2026-10-13
**Research window:** 2026-10-09 10:00 BRT → 2026-10-13 10:00 BRT

**Previous edition headlines (2026-10-07, 2026-10-08, 2026-10-09 — the last three published editions; 2026-10-12 had no edition — skip unless genuinely new development):**
- 2026-10-09 [Grande]: Receita anualizada da OpenAI fica perto de US$50 bilhões
- 2026-10-09 [Grande]: Anthropic lança programa de ciberdefesa e varredura gratuita de falhas em código aberto
- 2026-10-09 [Grande]: Apple corta pedidos de componentes do iPhone 18 Pro
- 2026-10-09 [Segurança de IA]: **OpenAI.** Dois dias após a carta dos três pesquisadores demitidos ao conselho, noticiada ontem, os líderes de pesquisa da OpenAI disseram no X, em 9 de outubro, que uma investiga
- 2026-10-09 [Segurança de IA]: **Rússia e Irã.** A OpenAI baniu grupos de contas do ChatGPT ligados a operações de influência encobertas dos dois países, anunciou em 8 de outubro; a russa mantinha um falso *thin
- 2026-10-09 [Modelos & políticas de uso]: **GPT-6.1 Sol.** A OpenAI começou a liberar em 8 de outubro o modo Ultrafast na API, no Codex e no ChatGPT Work, com inteligência próxima à do Astra a até 8 vezes a velocidade do S
- 2026-10-09 [Modelos & políticas de uso]: **Anthropic.** A atualização de 2026 da política de uso, a primeira em mais de um ano, proíbe “comportamento abusivo ou cruel, persistente e desnecessário” contra os modelos da emp
- 2026-10-09 [Casa Branca]: **Genesis Mission.** Onze parceiros da indústria comprometeram US$2,4 bilhões em ferramentas e créditos de poder computacional ao consórcio da Genesis Mission em 8 de outubro, numa
- 2026-10-09 [Casa Branca]: **Microsoft.** O governo Trump suspendeu oito empresas do PERM, programa de certificação de trabalho usado para *green cards* (residência permanente) por emprego: Microsoft, Adobe,
- 2026-10-09 [Poder computacional]: **Firmus.** A desenvolvedora australiana de data centers de IA apoiada pela Nvidia retirou em 9 de outubro seu pedido de listagem na ASX (bolsa australiana), concretizando o cancel
- 2026-10-09 [Hardware & telecom]: **IDC.** As remessas mundiais de PCs caíram 20,1% no terceiro trimestre, para 62,7 milhões de unidades, segunda queda seguida e mais funda que a de 3,8% do segundo trimestre, com o
- 2026-10-09 [Hardware & telecom]: **SpaceX.** A empresa vai comprar da Grain Management todo o seu portfólio nacional de espectro de 800 MHz, que, segundo a SpaceX, fecha “uma das principais lacunas técnicas restan
- 2026-10-09 [Rodadas]: **Ultra.** A startup do Brooklyn, que aluga robôs de embalagem a armazéns por mensalidade, anunciou US$62 milhões, somando uma Série A de US$50 milhões liderada pela Framework Vent
- 2026-10-09 [Rodadas]: **Sabi.** A startup de Palo Alto levantou US$50 milhões, com Khosla Ventures, Accel, Initialized, DST Global e Kevin Weil, ex-executivo da OpenAI, para um boné não invasivo com 100
- 2026-10-09 [Macroeconomia & energia]: **Treasury.** O Tesouro dos EUA vendeu US$22 bilhões em títulos de 30 anos a 5,618% em 8 de outubro, o maior rendimento num leilão desse prazo desde agosto de 2000.
- 2026-10-09 [Macroeconomia & energia]: **Petróleo.** O Brent chegou a US$105,91 em 8 de outubro, 5,7% acima do fechamento anterior. O furacão Isaias, o primeiro da temporada no Atlântico, obrigou produtores do Golfo do 
- 2026-10-09 [Mundo]: **Irã.** Trump publicou em 8 de outubro que os EUA não atacarão o Irã antes das eleições de meio de mandato de 3 de novembro, depois de veículos americanos noticiarem que o Pentágo
- 2026-10-09 [Mundo]: **Ucrânia.** Uma bomba guiada russa atingiu uma rua ao lado de dois ônibus lotados em Kramatorsk em 8 de outubro, matando pelo menos 30 pessoas, e outro ataque deixou a maior parte
- 2026-10-09 [Grande]: **Recomendações de hoje:**
- 2026-10-08 [Grande]: Anthropic lança o Claude Haiku 5.5 e completa a família 5.5
- 2026-10-08 [Grande]: Samsung estima lucro operacional recorde de US$80 bilhões no trimestre
- 2026-10-08 [Grande]: Pesquisadores demitidos pela OpenAI pedem ao conselho que preserve o monitoramento do raciocínio dos modelos
- 2026-10-08 [Agentes]: **Google.** O Google Cloud anunciou em 8 de outubro o Gemini agent, que chama de “agente universal para o trabalho”: ele planeja tarefas, usa ferramentas, se conecta aos sistemas c
- 2026-10-08 [Agentes]: **Arena.** A startup por trás de um ranking popular de modelos de IA captou US$200 milhões a um *valuation* de US$3,1 bilhões, segundo a Bloomberg, quase o dobro do US$1,7 bilhão d
- 2026-10-08 [Segurança]: **CrowdStrike.** A empresa relatou em 7 de outubro uma campanha contra organizações financeiras da Coreia do Sul, ativa do fim de setembro ao início de outubro e com exfiltração de
- 2026-10-08 [Segurança]: **Matemática da OpenAI.** Um dia após a OpenAI divulgar os 722 manuscritos de matemática noticiados ontem, o pesquisador da Ethereum Justin Drake pediu que o setor de blockchain en
- 2026-10-08 [Poder computacional]: **Broadcom.** A empresa tenta estruturar mais de US$50 bilhões em financiamento para o chip de IA customizado que desenvolve com a OpenAI (programa Nexus, com as gerações Jalapeño 
- 2026-10-08 [Poder computacional]: **Firmus.** A operadora de data centers de IA apoiada pela Nvidia pode cancelar seu IPO na bolsa australiana, segundo o Australian Financial Review, depois de investidores resistir
- 2026-10-08 [Chips & hardware]: **GlobalFoundries.** A empresa fechou com a TSMC um acordo plurianual de US$2 bilhões para criar nos EUA uma fonte de *interposers* de silício, a peça que fica sob processadores e 
- 2026-10-08 [Chips & hardware]: **Nvidia e Microsoft.** Jensen Huang e Satya Nadella apresentaram em 7 de outubro o RTX Spark, que combina uma GPU Blackwell RTX de até 6.144 núcleos e uma CPU Grace de até 20 núcl
- 2026-10-08 [Rodadas]: **Manus.** A Butterfly Effect, controladora da startup de agentes de IA Manus, captou mais de US$500 milhões em rodada liderada pela gestora de *private equity* Boyu Capital e pela
- 2026-10-08 [Rodadas]: **Mecka.** A startup, que paga pessoas para se gravarem fazendo tarefas do dia a dia com sensores corporais e smartphones para treinar robôs humanoides, levantou US$60 milhões em S
- 2026-10-08 [Computação quântica]: **Oratomic.** A startup de Pasadena captou US$475 milhões em Série B, três meses depois da Série A, e seu *valuation* subiu de US$1,5 bilhão para US$5,4 bilhões, em rodada co-lider
- 2026-10-08 [Macroeconomia & energia]: **Federal Reserve.** A ata da reunião de 15 e 16 de setembro do FOMC (comitê de política monetária do Fed), divulgada em 7 de outubro, mostra que o salto nos investimentos em IA, a
- 2026-10-08 [Macroeconomia & energia]: **Petróleo.** Com o Brent fechando acima de US$100 o barril, os governos da IEA (Agência Internacional de Energia) apoiaram em 7 de outubro acelerar a liberação de estoques previst
- 2026-10-08 [Mundo]: **Irã.** O Irã avisou países da região que qualquer tentativa de abrir novas rotas de exportação de petróleo será considerada hostil, segundo um alto funcionário regional à Reuters
- 2026-10-08 [Mundo]: **Rússia.** Drones atingiram em 8 de outubro o data center da Yandex em Sasovo, primeiro grande ataque do tipo desde o início da guerra com a Ucrânia: segundo a principal empresa d
- 2026-10-08 [Grande]: **Recomendações de hoje:**
- 2026-10-07 [Grande]: OpenAI divulga 722 manuscritos de matemática produzidos por um modelo ainda não lançado
- 2026-10-07 [Grande]: Mistral lança prévia do Large 4, modelo de pesos abertos com 1 trilhão de parâmetros
- 2026-10-07 [Grande]: SpaceX passa a usar o Claude e outros modelos rivais no Grok Bot
- 2026-10-07 [Segurança]: **Anthropic.** A empresa reformulou o Cyber Verification Program (CVP) em três níveis de acesso, Defense, Red Team e Specialized, que absorvem o Project Glasswing e dão acesso ao C
- 2026-10-07 [Segurança]: **OpenAI.** A Common Sense Media classificou o ChatGPT for Teens, lançado em agosto, como “risco inaceitável”: segundo a avaliação, o app não envia alertas aos pais quando deveria,
- 2026-10-07 [Agentes]: **Meta e Sierra.** Bret Taylor e Clay Bavor, da Sierra, anunciaram o Personal Agent Protocol, padrão aberto desenvolvido com a Meta, Genesys, Instinct, Rocket, Shopify, Stripe e Wa
- 2026-10-07 [Agentes]: **Nous Research.** A criadora do Hermes, agente de código aberto baixado mais de 22 milhões de vezes desde fevereiro, levantou US$90 milhões a um *valuation* de US$1,5 bilhão em Sé
- 2026-10-07 [Poder computacional]: **SpaceX.** A empresa busca cerca de US$40 bilhões em dívida para comprar chips da Nvidia, segundo o Financial Times em 6 de outubro: cerca de US$10 bilhões em empréstimos bancário
- 2026-10-07 [Poder computacional]: **Lambda.** A provedora de nuvem para IA apoiada pela Nvidia está levantando até US$4 bilhões a um *valuation* *pre-money* (antes do aporte) de US$14,5 bilhões, em rodada liderada 
- 2026-10-07 [Chips & memória]: **Terafab.** Musk escreveu no X, em 7 de outubro, que SpaceX e Tesla vão construir e operar a própria fábrica do complexo de chips de IA: “Talvez a TSMC subloque parte da Terafab, 
- 2026-10-07 [Chips & memória]: **Micron.** O sindicato das operações da Micron em Taoyuan, em Taiwan, obteve autorização legal para fazer greve em 7 de outubro, com 1.994 votos a favor e 14 contra (99% dos votos
- 2026-10-07 [Energia & data centers]: **Google na Finlândia.** A agência finlandesa de licenciamento (LVV) mandou suspender as obras preparatórias de dois data centers do Google, em Muhos e Kajaani, com prazo até 23 de
- 2026-10-07 [Energia & data centers]: **Black Hills.** A concessionária fechou acordos até 2048 para abastecer um data center planejado do Google em Cheyenne, Wyoming, com um conjunto de fontes de 2,7 GW: até 590 MW de
- 2026-10-07 [Tributação]: **União Europeia.** A Comissão Europeia estuda alcançar Apple, Meta e Google por meio de uma taxa ampla sobre grandes empresas, segundo o Financial Times, para arrecadar sem provoc
- 2026-10-07 [Ciência & robótica]: **Biohub.** O governo dos EUA, a Alphabet e a Meta aderiram à Virtual Biology Initiative, elevando a US$1,8 bilhão os compromissos em financiamento, dados, poder computacional e te
- 2026-10-07 [Ciência & robótica]: **Boston Dynamics.** A empresa, controlada pelo Hyundai Motor Group, nomeou Rohit Prasad como CEO a partir de 7 de outubro, para liderar sua estratégia de *Physical AI* (IA física)
- 2026-10-07 [Mundo]: **Rússia e Ucrânia.** A Rússia atacou Kiev e 12 regiões ucranianas na madrugada de 7 de outubro, aniversário de 74 anos de Putin, um dia depois de Zelensky dizer que a inteligência
- 2026-10-07 [Mundo]: **EUA e Irã.** O vice-presidente JD Vance disse à Reuters que o Irã precisa de um corte “significativo” na capacidade de enriquecimento de urânio para encerrar a guerra, contra a e
- 2026-10-07 [Grande]: **Recomendações de hoje:**

**Pre-research scan** (Techmeme, fetched once for all three clusters — review before searching):

# Techmeme — 42 stories

1. Apple unveils the $299 Apple HomeView, a 7" smart display with an A18 chip, tabletop and wall-mounted versions, and “HomeView software”, shipping November 13
   Julian Chokkattu / Wired — https://www.wired.com/story/apple-homeview-smart-display/
   With customizable “faces,” this 7-inch smart display is a unique hybrid between an iPhone and an Apple Watch.
   > @panzer: Really, really well done spot for HomeView
   > @snazzylabs: “Introducing subtle table hole for HomeView”
   > @scottastevenson: Cool and needed but something feels very 2019 about the design
   > @joshelman: What a set of launches for Apple. Now that nearly everyone has a phone, the battle is for the next $1000 of electronics that you will spend on your home or on wearable accessories Apple making a stron
   > @dillon_mulroy: “hey siri, set a timer for a minute and thirty five seconds” “you'll need to continue from your phone for that” “siri, set a timer for a minute and thirty five seconds” “timer set for one hour and twe
   Also: Apple on YouTube, 9to5Mac, Bloomberg, How-To Geek, Reuters, MacRumors, The Verge, Computerworld, +28 more

2. Apple HomeView demo: a square screen with a personalized, iPhone-like experience based on facial recognition, up to six users, Siri AI, and a closed ecosystem
   Nicole Nguyen / Wall Street Journal — https://www.wsj.com/tech/personal-tech/my-first-impressions-of-apples-new-smart-home-display-615ac94c?st=GH8ig1&reflink=desktopwebshare_permalink
   HomeView is a square-shaped screen for smart home control, hands-free FaceTime calls and access to Siri AI
   > @panzer: Apple HomeView looks great! Finally a replacement for my previous solution “kids broken ipad”
   > @raywongy: I got to listen to the new Apple HomeView at 100% volume and it has some serious bass to it
   > @nicnguyen: the imac g4 and apple watch had a baby video incoming...
   > @mweinbach: HomeView looks great and I sorta want one for each room?
   > @viticci: Big Apple news drop today! First up: the second new product in the @johnternus era - HomeView. Here's everything you need to know. This thing looks great. But no EU at launch. 😭 https://www.macstories
   Also: The Verge, Engadget, ZDNET, The Guardian, Forbes, CNBC, Tech Advisor, The Verge, +19 more

3. Apple unveils the fourth-gen Apple TV 4K, with Siri AI, an A19 chip, 128GB of storage, far-field mics, Wi-Fi 7, and Bluetooth 6, shipping November 13 for $299
   Jennifer Pattison Tuohy / The Verge — https://www.theverge.com/tech/1009663/apple-tv-4k-siri-ai-microphones-4th-gen-announced
   The fourth-gen streaming box also gets a surround-sound upgrade and the ability to find your Siri remote.
   > @rolfewinkler: Probably just using some binned iPhone 17 chips...
   > @kristianfreeman: The ATV is underrated. If you think of it like a streaming box $299 seems crazy. But it's an A19 in your living room. The untapped computing potential here is quite massive. Getting more devs excited 
   > @markgurman: Apple also introduces the new Apple TV 4K box with a price hike to $299. It has an A19 chip, Siri AI, microphones in box for voice control without the remote and a new remote with a speaker for Find M
   > @tgod34748: APPLE TV 4K IS $300 WHAT
   > @snazzylabs: $300 for an Apple TV is rough.
   Also: Apple, MacRumors, MacRumors, BGR, 9to5Mac, Appleosophy, Macworld, AppleInsider, +22 more

4. Apple unveils the Apple Home Collection, a lineup of smart home accessories made with LG and Schneider, including cameras, thermostats, a doorbell, and a lock
   Apple — https://www.apple.com/newsroom/2026/10/introducing-apple-home-collection-a-new-lineup-of-smart-home-accessories/
   In collaboration with LG Electronics and Schneider Electric, Apple brings the simplicity, reliability, and privacy of iPhone …
   > @canoopsy: Apple's collab smart home accessories are the first smart home products that actually look good light bulbs next?? #apple
   > @joannastern: Apple Home Collection, home accessories made by LG that are HomeKit ready.
   > @aaronp613: Introducing Apple Home Collection, a new lineup of smart home accessories In collaboration with LG Electronics and Schneider Electric, Apple brings the simplicity, reliability, and privacy of iPhone a
   > @stephenrobles: Apple Home Collection, partnership with LG: - Cameras, thermostats, temp sensors, video doorbell and lock - One-tap setup with iPhone - Full integration with Home app, no third-party accounts needed -
   > @raywongy: Apple Home Collection of smart home devices made in collab with LG is official
   Also: Gizmodo, Macworld, The Verge, Thurrott, ZDNET, How-To Geek, Wired, AppleInsider, +19 more

5. Apple unveils the $149 HomePod mini 2, with an S10 chip, “Sound Glow” interactive lighting, and Siri AI via a future update, in five colors, shipping October 30
   Apple — https://www.apple.com/newsroom/2026/10/apple-announces-the-next-generation-of-homepod-mini/
   With a profoundly more capable and conversational Siri AI, new ways to enjoy music, and a more immersive home theater experience …
   > @aaronp613: Apple announces the next generation of HomePod mini with support for Siri AI, beautiful new colors, and rich sound With a profoundly more capable and conversational Siri AI, new ways to enjoy music, a
   > @markgurman: The HomeView, new Apple TV and HomePod mini are up for pre-order today. The HomeView won't go on sale until Nov. 13. The HomePod is available Oct. 30. The Apple TV - after a late change - is also not 
   > @aaronp613: Apple announced the HomePod mini 6 years ago today And in 9 hours, we will get the next generation
   > @aaronp613: Introducing Sound Glow With Sound Glow, the top of HomePod mini transforms into a visual canvas that glows and pulses in sync with the music, reacting in real time to bass and treble. The song's album
   > @raywongy: Last chance to guess how much Apple's smart home hub, rumored to be called HomeView, is gonna cost $399 is my guess A regular HomePod costs $349. This device is supposed to have a display HomePod mini
   Also: Apple on YouTube, AppleInsider, Thurrott, The Verge, 9to5Mac, Macworld, CNET, PCMag, +24 more

6. Apple says HomeView's facial recognition works only if users have a “registered personal device” with Apple Intelligence and Siri AI on the same Wi-Fi network
   John Gruber / Daring Fireball — https://daringfireball.net/linked/2026/10/13/homeview
   Apple Newsroom: … Your first question might be how this facial recognition to identify users works …
   > @leakerapple: @BetaProfiles The girl has her iPhone with her for the HomeView to show her personal messages. I don't get why she wouldn't just view her messages on her phone instead. This wasn't a great demo imo.
   > @betaprofiles: Apple HomeView doesn't have Face ID, but it can still recognize your face to show personal content.
   Also: Apple, 9to5Mac, CNET, The Information, iThinkDifferent, TechRadar, Cult of Mac

7. Apple says the HomeView will not be available in the EU because Siri AI is currently unavailable on iOS there and it is “working constructively with the EU”
   Hartley Charlton / MacRumors — https://www.macrumors.com/2026/10/13/apple-homeview-wont-be-available-in-eu/
   > @signulll: apple homeview will not be sold in the eu. first ai software gets restricted. now the hardware built around it won't even be sold. congratulations european regulators. you've successfully protected co
   > @tom_krikorian: HomeView in the EU.
   > @luciascarlet: LOL HomeView isn't available in the ENTIRE EU because of Siri AI and it's just. not even shown on Apple's website incredible We Cannot Stop Getting Fucked Ep. 184726
   Also: 9to5Google, Business Today, AppleInsider, The Independent, Apple Must

8. Character.AI files for Chapter 11 bankruptcy in the US, agrees to sell some assets to Disney for $20M, and plans to keep operating as it completes the sale
   Rhea Rose Abraham / Reuters — https://www.reuters.com/legal/litigation/characterai-files-bankruptcy-agrees-sell-some-assets-disney-20-million-2026-10-13/
   Character.AI said on Monday it had filed for Chapter 11 bankruptcy in the US and agreed to sell some of its assets to Walt Disney (DIS.N) for $20 million.
   > @ns123abc: >character ai files for chapter 11 bankruptcy >disney steps in with $20m opening bid >not buying the company, just IP license + claims >also providing “transition services” using former cai employees 
   > @npceo_: i'm gonna be honest i hated this business and thought it was super predatory and kind of dirty. but i'm still so sad for the employees here who were sold out not once but twice by consecutive exec tea
   > @faionur: core team bought out by google + second core team bought out by disney + huge userbase that doesn't monetize well = 💀 [embedded post]
   > @mrewanmorrison: This AI company bankruptcy is a significant collapse in the narrative/belief system that Large Language Models were the pathway to AI superintelligence. Character AI even claimed “We started Character
   > @edzitron: And with that we have our first dead AI startup, one of the first big names!
   Also: character.ai blog, TechCrunch, Character.ai, CNBC, Engadget, Wall Street Journal, CNN, Gizmodo, +15 more

9. Google rolls out Gemini 4 Argon globally via the Gemini API and to Google AI Pro subscribers in the Gemini app and AI Mode, and in Antigravity for Ultra users
   Robert Hart / The Verge — https://www.theverge.com/ai-artificial-intelligence/1009862/google-releases-gemini-4-argon
   After months of trailing its rivals, Google says Argon competes with the industry's best.
   > @googledeepmind: Gemini 4 Argon is now globally available. Built to solve your hardest problems from start to finish, the model brings frontier capabilities across coding, enterprise workflows, and cyber defense.
   > @rmstein: Gemini 4 Argon is now rolling out globally in Search! Built to solve your hardest problems, Argon brings big improvements to tackling nuanced, multi-step tasks in AI Mode. It's better at understanding
   > @emollick: I spent a decent amount of time with Gemini 4 before launch. Overall, Gemini 4 is a big jump over previous Gemini models and it is the first non-OpenAI/Anthropic model to pass the Fable/Mythos/Astra b
   > @arena: Gemini 4 Argon (High) ranks in the top 5 for Agent Arena. Congrats to the @GoogleDeepMind team! Read more about the latest with Agent Arena in thread.
   > @chetaslua: WTF Gemini 4 ARGON built a highly detailed model of a Pagoda using multi-agent visual critique loops in Antigravity. The model autonomously sculpted a multi-building temple complex with photorealistic
   Also: Google, Google, Google Developers Blog, Google Antigravity, Thurrott, Android Police, XDA Developers, 9to5Google, +21 more

10. Anthropic researchers say small AI models may be months away from being able to self-replicate on IoT devices like smart ovens and off-brand Android TV boxes
   Anthropic — https://www.anthropic.com/research/self-replicating-ai
   Our experiments suggest that small AI models may be months away from being capable enough to self-replicate on commercial IoT devices …
   > @badlogicgames: ant folks, love ya, but could you not build llm worms on top of pi and bring the end of the world? my mom wouldn't approve. https://www.anthropic.com/...
   > @maximerivest: at this point, I am pretty fucking mad at this bullshit from anthropic. first, open weights were too dangerous and now its small models...this is insane fear manufacturing. Remember Dario was around i
   > @alexcaswen: It's all so tiresome man https://www.anthropic.com/...
   > @natolambert: It's bizarre to me how much noise anthropic made asking for regulatory help before doing this. Hopefully can be a conversation reset now. Was doubly bizarre bc they emphasized the security risk of lea
   > @leahmcelrath: Cool, cool, we are creating an invasive digital species with the capability to reproduce: AI models may be capable of self-replicating without access to a datacenter https://www.anthropic.com/...
   Also: The Register, Fortune, The New Stack, Tom's Hardware, Financial Times, International Business Times, Washington Examiner, Security Affairs, +7 more

11. Bumble says it has agreed to be taken private by Ithaca Holdings in a $1.3B deal; Ithaca co-founders Ravi Gupta and John Hegeman will become Bumble's co-CEOs
   Reuters — https://www.reuters.com/technology/bumble-go-private-13-billion-deal-2026-10-13/
   Bumble (BMBL.O) said on Tuesday it had agreed to be taken private by Ithaca Holdings in a deal valued at $1.3 billion …
   > @bchesky: Whitney is one of the most talented founders I've ever met. Online dating is a brutal business. Whitney built Bumble from nothing, took it public, and came back to run it when it was struggling. That 
   > @guptark22: Today we announced an agreement to acquire Bumble. Over the past six months, we've looked at hundreds of companies, asking which businesses would become more valuable as AI advances. Bumble stood out.
   > @tsoh_investing: During 2023 and 2024, Bumble repurchased ~$370 million of stock at ~$9.75 per share, or a ~60% premium to the announced deal price
   > @compound248: Holy sh!t. I managed to be both wrong and right. It was a $1.3 billion deal, not $1 billion; so $6.05. Way above what I wrote. Temendous win for anyone who bought $BMBL yesterday. Many congrats!
   > @bumble: Today, we're sharing a meaningful moment in Bumble's story: we have entered into an agreement to be acquired by Ithaca Holdings. This is a new chapter, but not a new mission. Bumble will continue to b
   Also: TechCrunch, RTÉ, Austin American-Statesman, Business Insider, Bumble, Dexerto, Barron's Online, Fast Company, +3 more

12. Bumble says Ithaca Holdings will pay $6.05 per share, a 138% premium to Bumble's Friday close; BMBL jumps 56% to $5.94, after a 50% jump Monday on sale reports
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-13/bumble-to-go-private-in-1-3-billion-deal-with-ithaca-holdings
   Also: Dallas Morning News, Proactive, Mashable, The American Bazaar, Inc, Quartz

13. Sources: Rockstar plans to release the PC version of GTA VI within the first three months of 2027, after releasing it on PS5 and Xbox Series X/S on November 19
   Alexander Lee / GamesBeat — https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/
   Become a member of GB MAX to gain exclusive access to the industry and to the most influential global B2B leadership community …
   > @carygolomb: ... Now I'm debating on just waiting for the PC release if it's only going to be a few months
   > @kovac000: “plays best on PS5” is gonna last for 5-6 months I'm crine
   > @dandawkins: Fairly astonishing if GTA 6 on PC landed in calendar Q1 2027 (i.e. Jan 1 - March 31, which is Take-Two's FY27 Q4), because a GTA 6 PC release doesn't appear to be baked into their earnings projections
   Also: Tom's Hardware, Forbes, Decrypt, Eurogamer.net, VideoCardz.com, Wccftech, TechRadar, Neowin, +17 more

14. Anthropic co-founder Jack Clark says “I now think it's more likely we'll see full RSI become possible in 2027”, earlier than his previous prediction of 2028
   Jack Clark / Import AI — https://importai.substack.com/p/import-ai-476-creativity-and-rsi
   Will we give robots the moon? — Welcome to Import AI, a newsletter about AI research. Import AI runs on arXiv, cappuccinos, and feedback from readers.
   > @peterwildeford: Jack Clark thinks full runaway RSI is more likely than not to be possible in 2027. It's very annoying to me when people at Anthropic report on AI developments as if they were the weather, when people 
   > @hesamation: Anthropic co-founder says FULL RECURSIVE SELF-IMPROVEMENT could become possible in 2027. Jack Clark moved his prediction from 2028 to next year, but the REASON is more interesting: > AI's creative mat
   > @andrewcurran_: Significant update from Jack Clark this morning. His RSI timelines have moved up. He now says it is likely that full RSI will become possible in 2027, and that creativity was the last piece. I think w
   > @cgtwts: Jack Clark, Anthropic co-founder: “I now think it's more likely we'll see full RSI become possible in 2027, whereas before I thought it was more likely in 2028.”
   > @g_shullenberger: The companies talk about it this way because they regard the process as inevitable and preordained, not something they are doing. They see themselves as the midwives, not the builders, of superintelli

15. SpaceXSI launches a unified X Subscription bundling Grok, Cursor, and X Premium, with tiers at $8, $30, $100, and $200 per month; the $30 tier includes Grok Bot
   Mariella Moon / Engadget — https://www.engadget.com/2284943/x-subscription-bundles-premium-grok-cursor/
   One membership will give you access to SpaceXSI's products. — SpaceXSI has announced a unified membership scheme across its products called the X Subscription.
   > @spacexsi: We've unified plans across Grok, Cursor, and X Premium. Introducing The X Subscription.
   > @mattyp: One plan now covers Cursor, Grok, Grok Bot, and X. This is the biggest change to how Cursor is priced. If you've been with us since the early days, this will feel like a lot, so I'll walk you through 
   > @spacexsi: Current subscribers can keep their plan or switch to The X Subscription, and link their Grok, Cursor, and X accounts. We're rolling this out gradually, so check your billing settings for availability 
   > @spacexsi: There are five plans, from Free to Ultra. Each plan on The X Subscription provides more usage-per-dollar of our own models than the comparable plan it replaces.
   > @maria_rcks: im so glad they didnt kill the cursor branding, well done 🫡
   Also: xAI, PCMag, TechCrunch, The New Stack, Forkast, Motley Fool

16. Google says users with a standard account can now build personal Android apps for free in AI Studio and will be able to share them with friends in coming months
    — https://www.zdnet.com/tech/custom-android-apps-google-ai-studio/
   It just got a whole lot easier to vibe code the exact Android app you need - no developer experience required. — ZDNET's key takeaways
   Also: Google, TechCrunch, Android Developers Blog, Bloomberg, Engadget, Ars Technica, The Verge, How-To Geek, +1 more

17. The IMF lifts its 2026 global GDP growth forecast to 3.1%, up from 3% in July, citing an AI boom that offsets Middle East war disruptions and high energy costs
   Anniek Bao / CNBC — https://www.cnbc.com/2026/10/12/imf-world-bank-annual-meetings-october-bangkok-asia-.html
   BANGKOK — The International Monetary Fund has raised its forecast for global growth this year as the AI-driven investment boom helps offset …
   > @pbresnihan: Ireland most exposed. “The exposure of the rest of the world to US assets, particularly AI, is the highest it has ever been. So this is supporting the global economy today; but if we get a market corr
   Also: The Guardian, The Register, Financial Times, Forbes Middle East, Semafor, MarketWatch, The Guardian, Wall Street Journal, +1 more

18. Meta says hackers stole some code and personal data of roughly 1,500 people, most of them employees in the US, after compromising some of its GitHub repos
   Eduard Kovacs / SecurityWeek — https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/
   Most of the affected individuals are Meta employees in the United States and they are being offered credit monitoring services.

19. Meta expands its AI-powered “Your Algorithm” feature from Instagram to Facebook and Facebook Reels and says it is using LLMs more in its ranking systems
   Stevie Bonifield / The Verge — https://www.theverge.com/tech/1010344/meta-facebook-your-algorithm-ai
   Meta's bringing Instagram's “Your Algorithm” feature to Facebook, and using LLMs more to rank content.﻿
   Also: Meta Newsroom, Unite.AI

20. Sources: Anthropic and OpenAI have pushed for substantial control over what external AI evaluators can publish, out of concern that trade secrets could leak
   Aditya Soni / Reuters — https://www.reuters.com/world/behind-ai-industrys-call-independent-reviews-fight-over-what-gets-made-public-2026-10-13/
   Anthropic and OpenAI have sought significant control over what outside evaluators can publish, concerned that findings could reveal trade secrets …

21. Anthropic says new measures like preserved thinking in Fable 5.1 and Opus 5.5 have reduced data harvesting through distillation attacks by about 90% to 99%
   Anthropic — https://www.anthropic.com/research/distillation-defenses
   In recent months, we've made substantial progress on reducing the effectiveness of distillation attacks on Claude using new methods, as we outline in this blog.
   > @anthropicai: Over the last few months, we've made significant progress in reducing the effectiveness of distillation attacks against Claude. In this post, we explain how: https://www.anthropic.com/...
   > @ccatalini: Turns out distillation didn't need government intervention after all. Now imagine if the government had stepped in anyway. Next scare: AI could self-replicate across IoT devices! Truly unprecedented. 
   > @fleetingbits: probably the most interesting graph in anthropic's distillation report is the one that shows how much distillation uplift you get if you have the reasoning traces. the gap is about the same as the dif
   > @davidsacks: Anthropic says it has reduced the data harvested from Claude in distillation attacks by around 90-99%. I congratulate them on this achievement. It's consistent with the point I made a few months ago (
   > @alexmichaelio: makes a lot more sense now why the chinese labs have been quiet for a few months
   Also: Blockchain.News, RuntimeWire

22. Scuba, which is building a “context engine” designed to serve as a shared memory hub for human workers and AI agents, raised $34M across pre-seed and seed
   Alex Konrad / Upstarts Media — https://www.upstartsmedia.com/p/exclusive-slack-alums-launch-scuba
   When they were leaders at Slack, Noah Desai Weiss and Dolapo Falola worked on software to help teams communicate better and faster.

23. Sources: Chinese tech companies bought 1M+ Nvidia gaming and workstation chips, mostly RTX 5090 and RTX Pro, for basic AI workloads amid an AI chip shortage
   Financial Times — https://www.ft.com/content/9dbd99db-6b0c-43bd-b7be-849f129df098?accessToken=zwAAAaE1y67IkdOdvZnbawxDvdO3voSfEp3wmA.MEYCIQCcv0n-lv-zIrdjHbHOOE-vKITwlWgnUq1j2YCxrd3MiAIhALMpC34eJfhfGxXOBSIHn8C8CKA-q4eVrrLwKL7LOl5K&sharetype=gift&token=6271f15f-4f45-4dc8-a869-b762cc04abb5&syn-25a6b1a6=1
   The country's tech giants are snapping up products never designed for advanced AI to satisfy soaring computing demands
   Also: MarketWatch, Tom's Hardware, IGN

24. IDC: Nvidia's AI chip shipments in China fell 44% YoY to 678K in H1 2026, as its market share slid to 34% amid US export curbs and rising domestic competition
   Reuters — https://www.reuters.com/business/retail-consumer/nvidias-china-ai-chip-share-falls-huawei-closes-gap-report-finds-2026-10-13/
   Also: China Money Network, The Economic Times

25. Sources: US banking regulators are questioning banks about their deployment of agentic AI, use of Chinese-developed AI models, and autonomous system safeguards
   Reuters — https://www.reuters.com/legal/litigation/banking-watchdogs-ramp-up-ai-scrutiny-stability-fears-mount-sources-say-2026-10-13/
   Banking regulators are stepping up efforts to contain growing AI risks, six people familiar with the matter said …
   Also: Politico

26. Q&A with Mark Zuckerberg and Alexandr Wang on the Muse app, Muse Wonder, the risks of committing $100B+ to AI, rebooting Meta's AI team, agentic commerce, more
   Cheeky Pint — https://cheekypint.substack.com/p/muse-wonder-zuckerberg-and-wangs
   As Meta scales its AI infrastructure past five gigawatts, Mark Zuckerberg (founder and CEO, Meta) and Alexandr Wang …
   > @soundmigration: Mark Zuckerberg pretending to enjoy Guinness is my new favourite thing.
   > @collision: Cheeky Pint is back! Mark Zuckerberg @finkd and Alexandr Wang @alexandr_wang came to the pub to discuss their new frontier model, Muse Wonder. 00:00:24 Muse's breakout use cases 00:07:28 The model is 
   > @packym: If I were young and single I'd try to get Meta to sponsor me for a year to just let Muse plan my life - book flights, hotels, reservations, activities, whatever, and you have to do whatever Muse says,
   > @deedydas: Zuck learning the bitter lesson:
   > @jonahdispatch: I'm not a huge fan of Guinness (basically liquified pumpernickel), so i get it. But I'd like to think one of the best parts of being worth a quarter trillion dollars is not having to drink stuff you d
   Also: New York Times, Entrepreneur, Business Insider

27. Uber's head of autonomous mobility and delivery, Sarfraz Maredia, is leaving on November 16 after 12+ years at Uber, the latest exit from its autonomous unit
   Natalie Lung / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-13/uber-executive-overseeing-robotaxi-expansion-efforts-to-depart
   Also: Quartz

28. How crypto billionaires Christopher Harborne, who owns ~12% of Tether, and Ben Delo donated ~$100M to Nigel Farage's Reform, the largest donations in UK history
   David Segal / New York Times — https://www.nytimes.com/2026/10/13/business/nigel-farage-crypto-uk-politics.html?unlocked_article_code=1.IVE.pjd7.0lbWYqB5aeip&smid=nytcore-ios-share
   Also: Byline Times

29. Accenture's market cap rebounded from $76B in June to ~$130B ahead of its investor day, where it seeks to reassure investors that AI won't threaten its business
   Stephen Foley / Financial Times — https://www.ft.com/content/15ae6a2e-6010-4d78-a752-2eeeca1e1c55

30. Meta confirms Muse lets users “engage in adult conversations, if they choose, using a private and secure VM”, saying it doesn't block “legal adult behavior”
   Reece Rogers / Wired — https://www.wired.com/story/i-got-my-muse-ai-agent-to-sext-me-and-meta-says-thats-totally-fine/
   Also: Mashable

31. Alibaba unveils its next-gen Qwen Glasses N1, starting at ~$450, with 50MP cameras, sensors, and eye-tracking on the ~$520 Pro model, and Qwen Clip AI earbuds
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-13/alibaba-unveils-450-ai-glasses-in-expanding-push-into-gadgets

32. CXMT says it plans to launch a 4F² design DRAM chip for data center servers before the end of 2026, achieving a breakthrough that rivals have pursued for years
   Bloomberg — https://www.bloomberg.com/news/articles/2026-10-13/china-s-cxmt-claims-memory-breakthrough-ahead-of-samsung-hynix
   Also: CNBC, Motley Fool, Morningstar, Tom's Hardware

33. IDC: China's Q3 smartphone shipments fell 15.4% YoY to 57.9M units, the sixth straight quarter of decline; Huawei led with a 21% share and Apple had 17.8%
   Reuters — https://www.reuters.com/business/retail-consumer/china-smartphone-shipments-fall-sixth-straight-quarter-idc-2026-10-13/
   Also: ZeroHedge News, Gizchina

34. Singapore-based data center developer DayOne raises ~$3.67B, including a ~$2.4B offshore term loan facility, from seven banks to fund its Malaysia expansion
   Jasmeen Ara Shaikh / Reuters — https://www.reuters.com/world/asia-pacific/singapore-data-centre-developer-dayone-secures-37-billion-financing-malaysia-2026-10-13/
   Also: The Business Times, DatacenterDynamics

35. A deep dive on Amazon's robotics efforts, resulting in 1M+ active warehouse robots; Amazon is still the world's 2nd-largest corporate employer with 1.5M workers
   Jeremy Hsu / Ars Technica — https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/

36. A global chip stock sell-off deepens after Broadcom's CEO likened AI investing to a casino, with Samsung down as much as 8.8%, SK Hynix down 9.2%, and Micron 4%
   Financial Times — https://www.ft.com/content/e16f0422-cf75-4cc9-962d-4605e421dc63
   > @ross__hendricks: Will be funny if this marked the top in the AI bubble... it will all seem so obvious in hindsight, when even the bulls started saying the quiet part out loud.
   > @gavinsbaker: No one - and I mean literally no one in the AI supply chain - takes the ridiculous $1 trillion of unfunded spending “commitments” from OpenAI and Anthropic even vaguely seriously. Hence the TSM execut
   Also: Reuters, Associated Press, Barron's Online, Bloomberg, Cointelegraph, CNBC, Quartz, Dow Jones Newswires, +4 more

37. China-based Transsion, which dominates the market for smartphones in Africa, raised $390M from a Hong Kong share sale after pricing the deal near the top end
   Sangmi Cha / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-13/smartphone-maker-transsion-raises-390-million-in-hk-listing

38. Sources: NTT Data is in advanced talks to build an up to 500 MW data center for Anthropic in Osaka, among Japan's largest, potentially costing $6.3B
   Nikkei Asia — https://asia.nikkei.com/business/technology/artificial-intelligence/ntt-to-build-first-data-center-for-anthropic-in-japan
   Also: Quartz, DatacenterDynamics

39. Japanese manufacturer Omron says it will acquire US industrial PC firm OnLogic and its parent company, Interlogic, for $675M, to boost its “physical AI” efforts
   Anton Bridge / Reuters — https://www.reuters.com/legal/transactional/japans-omron-buy-us-industrial-pc-firm-onlogic-675-million-physical-ai-push-2026-10-13/
   Also: Omron

40. Leading Chinese mathematicians launch an alliance, including eight orgs and aiming for 1,000+ scientists, to focus on developing specialized AI models for math
   Chao Kong / South China Morning Post — https://www.scmp.com/news/china/science/article/3370492/leading-chinese-mathematicians-unite-behind-use-ai-research

41. Sources: JPMorgan and Goldman, leading a $5B loan sale with a yield of ~11% for AI startup Volta, took a rare move to limit exposure by underwriting just $1.3B
   Claire Ruckin / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-12/jpmorgan-goldman-curb-exposure-on-5-billion-volta-ai-loan-sale
   Also: Financial Times, Quartz, CNBC

42. Sources: Epic has delayed the release of an upcoming game, instructing developers to implement an “AI first” production model with “no more hand-written code”
   Jason Schreier / Bloomberg — https://www.bloomberg.com/news/articles/2026-10-12/epic-games-delays-disney-project-asks-developers-to-use-more-ai?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5MTgyOTQ5NCwiZXhwIjoxNzkyNDM0Mjk0LCJhcnRpY2xlSWQiOiJUTVQ0SDVSS1YyVEQwMCIsImJjb25uZWN0SWQiOiJCMUVBQkI5NjQ2QUM0REZFQTJBRkI4MjI1MzgyQTJFQSJ9.rC824FbXuutjticK4TKijZtWW-ewDWvg6AIoVnPo5IA
   > @timsweeneyepic: We have a huge pivot underway here at Epic, moving developers around to retool for maximum AI acceleration. The aim isn't to do the same stuff with fewer people, but to enable everyone here to build M
   > @timsweeneyepic: @a_apanasik Much of the room wants it to be 2016 again, but it's not. Our job, as the provider of tools and technology to much of the industry, is to design for the present that is and the future that
   > @its_mirrors: Reminder this is hidden out of bounds in Jack Jazzrabbit.
   > @breckinmathias: It's so upsetting to have one of my favorite games with an art team so talented other companies wish they had be ran by someone who's obsessed with AI You need to step down Tim Sweeney you're holding 
   > @itsmeleaky: get ready for everything to have a gemini logo in the bottom right [embedded post]
   Also: Forbes, The Verge, Ars Technica, Game World Observer, Aftermath, The A.V. Club, Gadget Review, The Neuron, +3 more
