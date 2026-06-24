Sua tarefa: gerar o bloco teaser que vem antes do paywall da newsletter **no formato v2** e salvar os metadados para injeção automática no Substack.

## Contexto do formato v2

O artigo em {{V2_FILE}} tem três níveis:

```
# título
subtítulo
Por: ...                     ← byline
### Manchete da Grande 1
- **Rótulo.** ...            (bullets)
### Manchete da Grande 2
### Manchete da Grande 3
---                          ← O CORTE DO PAYWALL É AQUI (depois das grandes)
#### Cluster temático        (médias)
- **Entidade.** frase densa.
#### outro cluster
---
#### Leia também             (callout)
- [manchete que vira link](url)
```

**As 3 grandes ficam livres (acima do paywall). Tudo depois do primeiro `---` é pago:** todos os bullets das médias (cada `**Entidade.**` é uma história) e todos os itens de "Leia também" (cada manchete é uma história).

O corte é estrutural (sempre depois das grandes), então **você não escolhe o corte** — só gera os teasers das histórias pagas.

## Inputs

1. Leia {{V2_FILE}}.
2. Leia o exemplo de referência em {{EXAMPLE}} para calibrar voz e formato.

## O que fazer

Gere **um teaser por história paga** — uma linha para cada bullet de média e uma linha para cada item de "Leia também". Mantenha a ordem em que aparecem no documento.

## Formato dos teasers

```
Abaixo, apenas para assinantes:

**Categoria.** Frase única, factual e vaga.
**Categoria.** Frase única, factual e vaga.
...
```

## Regras de voz (obrigatórias)

1. **Curta e declarativa.** Sujeito + verbo no presente + complemento mínimo. Sem gancho relativo ("que ancora", "que pode").
   - ❌ "O contrato bilionário da Hut 8 que ancora um novo campus de IA."
   - ✅ "Hut 8 fecha contrato bilionário para um campus de IA no Texas."
2. **Factual.** Sem "por que", "à beira de", "pode ser que". Sem editorialização.
3. **Vaga.** Cortar números, percentuais, datas específicas. Nomes próprios (empresa, país) são permitidos.
4. **Sem em-dashes.** Use vírgulas, dois pontos, ponto.
5. **Frase única.** Pode juntar dois fatos próximos com "e" se a frase ficar curta.
6. Categorias: `**Data centers.**`, `**Energia.**`, `**Geopolítica.**`, `**Defesa.**`, `**Macro.**`, `**Capital.**`, `**Biotech.**`, `**Big techs.**`, `**Regulação.**`, `**Clima.**`, `**Robótica.**`, `**Modelos.**`, `**Agentes.**`, `**Hardware.**`, `**IPO.**`, `**Eleições.**`, ou outro rótulo específico.

## Saídas a gravar

**Arquivo 1 — {{OUTPUT_MD}}** (markdown, para inspeção):
Escreva o bloco teaser completo, formato exato acima (com o cabeçalho "Abaixo, apenas para assinantes:").

**Arquivo 2 — {{OUTPUT_META}}** (JSON, para injeção automática):
```json
{
  "cut_after": null,
  "teasers": [
    "**Categoria.** Frase.",
    "**Categoria.** Frase."
  ]
}
```

`cut_after` é `null` — o corte é estrutural (a injeção usa `--paywall-after-grandes`). `teasers` é a lista de linhas sem o cabeçalho.

## Processo

1. Leia {{V2_FILE}} e {{EXAMPLE}}.
2. Liste, na ordem, cada bullet de média e cada item de "Leia também" (essas são as histórias pagas).
3. Redija um teaser por história.
4. Releia: cada teaser é curto, declarativo, sem números, sem em-dash, frase única?
5. Grave {{OUTPUT_MD}} e {{OUTPUT_META}}.
