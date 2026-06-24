#!/usr/bin/env python3
"""
newsletter-images gather step. Pure mechanics -- no taste, no entity guessing.

Two modes:

  gather.py segment <YYYY-MM-DD>
      Scaffolding for the LLM: split pt.md into paragraph blocks, join each to its
      research story by source-URL overlap, print label / links / entities /
      category. The LLM reads this + the prose to author plan.json (deciding the
      visual subject, archetype, search query, and video flag per story -- the
      judgment calls regex gets wrong).

  gather.py plan <plan.json> <YYYY-MM-DD>
      Execute a plan. For each story: gather candidates from DuckDuckGo image
      search (the query), source og:image (og_urls), benchmark page-body scrape
      (archetype == benchmark), and YouTube (video == true). Download, probe
      dims, order landscape-first, montage one contact sheet PNG per story.

plan.json schema (list):
  [{ "idx":0, "label":"Política", "subject":"Abelardo de la Espriella",
     "archetype":"protagonist", "query":"Abelardo de la Espriella Colombia",
     "og_urls":["https://..."], "video":false }, ...]

No API keys, no browser. curl + ImageMagick only.
Output: pipeline/output/ai/<DATE>/images/  (candidates.json + sheet-NN-slug.png)
"""
import re, json, sys, os, subprocess, urllib.parse, html as H
from concurrent.futures import ThreadPoolExecutor

ROOT = "/Users/guilherme/ai-newsletter"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
PLACEHOLDER = ['default-logo', 'news-story.jpg', 'analysis_og', 'opengraph-illustration',
               'social/images', 'placeholder', 'sprite', 'blank.', 'data:image']
MIN_BYTES = 4000
PER_STORY_CAP = 12

# ---------------------------------------------------------------- http helpers
def curl(url, extra=None, out=None):
    cmd = ['curl', '-sL', '--max-time', '15', '-A', UA, '-H', 'Accept-Language: en-US,en;q=0.9']
    for h in (extra or []):
        cmd += ['-H', h]
    if out:
        cmd += ['-o', out]
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=22)
        return out if out else r.stdout.decode('utf-8', 'replace')
    except Exception:
        return out if out else ''

def is_placeholder(u):
    return (not u) or any(p in u.lower() for p in PLACEHOLDER)

def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:32] or 'story'

# ----------------------------------------------------------------- gather arms
def ddg_images(query, n=8):
    home = curl('https://duckduckgo.com/?q=' + urllib.parse.quote(query) + '&iax=images&ia=images')
    m = re.search(r'vqd=["\']?([\d-]+)', home) or re.search(r'vqd=([\d-]+)&', home)
    if not m:
        return []
    j = curl(f'https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}'
             f'&vqd={m.group(1)}&f=,,,,,&p=1', extra=['Referer: https://duckduckgo.com/'])
    try:
        res = json.loads(j).get('results', [])
    except Exception:
        return []
    res = [r for r in res if not is_placeholder(r.get('image'))]
    land = [r for r in res if r.get('width', 0) >= r.get('height', 1) * 1.3]
    if len(land) < 5:                                   # relax when pool is thin
        land = [r for r in res if r.get('width', 0) >= r.get('height', 1)] or res
    return [{'arm': 'ddg', 'url': r['image'], 'w': r.get('width', 0), 'h': r.get('height', 0),
             'page': r.get('url', ''),                          # originating article URL
             'source': urllib.parse.urlparse(r.get('url', '')).netloc.replace('www.', '')}
            for r in land[:n]]

def og_image(url):
    h = curl(url)
    for p in ['og:image', 'twitter:image', 'twitter:image:src']:
        m = (re.search(r'<meta[^>]+(?:property|name)=["\']' + re.escape(p) +
                       r'["\'][^>]+content=["\']([^"\']+)["\']', h, re.I) or
             re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\']' +
                       re.escape(p) + r'["\']', h, re.I))
        if m:
            u = H.unescape(m.group(1))
            if not is_placeholder(u):
                return u
    return None

