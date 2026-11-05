# Fatos — Newsletter [Tech] 3 de Novembro de 2026

## Anthropic — S-1/A diz que limiar de P&D acelerado por IA pode ser atingido "iminentemente"
- A Anthropic protocolou na SEC (Securities and Exchange Commission, o regulador do mercado de capitais dos EUA) em 2 de novembro de 2026 uma versão emendada de seu S-1 (S-1/A), o prospecto de registro para o IPO (oferta pública inicial de ações).
- O S-1/A acrescenta um fator de risco segundo o qual estimativas internas e expectativas sobre modelos futuros indicam que a empresa "pode atingir iminentemente" a definição de "progresso dramaticamente acelerado atribuível à IA" de sua Responsible Scaling Policy (RSP, a política interna de escalonamento responsável).
- A indicação se refere a modelos futuros, não aos modelos atuais.
- A Anthropic diz que não designou nenhum de seus modelos atuais como acima desse limiar.
- A empresa diz que continua avaliando os dados subjacentes.
- O documento admite que, no passado, a Anthropic não identificou uma aceleração significativa em seu ritmo de desenvolvimento até depois que ela ocorreu.
- O documento diz que isso pode voltar a acontecer no futuro.
- A dificuldade se deve ao fato de as evidências da empresa virem em grande parte de indicadores defasados.
- A Anthropic diz que não prevê conseguir usar o Claude com segurança para projetar e construir, de forma totalmente autônoma, modelos de fronteira sucessivos sem supervisão humana significativa.
- A empresa considera atualizações da RSP para manter humanos no controle do desenvolvimento de modelos de fronteira na Anthropic.
- Pela versão 3.4 da RSP, em vigor desde 8 de julho de 2026, a rota de "aceleração dramática" é definida como observar ou esperar o dobro do ritmo de progresso nas capacidades agregadas de IA.
- Esse ritmo é medido ao longo de pelo menos três gerações de modelos e precisa ser atribuível a pesquisa automatizada.
- Em relação ao S-1 de outubro, a emenda muda o tempo verbal do trecho sobre acelerações não detectadas.
- A emenda acrescenta que a Anthropic avalia exigir revisão humana de certas decisões de pesquisa.
**Fontes:**
- [S1] TechCrunch — https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/
- [S2] Idlen — https://www.idlen.io/news/anthropic-s1-recursive-self-improvement-rsp-threshold-ai-rd/
- [S3] Gattyworks — https://gattyworks.com/news/anthropic-s1a-imminent-rsp-acceleration-threshold

## Anthropic — números do terceiro trimestre no S-1/A e valuation do IPO
- O S-1 emendado da Anthropic mostra receita de cerca de US$17 bilhões no terceiro trimestre de 2026.
- A receita cresceu cerca de 1.127% na comparação anual.
- O crescimento sequencial desacelerou para cerca de 47% no terceiro trimestre, ante 144% no segundo trimestre.
- O prejuízo líquido do terceiro trimestre foi de US$23,3 bilhões, ante US$12,1 bilhões um ano antes.
- O prejuízo líquido inclui uma perda não caixa de US$21,9 bilhões por ajuste no valor justo de notas conversíveis.
- As despesas operacionais subiram 292%, para US$17,5 bilhões.
- A Anthropic passou a um prejuízo operacional de US$567 milhões no terceiro trimestre, depois de um lucro operacional de US$974 milhões no segundo trimestre.
- O prejuízo operacional veio principalmente de US$5 bilhões em poder computacional comprado sob compromissos de curto prazo, a preços mais altos.
- Também pesaram US$2 bilhões em encargos não caixa de um programa de contrapartida de doações.
- Cortes de preço (incluindo o do Opus 5.5) e descontos reduziram o crescimento da receita do terceiro trimestre em cerca de US$600 milhões.
- A Anthropic divulgou compromissos de compra e contratos de arrendamento de cerca de US$895,4 bilhões.
- Praticamente todos esses compromissos se referem a poder computacional e infraestrutura.
- Cerca de US$70 bilhões dos compromissos vencem no ano até setembro de 2027.
- Cerca de US$448 bilhões devem ser incorridos antes do fim de 2030.
- O documento estima que de 5% a 7% da receita de nove meses veio de clientes que violaram as regras de uso ou os termos comerciais da empresa.
- A Anthropic alerta que a repressão a essas violações pode reduzir o crescimento futuro da receita.
- Segundo o Wall Street Journal, investidores institucionais disseram à Anthropic que o valuation no IPO deveria ficar entre cerca de US$1,5 trilhão e US$1,6 trilhão.
- Esses valores ficam abaixo dos cerca de US$2 trilhões que vinham sendo cogitados.
- A recomendação veio após a liquidação de ações de tecnologia da semana passada.
- O IPO está planejado para ainda este mês.
- A Anthropic planeja listar suas ações na Nasdaq sob o ticker ANT.
- O roadshow (rodada de apresentações a investidores) pode começar já na próxima semana.
**Fontes:**
- [S4] CNBC — https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html
- [S5] The Economic Times (Bloomberg) — https://economictimes.indiatimes.com/markets/us-stocks/news/anthropic-revenue-up-12x-in-q3-commits-895-billion-spending/articleshow/135478994.cms
- [S6] Yahoo Finance (Euronews) — https://finance.yahoo.com/technology/ai/articles/anthropic-swings-back-operating-loss-132419900.html
- [S7] Wall Street Journal — https://www.wsj.com/finance/stocks/anthropic-investors-push-for-cautious-valuation-closer-to-1-5-trillion-2f2df9cf

