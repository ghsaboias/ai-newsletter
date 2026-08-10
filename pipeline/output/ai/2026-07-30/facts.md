# Fatos — Newsletter [Tech] 30 de Julho de 2026

## OpenAI — dois ajustes de API triplicam nota no ARC-AGI-3
- Em publicação de 29 de julho, a OpenAI afirmou que ligar dois ajustes de API que já usa no ChatGPT e no Codex — raciocínio retido (retained reasoning) e compactação (compaction) — triplicou a nota do GPT-5.6 Sol no ARC-AGI-3 no conjunto público de tarefas.
- Segundo a OpenAI, os mesmos dois ajustes reduziram em 6 vezes o consumo de tokens de output.
- Com o harness oficial do ARC-AGI-3, o GPT-5.6 Sol marcou 13,3% no conjunto público de tarefas.
- Reimplementado na Responses API da OpenAI, com raciocínio retido e compactação ligados, o mesmo modelo marcou 38,3%.
- Na configuração reimplementada, o modelo usou cerca de seis vezes menos tokens de output por partida.
- Os 38,3% superariam o Claude Opus 5, da Anthropic, que marcou 30,2%.
- No harness oficial do ARC, o GPT-5.6 Sol havia marcado apenas 7,8%, porque o raciocínio é descartado depois de cada ação.
- A OpenAI atribuiu o resultado baixo ao harness genérico: o raciocínio privado do agente era jogado fora depois de cada ação.
- O harness também usava truncamento rolante, descartando as partes mais antigas da conversa quando ela passava de 175.000 caracteres.
- O ARC Prize chamou a descoberta de "um resultado real e útil".
- O ARC Prize disse que suas notas verificadas usam deliberadamente uma abordagem "no harness" ("sem harness"), com o estado da conversa gerenciado no lado do cliente, para comparar todos os provedores sob os mesmos limites de observações, prompt e ações.
- O ARC Prize disse que está trabalhando com vários laboratórios da indústria, incluindo a OpenAI, para definir como incorporar o gerenciamento de estado no lado do servidor ao seu ambiente de teste verificado.
**Fontes:**
- [S1] OpenAI — https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/
- [S2] The Decoder — https://the-decoder.com/openai-claims-gpt-5-6-sol-beats-opus-5-on-arc-agi-3-with-its-latest-api-and-two-additional-settings/
- [S3] OfficeChai — https://officechai.com/ai/openai-says-gpt-5-6s-score-on-arc-agi-3-tripled-after-turning-on-two-api-settings/
- [S4] X — https://x.com/arcprize/status/2082672003765670160

## Microsoft — Copilot passa de 30 milhões de assentos pagos e Azure supera US$100 bilhões
- Satya Nadella disse que a receita do Azure superou US$100 bilhões pela primeira vez no ano fiscal de 2026.
- Nadella disse que o Microsoft 365 Copilot chegou a mais de 30 milhões de assentos pagos, "refletindo a confiança que os clientes estão depositando em nós para conduzir sua transformação de IA".
- A receita de Azure e outros serviços de nuvem cresceu 43% ano a ano no trimestre encerrado em junho.
- A receita da divisão Intelligent Cloud foi de US$39,3 bilhões, alta de 32%.
- As obrigações de desempenho remanescentes comerciais (contratos já fechados e ainda não reconhecidos como receita) subiram 84%.
- Na teleconferência de resultados, a Microsoft disse que a adição líquida de assentos pagos do Copilot mais que dobrou em relação ao trimestre anterior.
- A empresa disse que os resultados do Azure se beneficiaram de um consumo do GitHub Copilot maior que o esperado, após uma mudança de modelo de negócio em junho que alinhou o preço ao uso.
- A Microsoft projetou crescimento do Azure de aproximadamente 45% em moeda constante para o trimestre de setembro.
- A empresa disse que a demanda dos clientes continua a exceder a capacidade disponível.
- O trimestre incluiu um ganho de US$3,2 bilhões na participação da Microsoft na Anthropic, somando 33 centavos ao lucro por ação diluído.
- No mesmo trimestre, a participação na OpenAI foi baixada em cerca de US$600 milhões, reduzindo o lucro por ação em cerca de 7 centavos.
- No ano fiscal completo, o investimento da Microsoft na OpenAI gerou ganho de US$5 bilhões e somou US$0,67 ao lucro por ação.
- A receita trimestral foi de US$90 bilhões, com lucro líquido de US$35,8 bilhões.
- O Copilot adicionou cerca de 10 milhões de assentos pagos em um único trimestre.
- O crescimento de 43% do Azure acelerou em relação aos 40% do trimestre anterior e superou o consenso de analistas, de cerca de 40%.
**Fontes:**
- [S5] Microsoft — https://news.microsoft.com/source/2026/07/29/microsoft-cloud-and-ai-strength-fuels-fourth-quarter-results-4/
- [S6] Microsoft Investor Relations — https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
- [S7] TechCrunch — https://techcrunch.com/2026/07/29/microsoft-logs-3-2b-from-anthropic-investment-but-openai-was-a-mixed-bag/
- [S8] Tech Times — https://www.techtimes.com/articles/322143/20260729/azure-tops-100b-copilot-paid-seats-jump-30m-microsoft-blowout-quarter.htm

## OpenAI — receita anualizada de julho supera todo o segundo trimestre
- Em reunião interna na quarta-feira, 29 de julho, a CFO Sarah Friar disse a funcionários que a receita recorrente anualizada da OpenAI em julho superou todo o segundo trimestre.
- Friar acrescentou: "E o Q2 não foi fraco", segundo transcrição parcial da reunião revisada pela CNBC.
- O presidente do conselho, Bret Taylor, participou da reunião ao lado de Friar.
- Friar e Taylor atribuíram o crescimento à série de modelos GPT-5.6, ao agente corporativo ChatGPT Work e à adoção crescente da ferramenta de programação Codex.
- A mensagem visava tranquilizar os funcionários de que o negócio está saudável enquanto a competição se intensifica com a Anthropic e com modelos de pesos abertos mais baratos.
- A OpenAI não divulgou números absolutos.
- The Information já havia noticiado que a receita anualizada da OpenAI passou de US$25 bilhões ao fim de fevereiro.
**Fontes:**
- [S9] CNBC — https://www.cnbc.com/2026/07/29/openai-cfo-sarah-friar-tells-employees-arr-in-july-topped-all-of-q2.html
- [S10] The Economic Times — https://economictimes.indiatimes.com/tech/technology/gpt-5-6-chatgpt-work-lift-openais-july-arr-over-q2/articleshow/132728105.cms
- [S11] BeInCrypto — https://beincrypto.com/openai-revenue-big-tech-earnings-week/

