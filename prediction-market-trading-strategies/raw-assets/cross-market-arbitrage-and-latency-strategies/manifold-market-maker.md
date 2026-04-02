# Manifold Markets Market Maker Bot

## Metadata
- **URL:** https://github.com/manifoldmarkets/market-maker
- **Source:** GitHub
- **Type:** code-documentation
- **Author:** Manifold Markets
- **Date Published:** Unknown
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** medium

## Content

This is a simple market-making bot for Manifold's prediction markets. Manifold Markets is a different prediction market platform (not Polymarket or Kalshi), but the bot's approach provides useful patterns for understanding prediction market market making.

## Core Mechanism

The bot works by:
1. Computing an exponential moving average (EMA) and exponential moving variance of the market probability
2. Creating limit orders above and below the current market price using these statistics
3. If there's volatility, the paired orders get filled (buy low, sell high), earning profit

## Setup Requirements

1. Clone the repository
2. Obtain Manifold API key (from Your profile → Edit → API key)
3. Create .env file with:
   - MANIFOLD_API_KEY
   - MANIFOLD_USERNAME

4. Install npm packages with yarn
5. Run `yarn start`

**Warning:** The bot places limit orders with your mana (Manifold's internal currency). Understand the risk before running.

## Design Philosophy

The simplicity of this bot is notable compared to more complex Polymarket bots. The key insight is using exponential moving statistics to detect when the market is moving — if the market is volatile, both sides of the market maker's quotes may be filled, resulting in a round-trip profit.

This approach is similar to mean-reversion strategies in traditional markets: when prices deviate from their recent average, place orders expecting them to revert. In prediction markets, this means placing orders at prices away from the current market probability, expecting the market to revert to its recent average or for informed traders to move prices in a direction that fills your quote.

## Relevance to Polymarket/Kalshi

While Manifold Markets uses a different platform with different mechanics (mana-based, not real-money), the strategy pattern is applicable:
- Using statistical measures of recent price history to set quote prices
- Two-sided market making (place both buy and sell orders)
- Capturing spread when volatility causes both sides to be filled

## Key Excerpts

1. "The bot works by first computing an exponential moving average and exponential moving variance of the probability. Then it creates limit orders above and below the current market price using these stats."

2. "If there's volatility in the market, it will fill the pair of limit orders above and below, which will earn you profit (buy low, sell high!)."

## Scrape Notes
- **Content completeness:** partial (GitHub README was brief; limited detailed content)
- **Note:** This is a simpler, less mature project than the Polymarket bots; primarily useful as a reference for the basic market making pattern
