# Substack Format Inventory

Every formatting option the Substack post editor exposes, and how to produce each one through the publish API. Built by clicking through the live editor (publication `dailyjournalnews.substack.com`) and reading the resulting post body back from `GET /api/v1/drafts/<id>`.

## The one thing to know

The editor is a **TipTap / ProseMirror** instance. A post body is a **ProseMirror document** (`{"type":"doc","content":[ ...nodes ]}`), JSON-stringified into the `draft_body` field of the draft. Every visual format is either:

- a **block node** (`paragraph`, `heading`, `calloutBlock`, `paywall`, …), or
- an **inline mark** on a text node (`strong`, `em`, `link`, `strikethrough`, …).

So "how do I produce format X via the API" always reduces to "what node/mark does X map to, and what attrs does it carry". This file is that lookup table.

**Round-trip used to verify everything below:**
```
POST   https://<pub_host>/api/v1/drafts            # create draft (body = stringified PM doc)
GET    https://<pub_host>/api/v1/drafts/<id>       # read draft_body back to confirm node JSON
```
Auth: header `Cookie: substack.sid=<SID>`. Creds in `~/daily-journal-platform/.env.local` (`SUBSTACK_SID`, `SUBSTACK_PUB_HOST`). The pipeline already drives this in `pipeline/tools/substack_post.py` (HTML→ProseMirror converter) and `substack_upload.py` (image upload).

---

## 1. Toolbar map

Left → right in the editor toolbar:

`Estilo ▾` · **B** Bold · *I* Italic · ~~S~~ Strikethrough · `<>` Code · `T` text-color · `🖊` highlight · `A▾` super/subscript · 🔗 Link · 🖼 Image · 🎧 Audio · 🎥 Video · 💬 "Message Square Quote" (pull-quote, needs a text selection) · ☰ bullet list · ☰ numbered list · ☰▾ alignment · `Botão ▾` · `Modelo ▾` · `Mais ▾`

Plus, above the title: **Cabeçalho e rodapé de e-mail** (per-post email header/footer toggle), the **title**, **subtitle**, and **section/tag** chips.

---

## 2. Block-level formats