## Lilian Weng — sai da Thinking Machines e volta à OpenAI
- A OpenAI confirmou na quarta-feira, 29 de julho, que a cofundadora da Thinking Machines Lilian Weng está voltando à empresa.
- Weng foi anteriormente VP de Pesquisa em Segurança de IA na OpenAI.
- Segundo um porta-voz da OpenAI, Weng vai liderar uma equipe de alto nível voltada a acelerar a pesquisa interna da empresa.
- A equipe apoiará trabalhos transversais de pesquisa em auto-aprimoramento recursivo, processo em que um sistema de IA itera sobre si mesmo para se tornar mais poderoso.
- Weng anunciou sua saída dias antes citando saúde, escrevendo: "Não sinto que consiga continuar no ritmo que uma startup exige".
- Ela disse que estresse e carga de trabalho a levaram além do que sua saúde podia sustentar.
- Weng disse que 29 de julho seria seu último dia na Thinking Machines.
- Weng é a terceira cofundadora da Thinking Machines a voltar para a OpenAI em 2026, depois de Barret Zoph e Luke Metz em janeiro.
- O pesquisador Sam Schoenholz retornou à OpenAI junto com Zoph e Metz em janeiro.
- A saída de Weng ocorreu enquanto a Thinking Machines corria para lançar o Inkling, seu primeiro modelo de pesos abertos.
- Até maio, 13 dos 42 membros fundadores do laboratório já tinham saído, incluindo três de seus seis cofundadores.
- A CEO da Thinking Machines, Mira Murati, respondeu publicamente ao post de Weng: "Vamos sentir sua falta, foi maravilhoso construir a Thinky juntas. Fico feliz que você esteja colocando sua saúde em primeiro lugar."
**Fontes:**
- [S12] TechCrunch — https://techcrunch.com/2026/07/29/thinking-machines-co-founder-lilian-weng-left-the-company-citing-health-reasons-then-joined-openai/
- [S13] RuntimeWire — https://runtimewire.com/article/lilian-weng-returns-openai-recursive-self-improvement
- [S14] The Next Web — https://thenextweb.com/news/lilian-weng-thinking-machines-openai-recursive-self-improvement

## União Europeia — ChatGPT deve entrar nas regras mais duras de plataformas
- A Comissão Europeia vai designar o ChatGPT, da OpenAI, e o Roblox como "plataformas online muito grandes" (VLOPs) sob o Digital Services Act (DSA), a lei europeia de serviços digitais.
- A designação vem depois de os dois passarem de 45 milhões de usuários mensais no bloco.
- A medida deve sair já em agosto.
- As VLOPs precisam apresentar relatórios de transparência, detalhar planos de mitigação de risco e pagar uma taxa anual à Comissão.
- Violações do DSA podem gerar multas de até 6% do faturamento global anual.
- Em até quatro meses após a designação, as empresas devem criar um ponto de contato para autoridades e usuários.
- As empresas também devem publicar termos e condições em linguagem acessível e ser transparentes sobre publicidade, sistemas de recomendação e decisões de moderação de conteúdo.
- Plataformas designadas devem passar por auditorias anuais, compartilhar dados com a Comissão e dar acesso a pesquisadores credenciados.
- As plataformas designadas devem avaliar riscos sistêmicos, incluindo conteúdo ilegal e processos eleitorais.
- O ChatGPT passou de 120 milhões de usuários mensais na Europa no ano passado.
- 21 plataformas já estão sujeitas às regras, incluindo X, Amazon, Apple, Microsoft, LinkedIn e TikTok, desde o início da aplicação do DSA em 2024.
**Fontes:**
- [S15] The Straits Times (Bloomberg) — https://www.straitstimes.com/world/europe/chatgpt-roblox-to-fall-under-strictest-eu-rules-for-platforms
- [S16] Engadget — https://www.engadget.com/2226821/chatgpt-roblox-vlop-eu-scrutiny/
- [S17] Silicon Republic — https://www.siliconrepublic.com/business/chatgpt-and-roblox-reportedly-set-to-face-strictest-eu-dsa-rules

## Onyx Security — Série B de US$113 milhões liderada pela Bessemer
- A Onyx anunciou em 29 de julho uma Série B de US$113 milhões liderada pela Bessemer Venture Partners.
- Participaram da rodada Cyberstarts, TCV, Conviction, FirstMark, Vintage Investment Partners, QuantumLight e G Squared.
- A rodada avalia a Onyx em cerca de US$640 milhões.
- A rodada vem apenas quatro meses depois de a empresa sair do stealth com US$40 milhões — um seed de US$5 milhões mais uma Série A de US$35 milhões.
- A Onyx diz que seu "Secure AI Control Plane" já protege mais de 1,1 milhão de agentes em clientes corporativos.
- A empresa afirma inspecionar mais de 66 milhões de sessões de IA em tempo real.
- A Onyx foi fundada em 2024 pelo CEO Maxim Bar Kogan e pelo chief AI officer Gil Elbaz.
- A empresa já levantou US$153 milhões no total.
- A Onyx tem mais de 80 funcionários em Israel, Estados Unidos e Canadá.
- Em junho, a Anthropic anunciou que havia integrado a tecnologia da Onyx para ajudar empresas a adotar IA com segurança.
- O novo capital será usado para treinar a próxima geração dos modelos proprietários da Onyx e para expandir vendas e marketing nos Estados Unidos e em outros mercados.
- O conselho da Onyx passa a incluir os sócios da Bessemer Amit Karp e Sameer Dholakia, além de representantes da Cyberstarts e da Conviction e dos cofundadores da Armis.
**Fontes:**
- [S18] Onyx Security — https://www.onyx.security/blog/onyx-113m-series-b-keeping-humans-in-control-as-ai-becomes-smarter
- [S19] CTech — https://www.calcalistech.com/ctechnews/article/b1fsjydszg
- [S20] Globes — https://en.globes.co.il/en/article-israeli-ai-security-co-onyx-security-raises-113m-1001550885
- [S21] RuntimeWire — https://runtimewire.com/article/onyx-security-raises-113m-series-b-ai-agent-control

