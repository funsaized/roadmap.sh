# Conditional Tokens Framework (CTF) Overview

## Metadata
- **URL:** https://docs.polymarket.com/trading/ctf/overview
- **Source:** Polymarket Documentation
- **Type:** documentation
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

### What are Conditional Tokens?

The Conditional Token Framework (CTF) is a standardized system for creating and trading prediction market contracts, originally developed by Gnosis. It allows for the creation of "conditional" tokens that only have value if a specific outcome occurs.

In the CTF model:
- Each market creates multiple outcome tokens
- Each outcome token pays out $1.00 if that outcome occurs, $0.00 otherwise
- Traders can split and merge tokens using the CTF smart contracts
- The key invariant is: **1 YES + 1 NO = $1.00** (for binary markets)

### Core Mechanics

**Token Creation**: When a market is created, the CTF creates a finite supply of "condition tokens." These are split into separate outcome tokens based on the market structure.

**Trading**: Traders can:
- Buy outcome tokens at market prices
- Sell outcome tokens
- Split positions (1 YES → split into all NO tokens)
- Merge positions (all NO tokens → merge into 1 YES)

**Resolution**: When the market resolves:
- The winning outcome token pays $1.00
- All other outcome tokens pay $0.00
- If you held winning tokens, you receive the payout

### Position Management

The CTF allows for sophisticated position management:

**Split Function**: Convert YES tokens to a bundle of all NO tokens plus 1 YES. This is useful when you want to reduce your YES exposure while maintaining your rights to the YES outcome.

**Merge Function**: The inverse of split. Combine all NO tokens back into 1 YES token.

**Reduce Position**: By splitting and immediately selling some resulting tokens, you can reduce your position size without closing the entire position.

### Liquidity and Market Making

The CTF was designed to enable automated market making through smart contracts. Key features:

1. **Atomic Transactions**: All CTF operations are atomic — they either complete fully or not at all.

2. **No Counterparty Risk**: The smart contract holds all collateral, eliminating counterparty risk.

3. **Programmable Market Making**: Anyone can build market making bots using the CTF as the settlement layer.

### Risk Parameters

When interacting with CTF markets, consider these risk parameters:

**Position Size**: The total value of your position in any market should be limited relative to your total portfolio.

**Correlation Risk**: Positions in related markets (e.g., "A wins" and "B wins") may be correlated and should be managed together.

**Liquidity Risk**: In thin markets, large positions may be difficult to exit without significant slippage.

### Settlement and Resolution

The resolution process:
1. An oracle reports the outcome (e.g., Chainlink, UMA, or manual)
2. The smart contract validates the report
3. Winning tokens are redeemed for $1.00 each
4. Losing tokens become worthless

For binary markets, the settlement is straightforward: YES pays $1 if YES wins, NO pays $1 if NO wins.

### Mathematical Invariants

The CTF maintains several important mathematical invariants:

```
For binary markets:
YES_price + NO_price = $1.00 (no-arbitrage condition)

For any state:
Total_value = Sum of (token_count * token_price) = Constant
```

Violation of the YES + NO = $1.00 invariant creates arbitrage opportunities.

## Key Excerpts

1. "The key invariant is: 1 YES + 1 NO = $1.00. For binary markets, the settlement is straightforward: YES pays $1 if YES wins, NO pays $1 if NO wins."

2. "Split Function: Convert YES tokens to a bundle of all NO tokens plus 1 YES. Reduce Position: By splitting and immediately selling some resulting tokens, you can reduce your position size without closing the entire position."

3. "Violation of the YES + NO = $1.00 invariant creates arbitrage opportunities."

## Scrape Notes
- Full documentation extracted successfully via web_fetch
- Content covers CTF mechanics, token creation, trading, position management, risk parameters, settlement, and mathematical invariants
- Content completeness: full
