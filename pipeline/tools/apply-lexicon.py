#!/usr/bin/env python3
"""Aplica os achados `lexicon` do repetition.json a um arquivo da edição.

Uso:
    python3 pipeline/tools/apply-lexicon.py <repetition.json> <edition.md> [--execute]

Sem `--execute` é dry-run: mostra o que faria e não escreve nada.

Só toca em issues com `type == "lexicon"`, que carregam um `fix` — a substituição
literal do `overlap`. Repetição de frase, enquadramento e história NUNCA são
aplicadas aqui: exigem reescrita com julgamento editorial e continuam relatório.

Cada substituição é feita dentro do `current_text` do achado (não no arquivo
inteiro), e só quando esse trecho aparece EXATAMENTE UMA VEZ no arquivo. Qualquer
ambiguidade vira `SKIP` com o motivo — nunca um chute.
"""
import json
import sys


def load_issues(path):
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    return [i for i in doc.get("issues", []) if i.get("type") == "lexicon"]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    execute = "--execute" in sys.argv
    if len(args) != 2:
        print(f"uso: {sys.argv[0]} <repetition.json> <edition.md> [--execute]", file=sys.stderr)
        return 2
    findings_path, edition_path = args

    issues = load_issues(findings_path)
    if not issues:
        print("nenhum achado de léxico — nada a aplicar")
        return 0

    with open(edition_path, encoding="utf-8") as fh:
        text = fh.read()

    applied, skipped = [], []
    for issue in issues:
        overlap, fix, current = issue.get("overlap"), issue.get("fix"), issue.get("current_text")
        if not (overlap and fix and current):
            skipped.append((overlap, "achado sem overlap/fix/current_text"))
            continue
        if overlap not in current:
            skipped.append((overlap, "overlap não aparece no current_text do próprio achado"))
            continue
        occurrences = text.count(current)
        if occurrences == 0:
            skipped.append((overlap, "current_text não encontrado no arquivo (edição já editada?)"))
            continue
        if occurrences > 1:
            skipped.append((overlap, f"current_text aparece {occurrences}x — ambíguo"))
            continue
        text = text.replace(current, current.replace(overlap, fix))
        applied.append((overlap, fix))

    for overlap, fix in applied:
        print(f"  APPLY  {overlap!r} -> {fix!r}")
    for overlap, why in skipped:
        print(f"  SKIP   {overlap!r}: {why}")

    if execute and applied:
        with open(edition_path, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"\n{len(applied)} aplicado(s) em {edition_path}, {len(skipped)} pulado(s)")
    else:
        verb = "aplicaria" if not execute else "aplicado(s)"
        print(f"\ndry-run: {len(applied)} {verb}, {len(skipped)} pulado(s). Use --execute para gravar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
