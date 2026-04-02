# Polymarket Automated Market Making Bot

## Metadata
- **URL:** https://github.com/terrytrl100/polymarket-automated-mm
- **Source:** GitHub
- **Type:** code/documentation
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Content

### Overview

A market making bot for Polymarket prediction markets that automates the process of providing liquidity by maintaining orders on both sides of the order book with configurable parameters.

### Key Features

**Real-time Order Book Monitoring**
- Connects via WebSockets for live orderbook updates
- Monitors price movements and adjusts orders dynamically
- Maintains two-sided market making (bid and ask simultaneously)

**Reward-Optimized Pricing**
- Calculates optimal order placement based on Polymarket's maker reward formula
- Formula: `S = ((v - s) / v)^2` where v is max_spread and s is distance from mid-price
- Places orders at ~15% of max_spread distance for optimal reward/fill balance

**Position Management**
- Automatically manages positions with risk controls
- Supports position merging (combining opposing YES/NO positions)
- Tracks position sizes and exposure

**Market Selection**
- Data-driven selection of markets to trade
- Options: profitability mode, high reward mode, manual selection
- Filters markets by volatility, reward potential, and liquidity

### Risk Management Features

**Configurable Parameters**
- Max position size per market
- Max total positions across all markets
- Stop-loss thresholds
- Order size limits

**Inventory Risk Controls**
- Monitors inventory skew (unbalanced positions)
- Automatically adjusts order sizes to rebalance
- Prevents over-concentration in any single outcome

**Spread Management**
- Dynamic spread adjustment based on volatility
- Wider spreads during high volatility periods
- Tighter spreads when market is stable

### Architecture

The bot consists of several interconnected modules:
- `poly_data`: Core data management and market making logic
- `poly_merger`: Position merging utility
- `poly_stats`: Account statistics tracking
- `poly_utils`: Shared utility functions
- `data_updater`: Market information collection

### Configuration

Key parameters in the Google Sheets configuration:
- `max_spread`: Maximum spread from mid-price to place orders
- `order_size`: Base order size for each market
- `min_fill_probability`: Minimum probability of fill to place order
- `cancel_threshold`: Price movement threshold to cancel/replace orders

### Key Metrics Tracked

- Maker rewards (estimated hourly/daily)
- Position sizes by market
- Order fill rates
- Inventory balance (YES vs NO)
- P&L by market

## Key Excerpts

1. "Calculates optimal order placement based on Polymarket's maker reward formula: S = ((v - s) / v)^2 where v is max_spread and s is distance from mid-price. Places orders at ~15% of max_spread distance for optimal reward/fill balance."

2. "Position Management: Automatically manages positions with risk controls. Supports position merging (combining opposing YES/NO positions). Monitors inventory skew (unbalanced positions)."

3. "Key parameters: max_spread, order_size, min_fill_probability, cancel_threshold. The bot consists of: poly_data, poly_merger, poly_stats, poly_utils, data_updater."

## Scrape Notes
- Full README extracted successfully
- Content includes bot features, risk management, architecture, configuration, and metrics
- Content completeness: full
