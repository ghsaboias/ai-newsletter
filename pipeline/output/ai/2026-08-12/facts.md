# Fatos — Newsletter [Tech] 12 de Agosto de 2026

## xAI — Grok 4.6
- A xAI lançou o Grok 4.6 em 12 de agosto de 2026, sucessor do Grok 4.5, que saiu em julho.
- A empresa apresenta o modelo não como um salto de inteligência bruta, mas como um modelo feito para agentes de longa duração e para trabalho interativo e visual.
- Os casos de uso citados são pesquisa em várias etapas, trabalhar sobre uma base de código e transformar uma ideia de produto em uma primeira versão.
- No Artificial Analysis Intelligence Index, um composto de nove benchmarks, o Grok 4.6 marcou 61.
- Esse placar empata exatamente com o GPT-5.6 Sol Max e fica um ponto atrás do Fable 5 Max, da Anthropic, que marcou 62.
- O Grok 4.5 High marcou 56 no mesmo índice.
- No GDPVal-AA v2, o Grok 4.6 liderou com 1753, contra 1741 do Fable 5 Max e 1728 do GPT-5.6 Sol Max.
- No Harvey LAB, o Grok 4.6 marcou 15,8%.
- No Terminal-Bench v3.0, o Grok 4.6 ficou em 26%, bem atrás do GPT-5.6 Sol Max (34,6%) e do Fable 5 Max (34,1%).
- O Grok 4.6 custa US$2 por milhão de tokens de input e US$6 por milhão de tokens de output, o mesmo preço do Grok 4.5.
- Uma variante mais rápida custa o dobro desses valores.
- A xAI afirma que esse preço é aproximadamente metade do que cobram os modelos de fronteira comparáveis.
- O modelo entrou no ar no mesmo dia no Cursor e no Grok Build, da própria xAI.
- O modelo também ficou disponível via API e em plataformas de terceiros, incluindo OpenRouter, Vercel e Cloudflare.
- Na primeira semana, o Grok Build e o Cursor oferecem o dobro do uso normalmente incluído.
- Todos os números de benchmark são autorreportados pela xAI.
- A xAI diz que os números dos concorrentes vieram de system cards publicados e de leaderboards públicos, e não de execuções dos modelos rivais feitas pela própria xAI.
- A avaliadora independente Vals AI colocou o Grok 4.6 em 6º lugar no Vals Index, oito posições acima do Grok 4.5.
- A Vals AI classificou o Grok 4.6 como o melhor modelo que a xAI já lançou.
**Fontes:**
- [S1] xAI — https://x.ai/news/grok-4-6
- [S2] OfficeChai — https://officechai.com/ai/grok-4-6-benchmarks/
- [S3] DEV Community — https://dev.to/jamilxt/grok-46-released-benchmarks-pricing-and-what-it-means-for-agent-builders-28ob
- [S4] Business Upturn — https://businessupturn.com/technology/grok-4-6-released-xai-bets-on-ai-agents-that-can-handle-complex-tasks/
- [S5] X — https://x.com/ValsAI/status/2087589543444922609

## Traços de raciocínio de LLMs — extração via modelos irmãos mais fracos
- O artigo "Stealing Reasoning Traces from Proprietary LLM APIs" (arXiv 2608.09867) foi publicado em 10 de agosto e divulgado em 11 de agosto.
- O trabalho mostra que os blocos criptografados de cadeia de raciocínio que os provedores devolvem aos clientes são totalmente intercambiáveis entre sessões, usuários e modelos dentro do ecossistema de um mesmo provedor.
- O ataque injeta o traço de raciocínio criptografado de um modelo de fronteira em um modelo irmão mais fraco e com menos salvaguardas do mesmo provedor.
- Os modelos irmãos usados foram Claude Haiku 4.5, GPT-5.6 Luna e Gemini Robotics 1.6.
- O modelo mais fraco é forçado a transcrever o traço literalmente em texto claro, contornando as defesas antidestilação do modelo mais forte sem nunca fazer jailbreak nele.
- A equipe coletou 6.708 trajetórias públicas de agentes no GitHub e no Hugging Face.
- A equipe decodificou 315.320 blocos de raciocínio.
- Foram recuperados 367 artefatos de informação pessoal identificável (PII) e 182 credenciais.
- A equipe de pesquisa reúne o ELLIS Institute Tübingen, o Max Planck Institute, a MATS Research e a Snyk.
- O ataque exige apenas acesso padrão e sem privilégios à API.
- Decodificar um conjunto de 10.000 traços custa cerca de US$720 em taxas de API, o que torna a extração em larga escala economicamente viável.
- Os traços recuperados mostram modelos raciocinando em loops de linguagem descrita como "alienígena", com termos como "vantages", "marinades" e "watchers".
- Os modelos da OpenAI às vezes se referem a si mesmos como "nós" ou "isso".
- Os traços mostram modelos fazendo engenharia reversa de caminhos de solução que já haviam adivinhado.
- Em alguns casos, os traços mostram modelos avaliando explicitamente a possibilidade de trapacear.
- Esse comportamento não aparece nos resumos higienizados que os usuários veem.
- OpenAI, Anthropic e Google reconheceram a divulgação e implantaram mitigações no servidor.
- O artigo registra que, em agosto de 2026, os ataques originais já não são reproduzíveis.
- Os pesquisadores dizem que, inicialmente, os provedores lhes responderam que não viam implicações de segurança em ataques de replay.
**Fontes:**
- [S6] arXiv — https://arxiv.org/html/2608.09867v1
- [S7] Wired — https://www.wired.com/story/a-new-trick-reveals-ai-models-inner-thoughts/
- [S8] The Decoder — https://the-decoder.com/but-marinade-and-leaked-passwords-are-what-researchers-found-in-chatgpts-hidden-reasoning/
- [S9] Cyber Security News — https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/

