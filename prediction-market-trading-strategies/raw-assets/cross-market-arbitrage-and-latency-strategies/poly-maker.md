# Poly-Maker: Automated Market Making Bot for Polymarket

## Metadata
- **URL:** https://github.com/warproxxx/poly-maker
- **Source:** GitHub
- **Type:** code-documentation
- **Author:** warproxxx
- **Date Published:** 2024-2025
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** high

## Content

Poly-Maker is a Python-based automated market making bot for Polymarket. This is a comprehensive solution for providing liquidity to Polymarket prediction markets by maintaining orders on both sides of the order book.

**Important Disclaimer from Author:** "In today's market, this bot is not profitable and will lose money. Use it as a reference implementation for building your own market making strategies, not as a ready-to-deploy solution. Given the increased competition on Polymarket, I don't see a point in playing with this unless you're willing to dedicate a significant amount of time."

## Architecture Overview

The system consists of several interconnected modules:

- **poly_data**: Core data management and market making logic
- **poly_merger**: Utility for merging positions (based on open-source Polymarket code)
- **poly_stats**: Account statistics tracking
- **poly_utils**: Shared utility functions
- **data_updater**: Separate module for collecting market information

## Key Features

### Real-time Order Book Monitoring
- WebSocket connections for live order book updates
- Continuous price and spread tracking
- Position state management

### Two-Sided Market Making
- Places buy (YES) and sell (NO) orders simultaneously
- Earns from both maker rewards and spread capture
- Enabled via TWO_SIDED_MARKET_MAKING=true

### Position Management
- Automatic position merging functionality
- Risk controls and automated position consolidation
- Capital efficiency optimization through opposing position netting

### Reward-Optimized Pricing
The bot calculates optimal order placement based on Polymarket's maker reward formula:

**S = ((v - s) / v)²**

Where:
- v = max_spread
- s = distance from mid-price

Orders are placed at approximately 15% of max_spread distance for optimal reward/fill balance.

### Automated Market Selection
Markets can be selected automatically by profitability or daily rewards:
- Profitability Mode: Selects by profitability_score = gm_reward_per_100 / (volatility_sum + 1)
- High Reward Mode: Filters by minimum daily reward threshold

## Technical Stack

- Python 3.9.10+
- UV package manager (fast, reliable)
- Node.js (for poly_merger module)
- Google Sheets API (for configuration management)
- Polymarket API credentials

## Configuration via Google Sheets

The bot is configured via a Google Spreadsheet with several worksheets:
- **Selected Markets**: Markets to trade (can be auto-populated)
- **All Markets**: Database of all markets with metrics
- **Volatility Markets**: Filtered markets with volatility_sum for high-opportunity identification
- **Hyperparameters**: Trading parameters

This separation of configuration from code allows live parameter adjustment without redeployment.

## Important Considerations for Arbitrage

The poly-maker architecture reveals important details about cross-market arbitrage opportunities on Polymarket:

1. **Order Book Data**: WebSocket connections provide real-time order book depth, enabling detection of liquidity imbalances that create arbitrage windows

2. **Position Merging**: The ability to merge opposing YES/NO positions means arbitrageurs can efficiently close positions when mispricings resolve

3. **Maker Reward Calculation**: Understanding the maker reward formula S = ((v-s)/v)² helps identify markets where the reward for providing liquidity exceeds the risk

4. **Gas Optimization**: Since Polymarket runs on Polygon, gas fees are minimal but non-zero. The 30-second cooldown between trading actions in the bot design reflects the reality that excessive order cancellation destroys profitability

## Key Excerpts

1. "In today's market, this bot is not profitable and will lose money. Use it as a reference implementation for building your own market making strategies, not as a ready-to-deploy solution."

2. "The poly_merger module is a particularly powerful utility that handles position merging on Polymarket. Built on open-source Polymarket code, it provides a smooth way to consolidate positions, reducing gas fees and improving capital efficiency."

3. "Orders are placed at approximately 15% of max_spread distance for optimal reward/fill balance — maximizing maker rewards while maintaining fill probability."

## Scrape Notes
- **Content completeness:** full (GitHub README was fully accessible)
- **Note:** The author's explicit warning about current market conditions (not profitable due to competition) is significant for strategy design
