# Manifold Markets Market Maker Bot

## Metadata
- **URL:** https://github.com/manifoldmarkets/market-maker
- **Source:** GitHub / Manifold Markets
- **Type:** code/repository
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** medium

## Content

# Manifold Markets Market Maker Bot

## Overview

A market-making bot for Manifold's prediction markets. The bot creates limit orders via the Manifold API to provide liquidity, and potentially make a profit.

## How It Works

The bot works by first computing an exponential moving average and exponential moving variance of the probability. Then it creates limit orders above and below the current market price using these stats.

If there's volatility in the market, it will fill the pair of limit orders above and below, which will earn profit (buy low, sell high!).

In any case, creating open limit orders increases the liquidity in the markets, which is a service to traders.

## Setup

1. Clone the repository
2. Locate your Manifold API Key (Your profile => Edit => API key)
3. Create a .env file with your API key and username:

```
MANIFOLD_API_KEY=xxxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
MANIFOLD_USERNAME=YourUsername
```

4. Install npm packages with yarn
5. Run yarn start

## Key Excerpts

1. "Computes exponential moving average and variance of probability, then creates limit orders above and below the current market price"
2. "Fills occur when volatility causes both the upper and lower limit orders to execute, earning buy-low-sell-high profit"
