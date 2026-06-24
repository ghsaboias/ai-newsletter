#!/usr/bin/env python3
"""
Standalone builder for the v2 newsletter format — 2026-06-19 edition.

Sibling of build_v2_draft.py (06-23) and build_v2_0622.py. Same three-tier
itemized format. Dense AI/tech day → 5 balanced médias clusters of 2.

  GRANDES (3)    H3 headline + 3 labeled bullets
  ───────
  MÉDIAS (10)    H4 thematic cluster + dense bullets (2 each)
  ───────
  LEIA TAMBÉM    headline-only links

Usage:
  python3 build_v2_0619.py          # create draft (or update if id saved), print URL
  python3 build_v2_0619.py --new    # force a brand-new draft
"""
import os, sys, json, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ID_FILE = os.path.join(HERE, ".v2-draft-id-0619")
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


# ---- content: 2026-06-19 edition ----
B = "https://dailyjournal.news/news/2026-06-19/"
L = {
 'ira':       B + 'eua-e-ira-assinam-memorando-de-14-pontos-e-petroleo-cai-ao-menor-nivel-desde-fev',
 'india':     B + 'bloqueio-do-telegram-na-india-provoca-pico-de-49-em-downloads-de-vpns',
 'asml':      B + 'lutnick-diz-a-asml-que-suspeita-de-maquina-euv-em-territorio-chines',
 'intel':     B + 'intel-contrata-ex-ceo-da-sk-hynix-seok-hee-lee-como-vice-presidente-executivo-da',
 'amazon':    B + 'amazon-negocia-vender-chips-trainium-para-data-centers-de-terceiros-pela-primeir',
 'google':    B + 'google-da-garantia-de-us32-bilhoes-para-data-center-em-nova-york-que-vai-alugar',
 'anthropic': B + '200-organizacoes-do-project-glasswing-mantem-acesso-ao-mythos-preview-da-anthrop',
 'openai':    B + 'openai-cria-area-strategic-futures-sob-ex-conselheiro-de-ia-da-casa-branca-dean',
 'apple':     B + 'apple-abre-ios-no-brasil-a-marketplaces-alternativos-e-pagamentos-externos-sob-a',
 'accenture': B + 'accenture-investe-us418-bi-em-dragos-runzero-e-netrise-para-entrar-em-seguranca',
 'spacex':    B + 'spacex-prepara-oferta-de-us20-bi-em-divida-para-refinanciar-emprestimo-da-aquisi',
 'jio':       B + 'reliance-protocola-drhp-do-ipo-da-jio-platforms-que-pode-ser-o-maior-da-historia',
 'genint':    B + 'general-intuition-negocia-rodada-de-us300-mi-a-valuation-acima-de-us2-bi-com-bez',
 'xdof':      B + 'xdof-sai-do-stealth-com-us70-mi-e-libera-maior-dataset-aberto-de-manipulacao-rob',
 'meta':      B + 'meta-contrata-16-gw-de-capacidade-computacional-da-crusoe-no-texas-e-no-missouri',
 'takeda':    B + 'takeda-da-a-toda-a-sua-pesquisa-acesso-aos-modelos-biomoleculares-da-boltz',
 'midjourney':B + 'midjourney-estreia-em-hardware-e-medicina-com-aparelho-de-ultrassom-de-corpo-int',
}

TITLE = "FORMATO v2 — Grandes · Médias · Leia também [2026-06-19]"
SUB = ("Acordo EUA-Irã entra em vigor e o petróleo recua ao menor nível desde fevereiro; "
       "Amazon negocia vender seus chips Trainium fora da AWS; "
       "Apple abre o iOS no Brasil a marketplaces alternativos, sob acordo com o CADE.")
BYLINE = para(t("Por: Guilherme Saboia e Vinicius Gushiken"))


