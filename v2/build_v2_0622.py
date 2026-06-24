#!/usr/bin/env python3
"""
Standalone builder for the v2 newsletter format — 2026-06-22 edition.

Sibling of build_v2_draft.py (which holds 06-23). Same three-tier itemized
format; world-heavy day, so the tiering leans on tech relevance.

  GRANDES (3)    H3 headline + 3 labeled bullets
  ───────
  MÉDIAS (7)     H4 thematic cluster + 1 dense bullet each
  ───────
  LEIA TAMBÉM    headline-only links

Usage:
  python3 build_v2_0622.py          # create draft (or update if id saved), print URL
  python3 build_v2_0622.py --new    # force a brand-new draft
"""
import os, sys, json, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ID_FILE = os.path.join(HERE, ".v2-draft-id-0622")
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


# ---- content: 2026-06-22 edition ----
B = "https://dailyjournal.news/news/2026-06-22/"
L = {
 'china':         B + 'china-retalia-pentagono-e-impoe-controle-de-exportacao-a-10-empresas-e-veto-de-c',
 'ira':           B + 'vance-abre-conversas-euaira-na-suica-enquanto-teera-refecha-ormuz-e-trump-ameaca',
 'colombia':      B + 'direita-radical-de-la-espriella-vence-segundo-turno-na-colombia-por-250-mil-voto',
 'uk':            B + 'keir-starmer-renuncia-ao-governo-britanico-apos-revolta-no-partido-trabalhista',
 'skhynix':       B + 'sk-hynix-supera-samsung-electronics-e-vira-a-empresa-mais-valiosa-da-coreia-do-s',
 'toto':          B + 'toto-vai-investir-us495-milhoes-em-materiais-para-chips-de-1-nanometro',
 'samsung_ai':    B + 'samsung-implanta-chatgpt-enterprise-e-codex-para-todos-os-funcionarios-sul-corea',
 'getty':         B + 'getty-images-licencia-banco-de-imagens-ao-chatgpt-em-parceria-de-exibicao-com-a',
 'minimax':       B + 'minimax-lanca-m21-e-afirma-superar-claude-sonnet-45-em-programacao-multilingue',
 'tencent':       B + 'tencent-testa-xiaowei-agente-de-ia-dentro-do-wechat-baseado-em-welm-e-deepseek',
 'defesa_vc':     B + 'defesa-tech-capta-us123-bilhoes-em-2026-e-ja-supera-o-total-de-2025-anduril-fica',
 'anduril_israel':B + 'anduril-abre-conversas-para-montar-operacao-em-israel-com-elbit-e-ministerio-da',
 'coowa':         B + 'coowa-robotica-chinesa-apoiada-pelo-softbank-prepara-ipo-em-hong-kong-com-valuat',
 'lingyi':        B + 'fornecedora-da-apple-lingyi-itech-busca-us11-bilhao-em-ipo-em-hong-kong-para-ace',
 'fda':           B + 'fda-aprova-utebzi-da-gsk-e-spero-como-primeiro-antibiotico-carbapenemico-oral-pa',
 'europa':        B + 'onda-de-calor-varre-a-europa-franca-preve-49-departamentos-em-alerta-vermelho-e',
}

TITLE = "FORMATO v2 — Grandes · Médias · Leia também [2026-06-22]"
SUB = ("China retalia o Pentágono com controle de exportações e veto de compras; "
       "SK Hynix supera a Samsung como mais valiosa da Coreia; "
       "Irã refecha Ormuz e Vance abre rodada de paz na Suíça.")
BYLINE = para(t("Por: Guilherme Saboia e Vinicius Gushiken"))