def scrape_body_images(url, n=4):
    h = curl(url)
    base = '{0.scheme}://{0.netloc}'.format(urllib.parse.urlparse(url))
    seen, out = set(), []
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', h, re.I):
        u = H.unescape(m.group(1))
        if u.startswith('//'):
            u = 'https:' + u
        elif u.startswith('/'):
            u = base + u
        if (not u.startswith('http') or is_placeholder(u) or u in seen
                or not re.search(r'\.(png|jpe?g|webp|avif)(\?|$)', u, re.I)
                or any(t in u.lower() for t in ['logo', 'icon', 'avatar', 'favicon'])):
            continue
        seen.add(u)
        out.append({'arm': 'body', 'url': u, 'w': 0, 'h': 0, 'page': url,
                    'source': urllib.parse.urlparse(url).netloc.replace('www.', '')})
        if len(out) >= n:
            break
    return out

def youtube_search(query, n=4):
    h = curl('https://www.youtube.com/results?search_query=' + urllib.parse.quote(query))
    out, seen = [], set()
    for m in re.finditer(r'"videoId":"([\w-]{11})".*?"text":"([^"]{4,120})"', h):
        vid, title = m.group(1), m.group(2)
        if vid in seen:
            continue
        seen.add(vid)
        out.append({'videoId': vid, 'title': title,
                    'embed': f'https://www.youtube-nocookie.com/embed/{vid}'})
        if len(out) >= n:
            break
    return out

# -------------------------------------------------------------- pt.md / research
def parse_paragraphs(pt_path):
    """Every story-bearing paragraph -> a block. Bold-led paras and continuation
    paras are emitted separately (a dense section often hides several stories)."""
    txt = open(pt_path).read()
    txt = re.sub(r'^---.*?---\s*', '', txt, count=1, flags=re.DOTALL)
    blocks = []
    for para in re.split(r'\n\s*\n', txt):
        para = para.strip()
        if not para or para.startswith('#'):
            continue
        hm = re.match(r'^\*\*(.+?)\.\*\*\s*(.*)', para, re.DOTALL)
        label = hm.group(1).strip() if hm else None
        body = (hm.group(2) if hm else para).strip()
        urls = re.findall(r'\]\((https?://[^)]+)\)', para)
        plain = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', body).strip()
        if plain:
            blocks.append({'label': label, 'urls': urls, 'plain': plain})
    return blocks

def join_research(urls, research):
    keys = set(u.split('?')[0] for u in urls)
    best, best_score = None, 0
    for rs in research.get('stories', []):
        rurls = set(x['url'].split('?')[0] for x in rs.get('sources', []))
        score = len(keys & rurls)
        if score > best_score:
            best, best_score = rs, score
    return best

# ----------------------------------------------------------------- segment mode
def do_segment(date):
    base = f'{ROOT}/pipeline/output/ai/{date}'
    blocks = parse_paragraphs(f'{base}/pt.md')
    research = (json.load(open(f'{base}/research.json'))
                if os.path.exists(f'{base}/research.json') else {'stories': []})
    print(f'{len(blocks)} paragraph blocks in {date}/pt.md\n')
    for i, b in enumerate(blocks):
        rs = join_research(b['urls'], research) or {}
        ent = rs.get('entities', {})
        print(f'[{i:02d}] label={b["label"]!r}')
        print(f'     text: {b["plain"][:150]}')
        print(f'     people={ent.get("people", [])[:4]} orgs={ent.get("organizations", [])[:4]} '
              f'places={ent.get("places", [])[:3]}')
        print(f'     category={rs.get("category", [])}  links={len(b["urls"])}')
        print()

