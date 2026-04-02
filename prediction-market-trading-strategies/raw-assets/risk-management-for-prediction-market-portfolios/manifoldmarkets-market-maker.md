# Manifold Market Maker Bot

## Metadata
- **URL:** https://github.com/manifoldmarkets/market-maker
- **Source:** GitHub / Manifold Markets
- **Type:** code/documentation
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** medium

## Content

### Overview

A market-making bot for Manifold's prediction markets. Creates limit orders via the Manifold API to provide liquidity, and potentially make a profit.

### How It Works

The bot works by:
1. Computing an exponential moving average (EMA) and exponential moving variance of the probability
2. Creating limit orders above and below the current market price using these stats
3. If there's volatility in the market, it fills the pair of limit orders above and below, earning profit (buy low, sell high)

### Key Logic

**Price Calculation**:
```
upper_bound = EMA + k * sqrt(EMA_variance)
lower_bound = EMA - k * sqrt(EMA_variance)
```

Where k is a sensitivity parameter. Orders are placed at these bounds.

**EMA Parameters**:
- Uses exponential moving average of historical probabilities
- Also tracks exponential moving variance for volatility estimation
- These statistics determine where to place orders

**Spread Capture**: When both buy and sell orders fill (in a volatile market), the bot captures the spread as profit. The market maker is essentially buying at the lower bound and selling at the upper bound.

### Setup

1. Clone repository
2. Get Manifold API key from profile settings
3. Create `.env` file with API key and username
4. Run with `yarn start`

### Risk Considerations

- Bot places limit orders with mana (Manifold's internal currency)
- No real money is at risk, but mana losses are possible
- Volatility is key: sideways markets = no fills = no profit
- The bot can accumulate positions if one side keeps filling

### Extension Points

- Fork and extend with more advanced strategies
- Add position management controls
- Implement inventory rebalancing
- Add stop-loss mechanisms

## Key Excerpts

1. "The bot works by: Computing an exponential moving average (EMA) and exponential moving variance of the probability. Creating limit orders above and below the current market price using these stats. If there's volatility in the market, it fills the pair of limit orders above and below, earning profit (buy low, sell high)."

2. "Spread Capture: When both buy and sell orders fill (in a volatile market), the bot captures the spread as profit. The market maker is essentially buying at the lower bound and selling at the upper bound."

3. "Risk: Bot places limit orders with mana (Manifold's internal currency). Volatility is key: sideways markets = no fills = no profit."

## Scrape Notes
- Extracted from raw README.md
- Content includes bot logic, key formulas, setup, and risk considerations
- Content completeness: full
