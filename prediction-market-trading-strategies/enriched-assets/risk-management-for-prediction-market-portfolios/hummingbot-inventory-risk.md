# Inventory Risk Management for Market Makers

## Metadata
- **URL:** https://hummingbot.org/blog/what-is-inventory-risk/
- **Source:** hummingbot.org
- **Type:** article
- **Author:** Hummingbot
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high (risk management focus)

## Summary

Five mitigation strategies for inventory risk: inventory skew (rebalancing order sizes), filled order delay (spacing fills), hanging orders (keeping unfilled sides), ping pong (alternating sides), and one-sided spread adjustment. Prediction market specific: binary outcomes create extreme jump risk at resolution — no gradual exit possible.

## Enrichment

### Topic Tags
- inventory-risk
- risk-mitigation
- market-making
- position-management
- prediction-market-risk

### Content Depth
deep-dive

### Temporal Relevance
evergreen

### Entities

**Organizations:** Hummingbot
**Technologies:** Hummingbot framework, Python scripting

**Concepts:**
- 5 mitigation strategies: skew, delay, hanging, ping pong, spread adjustment
- Binary jump risk: $0 or $1 at resolution
- Inventory skew parameters: inventory_target_base_pct, inventory_range_multiplier
- Filled order delay: e.g., 300 seconds

### Cross-References
- **complements** → kelly-criterion-polymarket-bot (Kelly manages bet-level risk; inventory manages position-level)
- **complements** → paradigm-pm-amm (PM-AMM manages AMM-level risk via time-decay)
- **supports** → terrytrl100-polymarket-automated-mm (bot implements these concepts)
- **supports** → warproxxx-poly-maker (position merging is risk mitigation)