## Weight-Space Programming — GPT-6 Astra edita pesos do Qwen e melhora desempenho em matemática
- Pesquisadores, entre eles Omar Khattab, do MIT, publicaram o trabalho "Sparks of Weight-Space Programming".
- O trabalho argumenta que LLMs (grandes modelos de linguagem) conseguem ler e escrever pesos de redes neurais de forma nativa, sem treinamento baseado em gradiente.
- Os pesquisadores pediram ao GPT-6 Astra que tornasse o Qwen3.5-0.8B melhor em matemática.
- O GPT-6 Astra rastreou os loops de raciocínio do Qwen3.5-0.8B até uma única direção escrita pelos MLPs (perceptrons multicamadas) das camadas 15 e 19.
- O Astra subtraiu essa direção de 131.072 pesos, o equivalente a 0,016% do modelo.
- Com 50 forward passes (passagens diretas pelo modelo), o resultado no MATH-500 subiu de 7,9% para 48,1%.
- O resultado no GSM8K subiu de 13,8% para 67,1%.
- O resultado no IFEval, que mede seguimento de instruções, subiu de 21,0% para 62,3%.
- A fatia de respostas que atingiam o limite de tokens caiu de 93% para 33,1%.
- O Astra trabalhou por meio de um kernel Python rodando apenas em CPU sobre os pesos.
- O processo não usou gradiente descendente, acesso à internet nem acesso aos benchmarks de avaliação.
- Uma nova execução independente do checkpoint editado e publicado, no MATH-500 completo, marcou 51,0%.
- Os autores dizem que estão construindo um benchmark e um harness (ambiente de execução) para que LLMs explorem e escrevam pesos.
**Fontes:**
- [S8] Rikiya Takehi et al. (blog) — https://rikiyat.github.io/blog/weight-space-programming/
- [S9] VentureBeat — https://venturebeat.com/technology/like-gene-editing-for-neural-networks-mit-researchers-used-gpt-6-astra-to-edit-qwens-open-weights-directly-boosting-math-performance
- [S10] Hugging Face — https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming
- [S11] X — https://x.com/rikiyatakehi/status/2117313812768665832

## Salesforce — compra da Cresta, de IA de voz para atendimento
- A Salesforce anunciou em 2 de novembro de 2026 um acordo definitivo para adquirir a Cresta.
- A Cresta faz agentes de voz que resolvem ligações complexas de clientes de ponta a ponta.
- Os agentes da Cresta também orientam atendentes humanos em tempo real.
- A Salesforce não divulgou os termos do negócio.
- O The Information reportou o preço de US$2,7 bilhões.
- Entre os clientes da Cresta estão Marriott, Comcast e Alaska Airlines.
- O fechamento é esperado no primeiro trimestre do ano fiscal de 2028 da Salesforce, sujeito a aprovações regulatórias.
- Após o fechamento, a Cresta continuará dando suporte a plataformas de contact center e de telefonia concorrentes.
- Em 2026, a Salesforce concluiu a compra da Fin, por cerca de US$3,6 bilhões.
- Em 2026, a Salesforce também acertou a compra da Braze, por cerca de US$5,66 bilhões.
- A aquisição da Cresta estende a investida da Salesforce do suporte digital para as ligações telefônicas.
- Kishan Chetan, EVP (vice-presidente executivo) de Agentforce e Service Cloud, disse que a voz é "onde o atendimento é mais difícil de acertar e onde mais importa para os clientes".
**Fontes:**
- [S12] Salesforce — https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-cresta/
- [S13] The Information — https://www.theinformation.com/briefings/exclusive-salesforce-acquires-startup-cresta-2-7-billion
- [S14] CMSWire — https://www.cmswire.com/contact-center/salesforce-adds-cresta-to-the-cart-in-its-2026-cx-shopping-spree-01/
- [S15] Dealroom News — https://dealroom.co/news/168989-salesforce-to-buy-voice-ai-startup-cresta-for-2-7b/

