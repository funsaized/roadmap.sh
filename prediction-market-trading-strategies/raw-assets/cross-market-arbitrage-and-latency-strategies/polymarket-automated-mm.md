# Polymarket Automated Market Making Bot

## Metadata
- **URL:** https://github.com/terrytrl100/polymarket-automated-mm
- **Source:** GitHub
- **Type:** code-documentation
- **Author:** terrytrl100 (forked from @defiance_cr)
- **Date Published:** 2024-2025
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** high

## Content

This repository is a forked and enhanced version of a Polymarket automated market making bot. The original creator is @defiance_cr, with this fork adding significant features and improvements.

## Core Features

### Real-time Order Book Monitoring
- WebSocket connections for live Polymarket order book data
- Continuous tracking of price movements and spread changes
- Order state management and reconciliation

### Two-Sided Market Making
- Simultaneously places buy and sell orders on both sides of the book
- Works even without existing positions (can create both YES and NO positions from scratch)
- Enabled via TWO_SIDED_MARKET_MAKING=true environment variable

### Reward-Optimized Order Placement
The bot calculates optimal order placement using Polymarket's maker reward formula:

**S = ((v - s) / v)²**

Where:
- v = max_spread (the spread between best bid and best ask)
- s = distance from mid-price

The bot places orders at approximately 15% of max_spread distance from mid-price for optimal reward/fill balance. This maximizes maker rewards while maintaining reasonable fill probability.

### Position Management with Risk Controls
- Automated position merging when opposing positions exist
- Risk controls to limit exposure per market
- Position size limits and inventory management

### Automated Market Selection
Three modes for selecting which markets to trade:

1. **Profitability Mode** (default):
   - Selects markets by profitability_score = gm_reward_per_100 / (volatility_sum + 1)
   - Filters: reward >= 1.0%, volatility > threshold

2. **High Reward Mode** (--min-reward flag):
   - Filters markets by minimum daily reward (e.g., >= $100/day or $150/day)
   - Automatically assigns trade sizes based on reward level

3. **Manual Selection**:
   - Users add markets directly to the "Selected Markets" Google Sheet
   - Can select from the "Volatility Markets" sheet for best opportunities

## Technical Architecture

### Data Flow
1. **data_updater** module continuously fetches market information from Polymarket
2. Calculates reward and volatility metrics for each market
3. Updates Google Sheets with market database
4. **Trading bot** reads from Google Sheets to select markets
5. WebSocket connection monitors order book in real-time
6. Bot places/modifies/cancels orders based on configured parameters

### Configuration
- Environment variables in .env file:
  - PK: Polymarket private key
  - BROWSER_ADDRESS: Wallet address
  - SPREADSHEET_URL: Google Sheets configuration URL
  - POLYGON_RPC_URL: Polygon RPC endpoint (default: polygon-rpc.com)
  - TWO_SIDED_MARKET_MAKING: Enable two-sided mode
  - AGGRESSIVE_MODE: Skip safety checks (use with caution)

### Position Merging
The poly_merger module handles merging of opposing YES/NO positions:
- Triggered when mergeable amount > $20 (configurable)
- Built on open-source Polymarket code
- Frees locked capital and reduces gas costs
- Improves overall capital efficiency

### Performance Improvements Over Original

The README documents specific improvements made in this fork:

| Feature | Improvement |
|---------|------------|
| Order Cancellations | ~95% reduction through 30-second cooldown and wider thresholds |
| Reward Optimization | Orders placed at optimal distance for maximum rewards |
| Market Selection | Automated data-driven selection vs. manual |
| Capital Efficiency | Automatic position merging |
| Gas Fees | Significantly reduced through smarter cancellation logic |

**Cooldown and Threshold Settings:**
- 30-second cooldown between trading actions on price changes
- 1.5% price difference threshold before order modification
- 25% size difference threshold before order modification
- Result: ~95% reduction in unnecessary order cancellations

## Risk Warning

The repository includes strong risk warnings:
- This code interacts with real markets and can lose real money
- Test thoroughly with small amounts before deploying significant capital
- The data_updater should ideally run on a different IP than the trading bot

## Key Excerpts

1. "Places buy and sell orders simultaneously, even without existing positions. Enabled via TWO_SIDED_MARKET_MAKING=true. Earns from both maker rewards and spread capture."

2. "The bot calculates optimal order placement based on Polymarket's maker reward formula: S = ((v - s) / v)². Places orders at ~15% of max_spread distance for optimal reward/fill balance."

3. "The poly_merger module automatically merges opposing YES/NO positions: frees up locked capital when you have both sides of a market. Built on open-source Polymarket code."

## Scrape Notes
- **Content completeness:** full (GitHub README was fully accessible with comprehensive documentation)
- **Note:** The detailed performance improvements and explicit risk warnings are valuable for understanding practical market making challenges
