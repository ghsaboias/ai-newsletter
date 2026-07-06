# Fatos — Newsletter [Tech] 6 de Julho de 2026

## Departamento do Tesouro dos EUA — relatório interno sobre bolha de IA
- Um relatório preliminar dentro do Departamento do Tesouro dos EUA, obtido pela NOTUS, alerta para os riscos do mercado de inteligência artificial.
- O relatório compara aspectos-chave do mercado de IA à bolha das pontocom que estourou no início dos anos 2000.
- Analistas de carreira do Tesouro concluíram que empresas de IA estão mais enraizadas na economia americana do que suas antecessoras da era pontocom.
- Segundo o relatório, essas empresas representam risco sistêmico significativo caso as condições financeiras mudem, as metas de produtividade não sejam atingidas ou surjam gargalos ao crescimento.
- O relatório foi preparado para o secretário do Tesouro Scott Bessent, o presidente do Federal Reserve Kevin Warsh e reguladores financeiros federais.
- O documento está concluído há semanas e aguarda aprovação formal, com expectativa de eventualmente chegar ao público.
- Os analistas concluíram que o estouro de uma bolha de IA causaria um colapso imediato menor do que o da bolha pontocom.
- Ainda assim, empresas cortariam investimentos e investidores perderiam confiança, com efeitos se espalhando por mercados de ações, crédito privado, financiadores de data centers, provedores de nuvem, fabricantes de chips e concessionárias de energia.
- Um porta-voz do Tesouro descartou as conclusões como não verificadas e não representativas da posição da agência.
- Segundo o porta-voz, a posição oficial do secretário e do Tesouro é que a IA "será um motor-chave da nova Era de Ouro dos Estados Unidos".
- Em discurso de 25 de junho, em Nova York, Bessent elogiou as maiores empresas de tecnologia por investirem US$750 bilhões na expansão de IA neste ano.
- Bessent afirmou que o maior risco da IA é a China ultrapassar os EUA, e não questões de segurança ou perda de empregos.
**Fontes:**
- [S1] NOTUS — https://www.notus.org/economy/treasury-internal-report-warning-dangers-ai-bubble

## Doubao e Qwen — desativação de agentes de IA antropomórficos na China
- O Doubao, da ByteDance, e o Qwen, do Alibaba, vão desativar seus recursos de agentes de IA personalizados e humanizados.
- A medida antecede novas regras chinesas sobre serviços de interação com IA antropomórfica, que entram em vigor em 15 de julho.
- Em aviso na noite de sexta-feira, o Doubao informou aos usuários que seu recurso de agentes sairá do ar em 15 de julho, devido a "ajustes de funções do produto".
- Após 15 de outubro, os dados relacionados no Doubao não poderão mais ser visualizados nem recuperados dentro do aplicativo.
- Na manhã de sábado, o Qwen emitiu um aviso semelhante.
- Segundo o Qwen, seus "agentes interativos humanizados e funções de agentes criados por usuários" serão desativados em 10 de julho.
- As funções e serviços mais amplos de agentes do Qwen sairão do ar em 15 de julho.
- As medidas coincidem com as Medidas Provisórias para a Administração de Serviços de Interação Antropomórfica de Inteligência Artificial, em vigor a partir de 15 de julho.
- As regras foram publicadas em abril.
- As regras abrangem serviços de IA que "simulam traços de personalidade humana, padrões de pensamento e estilos de comunicação para fornecer interação emocional contínua".
- As regras excluem bots de atendimento ao cliente, perguntas e respostas de conhecimento, assistentes de trabalho e ferramentas de educação e pesquisa científica, desde que não envolvam interação emocional contínua.
- As medidas citam riscos como ideias extremistas, vazamentos de privacidade, danos à saúde física e mental, e dependência ou vício.
**Fontes:**
- [S2] South China Morning Post — https://www.scmp.com/tech/big-tech/article/3359482/bytedance-and-alibaba-disable-humanlike-ai-custom-agents-new-rules-loom