## China — NDRC promete acelerar legislação de IA e padrões de segurança para todo o ciclo de vida
- Em entrevista coletiva em 3 de novembro, Wang Ruomeng, vice-diretor do Departamento de Inovação e Desenvolvimento de Alta Tecnologia da NDRC (Comissão Nacional de Desenvolvimento e Reforma, órgão de planejamento econômico da China), disse que o país vai acelerar uma legislação de IA fundamental e abrangente.
- Wang disse que a China vai construir um sistema de leis e regulamentos de IA durante o 15º Plano Quinquenal.
- Wang disse que a China vai estabelecer padrões de segurança e diretrizes éticas que cubram todo o ciclo de vida da IA.
- Os padrões vão se estender a dados, poder computacional e algoritmos.
- Haverá revisões periódicas para ajustar as regras à rápida iteração da IA.
- A Bloomberg descreveu o plano como algumas das diretrizes mais abrangentes para evitar a perda de controle sobre uma IA cada vez mais poderosa.
- O esforço envolveria grandes desenvolvedores, como DeepSeek, Moonshot AI e Alibaba.
- Essas empresas concorrem com OpenAI e Anthropic.
**Fontes:**
- [S16] Bloomberg — https://news.bloomberglaw.com/artificial-intelligence/china-plans-broad-ai-guardrails-after-global-security-lapses
- [S17] Xinhua Finance (cnfin.com) — https://www.cnfin.com/hg-lb/detail/20261103/4490167_1.html
- [S18] TokenPost — https://www.tokenpost.com/news/regulation/47487

## Trajectory — Série A de US$45 milhões liderada pela Sequoia
- A Trajectory levantou US$45 milhões em uma rodada Série A, com valuation de US$300 milhões.
- A rodada foi liderada pela Sequoia.
- Nvidia, Bessemer Venture Partners e Bain Capital Ventures participaram da rodada.
- A startup tem 18 pessoas.
- A Trajectory foi fundada há cerca de um ano por três colegas de Stanford com passagem pelo Google DeepMind e pela Apple.
- A plataforma permite que especialistas não técnicos façam o pós-treinamento de modelos open source a partir de feedback (aprendizado contínuo).
- Harvey e Rogo usam a Trajectory para fazer o pós-treinamento de modelos open source.
- Outros clientes incluem Decagon, Mercor e Nvidia.
- A plataforma agora está disponível ao público.
- O cofundador Ronak Malde estava entre os pesquisadores da Windsurf contratados pelo Google DeepMind em um acqui-hire (aquisição feita para absorver a equipe).
- Entre os concorrentes da Trajectory estão Thinking Machines Lab, Applied Compute e Prime Intellect.
- A Applied Compute recebeu valuation de US$3,25 bilhões no mês passado.
- A Trajectory abriu uma lista de espera para a plataforma no dia do lançamento.
**Fontes:**
- [S19] TechCrunch — https://techcrunch.com/2026/11/02/trajectory-raises-45m-to-make-ai-model-training-accessible-to-nontechnical-experts/
- [S20] X — https://x.com/rronak_/status/2117361749586489360

## OpenAI — ChatGPT une abas Chat e Work; ChatGPT e Codex passam a dividir limite de uso
- A OpenAI informou usuários por e-mail que vai unir as abas Chat e Work no app desktop do ChatGPT.
- A mudança chega primeiro a usuários selecionados, para coleta de feedback, antes de uma distribuição ampla.
- Segundo o e-mail, os usuários poderão trazer arquivos e plugins.
- Segundo o e-mail, os usuários poderão pedir ao ChatGPT que crie sites, monte apresentações ou execute tarefas na web.
- O Codex continua como uma experiência separada no app desktop do ChatGPT.
- ChatGPT e Codex vão consumir tokens do mesmo limite de uso.
- A OpenAI diz que, dependendo do uso e do modelo, alguns usuários podem ter de esperar a renovação do limite com mais frequência.
- A rival Anthropic uniu as funções de chat e Cowork do Claude em uma só tela em setembro.
**Fontes:**
- [S21] TechCrunch — https://techcrunch.com/2026/11/02/openai-is-finally-merging-chatgpts-chat-and-work-tabs/

## Nvidia — clientes de nuvem devem vender ao menos 51% a empresas não chinesas, diz FT
- A Nvidia disse a clientes de computação em nuvem que eles devem vender pelo menos 51% de seus serviços a empresas não chinesas, segundo o Financial Times.
- O Financial Times cita cinco pessoas a par do assunto.
- Antes não havia restrição desse tipo.
- A instrução foi passada verbalmente pela equipe de vendas e pelos times regionais da Nvidia, e não por escrito.
- A regra vale para clientes da Nvidia no mundo todo, não apenas na Ásia.
- A regra abrange apenas contratos futuros, não os arrendamentos já existentes.
- Um rack de chips B300 da Nvidia, que custa cerca de US$600 mil no mercado internacional, foi negociado na China no mês passado por 18,5 milhões de yuans (cerca de US$2,8 milhões), por causa da escassez.
- Neste ano, a Nvidia já havia cortado em mais da metade o número de clientes asiáticos autorizados a comprar seus chips de IA.
- Esse corte veio após a Nvidia montar uma lista de empresas aprovadas em revisões de compliance mais rigorosas.
- Uma provedora de nuvem sediada em Singapura disse que é difícil encontrar clientes não chineses suficientes fora dos EUA.
- A mesma provedora disse que uma aplicação estrita da regra prejudicaria seus negócios.
- A Nvidia não confirmou nem negou a reportagem à AFP.
- Em nota, a Nvidia disse que "data centers e nuvens construídos com chips americanos são a base de que os desenvolvedores americanos de modelos e aplicativos precisam para competir no mundo todo".
- A porta-voz do Ministério das Relações Exteriores da China, Mao Ning, disse não ter conhecimento da reportagem.
**Fontes:**
- [S22] Investing.com — https://www.investing.com/news/stock-market-news/nvidia-tells-data-center-partners-to-limit-china-sales-ft-4993618
- [S23] Seoul Economic Daily — https://en.sedaily.com/international/2026/11/03/nvidia-tells-cloud-clients-51-percent-of-capacity-must-go
- [S24] The Times of India — https://timesofindia.indiatimes.com/technology/tech-news/nvidia-tells-data-centre-clients-to-sell-majority-of-services-to-non-chinese-buyers-company-says-datacenters-and-clouds-built-on-american-chips-are-the-foundation-/articleshow/135494554.cms
- [S25] AFP (via Iraqi News) — https://www.iraqinews.com/tech/nvidia-orders-data-center-clients-to-reduce-china-exposure-ft/

