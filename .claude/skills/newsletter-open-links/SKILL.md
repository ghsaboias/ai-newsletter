---
name: newsletter-open-links
description: >-
  Abre no navegador todos os links de um pt.md da newsletter. Extrai as URLs dos links markdown `[texto](url)`, dedupa preservando a ordem do documento, imprime a lista numerada e abre cada uma no Brave (macOS `open -a "Brave Browser"`). Por padrão atua no pt.md de hoje; aceita arg de path explícito, data (YYYY-MM-DD), ou a flag `lista` pra só listar sem abrir. Aciona quando o usuário diz "abrir os links", "abre todos os links do pt.md", "open all links", "/newsletter-open-links".
allowed-tools: Read, Bash
---

## Quando essa skill roda

Durante a revisão humana do `pt.md` — pra conferir as fontes de cada história abrindo todas de uma vez no navegador. Pode rodar a qualquer momento; não muda nenhum arquivo.

Só lê o arquivo e dispara o navegador. **Nenhuma escrita, nenhum efeito no repo.**

## Args

Invocada como `/newsletter-open-links [args]`. Parse do user message:

- (sem args) — atua no `pt.md` de hoje
- Path absoluto `/Users/.../alguma-pasta/arquivo.md` — atua nesse arquivo
- `YYYY-MM-DD` — atua no `pt.md` daquela data
- `lista` (sozinho ou junto com data/path) — **só lista** as URLs, não abre

## Step 0: Estabelecer a data (se necessário)

Se não veio arg de path nem data, rode `date '+%Y-%m-%d'` pra montar o path default:

```
TARGET = /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/pt.md
```

Se veio path explícito, use ele direto. Se veio data, monte o path equivalente.

## Step 1: Validar o arquivo

```bash
test -f "$TARGET" || echo "ERRO: arquivo não existe: $TARGET"
```

Se não existe, **não invente** — liste as datas disponíveis e peça pro usuário escolher:

```bash
ls -1 /Users/guilherme/ai-newsletter/pipeline/output/ai/ | tail -10
```

E pare.

## Step 2: Extrair, dedupar e listar

URLs só aparecem em links markdown inline `[texto](url)` no pt.md (sem reference-style, sem bare URLs). Extraia o miolo do `](...)`, dedupe preservando a ordem do documento:

```bash
grep -oE '\]\(https?://[^)]+\)' "$TARGET" \
  | sed -E 's/^\]\(//; s/\)$//' \
  | awk '!seen[$0]++' > /tmp/nl-links.txt
COUNT=$(wc -l < /tmp/nl-links.txt | tr -d ' ')
echo "Links únicos: $COUNT"
cat -n /tmp/nl-links.txt
```

Imprima a lista numerada pro usuário ver o que vai abrir. **Sempre liste antes de abrir** — transparência.

Se `COUNT == 0` → printa "Nenhum link encontrado." e para.

## Step 3: Abrir no navegador

Se o arg `lista` foi passado, **pule este step** — só a listagem do Step 2 basta.

Senão, abra cada URL no Brave. Um `open` por URL (mais confiável que passar tudo de uma vez):

```bash
while IFS= read -r url; do open -a "Brave Browser" "$url"; done < /tmp/nl-links.txt
echo "Abertas $COUNT abas no Brave."
```

`open -a "Brave Browser"` força o Brave mesmo que ele não seja o navegador padrão do sistema. Pra usar o navegador padrão, troque por `open "$url"`.

## Step 4: Report

Tight, sem narração de passos intermediários:

- Path do arquivo lido
- Quantos links únicos foram abertos (ou listados, no modo `lista`)

## Regras de comportamento

- **Read-only.** Essa skill nunca escreve nem edita nada. Só lê o pt.md e dispara o Brave.
- **Brave é o navegador alvo.** Sempre `open -a "Brave Browser"`, independente do navegador padrão do sistema.
- **Sempre liste antes de abrir.** O usuário vê a lista numerada antes de 20+ abas aparecerem.
- **Dedupe preservando ordem.** URLs repetidas abrem uma vez só, na ordem em que aparecem no documento.
- **Não invente path.** Se o arquivo não existe, liste as datas disponíveis e pare.
- **`lista` = só listar.** Nesse modo, nunca chame `open`.
- **Sem sleep entre os `open`.** Loop simples; o navegador agrupa as abas sozinho.
