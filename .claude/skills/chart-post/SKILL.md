---
name: chart-post
description: >-
  Cria um post de gráfico do Substack a partir de uma história da edição do dia da newsletter de AI/Tech. Lê o edition-final.md, propõe 6 candidatos de gráfico via AskUserQuestion (com previews ASCII), Gui escolhe, pesquisa dados de FONTES PRIMÁRIAS (citable > derived), resolve qualquer divergência de método com Gui, grava os dados auditáveis em posts/data/<slug>.json, constrói o chart copiando o scaffolding de marca de um posts/chart-*.html existente, renderiza em PNG 2× via render.sh (Mac: browser-tools no Brave real; Pi/Linux: Chromium headless), inspeciona os labels, e escreve a prosa em posts/chart-<slug>.md. Voz neutra/profissional, título factual/descritivo, todas as ressalvas no caption (não na prosa). Aciona quando o usuário diz "fazer um post com gráfico", "post de gráfico do dia", "craft a substack post with a chart", "/chart-post".
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch, AskUserQuestion
---

## Quando essa skill roda

Tarefa recorrente: "fazer um post de gráfico do Substack" a partir da edição do dia. O gráfico = dado histórico/comparativo confiável que conta a história sozinho e **promove aquela edição**. Os arquivos ficam em `posts/` (spec de marca no CLAUDE.md "Posts"). Roda depois que o `edition-final.md` do dia existe (o draft já foi empurrado pro Substack).

`edition-final.md` → **chart-post** → `posts/data/<slug>.json` (dados auditáveis) + `posts/chart-<slug>.html` (chart) + `posts/chart-<slug>.png` (render 2×) + `posts/chart-<slug>.md` (prosa) → rascunho de Note no Substack (`note-draft.sh`, depois do OK final; o Gui publica).

**Garimpo e mecânica são automáticos; gosto e rigor de dado são do Gui.** Os pontos de julgamento (qual gráfico, qual fonte, resolver divergência de método, aprovar labels, aprovar prosa) passam por ele via AskUserQuestion ou apresentação. Não publique sozinho.

## Args

`/chart-post [YYYY-MM-DD]` — sem arg usa hoje (`date '+%Y-%m-%d'`).

## Step 0: Data e validação

```bash
DATE=${ARG:-$(date '+%Y-%m-%d')}
BASE=~/ai-newsletter/pipeline/output/ai/$DATE
test -f "$BASE/edition-final.md" || { echo "sem edition-final.md em $BASE"; ls ~/ai-newsletter/pipeline/output/ai/ | tail -8; }
```
Sem `edition-final.md`, **não invente** — liste as datas e pare. **Leia o `edition-final.md` inteiro** (e o `research.json` pra fontes/números): a escolha do gráfico sai da história, não de uma entidade qualquer.

## Step 1: Propor candidatos de gráfico (julgamento do Gui)

Identifique as histórias com **dado confiável e visualizável** (série temporal, comparação, ranking) — não toda história vira gráfico. Proponha **6 candidatos**, cada um com um **preview ASCII** do que o gráfico mostraria e a fonte provável. O AskUserQuestion aceita no máximo 4 opções por pergunta, então mande **duas perguntas na mesma chamada** — "Candidatos 1-3" e "Candidatos 4-6", 3 opções cada, e uma quarta opção "nenhum deste bloco" em ambas. Gui marca o preferido de cada bloco (ou descarta o bloco); se ele marcar um em cada, confirme qual dos dois vai virar o post antes de pesquisar dado. Defina o `<slug>` (kebab-case) a partir da escolha.

Bons candidatos: séries anuais com uma virada clara (funding, shipments, adoção), comparações entre países/empresas, "antes vs depois". Evite: número solto sem série, dado que você só conseguiria por interpolação (ver Step 2).

## Step 2: Pesquisar os dados (FONTES PRIMÁRIAS) e resolver o fork de método

Pesquise a série de **fontes primárias** (relatórios anuais, releases oficiais, o report nominal — **não** agregadores). Firecrawl costuma estar sem créditos; use **Exa + WebFetch**, e `WebSearch` pra achar o report nominal.

