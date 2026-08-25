# Fronteira de Pareto

**Edição:** 2026-08-25
**Chart:** `chart-terminal-bench-fronteira-custo.png`
**Fonte:** Terminal-Bench — leaderboard 2.1 (snapshot de 11 de julho de 2026)

---

Três pares de agente e modelo formam a fronteira de Pareto do Terminal-Bench 2.1: o Grok 4.5 no Cursor CLI, com 79,3% de acerto e US$134 na rodada completa; o Fable 5 no Terminus 2, com 80,4% e US$439; e o Fable 5 no Claude Code, com 83,8% e US$553. Nos outros 14 pares existe sempre outro que acerta mais e custa menos.

O benchmark dá a cada par as mesmas 89 tarefas de linha de comando, entre elas administração de sistemas e treinamento de modelos, e roda cada tarefa cinco vezes. Uma suíte de testes automatizados checa se o estado final da máquina satisfaz a instrução.

O caso mais extremo fora da fronteira é o Codex com GPT-5.5. São US$2.059 para 83,1%, quinze vezes o custo do par mais barato da fronteira por 3,8 pontos a mais de acerto, e ainda abaixo do Claude Code com Fable 5, que gasta pouco mais de um quarto disso.

A nota mede o par, não o modelo sozinho. O *harness*, a camada que executa o modelo e o conecta às ferramentas, mexe nos números tanto quanto a escolha do modelo. O Fable 5 marca 83,8% no Claude Code e 80,4% no Terminus 2, e o GPT-5.5 cai de 83,1% para 78,0% ao trocar o Codex pelo Terminus 2, com o custo caindo de US$2.059 para US$494.
