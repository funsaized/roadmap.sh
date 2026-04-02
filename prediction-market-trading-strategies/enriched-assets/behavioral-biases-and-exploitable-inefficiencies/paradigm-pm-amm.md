# pm-AMM: A Uniform AMM for Prediction Markets

## Metadata
- **URL:** https://www.paradigm.xyz/2024/11/pm-amm
- **Source:** Paradigm
- **Type:** article/research
- **Author:** Ciamac Moallemi, Dan Robinson
- **Date Published:** November 2024
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Summary

Paradigm's foundational research on PM-AMM — a purpose-built AMM for prediction markets using Gaussian score dynamics. Introduces the Uniform AMM principle where expected LVR is constant regardless of price. Defines static and dynamic invariants using normal CDF/PDF, achieves predictable LP losses (total expected LVR = V₀/2), and addresses the fundamental flaw of CPMM guaranteed loss at binary expiration.

## Enrichment

### Topic Tags
- PM-AMM
- automated-market-maker
- LVR-analysis
- Gaussian-dynamics
- liquidity-provision
- mathematical-foundations

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**People:**
- Ciamac Moallemi — co-author (Columbia University/Paradigm)
- Dan Robinson — co-author (Paradigm)

**Organizations:**
- Paradigm — research firm

**Technologies:**
- PM-AMM (static and dynamic variants)
- Normal CDF/PDF pricing
- Brownian motion score dynamics

**Concepts:**
- Uniform AMM: LVR is constant fraction of pool value
- Static invariant: (y-x)Φ((y-x)/L) + Lφ((y-x)/L) - y = 0
- Dynamic invariant: L replaced by L√(T-t)
- Total expected LVR = V₀/2
- Liquidity concentration at p=0.5
- CPMM guaranteed loss at expiration
- LVR vs impermanent loss distinction

### Cross-References
- **extends** → gensyn-lmsr (PM-AMM solves LMSR limitations)
- **supports** → apostlex0-prediction-market-amm (Morpheus implements this paper)
- **contradicts** → gnosis-conditional-tokens-market-makers (CPMM approach has guaranteed loss)
- **complements** → hummingbot-inventory-risk (PM-AMM addresses time-based inventory risk)
