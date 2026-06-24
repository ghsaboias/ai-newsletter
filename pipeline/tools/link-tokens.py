#!/usr/bin/env python3
"""Source-link tokens for the newsletter draft chain (research → facts → v2).

Takes URL transcription away from the content agents. URLs live in facts.md's
`**Fontes:**` blocks; the v2-generator agent cites a short token (`S12`) instead
of retyping the URL, and a deterministic step resolves tokens → real URLs. The
agent copies a 3-char tag, never an 80-char opaque string, so it cannot corrupt a
URL (the failure that shipped a broken Qualcomm link — sibling-slug contamination).

Two subcommands:

  tokenize <facts.md>
      Add an `[S<n>]` tag to the front of every Fontes source line, in place.
      Deterministic + idempotent: strips any existing tags and re-numbers 1..N
      top-to-bottom, so re-running is a no-op on already-tokenized input.

  expand <v2.md> <facts.md>
      Build the token→URL map from facts.md, then replace every `](S<n>)` link
      target in v2.md with the real URL, in place. HARD-FAILS (exit 1) on:
        - an unknown token (`](S99)` with no S99 in facts.md) — a typo/hallucination
        - a raw URL as a link target (`](https://…)`) — the agent regressed to
          pasting URLs instead of citing tokens
        - any leftover `](S\d+)` after expansion
      A clean exit means every link in the edition traces to a Fontes URL by
      construction — this replaces the after-the-fact provenance lint.

Usage:
    link-tokens.py tokenize  /path/to/facts.md
    link-tokens.py expand    /path/to/v2.md  /path/to/facts.md
"""
import re
import sys

URL_RE = re.compile(r'https?://\S+')
SECTION_RE = re.compile(r'^##\s')
FONTES_RE = re.compile(r'^\*\*Fontes:\*\*\s*$')
LIST_ITEM_RE = re.compile(r'^(\s*-\s+)(.*)$')
EXISTING_TOKEN_RE = re.compile(r'^\[S\d+\]\s*')
LINK_TARGET_RE = re.compile(r'\]\(([^)]+)\)')


def _is_source_line(line, in_fontes):
    """A Fontes source line: a list item carrying a URL, inside a Fontes block.
    The URL requirement alone is near-sufficient (fact bullets are URL-free by
    contract); the in_fontes guard is belt-and-suspenders."""
    return in_fontes and line.lstrip().startswith('-') and bool(URL_RE.search(line))


def tokenize(facts_path):
    with open(facts_path, encoding='utf-8') as f:
        lines = f.read().split('\n')

    out = []
    in_fontes = False
    counter = 0
    for line in lines:
        if SECTION_RE.match(line):
            in_fontes = False
        elif FONTES_RE.match(line.strip()):
            in_fontes = True

        if _is_source_line(line, in_fontes):
            counter += 1
            m = LIST_ITEM_RE.match(line)
            prefix, rest = m.group(1), m.group(2)
            rest = EXISTING_TOKEN_RE.sub('', rest)  # strip any prior tag, re-number fresh
            line = f'{prefix}[S{counter}] {rest}'
        out.append(line)

    with open(facts_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(f'tokenize — {counter} source tokens written to {facts_path}')
    return counter


def build_map(facts_path):
    """token (e.g. 'S12') → URL, parsed from tokenized facts.md."""
    token_map = {}
    in_fontes = False
    with open(facts_path, encoding='utf-8') as f:
        for line in f.read().split('\n'):
            if SECTION_RE.match(line):
                in_fontes = False
            elif FONTES_RE.match(line.strip()):
                in_fontes = True
            if not _is_source_line(line, in_fontes):
                continue
            tok = re.search(r'\[(S\d+)\]', line)
            urls = URL_RE.findall(line)
            if tok and urls:
                token_map[tok.group(1)] = urls[-1].rstrip('.,;)')
    return token_map


def expand(v2_path, facts_path):
    token_map = build_map(facts_path)
    if not token_map:
        sys.exit(f'expand — ERROR: no source tokens found in {facts_path}; run tokenize first')

    with open(v2_path, encoding='utf-8') as f:
        text = f.read()

    # Idempotency: a v2.md with no `S<n>` token targets is already expanded (or
    # link-free). Re-running must be a clean no-op — NOT a raw-URL failure, since
    # post-expansion every target is a real URL.
    targets = [t.strip() for t in LINK_TARGET_RE.findall(text)]
    if not any(re.fullmatch(r'S\d+', t) for t in targets):
        print(f'expand — 0 tokens to resolve in {v2_path} (already expanded or link-free); no change')
        return 0

    unknown, raw, n = [], [], 0

    def repl(m):
        nonlocal n
        tgt = m.group(1).strip()
        if re.fullmatch(r'S\d+', tgt):
            if tgt in token_map:
                n += 1
                return f']({token_map[tgt]})'
            unknown.append(tgt)
            return m.group(0)
        if tgt.startswith('http'):
            raw.append(tgt)
            return m.group(0)
        # not a token, not a URL — leave it, but it's suspicious; report as unknown
        unknown.append(tgt)
        return m.group(0)

    new_text = LINK_TARGET_RE.sub(repl, text)

    problems = []
    if unknown:
        problems.append(f'{len(unknown)} unknown/invalid token target(s): ' + ', '.join(sorted(set(unknown))))
    if raw:
        problems.append(f'{len(raw)} raw-URL target(s) (agent pasted a URL instead of a token): ' + ', '.join(sorted(set(raw))[:5]))
    if problems:
        sys.exit('expand — FAIL:\n  ' + '\n  '.join(problems) + '\n  (v2.md NOT modified)')

    with open(v2_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f'expand — {n} tokens resolved to URLs in {v2_path}; 0 unknown, 0 raw-URL regressions')
    return n


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == 'tokenize':
        tokenize(sys.argv[2])
    elif cmd == 'expand':
        if len(sys.argv) < 4:
            sys.exit('expand needs: <v2.md> <facts.md>')
        expand(sys.argv[2], sys.argv[3])
    else:
        sys.exit(f'unknown command: {cmd}\n{__doc__}')


if __name__ == '__main__':
    main()
