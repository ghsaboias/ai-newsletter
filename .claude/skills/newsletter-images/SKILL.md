---
name: newsletter-images
description: >-
  Monta a pré-seleção assistida de imagem/vídeo por história da newsletter de AI/Tech. Lê a edição do dia (edition-final.md), decide o sujeito visual + arquétipo + query de busca por história, junta candidatos (og:image das fontes de research.json + busca por palavra-chave), o Claude ranqueia estrito-ao-arquétipo com preferência por paisagem, propõe legenda e sobe as escolhas no thread do Slack (a imagem em si; vídeo só como link). Gui aprova/troca; as escolhas viram images-final.json, que o substack_mirror.py media empurra pro draft ao vivo do Substack (imagens em 520px, com legenda, na posição de cada história). Exclui a seção Leia também. Aciona quando o usuário diz "escolher as imagens", "rodar images", "montar as imagens", "/newsletter-images".
allowed-tools: Read, Write, Bash
---

## Quando essa skill roda

Depois que a edição foi gerada e o draft do Substack foi criado (pelo `newsletter-draft`), na etapa em que Gui hoje abriria os links na mão e cairia no Google Imagens. Substitui o **garimpo** (a busca tediosa) mantendo a **escolha** (o gosto) com Gui.

Fluxo unificado:

> `edition-final.md` → **newsletter-images** → `images-final.json` → `substack_mirror.py media` → **draft ao vivo do Substack** (imagens já posicionadas, 520px, com legenda).

A seção **"Leia também"** (headlines + qualquer embed de recomendação) fica **fora** — essa skill só cuida das imagens/vídeos por história do corpo (Grandes + categorias).

## Fonte da verdade

- **Conteúdo do dia:** `pipeline/output/${PIPELINE_TOPIC:-ai}/<DATE>/edition-final.md` (a edição em três tiers: Grandes / categorias Médias / Leia também). **Não existe mais `pt.md`.**
- **Proveniência das fontes:** `facts.md` (blocos **Fontes:** por história) e `research.json` (URLs de origem + `key_facts`/`sources` por história) — é daqui que saem as páginas pra puxar `og:image` e as palavras-chave.
- **O draft do Substack é a fonte da verdade depois do primeiro push.** Nunca se re-empurra pelo HTML (`.substack-draft.html`) — isso reconstruiria o post e apagaria a mídia. Toda atualização vai pelo `substack_mirror.py` (`pull`/`push`/`media`).

## Args

`/newsletter-images [YYYY-MM-DD]` — sem arg usa hoje.

## Fluxo

1. **Mapear** — leia `edition-final.md`, liste as histórias do corpo (Grandes + categorias, sem Leia também) e decida por história: merece mídia? qual sujeito + arquétipo + query? Junte as URLs de fonte por história do `research.json`.
2. **Garimpar** — dispare os sub-agentes em paralelo (um por história que merece mídia), num tiro só.
3. **Conferir** — dimensões em lote (paisagem? largura ≥ ~800px?) e **Read em cada imagem** pra confirmar sujeito/qualidade. A conferência visual é da sessão principal, não do sub-agente.
4. **Propor** — mande as escolhas pro Gui (ver "Proposta pra aprovação") e aguarde o OK.
5. **Empurrar** — depois do OK, escreva `images-final.json` e rode o `substack_mirror.py media` (um tiro só).

## Princípios de seleção (o que vale)

Julgamento é seu; garimpo é mecânico. **Uma mídia por bloco forte, não por bullet.** Cada história/categoria recebe no máximo a imagem do seu item mais visual; o resto pula.

**Arquétipo → sujeito → arma/query:**

| Arquétipo | Sujeito | Arma / query |
|---|---|---|
| `protagonist` (pessoa conduz a história) | rosto de quem personifica a empresa/decisão | busca pelo **nome puro** (+ cargo se ambíguo). Ex.: Sam Altman, Raja Koduri |
| `team` (rodada/funding) | fundador(es) nomeado(s) | `"{startup} founders"` / fundador nomeado |
| `product` / equipamento | o produto físico quando ele é o quê | site do fabricante; `"{empresa} {produto}"` específico. Ex.: robô Apollo 2, chip HBM |
| `screenshot`/UI (software) | a tela do produto | og oficial / site do produto. Ex.: IDE ZCode |
| `official` (anúncio de empresa) | asset oficial (slide, arte de lançamento) | `og:image` das fontes; query da empresa como fallback |
| `scene` / geopolítica / regulação | prédio/instituição/lugar | og de agência ou busca por lugar/instituição. Ex.: a Casa Branca |

