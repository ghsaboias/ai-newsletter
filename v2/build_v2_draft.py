#!/usr/bin/env python3
"""
Standalone builder for the v2 newsletter format (three-tier, fully itemized).

Encodes the 2026-06-23 edition in the new format so we can see it in the
Substack editor and iterate. Self-contained: loads creds, builds the
ProseMirror doc, creates (or updates) a draft, prints the URL.

  GRANDES (3)    H3 headline + 3 labeled bullets  (the must-reads)
  ───────
  MÉDIAS (6)     H4 thematic cluster + 1 dense bullet each
  ───────
  LEIA TAMBÉM    headline-only links (the genuinely minor items)

Tier = importance. Block density signals it; no label says "this is small".

Usage:
  python3 build_v2_draft.py          # create draft (or update if .v2-draft-id exists), print URL
  python3 build_v2_draft.py --new    # force a brand-new draft (overwrites the saved id)

Creds: SUBSTACK_SID / SUBSTACK_PUB_HOST from env, falling back to
~/daily-journal-platform/.env.local (same as the rest of the pipeline).
"""
import os, sys, json, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ID_FILE = os.path.join(HERE, ".v2-draft-id")
PUB_USER_ID = 473611573


def creds():
    sid = os.environ.get("SUBSTACK_SID")
    host = os.environ.get("SUBSTACK_PUB_HOST")
    if not (sid and host):
        env = os.path.expanduser("~/daily-journal-platform/.env.local")
        for line in open(env):
            line = line.strip()
            if line.startswith("SUBSTACK_SID=") and not sid:
                sid = line.split("=", 1)[1]
            elif line.startswith("SUBSTACK_PUB_HOST=") and not host:
                host = line.split("=", 1)[1]
    if not (sid and host):
        sys.exit("Error: SUBSTACK_SID/SUBSTACK_PUB_HOST not set and not in .env.local")
    return sid, host


# ---- ProseMirror helpers ----
def t(text, *marks):
    n = {"type": "text", "text": text}
    if marks:
        n["marks"] = [m if isinstance(m, dict) else {"type": m} for m in marks]
    return n

def lk(text, href):
    return t(text, {"type": "link", "attrs": {"href": href, "target": "_blank",
                    "rel": "noopener noreferrer nofollow", "class": None}})

def para(*content): return {"type": "paragraph", "attrs": {"textAlign": None}, "content": list(content)}
def H(level, *content): return {"type": "heading", "attrs": {"level": level}, "content": list(content)}
def hr(): return {"type": "horizontal_rule"}
def li(*content): return {"type": "list_item", "content": [para(*content)]}
def ul(*items): return {"type": "bullet_list", "content": list(items)}
def callout(*paras): return {"type": "calloutBlock", "content": list(paras)}


# ---- content: 2026-06-23 edition, new tiering ----
B = "https://dailyjournal.news/news/2026-06-23/"
L = {
 'spacex_debt': B + 'spacex-capta-us20bi-em-divida-e-revela-us1008bi-em-caixa-acao-cai-16',
 'spacex_refl': B + 'spacex-fecha-contrato-de-computacao-de-us63bi-com-a-reflection-ai-no-colossus-2',
 'kospi':       B + 'kospi-despenca-999-e-aciona-circuit-breaker-em-rota-global-de-acoes-de-tecnologi',
 'fiveeyes':    B + 'five-eyes-alerta-que-ia-avancada-transformara-ataques-ciberneticos-em-meses-nao',
 'openai_cyber':B + 'openai-lanca-versao-completa-do-gpt-55-cyber-e-cria-patch-the-planet-com-a-trail',
 'chevron':     B + 'chevron-e-microsoft-firmam-acordo-de-20-anos-para-data-center-a-gas-no-oeste-do',
 'oracle':      B + 'oracle-corta-21-mil-vagas-em-um-ano-e-cita-adocao-de-ia-em-balanco-anual',
 'groq':        B + 'groq-capta-us650-mi-para-expandir-nuvem-de-inferencia-apos-acordo-com-a-nvidia',
 'modular':     B + 'qualcomm-negocia-compra-da-modular-por-cerca-de-us4-bilhoes',
 'appsflyer':   B + 'appsflyer-capta-us1-bi-de-google-meta-unity-e-moloco-a-valuation-de-us27-bi',
 'bending':     B + 'bending-spoons-dona-do-vimeo-fixa-ipo-nos-eua-em-ate-us162-bi-e-mira-us19-bi',
 'lineshine':   B + 'supercomputador-chines-lineshine-destrona-el-capitan-e-lidera-o-ranking-top500',
 'halos':       B + 'nvidia-lanca-halos-for-robotics-sistema-de-seguranca-aberto-para-robos',
 'sakana':      B + 'sakana-ai-lanca-fugu-orquestrador-de-multiplos-agentes-que-age-como-um-unico-mod',
 'geo':         B + 'eua-e-ira-encerram-1-rodada-na-suica-com-roteiro-para-acordo-em-60-dias',
 'definium':    B + 'lsd-em-dose-unica-da-definium-passa-em-estudo-de-fase-3-para-depressao-grave',
 'fda':         B + 'fda-recua-e-abre-caminho-para-terapia-genica-da-regenxbio-contra-sindrome-de-hun',
}