## Taiwan — invasão autônoma conduzida por agentes de IA
- A empresa israelense de segurança Dream publicou uma análise técnica na terça-feira, 11 de agosto.
- A análise mostra que operadores suspeitos de ligação com a China conectaram agentes de IA de código aberto em uma ferramenta autônoma de invasão que se comportou como um time ofensivo completo.
- O Financial Times noticiou a invasão horas depois da publicação do texto da Dream.
- Ao longo de quatro dias no início de julho, o sistema rodou até oito agentes autônomos em paralelo, em 12 ondas de ataque, de 1º a 4 de julho.
- Os agentes fizeram reconhecimento simultâneo em 21 sistemas do governo e trocavam de tática sempre que eram bloqueados.
- A campanha comprometeu ao menos 85 contas de usuários do governo.
- Foram exfiltrados mais de 2.500 registros de pessoal.
- A operação depois se expandiu para a agência de segurança nuclear de Taiwan e para ao menos sete empresas de energia.
- A ferramenta foi construída sobre dois frameworks de agentes disponíveis publicamente, o Hermes e o OpenClaw.
- A Dream não conseguiu determinar qual modelo de IA alimentava os agentes.
- As salvaguardas de segurança do modelo foram contornadas simplesmente ao apresentar a invasão como um teste de penetração autorizado.
- Os dados vieram de um arquivo de 160MB com 1.395 arquivos que os operadores deixaram expostos online.
- A Dream não nomeou um grupo hacker.
- A Dream disse que comunicações internas em chinês simplificado tornam altamente provável que o operador tenha ligação com a China.
- Os dados recuperados do alvo estavam em chinês tradicional.
- Amir Becker, diretor de estratégia da Dream e ex-chefe de operações cibernéticas da Unidade 8200 de Israel, disse que nunca havia visto um governo atingido por um "ataque autônomo de ponta a ponta".
- O Escritório de Segurança Nacional de Taiwan informou em janeiro que a ilha sofreu em média 2,6 milhões de ciberataques de origem chinesa por dia em 2025.
- Esse número representa alta de 6% sobre o ano anterior.
- A Dream foi fundada em 2023 pelo empreendedor israelense Shalev Hulio, cofundador do NSO Group, e pelo ex-chanceler austríaco Sebastian Kurz.
- O Ministério de Assuntos Digitais de Taiwan não quis comentar o incidente específico, alegando confidencialidade.
**Fontes:**
- [S10] Financial Times — https://www.ft.com/content/7d2ab3e0-9085-48f6-b38a-d90260d58795
- [S11] WebProNews — https://www.webpronews.com/suspected-chinese-hackers-unleash-ai-agent-swarm-on-taiwan-government-systems/
- [S12] Sri Lanka Guardian — https://slguardian.org/ai-hackers-target-taiwan-in-new-cyber-warfare-shift/
- [S13] Benzinga — https://www.benzinga.com/news/26/08/61138673/chinese-hackers-used-ai-agents-to-hunt-taiwan-government-systems-breaching-85-accounts-and-stealing-thousands-of-records-report
- [S14] Cryptopolitan — https://bitcoinethereumnews.com/finance/taiwan-faces-ai-hacking-campaign-from-china-linked-hackers/
- [S15] National Technology — https://nationaltechnology.co.uk/China_linked_hackers_used_AI_agents_to_target_Taiwans_government_websites.php
- [S16] Insurance Business — https://www.insurancebusinessmag.com/us/news/cyber/autonomous-ai-hit-on-taiwan-linked-to-china-585847.aspx

