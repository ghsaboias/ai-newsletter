#!/usr/bin/env python3
"""Recall check: what did the press cover heavily in the window that research.json lacks?

The researchers are the only recall the pipeline has, and each one sees its own
beat, 5 searches and 7 slots. Nothing checks the merged research against an
independent list of the window's biggest stories. On 2026-11-13 that let two
stories through: the Microsoft 365 global outage (DJ's largest cluster of the
window, 76 articles) and Starship Flight 15 (seen by the world researcher on
five consecutive days, never picked). This tool builds that independent list;
the recall-triage agent decides each item (covered / add / reject); `merge`
folds the result back into research.json.

Two independent sources, both bounded by the window end (safe for backtests):
  - DJ's own ingest: the `news` clusters that gained the most articles in the
    window (technology / science / world, Brazil-domestic excluded), with the
    underlying article URLs as sources;
  - the day's Techmeme scan (techmeme.md, fetched by research-brief.sh), top N.

Usage:
  recall-check.py candidates <DATE> [--top 30] [--techmeme 25] [--since ISO --until ISO]
      → $DAY_DIR/recall-candidates.json
  recall-check.py merge <DATE>
      reads $DAY_DIR/recall.json (written by the recall-triage agent), appends the
      added stories to research.json and tags matched stories with `salience`.

DAY_DIR = ${PIPELINE_OUTPUT:-pipeline/output/ai}/<DATE>, like the shell tools.
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LOOP_DIR = Path(os.environ.get("PIPELINE_OUTPUT") or REPO / "pipeline" / "output" / os.environ.get("PIPELINE_TOPIC", "ai"))
DJ_DIR = Path.home() / "daily-journal-platform"
BRT = dt.timezone(dt.timedelta(hours=-3))
CATEGORIES = ("technology", "science", "world")


def day_dir(date):
    return LOOP_DIR / date


def prev_date(date):
    """Same rule as research-brief.sh: most recent earlier day with research.json."""
    d = dt.date.fromisoformat(date)
    for i in range(1, 8):
        c = (d - dt.timedelta(days=i)).isoformat()
        if (LOOP_DIR / c / "research.json").is_file() and (LOOP_DIR / c / "research.json").stat().st_size:
            return c
    return (d - dt.timedelta(days=1)).isoformat()


def window(date, since=None, until=None):
    s = since or dt.datetime.fromisoformat(prev_date(date) + "T10:00:00").replace(tzinfo=BRT).isoformat()
    u = until or dt.datetime.fromisoformat(date + "T10:00:00").replace(tzinfo=BRT).isoformat()
    return s, u


def sbq(sql):
    out = subprocess.run(["sbq", "--sql", sql], cwd=DJ_DIR, capture_output=True, text=True, timeout=180)
    txt = out.stdout.strip()
    start = txt.find("[")
    if out.returncode != 0 or start < 0:
        raise SystemExit(f"recall-check: sbq failed: {out.stderr.strip() or txt[:300]}")
    return json.loads(txt[start:])


def dj_candidates(since, until, top):
    cats = ",".join(f"'{c}'" for c in CATEGORIES)
    sql = f"""
with w as (
  select n.id, n.slug, n.headline, n.summary, n.category, n.created_at, count(*) as arts
  from news n join news_articles na on na.news_id = n.id
  where na.added_at > '{since}' and na.added_at <= '{until}'
    and n.created_at <= '{until}'
    and n.duplicate_of is null and not coalesce(n.is_demoted, false)
    and n.category && array[{cats}]::text[] and not ('brazil' = any(n.category))
  group by n.id
  order by arts desc, n.created_at
  limit {int(top)}
)
select w.id, w.slug, w.headline, w.summary, w.category, w.created_at, w.arts,
  (select json_agg(json_build_object('url', a.url, 'title', a.title, 'outlet', s.name,
                                     'published_at', a.published_at) order by a.published_at)
     from news_articles na join article_ai ai on ai.id = na.article_ai_id
     join articles a on a.id = ai.article_id left join rss_sources s on s.id = a.source_id
    where na.news_id = w.id and na.added_at <= '{until}') as articles