**O rigor de dado do Gui é o coração da skill (forte e consistente):**
- **Citable > derived.** Ele rejeita números que você computou/interpolou (ex.: um acumulado somado de shipments anuais). Plote a **série crua reportada**.
- **Largue a série problemática em vez de fudge.** Se um corte tem método incompatível com os outros (ex.: EUA medido diferente) ou é um "0" achatado, **tire do gráfico** — o ângulo largado vai pra prosa, não pro chart.
- **Moeda: mantenha a unidade nativa da fonte** quando converter adiciona uma premissa (€→US$ precisa de uma taxa = número derivado). A newsletter padroniza US$, então **sinalize o trade-off e recomende o citável**.
- **Dado preliminar/projeção é OK SE marcado:** cor de projeção `#7DB89B`, segmento tracejado, ponto vazado, labels `≥`/`~`/"est.". Ano parcial (ex.: "jan–mai, ~5 meses") = barra preliminar.
- **Divergência entre fontes (método/data de corte) → fonte única + ponte no caption.** Se PitchBook e Crunchbase não batem, escolha **uma** fonte pro gráfico inteiro e explique a outra no caption. Nunca misture séries de métodos diferentes no mesmo eixo.

**Apresente os dados verificados ao Gui e, se houver um fork de método, resolva via AskUserQuestion** (com as opções concretas, ex.: "fonte A só / fonte B só / as duas lado a lado"). Só depois construa.

## Step 3: Gravar os dados auditáveis

Escreva `posts/data/<slug>.json` ANTES do chart. Estrutura (espelha os posts existentes):

```json
{
  "slug": "<slug>", "title_pt": "<título do dado>", "edition": "YYYY-MM-DD",
  "metric": "<o que mede + unidade>",
  "definition": "<definição exata da fonte: categoria, escopo, inclusões>",
  "series": [{ "year": 2025, "usd_bn": 9.6, "preliminary": false, "source_ref": "<id>" }],
  "sources": [{ "id": "<id>", "label": "<fonte — título do report (data)>", "url": "<url>", "provides": "<que números>" }],
  "notes": ["<fluxo vs estoque>", "<o que é parcial/estimado>", "<a ponte pro outro recorte que vai no caption>"]
}
```
`sources` = label + url (citável). `notes` = o que é medido vs estimado, e as ressalvas (que vão pro caption, não pra prosa). Dados auditáveis = commitados no repo.

## Step 4: Construir o chart (copiar o scaffolding de marca)

**Não escreva o HTML do zero — copie um `posts/chart-*.html` existente** e troque os dados. Use o que mais se parece com o teu formato:
- série temporal anual com projeção → `chart-asml-euv-machines.html`
- comparação entre países/categorias → `chart-genai-adoption-by-country.html`
- duas séries / dual-axis → idem ASML

```bash
ls posts/chart-*.html
```

Spec de marca completa no **CLAUDE.md "Posts"** (card 720px, H1 Helvetica 24px/700, footer fonte+`dailyjournal.news`, paleta `#044B2E`/`#7DB89B`/etc., logo via `<img src="../../daily-journal-platform/...">` — nunca duplique a logo). Regras fixas: `animation: false`, `tooltip: { enabled: false }`, `id="capture"` no card, e legenda com `.legend > span { display: inline-flex; align-items: center; }` (sem `vertical-align: middle` nos swatches — alinha pelo x-height do texto e deixa o quadradinho baixo). Labels só em endpoints e milestones (plugin `afterDraw`), não em toda barra.

- **Logo DJ: no header só se o título couber em UMA linha com ela ao lado.** Aí a logo vai no header, à direita, centralizada verticalmente no título (`.header` flex, `align-items:center`, `justify-content:space-between`; `.logo` 18px, `flex-shrink:0`). Se o título quebraria em duas linhas com a logo ali, o header fica só com o título (`max-width: none`) e a logo entra DENTRO do gráfico como marca d'água (Step 5). Confira no render. (Gui, 2026-09-23.)