## Google — Lyria 3.5 chega ao Flow Music
- O Google anunciou o Lyria 3.5 em 29 de julho e o liberou no mesmo dia no Google Flow Music.
- O Google diz que o modelo traz avanços em musicalidade, letras, vocais e controle criativo.
- O Google lista quatro melhorias: estruturas melódicas mais ricas; letras de qualidade superior, com melhor aderência ao prompt e consciência estrutural; vocais mais expressivos e realistas, com pronúncia aprimorada; e controle mais fácil de andamento e duração.
- A DeepMind descreve o Lyria 3.5 como seu modelo de geração musical mais avançado.
- O modelo suporta faixas de até três minutos.
- O lançamento adiciona controle direto de BPM (batidas por minuto).
- O Flow Music foi construído pelos fundadores da Riffusion, Seth Forsgren e Hayk Martiros, cuja startup o Google comprou no início deste ano.
- O Google não informou se o Lyria 3.5 substitui o Lyria 3 Pro no app Gemini e nas plataformas para desenvolvedores.
- Assinantes do Google AI Plus recebem o plano Starter do Flow Music; assinantes do AI Pro recebem o plano Plus; assinantes do AI Ultra recebem o plano Member.
- O Flow Music já permite editar trechos específicos de uma faixa, reescrever ou traduzir letras, trocar instrumentos e mudar o estilo de uma batida sem recriar a música inteira.
**Fontes:**
- [S22] Google — https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/
- [S23] Google DeepMind — https://deepmind.google/models/lyria/
- [S24] RuntimeWire — https://runtimewire.com/article/google-lyria-3-5-flow-music-bpm-controls
- [S25] Neowin — https://www.neowin.net/news/googles-lyria-35-makes-ai-generated-songs-sound-more-natural-and-expressive/

## Samsung — trimestre recorde com memória e alerta de escassez até 2028
- A Samsung Electronics reportou receita recorde de 171,5 trilhões de wons (cerca de US$119 bilhões) no segundo trimestre de 2026.
- O lucro operacional do trimestre foi de 89,5 trilhões de wons (cerca de US$62 bilhões).
- Receita e lucro operacional subiram 28% e 56%, respectivamente, em relação ao trimestre anterior.
- Na comparação anual, o lucro operacional subiu 1.813,83% e a receita, 130% — ambos recordes históricos.
- A divisão Device Solutions (semicondutores) sozinha gerou cerca de 127,5 trilhões de wons de receita e 89,2 trilhões de wons de lucro operacional, praticamente todo o lucro do grupo.
- A divisão de memória registrou vendas recordes de bits de DRAM e NAND.
- A Samsung ampliou o fornecimento de HBM4 (memória de alta largura de banda usada em chips de IA) e foi a primeira da indústria a enviar amostras de HBM4E a grandes clientes.
- O gasto com P&D atingiu o recorde de 16 trilhões de wons.
- Na teleconferência, a Samsung disse que a receita de HBM4 do terceiro trimestre vai mais que triplicar em relação ao trimestre anterior.
- A empresa disse que o HBM4 deve superar com folga 60% da receita total de HBM no segundo semestre.
- A divisão de foundry (fabricação para terceiros), que registrava prejuízos trilionários em wons a cada trimestre, está se aproximando do ponto de equilíbrio.
- O vice-presidente executivo da divisão de memória, Kim Jaejune, disse que o desfasamento entre oferta e demanda de chips deve se ampliar ainda mais em 2027.
- Kim disse que a escassez deve persistir até 2028.
- Os resultados da Samsung saíram um dia depois do trimestre recorde da SK Hynix; as duas são as maiores fabricantes de memória do mundo.
**Fontes:**
- [S26] Associated Press — https://apnews.com/article/samsung-ai-profit-memory-chips-10c2c548a392988862d8c7bd3f6fae05
- [S27] DigitalToday — https://www.digitaltoday.co.kr/en/view/87007/samsung-electronics-posts-record-q2-operating-profit-up-1814-percent-year-on-year
- [S28] The Asia Business Daily — https://www.asiae.co.kr/en/article/2026073009064678225
- [S29] Maeil Business Newspaper — https://www.mk.co.kr/en/business/12111532
- [S30] ChosunBiz — https://biz.chosun.com/en/en-it/2026/07/30/KDRBNCIRQJD2TNZJIRM3RWFY3A/?outputType=amp
- [S31] Euronews — https://www.euronews.com/business/2026/07/30/samsung-profit-jumps-1814-as-south-korean-tech-giants-benefit-from-global-ai-boom
- [S32] Samsung Electronics — https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2026_2Q_conference_eng.pdf