## HBM — contrabando de memória da Samsung e SK Hynix para a China; Ascend 960DT da Huawei depende dela
- Contrabandistas montam HBM (memória de alta largura de banda, usada em chips de IA) da Samsung e da SK Hynix, sujeita a controle de exportação, em placas com processadores de servidor baratos e de baixo desempenho, segundo o The Information.
- O esquema funciona porque as regras de exportação dos EUA avaliam o poder computacional de um pacote pelo processador, e não pela memória.
- Em oficinas de Shenzhen, técnicos aquecem as placas para derreter a solda, retiram as pilhas de memória e descartam os processadores.
- A taxa de falha desse processo é alta.
- Segundo um intermediário chinês, uma unidade de HBM3E custa hoje cerca de US$4.000 na China.
- Há um ano, a mesma unidade custava algumas centenas de dólares.
- Com 6 a 8 pilhas de HBM por chip de IA, só a memória custa de US$24.000 a US$32.000.
- A Huawei disse a alguns clientes que seu próximo chip de IA topo de linha, o Ascend 960DT, usará em grande parte HBM da Samsung e da SK Hynix.
- A Huawei orientou alguns clientes a obter a memória por conta própria.
- O Ascend 960DT é esperado para o primeiro trimestre de 2027.
- O Ascend 960DT deve ter o dobro da largura de banda e da capacidade de memória do chip atual da Huawei.
- O rendimento de produção (fatia de chips aproveitáveis) do HBM3E da CXMT seria de apenas 20% a 30%, segundo relatos.
- O rendimento da SK Hynix é de cerca de 70%.
- A SK Hynix disse que cumpre rigorosamente os controles de exportação dos EUA e da Coreia do Sul.
- A SK Hynix disse que não fornece à Huawei desde o início das restrições americanas, em 2020.
**Fontes:**
- [S26] Tom's Hardware — https://www.tomshardware.com/tech-industry/semiconductors/ai-chip-smugglers-exploit-trade-control-loophole-to-bring-banned-hbm-from-south-korea-into-china-expensive-memory-chips-packaged-with-cheap-unsanctioned-processors-to-become-legal-exports
- [S27] Businesskorea — https://www.businesskorea.co.kr/news/articleView.html?idxno=280371
- [S28] TrendForce — https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/

## Samsung — base dies de HBM para AMD e Nvidia na segunda fábrica de Taylor, no Texas
- A Samsung vai usar sua segunda fábrica de foundry (fabricação de chips sob encomenda) em Taylor, no Texas, para produzir base dies de HBM (o chip lógico na base da pilha de memória) para AMD e Nvidia, segundo o Maeil Business Newspaper.
- A reportagem do Maeil, de 3 de novembro, cita fontes do setor.
- A Samsung não quis comentar.
- A construção da fábrica deve começar formalmente neste mês.
- A fábrica já tem encomendas para toda a produção.
- A maior parte do volume encomendado é da AMD.
- A fábrica usará tecnologia de 2nm.
- A fábrica terá cerca de 2,7 milhões de pés quadrados.
- A área é cerca de 1,5 vez a da primeira fábrica da Samsung em Taylor.
- A primeira fábrica de Taylor tem contrato com a Tesla.
- A instalação de equipamentos está prevista a partir de fevereiro de 2029.
- A produção em massa está prevista para 2030.
- Os base dies feitos em Taylor seriam combinados com dies de núcleo DRAM fabricados na Coreia do Sul.
- A Broadcom, que faz chips de IA para Google, OpenAI e Anthropic, também pode ser cliente, segundo o Maeil.
- Há um risco para a Samsung: no padrão NVHBM proposto pela Nvidia, esperado para o HBM4E, a TSMC faria todos os base dies.
- Segundo a Nvidia, o desenho do NVHBM pode aumentar a largura de banda de memória em 30% e reduzir o consumo de energia do HBM em 15%.
**Fontes:**
- [S29] Reuters (via Investing.com) — https://www.investing.com/news/stock-market-news/samsung-to-make-amd-nvidia-chip-parts-at-second-texas-plant-maeil-business-reports-4994213
- [S30] Maeil Business Newspaper — https://www.mk.co.kr/en/business/12195087

