#!/usr/bin/env python3
"""List the previous editions the day's agents read as their reference.

Usage: prev-editions.py <YYYY-MM-DD>

Prints up to 3 lines 'YYYY-MM-DD: <path>', most recent first, walking back up
to 7 days from the date. Prints '(nenhuma)' when there is none.

The reference is each edition as it was SENT, not as the pipeline wrote it.
The editor's changes in Substack are the house style, and the pipeline's own
edition.md still holds the wording that was corrected. So for every previous
edition this pulls the Substack post and renders it back to edition markdown
(edition-published.md). When the post can't be pulled (no draft id, no
credentials, network), it falls back to the last pulled copy, then to
edition.md, and says so on stderr.
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import body_to_md  # noqa: E402
import substack_mirror  # noqa: E402

ROOT = os.path.join(os.path.dirname(HERE), "output", os.environ.get("PIPELINE_TOPIC", "ai"))


def draft_id(day_dir):
    meta = os.path.join(day_dir, "substack-draft.json")
    if os.path.exists(meta):
        return str(json.load(open(meta, encoding="utf-8"))["id"])
    idf = os.path.join(day_dir, ".substack-draft-id")
    if os.path.exists(idf):
        return open(idf, encoding="utf-8").read().strip()
    return None


def pull_published(day_dir, creds):
    """Write <day_dir>/edition-published.md from the live post. Returns its path."""
    did = draft_id(day_dir)
    if not did:
        raise RuntimeError("no draft id")
    sid, host = creds
    d = substack_mirror.get_draft(host, sid, did)
    body = d.get("draft_body")
    body = json.loads(body) if isinstance(body, str) else body
    md = body_to_md.render(
        {"title": d.get("draft_title"), "subtitle": d.get("draft_subtitle"), "body": body},
        edition=True,
    )
    if "### " not in md:
        raise RuntimeError("pulled post has no edition content")
    path = os.path.join(day_dir, "edition-published.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(md)
    return path


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    day = datetime.date.fromisoformat(sys.argv[1])
    try:
        creds = substack_mirror.load_creds()
    except SystemExit as e:
        creds = None
        print(f"prev-editions: {e} — using local copies", file=sys.stderr)

    found = []
    for _ in range(7):
        day -= datetime.timedelta(days=1)
        day_dir = os.path.join(ROOT, day.isoformat())
        raw = os.path.join(day_dir, "edition.md")
        if not (os.path.exists(raw) and os.path.getsize(raw)):
            continue
        path = None
        if creds:
            try:
                path = pull_published(day_dir, creds)
            except Exception as e:  # noqa: BLE001 — any failure means fall back
                print(f"prev-editions: {day}: could not pull the sent post ({e})", file=sys.stderr)
        if not path:
            cached = os.path.join(day_dir, "edition-published.md")
            path = cached if os.path.exists(cached) else raw
            print(f"prev-editions: {day}: using {os.path.basename(path)}", file=sys.stderr)
        found.append(f"{day}: {path}")
        if len(found) == 3:
            break
    print("\n".join(found) if found else "(nenhuma)")


if __name__ == "__main__":
    main()