# -------------------------------------------------------------------- plan mode
def gather_one(item, outdir):
    cands = []
    og_urls = item.get('og_urls', [])
    with ThreadPoolExecutor(max_workers=8) as ex:
        for src, img in zip(og_urls, ex.map(og_image, og_urls)):
            if img:
                cands.append({'arm': 'og', 'url': img, 'w': 0, 'h': 0, 'page': src,
                              'source': urllib.parse.urlparse(src).netloc.replace('www.', '')})
    if item.get('query'):
        cands += ddg_images(item['query'], n=8)
    if item.get('archetype') == 'benchmark' and og_urls:
        cands += scrape_body_images(og_urls[0], n=4)
    videos = youtube_search(item['query'] + ' demo', n=4) if item.get('video') else []

    seen, uniq = set(), []
    for c in cands:
        k = c['url'].split('?')[0]
        if k not in seen:
            seen.add(k); uniq.append(c)
    uniq = uniq[:PER_STORY_CAP]

    i = item['idx']
    def dl(idx_c):
        idx, c = idx_c
        ext = '.png' if '.png' in c['url'].split('?')[0].lower() else '.jpg'
        fn = f'{outdir}/_c{i:02d}_{idx:02d}{ext}'
        ref = 'https://' + urllib.parse.urlparse(c['url']).netloc
        if not (os.path.exists(fn) and os.path.getsize(fn) > MIN_BYTES):
            curl(c['url'], extra=[f'Referer: {ref}'], out=fn)
        if os.path.exists(fn) and os.path.getsize(fn) > MIN_BYTES:
            dim = subprocess.run(['magick', 'identify', '-format', '%w %h', fn],
                                 capture_output=True, text=True).stdout.split()
            if len(dim) == 2:
                c['w'], c['h'] = int(dim[0]), int(dim[1])
            c['file'] = fn
            return c
        return None
    files = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for c in ex.map(dl, list(enumerate(uniq))):
            if c:
                files.append(c)

    files = [c for c in files if c.get('w', 0) >= 200]
    land = sorted([c for c in files if c['w'] >= c['h'] * 1.1], key=lambda c: -c['w'])
    rest = [c for c in files if c not in land]
    ordered = (land + rest)[:PER_STORY_CAP]
    for idx, c in enumerate(ordered):
        c['idx'] = idx

    slug = slugify(item.get('label') or item.get('subject') or f'story{i}')
    sheet = f'{outdir}/sheet-{i:02d}-{slug}.png'
    if ordered:
        subprocess.run(['magick', 'montage'] + [c['file'] for c in ordered] +
                       ['-tile', '4x', '-geometry', '360x220+5+5', '-background', 'white', sheet],
                       capture_output=True)
    else:
        sheet = None
    return {
        'idx': i, 'label': item.get('label'), 'subject': item.get('subject'),
        'archetype': item.get('archetype'), 'query': item.get('query'),
        'is_video': bool(item.get('video')), 'sheet': sheet,
        'candidates': [{'idx': c['idx'], 'arm': c['arm'], 'source': c['source'],
                        'w': c['w'], 'h': c['h'], 'url': c['url'], 'page': c.get('page', ''),
                        'file': c['file']}
                       for c in ordered],
        'videos': videos,
    }

