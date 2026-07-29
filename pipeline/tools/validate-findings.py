#!/usr/bin/env python3
"""Valida o schema dos relatórios advisory (repetition.json / fact-check.json).

Uso:
    python3 pipeline/tools/validate-findings.py repetition <path>
    python3 pipeline/tools/validate-findings.py fact-check  <path>

Sai com 0 se o arquivo está conforme, 1 se não — imprimindo cada violação.
Os agentes `repetition-checker` e `fact-verifier` rodam isto antes de terminar;
a skill `newsletter-draft` roda de novo como gate advisory. Existe porque os
campos `severity`/`overlap` foram omitidos em rodadas reais e o roll-up passou a
imprimir `null` silenciosamente.
"""
import json
import sys

SEV = {"high", "medium", "low"}

SPECS = {
    "repetition": {
        "top": {"date", "previous_dates", "issues", "summary"},
        "arrays": {
            "issues": {
                "required": ["type", "severity", "overlap", "current_text", "suggestion"],
                "enums": {"type": {"story", "phrasing", "framing", "lexicon"}, "severity": SEV},
            }
        },
    },
    "fact-check": {
        "top": {"date", "fidelity_issues", "dropped_facts", "summary"},
        "arrays": {
            "fidelity_issues": {
                "required": ["severity", "where", "claim", "issue", "expected"],
                "enums": {
                    "severity": SEV,
                    "where": {"facts.md", "edition", "facts.md+edition"},
                },
            },
            "dropped_facts": {
                "required": ["severity", "story", "fact", "why_load_bearing"],
                "enums": {"severity": SEV},
            },
        },
    },
}


def validate(kind, path):
    spec = SPECS[kind]
    errs = []
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except FileNotFoundError:
        return [f"arquivo não existe: {path}"]
    except json.JSONDecodeError as exc:
        return [f"JSON inválido: {exc}"]

    if not isinstance(doc, dict):
        return ["a raiz do arquivo tem de ser um objeto JSON"]

    for extra in sorted(set(doc) - spec["top"]):
        errs.append(
            f"chave de topo fora do schema: '{extra}'. As únicas permitidas são "
            f"{sorted(spec['top'])}. Achados de léxico/estilo entram em 'issues' "
            f"com type 'lexicon', nunca num array próprio."
        )
    for missing in sorted(spec["top"] - set(doc)):
        errs.append(f"chave de topo ausente: '{missing}'")

    for name, rules in spec["arrays"].items():
        items = doc.get(name)
        if items is None:
            continue
        if not isinstance(items, list):
            errs.append(f"'{name}' tem de ser uma lista")
            continue
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                errs.append(f"{name}[{i}] não é um objeto")
                continue
            for field in rules["required"]:
                val = item.get(field)
                if val is None or (isinstance(val, str) and not val.strip()):
                    errs.append(f"{name}[{i}]: campo obrigatório '{field}' ausente ou vazio")
            for field, allowed in rules.get("enums", {}).items():
                val = item.get(field)
                if val is not None and val not in allowed:
                    errs.append(
                        f"{name}[{i}]: '{field}' = {val!r}; valores aceitos: {sorted(allowed)}"
                    )
            overlap, current = item.get("overlap"), item.get("current_text")
            if isinstance(overlap, str) and isinstance(current, str):
                if len(overlap) >= len(current):
                    errs.append(
                        f"{name}[{i}]: 'overlap' ({len(overlap)} chars) não é mais curto que "
                        f"'current_text' ({len(current)} chars) — overlap é o MENOR trecho "
                        f"que de fato se repete, não o bullet inteiro"
                    )
            if name == "issues":
                errs.extend(_check_lexicon_fix(i, item))
    return errs


def _check_lexicon_fix(i, item):
    """`fix` é obrigatório em lexicon (é o que o auto-apply consome) e proibido nos outros."""
    errs = []
    is_lex = item.get("type") == "lexicon"
    fix, overlap, current = item.get("fix"), item.get("overlap"), item.get("current_text")
    if is_lex:
        if not (isinstance(fix, str) and fix.strip()):
            errs.append(
                f"issues[{i}]: type 'lexicon' exige 'fix' — o texto exato que substitui "
                f"o 'overlap' (ex.: overlap 'sítio' → fix 'terreno')"
            )
        elif isinstance(overlap, str) and isinstance(current, str):
            if overlap not in current:
                errs.append(
                    f"issues[{i}]: 'overlap' ({overlap!r}) não aparece literalmente em "
                    f"'current_text' — o auto-apply não conseguiria localizá-lo"
                )
            elif fix == overlap:
                errs.append(f"issues[{i}]: 'fix' é idêntico ao 'overlap' — não corrige nada")
    elif fix is not None:
        errs.append(
            f"issues[{i}]: 'fix' só é permitido em type 'lexicon' (este é {item.get('type')!r}); "
            f"achados de repetição exigem julgamento humano e não são aplicados automaticamente"
        )
    return errs


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in SPECS:
        print(f"uso: {sys.argv[0]} {{{'|'.join(SPECS)}}} <path>", file=sys.stderr)
        return 2
    kind, path = sys.argv[1], sys.argv[2]
    errs = validate(kind, path)
    if errs:
        print(f"INVÁLIDO — {len(errs)} violação(ões) em {path}:")
        for e in errs:
            print(f"  - {e}")
        return 1
    print(f"OK {kind}: {path} conforme o schema")
    return 0


if __name__ == "__main__":
    sys.exit(main())
