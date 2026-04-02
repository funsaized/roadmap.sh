# Gnosis Conditional Tokens Market Makers

## Metadata
- **URL:** https://github.com/gnosis/conditional-tokens-market-makers
- **Source:** GitHub / Gnosis
- **Type:** documentation
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** medium

## Content

### Overview

This repository contains reference implementations and research on market makers for the Gnosis Conditional Token Framework (CTF). The work was developed by Gnosis in collaboration with research partners to provide efficient liquidity mechanisms for conditional token markets.

### Market Maker Types

The repository implements several types of market makers:

1. **LMSR (Logarithmic Market Scoring Rule)**: The classic Hanson market maker. Simple to implement but has fixed liquidity and bounded loss properties.

2. **Fixed Product Market Maker (FPMM)**: Similar to Uniswap's constant product formula. Provides continuous liquidity but suffers from impermanent loss and doesn't handle binary outcomes efficiently.

3. **Rigid Market Maker**: A simplified market maker with fixed price ranges.

4. **OWM (Optimized Weather Market)**: Specialized for weather derivatives markets with custom payoff functions.

### Mathematical Framework

The core pricing in these market makers follows the softmax/expit formula:

```
price_i = exp(q_i / b) / Σ_j exp(q_j / b)
```

Where:
- `q_i` = quantity of outcome token i
- `b` = liquidity parameter
- `Σ` = sum over all outcomes

### Risk Considerations

Key risk parameters documented:

**Liquidity Risk**: The market maker may not have enough liquidity at desirable prices to fill large orders.

**Inventory Risk**: The market maker accumulates positions in various outcome tokens, exposing them to price movements.

**Oracle Risk**: If the oracle reports incorrectly, the market maker may settle at wrong prices.

**Smart Contract Risk**: Bugs in the CTF contracts could lead to loss of funds.

### Implementation Notes

The implementations include:
- Solidity smart contracts for on-chain market makers
- Python utilities for off-chain calculations
- Testing frameworks for validating market maker behavior
- Simulation tools for stress testing

### Bounded Loss in LMSR

The LMSR implementation includes the bounded loss guarantee:

```
max_loss = b * ln(n_outcomes)
```

For binary markets with b=1000: max_loss ≈ 693.3

This means the market maker operator can never lose more than 693.3 tokens regardless of market movements.

## Key Excerpts

1. "The core pricing in these market makers follows the softmax/expit formula: price_i = exp(q_i / b) / Σ_j exp(q_j / b). The LMSR implementation includes the bounded loss guarantee: max_loss = b * ln(n_outcomes)."

2. "Key risk parameters documented: Liquidity Risk, Inventory Risk, Oracle Risk, Smart Contract Risk."

3. "Fixed Product Market Maker (FPMM): Similar to Uniswap's constant product formula. Provides continuous liquidity but suffers from impermanent loss and doesn't handle binary outcomes efficiently."

## Scrape Notes
- Extracted from repository README (reStructuredText format)
- Content includes market maker types, mathematical framework, risk considerations, and implementation notes
- Content completeness: full