def do_review(picks_path, date):
    """Build ONE review page: per story a row of [PUBLICADA | ESCOLHA | ALT2 | ALT3]
    plus a muted strip of the remaining candidates. Gui reviews all at once and
    says keep/swap/skip. Reads picks.json (the LLM's ranking, authored after
    viewing the sheets) + candidates.json (urls/files/dims)."""
    base = f'{ROOT}/pipeline/output/ai/{date}'
    outdir = f'{base}/images'
    cand = {s['idx']: {c['idx']: c for c in s['candidates']}
            for s in json.load(open(f'{outdir}/candidates.json'))}
    picks = json.load(open(picks_path))

    def cell(label, c, klass=''):
        if c is None:
            return (f'<div class="cell {klass}"><div class="tag">{label}</div>'
                    f'<div class="ph">— não publicada —</div></div>')
        if c.get('video'):
            thumb = f'https://i.ytimg.com/vi/{c["videoId"]}/hqdefault.jpg'
            meta = '▶ ' + c.get('title', 'vídeo')[:42]
            src = c.get('source', 'YouTube')
            href = f'https://www.youtube.com/watch?v={c["videoId"]}'
            onerr = ''
        else:
            thumb = c.get('url', '')                          # render from remote URL
            meta = f'{c.get("w","?")}×{c.get("h","?")} · {c.get("arm","")}'
            src = c.get('source', '')
            href = c.get('page') or c.get('url', '')           # click -> article (img URL fallback)
            local = c.get('file', '')                          # fall back to the downloaded copy
            onerr = (f" onerror=\"this.onerror=null;this.src='file://{local}'\""
                     if local else '')
        img = f'<img src="{thumb}"{onerr}>'
        if href:
            img = f'<a href="{href}" target="_blank" rel="noopener">{img}</a>'
        return (f'<div class="cell {klass}"><div class="tag">{label}</div>'
                f'{img}<div class="meta">{src}</div>'
                f'<div class="meta dim">{meta}</div></div>')

    shown = [p for p in picks if not p.get('skip')]
    skipped = [p for p in picks if p.get('skip')]
    rows = []
    for p in shown:
        cmap = cand.get(p['idx'], {})
        ranked = [cmap.get(i) for i in p.get('ranked', [])]
        pick = (dict(p['video'], video=True) if p.get('type') == 'video' and p.get('video')
                else (ranked[0] if ranked else None))
        shipped = p.get('shipped')
        shipped_c = ({'video': True, 'videoId': shipped.get('videoId'), 'title': shipped.get('caption', ''),
                      'source': shipped.get('source', '')} if shipped and shipped.get('videoId')
                     else ({'url': shipped['url'], 'file': None, 'source': shipped.get('source', ''),
                            'w': '', 'h': '', 'arm': 'publicada'} if shipped else None))
        # alts = ranked[1], ranked[2]; if pick is a video, alts are ranked[0],ranked[1]
        alt_pool = ranked[1:] if p.get('type') != 'video' else ranked
        cells = [cell('PUBLICADA', shipped_c, 'shipped'),
                 cell('✓ ESCOLHA', pick, 'pick'),
                 cell('alt 2', alt_pool[0] if len(alt_pool) > 0 else None),
                 cell('alt 3', alt_pool[1] if len(alt_pool) > 1 else None)]
        rest_start = 3 if p.get('type') != 'video' else 2
        strip = ''.join(
            f'<span class="s"><a href="{c.get("page") or c.get("url","")}" target="_blank" rel="noopener">'
            f'<img src="{c.get("url","")}" '
            f"onerror=\"this.onerror=null;this.src='file://{c['file']}'\"></a>"
            f'<b>#{c["idx"]}</b></span>'
            for c in (ranked[rest_start:] if ranked else []) if c and c.get('file'))
        vid_note = ''
        if p.get('type') != 'video' and p.get('videos_available'):
            vid_note = '<span class="vbadge">vídeo disponível</span>'
        rows.append(
            f'<div class="row"><div class="hd"><span class="ix">[{p["idx"]:02d}]</span> '
            f'<b>{p.get("label") or p.get("subject")}</b> '
            f'<span class="arch">{p.get("archetype","")}</span>{vid_note}'
            f'<div class="cap">“{p.get("caption","")}”</div></div>'
            f'<div class="cells">{"".join(cells)}</div>'
            + (f'<div class="strip">outros: {strip}</div>' if strip else '') + '</div>')

    css = """
    body{font-family:-apple-system,Helvetica,sans-serif;background:#f4f4f2;margin:0;padding:24px;color:#1a1a1a}
    h1{font-size:20px;letter-spacing:-.5px;border-bottom:3px solid #044B2E;padding-bottom:8px}
    .row{background:#fff;border:1px solid #e3e3e0;border-radius:8px;padding:14px 16px;margin:14px 0}
    .hd{margin-bottom:10px}.ix{color:#999;font-variant-numeric:tabular-nums}
    .arch{font-size:11px;background:#eef2ef;color:#044B2E;padding:2px 7px;border-radius:10px;margin-left:6px}
    .vbadge{font-size:11px;background:#7a1fa2;color:#fff;padding:2px 7px;border-radius:10px;margin-left:6px}
    .cap{color:#555;font-style:italic;margin-top:4px;font-size:13px}
    .cells{display:flex;gap:10px;flex-wrap:wrap}
    .cell{width:230px}.cell .tag{font-size:10px;font-weight:700;letter-spacing:.4px;color:#888;margin-bottom:3px}
    .cell img{width:230px;height:150px;object-fit:contain;background:#fafafa;border:1px solid #ddd;border-radius:4px}
    .pick img{border:3px solid #044B2E}.pick .tag{color:#044B2E}
    .shipped img{border:2px solid #888}
    .meta{font-size:11px;color:#666;margin-top:2px}.meta.dim{color:#aaa}
    .ph{width:230px;height:150px;display:flex;align-items:center;justify-content:center;
        background:#fafafa;border:1px dashed #ccc;border-radius:4px;color:#bbb;font-size:12px}
    .strip{margin-top:8px;font-size:11px;color:#999}
    .strip .s{display:inline-block;margin:0 6px;text-align:center}
    .strip .s img{width:84px;height:54px;object-fit:cover;border:1px solid #ddd;border-radius:3px;display:block}
    .strip .s b{font-weight:600;color:#666}
    .skipped{background:#fff;border:1px dashed #c9a23a;border-radius:8px;padding:12px 16px;margin:18px 0}
    .skipped h2{font-size:14px;margin:0 0 6px;color:#8a6d1a}
    .skipped ul{margin:0;padding-left:18px;font-size:13px;color:#555}
    .skipped li{margin:3px 0}.skipped .ix{color:#999}
    """
    skip_html = ''
    if skipped:
        items = ''.join(
            f'<li><span class="ix">[{p["idx"]:02d}]</span> '
            f'<b>{p.get("label") or p.get("subject") or ""}</b> — '
            f'{p.get("reason", "(sem motivo)")}</li>' for p in skipped)
        skip_html = (f'<div class="skipped"><h2>Puladas — sem imagem ({len(skipped)}) · '
                     f'diga "busca imagem pra #N" pra reverter qualquer uma</h2>'
                     f'<ul>{items}</ul></div>')
    html = (f'<!doctype html><meta charset=utf8><style>{css}</style>'
            f'<h1>Imagens — {date} · {len(shown)} com imagem · {len(skipped)} puladas · '
            f'verde = minha escolha, cinza = publicada</h1>' + ''.join(rows) + skip_html)
    out = f'{outdir}/images-review.html'
    open(out, 'w').write(html)
    print(f'review page -> {out}')
    print(f'open it:  open "{out}"')


