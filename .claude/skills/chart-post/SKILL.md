---
name: chart-post
description: >-
  Cria um post de gráfico do Substack a partir de uma história da edição do dia da newsletter de AI/Tech. Lê o pt.md, propõe 3-4 candidatos de gráfico via AskUserQuestion (com previews ASCII), Gui escolhe, pesquisa dados de FONTES PRIMÁRIAS (citable > derived), resolve qualquer divergência de método com Gui, grava os dados auditáveis em posts/data/<slug>.json, constrói o chart copiando o scaffolding de marca de um posts/chart-*.html existente, renderiza em PNG 2× via render.sh (browser-tools, não headless), inspeciona os labels, e escreve a prosa em posts/chart-<slug>.md. Voz neutra/profissional, título factual/descritivo, todas as ressalvas no caption (não na prosa). Aciona quando o usuário diz "fazer um post com gráfico", "post de gráfico do dia", "craft a substack post with a chart", "/chart-post".
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch, AskUserQuestion
---

## Quando essa skill roda

Tarefa recorrente: "fazer um post de gráfico do Substack" a partir da edição do dia. O gráfico = dado histórico/comparativo confiável que conta a história sozinho e **promove aquela edição**. Os arquivos ficam em `posts/` (spec de marca no CLAUDE.md "Posts"). Roda depois que o `pt.md` do dia existe (não precisa estar finalizado).

`pt.md` → **chart-post** → `posts/data/<slug>.json` (dados auditáveis) + `posts/chart-<slug>.html` (chart) + `posts/chart-<slug>.png` (render 2×) + `posts/chart-<slug>.md` (prosa pra colar como Substack Note).

**Garimpo e mecânica são automáticos; gosto e rigor de dado são do Gui.** Os pontos de julgamento (qual gráfico, qual fonte, resolver divergência de método, aprovar labels, aprovar prosa) passam por ele via AskUserQuestion ou apresentação. Não publique sozinho.

## Args

`/chart-post [YYYY-MM-DD]` — sem arg usa hoje (`date '+%Y-%m-%d'`).

## Step 0: Data e validação

```bash
DATE=${ARG:-$(date '+%Y-%m-%d')}
BASE=/Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE
test -f "$BASE/pt.md" || { echo "sem pt.md em $BASE"; ls /Users/guilherme/ai-newsletter/pipeline/output/ai/ | tail -8; }
```
Sem `pt.md`, **não invente** — liste as datas e pare. **Leia o `pt.md` inteiro** (e o `research.json` pra fontes/números): a escolha do gráfico sai da história, não de uma entidade qualquer.

## Step 1: Propor candidatos de gráfico (julgamento do Gui)

Identifique as histórias com **dado confiável e visualizável** (série temporal, comparação, ranking) — não toda história vira gráfico. Proponha **3-4 candidatos via AskUserQuestion**, cada um com um **preview ASCII** do que o gráfico mostraria e a fonte provável. Gui escolhe. Defina o `<slug>` (kebab-case) a partir da escolha.

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

Spec de marca completa no **CLAUDE.md "Posts"** (card 720px, H1 Helvetica 24px/700, footer fonte+`dailyjournal.news`, paleta `#044B2E`/`#7DB89B`/etc., logo via `<img src="../../daily-journal-platform/...">` — nunca duplique a logo). Regras fixas: `animation: false`, `tooltip: { enabled: false }`, `id="capture"` no card. Labels só em endpoints e milestones (plugin `afterDraw`), não em toda barra.

- **Header = só o título, largura cheia (`max-width: none`).** A logo DJ **não** vai no header — ela rouba largura e quebra o título em duas linhas. A logo entra DENTRO do gráfico como marca d'água (Step 5).

- **Título factual/descritivo, não editorial.** "Startups de defesa já captaram mais em 2026 do que em todo 2025" ✅; "como o VC descobriu a defesa" ❌ (editorial, foi rejeitado).
- **Não duplique no chart o que o título já diz.** Se o título carrega o "recorde", corte a linha de anotação "recorde" redundante.
- **Todas as ressalvas vão no CAPTION**, não no título nem na prosa: o que é medido (fluxo vs estoque), preço/método, o que é parcial/estimado, a ponte pro outro recorte. Ressalva de moeda mora no label da legenda.
- **Dual-axis:** alinhe as frações dos ticks pra ambos os eixos caírem nas MESMAS gridlines (ex.: esq max 75 step 25 = 0/25/50/75; dir max 18 step 6 = 0/6/12/18). `grid` só num eixo.

