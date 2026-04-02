# Conditional Token Framework (CTF) Overview

## Metadata
- **URL:** https://docs.polymarket.com/trading/ctf/overview
- **Source:** docs.polymarket.com
- **Type:** documentation
- **Author:** Polymarket
- **Date Published:** Unknown
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Overview

The Conditional Token Framework (CTF) is the token standard underlying Polymarket's prediction market infrastructure. It enables the creation and trading of outcome tokens — instruments that pay out based on whether a specific event occurs. The CTF was developed by Gnosis and is now the foundational standard for binary prediction markets on Polygon.

## What Are Conditional Tokens?

Conditional tokens are ERC-1155 multi-token standard instruments where ownership of tokens is conditional on the resolution of a specific event. Unlike traditional tokens where ownership is absolute, conditional tokens derive their value from an external outcome.

For a binary prediction market, the CTF creates two token types for each market:

- **YES tokens**: Pay out $1 if the event occurs, $0 otherwise
- **NO tokens**: Pay out $1 if the event does not occur, $0 otherwise

These two token types are complements — if YES tokens pay out, NO tokens are worthless, and vice versa. This creates the fundamental pricing invariant: P(YES) + P(NO) = $1.00.

## Key Properties

### Conditional Ownership

The core innovation of CTF is that token ownership is conditional. This means:
- Tokens cannot be transferred freely until the event is resolved
- The condition (event outcome) determines the redemption value
- Smart contracts enforce the conditional logic on-chain

### Binary Resolution

Binary markets resolve to one of two outcomes:
- YES occurs: YES tokens redeem for $1, NO tokens become worthless
- NO occurs: NO tokens redeem for $1, YES tokens become worthless

This binary structure simplifies pricing and settlement while enabling complex conditional logic through token composition.

### Split and Merge Operations

The CTF allows holders to split their collateral into a set of outcome tokens, or merge outcome tokens back into collateral. This is crucial for:
- **Entering positions**: Deposit $1 collateral, receive 1 YES + 1 NO (can then sell one side)
- **Exiting positions**: Combine YES + NO back to $1 collateral before resolution
- **Arbitrage**: Exploiting price discrepancies between outcome tokens and collateral

## Market Structure

### Creating Markets

Market creators define:
- The question being asked (e.g., "Will BTC close above $100,000 on Dec 31, 2025?")
- The outcomes (typically YES/NO for binary markets)
- The resolution source (e.g., Chainlink oracle, UMA Optimistic Oracle)
- Settlement timing and dispute mechanisms

### Liquidity Provision

LP tokens represent fractional ownership of the market's liquidity pool. When you provide liquidity:
1. You deposit collateral (e.g., USDC)
2. The system creates a set of outcome tokens
3. You receive LP tokens representing your share
4. Trading fees accumulate in the pool
5. When you withdraw, you receive your proportional share of remaining collateral + accumulated fees

### Fee Structure

Polymarket charges fees on trades:
- Maker fees: Paid by liquidity providers
- Taker fees: Paid by traders taking liquidity

The fee schedule is designed to incentivize providing liquidity while maintaining competitive spreads.

## Resolution Mechanisms

### Chainlink Oracle

For crypto-native markets (BTC price targets, ETH outcomes), Chainlink provides decentralized price feeds. The oracle reports the final value at resolution time, determining which outcome occurred.

### UMA Optimistic Oracle

For more complex or subjective outcomes, Polymarket uses UMA's optimistic oracle system:
1. A reporter submits the outcome they believe is correct
2. A bond is posted (e.g., 760 USDC)
3. A challenge period allows others to dispute (2 hours on mainnet)
4. If uncontested, the outcome is finalized
5. If contested, UMA token holders arbitrate

This creates a Schelling-point incentive structure where honest reporting is economically rational.

## Trading with CTF

### Order Types

- **Market orders**: Execute immediately at current best price
- **Limit orders**: Set a desired price, wait for fill
- **Conditional orders**: Execute only if specified conditions are met

### Position Management

After buying YES or NO tokens:
- You can hold through resolution and collect $1 per winning token
- You can sell before resolution at market prices
- You can split/merge to adjust exposure
- You can use outcome tokens as collateral elsewhere in DeFi

### Settlement

When a market resolves:
1. Oracle reports the outcome
2. Winning tokens become redeemable for $1
3. Losing tokens become worthless
4. Users redeem winning tokens for collateral
5. Market is marked as resolved

## Smart Contract Architecture

The CTF is built on ERC-1155, enabling:
- Batch transfers of multiple outcome types
- Approval mechanisms for trading bots
- Gas-efficient multi-token operations
- Composable DeFi integration

Key contract interfaces:
- `createMarket()`: Deploy a new prediction market
- `splitPosition()`: Convert collateral to outcome tokens
- `mergePositions()`: Combine outcome tokens back to collateral
- `redeemPositions()`: Claim winnings after resolution
- `splitBinary()`: Specialized split for binary markets

## Key Excerpts

1. "Conditional tokens are ERC-1155 multi-token standard instruments where ownership of tokens is conditional on the resolution of a specific event. Unlike traditional tokens where ownership is absolute, conditional tokens derive their value from an external outcome."

2. "Binary markets resolve to one of two outcomes: YES occurs → YES tokens redeem for $1, NO tokens become worthless. NO occurs → NO tokens redeem for $1, YES tokens become worthless."

3. "For more complex or subjective outcomes, Polymarket uses UMA's optimistic oracle system: A reporter submits the outcome they believe is correct, a bond is posted (e.g., 760 USDC), a challenge period allows others to dispute (2 hours on mainnet). If uncontested, the outcome is finalized. If contested, UMA token holders arbitrate."

## Scrape Notes
- Content completeness: full
- High-quality technical documentation from Polymarket's official docs
- Covers CTF mechanics, market structure, resolution, and settlement
