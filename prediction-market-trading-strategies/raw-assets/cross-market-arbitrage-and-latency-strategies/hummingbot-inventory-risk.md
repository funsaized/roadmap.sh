# What is Inventory Risk?

## Metadata
- **URL:** https://hummingbot.org/blog/what-is-inventory-risk/
- **Source:** Hummingbot Blog
- **Type:** article
- **Author:** Hummingbot Community
- **Date Published:** Unknown
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** medium-high

## Content

This article from the Hummingbot Academy provides a comprehensive explanation of inventory risk in market making — the primary risk that market makers face. While Hummingbot is primarily focused on crypto exchange market making, the concepts directly apply to prediction market market making.

## What is Inventory Risk?

Inventory risk is the probability that a market maker cannot find buyers for their inventory, resulting in the risk of holding more of an asset at exactly the wrong time — accumulating assets when prices are falling or selling too early when prices are rising.

As a market maker, your role is to provide liquidity by offering to buy and sell assets. You earn the bid-ask spread, but you must hold inventory to fulfill your role. This inventory is subject to price fluctuations, creating risk.

## The Core Problem

The ideal situation for a market maker is when prices move within a range (sideways market). In this scenario, buy orders and sell orders are filled with roughly equal frequency, and the market maker accumulates small profits from the spread.

**The trouble begins when prices start to trend in one direction.**

Example: If prices trend downward:
- Buy orders start getting filled (traders sell to the market maker)
- Sell orders are not filled (traders won't buy at the offered price)
- The market maker accumulates the asset that is losing value
- Total inventory value decreases over time

Eventually, the market maker must either:
1. Stop operations and wait for better prices
2. Sell inventory at a loss to continue operations

This is analogous to a retail store that buys inventory from suppliers but can't find customers to buy it — the store is stuck holding goods that are declining in value.

## Inventory Risk Management Strategies

Hummingbot provides several built-in mechanisms to manage inventory risk:

### 1. Inventory Skew

When `inventory_skew_enabled` is true, the bot adjusts order amounts to rebalance inventory toward a target proportion.

- `inventory_target_base_pct`: Defines the target proportion of each asset in inventory
- `inventory_range_multiplier`: Controls how much inventory can deviate from the target

**Example:** If BTC price is trending up and you have more BTC than USDT, the bot will sell more than it buys, trying to return to the target ratio. This protects against accumulating a declining asset.

**Analogy:** Inventory skew is like an ongoing pendulum — as the inventory tilts toward one asset, the bot adjusts order sizes to try to restore balance.

### 2. Filled Order Delay

The `filled_order_delay` parameter introduces a pause between when one order is filled and when the next pair of orders is placed.

**Example:** With `filled_order_delay = 300` (5 minutes):
- Order gets filled
- Bot waits 300 seconds before placing new orders
- This spaces out orders during trending markets, preventing rapid accumulation of the trending asset

**Without delay:** In a downward trend, the bot might buy 5 times in 5 minutes, accumulating significant inventory of the falling asset.

**With delay:** The bot buys only once every 5 minutes, giving prices time to stabilize or reverse.

### 3. Hanging Orders

When hanging orders mode is enabled, if one side of a paired order is filled, the other side is kept outstanding (not cancelled) through subsequent refresh cycles.

**Benefit:** Creates the possibility of "completing" the round trip — if you bought low, keeping the sell order outstanding gives it time to be filled at the higher price.

**Tradeoff:** Can leave the bot exposed if prices move against the unfilled hanging order.

### 4. Ping Pong Mode

Ping pong mode only places orders on the opposite side of a filled order:
- Buy order filled → next orders are only sell orders
- Sell order filled → next orders are only buy orders

This naturally creates a paired trading pattern where the bot tries to complete round trips (buy low, sell high) rather than accumulating one-sided inventory.

### 5. Asymmetric Spreads

A more sophisticated strategy is to use different bid and ask spreads:
- Tighter spreads on one side → higher probability of that side being filled first
- Wider spreads on the other side → lower probability of being filled

**Example:** Price trending up:
- bid_spread = 0.1% (tight — buy orders get filled)
- ask_spread = 0.9% (wide — sell orders less likely to be filled)

Total spread is still 1%, but the bot preferentially accumulates the rising asset (selling it) rather than the falling asset.

## Inventory Value Tracking

The article provides a practical example of tracking inventory value:

**Day 1:** 0.468 BTC + 14.64 ETH, total value = $10,000
**Day 2:** Same holdings, but BTC up and ETH down, total value = $9,761.38

The inventory value decreased even though no trades were made — purely due to price movements. This is the core risk market makers face.

## Relevance to Prediction Market Market Making

These inventory risk concepts directly apply to prediction market market making:

1. **YES/NO Inventory Imbalance**: A market maker on Polymarket who accumulates YES tokens when a market trends toward NO is equivalent to accumulating a falling asset

2. **Kelly Fractional Sizing**: The filled order delay concept maps to position sizing limits — don't accumulate too much exposure before the market direction is confirmed

3. **Spread Adjustment**: In thin prediction markets, widening spreads as an event approaches is analogous to the asymmetric spread strategy for trending markets

4. **Hanging Orders**: Keeping limit orders outstanding when you have a position is like hanging orders — allows time for the market to move in your favor

## Key Excerpts

1. "Inventory risk is the probability a market maker can't find buyers for his inventory, resulting in the risk of holding more of an asset at exactly the wrong time, e.g. accumulating assets when prices are falling or selling too early when prices are rising."

2. "The ping pong strategy is another strategy that tries to keep buys and sells balanced. It does so by creating orders only on the opposite side of an order that has been filled."

3. "Understanding the risks associated with each type of trading operation is essential to finding a sustainable and profitable strategy."

## Scrape Notes
- **Content completeness:** full (article was fully accessible with excellent diagrams and examples)
- **Note:** Hummingbot is a well-established crypto market making platform; their academy content is high quality and practitioner-focused
