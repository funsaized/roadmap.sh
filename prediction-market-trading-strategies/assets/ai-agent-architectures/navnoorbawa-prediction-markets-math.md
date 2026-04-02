# The Math of Prediction Markets: Binary Options, Kelly Criterion, and CLOB Pricing

## Metadata
- **URL:** https://navnoorbawa.substack.com/p/the-math-of-prediction-markets-binary
- **Source:** navnoorbawa.substack.com
- **Type:** article
- **Author:** Navnoor Bawa
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Summary

Institutional-quality quantitative analysis covering the full prediction market trading stack: binary contract mechanics (ERC-1155 via Gnosis CTF), price discovery, P&L mechanics (pre-resolution and hold-to-expiry), Kelly criterion with worked examples, cross-platform arbitrage (Polymarket/Kalshi/PredictIt), behavioral biases (longshot bias, recency bias, volume distortions), and AMM vs CLOB comparison. Includes 34 academic citations.

## Enrichment

### Topic Tags
- binary-options
- Kelly-criterion
- cross-platform-arbitrage
- behavioral-biases
- CLOB-mechanics
- quantitative-analysis
- position-sizing

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**People:**
- Navnoor Bawa — author (quantitative researcher)

**Organizations:**
- Polymarket — prediction market platform
- Kalshi — CFTC-regulated exchange
- PredictIt — prediction market platform
- Gnosis — CTF developer
- CFTC — regulatory body
- DC Circuit Court — regulatory decision

**Technologies:**
- ERC-1155 tokens
- Gnosis Conditional Tokens Framework
- Polygon PoS
- USDC
- UMA Optimistic Oracle
- CLOB (Central Limit Order Book)
- EIP-712 signed orders

**Concepts:**
- Core invariant: YES + NO = $1.00
- Share minting: atomic, fully collateralized
- Kelly formula: f* = (bp - q) / b
- Fractional Kelly: 0.25x to 0.5x recommended
- Cross-platform arbitrage: 1-3% risk-free returns
- Longshot bias: retail overpays for P < 15%
- Recency bias: negative autocorrelation in daily price changes
- Asymmetric convexity in low-probability positions
- Polymarket 2023 AMM→CLOB migration
- Slippage: Δp ≈ Q / (2 × depth) for CLOB

**Data Points:**
- Arbitrage example: $0.02/contract (2.04% return)
- Kelly example: 37.5% of bankroll at 75% true prob vs 60% market price
- Platform accuracy (2024 election): PredictIt 93%, Kalshi 78%, Polymarket 67%
- UMA bond: $750 USDC, 2-hour dispute window
- October 2, 2024: DC Circuit allowed Kalshi political contracts
- 34 academic citations

### Cross-References
- **extends** → kelly-criterion-polymarket-bot (detailed Kelly implementation vs theoretical overview here)
- **extends** → gensyn-lmsr (covers LMSR theory referenced here)
- **supports** → polymarket-ctf-overview (confirms CTF mechanics)
- **supports** → polymarket-clob-introduction (confirms CLOB architecture)
- **complements** → hummingbot-inventory-risk (behavioral patterns create inventory risks)
- **complements** → medium-lmsr-math (covers LMSR math in greater code detail)
- **complements** → paradigm-pm-amm (discusses AMM limitations that PM-AMM solves)
