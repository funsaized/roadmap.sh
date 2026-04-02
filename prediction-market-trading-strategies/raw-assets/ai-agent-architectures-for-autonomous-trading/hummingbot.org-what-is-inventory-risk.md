# What is Inventory Risk?

## Metadata
- **URL:** https://hummingbot.org/blog/what-is-inventory-risk/
- **Source:** hummingbot.org
- **Type:** article
- **Author:** Hummingbot
- **Date Published:** Unknown
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** medium

## Content

## Introduction

Inventory risk is the most important factor in all types of market making operations. As Warren Buffett said: "Risk comes from not knowing what you're doing."

A market maker's main role is providing liquidity to other market participants. You offer to buy and sell assets, getting paid through the spread between bid and ask offers. To do this, you must hold assets in inventory, and this inventory has a value that fluctuates with market prices.

## Inventory Value

Inventory value is the current value of all assets held in a portfolio, quantified in a benchmark currency (e.g., USD). Inventory value fluctuates because asset prices relative to the benchmark change constantly.

Example: Day 1 portfolio of 0.46820424 BTC + 14.6426 ETH = $10,000 USD value. Day 2 same assets = $9,761.38 due to price changes. Same assets, different value.

## The Market Maker's Goal

A market maker tries to increase portfolio value over time by capturing incremental bid-ask spreads. You simultaneously offer to buy at a slightly lower price and sell at a slightly higher price. If both sides fill, you capture the spread difference.

The ideal situation is when price moves within a range (no trend) — buy and sell orders fill with equal frequency, accumulating incremental profits.

## Inventory Risk

The trouble begins when prices start trending in one direction.

If price trends downward, buy orders start filling but sell orders don't. The market maker accumulates the asset that's losing value, and total inventory value decreases over time.

If this persists and price keeps dropping, the market maker's inventory locks entirely into the losing side. At some point, they must choose between stopping operations or selling at a loss.

**Inventory risk is the probability a market maker can't find buyers for their inventory, resulting in the risk of holding more of an asset at exactly the wrong time — accumulating assets when prices are falling or selling too early when prices are rising.**

## Risk Mitigation Strategies

### Inventory Skew

Using `inventory_skew_enabled`, the bot changes order_amount on every new order to rebalance inventory. The target proportion of each asset can be defined via `inventory_target_base_pct` and how much it can deviate via `inventory_range_multiplier`.

If BTC price is trending up, the bot sells more than it buys to reduce BTC accumulation. Inventory skew is like a pendulum — when one asset accumulates, the bot adjusts order sizes (smaller buys, larger sells) to return to the target ratio.

### Filled Order Delay

Through `filled_order_delay`, the bot waits before creating new orders after a previous order filled. For example, `filled_order_delay = 300` means 300 seconds between order cycles after a fill.

This spaces out orders and dampens potential asset accumulation, allowing time for price trends to stabilize. Without this delay, if a downward trend causes fills every refresh cycle, the bot could accumulate the losing asset in just a few cycles. With delay, it buys fewer times during the same trend.

### Hanging Orders

When one side of a paired order fills, the bot keeps the other side outstanding instead of canceling it. This creates the possibility for the pair to complete later.

Example: Buy order fills in period 1. Sell order from period 1 remains outstanding through periods 2-5. When price eventually reverses and sell fills in period 5, the spread is captured. Hanging orders allow completing buy+sell pairings while locking in the bid-ask spread.

### Ping Pong

Ping pong only places orders on the opposite side of a filled order. Buy fills → only place sell orders until a sell fills. Sell fills → only place buy orders. This keeps buys and sells balanced automatically.

### Adjusting Spread on One Side

During trending markets, instead of equal bid/ask spreads, tighten spread on the side moving against you (making those orders fill first) and widen spread on the side moving with you (reducing likelihood of fills on the wrong side).

Example: BTC-USDT with equal spreads (bid=0.5%, ask=0.5%). Price starts trending up. Change to bid=0.1%, ask=0.9%. Total spread still 1%, but buy offers have higher fill probability, rebalancing inventory faster.

### Custom Scripts

Hummingbot supports Python scripts that adjust parameters based on custom logic. Traders can implement any market making strategy and integrate with the bot framework.

## Key Insights

The major risk in market making is inventory risk. Understanding and managing it is essential for sustainable operation.

For prediction markets specifically, inventory risk is heightened because:
- Binary outcome tokens go to $0 or $1 at resolution
- You can't "HODL" through resolution — one side becomes worthless
- The jump risk near resolution is extreme (no gradual exit)
- Dynamic PM-AMM addresses this by reducing liquidity as expiration approaches

## Key Excerpts

1. "Inventory risk is the probability a market maker can't find buyers for their inventory, resulting in the risk of holding more of an asset at exactly the wrong time, e.g. accumulating assets when prices are falling or selling too early when prices are rising."

2. "Inventory skew is like an ongoing pendulum balancing act; once a trader accumulates more of one asset, Hummingbot adjusts order sizes (smaller buys, larger sells) to try to get back to the target holding amount, and vice versa. This minimizes the risk of inventory amounts swinging around too much."

3. "Understanding the risks associated with each type of trading operation is essential to finding a sustainable and profitable strategy. The major risk associated with market making is the inventory risk. Understanding and learning ways to mitigate it should be a priority."

## Scrape Notes
- Content completeness: full
- Hummingbot's educational content on market making risk
- Covers 5 inventory risk mitigation strategies with parameter examples
- Relevant for prediction market MM bot design