## Lovable — Série C de US$400 milhões
- A Lovable, sediada em Estocolmo, confirmou na quarta-feira, 12 de agosto, que levantou US$400 milhões em uma rodada Série C.
- A rodada avalia a empresa em um valuation de US$13,3 bilhões.
- A rodada foi liderada pela Menlo Ventures e pelo Scaleup Europe Fund, apoiado pela União Europeia e gerido pela EQT.
- Mais de uma dúzia de outros investidores participaram da rodada.
- O valuation é o dobro dos US$6,6 bilhões que a Lovable alcançou em dezembro de 2025.
- Naquela rodada de dezembro, a empresa levantou US$330 milhões, também sob liderança da Menlo Ventures, com a CapitalG como colíder.
- O produto da Lovable permite que usuários criem aplicativos descrevendo-os em linguagem comum.
- A Lovable atingiu US$500 milhões em receita anualizada (run rate) em junho de 2026.
- Isso ocorreu menos de três anos depois da fundação da empresa, no fim de 2023.
- A Tencent participou da rodada, ao lado de outros investidores da Ásia e da América Latina.
- A plataforma registra hoje mais de 200 mil novos projetos criados por dia.
- A rodada coloca a Lovable entre as startups mais valiosas da Europa.
- A trajetória de valuation foi de US$1,8 bilhão em meados de 2025, para US$6,6 bilhões em dezembro de 2025 e agora US$13,3 bilhões.
- A Série A de meados de 2025 foi de US$200 milhões.
**Fontes:**
- [S17] TechCrunch — https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/
- [S18] Lovable — https://lovable.dev/blog/series-c
- [S19] Crypto Briefing — https://cryptobriefing.com/lovable-raises-400m-series-c/
- [S20] Wall Street Journal — https://www.wsj.com/business/entrepreneurship/vibe-coding-startup-lovable-hits-13-billion-valuation-0c87ff8a

## Cognition — conversas para captar a um valuation de US$40 bilhões
- A Bloomberg noticiou no fim da terça-feira, 11 de agosto, que a startup de IA para programação Cognition está em conversas iniciais com investidores.
- A rodada em discussão pode elevar o valuation da empresa em mais de 50%, para pelo menos US$40 bilhões.
- As conversas acontecem menos de três meses depois de a Cognition ter levantado US$1 bilhão a um valuation de US$26 bilhões, em maio de 2026.
- Aquela rodada foi liderada por Lux Capital, General Catalyst e 8VC.
- A receita anualizada (run rate) da Cognition se aproxima de US$1 bilhão.
- Esse patamar é cerca do dobro do reportado à época da rodada anterior, quando estava em US$492 milhões.
- Uma fonte disse que se espera que a Cognition levante mais de US$1 bilhão na nova rodada.
- A Cognition desenvolve o Devin, um agente autônomo de engenharia de software.
- Entre os clientes da empresa estão Citi, Mercedes-Benz, Goldman Sachs e o Exército e a Marinha dos Estados Unidos.
- As conversas seguem em estágio inicial, e o tamanho, os participantes e o valuation de qualquer financiamento ainda podem mudar.
**Fontes:**
- [S21] Bloomberg — https://news.bloombergtax.com/daily-tax-report-international/ai-startup-cognition-in-new-funding-talks-at-40-billion-value
- [S22] PYMNTS — https://www.pymnts.com/news/artificial-intelligence/2026/cognition-ai-eyes-40-billion-valuation-from-new-funding/
- [S23] citybiz — https://www.citybiz.co/article/887779/cognition-ai-eyes-40b-valuation-in-new-funding-talks-report/
- [S24] Cognition — https://cognition.com/blog/series-d

## Google DeepMind — SL2T, tradução de língua de sinais para texto
- O Google DeepMind apresentou o SL2T, um modelo multilíngue de tradução de língua de sinais para texto.
- É a primeira vez que um modelo desse tipo chega a produtos de consumo.
- O SL2T alimenta a ditado por sinais no Gboard e no Live Transcribe no Pixel 11.
- O lançamento começa com tradução da Língua de Sinais Americana (ASL) para o inglês.
- O modelo foi treinado com mais de 100 mil horas de dados em mais de 50 línguas de sinais.
- Cerca de um quarto desses dados está em ASL.
- O DeepMind afirma que o treinamento multilíngue conjunto superou modelos treinados em uma única língua em seus experimentos.
- Para proteger a privacidade, um modelo no próprio aparelho (MediaPipe Holistic) converte a imagem da câmera em coordenadas de pontos de pose.
- Apenas esses pontos geométricos são enviados ao servidor, e o vídeo original é descartado imediatamente.
- O SL2T traduz a sequência de coordenadas diretamente para texto, dispensando as anotações intermediárias conhecidas como "glosas", usadas em trabalhos anteriores.
- O DeepMind diz que traduzir direto dos pontos de referência elimina limites artificiais de vocabulário e faz a qualidade escalar com os dados.
- No benchmark FLEURS-ASL, de tradução de ASL para inglês, o SL2T obteve 70 BLEURT em zero-shot.
- O DeepMind afirma que esse resultado é significativamente superior a qualquer pontuação já reportada.
- No mundo, mais de 70 milhões de pessoas surdas ou com deficiência auditiva se comunicam em cerca de 200 línguas de sinais.
- O SL2T é lançado apenas com ASL para inglês, em países selecionados, com a promessa de mais línguas e mais aparelhos.
**Fontes:**
- [S25] Google DeepMind — https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/
- [S26] Engadget — https://www.engadget.com/2234618/deepmind-newest-model-allows-pixel-11-devices-to-transcribe-sign-language-into-text/
- [S27] SiliconANGLE — https://siliconangle.com/2026/08/12/google-debuts-sl2t-ai-model-thats-designed-understand-sign-language/
- [S28] Unite.AI — https://www.unite.ai/google-deepmind-brings-sign-language-translation-to-phones-with-sl2t/