| UI (PT) | API node `type` | attrs | Newsletter fit |
|---|---|---|---|
| Texto normal | `paragraph` | `textAlign` | core |
| Título 1–6 (Estilo ▾) | `heading` | `level` 1–6 | **core** — section headers (H2–H4 read best in email) |
| Lista com marcadores | `bullet_list` › `list_item` › `paragraph` | — | core (already used in GENERATION.md) |
| Lista numerada | `ordered_list` › `list_item` › `paragraph` | `start, type, order` | core |
| Citação (pull-quote) | `blockquote` › `paragraph` | — | **core** — also the paywall teaser carrier |
| Bloco de destaque / callout | `calloutBlock` › `paragraph` | — | **core** — the gray teaser box (today's "Abaixo, apenas para assinantes") |
| Divisória | `horizontal_rule` | — | core — section breaks |
| Imagem (com legenda) | `captionedImage` › `image2` + `caption` | image2: `src, width, height, resizeWidth, alt, href, align, …` | core |
| Botão (CTA) | `button` | `url, text, action, class` | **core** — subscribe / share |
| Mural de Pagamento | `paywall` | — | **core** — the subscriber cut |
| Nota de rodapé | `footnoteAnchor` (inline) + `footnote` (block) | `number` | **useful** — source citations without inline link clutter |
| Enquete | `poll` | `id` (server-created entity) | optional — engagement |
| Bloco de código | `highlighted_code_block` | `language, nodeId` | rare |
| LaTeX | `latex_block` | `persistentExpression, id` | rare |
| Poesia | `preformatted_text_block` | `params, language` | rare — preserves whitespace |
| Gráfico financeiro | `captionedImage` (TradingView renders to a PNG) | — | rare — but note: it's just an image, so our own Chart.js PNGs are equivalent and on-brand |
| Mercado de previsões | server-backed embed (id reference, like `poll`) | — | n/a |
| Receita | structured recipe card (modal-configured) | — | n/a |
| Áudio / Vídeo | media upload / embed (`audio`, video upload, or oEmbed on URL paste) | — | rare |

### Key JSON shapes (verified)

```jsonc
// Heading
{"type":"heading","attrs":{"level":2},"content":[{"type":"text","text":"Seção"}]}

// Callout block (the teaser box)
{"type":"calloutBlock","content":[
  {"type":"paragraph","attrs":{"textAlign":null},"content":[
    {"type":"text","marks":[{"type":"strong"}],"text":"Manchete:"},
    {"type":"text","text":" resumo."}]}]}

// Blockquote (also paywall teaser)
{"type":"blockquote","content":[{"type":"paragraph","attrs":{"textAlign":null},"content":[
  {"type":"text","marks":[{"type":"strong"}],"text":"Abaixo, apenas para assinantes:"}]}]}

// Divider / Paywall (atoms, no attrs)
{"type":"horizontal_rule"}
{"type":"paywall"}

// Button (subscribe preset uses %%checkout_url%%; custom = real url + label)
{"type":"button","attrs":{"url":"%%checkout_url%%","text":"Assine agora","action":null,"class":null}}
{"type":"button","attrs":{"url":"https://dailyjournal.news","text":"Visite o site","action":null,"class":null}}

// Footnote: inline anchor in the text + a footnote block (Substack collects them at the end)
{"type":"text","text":"…afirmou a empresa"},{"type":"footnoteAnchor","attrs":{"number":1}}
{"type":"footnote","attrs":{"number":1},"content":[{"type":"paragraph","attrs":{"textAlign":null},
  "content":[{"type":"text","text":"Fonte: comunicado oficial, 23/jun."}]}]}

// Image with caption (image must be uploaded first via /api/v1/image → returns src)
{"type":"captionedImage","content":[
  {"type":"image2","attrs":{"src":"https://substack-post-media…png","width":1756,"height":1292,
    "resizeWidth":null,"alt":"…","href":null,"align":null}},
  {"type":"caption","content":[{"type":"text","text":"Legenda. "},
    {"type":"text","marks":[{"type":"link","attrs":{"href":"https://…","target":"_blank","rel":"noopener noreferrer nofollow","class":null}}],"text":"Fonte"}]}]}

// Poll references a server-created poll entity
{"type":"poll","attrs":{"id":639620}}

// Code / LaTeX / Poetry
{"type":"highlighted_code_block","attrs":{"language":"plaintext","nodeId":"<uuid>"},"content":[{"type":"text","text":"…"}]}
{"type":"latex_block","attrs":{"persistentExpression":"E = mc^2","id":"LQQRXZYPMM"}}
{"type":"preformatted_text_block","attrs":{"params":"","language":"en"},"content":[{"type":"text","text":"verso\nverso"}]}
```

---

## 3. Inline marks (text styling)

| UI (PT) | mark `type` | attrs | verified |
|---|---|---|---|
| Negrito | `strong` | — | ✅ |
| Itálico | `em` | — | ✅ |
| Link | `link` | `href, target, rel, class` | ✅ |
| Tachado | `strikethrough` | — | ✅ |
| Código (inline) | `code` | — | ✅ |
| Sobrescrito | `superscript` | — | ✅ |
| Subscrito | `subscript` | — | ✅ |
| Cor do texto | (text-color mark) | color | ⚠️ name not captured — picker needs a selection; couldn't automate. Full palette + 2 theme greens. Low value for a neutral news voice. |
| Destaque (highlight) | (highlight mark) | color | ⚠️ same as above |

```jsonc
{"type":"text","marks":[{"type":"strong"}],"text":"negrito"}
{"type":"text","marks":[{"type":"em"}],"text":"itálico"}
{"type":"text","marks":[{"type":"link","attrs":{"href":"https://dailyjournal.news","target":"_blank","rel":"noopener noreferrer nofollow","class":null}}],"text":"link"}
{"type":"text","marks":[{"type":"strikethrough"}],"text":"tachado"}
{"type":"text","marks":[{"type":"code"}],"text":"código"}
```
Marks compose: a text node can carry several (`[{"type":"strong"},{"type":"em"}]`).

---

## 4. Paragraph alignment

`Esquerda` · `Centralizar` · `À direita` · `Justificar` → carried on the block's `attrs.textAlign` (`null` | `"center"` | `"right"` | `"justify"`).

---

## 5. Button menu (`Botão ▾`) — all presets

Each inserts a `button` node; presets differ only by `url`/`action`:

Inscreva-se · Assinar com legenda · Compartilhar Post · Compartilhar post com legenda · Compartilhar publicação · Deixe um comentário · Enviar uma mensagem · Participe do chat · **Personalizado…** (free text + URL) · Obtenha o App · Indique um amigo · Indique um autor · Oferta especial · Ofereça uma assinatura de presente · Obtenha uma assinatura em grupo · Link para a pesquisa.

The subscribe-family presets use Substack template tokens in `url` (e.g. `%%checkout_url%%`); the rest point at publication routes.

---

## 6. `Mais ▾` special blocks (full list)

Bloco de código · Divisória · Gráfico financeiro · Nota de rodapé · LaTeX · Mural de Pagamento · Poesia · Enquete · Mercado de previsões · Receita. (Mapped in §2.)

---

## 7. Non-content editor features

- **Modelo ▾ (Templates):** save a reusable post skeleton ("O que é um modelo?" / "+ Novo modelo"). This is the native way to lock in a v2 layout so every edition starts pre-structured — worth using once the format is decided.
- **Cabeçalho e rodapé de e-mail:** per-post toggle for the email header/footer.
- **Title / Subtitle / Section tags:** `draft_title`, `draft_subtitle`, byline (`draft_bylines`), `draft_section_id`, `audience` (`everyone` | `only_paid` | `only_free`) — all set on the draft payload, not in the body.

---

## 8. Gaps / not captured authoritatively

- text-color & highlight mark names (picker requires a live text selection; automation couldn't form one). Low priority for the newsletter.
- video / audio / external oEmbed (tweet, YouTube) node shapes — available in the UI; produce by URL paste or upload. Capture if v2 wants embeds.
- recipe / prediction-market exact JSON (server/modal-backed; irrelevant to a news title).

## 9. Read for the newsletter redesign (task #2)

The realistic v2 palette, in rough priority: **headings** (break the wall of paragraphs), **callout blocks** (lead/teaser boxes), **bullet lists**, **dividers** between thematic sections, **pull-quotes** (`blockquote`), **footnotes** (sources without inline-link noise), **buttons** (CTA), plus the existing **paywall** + **captioned images/charts**. Everything else (latex, poetry, poll, recipe, financial-chart, code) is either niche or off-voice for a dense, neutral news brief.

Sandbox draft used for probing: `https://dailyjournalnews.substack.com/publish/post/203295452` (titled "ZZ — INVENTARIO DE FORMATOS"). Full captured PM doc: `scratchpad/sandbox_doc.json`.
