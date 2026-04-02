# CTF Overview: Conditional Token Framework

## Metadata
- **URL:** https://docs.polymarket.com/trading/ctf/overview
- **Source:** Polymarket Documentation
- **Type:** documentation
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Overview

The Conditional Token Framework (CTF) is the token standard used by Polymarket to represent prediction market outcomes. Built on Gnosis Conditional Tokens, CTF tokens enable binary outcome trading where each market creates a pair of outcome tokens (YES and NO) that can be freely traded until the market resolves.

## How CTF Tokens Work

When a new prediction market is created on Polymarket, the CTF creates two ERC-1155 tokens representing the YES and NO outcomes. These tokens are minted in equal quantities when traders deposit collateral (USDC).

### Token Minting

Users deposit USDC collateral to mint complete sets of outcome tokens. Depositing 1 USDC typically yields 1 YES token and 1 NO token. The user can then trade these tokens independently on the order book.

### Splitting and Merging

The CTF allows splitting and merging of outcome token sets. Splitting converts collateral into a set of YES+NO tokens. Merging does the reverse — combining YES and NO tokens back into collateral. This creates arbitrage opportunities when token prices diverge from collateral value.

### Market Resolution

When a market resolves, the winning outcome tokens become redeemable for 1 USDC each. The losing tokens become worthless. Users must explicitly redeem their tokens after resolution to receive their payout.

## Key CTF Operations

### Split (Collateral → YES + NO)

Users can split their collateral into YES and NO tokens. This is the primary way to acquire positions.

### Merge (YES + NO → Collateral)

Merging YES and NO tokens back into collateral. This is typically used to extract value before market resolution or when the combined token value exceeds the collateral.

### Redeem (Winning Tokens → USDC)

After market resolution, winning tokens are redeemed at par value (1 token = 1 USDC).

## Technical Details

The CTF is implemented as a set of Ethereum smart contracts on Polygon. Key properties:

- **Token Standard**: ERC-1155 (multi-token standard allowing YES and NO as separate token IDs)
- **Collateral**: USDC (on Polygon)
- **Settlement**: Atomic on-chain settlement via Polygon PoS
- **Oracle**: UMA Optimistic Oracle with 2-hour dispute window
- **Smart Contracts**: Exchange contract audited by Chainsecurity

## Key Excerpts

1. "When a new prediction market is created on Polymarket, the CTF creates two ERC-1155 tokens representing the YES and NO outcomes."

2. "Merging YES and NO tokens back into collateral creates arbitrage opportunities when token prices diverge from collateral value."

3. "The Exchange contract is audited by Chainsecurity. All trading is non-custodial — users can always cancel orders onchain independently."

## Scrape Notes
- Content completeness: full
- Provides excellent overview of the CTF token mechanics
- Key reference for understanding how Polymarket's token infrastructure works
