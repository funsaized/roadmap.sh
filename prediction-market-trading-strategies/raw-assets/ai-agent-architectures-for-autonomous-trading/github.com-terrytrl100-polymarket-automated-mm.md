# Poly-Maker: Automated Market Making Bot for Polymarket

## Metadata
- **URL:** https://github.com/terrytrl100/polymarket-automated-mm
- **Source:** github.com/terrytrl100/polymarket-automated-mm
- **Type:** code/documentation
- **Author:** terrytrl100 (forked from @defiance_cr)
- **Date Published:** 2024-2025
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Overview

Poly-Maker is a comprehensive automated market making bot for Polymarket. It automates the process of providing liquidity by maintaining orders on both sides of the book with configurable parameters, managed via Google Sheets.

**Disclaimer**: This code interacts with real markets and can lose real money. Test thoroughly before deploying significant capital.

## Key Features

### Real-time Order Book Monitoring
- WebSocket connections for live orderbook updates
- Continuous market data streaming from Polymarket's CLOB

### Two-Sided Market Making
- Places buy and sell orders simultaneously
- Can operate even without existing positions
- Enabled via TWO_SIDED_MARKET_MAKING=true
- Earns from both maker rewards and spread capture

### Reward-Optimized Pricing
Bot calculates optimal order placement based on Polymarket's maker reward formula:
```
S = ((v - s) / v)²
```
Where v = max_spread and s = distance from mid-price. Places orders at ~15% of max_spread distance for optimal reward/fill balance.

### Automated Market Selection
Three selection modes:
1. **Automated (default)**: Selects by profitability_score = gm_reward_per_100 / (volatility_sum + 1)
2. **High Reward Mode**: Markets with >= $100/day rewards
3. **Manual**: User-selected markets from Volatility Markets sheet

### Position Management
- Automatic position merging (when you have both YES and NO sides)
- Risk controls and configurable trade parameters
- Capital efficiency optimization through merging opposing positions

### Google Sheets Integration
All configuration managed via Google Spreadsheets:
- Selected Markets: Markets to trade (auto or manual)
- All Markets: Database of all Polymarket markets with metrics
- Volatility Markets: Filtered high-volatility markets
- Hyperparameters: Configurable trading parameters
- Maker Rewards: Real-time reward tracking

## Architecture

Repository modules:
- `poly_data`: Core data management and market making logic
- `poly_merger`: Position merging utility (based on open-source Polymarket code)
- `poly_stats`: Account statistics tracking
- `poly_utils`: Shared utility functions
- `data_updater`: Market information collection module

## Installation

```
git clone https://github.com/yourusername/poly-maker.git
cd poly-maker
pip install -r requirements.txt
cd poly_merger && npm install && cd ..
cp .env.example .env
# Configure credentials in .env
```

Required environment variables:
- `PK`: Private key for Polymarket
- `BROWSER_ADDRESS`: Wallet address
- `SPREADSHEET_URL`: Google Sheets URL

Requirements:
- Python 3.9+
- Node.js (for poly_merger)
- Google Sheets API credentials
- Polymarket account

## Usage

### Update Market Data
```
python data_updater/data_updater.py
```
Should run continuously in background (different IP than trading bot recommended).

### Select Markets
```
# Default automated selection
python update_selected_markets.py

# High reward mode ($100+/day)
python update_selected_markets.py --min-reward 100 --max-markets 10

# Manual selection
# Add markets to "Selected Markets" sheet
```

### Start Trading Bot
```
python main.py
```

## Order Management

### Cancellations
- 30-second cooldown between trading actions on price changes
- Wider cancellation thresholds: 1.5% price diff, 25% size diff
- Result: ~95% reduction in unnecessary order cancellations, saving gas fees

### Two-Sided Market Making
When enabled, places both buy and sell orders simultaneously:
- Buy order on one side, sell on the other
- Earns spread capture + maker rewards
- Significantly improves capital efficiency

### Position Merging
The `poly_merger` module automatically merges opposing YES/NO positions:
- Frees locked capital when both sides of a market are held
- Triggers when mergeable amount > $20 (configurable)
- Reduces gas fees, improves capital efficiency
- Built on open-source Polymarket code

## Risk Controls

- Configurable max markets (prevents over-diversification)
- Per-market position size limits
- Automatic spread adjustment based on volatility
- Configurable safety checks

## Performance Metrics

| Feature | Improvement |
|---------|------------|
| Order Cancellations | ~95% reduction via cooldown + wider thresholds |
| Reward Optimization | Orders at optimal distance for max rewards |
| Market Selection | Automated data-driven selection |
| Capital Efficiency | Automatic position merging |
| Gas Fees | Significantly reduced through smarter cancellation |

## Key Excerpts

1. "The bot calculates optimal order placement based on Polymarket's maker reward formula: S = ((v - s) / v)² where v is max_spread and s is distance from mid-price. Places orders at ~15% of max_spread distance for optimal reward/fill balance."

2. "30-second cooldown between trading actions on price changes. Wider cancellation thresholds: 1.5% price diff, 25% size diff. Result: ~95% reduction in unnecessary order cancellations, saving gas fees."

3. "The poly_merger module automatically merges opposing YES/NO positions: Frees up locked capital when you have both sides of a market. Triggers when mergeable amount > $20 (configurable). Reduces gas fees and improves capital efficiency."

## Scrape Notes
- Content completeness: full
- Comprehensive README with operational details
- Real-world production bot with risk management patterns
- MIT licensed
