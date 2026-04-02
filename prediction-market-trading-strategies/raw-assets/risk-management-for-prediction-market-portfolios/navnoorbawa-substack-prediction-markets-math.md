# The Math of Prediction Markets: Binary Options, Kelly Criterion, and CLOB Pricing Mechanics

## Metadata
- **URL:** https://navnoorbawa.substack.com/p/the-math-of-prediction-markets-binary
- **Source:** Substack / Navnoor Bawa
- **Type:** article
- **Author:** Navnoor Bawa
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

### Core Invariant: YES + NO = $1.00

Prediction market contracts are fully-collateralized binary options trading on central limit order books where the core invariant YES + NO = $1.00 creates deterministic P&L mechanics and persistent arbitrage opportunities.

On Polymarket, each market creates two ERC-1155 tokens (YES and NO) via Gnosis Conditional Tokens Framework. The foundational invariant is contract-enforced: P_YES + P_NO = $1.00. Violation creates immediate arbitrage.

**If YES trades at $0.55 and NO at $0.40 (total = $0.95)**: Buying both locks $0.05 risk-free profit at settlement.

**If the sum exceeds $1.00**: Selling both captures the excess.

Shares are atomically minted when opposing orders match. Zero fractional reserves, zero counterparty credit risk, 100% collateralization.

### Price Discovery and Settlement

Price discovery occurs through order book mechanics. Polymarket displays the midpoint of best bid/ask spread (or last traded price if spread exceeds $0.10).

Market Price ≈ Implied Probability under risk-neutral pricing (subject to risk preferences, liquidity, and platform frictions).

Resolution mechanisms:
- **Polymarket**: UMA Optimistic Oracle with $750 USDC bond, 2-hour dispute window
- **Kalshi**: Event contracts self-certify based on authoritative data sources

### P&L Mechanics

Pre-resolution trading P&L follows standard equity mechanics:
```
P&L = (Exit_Price - Entry_Price) × Position_Size
```

Example: Buy 5,000 YES @ $0.28, sell @ $0.61 → $1,650 profit [($0.61 — $0.28) × 5,000].

Holding to resolution creates asymmetric convexity tied to entry price. Low-probability tails ($0.05-$0.20) offer lottery-like payoff structures: Buy 10,000 YES @ $0.12, pay $1,200. If event occurs, receive $10,000 → $8,800 net profit (+733%). If event fails, lose entire $1,200 stake (-100%).

### Zero-Sum Structure

The zero-sum structure means every dollar won equals a dollar lost by counterparty. This is pure information transfer.

**Fee Structure**:
- Polymarket: No trading fees on primary platform
- Kalshi: Variable fees = ceil(0.07 × contracts × price × (1-price)), ranging ~0.6% for tail events to 1.75% at mid-market ($0.50) prices

### Kelly Criterion Implementation

Edge extraction requires probability estimation superiority + Kelly-optimal position sizing.

Expected value formula:
```
EV = p(true) × $1.00 - Market_Price
```

Kelly criterion determines optimal bankroll fraction:
```
f* = (bp - q) / b
```
Where:
- p = true probability (your forecast)
- q = 1 - p
- b = (1 - Market_Price) / Market_Price [net odds]

**Worked Example**: Market prices "Fed Rate Cut in March" at $0.60 (60% implied probability). Your econometric model forecasts 75% true probability.

```
b = (1 - 0.60) / 0.60 = 0.667
f* = (0.667 × 0.75 - 0.25) / 0.667 = (0.500 - 0.25) / 0.667 = 0.375
```

Kelly recommends 37.5% of bankroll in YES shares. EV per $1 risked = $0.75 — $0.60 = $0.15 edge (25% ROI if forecast correct).

Fractional Kelly (typically 0.25x to 0.5x full Kelly) reduces volatility and protects against probability estimation errors.

### Cross-Platform Arbitrage

Cross-platform arbitrage exploits price disparities between Polymarket, Kalshi, PredictIt.

Research findings (Clinton & Huang, 2025):
- Accuracy rates: PredictIt 93%, Kalshi 78%, Polymarket 67%
- Arbitrage opportunities peaked in final two weeks before Election Day

**Example arbitrage**:
- Polymarket YES: $0.42
- Kalshi NO: $0.56
- Total cost: $0.98
- Guaranteed payout: $1.00
- Net profit: $0.02 per contract (2.04% return)

### Systematic Mispricing Patterns

**Longshot Bias**: Retail traders systematically overpay for low-probability outcomes ($0.01-$0.15) seeking lottery-like payoffs, while underpricing favorites.

**Recency Bias**: Prices overreact to recent news then mean-revert.

**Volume Distortions**: National presidential markets showed highest volume but greater inefficiency than lower-liquidity state-level markets.

### CLOB vs AMM Architecture

Polymarket originally used AMM with Constant Product formula but migrated to CLOB in 2023.

**AMM Mechanics (legacy)**:
- Constant Product: x × y = k (YES shares × NO shares = constant)
- Logarithmic slippage for large orders
- Vulnerable to impermanent loss

**CLOB Mechanics (current)**:
- Linear slippage based on orderbook depth: Δp ≈ Q / (2 × depth)
- Discrete price jumps from sparse orders
- No impermanent loss risk

CLOB architecture dominates for binary outcomes due to superior price discovery and capital efficiency.

### Risk Management Framework

1. **Probability Forecasting Superiority**: Build proprietary models aggregating polling data, fundamental analysis. Even 3–5% edge over market consensus compounds significantly via Kelly criterion.

2. **Kelly-Optimal Position Sizing**: Full Kelly maximizes long-run growth but creates 33% probability of halving bankroll before doubling. Fractional Kelly (0.25x-0.5x) recommended.

3. **Exploit Behavioral Patterns**: Retail-dominated markets systematically misprice tail events. Target $0.05-$0.20 contracts.

4. **Platform Arbitrage**: Cross-platform price monitoring captures 1–3% risk-free returns on liquid markets.

### Key Equations Reference

```
Core Invariant: YES_price + NO_price = $1.00
P&L: (Exit_Price - Entry_Price) × Position_Size
EV: p(true) × $1.00 - Market_Price
Kelly: f* = (bp - q) / b
Binary Odds: b = (1 - price) / price
```

## Key Excerpts

1. "The core invariant YES + NO = $1.00 creates deterministic P&L mechanics and persistent arbitrage opportunities. Violation creates immediate arbitrage: if YES trades at $0.55 and NO at $0.40 (total = $0.95), buying both locks $0.05 risk-free profit at settlement."

2. "Fractional Kelly (typically 0.25x to 0.5x full Kelly) reduces volatility and protects against probability estimation errors. Full Kelly maximizes long-run growth but creates 33% probability of halving bankroll before doubling."

3. "Longshot Bias: Retail traders systematically overpay for low-probability outcomes ($0.01-$0.15) seeking lottery-like payoffs, while underpricing favorites. Volume Distortions: National presidential markets showed highest volume but greater inefficiency than lower-liquidity state-level markets."

## Scrape Notes
- Full article extracted successfully
- Content is very comprehensive covering binary options math, Kelly criterion, arbitrage, behavioral patterns, CLOB mechanics, and risk management
- Content completeness: full