- **Título factual/descritivo, não editorial.** "Startups de defesa já captaram mais em 2026 do que em todo 2025" ✅; "como o VC descobriu a defesa" ❌ (editorial, foi rejeitado). Pode ser o nome da métrica ("Remessas globais de smartphones do grupo Xiaomi") — o ângulo da notícia mora no subtítulo.
- **Não duplique no chart o que o título já diz.** Se o título carrega o "recorde", corte a linha de anotação "recorde" redundante.
- **Caption/footnote = SÓ fonte.** O footnote fica APENAS com dados sobre fontes: qual relatório/órgão dá cada número e a ponte de fonte (ex.: "2025: 170 mi conforme a Nikkei; o IDC mediu 165,3 mi"). Nada de caracterização da história ali. Ressalva de moeda mora no label da legenda. (Regra do Gui, 2026-06-30.) **Nem menção ao que NÃO está no gráfico** (série descartada, versão antiga do benchmark, outro recorte): isso vai pra prosa se for relevante, ou pra lugar nenhum. (Gui, 2026-09-21.)
- **Caracterização interessante sobre os dados → SUBTÍTULO (kicker), não o caption.** O que é medido (fluxo vs estoque, escopo/marcas), o que é meta vs realizado, o "cortou pela segunda vez no ano", o contexto setorial (Oppo/Vivo também cortaram) — tudo isso é a história e vai no subtítulo, com os números-chave em `<b>` (verde). O caption não conta história.
- **Dual-axis:** alinhe as frações dos ticks pra ambos os eixos caírem nas MESMAS gridlines (ex.: esq max 75 step 25 = 0/25/50/75; dir max 18 step 6 = 0/6/12/18). `grid` só num eixo.

## Step 5: Renderizar e inspecionar (julgamento dos labels)

```bash
.claude/skills/chart-post/render.sh <slug>
```
Faz o ciclo 2× retina inteiro (nav-se-existe-senão-abre → mede `#capture` → resize 800×H → screenshot → **recorta no card `#capture`** → grava `posts/chart-<slug>.png`). O PNG sai justo no card, sem a margem branca do body. Re-render depois de editar o HTML = rodar de novo (reaproveita a aba).

**Plataforma:** o render.sh detecta sozinho. No **Mac**, browser-tools no Brave **real** (headless trava no setup de perfil). No **Pi (Linux)**, Chromium headless via `headless-render.js` (CDP puro, sem deps npm; headless funciona no Linux) — mesmo output, mesmo card 1440px. A fonte no Pi cai num clone de Helvetica visualmente equivalente; sem ajuste necessário.

**Read o PNG** pra julgar. Pra ver overlap de label de perto, **crope** (um Read da imagem inteira rebaixa demais):
```bash
magick posts/chart-<slug>.png -crop WxH+X+Y +repage /tmp/x.png   # depois Read /tmp/x.png
# no Pi (ImageMagick 6): convert no lugar de magick
```
Itere o HTML → `render.sh` → Read até os labels estarem limpos. Se o PNG sair em branco/baixo, rode `render.sh` de novo.

**Posicionar a logo DJ dentro do gráfico (só quando o título não comporta a logo no header; julgamento visual, com o gráfico já pronto).** A logo vai DENTRO do gráfico, num `<img class="chart-logo">` (`height` ~15px) com `position:absolute` dentro do `.chart-container` (que precisa ser `position:relative`).

Primeiro ache o **quadrante vazio do plot**: padrão é o **canto inferior direito** (funciona quando os dados sobem pra direita). Se os dados ocupam esse canto (série decrescente, barras altas à direita), vá pro canto limpo (superior direito/esquerdo).

Depois **alinhe pela geometria do plot, não no olho** — meça com `render.sh --eval` (funciona no Mac e no Pi) e calcule o CSS:
```bash
.claude/skills/chart-post/render.sh <slug> --eval \
  "(function(){var c=Chart.getChart('<canvasId>');var k=document.querySelector('.chart-container');return {areaRight:Math.round(c.chartArea.right),areaBottom:Math.round(c.chartArea.bottom),contW:k.clientWidth,contH:k.clientHeight};})()"
```
Pra inferior-direito: `right = contW − areaRight` (a borda direita da logo encosta no fim da linha do eixo X) e `bottom = contH − areaBottom + ~12` (folga acima da linha do eixo). Re-renderize e confira: a logo respira, sem encostar nos labels do eixo nem nos dados.