## Agility Robotics — acionistas da Churchill Capital XI aprovam SPAC de US$2,5 bilhões
- Mais de 84% dos votos na assembleia especial de acionistas da Churchill Capital Corp XI, em 2 de novembro, aprovaram a fusão com a Agility Robotics.
- A Churchill Capital Corp XI é uma SPAC (empresa de aquisição com propósito específico, veículo listado em bolsa criado para se fundir com uma empresa de capital fechado).
- A Agility Robotics fabrica robôs humanoides.
- O fechamento da operação é esperado em 4 de novembro.
- A empresa combinada deve começar a ser negociada na Nasdaq em 5 de novembro, sob o ticker AGLT.
- As ações da Churchill fecharam em alta de quase 14% em 2 de novembro.
- A transação dá à Agility cerca de US$465 milhões em capital bruto, antes de despesas.
- A operação avalia a Agility em US$2,5 bilhões pre-money (antes do novo aporte).
- Os acionistas existentes da Agility transferem sua participação para a empresa combinada.
- Os robôs Digit operam em 9 ambientes de clientes, entre eles instalações da GXO.
- A Agility afirma ter mais de US$300 milhões em encomendas plurianuais firmes do Digit 5.
- A disponibilidade geral do Digit 5 está prevista para o fim de 2027.
**Fontes:**
- [S31] The Robot Report — https://www.therobotreport.com/agility-robotics-shareholders-approve-25b-humanoid-spac/

## Tutor Intelligence — Série B de US$75 milhões liderada pela a16z
- A Tutor Intelligence, fabricante de robôs para armazéns, levantou US$75 milhões em uma rodada Série B liderada pela a16z (Andreessen Horowitz).
- USV e Neo participaram da rodada.
- O anúncio foi feito pelo CEO, Josh Gruenstein, em 2 de novembro.
- A rodada eleva o financiamento total da Tutor para US$117 milhões.
- Os robôs da Tutor fazem tarefas de separação de itens (picking), reboque e empilhamento.
- Os robôs são guiados por operadores humanos remotos.
- O trabalho dos operadores gera dados que atualizam modelos de base usados por toda a frota.
- A Tutor opera em quase 4 vezes mais locais do que há um ano.
- A empresa espera ter mais de 1.000 robôs sob contrato até o fim de 2027.
- O dinheiro vai para treinamento de modelos de fronteira, fabricação de robôs e implantação na indústria.
**Fontes:**
- [S32] X — https://x.com/joshgruenstein/status/2117286162146746434
- [S33] Forbes — https://www.forbes.com/sites/johnwerner/2026/11/02/tutor-intelligence-why-not-just-teach-the-robots-ourselves/

## Drax, Brookfield e Radiant — data center de IA de escala gigawatt na usina de Drax
- A Drax assinou um acordo com a Brookfield e com a Radiant, plataforma de infraestrutura de IA da Brookfield no Reino Unido, para desenvolver, entregar e operar um data center de IA no terreno da usina Drax Power Station, em North Yorkshire.
- O projeto mira mais de 1GW de capacidade.
- A Fase 1 prevê até 100MW em operação a partir do primeiro trimestre de 2028, com energia da rede.
- A Fase 2 busca mais 500MW de capacidade entre 2028 e 2031.
- Na Fase 2, o data center usaria a geração da própria usina behind the meter (fornecimento direto, sem passar pela rede), sob um PPA (contrato de compra de energia) de longo prazo.
- A Brookfield estima que o investimento total, incluindo chips, pode passar de £20 bilhões (cerca de US$27 bilhões).
- A Fase 1 soma um investimento inicial de £2,5 bilhões (cerca de US$3,4 bilhões).
- O investimento tem apoio da joint venture de infraestrutura de IA Brookfield-Qai.
- A Fase 1 ainda depende de aprovações de planejamento e regulatórias, da obtenção de um inquilino e de decisões finais de investimento.
- As ações da Drax subiram 8,8% no início do pregão de Londres em 3 de novembro.
- O Guardian observa que a usina de Drax é a mais poluente do Reino Unido.
- A usina pode vir a abastecer o maior data center do país.
**Fontes:**
- [S34] Drax Global — https://www.drax.com/news/strategic-partnership-for-gw-scale-data-centre/
- [S35] CNBC — https://www.cnbc.com/2026/11/03/brookfield-ai-data-center-yorkshire-drax.html
- [S36] The Guardian — https://www.theguardian.com/business/2026/nov/03/uk-drax-power-station-ai-datacentre

