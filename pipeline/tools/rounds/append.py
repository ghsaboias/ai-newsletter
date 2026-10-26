"""Put the Funding Rounds section at the end of a pulled Substack mirror (substack-body.json).
Idempotent: an existing section (rule + heading + its centered paragraphs) is replaced in place.
usage: python3 append.py <substack-body.json> <section.json>"""
import json
import sys

HEADING = 'Funding Rounds da Semana'


def txt(n):
    if n.get('type') == 'text':
        return n.get('text', '')
    return ''.join(txt(x) for x in n.get('content', []) or [])


mirror_path, section_path = sys.argv[1], sys.argv[2]
mirror = json.load(open(mirror_path))
section = json.load(open(section_path))
body = mirror['body']
doc = json.loads(body) if isinstance(body, str) else body
content = doc['content']

heads = [i for i, n in enumerate(content) if n['type'] == 'heading' and txt(n).strip() == HEADING]
if heads:
    start = heads[0] - 1 if heads[0] > 0 and content[heads[0] - 1]['type'] == 'horizontal_rule' else heads[0]
    end = heads[0] + 1
    while end < len(content) and content[end]['type'] == 'paragraph' and (content[end].get('attrs') or {}).get('textAlign') == 'center':
        end += 1
    content[start:end] = section
    print(f'replaced nodes {start}..{end - 1}')
else:
    content.extend(section)
    print('appended at the end')
mirror['body'] = json.dumps(doc, ensure_ascii=False) if isinstance(body, str) else doc
json.dump(mirror, open(mirror_path, 'w'), ensure_ascii=False, indent=1)
print(f'{len(content)} nodes, section {len(section)} nodes')
