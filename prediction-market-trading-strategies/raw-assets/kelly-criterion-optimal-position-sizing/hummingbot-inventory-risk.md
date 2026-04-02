# What is Inventory Risk?

## Metadata
- **URL:** https://hummingbot.org/blog/what-is-inventory-risk/
- **Source:** Hummingbot
- **Type:** article
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** medium

## Content

# What is Inventory Risk?

## What is Inventory Value?

Inventory value is the current value of all assets held in a portfolio, quantified to some chosen benchmark or reference asset (e.g. USD).

As any market participant knows, asset prices are constantly changing. Inventory value fluctuates due to changes in market prices because the value of the assets relative to the benchmark asset can change.

Example: If you own 0.46820424 BTC and 14.6426 ETH:
- Day 1: Total value = $10,000
- Day 2: Same amounts, but BTC price up, ETH price down → Total value = $9,761.38

## Inventory Risk in Trading

The main objective of a market maker is to increase total inventory value over time. A market maker tries to capture incremental bid-ask spreads by continually offering to buy and sell assets, being at a slightly lower price than where they offer to sell.

The ideal situation for a market maker is when the price is moving without a trend. When prices trade within a range, buy and sell orders are filled with equal frequency, and the market maker accumulates incremental profits.

**The trouble begins when prices start to trend in one direction.**

When price trends downward, buy orders get filled but not sell orders. The market maker accumulates inventory of the asset losing value, resulting in total inventory value decreasing over time.

Eventually, the market maker must decide between stopping operation and waiting for better prices, or selling inventory at a loss.

## Inventory Risk Definition

Inventory risk is the probability a market maker can't find buyers for their inventory, resulting in the risk of holding more of an asset at exactly the wrong time — accumulating assets when prices are falling, or selling too early when prices are rising.

## Inventory Risk Management Strategies

### 1. Inventory Skew

Using config inventory_skew_enabled, the bot changes the order_amount on every new order to rebalance total inventory size. The target proportion of each asset can be defined through inventory_target_base_pct.

This is like an ongoing pendulum balancing act: once a trader accumulates more of one asset, Hummingbot adjusts order sizes (smaller buys, larger sells) to try to get back to the target holding amount.

### 2. Filled Order Delay

Through the filled_order_delay parameter, the market maker sets a delay time for the bot to create subsequent orders once a previous order has been filled. This spaces out orders and dampens the potential accumulation of assets during price trends.

### 3. Hanging Orders

Hanging orders mode keeps the unfilled side of a paired order outstanding even after the refresh cycle, creating the possibility for that side to eventually get filled. This allows traders to match buy and sell eventually while locking in the bid-ask spread.

### 4. Ping Pong Strategy

Ping pong creates orders only on the opposite side of a filled order. If a buy order is filled, the bot stops placing buy orders and only places sell orders until a sell is filled.

### 5. Spread Adjustment

Tighten the spread on one side to increase the probability of those orders being filled first. For example, if price is trending up, reduce bid_spread to 0.1 and increase ask_spread to 0.9 — total spread is the same but buy orders have higher fill probability.

## Key Excerpts

1. "Inventory risk is the probability a market maker can't find buyers for their inventory, holding more of an asset at exactly the wrong time — accumulating when prices fall or selling too early when prices rise"
2. "Inventory skew acts as a pendulum: when you accumulate too much of one asset, the bot adjusts order sizes to rebalance toward the target holding amount"
3. "Filled order delay spaces out orders during trending markets, dampening the potential accumulation of the losing asset"
