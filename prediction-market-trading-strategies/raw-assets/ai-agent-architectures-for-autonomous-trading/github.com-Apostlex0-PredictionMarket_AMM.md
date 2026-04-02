# Morpheus: PM-AMM Implementation on Aptos

## Metadata
- **URL:** https://github.com/Apostlex0/PredictionMarket_AMM
- **Source:** github.com/Apostlex0/PredictionMarket_AMM
- **Type:** code/documentation
- **Author:** Apostlex0
- **Date Published:** 2024-2025
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Overview

Morpheus is a high-fidelity, open-source implementation of Paradigm's Prediction Market Automated Market Maker (PM-AMM), built on the Aptos blockchain using the Move language. It addresses the shortcomings of traditional AMMs for prediction markets by providing a capital-efficient and mathematically sound framework for trading binary outcome tokens.

## The Problem with Standard AMMs

Standard Automated Market Makers (AMMs) like Uniswap use the constant product formula (x × y = k). While elegant for general token swaps, this approach is fundamentally mismatched for prediction markets:

- **Guaranteed Loss at Expiration**: At resolution, one outcome becomes worthless. Arbitrageurs drain valuable tokens from the pool, leaving LPs with zero-value assets — a permanent 100% capital loss.
- **Inefficient Liquidity Profile**: Constant product AMMs provide liquidity across an infinite price range (0 to ∞), but prediction market tokens are bounded between $0 and $1. This mismatch wastes capital and creates poor pricing at the extremes.

## The PM-AMM Solution

The PM-AMM replaces heuristic curve-fitting with explicit, model-based risk management. It uses Gaussian score dynamics — a mathematical model that treats the prediction market's underlying "score" (e.g., vote margin, price difference) as following a Brownian motion.

### The Static PM-AMM Invariant

The trading curve is defined by:

(y - x)Φ((y - x)/L) + L·φ((y - x)/L) - y = 0

Where:
- x = AMM's reserve of YES tokens
- y = AMM's reserve of NO tokens
- L = liquidity parameter (scales pool depth)
- Φ = CDF of standard normal distribution
- φ = PDF of standard normal distribution

### Price Formula

The marginal price of the YES token is:
P = Φ((y - x)/L)

This is the CDF of the normal distribution, always producing a valid probability between 0 and 1. As the AMM's YES reserves increase relative to NO, the price rises naturally.

### Key Innovation: Uniform LVR

Loss-vs-Rebalancing (LVR) is the key risk metric. Unlike impermanent loss in standard AMMs, LVR measures the pure cost of market-making — the value extracted by arbitrageurs trading against stale prices.

The PM-AMM achieves **uniform LVR**: the expected LVR is a constant fraction of pool value regardless of the current price. This makes LP risk stable and predictable. LPs can accurately model their costs and determine required trading fees for profitability.

### Liquidity Fingerprints

The static PM-AMM concentrates liquidity around 50% probability and provides less at extremes (near 0% or 100%). This is rational because:
- Legacy AMMs suffer disproportionately high LVR at price extremes
- Most trading activity happens near 50% (high uncertainty)
- Concentrating liquidity here maximizes capital efficiency

## The Dynamic PM-AMM

The Dynamic extension addresses the time dimension. As a market approaches expiration, uncertainty resolves and prices accelerate toward 0 or 1, magnifying LVR for LPs. The dynamic invariant replaces constant L with time-decaying L·√(T-t):

(y - x)Φ((y - x)/(L√(T-t))) + L√(T-t)·φ((y - x)/(L√(T-t))) - y = 0

As time t approaches expiration T, the liquidity term shrinks, reducing AMM exposure during the highest-risk phase.

### Constant Expected LVR

The design achieves a constant expected rate of loss for LPs over the market's lifetime. The total expected LVR over a market's lifetime equals V₀/2 — meaning an LP can expect to lose exactly half their initial capital to arbitrage. This transforms market-making from speculation into a calculable business.

## Architecture

The protocol uses modular Move contract architecture:

| Module | Responsibility | Key File |
|--------|---------------|---------|
| pm_amm.move | Main entry point, global protocol state | sources/pm_amm.move |
| prediction_market.move | Single market lifecycle, FA tokens | sources/market/prediction_market.move |
| pool_state.move | AMM pool state, fees, dynamic decay | sources/core/pool_state.move |
| invariant.move | Core pricing formulas | sources/core/invariant.move |
| liquidity_math.move | Liquidity calculations | sources/amm_math/liquidity_math.move |
| swap_math.move | Swap quote calculations | sources/amm_math/swap_math.move |
| dynamic_tracking.move | LP withdrawals, loss tracking | sources/core/dynamic_tracking.move |
| fixed_point.move | 64.64 fixed-point arithmetic | sources/math/fixed_point.move |
| normal_dist.move | Normal CDF, PDF, inverse CDF | sources/math/normal_dist.move |

## User Workflow

1. **Discover/Create**: Browse existing markets or create new ones
2. **Market Page**: Dedicated interface for all market interactions
3. **Core Actions**: Swap, Mint Pair, Add/Remove Liquidity, View Analytics

## Swap Infrastructure

- Entry functions: `buy_yes_tokens`, `buy_no_tokens`
- Route through `prediction_market.move` for FA operations
- Core calculation in `pool_state.move` using `swap_math.move`
- Final pricing via `invariant.move`
- Price = Φ((y - x)/L), always a valid probability [0,1]

## Mint Pair

- User deposits collateral (e.g., APT)
- Protocol mints equal YES + NO tokens
- 1-to-1 collateralization ensures full backing and solvency

## Add Liquidity

Key innovation: LP specifies desired_value_increase (single metric), not token ratios. The protocol:
1. Gets current price P from pool_state
2. Calculates ΔL from desired ΔV(P) using: ΔL = ΔV(P) / φ(Φ⁻¹(P))
3. Computes optimal YES/NO deposits to add liquidity without changing price
4. Mints LP tokens representing LP's share

## Remove Liquidity

- LP burns LP tokens
- Receives proportional share of YES + NO reserves
- Plus all accumulated trading fees (auto-distributed on withdrawal)
- `liquidity_math::remove_liquidity_pm_amm` handles proportional calculation

## Market Resolution

- Creator calls `resolve_prediction_market(outcome_yes: bool)`
- Access control: `assert!(raddr == m.creator, E_NOT_AUTHORIZED)`
- Sets resolved flag, disables trading
- Transitions market to settlement-only state

## Settlement

- Users call `settle_tokens_with_collateral`
- Burns all submitted tokens (winners + losers)
- Pays out only winning tokens at $1 each
- Example: Market resolves YES. User holds 100 YES + 50 NO. Burning all 150 tokens returns 100 collateral.

## PM-AMM vs Alternatives

| Feature | CPMM | LMSR | Static PM-AMM | Dynamic PM-AMM |
|---------|------|------|--------------|----------------|
| Invariant | x·y=k | Softmax | Normal CDF | Time-decaying Normal CDF |
| Asset Suitability | General tokens | Pred markets (subsidized) | Outcome tokens | Outcome tokens |
| Liquidity Profile | Uniform | Concentrated by subsidy | Statically at p=0.5 | Dynamically decaying |
| LVR Behavior | High at extremes, unpredictable | High at extremes | Uniform across price | Uniform across price & time |
| LP Loss Profile | Guaranteed at expiry | Potential, subsidized | Predictable rate | Predictable total |

## Key Excerpts

1. "The pm-AMM's core design philosophy is the Uniform AMM. An AMM is 'uniform' if its expected LVR is a constant fraction of the pool's value, regardless of the asset's current price. This makes LP risk stable and predictable, allowing LPs to accurately model their costs and determine the trading fees required for profitability."

2. "Total Expected LVR = V₀/2. This powerful result shows that an LP can expect to lose exactly half of their initial capital to arbitrage over the market's lifetime. This transforms LVR from an unpredictable risk into a quantifiable cost."

3. "The protocol allows providers to contribute capital by specifying a single value they wish to add to the pool. The smart contracts then automatically calculate the optimal amounts of YES and NO tokens required, maximizing efficiency and removing guesswork."

## Scrape Notes
- Content completeness: full
- Excellent README with deep mathematical analysis
- Contains PM-AMM theoretical foundation + Aptos Move implementation details
- Primary research: https://www.paradigm.xyz/2024/11/pm-amm
