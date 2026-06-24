---
name: newsletter-images
description: >-
  Monta a pré-seleção assistida de imagem/vídeo por história da newsletter de AI/Tech. Lê o pt.md, decide o sujeito visual + arquétipo + query de busca por história, junta candidatos via DuckDuckGo (busca de imagem), og:image das fontes e scrape de página (benchmarks), monta um contact sheet por história, e o Claude ranqueia estrito-ao-arquétipo com preferência por paisagem e propõe legenda. Gui aprova/troca; as escolhas viram images-final.json pro editor do Substack. Exclui a seção Recomendações. Aciona quando o usuário diz "escolher as imagens", "rodar images", "montar as imagens", "/newsletter-images".
allowed-tools: Read, Write, Bash
---

## Quando essa skill roda

Depois do `pt.md` revisado, antes/junto da finalização — a etapa em que Gui hoje abre todos os links na mão, olha cada aba e cai no Google Imagens. Substitui o **garimpo** (a busca tediosa) mantendo a **escolha** (o gosto) com Gui. A seção "Recomendações" (vídeos curados) fica **fora** — essa skill só cuida das imagens/vídeos por história do corpo.

`pt.md` → **newsletter-images** → `images-final.json` (entra no editor do Substack a mão; imagens não estão no `substack.html`).

## Args

`/newsletter-images [YYYY-MM-DD]` — sem arg usa hoje (`date '+%Y-%m-%d'`).

## Por que existe um gather.py

Garimpo de imagem é **mecânico** (buscar, baixar, montar); escolha de sujeito/query e o ranqueamento final são **julgamento**. Então: `gather.py` é puro mecanismo, e o Claude faz os dois julgamentos (autorar o plano, ranquear os sheets). Sem API key, sem navegador (browser-tools é gated por aprovação — não serve pra passo desacompanhado). Só `curl` + ImageMagick.

## Step 0: Data e validação

```bash
DATE=${ARG:-$(date '+%Y-%m-%d')}
BASE=/Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE
test -f "$BASE/pt.md" || { echo "sem pt.md em $BASE"; ls /Users/guilherme/ai-newsletter/pipeline/output/ai/ | tail -8; }
```
Sem `pt.md`, **não invente** — liste as datas e pare.

## Step 1: Segmentar (scaffolding)

```bash
python3 .claude/skills/newsletter-images/gather.py segment $DATE
```
Imprime cada parágrafo-bloco com label, texto, entidades (people/orgs/places) e categoria, juntando ao `research.json` por sobreposição de URL. **Leia também o `pt.md`** — a decisão de sujeito visual é sua, não das entidades (a primeira pessoa/org listada quase nunca é o sujeito da foto).

## Step 2: Autorar o plano (julgamento)

Decida história por história e escreva `/tmp/plan-$DATE.json` (lista) com as que **recebem imagem**:

```json
[{ "idx": 4, "label": "Política", "subject": "Abelardo de la Espriella",
   "archetype": "protagonist", "query": "Abelardo de la Espriella",
   "og_urls": ["https://..."], "video": false }]
```

### Pular ou não (a parte que erra fácil)

- **Pular é decisão consciente, com motivo.** Só o subtítulo e a continuação pura da mesma história (2º parágrafo que não abre tópico novo) somem de vez. Toda outra história que você **não** ilustrar entra no `picks.json` (Step 4) como `skip` **com `reason`** — vira a tira "Puladas" pro Gui reverter. Pular em silêncio = ponto cego.
- **Acordo/parceria ≠ sem sujeito.** Antes de pular um deal por "só logos", olhe as `people`: se tem principais nomeados (CEOs/fundadores), o aperto-de-mão/retrato deles é um `protagonist` limpo (ex.: Samsung×OpenAI → Lee Jae-yong + Sam Altman, foi o que publicamos). Não pule.
- **Case a imagem com o que a história É.** Negociação/regulação/geopolítica **não** é lançamento de produto — não cole um stock de drone/chip decorativo só pra ter imagem. Se o arquétipo honesto é `scene` ou pessoa, use isso; se nada bate de verdade, **pule com motivo** em vez de enfeitar.
- **Não repita a mesma empresa em parágrafos vizinhos.** Duas fotos da mesma marca coladas lêem repetitivo. Escolha a mais forte e pule a outra — "drone vs retrato da mesma Anduril" não é variedade.

