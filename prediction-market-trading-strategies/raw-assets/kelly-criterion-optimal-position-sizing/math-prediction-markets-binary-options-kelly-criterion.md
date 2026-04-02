# The Math of Prediction Markets: Binary Options, Kelly Criterion, and CLOB Pricing

## Metadata
- **URL:** https://navnoorbawa.substack.com/p/the-math-of-prediction-markets-binary
- **Source:** Substack / Navnoor Bawa
- **Type:** article
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Content

# The Math of Prediction Markets: Binary Options, Kelly Criterion, and CLOB Pricing

## Binary Options Structure

Prediction market contracts are fully-collateralized binary options trading on central limit order books where the core invariant YES + NO = $1.00 creates deterministic P&L mechanics and persistent arbitrage opportunities.

Prediction markets issue binary contracts with terminal payoffs of $1.00 or $0.00. On Polymarket, each market creates two ERC-1155 tokens (YES and NO) via Gnosis Conditional Tokens Framework.

The foundational invariant is contract-enforced: P_YES + P_NO = $1.00. Violation creates immediate arbitrage.

## P&L Mechanics

Pre-resolution P&L follows standard mechanics:

```
P&L = (Exit_Price - Entry_Price) × Position_Size
```

Example: Buy 5,000 YES @ $0.28, sell @ $0.61 → $1,650 profit [($0.61 — $0.28) × 5,000].

Holding to resolution creates asymmetric convexity tied to entry price. Low-probability tails ($0.05-$0.20) offer lottery-like payoff structures. Buy 10,000 YES @ $0.12, pay $1,200. If event occurs, receive $10,000 → $8,800 net profit (+733%). If event fails, lose entire $1,200 stake (-100%).

## Edge Extraction Framework

Edge extraction requires two components: probability estimation superiority and Kelly-optimal position sizing.

**Expected value formula:**

```
EV = p(true) × $1.00 - Market_Price
```

**Kelly criterion determines optimal bankroll fraction:**

```
f* = (bp - q) / b
```

Where:
- p = true probability (your forecast)
- q = 1 - p
- b = (1 - Market_Price) / Market_Price [net odds]

### Worked Kelly Example

Market prices "Fed Rate Cut in March" at $0.60 (60% implied probability). Your econometric model forecasts 75% true probability.

```
b = (1 - 0.60) / 0.60 = 0.667
f* = (0.667 × 0.75 - 0.25) / 0.667 = (0.500 - 0.25) / 0.667 = 0.375
```

Kelly recommends 37.5% of bankroll in YES shares. EV per $1 risked = $0.75 — $0.60 = $0.15 edge (25% ROI if forecast correct).

## Fractional Kelly

Full Kelly maximizes long-run growth rate but creates 33% probability of halving bankroll before doubling. Fractional Kelly (typically 0.25x to 0.5x full Kelly) reduces volatility and protects against probability estimation errors.

Academic research by Wolfers and Zitzewitz (2006) shows prediction market prices typically approximate mean beliefs but can deviate for extreme probabilities near $0.00 or $1.00, where risk preferences distort pricing.

### Why Fractional Kelly?

- **High variance:** Full Kelly can recommend very large bets
- **Model error sensitivity:** Small errors in p estimation lead to overbetting
- **Drawdown magnitude:** Aggressive sizing causes deeper drawdowns

### Growth-Variance Tradeoff

For α = 0.5 (half Kelly):
- Growth rate ≈ 75% of full Kelly
- Variance ≈ 25% of full Kelly

This is a highly favorable tradeoff for most traders.

## Brier Score Connection

The Brier score is a strictly proper scoring rule that measures probabilistic forecast accuracy:

```
Brier Score = mean((predicted_probability - actual_outcome)²)
```

In prediction market trading, the Brier score connects to P&L through the relationship between your probability estimates and realized outcomes. A well-calibrated model with low Brier score will capture the Kelly edge more reliably over time.

For a binary prediction market trader:
- Each trade's P&L is determined by whether your probability estimate was better than the market's
- Cumulative P&L approximates the Kelly growth rate scaled by your edge
- Brier score tracks your calibration quality, which determines how much edge you actually have

## CLOB vs. AMM Pricing

### AMM Mechanics (legacy):

- Constant Product: x × y = k (YES shares × NO shares = constant)
- Logarithmic slippage for large orders
- Liquidity providers earn bid-ask spread
- Vulnerable to impermanent loss

### CLOB Mechanics (current):

- Linear slippage based on orderbook depth: Δp ≈ Q / (2 × depth)
- Discrete price jumps from sparse orders
- Market makers post limit orders at specific prices
- No impermanent loss risk

CLOB architecture dominates for binary outcomes. Polymarket's 2023 migration to CLOB enabled significant liquidity growth and improved price discovery versus AMM predecessors.

## Systematic Mispricing Patterns

**Longshot Bias:** Retail traders systematically overpay for low-probability outcomes ($0.01-$0.15) seeking lottery-like payoffs, while underpricing favorites.

**Recency Bias:** Prices overreact to recent news then mean-revert, creating short-term reversals.

**Volume Distortions:** National presidential markets on Polymarket/Kalshi showed highest trading volume but greater inefficiency than lower-liquidity state-level markets.

## Key Excerpts

1. "Kelly criterion: f* = (bp - q) / b where p=true probability, q=1-p, b=net odds. Kelly recommends 37.5% of bankroll when your 75% estimate beats 60% market price"
2. "Full Kelly creates 33% probability of halving bankroll before doubling; Fractional Kelly (0.25x-0.5x) reduces volatility while preserving most of the growth rate"
3. "Brier score connects probability calibration to trading P&L: low Brier score = well-calibrated estimates = reliable Kelly edge capture"
4. "Binary prediction market contracts have deterministic payoff structure (YES + NO = $1.00), eliminating model risk present in vanilla options"
