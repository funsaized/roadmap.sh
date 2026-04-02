# Kelly Criterion — Polymarket Bot Implementation

## Metadata
- **URL:** https://www.mintlify.com/joicodev/polymarket-bot/risk/kelly-criterion
- **Source:** Mintlify / joicodev
- **Type:** documentation
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Summary

Production implementation of fractional Kelly criterion for a Polymarket trading bot. Covers full Kelly formula, simplified prediction market form f*=(p-q)/(1-q), Brier-tiered alpha system mapping model accuracy to position sizing, drawdown-adjusted modes (yellow/red), side determination logic, and worked examples for YES/NO bets. Includes code snippets showing actual PositionSizer implementation.

## Enrichment

### Topic Tags
- Kelly-criterion
- position-sizing
- Brier-score
- fractional-Kelly
- risk-management
- trading-bot
- drawdown-management

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**People:**
- J.L. Kelly Jr. — original Kelly criterion paper (1956)
- E.O. Thorp — optimal gambling systems (1969)

**Organizations:**
- joicodev — bot developer

**Technologies:**
- Polymarket Bot (PositionSizer)
- Brier score calculator
- JavaScript implementation

**Concepts:**
- Full Kelly: f* = (p×b - q) / b
- Simplified: f* = (p - q) / (1 - q)
- Fractional Kelly: α × f* where 0 < α ≤ 1
- Half Kelly: 75% growth rate, 25% variance
- Brier-tiered alpha: <0.18→0.40, 0.18-0.22→0.25, 0.22-0.26→0.20, >0.26→0.10
- Minimum 100 predictions before trading
- Drawdown modes: green (normal), yellow (0.5x alpha), red (halt)
- 3% fee on wins (Polymarket)
- Side determination: p≥0.5→YES, p<0.5→NO
- Risk of ruin: asymptotic approach to zero but practical constraints

**Data Points:**
- α=0.5: 75% of growth, 25% of variance
- Max alpha: 0.40 (never exceeds 40% full Kelly)
- Polymarket fee: 3% on wins
- Example: $677 bet at 6.77% of $10K bankroll
- Yellow mode: 0.5x alpha multiplier at 12.38% drawdown

### Cross-References
- **extends** → navnoorbawa-prediction-markets-math (implements Kelly theory from that article)
- **extends** → prediction-market-amm-with-kelly (same formula, different implementation focus)
- **complements** → arxiv-kelly-prediction-markets (academic theory vs practical implementation)
- **supports** → hummingbot-inventory-risk (position sizing is a form of risk management)
- **complements** → terrytrl100-polymarket-automated-mm (different strategy: MM spread vs Kelly edge)