TITLE = "FORMATO v2 — Grandes · Médias · Leia também [2026-06-23]"
SUB = ("Kospi despenca 9,99% e aciona circuit breaker em rota global de tech; "
       "SpaceX capta US$20bi em dívida e revela US$100,8bi em caixa; "
       "Oracle corta 21 mil vagas e cita a IA.")
BYLINE = para(t("Por: Guilherme Saboia e Vinicius Gushiken"))


def build_doc():
    c = [BYLINE, hr()]

    # ===== GRANDES — H3 headline + 3 labeled bullets =====
    c += [
      H(3, t("Kospi despenca 9,99%, aciona circuit breaker e arrasta a tech global")),
      ul(
        li(t("Coreia. ", "strong"), lk("Maior baixa diária desde março", L['kospi']),
           t("; Samsung e SK Hynix −12% cada, um dia depois de o Kospi cruzar 9.100 pontos pela 1ª vez.")),
        li(t("Contágio. ", "strong"),
           t("Nikkei −3,55%, Hang Seng −2% e o Stoxx 600 de tech −3,2% na abertura (STMicroelectronics e ASMI −7%); seguiu o Nasdaq −1% na segunda.")),
        li(t("Gatilho. ", "strong"),
           t("Relatório local aponta a SK Hynix desacelerando memória para IA e migrando para a DRAM comum, mais barata.")),
      ),
      H(3, t("SpaceX capta US$20bi em dívida e revela US$100,8bi em caixa")),
      ul(
        li(t("Dívida. ", "strong"), lk("Ao menos US$20bi em títulos", L['spacex_debt']),
           t(", vencimentos de 5 a 30 anos e grau de investimento nas três agências; ~US$100,8bi em caixa em 19/jun.")),
        li(t("Ação. ", "strong"),
           t("Caiu ~16% na segunda — 3ª sessão seguida de perdas (~24% em três dias) após o IPO recorde; parte dos recursos vai a data centers, inclusive no espaço.")),
        li(t("Compute. ", "strong"), lk("Contrato de US$6,3bi com a Reflection AI", L['spacex_refl']),
           t(", com chips Nvidia GB300 no Colossus 2 — menor que os da Anthropic (~US$1,25bi/mês) e do Google (~US$920mi/mês).")),
      ),
      H(3, t("Oracle corta 21 mil vagas em um ano e aponta para a IA")),
      ul(
        li(t("Corte. ", "strong"),
           t("Força global caiu para 141 mil (de 162 mil); a empresa diz que "),
           lk("a adoção de IA “resultou em reduções”", L['oracle']), t(".")),
        li(t("Custo. ", "strong"),
           t("~US$1,8bi em rescisões (vs US$374mi no ano anterior); o TD Cowen estima liberar US$8–10bi/ano em caixa.")),
        li(t("Contexto. ", "strong"),
           t("Em meio ao capex de US$55,7bi para erguer data centers de clientes como OpenAI e Meta.")),
      ),
      hr(),
    ]

    # ===== MÉDIAS — H4 cluster + 1 dense bullet each =====
    c += [
      H(4, t("Segurança")),
      ul(li(t("Five Eyes + OpenAI. ", "strong"),
            t("EUA, Reino Unido, Canadá, Austrália e Nova Zelândia publicaram uma "),
            lk("rara declaração conjunta", L['fiveeyes']),
            t(" pedindo controles básicos urgentes; no mesmo dia a OpenAI lançou o "),
            lk("GPT-5.5-Cyber", L['openai_cyber']),
            t(" (85,6% no CyberGym) e o Patch the Planet, que já gerou 64 pull requests em projetos como cURL, Go e Python."))),
      H(4, t("Infraestrutura & energia")),
      ul(li(t("Chevron + Microsoft. ", "strong"), t("O "),
            lk("Projeto Kilby", L['chevron']),
            t(" deve entregar ~2,67 GW (≈2 milhões de casas), entre os maiores complexos a gás para data center dos EUA — turbinas da GE Vernova, gás da Chevron, primeira energia em 2028."))),
      H(4, t("Hardware & modelos")),
      ul(
        li(t("TOP500. ", "strong"), t("O "),
           lk("LineShine destronou o El Capitan", L['lineshine']),
           t(" com 2,198 exaflops — 1ª liderança chinesa desde 2017 e 1ª máquina acima de 2 exaflops, só com chips domésticos (~14 mi de núcleos); ficou em 4º no teste voltado a IA.")),
        li(t("Sakana AI. ", "strong"), t("Libera o "),
           lk("Fugu", L['sakana']),
           t(", orquestrador de múltiplos agentes que age como um modelo só, para não depender de um único fornecedor nem de controles de exportação.")),
      ),
      H(4, t("Negócios")),
      ul(li(t("Qualcomm + Modular. ", "strong"), t("Qualcomm em "),
            lk("conversas para comprar a Modular por ~US$4bi", L['modular']),
            t(", 2× a avaliação de nove meses atrás; somada à Tenstorrent, passa de US$14bi em apostas de chips para data center."))),
      H(4, t("Mundo")),
      ul(li(t("EUA–Irã. ", "strong"),
            t("Washington suspendeu sanções e, segundo a imprensa iraniana, "),
            lk("liberou US$12bi", L['geo']),
            t(" congelados, com licença de 60 dias para retomar vendas de petróleo; as versões divergem no ponto nuclear (Bessent fala em Ormuz livre e inspetores; Teerã, em “discussão muito breve”)."))),
      hr(),
    ]

    # ===== LEIA TAMBÉM — headline-only links =====
    c += [
      H(4, t("Leia também")),
      ul(
        li(lk("Bending Spoons, dona do Vimeo, fixa IPO em até US$1,62bi e mira US$19bi", L['bending'])),
        li(lk("Groq capta US$650mi para expandir a nuvem de inferência", L['groq'])),
        li(lk("AppsFlyer capta US$1bi de Google, Meta, Unity e Moloco a US$2,7bi", L['appsflyer'])),
        li(lk("Nvidia lança Halos for Robotics, sistema aberto de segurança para robôs", L['halos'])),
        li(lk("LSD em dose única da Definium passa na fase 3 para depressão grave", L['definium'])),
        li(lk("FDA recua e abre caminho para a terapia gênica da Regenxbio contra a síndrome de Hunter", L['fda'])),
      ),
    ]
    return c


