# Poly-Maker: Automated Market Making Bot for Polymarket

## Metadata
- **URL:** https://github.com/terrytrl100/polymarket-automated-mm
- **Source:** GitHub
- **Type:** code
- **Author:** terrytrl100 (forked from @defiance_cr)
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Content

## Overview

A market making bot for Polymarket prediction markets that automates the process of providing liquidity by maintaining orders on both sides of the book with configurable parameters. Poly-Maker includes real-time order book monitoring via WebSockets, two-sided market making, reward-optimized pricing, and automated market selection.

## Architecture

The repository consists of several interconnected modules:

- **poly_data**: Core data management and market making logic
- **poly_merger**: Utility for merging positions (based on open-source Polymarket code)
- **poly_stats**: Account statistics tracking
- **poly_utils**: Shared utility functions
- **data_updater**: Separate module for collecting market information
- **Python 3.9+** with latest setuptools
- **Node.js** (for poly_merger)

## Key Features

### Real-Time WebSocket Order Book Monitoring
The bot connects to Polymarket's WebSocket API to receive real-time order book updates, enabling immediate response to price changes.

### Two-Sided Market Making
Places buy and sell orders simultaneously, even without existing positions. Earns from both maker rewards and spread capture. Enabled via TWO_SIDED_MARKET_MAKING=true.

### Reward-Optimized Pricing
Calculates optimal order placement based on Polymarket's maker reward formula: S = ((v - s) / v)^2 where v is max_spread and s is distance from mid-price. Places orders at ~15% of max_spread distance for optimal reward/fill balance.

### Automated Market Selection
Data-driven market selection by profitability or daily rewards. Selects markets by profitability_score = gm_reward_per_100 / (volatility_sum + 1).

### Position Management
Includes risk controls and automated position merging via poly_merger module. Merges opposing YES/NO positions when mergeable amount > $20, freeing up locked capital.

### Customizable Parameters
All trade parameters are fetched from Google Sheets, allowing real-time adjustment without code changes.

## Setup and Configuration

### Environment Variables
- **PK**: Your private key for Polymarket
- **BROWSER_ADDRESS**: Your wallet address
- **SPOLYGON_RPC_URL**: Polygon RPC endpoint (default: polygon-rpc.com)
- **TWO_SIDED_MARKET_MAKING**: Enable two-sided market making (default: false)
- **AGGRESSIVE_MODE**: Skip safety checks (default: false)

### Market Selection Modes
```
# Automated selection by profitability (default)
python update_selected_markets.py

# High reward mode (markets with >= $100/day)
python update_selected_markets.py --min-reward 100 --max-markets 10

# Manual selection from "Volatility Markets" sheet
```

### Running the Bot
```
# Terminal 1: Data updater (run continuously in background)
python data_updater/data_updater.py

# Terminal 2: Trading bot
python main.py
```

## Order Management

### Reduced Order Churn
30-second cooldown between trading actions on price changes. Wider cancellation thresholds: 1.5% price diff, 25% size diff. Results in ~95% reduction in unnecessary order cancellations.

### Maker Reward Tracking
Automatically logs order snapshots every 5 minutes. Estimates hourly/daily rewards based on order placement.

## Key Excerpts

1. "Places orders at ~15% of max_spread distance for optimal reward/fill balance, maximizing maker rewards while maintaining fill probability."

2. "~95% reduction in unnecessary order cancellations through 30s cooldown + wider thresholds, significantly reducing gas fees."

3. "Automated position merging frees locked capital when you have both sides of a market, reducing gas fees and improving capital efficiency."

## Scrape Notes
- Content completeness: full
- Highly practical reference implementation for Polymarket market making
- Excellent for understanding real-world order management strategies