## Apple — custo de memória "sem precedentes" e estoque 154% maior
- O CEO da Apple, John Ternus, disse na teleconferência de resultados de 2 de novembro que "o que estamos vendo com o preço de memória agora é sem precedentes".
- Ternus disse que a Apple espera "custos de memória ainda mais altos" no trimestre de dezembro.
- Ternus disse que, depois de dezembro, a Apple espera que os custos de memória continuem subindo.
- A Apple projetou margem bruta de 45% a 46% para o trimestre de dezembro.
- A margem bruta do trimestre de setembro foi de 47,9%.
- A queda projetada na margem se deve em grande parte aos custos mais altos de memória.
- O estoque da Apple subiu para US$14,54 bilhões.
- O estoque cresceu 31,1% ante os US$11,09 bilhões do trimestre anterior.
- Na comparação anual, o estoque cresceu 154,3%, ante US$5,72 bilhões.
- A alta do estoque reflete a formação de reservas de memória pela Apple.
- As obrigações de compra de manufatura subiram US$33 bilhões do trimestre de junho para o de setembro, enquanto a Apple busca garantir suprimento.
- A Apple atribuiu as vendas fracas de iPad a restrições de oferta.
- A receita do iPad caiu 10%, para US$6,2 bilhões.
- Analistas esperavam receita de US$6,7 bilhões com o iPad.
- O COO, Sabih Khan, não descartou novos aumentos de preço nos aparelhos da Apple.
**Fontes:**
- [S37] TechCrunch — https://techcrunch.com/2026/11/02/apples-inventory-surges-154-as-memory-chip-costs-climb/

## EUA e Irã — ataque à Ilha de Qeshm na véspera das midterms; petróleo cai
- As Forças Armadas dos EUA lançaram ataques limitados contra alvos iranianos na Ilha de Qeshm, no Estreito de Hormuz, na segunda-feira, 2 de novembro.
- Autoridades americanas descreveram os ataques como defensivos.
- Os ataques ocorreram depois que a Guarda Revolucionária Islâmica do Irã (IRGC) disparou contra uma aeronave americana.
- A mídia estatal iraniana relatou explosões nas ilhas de Qeshm e Hengam e em Bandar Abbas, no continente.
- Diferentemente de momentos anteriores da guerra, os ataques não foram anunciados publicamente.
- Trump havia dito antes que os EUA não atacariam o Irã antes das eleições de meio de mandato (midterms).
- A IRGC disse ter derrubado dois drones americanos MQM-170 ao sul de Qeshm.
- A IRGC disse ter derrubado um drone americano MQ-9 a leste do Estreito de Hormuz.
- Foi o primeiro ataque à Ilha de Qeshm desde junho.
- A guerra começou em 28 de fevereiro, com ataques dos EUA e de Israel ao Irã.
- A guerra levou ao fechamento do Estreito de Hormuz.
- Horas antes dos ataques, Trump escreveu que um acordo "poderia acontecer" e que "o Irã quer um acordo o mais rápido possível".
- O negociador-chefe do Irã, o presidente do Parlamento, Mohammad Bagher Ghalibaf, disse na terça-feira que "a bola agora está com os EUA para evitar a guerra".
- Mediadores do Catar esperam retorno de negociadores dos EUA e do Irã sobre uma nova proposta em até 36 horas.
- O Catar disse que Doha trabalha "rumo a um acordo provisório".
- Na segunda-feira, o petróleo Brent fechou a US$104,77 por barril, queda de 7,6%.
- O petróleo WTI caiu 7,4%, para US$96,46, voltando a ficar abaixo de US$100.
- Foram as maiores quedas percentuais diárias dos dois referenciais desde 27 de julho.
- Após as notícias dos ataques, o Brent subiu 0,5%, para US$105,25, no início do pregão asiático.
**Fontes:**
- [S38] CBS News — https://www.cbsnews.com/news/u-s-strikes-iran-targets/
- [S39] AP News — https://apnews.com/article/iran-us-strikes-strait-hormuz-183b3d32d9bf5241f744abb917e6713e
- [S40] BBC — https://www.bbc.com/news/articles/cx240mrm3g8vo
- [S41] Al Jazeera — https://www.aljazeera.com/news/2026/11/3/us-hits-qeshm-island-pezeshkian-signals-more-diplomacy-iran-war-latest
- [S42] CBS News — https://www.cbsnews.com/live-updates/iran-war-us-trump-negotiations-midterms/
- [S43] FinanSignal — https://finansignal.com/markets/stock-market-today-nov-2-2026
- [S44] The National — https://www.thenationalnews.com/news/us/2026/11/03/us-strike-qeshm-iran-hormuz/