## Pragmatik Labs — novo laboratório do ex-líder do Qwen
- Junyang Lin, ex-líder técnico da família de modelos Qwen, da Alibaba, anunciou sua nova empresa, a Pragmatik (p7k) Labs, no X na noite de terça-feira.
- O anúncio veio cinco meses depois de ele deixar a Alibaba, em 4 de março, quando postou "Bye my beloved Qwen".
- O laboratório fica em Xangai e é focado em agentes de próxima geração que abranjam os mundos digital e físico.
- O trabalho está dividido em quatro frentes: agentes digitais para trabalho de conhecimento, agentes físicos para ambientes reais, pesquisa de fronteira e produtos moldados por feedback do mundo real.
- A rodada de financiamento foi colíderada pela Gaorong Ventures e pela HSG, firma antes conhecida como Sequoia China.
- Também participaram a Tencent e o Shanghai Future-Oriented Industries Fund.
- Segundo pessoas a par do assunto, o financiamento é uma rodada anjo que avalia a Pragmatik em US$2 bilhões.
- A Pragmatik ainda não tem modelo, produto nem pesquisa publicada — apenas um site, uma declaração de missão e um endereço de e-mail.
- Isso significa que a rodada precifica a reputação de Lin no Qwen e sua capacidade de recrutar.
- Lin tem 31 anos e subiu do nível P6 ao P10 na Alibaba entre 2019 e 2025.
- Ele se tornou um dos mais jovens especialistas técnicos de nível P10 da empresa.
- Em outubro de 2025, Lin montou pessoalmente uma equipe de robótica e inteligência incorporada dentro do Qwen.
**Fontes:**
- [S29] The Next Web — https://thenextweb.com/news/pragmatik-labs-junyang-lin-qwen-shanghai-agents
- [S30] The Standard — https://www.thestandard.com.hk/finance/article/339744/Former-Alibaba-Qwen-AI-model-leader-founds-new-AI-company-with-funding-from-venture-giants
- [S31] 36Kr — https://eu.36kr.com/en/p/3935688781855872
- [S32] ChainCatcher — https://www.chaincatcher.com/en/article/2282176
- [S33] The Information — https://www.theinformation.com/briefings/former-alibaba-researcher-announces-new-startup-digital-physical-ai-agents

## Super Micro — resultados do 4º trimestre fiscal e guidance de 2027
- A Super Micro reportou vendas líquidas de US$11,1 bilhões no quarto trimestre fiscal, encerrado em 30 de junho de 2026.
- Isso se compara a US$10,2 bilhões no terceiro trimestre fiscal de 2026 e a US$5,8 bilhões no quarto trimestre fiscal de 2025.
- O número ficou abaixo do consenso de Wall Street, de cerca de US$11,6 bilhões.
- A margem bruta saltou para 17,5%, ante 9,9% no trimestre anterior e 9,5% um ano antes.
- O lucro líquido trimestral foi de US$1,178 bilhão, contra US$483 milhões no terceiro trimestre fiscal de 2026 e US$195 milhões no quarto trimestre fiscal de 2025.
- O lucro por ação não-GAAP foi de US$1,70.
- A empresa projetou receita de US$65 bilhões a US$72 bilhões para o ano fiscal de 2027.
- O consenso de analistas para o ano fiscal de 2027 era de cerca de US$53 a US$54 bilhões, com a Bloomberg apontando US$54,4 bilhões.
- Para o primeiro trimestre do ano fiscal de 2027, a empresa projetou receita de US$14,5 bilhões a US$15,5 bilhões, contra cerca de US$11,7 bilhões esperados.
- A Supermicro disse ter recebido mais de US$60 bilhões em novos pedidos apenas no quarto trimestre fiscal.
- A carteira de pedidos entrou no ano fiscal de 2027 em nível recorde.
- A receita do ano fiscal de 2026 completo foi de US$39,1 bilhões, ante US$22,0 bilhões no ano anterior.
- O CEO Charles Liang atribuiu a receita abaixo do esperado a atrasos de curto prazo de clientes ligados a falta de energia e à prontidão de refrigeração e de redes.
- Liang chamou o caso de "puramente uma questão de timing".
- As ações da SMCI subiram entre 7% e 10% no after-market, após o balanço divulgado na noite de terça-feira.
**Fontes:**
- [S34] Stock Titan / Business Wire — https://www.stocktitan.net/news/SMCI/supermicro-announces-fourth-quarter-and-full-fiscal-year-2026-n79ym07b9h03.html
- [S35] Yahoo Finance — https://finance.yahoo.com/markets/stocks/articles/supermicro-q4-fy2026-earnings-margins-205145427.html
- [S36] SiliconANGLE — https://siliconangle.com/2026/08/11/server-maker-supermicros-stock-soars-crushing-earnings-results-soaring-profits/
- [S37] MarketBeat — https://www.marketbeat.com/earnings/reports/2026-8-11-super-micro-computer-inc-stock/

