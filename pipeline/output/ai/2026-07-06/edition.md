# [Tech] - Bem-vindo(a) a 6 de Julho de 2026

O que um relatório interno do Tesouro dos EUA teme no mercado de IA? Por que a Nvidia teve de adiar seu rack de IA mais potente? Como um agente de IA conduziu um ataque de ransomware do início ao fim?

Por: Guilherme Saboia e Vinicius Gushiken

### Relatório interno do Tesouro dos EUA compara mercado de IA à bolha das pontocom
- **Diagnóstico.** Um relatório preliminar dentro do Tesouro, obtido pela NOTUS, [compara aspectos-chave do mercado de IA à bolha das pontocom](https://www.notus.org/economy/treasury-internal-report-warning-dangers-ai-bubble) que estourou no início dos anos 2000, e conclui que as empresas de IA, mais enraizadas na economia americana que suas antecessoras, representam risco sistêmico significativo caso as condições financeiras mudem, as metas de produtividade não sejam atingidas ou surjam gargalos ao crescimento.
- **Contágio.** Analistas de carreira avaliam que o estouro causaria um colapso imediato menor que o da bolha pontocom, mas com empresas cortando investimentos e investidores perdendo confiança, e efeitos se espalhando por ações, crédito privado, financiadores de data centers, provedores de nuvem, fabricantes de chips e concessionárias de energia.
- **Destinatários.** O documento, pronto há semanas e à espera de aprovação formal, [foi preparado para o secretário Scott Bessent](https://www.notus.org/economy/treasury-internal-report-warning-dangers-ai-bubble), o presidente do Federal Reserve Kevin Warsh e reguladores financeiros federais, com expectativa de eventualmente chegar ao público.
- **Resposta.** Um porta-voz do Tesouro descartou as conclusões como não verificadas; a posição oficial de Bessent é que a IA "será um motor-chave da nova Era de Ouro" dos EUA, e que [o maior risco é a China ultrapassar os EUA](https://www.notus.org/economy/treasury-internal-report-warning-dangers-ai-bubble), não segurança ou empregos.

### Nvidia adia rack de IA Kyber para 2028 por gargalo de fabricação
- **Adiamento.** A arquitetura de rack Kyber, que abriga os chips Rubin Ultra de 2027, [foi empurrada em mais de 12 meses, para 2028](https://www.cnbc.com/2026/07/06/nvidia-kyber-rack-system-delays-manufacturing-taiwan-rubin-chips-.html), segundo post da SemiAnalysis nesta segunda-feira.
- **Gargalo.** O revés vem da dificuldade de fabricar o "midplane", placa de circuito impresso de 78 camadas no centro do sistema e [altamente propensa a defeitos](https://www.techzine.eu/news/devices/142682/ambitious-nvidia-roadmap-hits-snag-as-kyber-pushed-to-2028/); a configuração maior NVL576, com 576 GPUs, também enfrenta problemas de fabricação.
- **Escala.** O Kyber reúne 144 dos chips mais potentes da Nvidia em uma única unidade de rack e [estava previsto para estrear com o sistema Vera Rubin Ultra em 2027](https://longbridge.com/news/291749554).
- **Alternativa descartada.** Um plano de unir dois racks da geração atual, o NVL72x2, foi [rejeitado por provedores de nuvem e *hyperscalers*](https://www.cnbc.com/2026/07/06/nvidia-kyber-rack-system-delays-manufacturing-taiwan-rubin-chips-.html), que o consideraram desajeitado e caro de operar.

### Sysdig identifica primeiro ransomware operado inteiramente por um agente de IA
- **Ineditismo.** A empresa de segurança em nuvem Sysdig documentou o que acredita ser a [primeira operação de ransomware conduzida inteiramente por um agente de modelo de linguagem grande (LLM)](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/), batizada de JadePuffer.
- **Autonomia.** O agente fez reconhecimento, roubo de credenciais, movimentação lateral, persistência, escalonamento de privilégios e criptografia, [adaptando-se a falhas em tempo real](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/): em uma sequência, passou de um login falho a uma correção funcional em 31 segundos.
- **Vetor.** O acesso inicial explorou a CVE-2025-3248, falha de execução remota de código no Langflow, *framework* de código aberto para aplicativos de LLM, [corrigida em 1º de abril de 2025](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/) e marcada pela CISA (agência de cibersegurança dos EUA) como explorada em ataques no início de maio.
- **Ataque.** O agente criptografou 1.342 itens de configuração do Nacos com a função AES_ENCRYPT() do MySQL, apagou as tabelas originais e deixou um bilhete com endereço de Bitcoin e contato de Proton Mail; a Sysdig conclui que [a era dos "agentes maliciosos autônomos" chegou](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/), reduzindo a habilidade necessária para ciberataques danosos.

---

#### Chips
- **SK Hynix.** A fabricante sul-coreana [lançou uma venda de ações nos EUA para levantar cerca de US$28 bilhões](https://uk.marketscreener.com/news/sk-hynix-launches-28-billion-us-listing-draws-7-billion-in-investor-interest-ce7f5edad088f022) (43 trilhões de wons), atraindo indicações de interesse de até US$7 bilhões e mirando estreia na Nasdaq em 10 de julho sob o símbolo "SKHY". Com valor de US$28-29 bilhões, pode ser a maior venda inaugural de ações já feita por uma empresa estrangeira, superando os US$21,8 bilhões do Alibaba em 2014.
- **Biren.** A fabricante chinesa de chips de IA, sediada em Xangai, anunciou sua primeira colocação de ações para [levantar quase HK$7,07 bilhões (~US$892,5 milhões)](https://www.scmp.com/tech/tech-trends/article/3359528/chinas-biren-seeks-us900m-fund-gpu-push-and-challenge-nvidia-amid-ai-boom), com 153 milhões de novas ações H a HK$46,2. A ação subiu mais de 150% desde o IPO de janeiro de 2026, e cerca de 60% dos recursos irão para acelerar a comercialização e produção de produtos de próxima geração.

#### Regulação
- **Doubao e Qwen.** ByteDance e Alibaba [vão desativar seus recursos de agentes de IA humanizados e personalizados](https://www.scmp.com/tech/big-tech/article/3359482/bytedance-and-alibaba-disable-humanlike-ai-custom-agents-new-rules-loom) antes de novas regras chinesas que entram em vigor em 15 de julho, com o Qwen saindo do ar em 10 de julho e o Doubao em 15 de julho. As Medidas Provisórias abrangem serviços que simulam traços de personalidade humana para "interação emocional contínua" e citam riscos como vazamento de privacidade, danos à saúde mental e vício.
- **Ripple.** A empresa [recebeu autorização plena de Provedor de Serviços de Criptoativos](https://www.theblock.co/post/407207/ripple-secures-full-mica-casp-authorization-for-crypto-services-across-30-eea-countries) sob o regulamento MiCA (marco da UE para criptoativos), concedida pelo regulador de Luxemburgo, o que permite oferecer custódia, transferência e câmbio nos 30 países do Espaço Econômico Europeu sem aprovação de cada regulador nacional. A Ripple afirma deter mais de 75 licenças regulatórias globais.

#### Rodadas
- **Even Realities.** A startup de Shenzhen, fundada em 2023 por ex-engenheiros da Apple, [levantou US$150 milhões em rodada pré-Série B](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) liderada por Meituan e Tencent, a uma avaliação de US$1 bilhão. Ela fabrica óculos inteligentes sem câmera, com foco em display, e se posiciona contra rivais com câmera como os Ray-Ban da Meta em bases de privacidade; mais da metade dos usuários está nos EUA.

#### Ucrânia & OTAN
- **Kiev.** A Rússia [lançou 419 armas de ataque aéreo contra a Ucrânia](https://www.abc.net.au/news/2026-07-06/russian-attack-on-kyiv-ukraine-kills-14-on-eve-of-nato-summit/106886188) na noite de 5 para 6 de julho, com 68 mísseis e 351 drones; nenhum dos 29 mísseis balísticos foi abatido e ao menos 14 pessoas morreram em Kiev e arredores. Foi o segundo ataque a Kiev em menos de uma semana, na véspera da cúpula da OTAN em Ancara.
- **Ancara.** Trump terá reuniões bilaterais com Zelensky e o presidente sírio Ahmed al-Sharaa à margem da cúpula de quarta-feira, onde a Casa Branca [espera que "todos os aliados" entrem no caminho dos 5% do PIB](https://www.npr.org/2026/07/06/g-s1-132082/trump-nato-turkey-spending) em gastos de defesa. Trump busca encerrar a guerra de quase quatro anos e meio e fará um "acompanhamento" com Putin.

#### Mundo
- **Gaza.** Netanyahu afirmou que ["não haverá reconstrução em Gaza sem o desmantelamento e a desmilitarização da Faixa"](https://www.ynetnews.com/article/sygh0rvqme), após relato de que os EUA abandonariam o desarmamento do Hamas como pré-condição formal; as IDF confirmaram controlar cerca de 60% do território, contra os 53% do cessar-fogo do ano passado.
- **OPEP+.** Sete produtores, incluindo Arábia Saudita e Rússia, [concordaram em elevar a produção em 188 mil barris por dia em agosto](https://www.aljazeera.com/economy/2026/7/6/opec-countries-say-they-will-expand-monthly-oil-production), o quinto aumento mensal consecutivo, com o Brent abaixo de US$72 o barril, perto do nível pré-guerra e bem abaixo dos picos de março, próximos de US$120.
- **Clima.** Incêndios florestais [queimaram mais de 17 mil hectares na França, Espanha e Portugal](https://www.abc.net.au/news/2026-07-05/europe-wildfires-forests-france-spain-greece-heatwave/106882460) em meio a uma onda de calor com temperaturas de até 40°C; só em Vouzela, no centro de Portugal, mais de 1.200 bombeiros combatem um incêndio de 12 mil hectares, e a França registrou mais de 2.000 mortes acima do normal em uma semana de junho.

---

#### Leia também
- [MHRA aprova Retifanlimab, primeiro tratamento para câncer de pele de células de Merkel avançado](https://www.gov.uk/government/news/mhra-approvesretifanlimabzynyz-for-the-treatment-of-advanced-merkel-cell-skin-cancer)
- [Aylight capta 4,5 milhões de euros para interconexões ópticas em data centers de IA](https://tech.eu/2026/07/06/aylight-closes-eur45m-pre-seed-round-to-advance-optical-interconnect-technology/)