## Rússia e Ucrânia — ataque maciço à rede elétrica e negociações em Abu Dhabi
- Zelensky disse que a Rússia lançou 289 drones, 17 mísseis balísticos e 59 mísseis de cruzeiro na madrugada de terça-feira, 3 de novembro.
- Os ataques atingiram usinas e subestações de Odesa, no sul, a Rivne, no oeste da Ucrânia.
- A DTEK, maior geradora privada de energia da Ucrânia, disse que três de suas cinco usinas termelétricas foram tiradas de operação.
- Houve apagões em Kyiv e em pelo menos seis outras regiões.
- Um ataque a um hospital em Kharkiv feriu 73 pessoas e danificou o setor de cardiologia.
- Mais de 180 mil pessoas ficaram sem energia na região de Zhytomyr.
- A Rússia disse que a Ucrânia incendiou uma grande refinaria de petróleo em Yaroslavl.
- O prefeito de Moscou, Sergei Sobyanin, disse que quase 500 drones que se dirigiam à região da capital foram destruídos.
- O enviado americano Steve Witkoff disse que os EUA vão mediar conversas de nível técnico entre Ucrânia e Rússia em Abu Dhabi, em 10 e 11 de novembro.
- As conversas vão tratar de arranjos de segurança pós-guerra, desescalada e questões humanitárias.
- O Kremlin confirmou a participação de uma delegação russa liderada por Vladimir Medinsky, assessor de Putin.
- Witkoff disse que negociadores americanos vão se reunir nesta semana em Bruxelas com Reino Unido, França, Alemanha, União Europeia e Otan para discutir garantias de segurança para a Ucrânia.
- Um ataque russo a uma escola usada como ponto de distribuição de ajuda em Komyshuvakha, na região de Zaporizhzhia, matou pelo menos 31 pessoas.
- Quase 50 pessoas seguem desaparecidas após o ataque à escola.
- O ataque ocorreu depois do fim, no domingo, de uma rara trégua em Kherson.
**Fontes:**
- [S45] Reuters (via Investing.com) — https://www.investing.com/news/commodities-news/russian-strikes-knock-out-power-to-swathes-of-ukraine-kyiv-hits-russian-refinery-4994629
- [S46] Al Jazeera — https://www.aljazeera.com/news/2026/11/3/at-least-73-injured-as-russia-bombs-ukrainian-hospital-and-power-plants
- [S47] RTÉ News — https://www.rte.ie/news/2026/1103/1597730-ukraine/
- [S48] The Guardian — https://www.theguardian.com/world/2026/nov/03/ukraine-war-briefing-us-to-mediate-talks-with-kyiv-and-moscow-in-abu-dhabi-next-week-says-witkoff

## Austrália — banco central eleva juros a 4,85%, maior nível em 18 anos
- O RBA (Reserve Bank of Australia, o banco central australiano) elevou a meta da taxa básica (cash rate) em 25 pontos-base, para 4,85%, em 3 de novembro de 2026.
- A decisão foi dividida: seis membros votaram pela alta.
- Três membros votaram por manter a taxa em 4,60%.
- O RBA citou preços de combustíveis e commodities afetados pelo conflito no Oriente Médio.
- O RBA disse que o investimento ligado a IA está impulsionando a alta rápida dos preços de bens de tecnologia.
- A inflação agora não deve chegar ao teto da meta de 2% a 3% antes do fim de 2027.
- A nova projeção é cerca de três trimestres mais tarde que a anterior.
- É a quinta alta de juros de 2026.
- É a maior taxa desde o fim de 2008.
- O comunicado retirou a menção à disposição de subir mais os juros, presente em todos os comunicados desde junho.
- A presidente do RBA, Michele Bullock, disse: "Basicamente estamos preservando nossas opções".
- O valor dos imóveis nas grandes cidades australianas caiu 1,4% em outubro.
- A Canstar estima que um tomador com empréstimo de A$500.000 (cerca de US$325 mil) pode pagar cerca de A$77 (cerca de US$50) a mais por mês.
**Fontes:**
- [S49] Reserve Bank of Australia — https://www.rba.gov.au/media-releases/2026/mr-26-30.html
- [S50] ABC News — https://www.abc.net.au/news/2026-11-03/rba-lifts-interest-rates-november-2026-highest-rate-in-18-years/107340050
- [S51] The Straits Times — https://www.straitstimes.com/business/australian-central-bank-chief-signals-pause-after-split-decision-on-latest-rate-hike
- [S52] SBS News — https://www.sbs.com.au/news/live-blog/rba-november-2026-interest-rates-decision-live/f6csn2n1w

## NCSC — China e Rússia usarão ataques cibernéticos com IA de forma rotineira até 2028
- O NCSC (National Cyber Security Centre, o centro nacional de cibersegurança do Reino Unido), parte do GCHQ (agência britânica de inteligência de sinais), publicou em 3 de novembro sua Revisão Anual 2026, "The State of the Cyber Nation".
- O NCSC considera "altamente provável" que, até 2028, China, Rússia e outros Estados usem rotineiramente capacidades cibernéticas de IA para atingir objetivos geopolíticos.
- O NCSC considera altamente provável que, até 2028, malware movido a IA tenha sido usado em um ataque de ransomware contra a infraestrutura nacional crítica do Reino Unido.
- O relatório chama a China de "desafio cibernético mais sofisticado e persistente" enfrentado pelo Reino Unido.
- O relatório chama a Rússia de ameaça cibernética atualmente "mais audaciosa" ao Reino Unido.
- O NCSC diz ser quase certo que a IA vai atuar como multiplicador de força para atacantes habilidosos.
- Segundo o NCSC, a IA vai acelerar reconhecimento, descoberta de vulnerabilidades e desenvolvimento de exploits.
- O CEO do NCSC, Richard Horne, escreveu que a resiliência cibernética do Reino Unido "ainda não está onde deveria".
- Horne escreveu que a ameaça "cresceu mais rápido que nossas capacidades defensivas".
- Horne disse que o Irã ainda conduz operações cibernéticas maliciosas no mundo, inclusive contra o Reino Unido, apesar do conflito no Oriente Médio.
- Horne anunciou um novo National Exposure and Real-Time Vulnerability Centre, que usará IA para encontrar vulnerabilidades em infraestrutura crítica.
**Fontes:**
- [S53] NCSC — https://www.ncsc.gov.uk/speech/richard-hornes-speech-at-the-ncsc-annual-review-2026-launch
- [S54] NCSC — https://www.ncsc.gov.uk/collection/annual-review-2026/understanding-threat/cyber-threat-uk
- [S55] NCSC — https://www.ncsc.gov.uk/collection/annual-review-2026/understanding-threat/ai-impact-cyber-threat
- [S56] NCSC — https://www.ncsc.gov.uk/collection/annual-review-2026/foreword-ncsc-ceo