## Sysdig — JadePuffer, primeiro ransomware operado de ponta a ponta por agente de IA
- A empresa de segurança em nuvem Sysdig identificou o que acredita ser a primeira operação de ransomware documentada conduzida inteiramente por um agente de modelo de linguagem grande (LLM).
- A operação, chamada JadePuffer, usou um agente de IA autônomo para reconhecimento do alvo, roubo de credenciais, movimentação lateral, persistência, escalonamento de privilégios e criptografia de dados.
- O agente de IA se adaptou a falhas em tempo real, de forma semelhante a um operador humano.
- Em uma sequência, o agente passou de um login falho a uma correção funcional em 31 segundos.
- O acesso inicial foi obtido explorando a CVE-2025-3248, uma falha de execução remota de código não autenticada no Langflow, um framework de código aberto para construir aplicativos de LLM.
- O fornecedor corrigiu a falha em 1º de abril de 2025.
- No início de maio de 2025, a CISA (agência de cibersegurança dos EUA) marcou a falha como explorada em ataques.
- O agente criptografou 1.342 itens de configuração de serviço do Nacos usando a função AES_ENCRYPT() do MySQL.
- O agente apagou as tabelas de configuração originais.
- O agente criou uma tabela de extorsão contendo a exigência, um endereço de Bitcoin e um contato de Proton Mail.
- A Sysdig conclui que a era dos "agentes maliciosos autônomos" (ATAs) chegou, reduzindo o nível de habilidade necessário para conduzir ciberataques danosos.
- Payloads gerados por LLM também criam novas oportunidades de detecção.
- O endereço de Bitcoin no bilhete de resgate era um endereço de exemplo amplamente usado em documentação pública, provavelmente reproduzido pelo LLM a partir de seus dados de treinamento.
- A chave de criptografia, gerada aleatoriamente, nunca foi armazenada nem transmitida ao atacante.
**Fontes:**
- [S3] BleepingComputer — https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/

## Nvidia — adiamento do rack de IA Kyber NVL144 para 2028
- A arquitetura de rack Kyber da Nvidia, projetada para abrigar seus chips Rubin Ultra de 2027, foi adiada em mais de 12 meses, para 2028.
- O adiamento foi reportado pela empresa de pesquisa SemiAnalysis em post publicado na segunda-feira, 6 de julho.
- O revés decorre da dificuldade de fabricar um "midplane", placa de circuito impresso (PCB) multicamadas especializada no centro do sistema.
- Segundo a SemiAnalysis, o midplane "permanece desafiador do ponto de vista da manufaturabilidade".
- O midplane é composto por 78 camadas e é altamente propenso a defeitos.
- A configuração maior, NVL576 (576 GPUs), também enfrenta problemas de fabricação.
- O Kyber reúne 144 dos chips mais potentes da Nvidia em uma única unidade de rack.
- O Kyber estava previsto para estrear com o sistema Vera Rubin Ultra em 2027.
- Um plano alternativo de unir dois racks da geração atual (NVL72x2) foi descartado.
- Provedores de nuvem e hyperscalers rejeitaram esse design por considerá-lo desajeitado e caro de operar.
**Fontes:**
- [S4] Longbridge — https://longbridge.com/news/291749554
- [S5] Techzine — https://www.techzine.eu/news/devices/142682/ambitious-nvidia-roadmap-hits-snag-as-kyber-pushed-to-2028/
- [S6] CNBC — https://www.cnbc.com/2026/07/06/nvidia-kyber-rack-system-delays-manufacturing-taiwan-rubin-chips-.html

## SK Hynix — venda de ações de ~US$28 bilhões para listagem na Nasdaq
- A SK Hynix lançou na segunda-feira, 6 de julho, uma venda de ações nos EUA para levantar 43 trilhões de wons (cerca de US$28,07 bilhões).
- A oferta atraiu indicações de interesse de até US$7 bilhões de grandes investidores.
- A empresa emitirá até 17.790.000 novas ações ordinárias, cerca de 2,50% de suas ações em circulação.
- A SK Hynix pretende listar os ADSs (American Depositary Shares, títulos que representam ações estrangeiras negociados nos EUA) no Nasdaq Global Select Market sob o símbolo "SKHY".
- Com valor aproximado de US$28-29 bilhões, a operação pode ser a maior venda inaugural de ações já feita por uma empresa estrangeira.
- A operação superaria a estreia de US$21,8 bilhões do Alibaba em Nova York em 2014.
- A SK Hynix planeja listar seus ADRs na Nasdaq em 10 de julho.
- Os recursos financiarão uma fábrica de chips, uma fábrica de empacotamento avançado na Coreia do Sul e equipamentos de fabricação de chips, como um scanner EUV (litografia ultravioleta extrema).
- BofA Securities, Citigroup Global Markets, Goldman Sachs e JP Morgan Securities coordenam a oferta.
**Fontes:**
- [S7] MarketScreener (Reuters) — https://uk.marketscreener.com/news/sk-hynix-launches-28-billion-us-listing-draws-7-billion-in-investor-interest-ce7f5edad088f022
- [S8] SEC (SK hynix Form F-1) — https://www.sec.gov/Archives/edgar/data/2120882/000119312526280172/d32785df1.htm
- [S9] Fortune — https://fortune.com/2026/07/05/sk-hynix-us-stock-listing-nasdaq-29-billion-micron-ai-boom-chips/
- [S10] Yonhap News Agency — https://en.yna.co.kr/view/AEN20260624010451320
- [S11] Nikkei Asia — https://asia.nikkei.com/business/markets/equities/sk-hynix-eyes-raising-up-to-29bn-in-nasdaq-adr-listing

