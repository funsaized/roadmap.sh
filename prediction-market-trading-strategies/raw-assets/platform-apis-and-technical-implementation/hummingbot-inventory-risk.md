# What is Inventory Risk?

## Metadata
- **URL:** https://hummingbot.org/blog/what-is-inventory-risk/
- **Source:** Hummingbot Blog
- **Type:** article
- **Author:** Hummingbot
- **Date Published:** Unknown
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** medium

## Content

## What is Inventory Risk?

Inventory risk is the probability a market maker can't find buyers for his inventory, resulting in the risk of holding more of an asset at exactly the wrong time — accumulating assets when prices are falling or selling too early when prices are rising.

Market makers provide liquidity by offering to buy and sell assets, earning the bid-ask spread. To do this, they must hold assets in inventory. When prices trend in one direction, buy orders get filled while sell orders don't, causing the market maker to accumulate the depreciating asset.

The main objective of a market maker is to increase inventory value over time by capturing incremental bid-ask spreads. The ideal situation is when price moves without a trend — within a range — so both buys and sells get filled with equal frequency.

## Inventory Value

Inventory value is the current value of all assets held in a portfolio, quantified to some chosen benchmark (e.g., USD). Inventory value fluctuates due to changes in market prices because the value of assets relative to the benchmark changes.

Example: If you own 0.468 BTC and 14.64 ETH:
- Day 1 at certain prices: Inventory = $10,000
- Day 2 after price changes: Inventory = $9,761.38

## The Problem: Directional Price Trends

When prices trend in one direction, the market maker accumulates inventory on the losing side. If BTC price trends down, buy orders keep getting filled but sell orders don't, causing the market maker to accumulate BTC at lower and lower prices. Eventually the market maker must decide between stopping operations or selling at a loss.

This is analogous to a retail store manager accumulating inventory that customers won't buy — the product sits on shelves, tying up capital that could be deployed elsewhere.

## Risk Management Strategies

### Inventory Skew

Using config inventory_skew_enabled, the bot changes order_amount on every new order to rebalance inventory size. The target proportion is defined via inventory_target_base_pct and how much it can deviate via inventory_range_multiplier.

If BTC price is trending up, the bot sells more than it buys, maintaining a target ratio. This acts as a pendulum — once you accumulate more of one asset, Hummingbot adjusts order sizes (smaller buys, larger sells) to return to target.

### Filled Order Delay

The filled_order_delay parameter sets a delay after a previous order is filled before creating new orders. This helps manage trending markets by spacing out fills and preventing rapid accumulation of one side.

Example: With delay=300 seconds, after a buy order fills, the bot waits 300 seconds before placing new orders. In a downward trend, this means the bot buys less frequently than if it placed orders every cycle.

### Hanging Orders

Hanging orders keeps the unfilled side of a paired order outstanding when one side fills. If a buy order fills, the corresponding sell order remains active rather than being cancelled. This allows the market maker to eventually complete the round trip and lock in the spread.

### Ping Pong Strategy

The ping pong strategy creates orders only on the opposite side of a filled order. If a buy fills, the bot only places sell orders until a sell also fills, then resumes two-sided order placement.

### Spread Adjustment

In trending markets, tightening the spread on one side increases fill probability. Example: bid_spread = 0.1, ask_spread = 0.9 with total spread still 1%. Buy offers now have higher chance of being filled first, helping rebalance inventory.

## Relevance to Prediction Markets

Inventory risk in prediction markets manifests differently than in traditional markets. Binary outcome tokens (YES/NO) mean inventory is always denominated in one outcome token. If the market trends toward one outcome, market makers accumulate YES tokens at lower prices as people sell. The key mitigation is similar: maintain balanced inventory, use position sizing rules, and adjust quotes based on current inventory exposure.

The zero-sum nature of prediction markets means inventory risk is somewhat more manageable — you're not holding volatile assets that can swing wildly in value, but rather binary claims that will resolve to $0 or $1.

## Key Excerpts

1. "Inventory risk is the probability a market maker can't find buyers for his inventory, resulting in the risk of holding more of an asset at exactly the wrong time."

2. "Inventory skew acts like an ongoing pendulum — once you accumulate more of one asset, Hummingbot adjusts order sizes (smaller buys, larger sells) to try to get back to the target ratio."

3. "Tightening the spread on one side increases fill probability on that side, allowing market makers to rebalance inventory during directional trends."

## Scrape Notes
- Content completeness: full
- Comprehensive explanation of market making inventory risk
- Applicable to prediction market market making where inventory skew management is critical
