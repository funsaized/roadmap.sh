# Prediction Market AMM with Kelly Criterion and Position Sizing

## Metadata
- **URL:** https://github.com/Apostlex0/PredictionMarket_AMM
- **Source:** GitHub / Apostlex0
- **Type:** code/documentation
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Summary

Comprehensive repository documentation combining PM-AMM implementation with Kelly criterion position sizing. Includes Python code for Kelly fraction calculation, Brier-adjusted alpha tables, LVR analysis, and practical bankroll management guidelines. Bridges AMM mechanics with optimal trading strategy.

## Enrichment

### Topic Tags
- Kelly-criterion
- PM-AMM
- position-sizing
- Brier-score
- LVR-analysis
- Python-implementation

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**Organizations:**
- Apostlex0 — author

**Technologies:**
- Python (Kelly + Brier implementations)
- PM-AMM invariant
- Brier score calculator

**Concepts:**
- Edge formula: p_true - Market_Price
- Kelly: f* = (p×b - q) / b
- Fractional Kelly: 0.25x = 75% growth/25% variance, 0.5x = 87.5% growth/50% variance
- Brier-adjusted Kelly tiers (same as polymarket bot)
- LVR = (p_true - p_AMM) × spread × Volume
- Bankroll limits: conservative 2-5%, moderate 5-10%, aggressive 10-20%

### Cross-References
- **complements** → kelly-criterion-polymarket-bot (JavaScript vs Python implementation)
- **extends** → apostlex0-prediction-market-amm (same repo, Kelly-focused content)
- **supports** → navnoorbawa-prediction-markets-math (implements same formulas)
