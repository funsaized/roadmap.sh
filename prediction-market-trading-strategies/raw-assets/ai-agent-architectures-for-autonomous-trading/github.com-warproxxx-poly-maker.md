# Poly-Maker: Automated Market Making Bot for Polymarket (Warproxxx Fork)

## Metadata
- **URL:** https://github.com/warproxxx/poly-maker
- **Source:** github.com/warproxxx/poly-maker
- **Type:** code/documentation
- **Author:** warproxxx
- **Date Published:** 2024-2025
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Content

## Overview

An automated market making bot for Polymarket that provides liquidity by maintaining orders on both sides of the order book with customizable parameters configured via Google Sheets.

**WARNING**: In today's market, this bot is not profitable and will lose money. Use it as a reference implementation for building your own market making strategies, not as a ready-to-deploy solution. Given the increased competition on Polymarket, unless you're willing to dedicate significant time, it's not worth playing with.

## Key Features

### Real-time Order Book Monitoring
- WebSocket connections for live market data

### Position Management
- Risk controls built into the trading logic
- Customizable trade parameters via Google Sheets

### Automated Position Merging
- Consolidates opposing YES/NO positions
- Reduces gas fees
- Improves capital efficiency
- Built on open-source Polymarket code

### Sophisticated Spread and Price Management
- Configurable bid/ask spreads
- Price-based order sizing
- Dynamic parameter adjustment via Google Sheets

## Architecture

Repository modules:
- `poly_data`: Core data management and market making logic
- `poly_merger`: Position merging utility
- `poly_stats`: Account statistics tracking
- `poly_utils`: Shared utility functions
- `data_updater`: Market information collection

## Installation

Uses UV for fast package management:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv

# Install all dependencies
uv sync

# Install with dev dependencies
uv sync --extra dev

# Run the market maker
uv run python main.py

# Update market data
uv run python update_markets.py

# Update statistics
uv run python update_stats.py
```

## Configuration

Google Spreadsheet worksheets:
- **Selected Markets**: Markets you want to trade
- **All Markets**: Database of all Polymarket markets
- **Hyperparameters**: Configuration parameters (default parameters that worked well in November are included)

## Key Excerpts

1. "WARNING: In today's market, this bot is not profitable and will lose money. Use it as a reference implementation for building your own market making strategies, not as a ready-to-deploy solution."

2. "The poly_merger module is a particularly powerful utility that handles position merging on Polymarket. It's built on open-source Polymarket code and provides a smooth way to consolidate positions, reducing gas fees and improving capital efficiency."

## Scrape Notes
- Content completeness: full
- Note: this fork explicitly warns about lack of profitability in current competitive market
- Reference implementation for market making architecture
- MIT licensed
