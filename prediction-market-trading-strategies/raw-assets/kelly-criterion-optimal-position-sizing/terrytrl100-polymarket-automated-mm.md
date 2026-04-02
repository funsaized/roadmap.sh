# Poly-Maker: Automated Market Making Bot for Polymarket

## Metadata
- **URL:** https://github.com/terrytrl100/polymarket-automated-mm
- **Source:** GitHub / terrytrl100
- **Type:** code/repository
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** medium

## Content

# Poly-Maker: Automated Market Making Bot for Polymarket

## Overview

Poly-Maker is an automated market making bot for Polymarket prediction markets. It automates providing liquidity by maintaining orders on both sides of the order book with configurable parameters configured via Google Sheets.

## Key Features

- **Real-time order book monitoring via WebSockets**
- **Two-sided market making** — Places buy and sell orders simultaneously
- **Reward-optimized pricing** — Calculates optimal order placement based on Polymarket's maker reward formula
- **Automated market selection** — Data-driven market selection by profitability or daily rewards
- **Position management with risk controls** and automated position merging
- **Customizable trade parameters** fetched from Google Sheets
- **Maker reward tracking** — Real-time visibility into estimated rewards
- **Reduced order churn** — Intelligent cancellation thresholds to minimize gas fees

## Reward Optimization Formula

The bot calculates optimal order placement based on Polymarket's maker reward formula:

```
S = ((v - s) / v)^2
```

Where:
- v = max_spread
- s = distance from mid-price

Places orders at ~15% of max_spread distance for optimal reward/fill balance. Maximizes maker rewards while maintaining fill probability.

## Two-Sided Market Making

Enables placing buy and sell orders simultaneously, even without existing positions. Earns from both maker rewards and spread capture. Enabled via TWO_SIDED_MARKET_MAKING=true in .env.

## Position Merging

The poly_merger module automatically merges opposing YES/NO positions:
- Frees up locked capital when you have both sides of a market
- Triggers when mergeable amount > $20 (configurable)
- Built on open-source Polymarket code
- Reduces gas fees and improves capital efficiency

## Configuration

Key environment variables:
- PK: Your private key for Polymarket
- BROWSER_ADDRESS: Your wallet address
- SPREADSHEET_URL: Google Sheets URL
- TWO_SIDED_MARKET_MAKING: Enable two-sided market making (default: false)
- POLYGON_RPC_URL: Polygon RPC endpoint

## Key Excerpts

1. "Orders placed at ~15% of max_spread distance for optimal reward/fill balance using formula S = ((v - s) / v)^2"
2. "Two-sided market making earns from both maker rewards and spread capture simultaneously"
3. "Position merging frees locked capital when opposing YES/NO positions exist in the same market"