**`og_urls`** = os links do bloco (o segment/parse já os tem; reaproveite). **Arquétipo → arma → query:**

| Arquétipo | Arma principal | Query |
|---|---|---|
| `protagonist` (pessoa conduz a história) | DuckDuckGo | **nome puro** (+ cargo se ambíguo). Nome+país enviesa pra cobertura de evento — evite |
| `team` (rodada/funding) | DuckDuckGo | `"{startup} founders"` / fundador nomeado |
| `official` (anúncio de empresa, Apple-style) | og das fontes | og costuma acertar; query de empresa como fallback |
| `benchmark` (lançamento de modelo) | DuckDuckGo + scrape do corpo da fonte oficial | `"{modelo} benchmark"` — o gráfico mora no corpo, **não** no og (og oficial costuma ser o card-logo) |
| `product`/equipment | DuckDuckGo + site do fabricante | `"{empresa} {coisa}"`; produto específico, não genérico |
| `scene`/geopolítica | og (artigo de agência) ou DuckDuckGo | lugar/instituição/evento |

`"video": true` quando a regra do Gui bate: **robótica → sempre; demo/lançamento → geralmente; clipe de notícia óbvio → às vezes** (ex.: renúncia de premiê). **Mas vídeo só vale se for específico.** Evento bem-coberto acha o clipe certo (Starmer). Empresa/robô pouco fotografado (ex.: Coowa) só acha vídeo genérico de feira — aí **a regra perde pro pivô**: vá no fundador nomeado (`protagonist`) em vez de forçar vídeo genérico. Regra de bolso: se você não reconheceria a empresa/robô numa busca, não é vídeo — é o fundador.

## Step 3: Executar

```bash
python3 .claude/skills/newsletter-images/gather.py plan /tmp/plan-$DATE.json $DATE
```
Gera `$BASE/images/sheet-NN-slug.png` (um por história, candidatos em ordem do manifesto) e `$BASE/images/candidates.json` (idx → arm/source/w/h/url/`page` por candidato + `videos`). `page` = URL do artigo de origem (pra linkar a thumb). ~1–1,5 min.

## Step 4: Ranquear e autorar picks.json (julgamento)

Leia o `candidates.json` (mapeia posição→fonte/dims; grade do sheet é **4 por linha, row-major**, posição = `#idx`) e **Read cada `sheet-*.png`**. Pra cada história, ordene os candidatos (melhor primeiro) por:

- **Estrito ao arquétipo.** Protagonista → retrato limpo da pessoa; descarte produto/evento/multidão. Benchmark → o gráfico, não o logo. Produto → o produto/fábrica.
- **Paisagem é preferência forte, não corte duro.** Prefira ratio ≥ ~1,3; se isso esvazia (retratos de gente pouco fotografada vêm retrato), relaxe e pegue o mais largo e limpo.
- **Descarte** logos/placeholders/marca-d'água ("gettyimages"/card de logo), thumbs com chyron/overlay pesado quando houver opção limpa, e off-subject.

Escreva `$BASE/images/picks.json` (lista, uma entrada por história):
```json
{ "idx":4, "label":"Política", "subject":"Abelardo de la Espriella",
  "archetype":"protagonist", "type":"image",
  "caption":"Abelardo de la Espriella. Imagem: Reuters",
  "ranked":[0,1,4,6],
  "videos_available": false,
  "shipped": {"url":"https://...","source":"Reuters"} }
```
- **`ranked`** = índices `#idx` dos candidatos, melhor primeiro. `ranked[0]` vira a ESCOLHA, `ranked[1]`/`ranked[2]` os alts, o resto vai pra tira "outros".
- **`type":"video"`** → adicione `"video": {"videoId":"...","title":"..."}` (do `videos` em candidates.json); a ESCOLHA passa a ser o vídeo e os alts viram `ranked[0]`/`ranked[1]` (stills).
- **`videos_available": true`** quando a história tem vídeo mas você escolheu imagem (marca um badge "vídeo disponível").
- **`caption`**: `{Sujeito}. Imagem: {Fonte}` — Fonte da marca-d'água ou domínio (agência: Reuters/AFP/AP/Getty/VCG; oficial: nome da empresa). Pessoa às vezes só o nome. **Não invente** — se não dá pra confirmar, ponha "fonte?".
- **`shipped`** (opcional, só em **backtest** de edição já publicada): pegue as imagens publicadas com `sstats post $DATE --html` (rode de `~/daily-journal-platform`), case cada `<figure>` à história pela legenda/sujeito, e preencha `{url, source}`. Numa run normal (edição nova, ainda não publicada) **omita** — a coluna vira "— não publicada —".
- **Histórias puladas** (Step 2) entram aqui como `{ "idx":8, "label":"Samsung × OpenAI", "skip":true, "reason":"..." }` — sem `ranked`. Viram a tira "Puladas" no fim da página, pro Gui reverter ("busca imagem pra #N"). **Sempre** registre o skip com motivo; nunca omita uma história em silêncio (menos subtítulo/continuação pura).