## Biren Technology — captação de ~US$892 milhões em colocação de ações H
- A fabricante de chips de IA Biren Technology, sediada em Xangai, anunciou sua primeira colocação de ações na segunda-feira, 6 de julho.
- A Biren emitirá 153 milhões de novas ações H a HK$46,2 cada.
- A operação deve levantar quase HK$7,07 bilhões (cerca de US$892,5 milhões) em recursos brutos.
- O preço da colocação representa um desconto de cerca de 9,94% em relação ao fechamento da sexta-feira anterior.
- A colocação corresponde a aproximadamente 11,3% do capital ampliado em ações H.
- Cerca de 60% dos recursos líquidos serão usados para acelerar a comercialização e produção de produtos de próxima geração.
- Cerca de 20% serão destinados a P&D.
- Cerca de 10% irão para investimentos estratégicos e aquisições.
- Cerca de 10% serão usados para capital de giro e fins corporativos gerais.
- A Biren, que se posiciona para desafiar a Nvidia, estreou na Bolsa de Valores de Hong Kong no início de janeiro de 2026.
- A ação da Biren subiu mais de 150% desde o IPO (oferta pública inicial).
- A Biren disse que novas necessidades de financiamento surgiram desde a listagem, devido à adoção acelerada de mercado, à expansão de programas de pré-pesquisa e a maiores compromissos de comercialização de curto prazo não totalmente previstos na época do IPO.
**Fontes:**
- [S12] The Standard — https://www.thestandard.com.hk/finance/article/336455/Biren-Technology-plans-to-raise-nearly-707-billion-through-first-placing
- [S13] South China Morning Post — https://www.scmp.com/tech/tech-trends/article/3359528/chinas-biren-seeks-us900m-fund-gpu-push-and-challenge-nvidia-amid-ai-boom
- [S14] The Next Web — https://thenextweb.com/news/biren-892m-gpu-raise-nvidia-china
- [S15] Techmeme — https://www.techmeme.com/260706/p2

## Even Realities — US$150 milhões e avaliação de US$1 bilhão para óculos inteligentes sem câmera
- A Even Realities, startup de três anos com sede em Shenzhen, levantou US$150 milhões em uma rodada pré-Série B.
- A rodada foi liderada pela Meituan e pela investidora anterior Tencent.
- A rodada avaliou a startup em US$1 bilhão.
- Fundada em 2023 por ex-engenheiros da Apple, a empresa fabrica óculos inteligentes sem câmera, com foco em display, que projetam informações no campo de visão do usuário.
- A empresa se posiciona contra rivais equipados com câmera, como os Ray-Ban da Meta, em bases de privacidade.
- Mais da metade dos usuários da Even Realities está nos Estados Unidos.
- Cerca de 80% de sua comunidade de desenvolvedores está nos Estados Unidos.
- A rodada eleva o financiamento total a mais de US$160 milhões.
- Investidores anteriores incluem Hillhouse, Sequoia China e Northern Light Venture Capital.
- O primeiro produto da empresa, o G1, foi lançado em 2024 com óptica de guia de onda (waveguide).
**Fontes:**
- [S16] TechCrunch — https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/
- [S17] Tech Funding News — https://techfundingnews.com/even-realities-1b-valuation-camera-free-glasses/
- [S18] Mezha — https://mezha.net/eng/bukvy/05e1a7ae_even_realities_raised/

