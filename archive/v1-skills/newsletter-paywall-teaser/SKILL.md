---
name: newsletter-paywall-teaser
description: >-
  Gera o bloco "Abaixo, apenas para assinantes:" que vem antes do paywall — uma frase teaser curta e declarativa por história, factual e vaga (sem números/datas específicos), no formato `**Categoria.** Frase curta no presente.`. Lê o pt.md, identifica onde o usuário pôs o corte (âncora textual de um parágrafo) e gera teasers para as histórias dos parágrafos posteriores. Aciona quando o usuário diz "gera o teaser do paywall", "cria o bloco antes da paywall", "/newsletter-paywall-teaser".
allowed-tools: Read, Write, Bash, Agent
---

## Quando essa skill roda

Depois do `pt.md` finalizado (idealmente pós-rewrite), antes de publicar no Substack. O teaser fica entre o último parágrafo público e a paywall.

Saídas:
- `pipeline/output/ai/<DATE>/paywall-teaser.md` — markdown (fonte)
- `pipeline/output/ai/<DATE>/paywall-teaser.html` — HTML pronto pra colar no editor `</>` do Substack

O Substack não interpreta markdown cru, então o HTML é o que vai colado.

## Args

Invocada como `/newsletter-paywall-teaser <âncora> [data]`. Parse do user message:

- **`<âncora>`** (obrigatório) — texto curto que aparece num parágrafo do pt.md, identificando o **último parágrafo público**. Ex: `"Corning"`, `"Hut 8"`, `"Big techs"`. O teaser será para os parágrafos **depois** desse.
- `[data]` opcional (YYYY-MM-DD) — default hoje.

Se a âncora não veio, **pare e pergunte** ao usuário antes de prosseguir. Não invente.

## Step 0: Estabelecer a data

Rode `date '+%Y-%m-%d'` se não veio data explícita.

## Step 1: Paths e idempotência

```
ROOT       = /Users/guilherme/ai-newsletter
DAY_DIR    = $ROOT/pipeline/output/ai/$DATE
PT_FILE    = $DAY_DIR/pt.md
OUTPUT_MD  = $DAY_DIR/paywall-teaser.md
OUTPUT_HTML= $DAY_DIR/paywall-teaser.html
EXAMPLE    = $ROOT/pipeline/output/ai/2026-05-29/paywall-teaser.md  # referência de estilo (curto/declarativo)
```

Checks:
- **`$OUTPUT_MD` já existe** → printa o conteúdo do `.md` e do `.html` (se existir; senão gera o HTML do md atual) e para. Pra regenerar do zero: deletar o `.md` (e o `.html` se quiser garantir reconversão).
- **`$PT_FILE` não existe** → erro.

## Step 2: Validar âncora

```bash
grep -c "<âncora>" "$PT_FILE"
```

- **0 matches** → erro: "âncora '<âncora>' não encontrada em pt.md".
- **>1 matches** → aviso ao usuário, mostra contexto de cada match, e pede pra refinar a âncora (a primeira ocorrência por padrão pode não ser o que ele quer).

## Step 3: Dispatch do sub-agente

Um Agent só. Sub-agente lê o pt.md, identifica o parágrafo da âncora, e gera teasers para o que vem depois.

```
Agent({
  description: "Generate paywall teaser block for <DATE>",
  subagent_type: "general-purpose",
  prompt: "<conteúdo do prompt abaixo, com <PT_FILE>, <ANCHOR>, <OUTPUT>, <EXAMPLE> substituídos>"
})
```

**Prompt do sub-agente:**

