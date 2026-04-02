# Manifold Markets Market Maker Bot

## Metadata
- **URL:** https://github.com/manifoldmarkets/market-maker
- **Source:** github.com/manifoldmarkets/market-maker
- **Type:** code
- **Author:** Manifold Markets
- **Date Published:** Unknown
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** medium

## Content

## Overview

A market-making bot for Manifold's prediction markets. The bot creates limit orders via the Manifold API to provide liquidity, and potentially make a profit.

## How It Works

The bot computes an exponential moving average (EMA) and exponential moving variance of the probability. It then creates limit orders above and below the current market price using these statistics.

If there's volatility in the market, it will fill the pair of limit orders above and below, which will earn the bot profit (buy low, sell high). In any case, creating open limit orders increases liquidity in the markets, which benefits all traders.

## Strategy Logic

1. **Calculate EMA of probability**: Tracks the smooth average probability over time
2. **Calculate EMV (Exponential Moving Variance)**: Tracks the volatility of the probability
3. **Place orders**: Creates buy orders below EMA and sell orders above EMA, with distance based on EMV
4. **Wait for fills**: If volatility causes the price to reach the orders, they fill and generate profit

## Installation

```bash
# Clone the repository
# Get your Manifold API Key (Profile => Edit => API key)
# Create .env file:
MANIFOLD_API_KEY=xxxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
MANIFOLD_USERNAME=YourUsername
# Install npm packages with yarn
# Run: yarn start
```

## Key Excerpts

1. "The bot works by first computing an exponential moving average and exponential moving variance of the probability. Then it creates limit orders above and below the current market price using these stats."

2. "If there's volatility in the market, it will fill the pair of limit orders above and below, which will earn you profit (buy low, sell high!)."

## Scrape Notes
- Content completeness: partial
- Short README, limited technical detail
- Basic EMA/EMV-based market making strategy
- Useful as a simple reference implementation
