# [Tech] - Bem-vindo(a) a 20 de Julho de 2026

Atrás de qual rival a Alibaba coloca seu novo Qwen3.8-Max? Como o governo Trump pretende conter os modelos de IA chineses? O que a Microsoft acaba de adotar da AMD para o Azure?

Por: Guilherme Saboia e Vinicius Gushiken

### Alibaba apresenta o Qwen3.8-Max de 2,4 trilhões de parâmetros e o coloca atrás só da Anthropic
- **Prévia.** A Alibaba mostrou na World AI Conference de Xangai (domingo, 19 jul) o [Qwen3.8-Max-Preview](https://www.siliconrepublic.com/business/alibaba-unveils-qwen3-8-max-preview), modelo de 2,4 trilhões de parâmetros em arquitetura esparsa Mixture-of-Experts (mistura de especialistas) e o primeiro Qwen acima de 1 trilhão a processar imagem, vídeo e documentos. Está disponível via assinatura Token Plan e nas plataformas Qoder e QoderWork a 10% do preço padrão no período de teste.
- **Ranking.** A empresa chama o modelo de ["um dos mais poderosos disponíveis hoje, perdendo apenas para o Fable 5"](https://www.scmp.com/tech/article/3361119/alibaba-says-newest-qwen-ai-model-second-only-anthropics-claude-fable-5), o topo da Anthropic, mas não publicou model card, contagem de parâmetros ativados nem benchmarks, e nenhuma avaliação independente confirmou a classificação.
- **Mercado.** A prévia vem dias após o [Kimi K3 da Moonshot](https://siliconangle.com/2026/07/19/alibaba-previews-qwen3-8-claims-second-claude-fable-5/), modelo de pesos abertos de 2,8 trilhões de parâmetros; a versão de pesos abertos do Qwen foi prometida "em breve", sem data, e as ações da Alibaba subiram mais de 3,5% na negociação overnight de segunda.

### Governo Trump retoma plano para restringir modelos de IA open-source chineses
- **Gatilho.** Áreas do governo reacenderam o esforço de [banir de facto modelos open-source estrangeiros](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) após a ascensão do Kimi na semana passada, movimento que, segundo fontes, poderia consolidar o domínio de OpenAI e Anthropic.
- **Ferramentas.** Em vez de um banimento direto, as fontes descrevem uma abordagem ["mais lenta e mais durável"](https://the-decoder.com/trump-administration-reportedly-builds-a-slow-motion-ban-on-chinese-ai-models-through-sanctions-and-soft-pressure/): incluir laboratórios chineses na Entity List (lista de restrições de exportação), usar regras de compras públicas, ameaças de sanções e advertências da NSA e do diretor cibernético sobre possíveis backdoors (acessos ocultos).
- **Política.** Também se estuda uma [ordem executiva](https://www.morningstar.com/news/marketwatch/2026072055/as-the-battle-for-ai-supremacy-intensifies-trump-white-house-reportedly-contemplates-a-ban-on-chinese-models) que responsabilizaria empresas dos EUA que hospedem modelos chineses; a saída do assessor Sriram Krishnan, contrário a qualquer intervenção, teria fortalecido os defensores das restrições.

### Microsoft vai implantar o sistema de IA em rack Helios, da AMD, no Azure
- **Acordo.** AMD e Microsoft ampliaram a parceria estratégica (20 jul): o [Helios em escala de rack](https://za.investing.com/news/assorted/microsoft-to-deploy-amd-helios-gpus-on-azure-for-ai-inference-432SI-4376501) vai alimentar inferência de modelos de fronteira para a Microsoft, seus clientes e os serviços Azure AI, com envios a clientes a partir do segundo semestre de 2026.
- **Hardware.** Cada rack integra [72 GPUs Instinct MI455X](https://www.amd.com/en/products/rackscale-solutions/helios.html) com CPUs EPYC "Venice" e rede Pensando "Vulcano" (UALink) sobre o formato Open Rack Wide da Meta; cada GPU carrega 432 GB de memória HBM4 (alta largura de banda) com até 19,6 TB/s.
- **Azure.** O Azure ganha [duas novas séries de máquinas virtuais](https://www.europesays.com/uk/1100635/) com EPYC "Venice" de 6ª geração (HDv2 para IA agêntica, HXv2 para projeto de chips); a Microsoft se junta a Meta, OpenAI, Oracle e TCS no Helios, e a Meta já prometeu até 6 GW de GPUs AMD.

---

#### Capital & IPOs
- **Moonshot AI.** A dona do Kimi K3 [pausou novas assinaturas](https://invezz.com/news/2026/07/20/moonshot-ai-pauses-kimi-k3-subscriptions-as-demand-strains-compute-capacity/) no domingo após a demanda causar "desafios de computação sem precedentes", com vendas diárias seis vezes maiores desde o lançamento. A empresa busca um IPO em Hong Kong em seis meses e fecha uma rodada que pode avaliá-la em mais de US$30 bilhões, contra US$20 bilhões em maio, com receita recorrente anual (ARR) de US$300 milhões.
- **CuspAI.** A startup britânica de descoberta de materiais por IA levantou uma [Série B de US$450 milhões](https://tech.eu/2026/07/20/jeff-bezos-and-sovereign-ai-back-cuspai-in-450m-raise/) liderada por Kleiner Perkins e NEA, com a Bezos Expeditions de Jeff Bezos, a um *valuation* de US$2,6 bilhões, cerca de cinco vezes o de setembro de 2025. Ela lançou a coalizão "AI Materials Foundry" com mais de 45 parceiros (NVIDIA, Meta, Samsung, Hyundai) e direciona 80% da pesquisa a materiais de semicondutores.
- **Zhongji Innolight.** A fabricante chinesa de transceptores ópticos para data centers sonda investidores para uma [listagem em Hong Kong de até US$8 bilhões](https://www.businesstimes.com.sg/companies-markets/chinas-innolight-eyes-us8-billion-hong-kong-ipo-potentially-citys-largest-seven-years), a maior da cidade desde o Alibaba em 2019; as ações subiram até 8% na segunda após a aprovação da bolsa.

#### Infraestrutura & chips
- **Google.** A empresa desenvolve o chip de servidor ["Frozen v2"](https://www.republicworld.com/tech/google-may-be-building-a-new-ai-chip-with-gemini-baked-directly-into-the-hardware-2026-07-20-132936), que fixa partes do modelo Gemini diretamente no silício e promete eficiência de seis a dez vezes maior por token servido; a implantação está prevista para 2028 e visa aliviar um aperto de computação e energia que já levou o Google Cloud a recusar negócios.
- **TSMC.** O CFO disse que a empresa vai [acelerar a expansão no Arizona](https://www.cnbc.com/2026/07/20/tsmc-arizona-fab-capacity-ai-chip-demand.html); o aporte extra de US$100 bilhões anunciado em 16 jul leva o total local a US$265 bilhões e elevou o capex (investimento de capital) de 2026 para US$60 a US$64 bilhões, com a escassez de mão de obra de construção como principal gargalo.
- **Amentum.** A NNSA do Departamento de Energia [selecionou a empresa](https://seekingalpha.com/news/4615266-amentum-selected-to-negotiate-phased-lease-for-doe-ai-data-center-and-power-project) para negociar um arrendamento e erguer um data center de IA de 1 GW no Savannah River Site, na Carolina do Sul, apoiado por cerca de 2 GW de geração local a gás com transição para nuclear; as ações subiram 5,7% no pré-mercado.

#### Fusões & aquisições
- **Blackstone.** O fundo de *private equity* fechou acordo para assumir o controle da sul-coreana [Futronic](https://apac.entrepreneur.com/business-news/blackstones-futronic-deal-puts-a-676-mn-value-on-south-koreas-robotics-supply-chain), fabricante de atuadores de alta precisão para automotivo e robótica, em transação que avalia a empresa em cerca de US$676 milhões; a gestora aposta que os atuadores dentro dos robôs guardam as margens duráveis conforme a IA converge com o mundo físico.
- **Samsung Biologics.** A companhia fez uma [oferta em dinheiro de US$1,8 bilhão](https://www.cnbc.com/2026/07/20/samsung-biologics-polypeptide-group-deal-switzerland.html) pela suíça PolyPeptide, a maior fusão da história da indústria farmacêutica coreana, para entrar em terapias com peptídeos e surfar a demanda por medicamentos GLP-1 de emagrecimento e diabetes.

#### Regulação & governo
- **CAISI.** Chris Fall [renuncia à direção](https://www.axios.com/2026/07/20/trump-ai-security-agency-head-resigns) do instituto federal de testes de IA apenas três meses após assumir, deixando um órgão-chave sem liderança permanente; ele havia substituído Collin Burns, ex-pesquisador da Anthropic e da OpenAI.
- **AliExpress.** A Comissão Europeia multou o *marketplace* do Alibaba em [€550 milhões (US$629 milhões)](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1654), a maior penalidade já aplicada sob o Digital Services Act (Lei de Serviços Digitais), por falhar em conter produtos inseguros e falsificados; a plataforma tem até 20 de outubro para apresentar um plano de ação.

#### Ferramentas & apps
- **App Store.** O número de novos apps na loja da Apple dobrou para cerca de [560 mil no primeiro semestre de 2026](https://www.nytimes.com/2026/07/20/technology/apple-app-store-vibecoding.html), a caminho de superar o total de todo o ano de 2025, puxado por *vibecoding* (descrever a ideia em linguagem natural para a IA gerar o código); as submissões do primeiro trimestre saltaram 84% no ano, e a Sensor Tower credita o Claude Code e o Codex.

#### Mundo
- **EUA e Irã.** A [nona noite consecutiva de ataques](https://apnews.com/article/iran-us-hormuz-strait-war-july-19-2026-63996576847424ab5f22887f38037ce8) do CENTCOM elevou a 17 o número de militares americanos mortos, com mais de 430 feridos; o Irã disparou drones e mísseis contra Kuwait, Bahrein e Jordânia, e Teerã mantém o Estreito de Ormuz fechado.
- **Petróleo.** O Brent atingiu [US$90,75 por barril](https://www.axios.com/2026/07/19/oil-prices-90-middle-east-fighting-gas-prices), alta de cerca de 3% e máxima de cinco semanas, com o colapso do tráfego de petroleiros em Ormuz; a gasolina nos EUA beira US$4 por galão e os estoques excedentes do início da guerra já foram quase esgotados.
- **Rússia.** A [maior barragem de mísseis balísticos sobre Kyiv](https://www.aljazeera.com/news/2026/7/19/russia-launches-largest-ballistic-missile-attack-on-kyiv-since-start-of-war) desde 2022, com 41 mísseis e 125 drones, matou ao menos 20 pessoas na Ucrânia; as defesas abateram 17 de 25 balísticos, sinal de estoques de interceptadores Patriot reabastecidos.

---

#### Leia também
- [Espanha combate incêndio ao norte de Madri que já queimou 13 mil hectares](https://www.france24.com/en/europe/20260719-wildfire-scorches-12-000-hectares-in-central-spain-s-guadalajara-province)
- [Enchentes e deslizamentos matam ao menos 12 em Jammu e Caxemira](https://www.thehindu.com/news/national/jammu-and-kashmir/heavy-downpour-slows-search-and-rescue-efforts-in-flood-hit-jk-death-toll-reaches-12/article71243803.ece)