**Empurrar um label específico** sem mexer nos outros: dê um offset `dx`/`dy` por ponto no plugin de labels (ex.: `ctx.fillText(r.label, pt.x + (r.dx||0), pt.y + ...)`) — assim "mexe o El Capitan 2px pra direita" vira só `dx: 2` naquela linha.

## Step 6: Escrever a prosa

Escreva `posts/chart-<slug>.md`. Formato (espelha os posts existentes):

```markdown
# <título factual = mesmo do chart>

**Edição:** YYYY-MM-DD
**Chart:** `chart-<slug>.png`
**Fonte:** <fonte>

---

<2-4 parágrafos: a história. Abre com o fato.>

As demais histórias do dia estão na [edição completa](<url pública da edição no Substack>):
```

**URL da edição = a pública `/p/<slug>`, NUNCA a do editor** (`/publish/post/<id>`, que é o que está em `substack-draft.json` e só abre pra quem edita). **Não derive o slug do título** (a regra de truncamento do Substack não é previsível: em 10/09/2026 saiu `...-10-de-setembro`, sem o `-de` que 09/09 tinha). Resolva pelo id, que o Substack redireciona pro slug canônico:
```bash
ID=$(python3 -c "import json;print(json.load(open('$BASE/substack-draft.json'))['id'])")
curl -sI "https://dailyjournalnews.substack.com/p/$ID" | grep -i '^location' | awk '{print $2}' | tr -d '\r'
```
Só funciona depois de publicado (draft não redireciona, o `Location` vem vazio ou aponta pra home). Se a edição ainda não foi publicada, deixe o link com o placeholder `/p/$ID` e diga ao Gui que precisa resolver depois; nunca chute. Alternativa quando o cache já atualizou: `curl -s 'https://dailyjournalnews.substack.com/api/v1/archive?sort=new&limit=3'` lista `canonical_url` por `id`. (Gui, 2026-09-10.)

**Voz (erros desta tarefa, não repita):**
- **Registro neutro/profissional, nunca coloquial.** "permaneceram próximos de US$3 bi" ✅; "travados", "o dinheiro seguiu", "atropelou" ❌.
- **Sem frase-moldura editorializante** (pigarro analítico): não abra parágrafo com "A mudança reflete...", "O movimento sinaliza...". Abra com o **fato**, mostre não conte.
- **Deixe o escopo do número explícito** (mundo vs EUA vs uma empresa). Se a série é global, diga "no mundo"; se um recorte é só-EUA, diga.
- **Glose o jargão uma vez** ("o venture capital, o capital de risco que financia startups").
- **Curto.** Posts são bem curtos (3 parágrafos é normal).
- **Ao mandar o texto no chat, mande SÓ o texto, sem NENHUMA formatação** — sem blockquote (`>`), sem barra de metadados, sem negrito, sem aspas de cerca. Texto cru, pronto pra copiar e colar direto. (Gui, 2026-06-30.)