from w order by w.arts desc, w.created_at
"""
    rows = sbq(sql)
    out = []
    for i, r in enumerate(rows, 1):
        arts = [a for a in (r.get("articles") or []) if a.get("url")][:8]
        out.append({
            "key": f"dj:{i}",
            "source": "dj",
            "rank": i,
            "articles_in_window": r["arts"],
            "headline_pt": r["headline"],
            "summary_pt": r.get("summary") or "",
            "category": r.get("category") or [],
            "dj_url": f"https://dailyjournal.news/news/{str(r['created_at'])[:10]}/{r['slug']}",
            "sources": arts,
        })
    return out


TM_ITEM = re.compile(r"^(\d+)\. (.+)$")
TM_SRC = re.compile(r"^\s+(.+?) — (https?://\S+)\s*$")


def techmeme_candidates(path, top):
    if not path.is_file():
        return []
    items, cur = [], None
    for line in path.read_text().splitlines():
        m = TM_ITEM.match(line)
        if m:
            cur = {"rank": int(m.group(1)), "headline": m.group(2).strip(), "outlet": "", "url": "", "snippet": ""}
            items.append(cur)
            continue
        if cur is None:
            continue
        s = TM_SRC.match(line)
        if s and not cur["url"]:
            cur["outlet"], cur["url"] = s.group(1).strip(), s.group(2)
        elif cur["url"] and not cur["snippet"] and line.strip() and not line.strip().startswith((">", "Also:")):
            cur["snippet"] = line.strip()
    out = []
    for it in items[:top]:
        out.append({
            "key": f"tm:{it['rank']}",
            "source": "techmeme",
            "rank": it["rank"],
            "headline": it["headline"],
            "snippet": it["snippet"],
            "sources": [{"url": it["url"], "title": it["headline"], "outlet": it["outlet"].split(" / ")[-1], "published_at": None}] if it["url"] else [],
        })
    return out


def cmd_candidates(a):
    d = day_dir(a.date)
    since, until = window(a.date, a.since, a.until)
    cands = dj_candidates(since, until, a.top) + techmeme_candidates(d / "techmeme.md", a.techmeme)
    doc = {"date": a.date, "window": {"since": since, "until": until}, "candidates": cands}
    (d / "recall-candidates.json").write_text(json.dumps(doc, ensure_ascii=False, indent=2))
    n_dj = sum(c["source"] == "dj" for c in cands)
    print(f"recall candidates: {n_dj} DJ + {len(cands) - n_dj} Techmeme → {d / 'recall-candidates.json'} (window {since} → {until})")


def cmd_merge(a):
    d = day_dir(a.date)
    research_p, recall_p, cand_p = d / "research.json", d / "recall.json", d / "recall-candidates.json"
    research = json.loads(research_p.read_text())
    if research.get("recall_merged"):
        print("recall: already merged — skip")
        return
    recall = json.loads(recall_p.read_text())
    cands = {c["key"]: c for c in json.loads(cand_p.read_text())["candidates"]}
    allowed_urls = {s["url"] for c in cands.values() for s in c.get("sources", [])}

    def salience_of(keys):
        sal = {}
        for k in keys:
            c = cands.get(k)
            if not c:
                continue
            if c["source"] == "dj":
                sal["dj_rank"], sal["dj_articles"] = c["rank"], c["articles_in_window"]
            else:
                sal["techmeme_rank"] = c["rank"]
        return sal

    by_id = {s["id"]: s for s in research["stories"]}
    keys_by_story = {}
    for dec in recall.get("decisions", []):
        if dec.get("action") in ("covered", "add") and dec.get("story_id"):
            keys_by_story.setdefault(dec["story_id"], []).append(dec.get("candidate"))

    added, dropped = 0, []
    for st in recall.get("stories", []):
        bad = [s["url"] for s in st.get("sources", []) if s.get("url") not in allowed_urls]
        srcs = {s["url"] for s in st.get("sources", [])}
        bad += [f["source_url"] for f in st.get("key_facts", []) if f.get("source_url") not in srcs]
        if bad or not st.get("key_facts") or not st.get("id") or st["id"] in by_id:
            dropped.append((st.get("id"), bad[:2] or "missing facts/id or id clash"))
            continue
        st["origin"] = "recall"
        research["stories"].append(st)
        by_id[st["id"]] = st
        added += 1

    for sid, keys in keys_by_story.items():
        if sid in by_id:
            sal = salience_of(keys)
            if sal:
                by_id[sid]["salience"] = sal

    research["story_count"] = len(research["stories"])
    research["source_count"] = sum(len(s.get("sources", [])) for s in research["stories"])
    research["recall_merged"] = True
    research_p.write_text(json.dumps(research, ensure_ascii=False, indent=2))

    decs = recall.get("decisions", [])
    count = lambda act: sum(x.get("action") == act for x in decs)
    print(f"recall: {count('covered')} covered, {added} added, {count('reject')} rejected"
          + (f", {len(dropped)} added-story(ies) DROPPED by validation: {dropped}" if dropped else ""))
    for x in decs:
        if x.get("action") == "add":
            print(f"  + {x.get('candidate')}: {x.get('story_id')}")
        elif x.get("action") == "reject":
            c = cands.get(x.get("candidate"), {})
            print(f"  - {x.get('candidate')} {c.get('headline_pt') or c.get('headline', '')[:90]} — {x.get('reason')}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("candidates")
    c.add_argument("date")
    c.add_argument("--top", type=int, default=30)
    c.add_argument("--techmeme", type=int, default=25)
    c.add_argument("--since")
    c.add_argument("--until")
    m = sp.add_parser("merge")
    m.add_argument("date")
    a = p.parse_args()
    {"candidates": cmd_candidates, "merge": cmd_merge}[a.cmd](a)


if __name__ == "__main__":
    main()
