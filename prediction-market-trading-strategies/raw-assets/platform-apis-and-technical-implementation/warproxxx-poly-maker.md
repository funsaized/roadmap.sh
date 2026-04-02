# Poly-Maker: Automated Market Making Bot for Polymarket

## Metadata
- **URL:** https://github.com/warproxxx/poly-maker
- **Source:** GitHub
- **Type:** code
- **Author:** warproxxx
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Content

## Overview

An automated market making bot for Polymarket that provides liquidity by maintaining orders on both sides of the order book with customizable parameters configured via Google Sheets.

**Important Warning**: In today's market, this bot is not profitable as-is and will lose money. Use it as a reference implementation for building your own market making strategies, not as a ready-to-deploy solution. Given increased competition, significant time investment is needed to make it profitable.

## Architecture

Modules:
- **poly_data**: Core data management and market making logic
- **poly_merger**: Utility for merging positions (based on open-source Polymarket code)
- **poly_stats**: Account statistics tracking
- **poly_utils**: Shared utility functions
- **data_updater**: Separate module for collecting market information

## Requirements

- Python 3.9.10+
- Node.js (for poly_merger)
- Google Sheets API credentials
- Polymarket account and API credentials

## Setup

Uses UV for package management:
```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Run market maker
uv run python main.py

# Update market data
uv run python update_markets.py
```

Environment variables in .env:
- **PK**: Your private key for Polymarket
- **BROWSER_ADDRESS**: Your wallet address

Note: Ensure your wallet has done at least one trade through the UI so permissions are proper.

## Google Sheets Configuration

1. Create a Google Service Account and download credentials to the main directory
2. Copy the sample Google Sheet template
3. Add your service account to the sheet with edit permissions
4. Update SPREADSHEET_URL in .env

Worksheets:
- **Selected Markets**: Markets to trade
- **All Markets**: Database of all markets on Polymarket
- **Hyperparameters**: Trading parameters

## Key Excerpts

1. "In today's market, this bot is not profitable and will lose money. Use it as a reference implementation for building your own market making strategies."

2. "Given increased competition on Polymarket, I don't see a point in playing with this unless you're willing to dedicate a significant amount of time."

## Scrape Notes
- Content completeness: full
- Note: Author explicitly states the strategy is not profitable in current competitive environment
- Useful as architecture reference for building custom Polymarket market making bots
