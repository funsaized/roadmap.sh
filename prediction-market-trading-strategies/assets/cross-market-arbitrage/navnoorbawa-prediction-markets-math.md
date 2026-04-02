# Cross-Platform Arbitrage in Prediction Markets

## Metadata
- **URL:** https://navnoorbawa.substack.com/p/the-math-of-prediction-markets-binary
- **Source:** navnoorbawa.substack.com
- **Type:** article
- **Author:** Navnoor Bawa
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high (arbitrage focus)

## Summary

Covers cross-platform arbitrage between Polymarket, Kalshi, and PredictIt. Documents persistent price divergences, arbitrage mechanics exploiting the YES+NO=$1 invariant across platforms, and reasons why inefficiencies persist (low institutional participation, platform fragmentation, thin liquidity). Includes worked arbitrage example yielding 2.04% risk-free return.

## Enrichment

### Topic Tags
- cross-platform-arbitrage
- price-divergence
- risk-free-returns
- platform-comparison
- market-efficiency

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**Organizations:** Polymarket, Kalshi, PredictIt

**Concepts:**
- Arbitrage: buy YES on one platform + NO on another when sum < $1
- 2024 election: arbitrage peaked in final 2 weeks (counter to efficiency hypothesis)
- Platform accuracy divergence: PredictIt 93%, Kalshi 78%, Polymarket 67%
- Persistence factors: retail-dominated, fragmented, thin liquidity, high latency

**Data Points:**
- Example: Polymarket YES $0.42 + Kalshi NO $0.56 = $0.98 → $0.02 profit (2.04%)
- Cross-platform returns: 1-3% risk-free

### Cross-References
- **complements** → polymarket-clob-introduction (API needed for automated arbitrage)
- **supports** → hummingbot-inventory-risk (arbitrage positions carry settlement risk)