## Aylight — 4,5 milhões de euros para interconexões ópticas em data centers de IA
- A startup suíça de deeptech Aylight, sediada em Zurique, fechou uma rodada pré-seed de 4,5 milhões de euros.
- A empresa desenvolve lasers multicomprimento de onda em escala de chip para interconexões ópticas em data centers de IA e sensoriamento FMCW.
- A rodada foi coliderada pela Elaia e pela Swisscom Ventures.
- Verve Ventures e Plug and Play participaram da rodada.
- A tecnologia da Aylight gera múltiplos comprimentos de onda com espaçamento preciso a partir de um único chip, reduzindo a necessidade de vários lasers discretos.
- A tecnologia foi projetada para ser fabricada em foundries de fotônica de semicondutores já existentes.
- A Aylight foi fundada em 2025 por Bahareh Marzban e Dmitry Kazakov, após pesquisa na ETH Zurich.
- O financiamento apoiará seus primeiros protótipos em foundry de semicondutores.
**Fontes:**
- [S19] Tech.eu — https://tech.eu/2026/07/06/aylight-closes-eur45m-pre-seed-round-to-advance-optical-interconnect-technology/

## Rússia — segundo ataque com mísseis balísticos a Kiev em uma semana
- A Rússia lançou 419 armas de ataque aéreo contra a Ucrânia na noite de 5 para 6 de julho.
- Foram 68 mísseis e 351 drones.
- Kiev foi o principal alvo do ataque.
- 29 mísseis balísticos (incluindo mísseis antinavio) atingiram 34 localidades.
- Nenhum dos mísseis balísticos foi abatido.
- Até as 8h30, as defesas aéreas ucranianas haviam abatido ou neutralizado 363 alvos — 37 mísseis e 326 drones.
- A ABC News relatou ao menos 14 mortos em Kiev e na região vizinha, com cerca de 60 feridos.
- A LIGA relatou 11 mortos apenas em Kiev.
- Foi o segundo ataque russo a Kiev em menos de uma semana.
- O ataque anterior, na semana passada, matou mais de 30 pessoas.
- O ataque ocorreu na véspera de uma cúpula da OTAN em Ancara.
- Zelensky pediu que a OTAN tome "decisões firmes" sobre defesas aéreas.
- Autoridades disseram que a Ucrânia tem interceptadores insuficientes para deter os mísseis balísticos, que a Rússia vem explorando cada vez mais.
**Fontes:**
- [S20] ABC News — https://www.abc.net.au/news/2026-07-06/russian-attack-on-kyiv-ukraine-kills-14-on-eve-of-nato-summit/106886188
- [S21] LIGA.net — https://news.liga.net/en/war/news/the-russians-launched-68-missiles-and-351-drones-at-ukraine-none-of-the-29-ballistic-missiles-were-shot-down
- [S22] RBC-Ukraine — https://newsukraine.rbc.ua/news/ballistic-missiles-and-zircons-got-through-1783320438.html

## Cúpula da OTAN em Ancara — Trump e Zelensky, pressão por gastos de defesa de 5%
- A Casa Branca informou em 5 de julho que Trump terá reuniões bilaterais com o presidente ucraniano Zelensky e o presidente sírio Ahmed al-Sharaa.
- As reuniões ocorrerão à margem da cúpula da OTAN em Ancara, na quarta-feira.
- Trump parte de Washington na noite de segunda-feira e chega a Ancara na terça-feira à tarde para encontrar Erdogan.
- Na quarta-feira, Trump participa da recepção oficial, da foto de família e da sessão de trabalho dos líderes da OTAN antes das bilaterais.
- O embaixador dos EUA na OTAN, Matt Whitaker, disse que Trump "espera plenamente que todos os aliados avancem imediatamente e entrem no caminho dos 5%" de gastos com defesa.
- A declaração busca fazer valer o compromisso assumido no ano passado.
- Trump conversou por telefone com Zelensky e Putin em 4 de julho.
- Um funcionário dos EUA disse que Trump faria um "acompanhamento" com Putin depois de se reunir com Zelensky sobre o fim da guerra.
- A cúpula ocorre enquanto Trump busca encerrar a guerra de quase quatro anos e meio.
- Espera-se que a guerra, em seu quinto ano, seja um foco central em Ancara.
**Fontes:**
- [S23] The Straits Times — https://www.straitstimes.com/world/united-states/trump-to-meet-leaders-of-ukraine-syria-alongside-nato-summit
- [S24] TRT World — https://www.trtworld.com/article/db44014e3885
- [S25] NPR — https://www.npr.org/2026/07/06/g-s1-132082/trump-nato-turkey-spending
- [S26] The Japan Times — https://www.japantimes.co.jp/news/2026/07/06/world/trump-nato-summit-zelenskyy-allies/

