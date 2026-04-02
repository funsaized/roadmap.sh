# LMSR: Logarithmic Market Scoring Rule

## Metadata
- **URL:** https://blog.gensyn.ai/lmsr-logarithmic-market-scoring-rule/
- **Source:** Gensyn.ai Blog
- **Type:** article
- **Author:** Gensyn.ai
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** high

## Content

# LMSR: Logarithmic Market Scoring Rule

## What is the Logarithmic Market Scoring Rule?

The Logarithmic Market Scoring Rule (LMSR) is a market maker mechanism for prediction markets introduced by Robin Hanson. It allows markets to be created for any topic without requiring a human market maker to set initial prices. Instead, liquidity providers fund the market, and traders move prices by buying shares.

## The Core Mechanism

LMSR works by maintaining a "liquidity parameter" b (also called the budget or liquidity parameter) and tracking the number of shares outstanding for each outcome. The cost of buying shares follows a logarithmic cost function.

### Cost Function

When you buy δ shares of outcome i in a market with current share vector (b1, b2, ..., bn) for n outcomes, the cost is:

```
cost = b × ln(e^(b1/b) + e^(b2/b) + ... + e^(bn/b) + e^δ/b) - b × ln(e^(b1/b) + ... + e^(bn/b))
```

This simplifies to:

```
cost = b × ln(sum(e^(bj/b)) after purchase) - b × ln(sum(e^(bj/b)) before purchase)
```

### Price Calculation

The current price (probability estimate) for outcome i is:

```
price_i = e^(bi/b) / sum(e^(bj/b) for all j)
```

This gives a probability distribution across all outcomes that always sums to 1.0.

## Binary Markets

For binary (YES/NO) markets, the formula simplifies considerably:

```
price_YES = e^(n_yes/b) / (e^(n_yes/b) + e^(n_no/b))
```

Where n_yes and n_no are the current numbers of YES and NO shares outstanding.

This can be rewritten as:

```
price_YES = 1 / (1 + e^((n_no - n_yes)/b))
```

This is equivalent to a sigmoid function centered at n_yes = n_no.

## The Liquidity Parameter b

The liquidity parameter b controls how much the price moves per share purchased:

- **High b:** Prices move slowly (more liquidity, more shallow slope)
- **Low b:** Prices move quickly (less liquidity, steeper slope)

The total money in the market equals b plus the net position of traders. When a trader buys shares worth $X, the market maker's inventory increases by $X. The market maker earns when prices move against traders.

## Net Market Maker Profit

The market maker's net profit equals the total money paid by traders minus the total winnings paid out:

```
MM_profit = sum(all trader payments) - sum(all trader winnings)
```

Since the total money collected is fixed at b + trader payments, and winnings are determined by resolution outcomes, the market maker's expected profit depends on how well the market price predicts actual outcomes.

## Revenue Max vs. Accuracy Max

Robin Hanson identified an important trade-off:

1. **Revenue-maximizing market maker:** Sets b to maximize market maker revenue. This tends to create "favorite-longshot" biases where traders overpay for low-probability outcomes.

2. **Accuracy-maximizing market maker:** Sets b to maximize price accuracy. This typically requires lower b values, which reduce revenue but improve price discovery.

The standard LMSR as originally proposed is accuracy-maximizing. Revenue-maximizing variants use dynamic b adjustments.

## Arbitrage and Price Discovery

LMSR markets maintain the invariant that the total cost to buy all outcomes = b. This means:

- Buying all outcomes costs exactly b
- This creates arbitrage opportunities when market prices sum to less than $1.00

## Practical Implementation Notes

- The market maker never loses money in aggregate (assuming infinite liquidity)
- Prices are always between 0 and 1
- The cost function is convex, making it computationally efficient
- LMSR is a "budget-balanced" mechanism: money flows from traders to market maker, not vice versa

## Key Excerpts

1. "The LMSR cost function uses b × ln(sum(e^(bj/b))) to determine prices, giving a softmax probability distribution"
2. "The liquidity parameter b controls price sensitivity: higher b means prices move less per trade"
3. "For binary markets, price_YES = 1 / (1 + e^((n_no - n_yes)/b)) — a sigmoid function centered at equilibrium"
4. "The accuracy-maximizing market maker sets b lower than the revenue-maximizing variant"
