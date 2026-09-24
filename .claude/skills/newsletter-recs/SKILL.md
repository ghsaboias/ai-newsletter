---
name: newsletter-recs
description: >-
  Monta a seção "Recomendações de hoje" da newsletter de AI/Tech escolhendo automaticamente vídeos recentes e ainda não recomendados dos canais-fonte (Sequoia Capital, Invest Like The Best, a16z, Dwarkesh Patel, Peter H. Diamandis, David Senra, All-In Podcast) e empurrando a seção pro draft do Substack. Um helper busca no pool de vídeos do DJ (`video_articles`, auto-ingeridos) os 2 vídeos mais recentes de cada canal que ainda não entraram no arquivo `recommendations/RECOMMENDATIONS.md`; o modelo escolhe 2 favorecendo AUTORIDADE (figura importante da tech) e RECÊNCIA, apara o start-time pra pular a intro, usa a descrição do DJ (1º parágrafo do resumo) como legenda, e empurra a seção pro draft do Substack como nós ProseMirror (idempotente — troca a seção existente, não duplica). Aciona quando o usuário diz "montar as recomendações", "rodar as recs", "escolher os vídeos do dia", "/newsletter-recs". Aceita `YYYY-MM-DD` (default: hoje).
allowed-tools: Read, Bash, Write
---

## O que essa skill faz

Gera e empurra a seção **"Recomendações de hoje"** — os vídeos no fim da edição
(depois do paywall, depois do "Leia também"). Automatiza o que hoje é feito à mão no
editor do Substack: a *escolha* dos vídeos e a *injeção* da seção no draft.

Divisão de trabalho:
- **Determinístico** (`recommendations/gather-rec-candidates.py`): busca candidatos,
  dedup, extrai a descrição do DJ (1º parágrafo do resumo) e os capítulos.
- **Julgamento** (o modelo, nesta sessão): escolhe os 2 e apara o start-time.
- **Push** (`pipeline/tools/substack_recs.py`): monta os nós ProseMirror e atualiza o draft.

## Args

`/newsletter-recs [YYYY-MM-DD]`. Sem arg → hoje (`date '+%Y-%m-%d'`). A data rotula a
saída e localiza o draft do dia; a seleção não filtra por data (recência é preferência,
não corte).

## Step 0: Paths

Repo = três níveis acima do diretório-base desta skill. Saída do dia:

```
OUTDIR = <REPO>/pipeline/output/ai/<DATE>
```

Garanta que existe: `mkdir -p "$OUTDIR"` (normalmente já existe, criado pelo draft).

## Step 1: Sincronizar o arquivo de recomendações

Antes de buscar candidatos, atualize o `RECOMMENDATIONS.md` — sem isso o dedup roda
contra um arquivo até 24h defasado (o cron do meio-dia) e pode repetir a rec de ontem
se o draft rodar de manhã:

```bash
bash <REPO>/recommendations/sync-recommendations.sh
```

É o mesmo script do cron: upsert da janela recente de posts publicados + commit/push
só do arquivo (idempotente; sem edição nova não produz diff). Se falhar (rede, sstats),
**não pare**: siga com o arquivo local, avise o usuário, e aplique com rigor extra o
guard de já-usados do Step 3.

## Step 2: Buscar candidatos

```bash
python3 <REPO>/recommendations/gather-rec-candidates.py --date <DATE> > "$OUTDIR/rec-candidates.json"
```

Até 2 candidatos por canal (os mais recentes **fora** do `RECOMMENDATIONS.md`). Cada um:
`youtube_id`, `title`, `channel`, `published_at`, `url`, `view_count`, `chapters`,
**`description_pt`** (1º parágrafo do resumo do DJ — a legenda pronta), `yt_description`,
`summary_md`.

- `candidate_count == 0` → não há vídeo novo; reporte e **pare**.
- `channels_with_no_fresh_candidate` → canais sem candidato fresco (normal). Não force.

## Step 3: Escolher 2 (o julgamento)

Do pool, escolha **exatamente 2**. Critérios, em ordem:

1. **Autoridade** — traz uma **figura importante da tech** (fundador/CEO, pesquisador
   de fronteira, investidor de peso)? Priorize. Painel genérico sem nome forte perde.