## Step 5: Renderizar e inspecionar (julgamento dos labels)

```bash
.claude/skills/chart-post/render.sh <slug>
```
Faz o ciclo 2× retina inteiro (nav-se-existe-senão-abre → mede `#capture` → resize 800×H → screenshot → **recorta no card `#capture`** → grava `posts/chart-<slug>.png`). O PNG sai justo no card, sem a margem branca do body. Re-render depois de editar o HTML = rodar de novo (reaproveita a aba). Browser-tools usa o Brave **real** (headless trava).

**Read o PNG** pra julgar. Pra ver overlap de label de perto, **crope** (um Read da imagem inteira rebaixa demais):
```bash
magick posts/chart-<slug>.png -crop WxH+X+Y +repage /tmp/x.png   # depois Read /tmp/x.png
```
Itere o HTML → `render.sh` → Read até os labels estarem limpos. Se o PNG sair em branco/baixo, rode `render.sh` de novo.

**Posicionar a logo DJ (julgamento visual, com o gráfico já pronto).** A logo vai DENTRO do gráfico, num `<img class="chart-logo">` (`height` ~15px) com `position:absolute` dentro do `.chart-container` (que precisa ser `position:relative`).

Primeiro ache o **quadrante vazio do plot**: padrão é o **canto inferior direito** (funciona quando os dados sobem pra direita). Se os dados ocupam esse canto (série decrescente, barras altas à direita), vá pro canto limpo (superior direito/esquerdo).

Depois **alinhe pela geometria do plot, não no olho** — meça com browser-eval e calcule o CSS:
```bash
cd ~/agent-tools/browser-tools && ./browser-eval.js -t="chart-<slug>.html" \
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

As demais histórias do dia estão na [edição completa](<url da edição no Substack>):
```

**Voz (erros desta tarefa, não repita):**
- **Registro neutro/profissional, nunca coloquial.** "permaneceram próximos de US$3 bi" ✅; "travados", "o dinheiro seguiu", "atropelou" ❌.
- **Sem frase-moldura editorializante** (pigarro analítico): não abra parágrafo com "A mudança reflete...", "O movimento sinaliza...". Abra com o **fato**, mostre não conte. Ver memória `feedback_no_framing_sentences`.
- **Deixe o escopo do número explícito** (mundo vs EUA vs uma empresa). Se a série é global, diga "no mundo"; se um recorte é só-EUA, diga.
- **Glose o jargão uma vez** ("o venture capital, o capital de risco que financia startups").
- **Curto.** Posts são bem curtos (3 parágrafos é normal). Mande o texto puro (sem a barra de metadados) quando o Gui for colar.

**Antes de dar OK pra postar, releia fato a fato + gramática** e confirme que cada número casa com o `posts/data/<slug>.json`.

## Step 7: Commit (quando o Gui pedir)

Posts são commitados (charts + `posts/data/*.json` = dados auditáveis). `origin/main` avança sozinho (Pi recommendations cron, ~meio-dia BRT, pusha deste clone) — **`git pull --rebase origin main` antes de pushar** ou o push é rejeitado. A publicação em si é manual (cola o `.md`/`.png` no editor do Substack como Note; ver memórias `publish-gap-substack`, `chart-post-workflow`).

## Regras

- **Garimpo automático, escolha humana.** Candidato de gráfico, fonte, fork de método, labels e prosa passam pelo Gui. Nunca publique sozinho.
- **Citable > derived.** Plote números reportados, não interpolados/computados. Largue a série problemática em vez de fudge.
- **Todas as ressalvas no caption**, nunca na prosa nem no título.
- **Render via browser-tools (`render.sh`), não headless.** Brave headless trava no setup de perfil.
- **Não duplique a logo DJ** — referencie de `daily-journal-platform`.
- **Título factual, voz neutra, sem frase-moldura.** Os três erros que o Gui corrigiu — não os repita.