```
Sua tarefa: gerar o bloco teaser que vem antes do paywall da newsletter. Salvar em <OUTPUT_MD>.

INPUTS

1. Leia o draft em <PT_FILE>.
2. Encontre o parágrafo que contém a âncora "<ANCHOR>". Esse é o ÚLTIMO parágrafo público — leitores não-assinantes leem até aqui.
3. Os parágrafos DEPOIS dele são paywalled. Vai gerar teasers para as histórias desses parágrafos.
4. Leia também o exemplo de referência em <EXAMPLE> pra calibrar voz e formato.

FORMATO DE SAÍDA

Estrutura:

    Abaixo, apenas para assinantes:

    **Categoria.** Frase única, factual e vaga.

    **Categoria.** Frase única, factual e vaga.

    ...

Granularidade: **uma linha por história**, não por parágrafo. Se um parágrafo tem 2-3 histórias, gere 2-3 teasers (cada um com sua categoria apropriada). Se um parágrafo tem 1 história, 1 teaser.

REGRAS DE VOZ

1. **Curta e declarativa.** Uma afirmação direta no presente: sujeito + verbo + complemento mínimo. Não use construções com gancho relativo ("que ancora", "que pode", "O contrato bilionário que..."). Diga o fato, seco.
   - ❌ "O contrato bilionário da Hut 8 que ancora um novo campus de IA no Texas."
   - ✅ "Hut 8 fecha contrato bilionário para um campus de IA no Texas."
   - ✅ "ByteDance investe em chips próprios."
   - ✅ "Wix faz o maior corte de sua história e cita a IA."
2. **Factual.** Sem "por que", "à beira de", "acha que", "pode ser que". Sem editorialização.
3. **Vaga.** Cortar números, percentuais, datas específicas. Nomes próprios (empresa, país, órgão) são permitidos e ajudam.
   - ❌ "A Wix vai demitir 1.000 funcionários, 20% do quadro."
   - ✅ "Wix faz o maior corte de sua história e cita a IA."
4. **Sem em-dashes.** Use vírgulas, dois pontos, ponto.
5. **Frase única.** Não duas. Não três. Pode juntar dois fatos próximos com "e" se a frase seguir curta ("Ataques americanos ao Irã e ameaça de Trump a Omã.").
6. **Categoria emerge da história.** Use rótulos como `**Data centers.**`, `**Energia.**`, `**Geopolítica.**`, `**Defesa.**`, `**Macro.**`, `**Capital.**`, `**Biotech.**`, `**Big techs.**`, `**Regulação.**`, `**Clima.**`. O mesmo rótulo do parágrafo do pt.md pode servir, ou um mais específico se o parágrafo tinha histórias mistas.
7. **Sem gancho de curiosidade artificial.** Não construa suspense ("a primeira a vencer", "o que veio junto"). A própria notícia, dita de forma curta e concreta, é o gancho.

PROCESSO

1. Leia pt.md inteiro e <EXAMPLE>.
2. Localize o parágrafo da âncora; mentalmente marque tudo depois dele.
3. Para cada história nos parágrafos paywalled:
   - Identifique o sujeito principal (empresa/governo/pessoa)
   - Reduza a ação a um verbo no presente + complemento mínimo
   - Escolha categoria
   - Escreva uma frase curta e declarativa
4. Releia: cada teaser fica curto + declarativo no presente? Sem gancho relativo ("que ...")? Sem números específicos? Sem em-dashes? Frase única?
5. Escreva <OUTPUT_MD> com o bloco completo.

SAÍDA

Quando terminar, reporte:
- Quantos teasers gerou
- Quais parágrafos foram cobertos (label + breve)
```

## Step 4: Validar o markdown

```bash
test -f "$OUTPUT_MD" || echo "ERRO: paywall-teaser.md missing"
DASH_COUNT=$(grep -o '—' "$OUTPUT_MD" | wc -l | tr -d ' ')
[[ $DASH_COUNT -gt 0 ]] && echo "AVISO: $DASH_COUNT em-dashes no teaser (regra de voz violada)"
ITEM_COUNT=$(grep -c '^\*\*' "$OUTPUT_MD")
echo "Items: $ITEM_COUNT"
```

## Step 5: Converter pra HTML (pandoc)

Substack renderiza `**` literalmente. Converter pra HTML antes de mandar:

```bash
pandoc "$OUTPUT_MD" --from markdown-tex_math_dollars --to html -o "$OUTPUT_HTML"
test -f "$OUTPUT_HTML" || echo "ERRO: paywall-teaser.html missing — pandoc falhou"
```

Mesma flag usada pelo antigo `pipeline/substack.sh` (`--from markdown-tex_math_dollars --to html`), pra garantir consistência caso o resto da newsletter também passe por pandoc.

Se pandoc não estiver instalado, reportar erro claro: `brew install pandoc`.

## Step 6: Report

Printa:
- Path dos dois arquivos (`.md` fonte, `.html` pra colar)
- Quantidade de itens
- Aviso se sobrou em-dash (regra de voz quebrada)
- Conteúdo do `.md` (pra inspeção rápida sem precisar abrir)
- Lembrete: colar o **HTML** no editor `</>` do Substack, não o markdown

```bash
cat "$OUTPUT_MD"
```

## Regras de comportamento

- **Âncora é obrigatória** — sem âncora, peça ao usuário. Não chute o ponto de corte.
- **Idempotência**: se `paywall-teaser.md` existe, mostra e para. Re-run completo = deletar o `.md`. Se só o `.html` está faltando (md já existe), reconverter direto via pandoc sem chamar o sub-agente.
- **Sempre gerar HTML.** O Substack come HTML, não markdown. Sem o `.html` a skill não terminou.
- **Sem em-dashes** no output. Se aparecer, é falha — reporte.
- **Não toque no pt.md.** Skill é puramente generativa, escreve só os dois arquivos do teaser.
- **Voz curta + declarativa + factual é o contrato.** Se o sub-agente vazar números específicos, gancho relativo ("que ...") ou editorialização, o resultado falhou — usuário pode invocar `/newsletter-paywall-teaser` de novo (após deletar) ou editar à mão.

## Referência de estilo

`pipeline/output/ai/2026-05-29/paywall-teaser.md` é o exemplo calibrado da voz curta e declarativa (frases no presente, sujeito + ação, sem gancho relativo). O sub-agente DEVE ler esse arquivo antes de gerar o novo. O de `2026-05-07` usa a voz antiga (gancho de curiosidade) e **não** deve ser seguido. Quando o corpus crescer, considere apontar pra um curated set de exemplos no estilo novo.