**Negrito e itálico na prosa** (o `.md` carrega as marcas; `note-draft.sh` as leva pro Note. Levantado dos 30 Notes de gráfico de 23/06 a 23/09/2026; Gui, 2026-10-01):
- **Itálico (`*termo*`) = jargão em inglês não aportuguesado**, o mesmo critério da edição: *tokens*, *input*, *output*, *neoclouds*, *releases*, *preview*, *gateway*, *float*, *follow-on*, *capture-the-flag*, *stablecoins*. Vale no parágrafo da primeira menção (todas as ocorrências ali); nos parágrafos seguintes o termo volta sem itálico. **Sem itálico:** nomes próprios, produtos e empresas, siglas (HBM, IPO), e os termos já correntes em português (startup, data center, chip, software, venture capital, run-rate, pull request).
- **Negrito (`**termo**`) = as entidades que ancoram a história, na primeira menção**: quem age (empresa/país), o produto, modelo ou benchmark que o gráfico mede, e a fonte do dado (ex. de 21 a 23/09: "**Anthropic**", "**Claude Opus 5.5**", "**FrontierMath Tier 4**", "**Epoch AI**", "**Pew Research Center**"). Quase tudo no primeiro parágrafo; num parágrafo posterior só entra entidade nova que seja o gancho da notícia (ex.: os outros modelos comparados). De 2 a 5 negritos por Note, nunca frase inteira.
- **Sem negrito em números.** Notes de julho negritavam cifras e frases ("**485 TWh**"); o padrão recente largou isso. O número já está no gráfico.
- A linha final ("As demais histórias do dia...") fica sem marca nenhuma.
- Negrito e itálico não se combinam no mesmo termo: termo estrangeiro que também é o sujeito da história fica só em itálico.

**Antes de dar OK pra postar, releia fato a fato + gramática** e confirme que cada número casa com o `posts/data/<slug>.json`.

## Em dashes

Proibidos em tudo que a skill produz: título, kicker, legenda, footer e prosa. No lugar, vírgula, ponto ou dois-pontos. (Gui, 2026-09-01.)

## Step 7: Rascunho do Note no Substack (quando o Gui der o OK final)

Só depois do OK final do Gui no chart **e** na prosa:

```bash
.claude/skills/chart-post/note-draft.sh <slug>
```
Sobe o PNG, anexa o card da edição e salva o texto como **rascunho** de Note (`sstats note-draft`; devolve `id` + `attachments: ["image","post"]`). **Não publica**: o rascunho aparece no composer de Notes do Substack, em Drafts, e o Gui posta de lá (é onde ele põe os negritos). Diga a ele o `id` e que está em Drafts.

- **Mudou a prosa ou o chart depois?** `note-draft.sh <slug> --id <id>` substitui o mesmo rascunho. Não crie um segundo. `sstats note-drafts` lista; `sstats note-draft-delete <id>` apaga.
- O script recusa link placeholder (`/p/<id>`) ou de editor: resolva a URL pública antes (Step 6).
- **Nunca** chame `POST /api/v1/comment/feed`: esse endpoint publica o Note na hora. A skill só cria rascunho.
- Se `sstats note-draft` falhar (API do Substack mudou), o fallback é o manual: Gui cola o texto e o PNG no composer.

## Step 8: Commit (quando o Gui pedir)

Posts são commitados (charts + `posts/data/*.json` = dados auditáveis). `origin/main` avança sozinho (Pi recommendations cron, ~meio-dia BRT, pusha deste clone) — **`git pull --rebase origin main` antes de pushar** ou o push é rejeitado. A publicação em si é manual: o Gui posta o rascunho do Step 7 pelo composer de Notes.

## Regras

- **Garimpo automático, escolha humana.** Candidato de gráfico, fonte, fork de método, labels e prosa passam pelo Gui. Nunca publique sozinho.
- **Rascunho sim, publicação não.** Com o OK final, `note-draft.sh` salva o Note como rascunho no Substack; quem publica é o Gui, no composer.
- **Citable > derived.** Plote números reportados, não interpolados/computados. Largue a série problemática em vez de fudge.
- **Caption/footnote = só fonte; caracterização da história → subtítulo.** O footnote fica só com de-onde-vem-cada-número (e a ponte de fonte). O que é medido, meta vs realizado, contexto setorial = subtítulo. Nunca na prosa nem no título. (Gui, 2026-06-30.)
- **Render sempre via `render.sh`** — ele escolhe o backend pela plataforma: Mac = browser-tools no Brave real (headless de Brave trava no setup de perfil), Pi/Linux = Chromium headless (`headless-render.js`). Nunca tente headless no Mac nem browser-tools no Pi.
- **Não duplique a logo DJ** — referencie de `daily-journal-platform`.
- **Título factual, voz neutra, sem frase-moldura.** Os três erros que o Gui corrigiu — não os repita.
