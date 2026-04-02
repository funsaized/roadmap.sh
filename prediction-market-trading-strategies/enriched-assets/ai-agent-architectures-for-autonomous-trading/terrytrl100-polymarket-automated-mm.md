# Poly-Maker: Automated Market Making Bot for Polymarket

## Metadata
- **URL:** https://github.com/terrytrl100/polymarket-automated-mm
- **Source:** github.com/terrytrl100
- **Type:** code/documentation
- **Author:** terrytrl100 (forked from @defiance_cr)
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Summary

Production-grade automated market making bot for Polymarket's CLOB. Features real-time WebSocket order book monitoring, two-sided market making, reward-optimized pricing using Polymarket's maker formula S=((v-s)/v)², automated market selection by profitability score, position merging, and Google Sheets configuration. Includes sophisticated risk controls and 95% reduction in unnecessary order cancellations.

## Enrichment

### Topic Tags
- market-making-bot
- Polymarket
- CLOB-trading
- maker-rewards
- position-management
- automated-trading
- risk-controls

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**People:**
- terrytrl100 — author
- @defiance_cr — original fork source

**Organizations:**
- Polymarket — trading platform

**Technologies:**
- Polymarket CLOB API
- WebSocket connections
- Google Sheets API
- Python 3.9+
- Node.js (poly_merger)
- EIP-712 signed orders

**Concepts:**
- Maker reward formula: S = ((v - s) / v)²
- Optimal order placement at ~15% of max_spread
- Profitability score = gm_reward_per_100 / (volatility_sum + 1)
- Position merging (YES+NO → collateral)
- Two-sided market making
- 30-second cooldown on cancellations
- Cancellation thresholds: 1.5% price diff, 25% size diff
- 95% reduction in unnecessary cancellations

**Data Points:**
- Merger threshold: $20 configurable
- Cancellation reduction: ~95%
- Order placement: ~15% of max_spread distance

### Cross-References
- **extends** → warproxxx-poly-maker (forked from same codebase, different optimization focus)
- **supports** → hummingbot-inventory-risk (implements inventory management concepts)
- **complements** → polymarket-clob-introduction (uses CLOB API documented there)
- **complements** → polymarket-ctf-overview (uses CTF for position merging)
- **complements** → manifold-market-maker (simpler MM bot for different platform)
