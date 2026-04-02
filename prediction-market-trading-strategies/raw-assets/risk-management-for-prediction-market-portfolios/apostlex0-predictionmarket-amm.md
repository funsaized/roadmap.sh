# PredictionMarket_AMM

## Metadata
- **URL:** https://github.com/Apostlex0/PredictionMarket_AMM
- **Source:** GitHub
- **Type:** code/documentation
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

### Project Overview

A comprehensive Python implementation of prediction market AMM mechanics including LMSR, constant product market makers, and analysis tools. This repository provides working code for understanding how prediction market AMMs work mathematically and how to implement them.

### AMM Types Implemented

**1. LMSR (Logarithmic Market Scoring Rule)**
- Implements the classic Hanson market maker
- Cost function: `C(q) = b * log(sum(exp(q_i/b)))`
- Price function: softmax over token quantities
- Bounded loss property for market maker risk management

**2. Constant Product AMM**
- Traditional `x * y = k` formula
- Used in Uniswap-style DEXs
- For binary outcomes: prices approach 0 or 1 as liquidity concentrates on one side
- Issues with binary outcomes: requires large liquidity to maintain reasonable prices near 50%

**3. Constant Sum AMM**
- Simple `x + y = k` formula
- Works well near 50/50 but breaks down at extremes
- Used in some prediction markets for symmetric contracts

**4. Hybrid AMMs**
- Combines features of multiple AMM types
- Tries to get benefits of constant product (unbounded liquidity) with LMSR-like pricing

### Mathematical Analysis

The repository includes detailed mathematical analysis of:

**Price Impact Formula**: For small orders in an LMSR market:
```
Δprice ≈ Δq / (b * p * (1-p))
```
Where p is the current price and b is the liquidity parameter.

**Liquidity Efficiency**: LMSR is more capital-efficient than constant product for binary outcomes:
- LMSR: Price can move from 1% to 99% with finite capital
- Constant Product: Price moves exponentially, requiring huge liquidity at extremes

**Spread Dynamics**: The effective spread in LMSR is approximately:
```
spread ≈ 2 / b (at 50% price)
spread → 0 as price → 0 or 1
```

### Risk Management Framework

The repository implements several risk management concepts:

**1. Position Sizing**
- Calculate maximum position based on bankroll
- Use Kelly criterion for optimal sizing
- Implement position limits to prevent ruin

**2. Liquidity Management**
- Monitor available liquidity at each price level
- Calculate slippage for large orders
- Implement order sizing based on liquidity

**3. Inventory Risk**
- Track current inventory (net position)
- Rebalance when inventory skews too far
- Use hedging strategies to reduce inventory risk

**4. Greeks for Binary Options**
- Delta: change in price for change in underlying
- Gamma: rate of delta change
- For binary options, these map to different sensitivities than vanilla options

### Simulation Framework

The repository includes Monte Carlo simulation tools for:
- Testing AMM behavior under various market conditions
- Calculating expected losses and gains
- Stress testing risk management strategies
- Optimizing AMM parameters (liquidity, fees)

### Key Insights for Risk Management

1. **LMSR is inherently safer for AMM operators**: The bounded loss property means you can never lose more than `b * ln(n)`.

2. **Constant product AMMs can lose unlimited amounts**: In volatile markets, large price swings can cause massive losses.

3. **Position sizing is critical**: Even with bounded loss AMMs, over-sizing positions can lead to ruin.

4. **Correlation between markets matters**: A portfolio of related prediction markets has correlated risk.

5. **Time decay affects pricing**: As markets approach resolution, the risk profile changes.

## Key Excerpts

1. "LMSR is more capital-efficient than constant product for binary outcomes: Price can move from 1% to 99% with finite capital, while Constant Product requires huge liquidity at extremes."

2. "The effective spread in LMSR is approximately: spread ≈ 2/b (at 50% price), spread → 0 as price → 0 or 1."

3. "Position sizing is critical: Even with bounded loss AMMs, over-sizing positions can lead to ruin. The repository implements several risk management concepts: Position Sizing, Liquidity Management, Inventory Risk, and Greeks for Binary Options."

## Scrape Notes
- Very comprehensive GitHub repository with code, mathematical analysis, and risk management frameworks
- Content includes AMM types, mathematical analysis, risk management, simulation framework
- Content completeness: full (README is very detailed)