## Qualcomm — receita com a Apple deve cair mais rápido e custo de memória aperta chips de celular
- A Qualcomm reportou receita de US$9,95 bilhões no terceiro trimestre fiscal, queda de 4% ano a ano, acima do consenso de US$9,67 bilhões.
- O lucro por ação non-GAAP foi de US$2,21, contra US$2,23 esperados.
- Para o trimestre atual, a empresa projeta lucro ajustado por ação de US$2,05 a US$2,25, abaixo da estimativa média de analistas de US$2,36.
- A projeção de receita é de US$9,7 bilhões a US$10,5 bilhões, contra estimativas de US$10,02 bilhões.
- Por causa de restrições de oferta, a Qualcomm agora espera uma queda acelerada da receita com produtos da Apple a partir do quarto trimestre fiscal.
- A empresa disse que sua fatia de modems no próximo lançamento do iPhone deve ser "materialmente menor" que sua estimativa anterior de 20%.
- A receita com chips para celulares caiu 20%, a US$5,09 bilhões.
- A Qualcomm espera que a receita com aparelhos Android caia cerca de 20% no ano fiscal de 2026 por causa de aumentos sem precedentes no preço da memória.
- A empresa afirma que esse efeito reduz o lucro anual por ação em mais de US$1,50.
- O CEO Cristiano Amon disse que o crescimento da receita fora de celulares, incluindo data center, deve acelerar de 24% no ano fiscal de 2026 para mais de 60% no ano fiscal de 2027.
- A Qualcomm tem como meta US$40 bilhões de receita fora de celulares até o ano fiscal de 2029.
- No trimestre, a Qualcomm concluiu a aquisição da Modular Inc.
- A receita automotiva subiu 61%, a US$1,59 bilhão, e a de IoT subiu 9%, a US$1,83 bilhão.
- A receita total de chips da divisão QCT caiu 5%, para US$8,5 bilhões.
- As ações caíram no after-market.
- Amon disse que, dentro da faixa premium, a preferência do consumidor está migrando para aparelhos mais baratos e para o modelo do ano anterior por causa dos aumentos de preço da memória.
**Fontes:**
- [S33] CNBC — https://www.cnbc.com/2026/07/29/qualcomm-qcom-earnings-report-q3-2026-.html
- [S34] Reuters via Yahoo Finance — https://finance.yahoo.com/markets/stocks/articles/qualcomm-forecasts-weak-quarterly-profit-200152315.html
- [S35] Qualcomm — https://s204.q4cdn.com/645488518/files/doc_financials/2026/q3/FY2026-3rd-Quarter-Earnings-Presentation_7-29-26_Final.pdf
- [S36] Qualcomm — https://s204.q4cdn.com/645488518/files/doc_financials/2026/q3/FY2026-3rd-Quarter-Earnings-Release.pdf
- [S37] Stock Titan — https://www.stocktitan.net/sec-filings/QCOM/8-k-qualcomm-inc-de-reports-material-event-c8f67e4983cc.html

## Arm — trimestre recorde com royalties de data center dobrando
- A Arm reportou receita de US$1,289 bilhão no primeiro trimestre do ano fiscal 2027, alta de 22% ano a ano e um recorde.
- A receita ficou acima do consenso FactSet de US$1,26 bilhão.
- A receita de royalties subiu 22%, a US$715 milhões, e a de licenciamento subiu 23%, a US$574 milhões.
- Os royalties de data center mais que dobraram ano a ano.
- A empresa citou a adoção continuada de tecnologia Arm com taxas de royalty mais altas por chip, como a arquitetura Armv9 e os Arm Compute Subsystems (CSS).
- O lucro por ação non-GAAP cresceu 29%, a US$0,45, acima do topo da projeção.
- O lucro líquido GAAP foi de US$270 milhões, ou US$0,25 por ação, contra US$130 milhões e US$0,12 um ano antes.
- A Arm projetou receita de US$1,38 bilhão, mais ou menos US$50 milhões, para o segundo trimestre.
- A projeção de lucro ajustado por ação é de US$0,47, mais ou menos US$0,04.
- As duas projeções ficaram acima das estimativas de analistas, de US$1,34 bilhão e US$0,44.
- Na teleconferência, a direção disse que IA em nuvem foi novamente o maior motor do crescimento de royalties.
- A empresa citou chips de servidor baseados em Arm em rampa de produção em todos os grandes hyperscalers.
- A Arm disse que sua tecnologia está em praticamente todas as principais DPUs e SmartNICs (chips de rede de data center).
**Fontes:**
- [S38] SEC — https://www.sec.gov/Archives/edgar/data/1973239/000197323926000113/exhibit992fye27q130-junx26.htm
- [S39] Arm — https://newsroom.arm.com/news/arm-q1-fye27-results
- [S40] Dow Jones via MarketScreener — https://ca.marketscreener.com/news/arm-posts-higher-1q-revenue-profit-as-ai-demand-drives-growth-ce7f51d3dd8ef225
- [S41] StockAnalysis — https://stockanalysis.com/stocks/arm/transcripts/632326-q1-2027/

## Intel — tecnologia do processador Atom vai para a startup RosaicLabs
- A Reuters noticiou em 29 de julho que a Intel deu à nova startup RosaicLabs Inc. acesso à tecnologia de seus processadores Atom.
- É um movimento raro para a Intel, que historicamente não licenciou amplamente partes de sua arquitetura x86 nem cedeu tecnologia Atom.
- A Intel pretende entregar à startup o código de nível de transferência de registradores (RTL) dos núcleos Atom, a forma que projetistas usam para integrar um processador a um chip customizado.
- A RosaicLabs registrou seus primeiros documentos de incorporação em Delaware em maio.
- Um documento alterado, datado de 24 de julho, nomeia Amarjit Gill como CEO e permite uma rodada seed de cerca de US$10 milhões.
- Gill e o CEO da Intel, Lip-Bu Tan, são coinvestidores de longa data.
- Gill ajudou Tan a montar o time fundador da Rivos, empresa de chips que a Meta comprou no ano passado após superar a oferta da Intel; Tan era presidente do conselho da Rivos na época.
- Tan e Gill fizeram investimentos seed na Nuvia, startup de chips depois vendida à Qualcomm.
- O time fundador da Rosaic inclui veteranos da Rivos, e o ex-diretor financeiro da Rivos, Amit Parikh, assinou o documento de incorporação.
- A Intel não quis comentar.
- Os termos financeiros do acordo, os mercados permitidos, as condições de fabricação e as restrições técnicas não são públicos.
- A Intel não disse qual núcleo Atom a Rosaic vai receber.
- O Atom é a linha x86 de baixo consumo da Intel, projetada para operar com pouca energia e gerar pouco calor, atributos adequados a dispositivos móveis e de borda.
**Fontes:**
- [S42] Reuters via CNA — https://www.channelnewsasia.com/business/exclusive-intel-providing-chip-technology-startup-led-co-investor-tan-in-rare-deal-6287056
- [S43] Reuters via Yahoo Finance — https://finance.yahoo.com/technology/articles/exclusive-intel-providing-chip-technology-225454435.html
- [S44] Gadgets Now — https://gadgetsnow.indiatimes.com/tech-news/intels-rare-atom-deal-with-rosaiclabs-could-open-a-new-front-against-arm-and-risc-v/articleshow/132730148.cms