## OPEP+ — aumento de produção de agosto em 188 mil barris por dia
- Sete produtores da OPEP+ — Arábia Saudita, Rússia, Iraque, Kuwait, Cazaquistão, Argélia e Omã — concordaram em elevar a produção.
- O acordo foi fechado em reunião virtual de 5 de julho.
- O aumento combinado será de 188.000 barris por dia em agosto.
- É o quinto aumento mensal consecutivo.
- O movimento dá continuidade ao desmonte gradual dos cortes voluntários que o grupo anunciou pela primeira vez em 2023.
- O petróleo Brent era negociado abaixo de US$72 o barril na abertura dos mercados na noite de domingo — aproximadamente seu nível pré-guerra.
- O WTI estava perto de US$68 o barril.
- Ambos ficam bem abaixo dos picos de março, próximos de US$120.
- A produção total da OPEP+ caiu para 33,13 milhões de barris/dia em maio, ante 42,77 milhões em fevereiro, após o fechamento do Estreito de Ormuz.
- A oferta agora se recupera após o cessar-fogo entre EUA e Irã.
- Os produtores disseram manter total flexibilidade para pausar ou reverter os aumentos.
- Os sete países têm nova reunião marcada para 2 de agosto de 2026.
**Fontes:**
- [S27] Al Jazeera — https://www.aljazeera.com/economy/2026/7/6/opec-countries-say-they-will-expand-monthly-oil-production
- [S28] Euronews — https://www.euronews.com/business/2026/07/06/opec-agrees-another-modest-output-rise-as-oil-prices-fall-back-to-pre-war-levels
- [S29] The Economic Times — https://economictimes.indiatimes.com/news/international/world-news/opec-adjusts-august-production-reaffirms-stability-commitment-next-meet-august-2/articleshow/132193931.cms

## Incêndios florestais na Europa — 17 mil hectares queimados em meio a onda de calor
- Incêndios florestais devastaram mais de 17.000 hectares na França, Espanha e Portugal.
- As temperaturas em alguns locais deveriam chegar a 40°C em 5 de julho.
- A onda de calor deveria avançar para o norte na segunda-feira.
- Na região de Vouzela, no centro de Portugal, mais de 1.200 bombeiros combateram um incêndio que já havia queimado 12.000 hectares desde quinta-feira.
- A Espanha enviou 120 bombeiros.
- Itália e Espanha despacharam aviões de combate a incêndio.
- Os serviços de bombeiros da Grécia responderam a 60 incêndios florestais em um período de 24 horas.
- Um incêndio de rápido avanço perto de Thessaloniki disparou alertas de evacuação para três subúrbios.
- Nos EUA, ao menos 19 mortes em Nova Jersey foram suspeitas de estarem relacionadas ao calor.
- Cerca de 900.000 clientes de concessionárias ficaram sem energia quando tempestades severas se seguiram à cúpula de calor.
- A França registrou mais de 2.000 mortes acima do normal em apenas uma semana durante a onda de calor de junho.
- Espanha e Bélgica relataram, cada uma, mais de 1.000 mortes acima do normal.
**Fontes:**
- [S30] ABC News — https://www.abc.net.au/news/2026-07-05/europe-wildfires-forests-france-spain-greece-heatwave/106882460
- [S31] PBS NewsHour — https://www.pbs.org/newshour/world/wildfires-rage-in-portugal-greece-and-spain-while-greek-authorities-warn-of-toxic-smoke
- [S32] GreekReporter — https://greekreporter.com/2026/07/05/greece-sixty-wildfires-day/
- [S33] PBS NewsHour — https://www.pbs.org/newshour/nation/unbearable-heat-suspected-in-19-new-jersey-deaths-as-high-temperatures-give-way-to-thunderstorms