## Step 5: Montar e abrir a página de review

```bash
python3 .claude/skills/newsletter-images/gather.py review $BASE/images/picks.json $DATE
open "$BASE/images/images-review.html"
```
Gera **uma** página `images-review.html`: por história, uma linha com **PUBLICADA · ✓ ESCOLHA · alt 2 · alt 3** + tira "outros: #idx" com o resto dos candidatos. Verde = minha escolha, cinza = publicada. As miniaturas **renderizam da URL remota** (com `onerror` que cai pro download local se a fonte bloquear hotlink) e **cada uma linka pra URL do artigo** (`page`) — clicar abre a matéria, não o arquivo de imagem. Gui olha tudo de uma vez e diz, por história, **mantém / troca pro #N / pula**. **Ele dirige** — o gosto é dele (memória `image-video-automation` + princípios de review do CLAUDE.md).

## Step 6: Gravar as escolhas

Depois do OK, escreva `$BASE/images/images-final.json` (lista):
```json
{ "idx":4, "label":"Política", "subject":"Abelardo de la Espriella",
  "type":"image", "url":"https://...", "caption":"Abelardo de la Espriella. Imagem: Reuters",
  "source":"Reuters", "file":"/.../images/_c04_00.jpg",
  "anchor":"Na Colômbia, o advogado criminalista" }
```
`type:"video"` usa `"embed"` no lugar de `url`. **`file`** = o caminho local do candidato escolhido (já baixado em `candidates.json`) — pra arrastar direto pro editor sem rebaixar. **`anchor`** = início do texto puro do parágrafo da história (pro Step 7 achar onde inserir).

## Step 7: Injetar no substack.html (opcional)

```bash
python3 .claude/skills/newsletter-images/gather.py inject $BASE/images/images-final.json $DATE
```
Insere cada `<figure>` (img+legenda) / embed de vídeo logo depois do `<p>` da história em `substack.html`, gravando `$BASE/substack-images.html` (não-destrutivo; o pandoc `substack.html` fica intacto). O Substack re-hospeda imagens externas no paste (proxy `substackcdn.com/image/fetch/...`) e converte URLs do YouTube em embed — então colar o `substack-images.html` deve trazer as imagens já posicionadas. **Verifique com um paste real** antes de confiar nisso como padrão; se o Substack remover as externas, o fallback é subir os `file` locais a mão (mas a escolha + legenda já estão prontas).

## Regras

- **Garimpo automático, escolha humana.** Nunca finalize a seleção sozinho; proponha e deixe Gui decidir.
- **Recomendações fora de escopo.** Só imagens/vídeos por história do corpo.
- **Sem navegador, sem key.** Só `gather.py` (curl + ImageMagick). Se montage reclamar de Freetype/ghostscript, é só o `-label` (não usamos) — ignore.
- **Não invente fonte/legenda.** Se não dá pra confirmar a fonte, diga "fonte?" em vez de chutar.
- **`$BASE/images/` é scratch** (downloads `_c*` + sheets). Não commitar (direitos autorais + peso); o que vale é `images-final.json` (URLs + legendas).
- **Pule histórias sem imagem boa.** Nem toda história precisa de imagem; se nada bate o arquétipo, diga e siga.