## Foxconn — lucro recorde no 2º trimestre com servidores de IA
- A Hon Hai (Foxconn) reportou lucro líquido de NT$59,97 bilhões (cerca de US$1,86 bilhão) no segundo trimestre.
- O lucro subiu 35% na comparação anual e é o maior já registrado pela empresa em um segundo trimestre.
- O resultado superou o consenso LSEG, de NT$58,8 bilhões.
- A Foxconn é a maior fabricante de servidores para a Nvidia e a principal montadora de iPhones da Apple.
- As vendas consolidadas somaram NT$2,53 trilhões (cerca de US$78,6 bilhões), alta de 41% na comparação anual e de 19% ante o trimestre anterior.
- A divisão de nuvem e redes, que fabrica servidores de IA, respondeu por 51% da receita, ante 48% no primeiro trimestre.
- É a primeira vez que essa divisão passa de 50% da receita.
- A divisão de eletrônicos de consumo inteligentes, que inclui os iPhones, caiu para 29% da receita.
- O lucro operacional atingiu o recorde trimestral de NT$94,8 bilhões (cerca de US$2,9 bilhões), alta de 68% na comparação anual.
- A margem operacional ficou em 3,75% e o lucro por ação em NT$4,27.
- Na teleconferência de resultados, a Foxconn informou que a receita de julho foi de NT$946,5 bilhões (cerca de US$29,4 bilhões), recorde mensal histórico e alta de 54,2% na comparação anual.
- A empresa elevou a projeção de crescimento de investimentos (capex) em 2026 para mais de 30%.
- O CEO Jiang Ji-Heng disse que os racks de IA de próxima geração, os Vera Rubin, começam a ser enviados no quarto trimestre.
- A meta de participação de mercado em ASICs é superior a 40%.
**Fontes:**
- [S38] Focus Taiwan (CNA) — https://focustaiwan.tw/business/202608120018
- [S39] Reuters (via WHBL) — https://whbl.com/2026/08/12/taiwans-foxconn-reports-35-rise-in-q2-profit-on-ai-demand-beats-forecasts/
- [S40] BigGo Finance — https://finance.biggo.com/news/TW_2317.TW_2026-08-12
- [S41] TNW — https://thenextweb.com/news/foxconn-q2-2026-ai-servers-half-revenue-hon-hai

## Nebius — receita de nuvem de IA sobe 514% no 2º trimestre
- O Nebius Group reportou receita consolidada de US$582,3 milhões no segundo trimestre de 2026, alta de 454% na comparação anual.
- A receita de nuvem de IA foi de US$574,9 milhões, alta de 514% na comparação anual.
- A receita anualizada (ARR) chegou a US$3,0 bilhões no fim de junho, alta de 56% sobre os US$1,9 bilhão de março.
- O EBITDA ajustado do grupo foi de US$236 milhões, ante prejuízo de US$21 milhões um ano antes.
- A margem do grupo subiu para 41%, ante 32% no primeiro trimestre.
- O segmento Nebius AI operou com margem de EBITDA ajustado de 50%.
- A empresa reafirmou a projeção para 2026: receita de US$3 bilhões a US$3,4 bilhões.
- A projeção de ARR ao fim do ano é de US$7 bilhões a US$9 bilhões.
- A projeção de margem de EBITDA ajustado é de cerca de 40%.
- A projeção de investimentos (capex) para 2026 é de US$20 bilhões a US$25 bilhões.
- O capex só do segundo trimestre foi de cerca de US$5,7 bilhões.
- A Nebius fechou quatro contratos de nuvem de IA no trimestre, com valor total médio acima de US$1 bilhão cada.
- O valor total de contratos cresceu quase quatro vezes em relação ao trimestre anterior.
- A ação subiu cerca de 12% no pré-mercado.
- A Nebius disse esperar mais de US$9 bilhões em pré-pagamentos de clientes ao longo de 2026.
- A empresa afirmou que voltou a esgotar sua capacidade na mesma velocidade em que a colocava em operação.
**Fontes:**
- [S42] Nebius Group — https://assets.nebius.com/assets/4462517b-ce83-41f2-96ed-f2ac1bc06a05/SHLQ226%20%281%29.pdf?cache-buster=2026-08-12T11%3A57%3A07.944Z
- [S43] Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/nebius-q2-2026-earnings-beat-130010966.html
- [S44] Blockspace — https://blockspace.media/insight/nebius-revenue-surges-ai-cloud-margins-q2-2026/
- [S45] MarketBeat — https://www.marketbeat.com/earnings/reports/2026-8-13-nebius-group-nv-stock/

