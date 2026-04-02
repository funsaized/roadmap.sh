# PredictionMarket AMM Implementation

## Metadata
- **URL:** https://github.com/Apostlex0/PredictionMarket_AMM
- **Source:** GitHub
- **Type:** code-documentation
- **Author:** Apostlex0
- **Date Published:** Unknown
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** high

## Content

This repository implements a pm-AMM (Prediction Market Automated Market Maker) inspired by Paradigm's November 2024 research paper. The pm-AMM is a theoretically-grounded AMM designed specifically for binary outcome prediction markets, replacing the constant-product formula with a normal distribution-based pricing model.

## Core Innovation: Why Standard AMMs Fail for Prediction Markets

Standard constant-product AMMs (x × y = k) work well for token swaps where both assets have positive value at all times. But prediction market outcome tokens resolve to either $1.00 or $0.00 — a fundamentally different payoff structure.

The problem: Constant-product AMMs create extreme liquidity concentration at $0.50 for binary markets, while real prediction markets spend most of their time at very high or very low prices (near $0.00 or $1.00). Standard AMMs are capital-inefficient for this payoff structure.

## The pm-AMM Formula

Instead of constant product, the pm-AMM uses:

**(y - x) × Φ((y - x)/L) + L × φ((y - x)/L) - y = 0**

Where:
- x = amount of one outcome token in the pool
- y = amount of the other outcome token (collateral)
- L = liquidity parameter (controls spread and LVR rate)
- Φ = CDF of standard normal distribution
- φ = PDF of standard normal distribution

The invariant can be derived from assuming the market's implied probability follows a normal distribution around the current price.

### Price Function

The price (implied probability) for the YES outcome is:

**p = Φ((y - x)/L)**

This means price is the CDF of a normal distribution centered at the pool's current position. The liquidity parameter L controls the standard deviation — lower L = sharper distribution = wider effective spread.

### Why This Works for Prediction Markets

1. **Natural probability distribution**: Real prediction market prices spend more time near $0 or $1 than at $0.50. A normal distribution of liquidity naturally concentrates where prices are most of the time.

2. **Constant LVR property**: With the right L decay schedule, the pm-AMM achieves "Uniform LVR" — expected loss-vs-rebalancing is a constant fraction of the pool's value regardless of current price.

3. **No extreme slippage near expiry**: Unlike constant-product AMMs which become extremely one-sided near resolution, the pm-AMM smoothly transitions.

## Dynamic pm-AMM: Time-Decaying Liquidity

The static pm-AMM still has a problem: total expected LVR grows over time. The Dynamic pm-AMM solves this by making liquidity decay as the market approaches resolution:

**L(t) = L₀ × √(T - t)**

Where T is the market expiration time and t is the current time.

This ensures:
- Expected LVR rate is constant over the market's lifetime
- Total expected LVR = V₀ / 2 (LP can expect to lose half their capital to arbitrage)
- Liquidity concentrates where traders need it most near resolution

## Loss-vs-Rebalancing (LVR) Analysis

LVR (Loss-vs-Rebalancing) is the key metric for LP performance in prediction market AMMs:

**LVR = (Price Impact from Informed Trades) - (True Probability Update)**

In a standard AMM, arbitrageurs extract value from LP positions every time prices move. In prediction markets, this happens constantly as events unfold. The pm-AMM was designed to make this expected loss predictable and bounded.

The Dynamic pm-AMM achieves: **Expected LVR = V₀ / 2** regardless of how the market evolves, making LP returns predictable and enabling proper risk pricing.

## Implementation Code

The repository implements:
- Static pm-AMM with normal distribution pricing
- Dynamic pm-AMM with time-decaying liquidity
- LVR calculation and tracking
- Integration with Gnosis Conditional Tokens

## Comparison with Other Mechanisms

| Mechanism | Price Discovery | Capital Efficiency | LVR Predictability |
|-----------|----------------|-------------------|-------------------|
| LMSR | Good | Low | Bounded but non-constant |
| Constant Product | Moderate | Moderate | Poor (price-dependent) |
| pm-AMM (static) | Good | High | Partial |
| pm-AMM (dynamic) | Excellent | High | Excellent (constant rate) |
| CLOB | Excellent | Excellent | None (LP is Maker) |

## Key Excerpts

1. "The pm-AMM replaces the constant-product invariant with a normal distribution-based pricing model, naturally concentrating liquidity where prediction market prices spend most of their time — near $0 and $1."

2. "The Dynamic pm-AMM with time-decaying liquidity L(t) = L₀ × √(T-t) achieves constant expected LVR rate over the market's lifetime, making LP returns predictable and enabling proper risk pricing."

3. "The core innovation of Uniform LVR is making expected LP loss a constant fraction of pool value regardless of the current market price — transforming liquidity provision from speculation into a calculable business."

## Scrape Notes
- **Content completeness:** partial (code extraction from GitHub was limited; README provided most substantive content)
- **Note:** Implementation quality is high; the README provides excellent theoretical background
