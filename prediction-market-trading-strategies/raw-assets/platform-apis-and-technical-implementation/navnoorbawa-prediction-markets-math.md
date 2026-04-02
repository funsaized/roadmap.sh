# The Math of Prediction Markets: Binary Options, Kelly Criterion, and CLOB Pricing Mechanics

## Metadata
- **URL:** https://navnoorbawa.substack.com/p/the-math-of-prediction-markets-binary
- **Source:** Substack (Navnoor Bawa)
- **Type:** article
- **Author:** Navnoor Bawa
- **Date Published:** Unknown
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Binary Contract Structure

Prediction market contracts are fully-collateralized binary options with terminal payoffs of $1.00 or $0.00. On Polymarket, each market creates two ERC-1155 tokens (YES and NO) via the Gnosis Conditional Tokens Framework. On Kalshi, the same binary structure applies with fiat USD settlement.

The foundational invariant is contract-enforced: P_YES + P_NO = $1.00. Violation creates immediate arbitrage. If YES trades at $0.55 and NO at $0.40 (total = $0.95), buying both locks $0.05 risk-free profit at settlement.

Shares are atomically minted when opposing orders match. The exchange collects $1.00 total, mints 1 YES + 1 NO token simultaneously, distributes to each party. Zero fractional reserves, zero counterparty credit risk, 100% collateralization.

## Price Discovery

Price discovery occurs through order book mechanics. Polymarket displays the midpoint of best bid/ask spread (or last traded price if spread exceeds $0.10). YES @ $0.72 equals 72% market-assigned probability.

Polymarket uses hybrid-decentralized infrastructure: off-chain order matching (gasless), EIP-712 signed orders, on-chain settlement via Polygon PoS with USDC collateral. Kalshi operates as fully-regulated exchange under CFTC oversight with fiat USD settlement.

## Resolution Mechanisms

**Polymarket**: UMA Optimistic Oracle with $750 USDC bond, 2-hour dispute window, Schelling-point arbitration by UMA token holders if contested.

**Kalshi**: Event contracts self-certify outcomes based on authoritative data sources (AP, NBC, government statistics).

The October 2, 2024 D.C. Circuit decision allowed Kalshi to list political event contracts and materially changed the regulatory landscape.

## P&L Mechanics

Pre-resolution P&L follows standard equity mechanics: P&L = (Exit_Price - Entry_Price) × Position_Size. Example: Buy 5,000 YES @ $0.28, sell @ $0.61 → $1,650 profit.

Holding to resolution creates asymmetric convexity tied to entry price. Low-probability tails ($0.05-$0.20) offer lottery-like payoff structures. Buy 10,000 YES @ $0.12, pay $1,200. If event occurs, receive $10,000 → $8,800 net profit (+733%).

## Zero-Sum Structure

The deterministic payoff structure eliminates model risk present in vanilla options. Zero-sum means every dollar won equals a dollar lost by counterparty — pure information transfer. Polymarket charges no trading fees. Kalshi charges variable fees calculated as ceil(0.07 × contracts × price × (1-price)), ranging from ~0.6% for tail events to 1.75% at mid-market prices.

## Edge Extraction

Expected value formula: EV = p(true) × $1.00 - Market_Price

Kelly criterion determines optimal bankroll fraction: f* = (bp - q) / b

Worked example: Market prices "Fed Rate Cut in March" at $0.60. Your model forecasts 75% true probability. Net odds b = (1-0.60)/0.60 = 0.667. f* = (0.667 × 0.75 - 0.25) / 0.667 = 0.375. Kelly recommends 37.5% of bankroll in YES shares.

## Cross-Platform Arbitrage

Cross-platform arbitrage exploits price disparities between Polymarket, Kalshi, PredictIt. Research found persistent opportunities with accuracy rates: PredictIt 93%, Kalshi 78%, Polymarket 67%.

Example: Polymarket YES $0.42 + Kalshi NO $0.56 = $0.98 cost → $1.00 guaranteed payout → $0.02 profit (2.04% return). These opportunities persist due to low institutional participation, platform fragmentation, thin liquidity in niche markets, and high latency HFT competition.

## Behavioral Biases Exploitable

**Longshot Bias**: Retail traders systematically overpay for low-probability outcomes ($0.01-$0.15) seeking lottery payoffs. Professionals exploit by selling tail events and buying high-probability outcomes.

**Recency Bias**: Prices overreact to recent news then mean-revert, creating short-term reversals. Momentum doesn't persist.

**Volume Distortions**: National presidential markets showed highest volume but greater inefficiency than lower-liquidity state-level markets.

## CLOB vs AMM Mechanics

Polymarket originally used AMM with Constant Product formula but migrated to CLOB in 2023 for superior price discovery. Under CLOB, linear slippage is based on orderbook depth: Δp ≈ Q / (2 × depth). No impermanent loss risk unlike AMM.

## Key Platform Documentation Links

- Conditional Tokens Framework: https://conditional-tokens.readthedocs.io/
- Polymarket CLOB: https://docs.polymarket.com/developers/CLOB/introduction
- Polymarket Price Calculation: https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated
- Polymarket Fees: https://docs.polymarket.com/polymarket-learn/trading/fees
- Kalshi: https://kalshi.com/about
- Kalshi Fee Structure: https://help.kalshi.com/trading/fees

## Key Excerpts

1. "The fundamental invariant is contract-enforced: P_YES + P_NO = $1.00. Violation creates immediate arbitrage — if sum < $1.00, buying both locks risk-free profit."

2. "Kelly criterion recommends 37.5% of bankroll in YES shares with 75% true probability vs 60% market price, yielding 25% ROI if forecast correct."

3. "Cross-platform arbitrage opportunities persist due to low institutional participation, platform fragmentation, thin liquidity in niche markets, and high latency HFT competition."

## Scrape Notes
- Content completeness: full
- Comprehensive technical overview of prediction market mechanics
- Excellent resource covering binary options pricing, Kelly criterion, and CLOB mechanics
