# Search Provider Benchmark — Exa vs WebSearch vs Firecrawl

**Status: desenhado, não executado.** Bloqueado até **2026-08-16**, quando os créditos da Firecrawl renovam. Este doc guarda a medição de baseline, a capacidade de cada provedor e o desenho do teste, para que rodar no dia 16 seja executar — não redescobrir.

Escopo: a etapa de **research** do pipeline (os subagents "Research — News Cluster" e os de imagem editorial). Não trata de escrita, tradução ou ingestão.

---

## Por que isso importa

Os agentes de research recebem uma janela de 24h explícita — "eventos que ocorreram entre 30/07 10:00 BRT e 31/07 10:00 BRT". A qualidade da busca é medida sobretudo por **quantos resultados caem dentro da janela** e **se a fonte primária aparece**. Hoje isso é resolvido no texto da query e na leitura do agente, não no provedor.

---

## Baseline medido — sessão de 2026-07-31

Sessão `bf36ab9a-e179-4c47-bbaa-efaf0fb0dfd0` (rodou no Pi, ~09:55–10:30 BRT). Arquivada em
`~/Documents/claude-sessions-archive/pi/-home-guilhermesaboia-ai-newsletter/`.

- **18 subagents** no total; **5 usaram Exa**, 13 não tocaram em busca (escrita/tradução/montagem).
- **34 chamadas Exa**: 32 × `web_search_exa` + 2 × `web_fetch_exa` (3 URLs).
- **32 queries distintas**, nenhuma repetida entre agentes.
- 1 única chamada `WebSearch` nativa, com `allowed_domains: ["youtube.com"]`.

Distribuição de `numResults`: 6 em 18 queries, 8 em 13, 10 em 1. Todas ≤ 10 → sem cobrança de resultado extra na Exa (**32 × $0.007 ≈ $0.22** na edição).

Por agente:

| agente | papel | buscas |
|---|---|---|
| `agent-af2a5bbbc1c30b7ec` | Research — cluster chips/hardware | 12 |
| `agent-a5c49bcad3a0e80b3` | Research — cluster mundo/mercados | 12 |
| `agent-a9d3c543957b50529` | Research — cluster modelos/labs | 6 |
| `agent-a8f5f0c23015af7ef` | Imagem editorial | 1 |
| `agent-aee543b7f73be5cbf` | Imagem editorial | 1 |

### Nenhum parâmetro de tempo foi usado

As 32 chamadas passaram **exatamente dois campos**: `query` e `numResults`. As chaves distintas em todos os 34 inputs são `query`, `numResults`, `urls`, `maxCharacters`. Nada mais.

O recorte temporal existiu **só como texto dentro da query**:

| forma | n |
|---|---|
| `July 30` no texto | 10 |
| `July 31` no texto | 9 |
| `July 2026` (mês, sem dia) | 1 |
| `2026` sem `July` (era `Q3 2026`) | 1 |
| **nenhum marcador temporal** | **11** |

Isso não foi descuido do agente: a tool MCP da Exa **não expõe** filtro de data (ver matriz abaixo).

### Os dois perfis de query

O padrão de quem tem e quem não tem data revela dois usos distintos, e o benchmark precisa separá-los.

**A — Exploratória (20 queries).** "O que aconteceu na categoria X nesse dia." A data é parte da busca; o agente não sabe o fato ainda.

> `Nvidia data center announcement July 30 2026` · `pharma deal acquisition July 31 2026 biotech billion` · `chip export controls China semiconductor restrictions announcement July 30 2026` · `US jobs report July 31 2026 economy data` · `humanoid robotics startup funding round announced July 30 2026` · …

**B — Confirmação (11 queries).** O agente já sabe o fato (de outra fonte do pipeline) e busca corroboração. Os termos já são discriminantes; data seria ruído.

- Space-Eyes SPAC merger $638 million Eric Trump defense technology
- Leopold Aschenbrenner profile article Situational Awareness hedge fund photo
- Anthropic models unauthorized access three organizations cybersecurity evaluations incident
- DeepSeek V4 Flash API public beta pricing benchmark
- OpenAI cuts price GPT-5.6 Luna 80% Terra 20% Sol fast mode API
- Thinking Machines Inkling-Small open weights 276B parameters release
- MiniMax H3 video model 2K resolution native audio release
- Chinese military researchers distilled OpenAI Anthropic models defence systems papers patents
- Google DeepMind Gemini Robotics 2 humanoid robots launch
- Commerce Department CHIPS Act equity stakes GlobalFoundries $874 million letters of intent
- Anthropic custom chip Samsung foundry beyond Nvidia report