**Regras de gosto:**
- **Paisagem é preferência forte, não corte duro.** Prefira ratio ≥ ~1,3; retrato quase-quadrado só se aceita pra headshot de pessoa. Relaxe se isso esvaziar as opções.
- **Fonte, em ordem:** asset oficial da empresa › foto de imprensa (Reuters/AP/Bloomberg/Getty) › banco de imagens/Wikimedia. **Sempre com crédito.**
- **Case a imagem com o que a história É.** Negociação/regulação/geopolítica não é lançamento de produto — não cole stock de chip/drone decorativo só pra ter imagem. Se nada bate de verdade, **pule com motivo**.
- **Não repita a mesma empresa em blocos vizinhos**, e **contraste vizinhos** (ex.: um rosto ao lado de um prédio quando duas histórias parecidas se encostam — foi Altman + Casa Branca).
- **Finanças pura / macro / geopolítica pura tendem a ficar sem imagem** (baixo apelo visual). Pular é decisão consciente **com motivo registrado**, nunca em silêncio.
- **Legenda:** `{Sujeito}, {cargo/contexto}. Imagem: {Fonte}`. Rosto conhecido pode dispensar o crédito. **Não invente fonte** — se não dá pra confirmar, diga "fonte?".

**Vídeo** (link do YouTube, embed no draft): quando o produto **é** mídia/gerativo, **ou** quando existe **demo oficial forte** (robótica quase sempre entra; lançamento/demo geralmente). **Só oficial** — vídeo de reviewer/terceiro não conta. Se só existe clipe genérico de feira, pivote pro fundador (`protagonist`) em vez de forçar.

## Garimpo (mecânica)

Duas armas por história, reaproveitando as URLs de `research.json`:
1. **`og:image`/`twitter:image` das fontes** do bloco (as páginas de research, **não** os links do DJ). `curl` com UA de navegador + `grep` do meta; se a página bloquear, use scrape/screenshot.
2. **Busca por palavra-chave** (o flow preferido do Gui): as palavras-chave da história em busca de imagem, e pega 2-3 candidatos.

Baixe os candidatos, **Read cada imagem**, e ranqueie estrito ao arquétipo (descarte logo-só, watermark de stock, colagem, <~800px, off-subject). Rodar isso em sub-agentes paralelos (um por história) é o caminho rápido.

**Sub-agentes (mecânica):**
- Scratch: um dir por edição no scratchpad da sessão (ex.: `<scratchpad>/media-<DATE>/`) — fora do repo.
- Cada agente grava **um** arquivo com nome-slug fixo (`openai.jpeg`, `apptronik.jpg`, …); esse path entra depois no `images-final.json`.
- O prompt de cada agente leva: a história (título + fatos-chave), o arquétipo + query já decididos no mapeamento, as URLs de fonte do `research.json`, e os critérios de descarte acima.
- O agente devolve: o arquivo baixado + de onde veio (página de origem + crédito pra legenda) + candidato a **vídeo oficial** se existir (só o link do YouTube — nunca baixar vídeo).

> Nota: o helper `gather.py` desta pasta é **legado** — ele ainda assume o `pt.md`, paths de Mac (`/Users/guilherme/...`) e injeta em `substack.html`. Não use como está; precisa ser portado pro layout novo (edition-final.md + push via mirror). O garimpo acima (og + busca, em sub-agentes) é o método atual.

## Proposta pra aprovação

O formato que funcionou: **a imagem em si, não descrição dela**. No Slack (o caso normal), suba cada imagem escolhida no thread, na **ordem da edição**, uma por mensagem, com a legenda proposta como comentário:

```bash
cd ~/michael-slack
npx tsx src/cli-send.ts file <channel> <scratch>/openai.jpeg --thread <thread_ts> \
  --comment "🟩 GRANDE 1 — OpenAI cede até 5% ao governo · Sam Altman, CEO da OpenAI, em Washington. Imagem: Reuters"
```