2. **Recência** — mais novo ganha (`published_at`). Evite vídeo com >~4-5 semanas,
   salvo se excepcional.
3. **Interesse** pro leitor de AI/Tech.

Diversidade: prefira **2 canais / 2 pessoas diferentes**; 2 do mesmo canal só se forem
claramente os dois mais fortes; **nunca** 2 com a mesma pessoa em destaque.

**Já-recomendado nunca volta.** O helper dedup contra o `RECOMMENDATIONS.md`, que o
Step 1 acabou de sincronizar — mas o sync só enxerga posts *publicados*. Se um draft
recente com recs ainda não publicou (ou o Step 1 falhou), esses vídeos não estão no
arquivo: **trate-os como já-usados** e não os repita — confira o post atual se tiver dúvida.

## Step 4: Aparar o start-time

Pra cada escolhido, olhe `chapters`. Se o 1º capítulo (00:00) for intro/cold-open/
teaser/patrocínio e houver conteúdo logo depois, use o timestamp desse capítulo **em
segundos** (`start_seconds`). Sem capítulos claros → `null`. Ex.:
`00:00 Intro / 01:00 Why Nobody...` → `start_seconds: 60`.

A descrição **não** se escreve — é o `description_pt` do candidato (1º parágrafo do DJ),
usado como está.

## Step 5: Gravar a seleção

Grave `<OUTDIR>/recs.json`:

```json
{
  "date": "<DATE>",
  "section_title": "Recomendações de hoje:",
  "items": [
    {"title": "<título original do vídeo>", "description_pt": "<1º parágrafo do DJ, verbatim>",
     "youtube_id": "...", "start_seconds": 60, "channel": "...", "published_at": "...",
     "url": "https://www.youtube.com/watch?v=..."}
  ]
}
```

`title` = título original do vídeo (não traduza). `description_pt` = copie do candidato.

Preview opcional do HTML (mesmo formato do Substack, pra conferência):

```bash
python3 <REPO>/recommendations/render-recs-html.py --in "$OUTDIR/recs.json"
```

## Step 6: Empurrar pro draft do Substack

Mostre a seleção pro usuário (título, canal, data, por quê, start-time). Então empurre a
seção pro **draft do dia** — monta os nós ProseMirror (heading + parágrafo bold "Título:"
+ descrição + embed youtube2, `<hr>` entre vídeos) e anexa depois do "Leia também".
**Idempotente**: troca qualquer seção de recs existente, não duplica.

```bash
python3 <REPO>/pipeline/tools/substack_recs.py --file "$OUTDIR/recs.json" --dir "$OUTDIR"
```

`--dir` lê o id do draft de `<OUTDIR>/.substack-draft-id`. Reporte o link do editor que
o comando imprime.

**Testar sem risco** (numa cópia do post, sem tocar no original):

```bash
python3 <REPO>/pipeline/tools/substack_recs.py --file "$OUTDIR/recs.json" --duplicate-from <POST_ID>
```

Cria um draft `[TESTE] …` idêntico, troca as recs pela seleção nova, e imprime o link.

## Regras de comportamento

- **Autoridade + recência mandam**, nessa ordem. Figura importante da tech > painel genérico.
- **Descrição = DJ (1º parágrafo), verbatim.** Não reescreva.
- **Título original.** Não traduza.
- **Já-recomendado nunca volta** — inclusive recs de drafts ainda não publicados, que o
  sync não enxerga (ver Step 3).
- **Não invente vídeo.** Só do que o helper retornou. Pool magro → diga, não force um 2º fraco.
- **Push é idempotente.** Rodar de novo troca a seção, não empilha.
- **Nunca empurre pra um post que o usuário disse estar pronto/publicado sem avisar.**
  Na dúvida, use `--duplicate-from` pra testar numa cópia primeiro.

## Pendência conhecida (dedup lag)

O sync (Step 1 + cron meio-dia) só registra recs de posts **publicados**. O Step 1
fecha o lag de calendário (edição de ontem publicada de manhã, draft rodando antes do
cron — foi assim que a rec de 2026-08-10 repetiu em 2026-08-11), mas um vídeo empurrado
pra um draft ainda **não publicado** continua invisível até publicar. Esse resto o
Step 3 cobre manualmente. Melhoria futura: o push anexar os IDs escolhidos ao arquivo
na hora, fechando o lag de vez.