**Consequência para o teste:** filtro de data deve ajudar no perfil A e **atrapalhar** no B — a matéria que corrobora o fato pode ter sido publicada fora da janela, e o próprio prompt dos agentes admite isso ("Articles covering the event may be published slightly after the window closes; that's fine"). Medir os dois juntos faz o filtro parecer que derruba recall quando está sendo aplicado onde não devia.

---

## Matriz de capacidade

### Filtro de tempo

| | parâmetro | granularidade | ordenar por data |
|---|---|---|---|
| **WebSearch** (Claude Code) | **nenhum** | — | não |
| **Exa** — tool MCP | **nenhum** | — | não |
| **Exa** — REST | `startPublishedDate` / `endPublishedDate` | ISO 8601, **hora e minuto** | não exposto |
| **Firecrawl** `/search` | `tbs` | `cdr` = **dia inteiro**; `qdr` = janela relativa | sim (`sbd:1`) |

Valores de `tbs`: `qdr:h|d|w|m|y` (última hora/dia/semana/mês/ano) · `cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY` · `sbd:1` · combináveis (`"sbd:1,qdr:w"`).
`startCrawlDate`/`endCrawlDate` da Exa existem mas estão **deprecados e ignorados**.

**A janela do pipeline atravessa a virada do dia** (30/07 10:00 BRT → 31/07 10:00 BRT = 13:00Z → 13:00Z):

- **Exa REST** expressa exato: `startPublishedDate=2026-07-30T13:00:00Z`, `endPublishedDate=2026-07-31T13:00:00Z`.
- **Firecrawl `cdr`** só chega a `cd_min:07/30/2026,cd_max:07/31/2026` — dois dias inteiros, ~48h, o dobro da janela.
- **Firecrawl `qdr:d`** é 24h relativas à chamada. Como o cron roda ~10:00 BRT, cai praticamente em cima da janela editorial de graça. **Frágil**: se o cron atrasar 40 min, a janela desliza junto.

### Superfície completa dos parâmetros

| | WebSearch | Exa REST | Firecrawl `/search` |
|---|---|---|---|
| query | ✔ | ✔ (máx. n/d) | ✔ (máx. 500 chars) |
| nº de resultados | — | `numResults` 1–100 (default 10) | `limit` default 10, máx 100 |
| domínios | `allowed_domains` / `blocked_domains` | `includeDomains` / `excludeDomains` (até 1200) | `includeDomains` / `excludeDomains` (mutuamente exclusivos) |
| categoria | — | `category`: company, publication, **news**, personal site, financial report, people | `sources`: web, images, **news**; `categories`: github, research, pdf |
| profundidade | — | `type`: instant, fast, auto, deep-lite, deep, deep-reasoning | — |
| conteúdo extraído | — | `contents` (text / highlights / summaries / extras) | `highlights` (**default true**), `scrapeOptions` |
| saída estruturada | — | `outputSchema` (JSON schema), `systemPrompt` | — |
| geo | — | `userLocation` (ISO-2) | `location`, `country` (default US) |
| outros | — | `moderation`, `stream` | `timeout` (default 60s), `ignoreInvalidURLs`, `enterprise` (ZDR), `threatProtection` |

A tool server-side da Anthropic (`web_search_20260209`, usada via API e não via Claude Code) tem um pouco mais que a tool do CLI — `max_uses`, `allowed_domains`/`blocked_domains`, `user_location` — mas **também nenhum filtro de data**.

### Custo

| | preço |
|---|---|
| **Exa** `/search` | **$7 / 1k requests** (até 10 resultados) · +$1/1k por resultado acima de 10 · `deep-lite`/`deep` $12/1k · `deep-reasoning` $15/1k · resumos IA +$1/1k páginas |
| **Firecrawl** `/search` | **2 créditos por 10 resultados**, arredondando pra cima (1–10 → 2; 11–20 → 4) · `scrapeOptions` +1 crédito/página · PDF +1/página · proxy enhanced +4/página · JSON mode +4/página |
| **WebSearch** (Claude Code) | não medido — ver questões em aberto |

---

## Head-to-head preliminar (n=1)

Query `Nvidia Hut 8 Beacon Point Texas lease Financial Times July 30 2026`, rodada em 2026-07-31 nas duas ferramentas disponíveis.

