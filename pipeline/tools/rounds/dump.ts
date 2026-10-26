// Dumps the week's vc_round deals exactly as the Monday Slack job ("Rodadas da semana",
// DJ cron deals-weekly-slack, 12:00 UTC) sees them, plus the context the reviewers need.
// usage: cd ~/daily-journal-platform && bun --env-file=.env.local <this> <YYYY-MM-DD> <outdir>
// writes: <outdir>/digest.txt (the Slack text), <outdir>/items.json (one item per round, ranked)
import { writeFileSync, mkdirSync } from 'node:fs'

const DJ = `${process.env.HOME}/daily-journal-platform`
const { fetchWeeklyRounds, formatWeeklyDigest, formatRoundItem, roundUrl } = await import(`${DJ}/lib/deals/ingest-weekly-digest`)
const { supabaseServer } = await import(`${DJ}/lib/supabase/server`)

const [date, out] = process.argv.slice(2)
if (!/^\d{4}-\d{2}-\d{2}$/.test(date ?? '') || !out) throw new Error('usage: dump.ts <YYYY-MM-DD> <outdir>')
mkdirSync(out, { recursive: true })

// Same window as the job: the 7 days before Monday 12:00 UTC.
const now = new Date(`${date}T12:00:00Z`)
const from = new Date(now.getTime() - 7 * 864e5)
const rounds = await fetchWeeklyRounds({ now })
const digest = formatWeeklyDigest(rounds, { from, to: now })
writeFileSync(`${out}/digest.txt`, `${digest.headline}\n\n${digest.replies.join('\n\n')}\n`)

const sorted = [...rounds].sort((a, b) => (b.amount_usd ?? -1) - (a.amount_usd ?? -1))
const ids = sorted.map((r) => r.id)
const { data: extra, error } = await supabaseServer
  .from('deals')
  .select('id, company_key, confidence, fx_rate, review_flags, source_excerpt, terms, verification, is_brazil, deal_news(news_id)')
  .in('id', ids)
if (error) throw error
const extraById = new Map(extra.map((e) => [e.id, e]))
const newsIds = [...new Set(extra.flatMap((e) => e.deal_news.map((d) => d.news_id)))]
const { data: news, error: ne } = await supabaseServer
  .from('news')
  .select('id, slug, headline, created_at, primary_source')
  .in('id', newsIds)
if (ne) throw ne
const newsById = new Map(news.map((n) => [n.id, n]))
const keys = [...new Set(extra.map((e) => e.company_key))]
const { data: prior, error: pe } = await supabaseServer
  .from('deals')
  .select('id, company_key, company_name, deal_type, status, stage, amount_usd, announced_at, first_news_at')
  .in('company_key', keys)
if (pe) throw pe

const leadsOf = (r) => r.parties.filter((p) => p.role === 'lead').map((p) => p.name.toLowerCase())
const items = sorted.map((r, i) => {
  const e = extraById.get(r.id)
  const others = prior.filter((p) => p.company_key === e.company_key && p.id !== r.id)
  // Cheap cross-item hints; a reviewer only sees its own batch, so the orchestrator reads these.
  const hints = []
  for (const [j, s] of sorted.entries()) {
    if (j === i) continue
    const se = extraById.get(s.id)
    if (se.company_key === e.company_key) hints.push(`same company_key as #${j + 1} ${s.company_name}`)
    else if (
      r.amount_usd && s.amount_usd && Math.abs(r.amount_usd - s.amount_usd) / r.amount_usd < 0.02 &&
      leadsOf(r).some((l) => leadsOf(s).includes(l))
    )
      hints.push(`same amount and lead as #${j + 1} ${s.company_name}`)
  }
  for (const p of others) {
    const days = (new Date(r.announced_at).getTime() - new Date(p.announced_at).getTime()) / 864e5
    if (p.status === 'published' && !ids.includes(p.id) && days >= 0 && days < 180)
      hints.push(`earlier deal ${p.announced_at.slice(0, 10)} ${p.stage ?? ''} US$${p.amount_usd ?? '?'} (possible recycle/extension)`)
  }
  return {
    n: i + 1,
    id: r.id,
    output: formatRoundItem(r, i + 1),
    hints,
    db: { ...r, url: roundUrl(r), company_key: e.company_key, confidence: e.confidence, fx_rate: e.fx_rate, review_flags: e.review_flags, source_excerpt: e.source_excerpt, terms: e.terms, verification: e.verification },
    linked_news: e.deal_news.map((d) => newsById.get(d.news_id)),
    other_deals_same_company: others,
  }
})
writeFileSync(`${out}/items.json`, JSON.stringify(items, null, 2))
console.log(digest.headline.replace(/\*/g, ''))
console.log(`items: ${items.length}, with hints: ${items.filter((x) => x.hints.length).length}`)
