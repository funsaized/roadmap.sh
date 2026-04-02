# PM-AMM LP Risk Management

## Metadata
- **URL:** https://www.paradigm.xyz/2024/11/pm-amm
- **Source:** Paradigm
- **Type:** article/research
- **Author:** Ciamac Moallemi, Dan Robinson
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high (LP risk context)

## Summary

PM-AMM transforms LP risk from unpredictable speculation into calculable business. Key risk metrics: uniform LVR (constant loss rate across prices), total expected LVR = V₀/2, time-decaying liquidity reducing exposure near expiry. Addresses CPMM guaranteed total loss at binary resolution.

## Enrichment

### Topic Tags
- LP-risk
- LVR-analysis
- time-decay
- risk-quantification
- PM-AMM

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**Concepts:**
- Total expected LVR = V₀/2 (50% capital loss to arbitrage over lifetime)
- Time-decaying liquidity: L√(T-t) reduces exposure near expiry
- CPMM guaranteed 100% loss at binary resolution
- Uniform AMM: predictable LP risk profile
- Fees must exceed LVR for profitable LP operation

### Cross-References
- **complements** → hummingbot-inventory-risk (operational risk vs theoretical risk framework)
- **extends** → gensyn-lmsr (quantifies previously unbounded LMSR risk)
- **supports** → apostlex0-prediction-market-amm (implementation proves theoretical risk model)