| dimensão | WebSearch | Exa (MCP, `numResults: 6`) |
|---|---|---|
| resultados | 10 links + resumo em prosa | 6 itens com metadados |
| **datas de publicação** | **ausentes** | ISO em todo resultado |
| **fonte primária (ft.com)** | **não apareceu** | **resultado #1** |
| duplicação | 50% (5/10 do mesmo fio Reuters em rádios locais) | 50% (3/6 do mesmo texto Insider Monkey) |
| histórias únicas | ~6 de 10 slots | 4 de 6 slots |
| conteúdo | síntese escrita por um modelo | highlights extraídos, texto verbatim |
| volume | ~2,6 mil chars | ~7,5 mil chars |
| fact-check embutido | **sim** — corrigiu a premissa da query (o FT publicou em 28/07, não 30/07) | não |

**Ressalvas:** n=1; a query escolhida favorece a Exa (evento datado com fonte primária identificável); e não é apples-to-apples — o `WebSearch` do Claude Code roda um modelo de síntese em cima dos resultados, então é "busca + resumo" contra "busca + extração", não rankings crus.

---

## Desenho do benchmark

**5 configurações × 2 perfis de query = 10 células.**

| # | configuração |
|---|---|
| 1 | `WebSearch` nativo (baseline do harness) |
| 2 | Exa via MCP — `query` + `numResults`, **o que roda hoje** |
| 3 | Exa REST — `startPublishedDate`/`endPublishedDate` + `category: news` |
| 4 | Firecrawl — `tbs: "qdr:d"`, `sources: ['news']` |
| 5 | Firecrawl — `tbs: "cdr:1,cd_min:07/30/2026,cd_max:07/31/2026"` |

**Perfil A** = as 20 queries exploratórias · **Perfil B** = as 11 de confirmação. Nas configs 3–5, rodar o perfil A **também sem a data no texto da query** — o ponto de usar filtro server-side é liberar esses tokens para termos mais discriminantes.

### Métricas

1. **Precisão de janela** — % de resultados cuja data de publicação cai em 30/07 13:00Z – 31/07 13:00Z. A métrica principal do perfil A.
2. **Fonte primária no top-3** — apareceu o veículo que deu o furo, ou só agregadores?
3. **Histórias únicas / slots** — o dedup foi 50% nas duas na amostra n=1; medir se alguma config melhora.
4. **Recall no perfil B** — achou corroboração do fato conhecido? Filtro de data deve **piorar** aqui; quantificar o quanto.
5. **Custo por query** e **chars de contexto por query** — o segundo importa: são 32 buscas × 5 agentes numa edição.

---

## Questões em aberto — medir, não assumir

- **`tbs` é sintaxe do Google.** A Firecrawl expõe o parâmetro, mas o filtro opera sobre a noção de data do buscador, que para muitas páginas é **inferida**, não a data de publicação declarada. Não é necessariamente o mesmo que o `publishedDate` da Exa. Comparar o que cada uma considera "publicado em" faz parte do teste.
- **A Firecrawl devolve data no resultado?** Não confirmado. Se não devolver, o filtro server-side ajuda mas o agente perde a checagem de janela na leitura — e a métrica 1 fica impossível de calcular sem um fetch extra por resultado.
- **Preço do crédito Firecrawl em dólar.** Não verificado numa fonte. Sem isso, a comparação de custo com a Exa ($7/1k) não fecha.
- **Custo do `WebSearch` do Claude Code.** Não medido.
- **A Exa REST tem `sbd`-equivalente?** Não achei ordenação por data na doc; se não houver, `endPublishedDate` + relevância é o máximo.

---

## Como reproduzir a extração

As chamadas ficam nos JSONL de subagents, não no transcript principal (lá só aparecem menções nos prompts dos `Agent`).

```bash
D=~/Documents/claude-sessions-archive/pi/-home-guilhermesaboia-ai-newsletter/<session-id>
for f in $D/subagents/*.jsonl; do
  jq -c --arg agent "$(basename $f .jsonl)" \
    '.. | objects | select(.type?=="tool_use" and (.name?|tostring|test("exa";"i")))
     | {agent:$agent, id:.id, name:.name, input:.input}' "$f"
done
```

Dois cuidados: use varredura recursiva (`.. | objects`) — um `select(.message.content[])` raso perde chamadas; e `grep -c "web_search_exa"` **superconta**, porque o nome da tool também aparece em prompts e system reminders.

---

## Histórico

- **2026-07-31** — baseline medido na sessão `bf36ab9a`, capacidades levantadas nas docs dos três provedores, head-to-head n=1, desenho fechado. Execução adiada: créditos Firecrawl esgotados, renovam 2026-08-16.