def build_doc():
    c = [BYLINE, hr()]

    # ===== GRANDES =====
    c += [
      H(3, t("Acordo que encerra a guerra EUA-Irã entra em vigor e o petróleo recua ao menor nível desde fevereiro")),
      ul(
        li(t("Memorando. ", "strong"), t("Trump e Pezeshkian "),
           lk("assinaram remotamente o memorando de 14 pontos", L['ira']),
           t(", em vigor de imediato — fim das hostilidades, reabertura de Ormuz, fim do bloqueio naval e volta das exportações de petróleo iraniano.")),
        li(t("Petróleo. ", "strong"), t("O Brent fechou a US$77,69 (WTI a US$74,90), "),
           lk("menor nível desde 27/fev", L['ira']),
           t(", devolvendo a maior parte do prêmio de risco; Vance disse que +12 mi de barris já cruzaram o Estreito.")),
        li(t("Próximos passos. ", "strong"),
           t("Teerã tem 60 dias para apresentar o plano nuclear; Washington promete US$300bi em reconstrução se houver cumprimento, e Trump avisou que pode “voltar a bombardear”.")),
      ),
      H(3, t("Amazon negocia vender seus chips Trainium para data centers de terceiros pela primeira vez")),
      ul(
        li(t("Virada. ", "strong"),
           lk("Os chips, até agora exclusivos da AWS", L['amazon']),
           t(", poderiam ir a data centers externos; o gatilho é a demanda por infraestrutura de IA soberana, sobretudo europeia.")),
        li(t("Tamanho. ", "strong"), t("Jassy estima que o negócio de chips pode chegar a "),
           lk("~US$50bi anualizados", L['amazon']),
           t(" (vs US$20bi hoje); os compromissos só da linha Trainium passam de US$225bi, e o Trainium4 está reservado por +1 ano.")),
        li(t("Padrão. ", "strong"),
           t("Espelha o Google, que começou a oferecer suas TPUs (chips dedicados a IA) a parceiros externos.")),
      ),
      H(3, t("Apple abre o iOS no Brasil a marketplaces alternativos e pagamentos externos, sob acordo com o CADE")),
      ul(
        li(t("Abertura. ", "strong"), t("A partir do iOS 26.5, "),
           lk("devs brasileiros poderão distribuir apps fora da App Store e cobrar fora do In-App Purchase", L['apple']),
           t("; marketplaces alternativos precisam de aval da Apple e pagam 5% sobre bens digitais.")),
        li(t("Taxas. ", "strong"),
           t("A comissão padrão cai para no máximo 21% (era até 30%), com 10% para Small Business e assinaturas após o 1º ano; links externos pagam 15% sobre compras em até 7 dias.")),
        li(t("Origem. ", "strong"),
           t("Encerra um processo no CADE aberto em 2022 por queixa do MercadoLibre; devs têm até 6/jul para aderir.")),
      ),
      hr(),
    ]

    # ===== MÉDIAS =====
    c += [
      H(4, t("Semicondutores")),
      ul(
        li(t("ASML. ", "strong"), t("Lutnick disse à fabricante holandesa que "),
           lk("suspeita de uma máquina EUV em território chinês", L['asml']),
           t(" — a ASML nega (“314 no mundo, nenhuma na China”); o MATCH Act miraria até a DUV, ~1/5 da receita de 2026.")),
        li(t("Intel. ", "strong"), t("Contrata o ex-CEO da SK Hynix "),
           lk("Seok-Hee Lee como vice-presidente executivo da Foundry", L['intel']),
           t(", para empacotamento e back-end (a etapa que transforma o transistor gravado em chip funcional).")),
      ),
      H(4, t("Infraestrutura de IA")),
      ul(
        li(t("Google. ", "strong"), t("Dá "),
           lk("garantia de US$3,2bi a um data center em NY", L['google']),
           t(" que vai alugar suas TPUs à Anthropic e prepara captação de US$85bi — a fórmula da Nvidia de bancar a própria demanda.")),
        li(t("Meta. ", "strong"), t("Contrata "),
           lk("~1,6 GW de capacidade da Crusoe", L['meta']),
           t(" (Texas e Missouri); a desenvolvedora já tem contratos firmes para 4,9 GW e +40 GW em projetos.")),
      ),
      H(4, t("Labs de IA")),
      ul(
        li(t("Anthropic. ", "strong"), t("Cerca de 200 orgs do Project Glasswing "),
           lk("mantêm acesso ao Mythos Preview", L['anthropic']),
           t(" apesar do veto do governo ao lançamento público; o modelo já apontou +10 mil falhas de severidade alta ou crítica.")),
        li(t("OpenAI. ", "strong"), t("Cria a "),
           lk("Strategic Futures sob Dean Ball, ex-Casa Branca", L['openai']),
           t(", com mandato sobre risco catastrófico, auto-melhoria recursiva e impacto no emprego.")),
      ),
      H(4, t("Robótica")),
      ul(
        li(t("General Intuition. ", "strong"), t("Negocia "),
           lk("US$300mi", L['genint']), t(" a um "), t("valuation", "em"),
           t(" acima de US$2bi (Bezos, Schmidt); treina agentes com ~2 bi de clipes de games/ano e recusou uma compra de US$500mi da OpenAI.")),
        li(t("XDOF. ", "strong"), t("Capta "),
           lk("US$70mi (Thrive, a16z, Lux)", L['xdof']),
           t(" e libera o ABC-130K, maior dataset aberto de manipulação robótica com dois braços (+130 mil demonstrações).")),
      ),
      H(4, t("Mercado")),
      ul(
        li(t("SpaceX. ", "strong"), t("Bancos preparam "),
           lk("US$20bi em dívida para refinanciar o empréstimo da compra da xAI", L['spacex']),
           t(" — 1ª oferta da empresa com grau de investimento; ela tem ~US$45bi em contratos de compute com a Anthropic.")),
        li(t("Jio Platforms. ", "strong"), t("A Reliance protocolou o "),
           lk("prospecto do IPO que pode ser o maior da história da Índia", L['jio']),
           t(" (US$130–180bi); Meta e Google detêm fatias relevantes.")),
      ),
      hr(),
    ]

    # ===== LEIA TAMBÉM =====
    c += [
      H(4, t("Leia também")),
      ul(
        li(lk("Accenture investe US$4,18bi em Dragos, runZero e NetRise para entrar em segurança de tecnologia operacional", L['accenture'])),
        li(lk("Bloqueio do Telegram na Índia provoca pico de 49% em downloads de VPNs", L['india'])),
        li(lk("Takeda dá a toda a sua pesquisa acesso aos modelos biomoleculares da Boltz", L['takeda'])),
        li(lk("Midjourney estreia em hardware e medicina com aparelho de ultrassom de corpo inteiro", L['midjourney'])),
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
