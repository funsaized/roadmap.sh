# Polymarket CTF Overview

## Metadata
- **URL:** https://docs.polymarket.com/trading/ctf/overview
- **Source:** Polymarket Documentation
- **Type:** documentation
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Content

# Polymarket Conditional Tokens Framework (CTF) Overview

## What is the Conditional Tokens Framework?

The Conditional Tokens Framework (CTF) is the underlying infrastructure that powers Polymarket prediction markets. It enables the creation, trading, and settlement of binary outcome contracts (YES/NO tokens) on Ethereum/Polygon.

## Binary Outcome Mechanics

In the CTF:
- Each prediction market creates two fungible token types: **YES** tokens and **NO** tokens
- The fundamental invariant: **YES + NO = $1.00** at all times
- When you buy 1 YES share for $0.60, you spend $0.60 and receive 1 YES token and 1 NO token (bundled as a set)
- You can redeem the full set for $1.00 if the outcome resolves positively, or hold and sell

## Share Minting and Settlement

**Buying Shares:**
- When you submit an order and it matches, 1 YES + 1 NO share is atomically minted
- You pay $1.00 total (which goes to the liquidity pool/market maker)
- The exchange of shares for collateral happens atomically on-chain

**Resolving Markets:**
- When a market resolves to YES: YES tokens pay $1.00, NO tokens pay $0.00
- When a market resolves to NO: NO tokens pay $1.00, YES tokens pay $0.00
- Holders of winning tokens can redeem for the payout amount

## Order Matching

Polymarket uses a **CLOB (Central Limit Order Book)** mechanism:
- Orders are matched based on price-time priority
- Makers post limit orders; takers sweep the order book
- Real-time price discovery through continuous trading
- No AMM slippage formula — linear price discovery from order book depth

## Position Management

**Opening Positions:**
- Buy YES if you believe the event will occur
- Buy NO if you believe the event will not occur
- Position value changes as the market price changes

**Closing Positions:**
- Sell your shares at any time before resolution
- Profit/loss = (exit price - entry price) × position size

**Position Merging:**
- You can merge opposing YES/NO positions in the same market
- This frees up locked capital (receiving back the difference)
- Example: 100 YES @ $0.40 + 100 NO @ $0.30 → receive $70, keep 100 shares of each

## Liquidity and Spread

- Polymarket charges **zero trading fees** on the main platform
- Liquidity is provided by market makers operating on the CLOB
- Bid-ask spreads are determined by market maker pricing
- Spreads tend to be tightest for high-volume markets

## Collateral and Risk

- All positions are backed by **USDC** collateral on Polygon
- Positions are fully collateralized — no fractional reserve
- No counterparty risk: smart contracts enforce settlement
- Funds are locked in smart contracts until position is closed or market resolves

## Resolution Process

Markets resolve based on the outcome of real-world events:
- Polymarket uses the **UMA Optimistic Oracle** for dispute resolution
- A $750 USDC bond is posted by the reporter
- 2-hour dispute window before resolution is finalized
- Schelling-point arbitration by UMA token holders if contested

## Key Excerpts

1. "YES + NO = $1.00 invariant: buying a full set costs exactly $1.00 regardless of market price"
2. "Shares are atomically minted when orders match — no fractional reserve, no counterparty credit risk"
3. "CLOB mechanism replaced AMM in 2023 for superior price discovery and capital efficiency"
4. "Zero trading fees on Polymarket's primary platform"

## Scrape Notes
- **Content completeness:** full
- **Issue:** None — clean extraction