## SUSE — corte de cerca de 10% dos funcionários atribuído à IA
- Em memorando de segunda-feira visto pelo The Register, o CEO da SUSE, Dirk-Peter van Leeuwen, anunciou um corte de cerca de 10% da força de trabalho global da empresa.
- A SUSE é uma empresa de software open source com 1.900 funcionários.
- Van Leeuwen escreveu que "automação e IA estão mudando fundamentalmente a forma como empresas de software operam".
- Van Leeuwen escreveu que "a necessidade de algumas funções existentes diminuiu muito".
- Os funcionários afetados serão informados até 4 de novembro.
- O restante da empresa conhecerá a estratégia do ano fiscal de 2027 em 16 de novembro.
- A SUSE pertence à gestora sueca de private equity EQT.
- A EQT comprou a SUSE por US$2,5 bilhões em 2018.
- A EQT fechou novamente o capital da SUSE em 2023.
- Em setembro, a SUSE havia oferecido desligamento voluntário a funcionários.
**Fontes:**
- [S57] The Register — https://www.theregister.com/software/2026/11/02/suse-to-cut-one-in-ten-employees-because-of-ai/5306950

## Mercado Bitcoin — ataque de US$46 milhões e saques suspensos
- O Mercado Bitcoin, maior exchange de criptomoedas do Brasil, confirmou na segunda-feira, 2 de novembro, um incidente de segurança envolvendo cerca de US$46,3 milhões em ativos, segundo dados da Arkham.
- A exchange disse ter "identificado e contido rapidamente" o incidente no início da manhã.
- O Mercado Bitcoin suspendeu temporariamente depósitos e saques.
- A exchange disse que os clientes não foram afetados e que não houve vazamento de dados.
- O CEO da Tether, Paolo Ardoino, disse que a emissora de stablecoin (criptomoeda atrelada ao dólar) congelou mais de 4,5 milhões de USDT ligados ao incidente.
- O analista da Arkham Emmett Gallic disse que o atacante estava varrendo fundos de endereços de depósito antigos.
- Segundo Gallic, o atacante estava vendendo memecoins e outras altcoins.
- O ataque ocorre depois do hack de US$6 bilhões contra a Binance na quinta-feira.
- No mesmo dia do hack da Binance, a Polymarket sofreu um exploit de US$2,65 milhões.
**Fontes:**
- [S58] The Block — https://www.theblock.co/news/defi/2026-11-02-mercado-bitcoin-hack-46-million-brazil-exchange-432333

## Wall Street — Nasdaq cai 1,1% com rotação para fora de tecnologia; ouro sobe 1,8%
- Em 2 de novembro, o Nasdaq caiu 1,07%, para 25.164,32 pontos.
- O S&P 500 perdeu 0,51%, para 7.541,40 pontos, depois de devolver os ganhos do início do pregão.
- O Dow Jones subiu 0,41%, para 51.983,98 pontos.
- A Oracle caiu 8% após dizer que planeja vender US$10 bilhões em ações ordinárias e US$10 bilhões em títulos de dívida para financiar sua expansão em IA.
- Ações da "velha economia" puxaram o Dow Jones.
- A Sherwin-Williams subiu quase 6%, e a Home Depot, 3,6%.
- Honeywell, 3M e Boeing subiram mais de 2% cada.
- A maioria das ações do S&P 500 subiu, ajudada pela queda de 7,6% do petróleo Brent, para US$104,77.
- O ouro subiu 1,81%, para US$3.969,60.
- O rendimento do título do Tesouro americano de 10 anos caiu cerca de 3 pontos-base, para 4,91%.
**Fontes:**
- [S59] CNBC — https://www.cnbc.com/2026/11/01/stock-market-today-live-updates.html
- [S60] AP News — https://apnews.com/article/stocks-markets-ai-earnings-oil-iran-048328e49e47ce7afe6c1fb9d9acf13d
- [S61] FinanSignal — https://finansignal.com/markets/stock-market-today-nov-2-2026
