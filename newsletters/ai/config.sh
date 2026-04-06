#!/bin/bash
#
# AI Newsletter — Topic Configuration
#
# Sourced by _lib.sh when --topic ai (or no --topic, since ai is the default).
# All topic-specific values live here. Pipeline scripts read these instead of
# hardcoding clusters, tools, bylines, etc.
#

# --- Identity ---
TOPIC_ID="ai"
TOPIC_LABEL="AI & Tech"
TOPIC_TITLE_PREFIX="[Tech]"
TOPIC_BYLINE="Por: Guilherme Saboia e Vinicius Gushiken"

# --- Research ---
TOPIC_ALLOWED_TOOLS="Write,Read,WebFetch,WebSearch,mcp__exa__web_search_exa,mcp__exa__crawling_exa,Bash(bird *)"

# Pre-research sources (run before clusters, output passed to all of them)
TOPIC_PRE_RESEARCH_CMD="python3 \"\$DIR/tools/techmeme.py\" 2>/dev/null || echo '[Techmeme fetch failed]'"

# Cluster names — space-separated, order matters for merge
TOPIC_CLUSTERS="ai hw world"

# --- Cluster definitions ---
read -r -d '' TOPIC_CLUSTER_AI << 'EOF' || true
- AI capabilities: new model releases, updates, benchmark results (frontier and open-source)
- Reasoning, coding, and multimodal capability jumps
- Agentic systems: tool use, computer use, autonomous coding, long-horizon tasks
- AI safety: alignment, evaluations, red-teaming, governance proposals
- AI in science: protein folding, drug discovery, materials, math proofs
- AI economics: pricing, API changes, adoption metrics, enterprise deals
- Recursive self-improvement: AI training AI, automated ML research
Key X accounts: @sama, @AnthropicAI, @OpenAI, @GoogleDeepMind, @scaling01, @metr_evals, @epochairesearch, @arcprize
EOF

read -r -d '' TOPIC_CLUSTER_HW << 'EOF' || true
- Chips & semiconductors: Nvidia, AMD, Intel, Broadcom, custom silicon (Google TPU, Amazon Trainium, Microsoft Maia)
- Foundries: TSMC, Samsung, Intel Foundry — capacity, process nodes, orders
- Data centers: new builds, power deals, cooling tech, geographic expansion
- Energy for compute: nuclear, solar, grid upgrades, power purchase agreements
- Export controls: US-China chip restrictions, ASML/EUV, sanctions
- Robotics: humanoids (Tesla Optimus, Figure, Unitree), industrial automation, warehouse robots
Key X accounts: @elonmusk, @jimfanAI, @chilobrandt
EOF

read -r -d '' TOPIC_CLUSTER_WORLD << 'EOF' || true
- Geopolitics: conflicts, alliances, sanctions, trade wars, diplomatic shifts
- Military: operations, weapons systems, defense deals, intelligence
- Economics: jobs reports, GDP, inflation, central bank moves, oil/energy prices
- Labor & AI displacement: layoffs citing AI, hiring freezes, workforce shifts
- Markets: major moves in equities, commodities, crypto tied to news events
- Funding: major rounds, IPOs, acquisitions, SPAC deals
- Biotech: drug approvals, clinical trial results, CRISPR/gene therapy, longevity research
- Health policy: FDA decisions, pandemic preparedness, health system changes
- Space: launches, missions, orbital debris, satellite constellations, exploration milestones
- Climate/energy: transition milestones, extreme events, policy moves
Key X accounts: @xaborsa
Key sources: Reuters, AP, BBC, Al Jazeera, FT, STAT News, BioPharma Dive, Nature Medicine
EOF