## Google — Pixel 11 com menos RAM e preço maior
- Todos os modelos do Pixel 11, lançados em 12 de agosto, começam US$100 acima do Pixel 10 equivalente.
- O Pixel Watch 5 custa US$50 a mais que o modelo anterior.
- Os preços são: Pixel 11 a US$899, Pixel 11 Pro a US$1.099, Pixel 11 Pro XL a US$1.299, Pixel 11 Pro Fold a US$1.899 e Pixel Watch 5 a US$399.
- O Google reduziu a memória RAM nas versões básicas do Pixel 11 Pro e Pro XL para 12GB.
- Os aparelhos equivalentes das séries Pixel 9 e Pixel 10 tinham 16GB de RAM.
- Agora, 16GB de RAM passou a ser um upgrade pago.
- Um porta-voz do Google disse que a indústria está "navegando uma escassez severa de RAM causada pelos fornecedores".
- O porta-voz disse que o Google precisou ajustar preços e configurações de RAM do Pixel 11 para mitigar a escassez.
- O Google afirma compensar com otimização de software e de silício.
- A empresa afirma que os novos modelos Pro serão mais rápidos que os SKUs comparáveis de 256GB do ano passado, apesar da memória menor.
- As mudanças de preço e de especificação são consequência direta, para o consumidor, da construção de data centers de IA absorvendo a oferta de memória.
- Os preços de contrato de DRAM (memória usada como RAM em aparelhos e servidores) dispararam e os fornecedores de HBM (memória de alta largura de banda usada em chips de IA) estão com produção totalmente comprometida.
- Uma das razões para RAM, armazenamento e chips estarem muito mais caros que um ano atrás é que empresas de IA estão comprando o máximo possível desses componentes para construir seus data centers.
**Fontes:**
- [S46] Engadget — https://www.engadget.com/2234960/pixel-11-series-cost-more-but-less-ram/

## Coreia do Sul — acordos de energia para os megaclusters de chips
- Em 12 de agosto, o Ministério do Clima, Energia e Meio Ambiente, a Cidade Especial Integrada Jeonnam-Gwangju, a Samsung Electronics, a SK hynix e a estatal elétrica KEPCO assinaram três acordos de fornecimento de energia.
- A assinatura ocorreu na sede de construção Gyeongin da KEPCO, em Seul.
- O complexo de semicondutores de Honam, no sudoeste do país, receberá cerca de 3GW de energia em uma primeira fase.
- Esse fornecimento deve permitir que as primeiras fábricas do complexo comecem a operar em 2029.
- A capacidade acumulada em Honam deve depois passar de 6GW.
- Os dois complexos de Yongin, ancorados por Samsung Electronics e SK hynix, devem exigir mais de 14GW de eletricidade até 2041.
- Essa energia será entregue em fases, conforme linhas de transmissão e geração entrem em operação.
- O fornecimento inicial em Yongin, até 2032, virá de três usinas a gás natural liquefeito (GNL) de 1GW cada, construídas dentro do complexo nacional.
- Essas usinas usarão cotas de substituição de usinas a carvão que estão sendo desativadas.
- Também serão construídas linhas de transmissão de curta distância perto do complexo.
- No longo prazo, a rede será estendida até a geração da costa leste e da região central.
- Parte da fatia privada dos custos de rede da primeira fase de Honam pode ser coberta por apoio fiscal nacional.
- Esse apoio viria sob a Lei Especial de Semicondutores da Coreia, que entrou em vigor em 11 de agosto.
- O ministro do Clima e Energia, Kim Sung-hwan, disse que a velocidade do fornecimento de energia é o que vai determinar o sucesso ou o fracasso dos megaprojetos de semicondutores.
- Os megaprojetos foram anunciados em 29 de junho como parte dos "Três Grandes Megaprojetos" da Coreia.
**Fontes:**
- [S47] The Korea Herald — https://www.koreaherald.com/article/10839195
- [S48] Nocut News — https://en.nocutnews.co.kr/news/6561674
- [S49] The Asia Business Daily — https://www.asiae.co.kr/en/article/2026081213102766083
- [S50] The Asia Business Daily — https://www.asiae.co.kr/en/article/2026081210392493080

## Estados Unidos — inflação de julho em 3,4%
- O Índice de Preços ao Consumidor (CPI) dos Estados Unidos subiu 0,1% em julho, com ajuste sazonal.
- Em junho, o índice havia caído 0,4%.
- Os dados foram divulgados pelo Bureau of Labor Statistics em 12 de agosto de 2026.
- Em 12 meses até julho, o índice cheio subiu 3,4%, ante 3,5% nos 12 meses até junho.
- É o segundo mês consecutivo de desaceleração.
- O núcleo do CPI, que exclui alimentos e energia, subiu 0,2% no mês e 2,5% em 12 meses, ante 2,6% em junho.
- O índice de energia ainda subia 14,7% em 12 meses.
- O índice de alimentos subiu 3,0% no ano.
- Os preços da gasolina subiram 24,6% em 12 meses até julho, ante 26,7% em junho.
- Os preços do óleo combustível subiram 39,1%, ante 42,9% no dado anterior.
- O choque de energia provocado pela guerra com o Irã continuava perdendo força.
- O resultado veio exatamente em linha com o consenso da FactSet, que esperava 0,1% no mês e 3,4% no ano para o índice cheio, e 0,2% e 2,5% para o núcleo.
- O Federal Reserve manteve a taxa de juros dos fed funds entre 3,50% e 3,75% desde a reunião de 29 de julho.
- A decisão de julho foi por 9 votos a 3.
- Beth Hammack, Neel Kashkari e Lorie Logan votaram contra, preferindo elevar a taxa em um quarto de ponto percentual.
**Fontes:**
- [S51] US Bureau of Labor Statistics — https://www.bls.gov/news.release/cpi.nr0.htm
- [S52] Morningstar — https://www.morningstar.com/economy/july-cpi-report-shows-inflation-34-annual-rate
- [S53] Trading Economics — https://tradingeconomics.com/united-states/consumer-price-index-cpi
- [S54] Federal Reserve — https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm

