# Polymarket CTF Overview

## Metadata
- **URL:** https://docs.polymarket.com/trading/ctf/overview
- **Source:** Polymarket Documentation
- **Type:** documentation
- **Author:** Polymarket
- **Date Published:** Continuously updated
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Content

This is the official Polymarket documentation on the Conditional Token Framework (CTF), explaining the underlying token mechanics that power Polymarket's prediction markets.

## Conditional Token Framework (CTF)

The CTF (Conditional Tokens Framework), developed by Gnosis, is the technical foundation that enables Polymarket's prediction market mechanics. It allows the creation of outcome tokens (YES/NO) that are conditional on market resolution.

### Core Concepts

**Tokens:**
- Each binary market creates two ERC-1155 tokens: YES and NO
- Each token pays out $1.00 if that outcome occurs, $0.00 otherwise
- Traders hold positions in these tokens as evidence of their predictions

**Collateral:**
- All positions are backed by USDC collateral
- When you buy YES tokens, you deposit USDC which is held as collateral
- At resolution, winning tokens are redeemed for collateral

**The Fundamental Invariant:**
P_YES + P_NO = $1.00

This is enforced by the CTF contract logic. Holding 1 YES + 1 NO token is always worth exactly $1.00 at settlement (redeemable for 1 USDC), because you can always split/merge positions through the CTF.

### Key Technical Features

**1. Position Merging:**
Opposing positions (YES and NO for the same market) can be merged back into collateral. This is a key feature for market makers and arbitrageurs who want to close positions efficiently.

**2. Conditional Splitting:**
YES tokens can be conditionally split into more granular outcomes. For example, a "Candidate A wins" YES token can be split to create positions on "Candidate A wins by >5%" or "Candidate A wins by <5%".

**3. Cross-Market Implications:**
Because the CTF enforces mathematical relationships between tokens, mispricings in related markets create arbitrage opportunities. For example:
- If "Candidate A wins" YES = $0.70
- And "Candidate A wins the popular vote" YES = $0.65
- But the popular vote winner always wins the election (in US system)
- The second price is mathematically impossible (the winner of the popular vote must be the winner if they win the election)
- → Buy "A wins popular vote" at $0.65, wait for convergence, profit

### Market Resolution

**Resolution Process:**
1. Markets have an assigned resolution source (e.g., Associated Press, official government data)
2. The result is determined by the data source
3. Winning tokens are redeemed for $1.00 each
4. Losing tokens become worthless

**UMA Optimistic Oracle:**
Polymarket uses the UMA Optimistic Oracle for dispute resolution:
- A bond of $750 USDC is posted when reporting a market result
- A 2-hour dispute window allows anyone to challenge the result
- If contested, UMA token holders arbitrate via Schelling-point mechanism
- Most markets resolve without dispute

**Self-Resolving Markets:**
For markets with unambiguous outcomes (e.g., sports results from known sources), the system can self-resolve using predefined data sources.

### Trading Mechanics

**Order Matching:**
Polymarket uses a Central Limit Order Book (CLOB) architecture:
- Orders are matched on-chain via Polygon
- Off-chain order submission (gasless) for user experience
- EIP-712 signed orders for authentication
- Continuous trading with no market hours

**Price Display:**
Polymarket displays the midpoint of the best bid/ask spread as the current price. If the spread exceeds $0.10 or there are no orders, the last traded price is shown.

**Fee Structure:**
Polymarket charges zero trading fees on the primary platform. However, gas fees on Polygon still apply (typically <$0.01 per transaction).

**Maker Rewards:**
Polymarket distributes a portion of the spread (maker rewards) to liquidity providers who post limit orders. The reward formula is designed to incentivize tight spreads and consistent liquidity.

### API Access

**Gamma API:**
The Gamma API provides market metadata, event information, and historical data:
- Market lists, categories, and tags
- Historical prices and volumes
- Resolution data

**CLOB API:**
For direct order book access and trading:
- Order book depth and updates
- Trade history
- Order placement and cancellation
- WebSocket connections for real-time updates

## Key Excerpts

1. "The fundamental invariant P_YES + P_NO = $1.00 means that any pricing deviation from this sum represents an arbitrage opportunity — the market is self-correcting."

2. "Position merging allows traders to efficiently close positions by combining opposing YES/NO tokens back into collateral without needing to find a counterparty."

3. "The UMA Optimistic Oracle provides decentralized, tamper-resistant resolution with economic security through the $750 bond mechanism."

## Scrape Notes
- **Content completeness:** full (official Polymarket documentation was fully accessible)
- **Note:** This is the most authoritative source on Polymarket's technical architecture
