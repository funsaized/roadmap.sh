# Poly-Maker: Polymarket Market Making Bot

## Metadata
- **URL:** https://github.com/warproxxx/poly-maker
- **Source:** GitHub
- **Type:** code/documentation
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Content

### Overview

An automated market making bot for Polymarket that provides liquidity by maintaining orders on both sides of the order book with customizable parameters configured via Google Sheets.

**Note**: In today's market, this bot is not profitable without significant optimization and competition awareness. Use as reference implementation for building your own market making strategies, not as a ready-to-deploy solution.

### Features

**Real-time Order Book Monitoring**
- WebSocket connections for live market data
- Dynamic order placement based on price movements
- Support for multiple simultaneous markets

**Position Management**
- Automatic position tracking
- Risk controls and size limits
- Support for position merging (consolidating YES/NO positions)

**Google Sheets Integration**
- Configuration via spreadsheet
- Real-time statistics and P&L tracking
- Market selection and parameter management

**Automated Position Merging**
- Reduces gas fees by combining opposing positions
- Built on open-source Polymarket code
- Improves capital efficiency

### Architecture

```
poly_data:    Core data management and market making logic
poly_merger:  Position merging functionality (Node.js)
poly_stats:   Account statistics tracking
poly_utils:   Shared utility functions
data_updater: Market information collection
```

### Risk Management

**Position Limits**
- Configurable maximum position size per market
- Total portfolio exposure limits
- Per-market stop-loss thresholds

**Inventory Controls**
- Monitors inventory balance (YES vs NO exposure)
- Automatic rebalancing when positions skew
- Prevents over-concentration in any outcome

**Order Sizing**
- Dynamic sizing based on market volatility
- Liquidity-aware order placement
- Spread management for capital efficiency

### Configuration

Key parameters via Google Sheets:
- `max_spread`: Maximum bid-ask spread
- `order_size`: Base order size per market
- `min_profitability`: Minimum expected return
- `max_markets`: Maximum concurrent markets to trade

### Important Disclaimer

"Given the increased competition on Polymarket, I don't see a point in playing with this unless you're willing to dedicate a significant amount of time."

Key requirements for profitability:
1. Sophisticated parameter optimization
2. Low-latency execution infrastructure
3. Advanced market selection
4. Proper risk management
5. Continuous monitoring and adjustment

## Key Excerpts

1. "In today's market, this bot is not profitable without significant optimization and competition awareness. Given the increased competition on Polymarket, I don't see a point in playing with this unless you're willing to dedicate a significant amount of time."

2. "Risk Management: Position Limits (max position size per market, total portfolio limits, per-market stop-loss), Inventory Controls (YES vs NO exposure balance, automatic rebalancing), Order Sizing (dynamic sizing based on volatility, liquidity-aware placement)."

3. "Automated Position Merging: Reduces gas fees by combining opposing positions. Built on open-source Polymarket code. Improves capital efficiency."

## Scrape Notes
- Full README extracted successfully
- Content includes overview, features, architecture, risk management, and configuration
- Content completeness: full
