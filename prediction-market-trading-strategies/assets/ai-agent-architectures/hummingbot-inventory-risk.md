# What is Inventory Risk?

## Metadata
- **URL:** https://hummingbot.org/blog/what-is-inventory-risk/
- **Source:** hummingbot.org
- **Type:** article
- **Author:** Hummingbot
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** medium

## Summary

Educational deep-dive on inventory risk — the core risk in market making operations. Explains how trending markets cause asymmetric fill rates leading to accumulation of losing-side assets. Covers five mitigation strategies: inventory skew, filled order delay, hanging orders, ping pong, and one-sided spread adjustment. Connects to prediction market specifics where binary outcomes amplify jump risk near resolution.

## Enrichment

### Topic Tags
- inventory-risk
- market-making
- risk-management
- Hummingbot
- mitigation-strategies
- position-management

### Content Depth
deep-dive

### Temporal Relevance
evergreen

### Entities

**People:**
- Warren Buffett — quoted on risk

**Organizations:**
- Hummingbot — author and trading bot platform

**Technologies:**
- Hummingbot bot framework
- Python scripting engine
- inventory_skew_enabled parameter
- filled_order_delay parameter

**Concepts:**
- Inventory risk: probability of holding wrong-side assets
- Inventory skew: rebalancing via asymmetric order sizes
- Filled order delay: spacing orders after fills (e.g., 300 seconds)
- Hanging orders: keeping unfilled side outstanding
- Ping pong: alternating buy/sell only after fills
- One-sided spread adjustment: tighten against-trend side
- Prediction market jump risk at resolution (binary $0/$1)
- Dynamic PM-AMM as mitigation (reducing liquidity near expiry)

### Cross-References
- **supports** → apostlex0-prediction-market-amm (PM-AMM's time-decay directly addresses inventory risk near expiry)
- **supports** → terrytrl100-polymarket-automated-mm (practical implementation of inventory management)
- **supports** → warproxxx-poly-maker (position merging reduces inventory exposure)
- **complements** → kelly-criterion-polymarket-bot (position sizing also manages risk exposure)
- **extends** → paradigm-pm-amm (PM-AMM provides theoretical framework for managing this risk)
