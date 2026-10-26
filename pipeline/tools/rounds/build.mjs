// Builds the "Funding Rounds da Semana" section (ProseMirror nodes) in the format published
// on 2026-10-19, from dump.ts's items.json with the consolidated review (final.json) applied.
// usage: node build.mjs <YYYY-MM-DD> <items.json> <final.json> <section.json> <preview.md>
// final.json: [{ n, verdict: "ok"|"fix"|"drop", drop_reason?, corrected?: {<db field>: value} }],
// one entry per item. corrected uses the db field names: company_name, amount_original, currency,
// amount_usd, stage, company_country (ISO2), sector_detail, leads (string[]), valuation_usd, summary,
// announced_at (YYYY-MM-DD).
import fs from 'node:fs'

const [, , date, itemsPath, finalPath, outPath, previewPath] = process.argv
const items = JSON.parse(fs.readFileSync(itemsPath, 'utf8'))
const final = new Map(JSON.parse(fs.readFileSync(finalPath, 'utf8')).map((d) => [d.n, d]))

const FIELDS = new Set(['company_name', 'amount_original', 'currency', 'amount_usd', 'stage', 'company_country', 'sector_detail', 'leads', 'valuation_usd', 'summary', 'announced_at'])
const missing = items.filter((it) => !final.has(it.n)).map((it) => it.n)
if (missing.length) throw new Error(`final.json has no decision for items ${missing.join(', ')}`)

const rounds = []
for (const it of items) {
  const d = final.get(it.n)
  if (d.verdict === 'drop') continue
  const r = { ...it.db }
  for (const [k, v] of Object.entries(d.corrected ?? {})) {
    if (!FIELDS.has(k)) throw new Error(`#${it.n} ${it.db.company_name}: unknown field ${k}`)
    if (k === 'leads') r.parties = [...v.map((name) => ({ name, role: 'lead' })), ...r.parties.filter((p) => p.role !== 'lead')]
    else r[k] = v
  }
  const c = d.corrected ?? {}
  if (('amount_original' in c || 'currency' in c) && !('amount_usd' in c)) {
    if ((r.currency ?? 'USD') === 'USD') r.amount_usd = r.amount_original
    else throw new Error(`#${it.n} ${r.company_name}: amount changed in ${r.currency}; set amount_usd too`)
  }
  rounds.push(r)
}

const SYMBOL = { USD: 'US$', BRL: 'R$', EUR: '€', GBP: '£' }
const MONTHS = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
const STAGE = {
  pre_seed: 'rodada pré-seed', seed: 'rodada seed', series_a: 'Série A', series_b: 'Série B',
  series_c: 'Série C', series_d: 'Série D', series_e: 'Série E', series_f: 'Série F',
  growth: 'rodada growth', late: 'rodada late stage', pre_ipo: 'rodada pré-IPO',
}
const one = new Intl.NumberFormat('pt-BR', { maximumFractionDigits: 1 })
const two = new Intl.NumberFormat('pt-BR', { maximumFractionDigits: 2 })
const regions = new Intl.DisplayNames(['pt-BR'], { type: 'region' })

// Billions keep two decimals so Ramp reads 1,85 and not 1,9.
function money(value, currency) {
  const s = SYMBOL[currency ?? 'USD'] ?? currency ?? 'US$'
  const a = Math.abs(value)
  if (a >= 1e9) return `${s} ${two.format(a / 1e9)} ${a / 1e9 < 2 ? 'bilhão' : 'bilhões'}`
  if (a >= 1e6) return `${s} ${one.format(a / 1e6)} ${a / 1e6 < 2 ? 'milhão' : 'milhões'}`
  if (a >= 1e3) return `${s} ${one.format(a / 1e3)} mil`
  return `${s} ${one.format(a)}`
}
const flag = (cc) => String.fromCodePoint(...[...cc.toUpperCase()].map((ch) => 0x1f1e6 + ch.charCodeAt(0) - 65))
const joinPt = (xs) => (xs.length < 2 ? xs[0] ?? '' : `${xs.slice(0, -1).join(', ')} e ${xs.at(-1)}`)
const parts = (d) => { const m = /^(\d{4})-(\d{2})-(\d{2})/.exec(d); return { day: Number(m[3]), month: MONTHS[Number(m[2]) - 1] } }
const longDate = (d) => { const p = parts(d); return `${p.day} de ${p.month}` }