## Netanyahu — sem reconstrução de Gaza até desarmamento do Hamas
- Na reunião semanal do gabinete em 5 de julho, Netanyahu disse que "não haverá reconstrução em Gaza sem o desmantelamento e a desmilitarização da Faixa".
- As declarações responderam a um relato de que o governo dos EUA decidiu abandonar o desarmamento do Hamas como pré-condição formal para a reconstrução.
- Netanyahu não negou o relato.
- O plano dos EUA, anunciado no início deste ano, inclui a criação de um mecanismo de governança tecnocrática palestina para a Faixa.
- O plano prevê um arcabouço internacional para supervisionar a reconstrução.
- As Forças de Defesa de Israel (IDF) confirmaram que agora controlam cerca de 60% da Faixa de Gaza.
- É um aumento em relação aos 53% acordados no cessar-fogo do ano passado.
- A "Linha Amarela" foi movida mais para dentro do enclave.
**Fontes:**
- [S34] Ynetnews — https://www.ynetnews.com/article/sygh0rvqme
- [S35] ABC News — https://www.abc.net.au/news/2026-07-06/idf-controls-more-gaza-territory-as-israel-yellow-line-moves/106836640
- [S36] Al Arabiya — https://english.alarabiya.net/News/middle-east/2026/07/05/gaza-s-disarmament-a-prerequisite-for-reconstruction-netanyahu-says-

## Ripple — licença MiCA plena em Luxemburgo para serviços de cripto em 30 países do EEE
- A Ripple anunciou em 6 de julho que recebeu autorização plena de Provedor de Serviços de Criptoativos (CASP).
- A autorização foi concedida sob o regulamento MiCA (Markets in Crypto-Assets, o marco da UE para criptoativos) pela CSSF, o regulador financeiro de Luxemburgo.
- A licença permite que a Ripple ofereça serviços de custódia, transferência e câmbio a partir de Luxemburgo para todos os 30 países do Espaço Econômico Europeu (EEE), sem aprovação de cada regulador nacional.
- O EEE inclui os 27 estados-membros da UE mais Islândia, Noruega e Liechtenstein.
- A autorização vem após uma "Green Light Letter" (carta de luz verde) preliminar da CSSF em 23 de junho.
- O período de transição do MiCA expirou em 1º de julho, impedindo empresas não licenciadas de oferecer legalmente a maioria dos serviços regulados de cripto na UE.
- Combinada com sua licença de Instituição de Moeda Eletrônica da UE, a Ripple agora pode oferecer pagamentos em cripto de ponta a ponta a instituições europeias.
- A Ripple afirma deter mais de 75 licenças regulatórias globalmente.
**Fontes:**
- [S37] The Block — https://www.theblock.co/post/407207/ripple-secures-full-mica-casp-authorization-for-crypto-services-across-30-eea-countries
- [S38] BanklessTimes — https://www.banklesstimes.com/articles/2026/07/06/ripple-secures-luxembourg-casp-license-achieves-full-mica-compliance-across-eea/
- [S39] Coinpedia — https://coinpedia.org/news/xrp-news-ripple-receives-full-mica-casp-authorization-in-europe/

## MHRA — Retifanlimab, primeiro tratamento para câncer de pele de células de Merkel avançado
- Em 6 de julho, a MHRA (agência reguladora de medicamentos do Reino Unido) aprovou o Retifanlimab (ZYNYZ) como o primeiro tratamento para adultos com carcinoma de células de Merkel avançado.
- O tratamento é indicado para casos que se espalharam ou retornaram e não podem ser curados por cirurgia ou radioterapia.
- O Retifanlimab é uma imunoterapia que bloqueia uma via usada pelas células cancerígenas para escapar do sistema imunológico.
- O medicamento é administrado por infusão intravenosa diluída ao longo de 30 minutos.
- Em estudo com 101 adultos não tratados anteriormente, 53,5% responderam ao Retifanlimab.
- Desses, 16,8% ficaram sem sinais detectáveis de câncer.
- 36,6% apresentaram redução do tumor.
- As respostas normalmente duraram pouco mais de dois anos.
- A aprovação foi concedida à Incyte Biosciences UK Ltd por meio do Procedimento de Reconhecimento Internacional (IRP).
**Fontes:**
- [S40] GOV.UK (MHRA) — https://www.gov.uk/government/news/mhra-approvesretifanlimabzynyz-for-the-treatment-of-advanced-merkel-cell-skin-cancer