def request(method, url, payload, sid):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"), method=method,
        headers={"Content-Type": "application/json",
                 "Cookie": f"substack.sid={sid}",
                 "User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req).read().decode("utf-8"))


def main():
    force_new = "--new" in sys.argv
    sid, host = creds()
    doc = {"type": "doc", "content": build_doc()}
    payload = {
        "draft_title": TITLE,
        "draft_subtitle": SUB,
        "draft_body": json.dumps(doc, ensure_ascii=False),
        "draft_bylines": [{"id": PUB_USER_ID}],
        "draft_section_id": None,
        "audience": "only_paid",
        "type": "newsletter",
    }

    draft_id = None
    if not force_new and os.path.exists(ID_FILE):
        draft_id = open(ID_FILE).read().strip()

    if draft_id:
        r = request("PUT", f"https://{host}/api/v1/drafts/{draft_id}", payload, sid)
        action = "updated"
    else:
        r = request("POST", f"https://{host}/api/v1/drafts", payload, sid)
        action = "created"
        draft_id = str(r.get("id"))
        open(ID_FILE, "w").write(draft_id)

    print(f"  {action} draft {draft_id}")
    print(f"  Nodes: {len(doc['content'])} top-level")
    print(f"  URL:   https://{host}/publish/post/{draft_id}")


if __name__ == "__main__":
    main()
