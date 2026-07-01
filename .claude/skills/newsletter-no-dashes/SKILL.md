---
name: newsletter-no-dashes
description: >-
  Remove todos os em-dashes (—, U+2014) de um arquivo PT-BR mantendo o texto fluido e gramaticalmente correto. Forced removal — nenhum em-dash sobrevive; sub-agente reestrutura a frase quando a substituição mecânica ficaria ambígua. Por padrão atua no pt.md de hoje; aceita arg de path explícito. Aciona quando o usuário diz "tirar em-dashes", "limpar dashes", "remover travessões", "/newsletter-no-dashes".
allowed-tools: Read, Write, Edit, Bash, Agent
---

## Quando essa skill roda

Limpeza editorial de em-dashes — pode rodar a qualquer momento, mas o uso típico é **depois de `newsletter-rewrite`**, antes da revisão humana / finalize.

Apenas U+2014 (—) é alvo. **Hífens (-) e en-dashes (–) NÃO são tocados.**

## Args

Invocada como `/newsletter-no-dashes [args]`. Parse:

- (sem args) — atua no `pt.md` de hoje
- Path absoluto `/Users/.../alguma-pasta/arquivo.md` — atua nesse arquivo
- `YYYY-MM-DD` — atua no `pt.md` daquela data

## Step 0: Estabelecer a data (se necessário)

Se não veio arg de path, rode `date '+%Y-%m-%d'` pra montar o path default:

```
TARGET = /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/pt.md
```

Se veio path explícito, use ele direto.

Se veio data, monte o path equivalente.

## Step 1: Validar e contar

**Importante:** use `grep -o … | wc -l` pra contar **ocorrências**, não linhas. `grep -c` conta linhas, e uma linha pode ter múltiplos em-dashes — subcount.

```bash
test -f "$TARGET" || echo "ERRO: arquivo não existe: $TARGET"
DASH_COUNT=$(grep -o '—' "$TARGET" 2>/dev/null | wc -l | tr -d ' ')
echo "Em-dashes encontrados: $DASH_COUNT"
```

Se `DASH_COUNT == 0` → printa "Nada a limpar." e para. Idempotência natural.

## Step 2: Dispatch do sub-agente

Um Agent só. Sub-agente edita o arquivo em-place.

```
Agent({
  description: "Remove em-dashes de <basename($TARGET)>",
  subagent_type: "general-purpose",
  prompt: "<conteúdo do bloco abaixo, com <TARGET> substituído>"
})
```

**Prompt do sub-agente:**

```
Sua tarefa: remover TODOS os em-dashes (—, U+2014) do arquivo <TARGET>, mantendo o texto fluido e gramaticalmente correto em português brasileiro. O significado original deve ser preservado.

REGRAS

1. **Forced removal**: nenhum em-dash pode sobreviver. Conte antes e depois — depois precisa ser zero.
2. **Apenas U+2014 (—)** é alvo. NÃO toque em hífens (-) nem en-dashes (–).
3. **Frontmatter intocado**: preserve o bloco YAML do topo verbatim.
4. **Significado preservado**: nenhum fato, número, link ou nome muda.

ESTRATÉGIAS por contexto

- **Aposto explicativo** → vírgulas: "A empresa — americana — fez X" vira "A empresa, americana, fez X".
- **Introdução de explicação/lista** → dois pontos: "Resultado — ele venceu." vira "Resultado: ele venceu."
- **Mudança brusca de assunto** → ponto + nova frase.
- **Parêntese forte** → parênteses ou vírgulas, escolha o que flui melhor.
- **Quando substituição mecânica fica ambígua ou feia** → reestruture a frase: inverta ordem, mude conector, divida em duas. Prefira reestruturar a manter o em-dash.

PROCESSO

1. Leia <TARGET>.
2. Para cada em-dash, decida a estratégia. Edite com Edit (uma ocorrência por chamada quando faz sentido, ou batch quando o padrão é igual).
3. Releia depois pra confirmar que ficou natural.
4. Rode `grep -o '—' <TARGET> | wc -l` (conta ocorrências, não linhas) — se sobrou algum, volte e remova.

SAÍDA

Quando terminar, escreva um resumo curto:
- Em-dashes antes: N
- Em-dashes depois: 0
- Estratégias usadas: ex. "12 viraram vírgulas, 3 dois pontos, 2 reestruturados em duas frases"
```

## Step 3: Validar pós-edit

```bash
AFTER=$(grep -o '—' "$TARGET" | wc -l | tr -d ' ')
if [[ $AFTER -gt 0 ]]; then
  echo "AVISO: $AFTER em-dashes ainda presentes (sub-agente não terminou o trabalho)"
else
  echo "OK: 0 em-dashes restantes"
fi
```

Se sobrou em-dash, é falha do sub-agente — não tente "consertar" no orchestrator. Reporte ao usuário pra decidir (re-rodar ou inspecionar).

## Step 4: Report

Printa:
- Path do arquivo editado
- Contagem antes / depois
- Estratégias usadas (do summary do sub-agente)
- Comando pra diff: `git diff <TARGET>` (assumindo que tá em repo git)

Tight. Sem narração de passos intermediários.

## Regras de comportamento

- **Forced removal é o contrato.** 0 em-dashes no fim. Se o sub-agente devolver com em-dashes ainda presentes, é falha — reporte, não maquile.
- **Sem backup explícito.** O arquivo está em repo git; `git diff` e `git checkout` são o undo.
- **Não toque em hífens nem en-dashes.** Esses são caracteres diferentes (U+2010 e U+2013).
- **Idempotência natural.** Se já tem 0 em-dashes, no-op.
- **Não mude fatos.** Só pontuação e estrutura de frase. Nenhum número, nome, link ou data muda.