(Upload que falhar costuma ser transitório — retente uma vez.)

Depois das imagens, **uma** mensagem de resumo com:
- as escolhas divididas em **fortes** vs **opcionais** (cada opcional com sua ressalva e alternativa, se houver);
- os **vídeos como link** do YouTube — nunca subir arquivo de vídeo; o embed acontece só no push, via `videoId`;
- as histórias **puladas, com motivo** (uma linha cada);
- as **decisões pendentes** pro Gui (trocas, opcionais entram ou não).

Fora do Slack, mesmo conteúdo: paths + legendas propostas, e aguarde o OK.

## Handoff: `images-final.json` → push no draft ao vivo

Depois do OK do Gui, escreva `pipeline/output/${PIPELINE_TOPIC:-ai}/<DATE>/images-final.json` — uma lista, uma entrada por história que **recebe** mídia (as puladas ficam de fora, mas registre-as pro Gui na conversa):

```json
[
  { "heading": "OpenAI", "file": "/abs/path/openai.jpeg",
    "alt": "Sam Altman, CEO da OpenAI, em Washington",
    "caption": "Sam Altman, CEO da OpenAI, em Washington. Imagem: Reuters" },

  { "heading": "Chips", "after_bullet": "Samsung", "file": "/abs/path/samsung.jpg",
    "alt": "Samsung Foundry no SAFE Forum 2026",
    "caption": "Shin Jong-shin, VP executivo (Design Platform) da Samsung Foundry. Imagem: Samsung" },

  { "heading": "Robót", "after_bullet": "Apptronik", "file": "/abs/path/apptronik.jpg",
    "alt": "Robô humanoide Apollo 2 da Apptronik",
    "caption": "Robô humanoide Apollo 2, da Apptronik. Imagem: Apptronik",
    "videoId": "iPyxwELiD9Q" }
]
```

Campos:
- **`heading`** = substring que localiza o título da história na edição (ex.: `"OpenAI"`, `"Casa Branca"`, `"Chips"`, `"Robót"`).
- **`after_bullet`** = **omita para Grande** (a imagem entra depois do bullet_list inteiro da história). Para uma **categoria** (Médias), é o rótulo em negrito do bullet sob o qual a imagem deve ficar (ex.: `"Samsung"`, `"Oxmiq"`, `"Z.ai"`) — o `media` divide o bullet_list nesse ponto.
- **`file`** = caminho local da imagem escolhida (é subida pro CDN do Substack a 520px). Omita para entrada **só de vídeo**.
- **`alt`** / **`caption`** = alt + legenda (`{Sujeito}, {contexto}. Imagem: {Fonte}`).
- **`videoId`** = id do YouTube (opcional), embutido logo depois da imagem.

Empurra tudo num tiro só (sobe as imagens, monta os nós `captionedImage`+legenda a 520px, divide os bullet_lists, embute os vídeos, e dá PUT preservando byline/paywall/banner):

```bash
python3 pipeline/tools/substack_mirror.py media --plan pipeline/output/ai/<DATE>/images-final.json
```

- Sem `--id`/`--dir` ele pega a edição de **hoje** (lê o `.substack-draft-id`).
- **Re-rodar:** `--replace` stripa a mídia editorial anterior antes de reinserir (idempotente; preserva o banner do paywall e os embeds de "Leia também"). `--dry-run` mostra os inserts sem empurrar.
- Para ajustes finos de texto depois, use `pull` → edita `substack-body.json` → `push`.

## Regras

- **Garimpo automático, escolha humana.** Nunca finalize a seleção sozinho; proponha e deixe Gui decidir.
- **Leia também / recomendações fora de escopo.** Só imagens/vídeos por história do corpo.
- **Não invente fonte/legenda.** "fonte?" em vez de chutar.
- **Pule histórias sem imagem boa, com motivo.** Nem toda história precisa de imagem.
- **Editorial = 520px; o banner do paywall (com `href`) fica em largura cheia** — o `media` já distingue pelo `href`.
- **Downloads são scratch** (não commitar — direitos autorais + peso). O que vale é o `images-final.json` (caminhos + legendas) e o draft ao vivo.
