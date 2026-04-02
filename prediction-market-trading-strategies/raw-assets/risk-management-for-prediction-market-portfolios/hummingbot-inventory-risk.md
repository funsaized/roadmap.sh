# What is Inventory Risk?

## Metadata
- **URL:** https://hummingbot.org/blog/what-is-inventory-risk/
- **Source:** Hummingbot Blog
- **Type:** article
- **Author:** Hummingbot Academy
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Content

### What is Inventory Risk?

As a market maker, your main role is to provide liquidity to other market participants. You are providing a service to other traders, offering to buy and sell assets from and to everyone else, while getting paid to do so through the spread size between your bid and ask offers.

To be able to provide this service, the market maker must hold some amount of assets in inventory in order to create orders and make trades, and this inventory has a value associated with it.

**Inventory Value** is the current value of all assets held in a portfolio, quantified to some chosen benchmark or reference asset (e.g. USD).

### The Core Problem

The main objective of a market maker is to increase his total inventory value over time by capturing incremental bid-ask spreads.

The ideal situation for a market maker is when the price is moving without a trend (sideways market). When prices are trading within a range, the market maker's buys and sells are filled with equal frequency, accumulating incremental profits.

**The trouble begins when prices start to trend in one direction.**

Example: If the price starts to trend downward, buy orders start being filled, but not sell orders. The consequence is that the market maker accumulates inventory of the asset that is losing value, resulting in total inventory value decreasing over time.

### Inventory Risk Definition

**Inventory risk** is the probability a market maker can't find buyers for his inventory, resulting in the risk of holding more of an asset at exactly the wrong time, e.g., accumulating assets when prices are falling or selling too early when prices are rising.

Key aspects:
- Asymmetric exposure: You might accumulate assets losing value OR sell off assets that are appreciating
- Trend vulnerability: Directional price movements expose inventory imbalances
- Opportunity cost: Locked capital can't be deployed elsewhere

### Risk Mitigation Strategies

**1. Inventory Skew**

Using `inventory_skew_enabled`, the bot changes order_amount on every new order to rebalance total inventory size. The target proportion of each asset can be defined, and the bot adjusts order sizes (smaller buys, larger sells) to maintain the target ratio.

"This parameter can be used as inventory protection. If you spot a trend forming in one direction, you could start accumulating more of the appreciating asset."

**2. Filled Order Delay**

Through the `filled_order_delay` parameter, the market maker sets a delay time for the bot to create subsequent new orders once a previous order has been filled.

Example: With `filled_order_delay = 300`, when an order is filled, the next pair of orders only be created 300 seconds later.

This helps manage periods when prices are trending. By introducing a delay between filled orders, this spaces out orders and dampens the potential accumulation of assets, allowing time for price trends to stabilize.

**3. Hanging Orders**

Hanging orders is a function that treats buys and corresponding sell orders created at the same time as a pairing. If one side gets filled, the bot keeps the other side outstanding, creating the opportunity for that side to eventually get filled.

Benefit: Creates the possibility of the pairings to be "completed" and balanced, while locking in the bid-ask spread.

**4. Ping Pong Strategy**

The ping pong strategy creates orders only on the opposite side of an order that has been filled. If a buy order was filled, the bot stops placing buy orders and only places sell orders. Only when a sell order is eventually filled will the bot resume creating both buy and sell orders.

**5. Adjust Spread on One Side**

Usually, market makers apply the same bid_spread and ask_spread. But during a trending market, inventory may start to accumulate on the side of the less valuable asset.

Mitigation: Tighten the spread on one side to increase the probability of those orders being filled first.

Example: If BTC price is trending up, change from `bid_spread = 0.5, ask_spread = 0.5` to `bid_spread = 0.1, ask_spread = 0.9`. Total spread is still 1%, but buy offers now have a higher chance of being filled.

### Mathematical Framework

The Avellaneda-Stoikov model provides a framework for market making with inventory risk:

```
Reservation price: r(s,t) = s - q * γ * σ² * (T-t)
```

Where:
- s = mid-price
- q = current inventory
- γ = risk aversion parameter
- σ = volatility
- T = time to end of trading period
- t = current time

This shows that the reservation price (fair price you should quote) depends on:
- Current inventory (more inventory → lower reservation price for buys)
- Risk aversion (higher γ → more conservative pricing)
- Time remaining (as T-t decreases, inventory risk increases)

### Connection to Prediction Markets

In prediction market market making, inventory risk has unique characteristics:
- Binary outcomes (only $0 or $1 at resolution)
- "Event cliffs" where price can gap from any level to 0 or 1 instantaneously
- Time decay as event approaches increases jump risk

For prediction markets, the inventory risk is more extreme than traditional assets because the final settlement is always binary — you can't "wait out" a bad position like you might with equities.

## Key Excerpts

1. "Inventory risk is the probability a market maker can't find buyers for his inventory, resulting in the risk of holding more of an asset at exactly the wrong time, e.g., accumulating assets when prices are falling or selling too early when prices are rising."

2. "The Avellaneda-Stoikov model: Reservation price r(s,t) = s - q * γ * σ² * (T-t). As T-t decreases (event approaches), inventory risk increases and spreads should widen accordingly."

3. "For prediction markets, the inventory risk is more extreme than traditional assets because the final settlement is always binary — you can't 'wait out' a bad position like you might with equities."

## Scrape Notes
- Full article extracted successfully
- Content covers inventory risk definition, problem analysis, mitigation strategies (inventory skew, filled order delay, hanging orders, ping pong, spread adjustment), and mathematical framework
- Content completeness: full
