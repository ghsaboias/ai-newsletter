#!/bin/bash
#
# M&A Newsletter — Topic Configuration
#

# --- Identity ---
TOPIC_ID="ma"
TOPIC_LABEL="M&A"
TOPIC_TITLE_PREFIX="[M&A]"
TOPIC_BYLINE="Por: Guilherme Saboia e Vinicius Gushiken"

# --- Research ---
TOPIC_ALLOWED_TOOLS="Write,Read,WebFetch,WebSearch,mcp__exa__web_search_exa,mcp__exa__crawling_exa"

# No pre-research scan for M&A (no Techmeme equivalent)
TOPIC_PRE_RESEARCH_CMD=""

# Cluster names
TOPIC_CLUSTERS="deals regulatory advisors"

# --- Cluster definitions ---
read -r -d '' TOPIC_CLUSTER_DEALS << 'EOF' || true
- Announced mergers and acquisitions: acquirer, target, deal value, structure (cash/stock/mixed), premium to last close, expected close date
- Pricing and valuation: EV/EBITDA multiple, EV/Revenue multiple, P/E, % stake acquired, implied equity value, target revenue/EBITDA/margins when disclosed
- Completed deals: final terms, regulatory approvals obtained, price adjustments from announcement
- Failed/withdrawn deals: why it fell apart, breakup fees, regulatory blocks
- Hostile bids and unsolicited offers: activist pressure, poison pills, defense tactics
- Cross-border M&A: US-EU, US-China, emerging market deals, foreign investment reviews (CFIUS, EU FDI screening)
- Divestitures and spinoffs: strategic rationale, who's buying the carved-out unit, valuation of carved-out business
- Major sectors: tech, healthcare/pharma, energy, financial services, industrials, media/telecom
Key sources: Reuters, Bloomberg, FT, WSJ, The Deal, Mergermarket, Dealogic
EOF

read -r -d '' TOPIC_CLUSTER_REGULATORY << 'EOF' || true
- Antitrust reviews: FTC, DOJ, European Commission, CMA (UK), CADE (Brazil), SAMR (China)
- Merger challenges and lawsuits: blocked deals, conditions/remedies imposed, consent decrees
- New antitrust policy: guidelines updates, enforcement priorities, leadership changes
- Sector-specific regulation: banking (Fed/OCC approvals), healthcare (FTC pharma focus), tech (digital markets)
- CFIUS and foreign investment: national security reviews, forced divestitures, blocked acquisitions
- Shareholder litigation: appraisal rights, fiduciary duty challenges, deal price disputes
Key sources: FTC.gov, DOJ Antitrust Division, European Commission competition, CMA, Law360, Global Competition Review
EOF

read -r -d '' TOPIC_CLUSTER_ADVISORS << 'EOF' || true
- Investment bank mandates: who's advising whom on major deals
- League tables and market share: quarterly/annual rankings shifts
- Advisory fee disclosures and notable engagement terms
- Law firm roles: counsel to acquirer, target, or special committee
- Activist investors: new positions, campaigns, board fights, settlement agreements
- M&A market trends: deal volume, valuation multiples, sector momentum, dry powder, financing conditions
- Notable hires and departures in M&A advisory (bankers, lawyers, activists)
Key sources: Bloomberg, Dealogic, Refinitiv, PitchBook, Activist Insight, WSJ, FT
EOF