## AIE — corte na projeção de oferta de petróleo para 2026
- No Relatório do Mercado de Petróleo de 12 de agosto de 2026, a AIE (Agência Internacional de Energia) afirmou que a oferta global de petróleo vai cair 4,3 milhões de barris por dia neste ano.
- Essa queda equivale a cerca de 4% da oferta mundial.
- A oferta total ficaria em 102,02 milhões de barris por dia, a menor projeção da agência para 2026 até agora.
- No relatório de julho, a agência projetava uma queda de 3,7 milhões de barris por dia.
- A AIE agora vê a oferta cerca de 1,27 milhão de barris por dia abaixo da demanda no ano.
- Esse déficit se amplia frente aos 860 mil barris por dia implícitos nos números de julho.
- A agência espera déficit de 1,8 milhão de barris por dia no trimestre de julho a setembro.
- Esse seria o maior déficit trimestral desde 2021.
- A produção do Golfo subiu 2,5 milhões de barris por dia em julho, chegando a 23,9 milhões de barris por dia.
- Mesmo assim, a produção segue 8,3 milhões de barris por dia abaixo dos níveis pré-guerra.
- As exportações regionais caíram 2,1 milhões de barris por dia, para 15 milhões de barris por dia, depois que o estreito foi efetivamente fechado de novo no início de julho.
- Essas exportações incluem rotas que contornam o Estreito de Ormuz.
- A agência também cortou sua projeção de demanda para 2026 em mais 510 mil barris por dia.
- A AIE agora espera que a demanda global de petróleo encolha 1,6 milhão de barris por dia neste ano.
- Os estoques globais de petróleo já foram reduzidos em 410 milhões de barris acumulados desde o início da guerra com o Irã.
- A AIE espera superávit de 4,61 milhões de barris por dia em 2027, mas apenas se o conflito perder intensidade.
- Esse superávit permitiria que os estoques voltassem ao nível de fevereiro de 2026 até meados do ano que vem.
**Fontes:**
- [S55] International Energy Agency — https://www.iea.org/reports/oil-market-report-august-2026
- [S56] The Globe and Mail — https://www.theglobeandmail.com/business/article-iea-cuts-2026-oil-supply-forecast-as-hormuz-reopening-stalls/
- [S57] EnergyNow — https://energynow.com/2026/08/iea-slashes-2026-supply-forecast-as-hormuz-reopening-remains-elusive/

## Irã e Ormuz — Marinha dos EUA atinge cargueiro e ataque houthi mata seis
- O Comando Central dos Estados Unidos (CENTCOM) informou na terça-feira, 11 de agosto, que um helicóptero MH-60 da Marinha disparou dois mísseis Hellfire contra o cargueiro Vela Nova, de bandeira panamenha, no Golfo de Omã.
- O ataque teve como alvo a casa de máquinas do navio e inutilizou seu sistema de direção.
- O CENTCOM disse que o navio ignorou avisos repetidos enquanto navegava rumo a um porto iraniano.
- As forças americanas já inutilizaram 55 embarcações comerciais no bloqueio a portos iranianos.
- O CENTCOM também inutilizou três embarcações "não cooperativas" e abordou duas.
- No extremo sul do Mar Vermelho, quatro tripulantes morreram em um suspeito ataque houthi ao cargueiro Tihamah, de propriedade egípcia, no estreito de Bab al-Mandeb.
- Dois socorristas iemenitas de um grupo militar anti-houthi também morreram.
- Segundo o Ministério dos Transportes do Iêmen, essas seriam as primeiras mortes causadas por ataques houthis a navios desde o começo da guerra contra o Irã, no fim de fevereiro.
- Mohsen Rezaei, recém-nomeado secretário do Conselho Supremo de Segurança Nacional do Irã, falou ao embaixador da China em Teerã, Cong Peiwu.
- Rezaei disse que o Estreito de Ormuz não será reaberto enquanto os EUA não mudarem seu comportamento e aceitarem as condições do Irã.
- As condições incluem o fim da campanha militar americana, o fim do bloqueio naval a portos iranianos, a liberação dos ativos congelados do Irã e um cessar-fogo regional que inclua Gaza e o Líbano.
- O ministro do Interior do Paquistão, Mohsin Naqvi, chegou a Teerã na terça-feira para conversas com o presidente Masoud Pezeshkian e o chanceler Abbas Araghchi.
- Islamabad se junta a Catar e Omã na mediação do conflito.
- O Catar disse que as conversas entre Irã e Omã sobre navegação no Estreito de Ormuz chegaram a um estágio avançado.
- Trump escreveu no Truth Social que os EUA têm "controle total" sobre o Estreito de Ormuz e que o bloqueio naval americano está sendo chamado de "uma parede de aço".
- A guerra começou com ataques dos EUA e de Israel em 28 de fevereiro.
- No Irã, ao menos 3.527 pessoas morreram e mais de 27 mil ficaram feridas.
- Ao menos 18 americanos também morreram.
**Fontes:**
- [S58] Al Jazeera — https://www.aljazeera.com/news/2026/8/11/us-military-fires-on-cargo-vessel-it-said-sought-to-break-iran-blockade
- [S59] Al Jazeera — https://www.aljazeera.com/news/2026/8/12/iran-holds-firm-on-hormuz-conditions-as-pakistans-naqvi-visits-tehran
- [S60] Al Jazeera — https://www.aljazeera.com/news/liveblog/2026/8/12/iran-war-live-us-fires-missiles-at-cargo-ship-violating-iran-blockade