const text = (t, bold) => (bold ? { type: 'text', marks: [{ type: 'strong' }], text: t } : { type: 'text', text: t })
const br = { type: 'hard_break' }
const link = (href, t) => ({ type: 'text', marks: [{ type: 'link', attrs: { href, target: '_blank', rel: 'noopener noreferrer nofollow', class: null } }], text: t })
const center = (content) => ({ type: 'paragraph', attrs: { textAlign: 'center' }, content })

function title(r, i) {
  const stage = r.stage ? STAGE[r.stage] : null
  const amount = r.amount_original != null ? money(r.amount_original, r.currency) : r.amount_usd != null ? money(r.amount_usd, 'USD') : null
  if (amount) return `${i}. ${r.company_name} — ${amount}${stage ? ` em ${stage}` : ''}`
  if (stage) return `${i}. ${r.company_name} — ${stage[0].toUpperCase()}${stage.slice(1)}, valor não divulgado`
  return `${i}. ${r.company_name} — Valor não divulgado`
}

const sorted = [...rounds].sort((a, b) => (a.amount_usd == null) - (b.amount_usd == null) || (b.amount_usd ?? 0) - (a.amount_usd ?? 0))
const md = []
const entries = sorted.map((r, k) => {
  const c = [text(title(r, k + 1), true)]
  const md1 = [`**${title(r, k + 1)}**`]
  const ident = []
  if (r.company_country) ident.push(/^[A-Z]{2}$/.test(r.company_country) ? `${flag(r.company_country)} ${regions.of(r.company_country)}` : r.company_country)
  if (r.sector_detail) ident.push(r.sector_detail)
  if (ident.length) { c.push(br, text(ident.join(' · '))); md1.push(ident.join(' · ')) }
  const leads = r.parties.filter((p) => p.role === 'lead').map((p) => p.name)
  const det = []
  if (leads.length) det.push(['Liderança:', ` ${joinPt(leads)}`])
  if (r.valuation_usd != null) det.push(['Valuation:', ` ${money(r.valuation_usd, 'USD')}`])
  if (det.length) {
    c.push(br)
    det.forEach(([k2, v], j) => { c.push(text(k2, true), text(v + (j < det.length - 1 ? ' · ' : ''))) })
    md1.push(det.map(([k2, v]) => `**${k2}**${v}`).join(' · '))
  }
  if (r.summary) { c.push(br, text(r.summary)); md1.push(r.summary) }
  const when = longDate(r.announced_at)
  if (r.url) {
    c.push(br, link(r.url, 'Notícia no Daily Journal'), text(` · ${when}`))
    md1.push(`[Notícia no Daily Journal](${r.url}) · ${when}`)
  } else { c.push(br, text(when)); md1.push(when) }
  md.push(md1.join('  \n'))
  return center(c)
})

const total = rounds.reduce((s, r) => s + (r.amount_usd ?? 0), 0)
const totalTxt = total >= 1e9 ? `US$ ${one.format(total / 1e9)} ${total / 1e9 < 2 ? 'bilhão' : 'bilhões'}` : money(total, 'USD')
const brazil = rounds.filter((r) => r.company_country === 'BR').length
const start = new Date(new Date(`${date}T12:00:00Z`).getTime() - 7 * 864e5).toISOString().slice(0, 10)
const a = parts(start), b = parts(date)
const period = a.month === b.month ? `${a.day} e ${b.day} de ${b.month}` : `${a.day} de ${a.month} e ${b.day} de ${b.month}`
const head = `${totalTxt} em ${rounds.length} rodadas entre ${period}, sendo ${brazil} no Brasil`
const nodes = [
  { type: 'horizontal_rule' },
  { type: 'heading', attrs: { textAlign: 'center', level: 3 }, content: [text('Funding Rounds da Semana', true)] },
  center([text('Todos os investimentos em startups no mundo.')]),
  center([text(head, true)]),
  ...entries,
]
fs.writeFileSync(outPath, JSON.stringify(nodes, null, 1))
fs.writeFileSync(previewPath, `### Funding Rounds da Semana\nTodos os investimentos em startups no mundo.\n\n**${head}**\n\n${md.join('\n\n')}\n`)
console.log(`${head} | ${entries.length} entries, ${items.length - rounds.length} dropped`)