## Zhongji Innolight — ação cai na estreia após IPO de US$6,8 bilhões em Hong Kong
- A Zhongji Innolight, fabricante chinesa de transceptores ópticos para data centers de IA, levantou HK$53,4 bilhões (US$6,8 bilhões) em seu IPO (oferta pública inicial) em Hong Kong.
- A oferta foi precificada a HK$980 por ação, abaixo do máximo indicado de HK$1.010.
- As ações caíram na estreia em Hong Kong, em 30 de julho: recuo de cerca de 5% no início e 7,4% abaixo do preço de emissão, a HK$908, no intervalo do meio-dia.
- A estreia coincidiu com uma venda global de ações ligadas a IA.
- Foi o maior IPO de Hong Kong em 2026 e o segundo maior da Ásia no ano, atrás da listagem de US$8,6 bilhões da fabricante de memória CXMT em Xangai.
- O valor de mercado da Innolight passou de HK$1 trilhão.
- Investidores de varejo subscreveram cerca de 16,8 vezes a tranche de Hong Kong e investidores internacionais, 9,7 vezes.
- Os recursos brutos foram de HK$53.410 milhões, contra recursos líquidos de HK$52.891 milhões.
- A Innolight é a maior fornecedora mundial de soluções de interconexão óptica por receita, com 21,2% do mercado global em 2025.
- A empresa planeja usar os recursos em P&D, capacidade de produção no exterior, cadeia de suprimentos e aquisições.
- Dias antes da estreia, a empresa anunciou um plano de recompra de ações A de até 8 bilhões de yuans (US$1,2 bilhão).
- A ação listada em Shenzhen havia caído 16% desde o lançamento da oferta de ações H.
**Fontes:**
- [S45] CNBC — https://www.cnbc.com/2026/07/30/china-ai-supplier-zhongji-innolight-hong-kong-debut.html
- [S46] South China Morning Post — https://www.scmp.com/business/companies/article/3362321/zhongji-innolight-shares-fall-hong-kong-debut-amid-global-ai-sell
- [S47] HKEXnews — https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0729/2026072901629.pdf
- [S48] Nikkei Asia — https://asia.nikkei.com/business/markets/ipo/ai-supplier-innolight-dips-in-asia-s-second-biggest-listing-of-20262

## União Europeia — abre licitação para sete gigafábricas de IA
- A Comissão Europeia publicou na quinta-feira o edital de licitação, longamente adiado, com um aviso de contratação de 5 bilhões de euros da UE.
- O edital cobre um desenho multissítio e multipaís de sete gigafábricas de IA.
- O investimento total nos sete sítios é estimado em 30 bilhões de euros: 5 bilhões da UE, 5 bilhões dos Estados-membros e 20 bilhões de investidores privados.
- O edital se encerra em 12 de novembro.
- Os proponentes precisam demonstrar medidas para mitigar "vendor lock-in" (dependência de um único fornecedor), disposição voltada a limitar o domínio da Nvidia em chips de IA para data centers.
- Consórcios com pontuação baixa nesse critério podem ser desqualificados.
- O financiamento passa pela EuroHPC Joint Undertaking, com 18 Estados-membros, incluindo a Espanha, que comprarão em conjunto o acesso ao poder computacional.
- Há duas linhas de financiamento: uma de até 500 milhões de euros e outra de até 1 bilhão de euros por instalação.
- As decisões de adjudicação são esperadas para o início de 2027.
- A Comissão ampliou o escopo inicial de quatro ou cinco gigafábricas para até sete, após 76 manifestações de interesse cobrindo 60 sítios em 16 Estados-membros.
- A construção deve começar no início de 2027 e as instalações devem estar operacionais até meados de 2028.
- Cada gigafábrica deve abrigar ao menos 100.000 chips de IA de ponta, o que as torna cerca de quatro vezes mais potentes que os data centers hoje em operação na UE.
- O poder computacional atual da UE mais que dobraria com os sete sítios em operação.
- A iniciativa remonta ao compromisso de Ursula von der Leyen, em fevereiro de 2025, de mobilizar 20 bilhões de euros para várias gigafábricas.
- A licitação formal estava prevista para o fim de 2025 e foi adiada duas vezes.
**Fontes:**
- [S49] Euractiv — https://www.euractiv.com/news/eu-finally-fires-the-start-gun-on-ai-gigafactories/
- [S50] Euronews — https://www.euronews.com/my-europe/2026/07/30/eu-opens-call-for-seven-gigafactories-to-train-next-generation-ai-technologies
- [S51] Brussels Signal — https://brusselssignal.eu/2026/07/european-commission-opens-bidding-to-build-seven-ai-gigafactories/
- [S52] European Commission — https://commission.europa.eu/topics/competitiveness/competitiveness-coordination-tool-projects/ai-gigafactories_en
- [S53] Swadesi — https://swadesi.com/news/eu-lays-out-usd-114-billion-for-7-ai-gigafactories-as-it-aims-to-catch-ms7d5c2i