def do_inject(final_path, date):
    """Insert approved picks into substack.html -> substack-images.html.

    Each pick carries an `anchor` (start of its story paragraph's plain text);
    the figure/embed is inserted right after that <p>...</p>. Non-destructive:
    the pandoc output substack.html is left untouched."""
    base = f'{ROOT}/pipeline/output/ai/{date}'
    src = f'{base}/substack.html'
    html = open(src).read()
    picks = json.load(open(final_path))

    def norm(s):
        return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()

    # index every <p>...</p> with its end offset and normalized text
    paras = [(m.end(), norm(m.group(0))) for m in re.finditer(r'<p\b.*?</p>', html, re.DOTALL)]
    inserts = []
    for p in picks:
        anchor = norm(p['anchor'])[:50]
        pos = next((end for end, txt in paras if anchor and txt.startswith(anchor[:30])), None)
        if pos is None:                       # looser contains-match fallback
            pos = next((end for end, txt in paras if anchor[:30] in txt), None)
        if pos is None:
            print(f'  ! anchor not found for [{p["idx"]}] {p.get("label")}: "{anchor[:40]}"')
            continue
        cap = p.get('caption', '')
        if p['type'] == 'video':
            block = (f'\n<figure>\n<iframe src="{p["embed"]}" frameborder="0" '
                     f'allowfullscreen loading="lazy"></iframe>\n'
                     + (f'<figcaption>{cap}</figcaption>\n' if cap else '') + '</figure>')
        else:
            block = (f'\n<figure>\n<img src="{p["url"]}" alt="{cap}">\n'
                     f'<figcaption>{cap}</figcaption>\n</figure>')
        inserts.append((pos, block, p))
    # apply bottom-to-top so offsets stay valid
    for pos, block, p in sorted(inserts, key=lambda x: -x[0]):
        html = html[:pos] + block + html[pos:]
    out = f'{base}/substack-images.html'
    open(out, 'w').write(html)
    print(f'{len(inserts)}/{len(picks)} picks injected -> {out}')


def do_plan(plan_path, date):
    base = f'{ROOT}/pipeline/output/ai/{date}'
    outdir = f'{base}/images'
    os.makedirs(outdir, exist_ok=True)
    plan = json.load(open(plan_path))
    manifest = []
    for item in plan:
        m = gather_one(item, outdir)
        manifest.append(m)
        vtag = ' [VIDEO]' if m['is_video'] else ''
        print(f'[{m["idx"]:02d}] {str(m["label"]):20} {str(m["archetype"]):11} '
              f'{len(m["candidates"]):2d} cand  "{m["query"]}"{vtag}')
    json.dump(manifest, open(f'{outdir}/candidates.json', 'w'), ensure_ascii=False, indent=2)
    print(f'\nmanifest -> {outdir}/candidates.json\nsheets   -> {outdir}/sheet-*.png')

# ----------------------------------------------------------------------- cli
def main():
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == 'segment':
        do_segment(a[1])
    elif len(a) == 3 and a[0] == 'plan':
        do_plan(a[1], a[2])
    elif len(a) == 3 and a[0] == 'review':
        do_review(a[1], a[2])
    elif len(a) == 3 and a[0] == 'inject':
        do_inject(a[1], a[2])
    else:
        print(__doc__); sys.exit(2)

if __name__ == '__main__':
    main()
