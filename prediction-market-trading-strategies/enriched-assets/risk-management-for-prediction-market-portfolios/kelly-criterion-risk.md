# Kelly Criterion as Risk Management Framework

## Metadata
- **URL:** https://www.mintlify.com/joicodev/polymarket-bot/risk/kelly-criterion
- **Source:** Mintlify / joicodev
- **Type:** documentation
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high (risk management context)

## Summary

Kelly criterion framed as risk management: fractional Kelly (0.10-0.40 alpha) prevents overbetting, Brier-tiered sizing automatically reduces exposure when model accuracy degrades, drawdown modes (yellow at 12%+, red for halt) enforce loss limits. Never risks total ruin theoretically, but practical constraints require fractional approach.

## Enrichment

### Topic Tags
- Kelly-criterion
- risk-management
- drawdown-protection
- position-sizing
- model-accuracy

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**Concepts:**
- Fractional Kelly: trades growth for stability
- Half Kelly: 75% growth, 25% variance
- Drawdown modes: green/yellow/red
- Yellow mode: 0.5x alpha at 12%+ drawdown
- Brier feedback loop: poor predictions → small positions → limited losses
- Risk of ruin: asymptotic zero approach but minBetUsd creates practical floor

### Cross-References
- **complements** → hummingbot-inventory-risk (different risk layer: bet sizing vs position management)
- **extends** → navnoorbawa-prediction-markets-math (implements Kelly theory as risk framework)
- **supports** → arxiv-kelly-prediction-markets (academic backing for KL-divergence error analysis)