## Microsoft e Meta — gastos com data center sobem para US$41 bilhões e US$31 bilhões no trimestre
- Os investimentos de capital da Microsoft entre abril e junho foram de US$41 bilhões, alta de mais de 70% ano a ano.
- Cerca de dois terços desse valor foram para ativos de vida curta, principalmente CPUs e GPUs.
- Os arrendamentos financeiros totalizaram US$5,6 bilhões no trimestre.
- A Microsoft adicionou 88 data centers no ano fiscal de 2026 e mais 1 GW de capacidade no quarto trimestre.
- A empresa gastou quase US$116 bilhões em propriedades e equipamentos no ano.
- O saldo de propriedades e equipamentos subiu para US$313,1 bilhões, de US$205,0 bilhões um ano antes.
- A Microsoft passará a distribuir arrendamentos de longo prazo de data centers em 25 anos, em vez de 15, o que reduz o investimento de capital reportado anualmente.
- A empresa projetou cerca de US$175 bilhões de investimento de capital reportado para o ano-calendário de 2026, contra sua própria estimativa anterior de US$190 bilhões.
- A Microsoft projetou mais de US$50 bilhões de investimento de capital no trimestre atual, o primeiro do ano fiscal de 2027.
- A empresa disse que seus planos de gasto permanecem inalterados.
- Em documento regulatório, a Microsoft revelou US$329,1 bilhões em arrendamentos de data center que ainda não começaram, com início entre os anos fiscais de 2027 e 2033.
- A Meta gastou US$31,08 bilhões em investimento de capital, incluindo pagamentos de principal de arrendamentos financeiros, no trimestre.
- Esse valor é 83% maior que os US$17,01 bilhões registrados na mesma base um ano antes.
- A Meta estreitou para cima sua faixa de investimento de capital para 2026: US$130 bilhões a US$145 bilhões, contra os US$125 bilhões a US$145 bilhões anteriores.
- A expansão consumiu quase todo o caixa operacional da Meta: o fluxo de caixa operacional subiu 25%, a US$31,86 bilhões, mas o fluxo de caixa livre caiu para US$784 milhões, de US$8,55 bilhões um ano antes.
- As propriedades e equipamentos líquidos da Meta chegaram a US$225,72 bilhões em 30 de junho, alta de US$49,32 bilhões, ou 28%, desde o fim de 2025.
- A Meta confirmou a projeção de investimento de capital de 2026 em seu comunicado de resultados e projetou receita de US$61 bilhões a US$64 bilhões no terceiro trimestre.
**Fontes:**
- [S54] Converge Digest — https://convergedigest.com/microsoft-plans-175-billion-in-2026-capital-spending/
- [S55] Reuters via Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/microsoft-tops-quarterly-cloud-growth-200428732.html
- [S56] Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/meta-lifts-2026-capex-floor-203035634.html
- [S57] PR Newswire — https://www.prnewswire.com/news-releases/meta-reports-second-quarter-2026-results-302838214.html

## Estados Unidos e Irã — nova "onda pesada" de ataques a alvos da Guarda Revolucionária
- O Comando Central dos EUA (CENTCOM) disse ter concluído uma "onda pesada de ataques contra o Irã" até as 22h ET de quarta-feira, 29 de julho (02:00 GMT de 30 de julho).
- Os ataques vieram após uma pausa de cinco noites nos bombardeios.
- Os ataques começaram às 20h ET e duraram duas horas.
- O CENTCOM disse ter atingido dezenas de alvos do Corpo da Guarda Revolucionária Islâmica (IRGC), incluindo centros de comando militar, instalações de mísseis e drones, sítios de vigilância e defesa costeira e capacidades marítimas.
- O CENTCOM apresentou a operação como retaliação à tentativa de ataque com mísseis do Irã contra forças americanas em uma base na Jordânia, um dia antes.
- O exército jordaniano disse ter interceptado cinco mísseis iranianos.
- A imprensa iraniana reportou três civis mortos nos últimos ataques.
- A Guarda Revolucionária disse que três de seus militares foram mortos em um ataque com mísseis dos EUA.
- Na quinta-feira, a Guarda Revolucionária disse que "vai punir o agressor hoje" e advertiu que países que ajudarem os EUA receberão uma "resposta severa".
- A Guarda Revolucionária afirmou manter "controle total" do Estreito de Ormuz.
- Horas antes, Trump antecipou a retaliação à Fox News: "Vamos atingi-los com força... Vamos acabar com eles."
- O ministro da Defesa da Arábia Saudita se reuniu com o vice-presidente americano JD Vance para pedir à administração que não escale mais o conflito atacando os houthis do Iêmen ou realizando novos ataques no Iraque.
**Fontes:**
- [S58] Al Jazeera — https://www.aljazeera.com/news/2026/7/30/us-launches-another-round-of-attacks-on-iran
- [S59] AP News — https://apnews.com/article/iran-war-us-hormuz-strait-july-29-2026-e31d249ba6443decdd3e63cd00f0fb84
- [S60] France 24 — https://www.france24.com/en/middle-east/20260730-us-carries-out-powerful-strikes-on-iran-after-attacks-on-bases-and-regional-allies
- [S61] The Times of Israel — https://www.timesofisrael.com/us-strikes-irans-revolutionary-guards-in-powerful-response-to-attacks-on-its-forces/
- [S62] CNA — https://www.channelnewsasia.com/world/us-strike-iran-war-retaliation-6286796
- [S63] ABC News (Australia) — https://www.abc.net.au/news/2026-07-30/iran-war-us-resumes-strikes-july-30-2026/106975718

## Petróleo — Brent sobe 7,9% e fecha a US$90,74
- Os futuros do Brent fecharam em alta de US$6,65, ou 7,91%, a US$90,74 o barril, em 29 de julho.
- O petróleo americano West Texas Intermediate ganhou US$5,20, ou 6,56%, a US$84,46 o barril.
- A alta reverteu a maior queda em três dias desde 2020, depois de os preços recuarem para a faixa dos US$80 e poucos quando Trump suspendeu a campanha de bombardeios no fim de semana.
- Dados da Administração de Informação de Energia dos EUA mostraram queda de 7,2 milhões de barris nos estoques de petróleo na semana anterior, a maior desde meados de junho.
- Apenas alguns navios de carga passaram pelo Estreito de Ormuz durante a semana.
- Cinco navios passaram pelo Estreito de Bab el-Mandeb na quarta-feira, contra 39 na terça.
- O Irã rejeitou como "irracional" uma proposta de Omã, apoiada por países do Golfo, de gestão regional conjunta do Estreito de Ormuz.
- O Irã disse ter atirado contra três petroleiros que tentavam a travessia.
- Os EUA sancionaram duas empresas iranianas envolvidas na cobrança de embarcações pela passagem no Estreito de Ormuz.
- Incêndios atingiram dois navios de GNL no porto de Damietta, no Egito.
- O Brent oscilou entre cerca de US$72 e US$102 o barril ao longo de julho.
- Cerca de 20% da oferta global de petróleo normalmente passa por Ormuz.
**Fontes:**
- [S64] LSE / Reuters — https://www.lse.co.uk/news/oil-rises-as-us-iran-tension-escalates-after-iraq-strikes-missile-attack-7pash1kwzvypxcc.html
- [S65] World Oil — https://www.worldoil.com/news/2026/7/29/oil-surges-above-90-as-trump-warns-of-new-strikes-on-iran/
- [S66] gCaptain — https://gcaptain.com/hormuz-tensions-flare-after-u-s-saudi-strikes-iran-claims-attacks-on-tankers/
- [S67] Global News — https://globalnews.ca/news/12001205/oil-prices-jump-renewed-fighting-middle-east/
- [S68] The New York Times — https://www.nytimes.com/2026/07/29/business/oil-prices-iran-war-us-attacks.html

