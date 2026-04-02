# The Math of Prediction Markets: Binary Options, Kelly Criterion, and CLOB Pricing Mechanics

## Metadata
- **URL:** https://navnoorbawa.substack.com/p/the-math-of-prediction-markets-binary
- **Source:** navnoorbawa.substack.com
- **Type:** article
- **Author:** Navnoor Bawa
- **Date Published:** Unknown
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## The Fundamental Structure

Prediction market contracts are fully-collateralized binary options trading on central limit order books where the core invariant YES + NO = $1.00 creates deterministic P&L mechanics and persistent arbitrage opportunities.

Edge extraction comes primarily from superior probability forecasting combined with Kelly-optimal position sizing. These are vanilla digital options priced by the market, not Black-Scholes.

## Binary Contract Mechanics

Prediction markets issue binary contracts with terminal payoffs of $1.00 or $0.00. On Polymarket, each market creates two ERC-1155 tokens (YES and NO) via Gnosis Conditional Tokens Framework. On Kalshi, the same binary structure applies with fiat settlement.

### The Core Invariant

P_YES + P_NO = $1.00 — this is contract-enforced and violation creates immediate arbitrage:
- If YES = $0.55 and NO = $0.40 (sum = $0.95): Buy both → $0.05 risk-free profit
- If sum > $1.00: Sell both → capture the excess

### Share Minting

Shares are atomically minted when opposing orders match:
- Trader A submits limit buy YES @ $0.65
- Trader B submits limit buy NO @ $0.35
- Exchange collects $1.00 total, mints 1 YES + 1 NO simultaneously
- Zero fractional reserves, zero counterparty credit risk, 100% collateralization

## Price Discovery

Price discovery occurs through order book mechanics. Market Price ≈ Implied Probability under risk-neutral pricing (subject to risk preferences, liquidity, and platform frictions). YES @ $0.72 = 72% market-assigned probability.

### Platform Infrastructure

**Polymarket**: Hybrid-decentralized — off-chain order matching (gasless), EIP-712 signed orders, on-chain settlement via Polygon PoS with USDC collateral.

**Kalshi**: Fully-regulated exchange under CFTC oversight with fiat USD settlement.

### Resolution Mechanisms

- **Polymarket**: UMA Optimistic Oracle with $750 USDC bond, 2-hour dispute window, Schelling-point arbitration
- **Kalshi**: Event contracts self-certify outcomes based on authoritative data sources (AP, NBC, government statistics)

The October 2, 2024 DC Circuit decision allowed Kalshi to list political event contracts, materially changing the regulatory landscape.

## P&L Mechanics

### Pre-Resolution Trading
P&L = (Exit_Price - Entry_Price) × Position_Size

Example: Buy 5,000 YES @ $0.28, sell @ $0.61 → $1,650 profit [($0.61 — $0.28) × 5,000].

### Holding to Resolution
Creates asymmetric convexity tied to entry price. Low-probability tails ($0.05-$0.20) offer lottery-like payoff structures: Buy 10,000 YES @ $0.12, pay $1,200. If event occurs, receive $10,000 → $8,800 net profit (+733%). If event fails, lose entire $1,200 (-100%).

## Kelly Criterion

### Expected Value Formula
EV = p(true) × $1.00 - Market_Price

### Kelly Formula
f* = (bp - q) / b

Where:
- p = true probability (your forecast)
- q = 1 - p
- b = (1 - Market_Price) / Market_Price [net odds]

### Worked Example
Market prices "Fed Rate Cut in March" at $0.60 (60% implied). Your model forecasts 75% true probability.

b = (1 - 0.60) / 0.60 = 0.667
f* = (0.667 × 0.75 - 0.25) / 0.667 = (0.500 - 0.25) / 0.667 = 0.375

Kelly recommends 37.5% of bankroll in YES shares. EV per $1 risked = $0.75 — $0.60 = $0.15 edge (25% ROI).

Fractional Kelly (typically 0.25x to 0.5x full Kelly) reduces volatility and protects against probability estimation errors.

## Cross-Platform Arbitrage

Exploits price disparities between Polymarket, Kalshi, PredictIt. Research on 2024 US Presidential election markets found:

- Persistent price divergences across platforms
- Accuracy: PredictIt 93%, Kalshi 78%, Polymarket 67% (in their sample)
- Arbitrage peaked in final two weeks before Election Day (contrary to efficiency hypothesis)

### Example Arbitrage
- Polymarket YES: $0.42
- Kalshi NO: $0.56
- Total cost: $0.98
- Guaranteed payout: $1.00
- Net profit: $0.02 per contract (2.04% return)

### Why These Persist
- Low institutional participation (retail-dominated flow)
- Platform fragmentation (no unified orderbook)
- Thin liquidity in niche markets
- High latency between price discovery sources

## Behavioral Patterns

### Longshot Bias
Retail traders systematically overpay for low-probability outcomes ($0.01-$0.15) seeking lottery-like payoffs. Professional traders exploit by selling tail events and buying high-probability outcomes.

### Recency Bias
Prices overreact to recent news then mean-revert. Markets show negative autocorrelation in daily price changes.

### Volume Distortions
National presidential markets showed highest volume but greater inefficiency than lower-liquidity state-level markets. Attention-driven mispricing overwhelms information aggregation.

## AMM vs CLOB

### AMM Mechanics (legacy)
- Constant Product: x × y = k
- Logarithmic slippage for large orders
- Vulnerable to impermanent loss

### CLOB Mechanics (current)
- Linear slippage based on orderbook depth: Δp ≈ Q / (2 × depth)
- Discrete price jumps from sparse orders
- No impermanent loss risk

Polymarket's 2023 migration to CLOB enabled significant liquidity growth and improved price discovery.

## Systematic Trading Framework

Prediction markets are pure information bets. Systematic profitability requires:

1. **Probability Forecasting Superiority**: Build proprietary models aggregating polling data, fundamental analysis. Even 3-5% edge over market consensus compounds significantly via Kelly criterion.

2. **Kelly-Optimal Position Sizing**: Full Kelly maximizes long-run growth but creates 33% probability of halving bankroll before doubling. Fractional Kelly (0.25x-0.5x) recommended.

3. **Exploit Behavioral Patterns**: Retail-dominated markets systematically misprice tail events. Target $0.05-$0.20 contracts.

4. **Platform Arbitrage**: Cross-platform price monitoring captures 1-3% risk-free returns.

## Key Excerpts

1. "Prediction market contracts are fully-collateralized binary options trading on central limit order books where the core invariant YES + NO = $1.00 creates deterministic P&L mechanics and persistent arbitrage opportunities. Edge extraction comes primarily from superior probability forecasting combined with Kelly-optimal position sizing."

2. "Kelly recommends 37.5% of bankroll in YES shares. EV per $1 risked = $0.75 — $0.60 = $0.15 edge (25% ROI if forecast correct). Fractional Kelly (typically 0.25x to 0.5x full Kelly) reduces volatility and protects against probability estimation errors."

3. "Research on 2024 US Presidential election markets found: Accuracy rates: PredictIt 93%, Kalshi 78%, Polymarket 67%. Arbitrage opportunities peaked in final two weeks before Election Day (contrary to efficiency hypothesis)."

## Scrape Notes
- Content completeness: full
- High-quality institutional-quality analysis
- Covers binary options math, Kelly criterion, arbitrage mechanics, behavioral patterns
- Author is a quantitative researcher
- Includes extensive reference list (34 citations)
