# The Math of Prediction Markets: Binary Options, Kelly Criterion, and CLOB Pricing Mechanics

## Metadata
- **URL:** https://navnoorbawa.substack.com/p/the-math-of-prediction-markets-binary
- **Source:** Navnoor Bawa (Substack)
- **Type:** article
- **Author:** Navnoor Bawa
- **Date Published:** Unknown
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Content

This is an institutional-quality research piece covering the mathematical foundations of prediction market trading, including binary options pricing, Kelly criterion position sizing, CLOB mechanics, and cross-platform arbitrage.

## Binary Options Structure

Prediction market contracts are fully-collateralized binary options trading on central limit order books where the core invariant **YES + NO = $1.00** creates deterministic P&L mechanics and persistent arbitrage opportunities.

### Contract Mechanics

- Each market creates two ERC-1155 tokens (YES and NO) via Gnosis Conditional Tokens Framework
- Terminal payoffs are $1.00 or $0.00
- Kalshi operates the same binary structure with fiat USD settlement under CFTC regulation
- Resolution mechanisms differ:
  - **Polymarket**: UMA Optimistic Oracle with $750 USDC bond, 2-hour dispute window
  - **Kalshi**: Event contracts self-certify based on authoritative data sources (AP, NBC, government)

### Pre-Resolution P&L

Standard equity mechanics apply before resolution:
- **P&L = (Exit_Price - Entry_Price) × Position_Size**
- Example: Buy 5,000 YES @ $0.28, sell @ $0.61 → $1,650 profit [($0.61 - $0.28) × 5,000]

### Convexity and Asymmetric Payoffs

Holding to resolution creates asymmetric convexity:
- Low-probability tails ($0.05-$0.20) offer lottery-like payoff structures
- Buy 10,000 YES @ $0.12, pay $1,200. If event occurs: receive $10,000 → +$8,800 (+733%)
- If event fails: lose entire $1,200 stake (-100%)

### Fee Structure

- **Polymarket**: Zero fees on primary platform (minimal Polygon gas fees)
- **Kalshi**: Variable fees = ceil(0.07 × contracts × price × (1-price))
  - Ranges from ~0.6% for tail events to 1.75% at mid-market ($0.50) prices

## Cross-Platform Arbitrage

Cross-platform arbitrage exploits price disparities between Polymarket, Kalshi, PredictIt, and Robinhood.

### Research Evidence

From Ng, Peng, Tao, Zhou (2025): "Using unique dataset from Polymarket, Kalshi, PredictIt, and Robinhood during 2024 U.S. election, we find significant price disparities across platforms creating economically meaningful arbitrage opportunities."

Clinton and Huang (2025) found:
- Accuracy rates: PredictIt 93%, Kalshi 78%, Polymarket 67%
- Significant price divergences for identical contracts across platforms
- Arbitrage opportunities peaked in final two weeks before Election Day (contrary to efficiency hypothesis)

### Concrete Example

Given identical contracts:
- Polymarket YES: $0.42
- Kalshi NO: $0.56
- Total cost: $0.98
- Guaranteed payout: $1.00
- **Net profit: $0.02 per contract (2.04% return)**

### Why Arbitrage Persists

- Low institutional participation (retail-dominated flow)
- Platform fragmentation (no unified orderbook)
- Thin liquidity in niche markets
- Millisecond HFT competition for obvious opportunities

### Intra-Platform Arbitrage

When dependent markets misprice probability distributions:
- Individual swing state markets sum to 87% probability
- National "Trump wins" market trades at 65%
- Buying the underpriced distribution captures guaranteed profit when probabilities converge

## Platform Comparison

| Platform | Settlement | Regulation | Fee Range |
|----------|-----------|-----------|-----------|
| Polymarket | USDC | Crypto-native | 0% (plus gas) |
| Kalshi | USD | CFTC-regulated | 0.6-1.75% |
| PredictIt | USD | CFTC (no-action letter) | 10% of profits |
| Robinhood | USD | CFTC via CDNA | Variable |

## Behavioral Biases and Mispricing Patterns

### Longshot Bias
Retail traders systematically overpay for low-probability outcomes ($0.01-$0.15) seeking lottery-like payoffs. Professional traders exploit by selling tail events and buying high-probability outcomes.

### Recency Bias
Prices overreact to recent news then mean-revert, creating short-term reversals. Markets show negative autocorrelation in daily price changes.

### Volume Distortions
National presidential markets showed highest volume but greater inefficiency than lower-liquidity state-level markets. Attention-driven mispricing overwhelms information aggregation in high-profile markets.

## CLOB vs AMM Architecture

Polymarket originally used AMM with Constant Product formula but migrated to CLOB in 2023 for superior price discovery and capital efficiency.

**AMM Mechanics (legacy):**
- Constant Product: x × y = k
- Logarithmic slippage for large orders
- Vulnerable to impermanent loss

**CLOB Mechanics (current):**
- Linear slippage based on orderbook depth: Δp ≈ Q / (2 × depth)
- Discrete price jumps from sparse orders
- No impermanent loss risk
- Market makers post limit orders at specific prices

## Kelly Criterion Implementation

Edge extraction requires two components: probability estimation superiority and Kelly-optimal position sizing.

**Expected value formula:**
- EV = p(true) × $1.00 - Market_Price

**Kelly criterion:**
- f* = (bp - q) / b

**Worked Example:**
- Market prices "Fed Rate Cut in March" at $0.60 (60% implied probability)
- Your econometric model forecasts 75% true probability
- b = (1 - 0.60) / 0.60 = 0.667
- f* = (0.667 × 0.75 - 0.25) / 0.667 = 0.375
- Kelly recommends 37.5% of bankroll in YES shares

**Fractional Kelly** (0.25x-0.5x) reduces volatility and protects against probability estimation errors.

## Key Excerpts

1. "Prediction market contracts are fully-collateralized digital options where YES + NO = $1.00 invariant enforces zero-sum structure. Alpha comes primarily from superior probability estimation combined with Kelly-optimal sizing."

2. "From Ng, Peng, Tao, Zhou (2025): Using unique dataset from Polymarket, Kalshi, PredictIt, and Robinhood during 2024 U.S. election, we find significant price disparities across platforms creating economically meaningful arbitrage opportunities."

3. "The deterministic payoff structure eliminates model risk present in vanilla options. If your probability forecast is calibrated, binary options offer the cleanest expression of edge. No volatility surface to model, no Greeks to hedge, just pure probability times payout."

## Scrape Notes
- **Content completeness:** full (Substack article was fully accessible with comprehensive content)
- **Note:** Article includes extensive bibliography with academic and industry references, making it a valuable reference document