## Federal Reserve — juros mantidos com três votos dissidentes por alta
- O FOMC votou 9 a 3, em 29 de julho, para manter a meta dos juros básicos entre 3,5% e 3,75%, a quinta manutenção consecutiva.
- Beth Hammack (Cleveland), Neel Kashkari (Minneapolis) e Lorie Logan (Dallas) votaram contra, preferindo uma alta de 0,25 ponto percentual.
- Foi a primeira vez que três votantes divergiram desde setembro de 2016.
- O comunicado disse que a atividade econômica está se expandindo em ritmo sólido "apesar da elevada incerteza que decorre, em parte, do conflito no Oriente Médio".
- O comunicado afirmou que a inflação continua elevada em relação à meta de 2%, em parte por choques de oferta em setores como energia.
- O presidente do Fed, Kevin Warsh, em sua segunda reunião no cargo, disse: "Pedi uma boa briga de família e recebi uma."
- Warsh reiterou que não existe meta de inflação branda ou implícita acima de 2%: "Há apenas uma meta, e ela é de 2%."
- Depois da decisão, a ferramenta CME FedWatch mostrava 57,2% de probabilidade de alta de 25 pontos-base na reunião de 15 e 16 de setembro.
- A ferramenta mostrava 41,9% de chance de os juros ficarem no nível atual em setembro, acima dos 24% do dia anterior.
- A última mudança nos juros foi um corte de 0,25 ponto percentual em dezembro de 2025.
- A inflação está acima da meta de 2% do Fed há mais de cinco anos.
**Fontes:**
- [S69] Federal Reserve — https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
- [S70] Federal Reserve — https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260729.pdf
- [S71] Fox Business — https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-july-29-2026
- [S72] CNBC — https://www.cnbc.com/2026/07/29/fed-meeting-today-live-updates.html
- [S73] CBS News — https://www.cbsnews.com/news/federal-reserve-interest-rates-kevin-warsh-july-206/
- [S74] BNN Bloomberg — https://www.bnnbloomberg.ca/business/economics/2026/07/29/us-federal-reserve-votes-9-3-to-leave-key-rate-unchanged-despite-persistently-high-inflation/

## Rússia e Ucrânia — 74 mísseis e 284 drones, e um míssil russo aparentemente cai na Polônia
- A Rússia lançou mais de 70 mísseis, muitos deles balísticos, e mais de 280 drones de ataque na madrugada de 30 de julho.
- Os ataques atingiram Kiev e outras nove regiões, de Lviv a Kharkiv.
- A força aérea ucraniana disse ter derrubado 55 mísseis e 265 drones, mas apenas um de nove mísseis balísticos.
- Segundo a força aérea, 11 mísseis e 17 drones atingiram alvos em 20 localidades.
- Zelensky informou pelo menos oito mortos, incluindo três crianças; a Reuters reportou depois pelo menos 13 mortos em toda a Ucrânia.
- O ataque mais letal atingiu o povoado de Radushne, perto de Kryvyi Rih, onde um míssil balístico Iskander-M destruiu a casa de uma família.
- Seis pessoas morreram em Radushne, incluindo os pais e três crianças: uma menina de 6 anos e meninos de 11 e 17 anos.
- Em Lviv, mísseis danificaram mais de 20 prédios residenciais, uma escola e duas creches, ferindo pelo menos 26 pessoas.
- A Polônia acionou um F-16 e um helicóptero após detectar um objeto não identificado.
- Uma cratera de 10 metros e destroços foram encontrados na região de Lublin, na Polônia.
- O primeiro-ministro Donald Tusk disse: "Parece que foi um míssil russo, mas não temos certeza absoluta de que tipo de míssil."
- O ministro das Relações Exteriores da Ucrânia, Andrii Sybiha, afirmou que o objeto que cruzou para a Polônia era um míssil de cruzeiro russo Kh-101, chamando o episódio de violação do espaço aéreo da OTAN.
- O ataque ocorreu quando Zelensky voltava de Washington dizendo que Trump concordou em licenciar mísseis Patriot para a Ucrânia.
- O Ministério da Defesa da Rússia disse ter atingido instalações militares de Kiev a Lviv e Dnipropetrovsk, além de três navios de carga.
- Um armazém da varejista online russa Wildberries pegou fogo em Penza após um ataque de drone ucraniano.
**Fontes:**
- [S75] NBC News — https://www.nbcnews.com/world/ukraine/russian-strikes-ukraine-kill-13-poland-scrambles-fighter-jets-rcna589964
- [S76] The Straits Times — https://www.straitstimes.com/world/europe/russia-pounds-ukraine-in-new-air-attack-killing-8-including-children
- [S77] RBC-Ukraine — https://newsukraine.rbc.ua/news/deadly-russian-missile-and-drone-attack-hits-1785401960.html
- [S78] Meduza — https://meduza.io/en/news/2026/07/30/russia-strikes-kyiv-lviv-and-kryvyi-rih-with-missiles-at-least-two-children-among-the-dead
- [S79] The Independent — https://www.the-independent.com/news/world/europe/ukraine-russia-war-live-wildberries-drone-strikes-putin-attack-b3024254.html
- [S80] ABC News — https://abcnews.com/International/russian-strikes-ukraine-kill-8-zelenskyy-blames-insufficient/story?id=135216948