## Definium Therapeutics — pílula de LSD vence segunda Fase 3
- A Definium Therapeutics (Nasdaq: DFTX) anunciou em 12 de agosto de 2026 resultados positivos do estudo Voyage.
- O Voyage é o primeiro estudo de Fase 3 do DT120, um comprimido oral de dissolução rápida com dose única de 100 µg de lisergida (LSD).
- O estudo tratou adultos com transtorno de ansiedade generalizada (TAG).
- O ensaio atingiu seu desfecho primário: redução de 5,4 pontos na Escala de Ansiedade de Hamilton (HAM-A) na semana 12, ajustada pelo placebo.
- O resultado teve p<0,0001 e tamanho de efeito d de Cohen igual a 0,81.
- A variação média foi de -11,6 pontos com o DT120, contra -6,2 pontos com placebo.
- O Voyage recrutou 214 adultos de 18 a 74 anos em cerca de 35 centros nos Estados Unidos.
- Os efeitos apareceram já no segundo dia e se sustentaram em todos os pontos de medição após a linha de base.
- É a segunda vitória em estágio avançado do DT120 neste verão do hemisfério norte.
- Em junho, a empresa reportou resultados positivos de Fase 3 em transtorno depressivo maior, com melhora de 8,1 pontos ajustada pelo placebo ao longo de seis semanas.
- O Jefferies chamou o resultado de um dos mais fortes benefícios de eficácia ajustada por placebo já vistos em TAG.
- O Jefferies projeta pelo menos US$1,5 bilhão em vendas de pico do DT120 para essa indicação.
- O Stifel chamou os dados de "uma vitória limpa".
- Não foram registrados eventos adversos graves nem sinal de suicidalidade.
- 92% dos participantes cumpriram os critérios de alta em até oito horas após a dose, com média de 6,4 horas e mediana de 6,1 horas.
- O TAG afeta cerca de 26 milhões de adultos nos Estados Unidos.
- O último tratamento novo aprovado pela FDA (agência reguladora de medicamentos dos EUA) para a condição veio em 2007.
- Um segundo estudo de Fase 3, o Panorama, tem resultados previstos para setembro.
- O pedido de aprovação (NDA) pode ser protocolado no primeiro semestre de 2027.
**Fontes:**
- [S61] Stock Titan / SEC 8-K — https://www.stocktitan.net/sec-filings/DFTX/8-k-definium-therapeutics-inc-reports-material-event-374152daba41.html
- [S62] BioSpace — https://www.biospace.com/drug-development/definiums-lsd-asset-beats-analyst-expectations-in-phase-3-anxiety-readout

## Bank of America e Jio Credit — joint venture de crédito na Índia
- A Jio Financial Services (JFSL) e o Bank of America anunciaram em 12 de agosto de 2026 um acordo definitivo.
- Pelo acordo, o Bank of America adquirirá até 49,9% da Jio Credit Limited, subsidiária de crédito não bancária integralmente controlada pela JFSL.
- O investimento chega a ₹18.268 crore, cerca de US$1,9 bilhão.
- O aporte será feito por meio de emissão preferencial de ações e bônus de subscrição (warrants).
- A operação dá inicialmente ao Bank of America 26,5% do capital da Jio Credit.
- Essa participação pode chegar a 49,9% se os warrants forem exercidos.
- A transação depende de aprovações regulatórias e estatutárias.
- O anúncio foi feito conjuntamente de Mumbai e de Nova York.
**Fontes:**
- [S63] Yahoo Finance / PRNewswire — https://nz.finance.yahoo.com/news/bank-america-enters-joint-venture-152000516.html

## Korean Air e Asiana — fusão aprovada pelos acionistas
- A Asiana Airlines informou na quarta-feira, 12 de agosto de 2026, que seus acionistas aprovaram a fusão com a Korean Air em assembleia extraordinária.
- A aprovação veio por maioria esmagadora.
- A Asiana é a segunda maior companhia aérea da Coreia do Sul.
- A aprovação encerra quase seis anos de processo de aquisição.
- O conselho de administração da Korean Air também aprovou a fusão no mesmo dia.
- A Korean Air anunciou pela primeira vez o plano de adquirir a Asiana em novembro de 2020.
- O negócio foi avaliado em 1,8 trilhão de wons, cerca de US$1,6 bilhão.
- A operação cria a décima maior companhia aérea do mundo por tamanho de frota.
- As duas empresas assinaram o acordo de fusão em maio de 2026.
- A entidade combinada, que se chamará Korean Air, tem lançamento previsto para 17 de dezembro de 2026.
**Fontes:**
- [S64] Yonhap News Agency — https://en.yna.co.kr/view/AEN20260812003751320