def build_doc():
    c = [BYLINE, hr()]

    # ===== GRANDES =====
    c += [
      H(3, t("China retalia o Pentágono com controle de exportações e veto de compras a empresas dos EUA")),
      ul(
        li(t("Retaliação. ", "strong"),
           t("Resposta à Seção 1260H (que passou a incluir Alibaba, BYD, Baidu, NIO e Unitree); o Ministério do Comércio "),
           lk("vetou de imediato o embarque de itens de uso dual", L['china']),
           t(" a 10 empresas americanas.")),
        li(t("Terras raras. ", "strong"),
           t("Entre as atingidas, MP Materials (única mina ativa dos EUA) e USA Rare Earth (ímãs) — centrais ao esforço de Washington por terras raras próprias.")),
        li(t("Compras. ", "strong"), t("Pequim também "),
           lk("proibiu o governo de comprar de 46 firmas", L['china']),
           t(" (subsidiárias de Lockheed, Raytheon e General Dynamics); um analista chama a medida de “em grande parte simbólica”. Vale a partir de 30/jun.")),
      ),
      H(3, t("SK Hynix supera a Samsung e vira a empresa mais valiosa da Coreia do Sul")),
      ul(
        li(t("Virada. ", "strong"),
           lk("Interrompe a liderança da Samsung desde 2000", L['skhynix']),
           t("; a SK Hynix acumula +340% no ano e é a fabricante de memória mais valiosa do mundo.")),
        li(t("Tamanho. ", "strong"),
           t("As duas valem ~2 quatrilhões de wons (US$1,35 tri) cada, excluindo ações preferenciais.")),
        li(t("HBM. ", "strong"),
           t("Em 2025 a SK Hynix tinha 61% do mercado de HBM (a memória empilhada que alimenta GPUs de IA), contra 21% da Micron e 17% da Samsung.")),
      ),
      H(3, t("Irã refecha o Estreito de Ormuz e Vance abre rodada de conversas na Suíça")),
      ul(
        li(t("Ormuz. ", "strong"),
           t("Citando ataques israelenses ao Líbano e “má-fé” dos EUA, o Irã "),
           lk("anunciou no sábado o refechamento do Estreito", L['ira']), t(".")),
        li(t("Conversas. ", "strong"),
           t("No domingo, JD Vance abriu em Bürgenstock a 1ª rodada sob o memorando de junho, mirando estender por 60 dias o cessar-fogo de abril; Trump ameaçou “bombardear de novo, só que mais forte”.")),
        li(t("Petróleo. ", "strong"), t("O Brent abriu em alta mas "),
           lk("recuou após o Irã dizer ter obtido isenções", L['ira']),
           t(" para exportar petróleo; o total de mortos no Líbano desde 2/mar passa de 4 mil.")),
      ),
      hr(),
    ]

    # ===== MÉDIAS =====
    c += [
      H(4, t("IA corporativa & modelos")),
      ul(
        li(t("Samsung. ", "strong"), t("Vai dar "),
           lk("ChatGPT Enterprise e Codex a todos os funcionários sul-coreanos", L['samsung_ai']),
           t(" e à divisão global DX, revertendo o veto de 2023; o Codex cresceu ~800% na Coreia desde fevereiro.")),
        li(t("Tencent. ", "strong"), t("Testa o "),
           lk("Xiaowei, agente de IA dentro do WeChat", L['tencent']),
           t(" (1,4 bi de usuários), sobre o WeLM e roteando ao DeepSeek; virou prioridade estratégica máxima, atrás de ByteDance e Alibaba.")),
        li(t("MiniMax. ", "strong"), t("Lança o "),
           lk("M2.1", L['minimax']),
           t(", modelo chinês de programação que diz “superar o Claude Sonnet 4.5 e se aproximar do Opus 4.5”.")),
      ),
      H(4, t("Defesa")),
      ul(
        li(t("Venture capital. ", "strong"), t("Startups de defesa já "),
           lk("captaram US$12,3bi em 2026", L['defesa_vc']),
           t(" (quase 2× o ano passado), 93% nos EUA; a Anduril levou quase metade e agora vale US$61bi.")),
        li(t("Anduril. ", "strong"), t("Em "),
           lk("conversas para montar operação em Israel", L['anduril_israel']),
           t(" com a Elbit e o Ministério da Defesa — P&D local, vendas e contribuição à linha global.")),
      ),
      H(4, t("Mundo")),
      ul(
        li(t("Colômbia. ", "strong"), t("A direita radical de "),
           lk("de la Espriella venceu o 2º turno por ~250 mil votos", L['colombia']),
           t(" (o mais votado da história do país); Petro contesta, mas observadores validaram o pleito.")),
        li(t("Reino Unido. ", "strong"),
           lk("Keir Starmer renuncia", L['uk']),
           t(" após o Trabalhista perder mil cadeiras em maio; Andy Burnham, o “Rei do Norte”, é o favorito.")),
      ),
      hr(),
    ]

    # ===== LEIA TAMBÉM =====
    c += [
      H(4, t("Leia também")),
      ul(
        li(lk("Coowa, robótica chinesa apoiada pelo SoftBank, prepara IPO em Hong Kong com valuation acima de US$3bi", L['coowa'])),
        li(lk("Fornecedora da Apple, Lingyi iTech busca US$1,1bi em IPO em Hong Kong para acelerar em hardware de IA", L['lingyi'])),
        li(lk("Getty Images licencia banco de imagens ao ChatGPT em parceria de exibição com a OpenAI", L['getty'])),
        li(lk("Toto vai investir US$495mi em materiais para chips de 1 nanômetro", L['toto'])),
        li(lk("FDA aprova Utebzi (GSK e Spero), primeiro antibiótico carbapenêmico oral", L['fda'])),
        li(lk("Onda de calor varre a Europa; França prevê 49 departamentos em alerta vermelho", L['europa'])),
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
