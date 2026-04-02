# Manifold Markets Market Maker

## Metadata
- **URL:** https://github.com/manifoldmarkets/market-maker
- **Source:** GitHub
- **Type:** code
- **Author:** Manifold Markets
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** medium

## Content

## Overview

A market-making bot for Manifold's prediction markets. The bot creates limit orders via the Manifold API to provide liquidity, potentially earning profit through the bid-ask spread.

## How It Works

The bot computes an exponential moving average (EMA) and exponential moving variance of the probability for each market. It then creates limit orders above and below the current market price using these statistics.

If there's volatility in the market, the bot's paired limit orders (above and below) will both get filled, earning profit by buying low and selling high. Creating open limit orders also increases market liquidity, which benefits all traders.

## Setup

1. Clone the repository
2. Locate your Manifold API Key (Your profile => Edit => API key)
3. Create a .env file:
```
MANIFOLD_API_KEY=xxxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
MANIFOLD_USERNAME=YourUsername
```
4. Install npm packages with yarn
5. Run: yarn start

## Key Excerpts

1. "The bot computes an exponential moving average and exponential moving variance of the probability, then creates limit orders above and below the current market price using these stats."

2. "If there's volatility in the market, it will fill the pair of limit orders above and below, earning profit (buy low, sell high)."

## Scrape Notes
- Content completeness: full
- Simple reference implementation focused on EMA-based market making
- Useful as a basic pattern for market making bot architecture