## FDA — comitê vota 9 a 3 contra terapia celular da Capricor para distrofia de Duchenne
- O Comitê Assessor de Terapias Celulares, Teciduais e Genéticas da FDA (agência reguladora de medicamentos dos EUA) votou 9 a 3 na quarta-feira, 29 de julho, contra o deramiocel.
- O deramiocel é a terapia celular da Capricor Therapeutics para distrofia muscular de Duchenne.
- Alguns membros do comitê expressaram apoio moderado ao medicamento.
- O voto acompanhou os revisores da FDA, que sustentaram que o deramiocel não demonstrou eficácia significativa.
- Essa análise dos revisores provocou queda de mais de 60% nas ações da Capricor na segunda-feira.
- O diretor interino de produtos biológicos da agência, Karim Mikhail, disse que nenhuma decisão final foi tomada.
- A FDA tem até 22 de agosto para aprovar ou rejeitar a terapia.
- A FDA rejeitou o medicamento pela primeira vez em julho de 2025, mas depois deu à Capricor a chance de defender seu caso.
- A revista The Lancet publicou simultaneamente os resultados do estudo HOPE-3 da Capricor, o que, segundo a empresa, oferece "validação externa" dos achados positivos do estudo.
- A Capricor argumenta que os materiais informativos da FDA se basearam em um plano de análise estatística obsoleto (SAP versão 1.1), e não no SAP 3.0 final, concluído antes da quebra do cegamento do estudo.
- A Capricor afirma que o HOPE-3 alcançou seu desfecho primário, o PUL 2.0, com significância estatística.
- Separadamente, revisores da FDA criticaram o terceiro pedido de aprovação da Replimune para sua terapia contra melanoma RP1, antes de uma reunião do comitê assessor na quinta-feira.
- As ações da Replimune caíram cerca de um terço.
**Fontes:**
- [S81] Endpoints News — https://endpoints.news/fda-capricor-battle-over-dmd-cell-therapys-efficacy-at-adcomm/
- [S82] Capricor Therapeutics — https://www.capricor.com/investors/news-events/press-releases/detail/349/capricor-comments-on-briefing-materials-ahead-of-july-29
- [S83] The Pharma Letter — https://www.thepharmaletter.com/biotech-news/replimune-shares-slump-as-fda-staff-again-pan-rp1-melanoma-filing

## SpaceX — US$1,6 bilhão em encomendas de lançamento da Força Espacial
- A Força Espacial dos EUA concedeu à SpaceX duas ordens de tarefa de lançamento no valor de US$1,6 bilhão para implantar constelações de satélites militares.
- É o maior lote de missões anunciado publicamente até agora no programa National Security Space Launch (NSSL) Fase 3.
- A encomenda cobre 18 lançamentos de Falcon 9 da Base da Força Espacial de Vandenberg, na Califórnia, até o fim de 2027.
- Os lançamentos apoiam o portfólio Space Based Sensing and Targeting (sensoriamento e definição de alvos a partir do espaço).
- É a maior encomenda divulgada na Lane 1 da Fase 3 do NSSL.
- O contrato vem depois de a Força Espacial elevar, no início de julho, o teto do contrato da Fase 3 Lane 1 para US$17 bilhões, de US$5,6 bilhões.
- Concluir 18 lançamentos até o fim de 2027 implica cerca de uma missão por mês a partir de Vandenberg.
- Sete empresas têm posições na Lane 1, mas a SpaceX é a única com a cadência de lançamento, os foguetes Falcon 9 operacionais e a infraestrutura na Costa Oeste necessários para uma campanha dessa escala.
- Separadamente, a SpaceX lançou a carga classificada NROL-95 para o Escritório Nacional de Reconhecimento (NRO) de Cabo Canaveral às 3h09 ET de 30 de julho, do Complexo de Lançamento Espacial 40.
- Foi o quarto lançamento do NRO em 2026 e sua terceira missão em Falcon 9 na Fase 2 do NSSL.
- Com a Blue Origin e a ULA fora de operação por problemas em seus sistemas de lançamento, a SpaceX é atualmente a única provedora que voa cargas de segurança nacional a partir do Cabo.
**Fontes:**
- [S84] SpaceNews — https://spacenews.com/spacex-wins-1-6-billion-in-launch-orders-for-military-satellite-networks/
- [S85] Spaceflight Now — https://spaceflightnow.com/2026/07/29/live-coverage-spacex-to-launch-classified-payload-for-national-reconnaissance-office/
- [S86] Space.com — https://www.space.com/space-exploration/launches-spacecraft/spacex-falcon-9-spy-satellite-launch-nrol-95
- [S87] Talk of Titusville — https://talkoftitusville.com/2026/07/29/falcon-9-launching-classified-nro-payload-overnight-expect-a-sonic-boom-locally/

## Grant Thornton — compra da CBIZ por US$5 bilhões
- A Grant Thornton Advisors, apoiada pela New Mountain Capital, concordou em 29 de julho em adquirir a CBIZ (NYSE: CBZ) em transação totalmente em dinheiro, com valor de empresa de US$5 bilhões.
- Os acionistas da CBIZ vão receber US$55,00 em dinheiro por ação.
- O preço representa prêmio de cerca de 54% sobre o preço médio ponderado por volume das ações da CBIZ nos últimos 30 dias.
- Com o fechamento, a Grant Thornton nos EUA deve se tornar a quinta maior fornecedora de serviços profissionais, tributários e de consultoria, com mais de US$5 bilhões de receita doméstica anual.
- A transação é descrita como a maior do tipo em mais de 25 anos.
- O conselho da CBIZ aprovou o negócio de forma unânime.
- O fechamento é esperado para o quarto trimestre de 2026, sujeito a aprovações dos acionistas e regulatórias.
- As ações da CBIZ deixarão de ser negociadas e serão retiradas da Bolsa de Nova York.
- A New Mountain Capital, que liderou um investimento na Grant Thornton Advisors em maio de 2024, vai aportar capital adicional para apoiar a transação.
- As ações da CBIZ subiram cerca de 17,6% com a notícia.
- A CBIZ registrou um formulário 8-K em 29 de julho divulgando o evento relevante junto com seus resultados do segundo trimestre e do primeiro semestre de 2026.
**Fontes:**
- [S88] GlobeNewswire — https://www.globenewswire.com/news-release/2026/07/29/3335168/0/en/Grant-Thornton-Advisors-to-Acquire-CBIZ-for-5-Billion-in-Transaction-Supported-by-New-Mountain-Capital.html
- [S89] Markets Insider — https://markets.businessinsider.com/news/stocks/grant-thornton-advisors-to-acquire-cbiz-for-5-billion-in-transaction-supported-by-new-mountain-capital-1036377917
- [S90] Stock Titan — https://www.stocktitan.net/sec-filings/CBZ/8-k-cbiz-inc-reports-material-event-1681ba1fa6ec.html
