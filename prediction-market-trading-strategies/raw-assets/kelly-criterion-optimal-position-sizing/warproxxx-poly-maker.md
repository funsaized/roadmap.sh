# Poly-Maker: Polymarket Automated Market Making Bot

## Metadata
- **URL:** https://github.com/warproxxx/poly-maker
- **Source:** GitHub / warproxxx
- **Type:** code/repository
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** medium

## Content

# Poly-Maker: Polymarket Automated Market Making Bot

## Warning

In today's market, this bot is not profitable and will lose money. Use it as a reference implementation for building your own market making strategies, not as a ready-to-deploy solution. Given the increased competition on Polymarket, significant time dedication is required to be profitable.

## Overview

An automated market making bot for Polymarket that provides liquidity by maintaining orders on both sides of the order book with customizable parameters configured via Google Sheets.

## Key Features

- **Real-time order book monitoring via WebSockets**
- **Position management with risk controls**
- **Customizable trade parameters** fetched from Google Sheets
- **Automated position merging** functionality
- **Sophisticated spread and price management**

## Modules

- poly_data: Core data management and market making logic
- poly_merger: Utility for merging positions (based on open-source Polymarket code)
- poly_stats: Account statistics tracking
- poly_utils: Shared utility functions
- data_updater: Separate module for collecting market information

## Position Merging

The poly_merger module handles position merging on Polymarket. Built on open-source Polymarket code, it provides a smooth way to consolidate positions, reducing gas fees and improving capital efficiency.

## Risk Warning

- This code interacts with real markets and can potentially lose real money
- Test thoroughly with small amounts before deploying with significant capital
- The data_updater should ideally run on a different IP than the trading bot

## Key Excerpts

1. "Position merging utility reduces gas fees and improves capital efficiency by consolidating opposing YES/NO positions"
2. "WebSocket-based real-time order book monitoring enables responsive market making with configurable parameters via Google Sheets"
