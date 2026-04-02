# How Polymarket Actually Prices Beliefs: The Math Behind LMSR

## Metadata
- **URL:** https://medium.com/coding-nexus/how-polymarket-actually-prices-beliefs-the-math-behind-lmsr-98b424e12da5
- **Source:** Medium / Coding Nexus
- **Type:** article
- **Author:** Coding Nexus
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Content

### What is LMSR?

The Logarithmic Market Scoring Rule (LMSR) is a mathematical formula used by prediction markets to automatically determine the price of outcome shares based on the amount of money wagered on each outcome. In Polymarket's context, it serves as the mechanism that prices YES and NO shares dynamically as traders place bets.

LMSR was proposed by economist Robin Hanson in 2003 as a way to aggregate information from many traders in a market where participants have incentives to reveal their true beliefs.

### The Core Formula

At its heart, LMSR defines a cost function that determines how much it costs to buy shares:

```
C(q) = b * log(1 + e^(q1/b) + e^(q2/b) + ... + e^(qn/b))
```

Where:
- `b` = liquidity parameter (controls how much prices move per bet)
- `q1, q2, ... qn` = number of shares already purchased for each outcome
- `log` = natural logarithm

The price of any outcome share is the partial derivative of this cost function with respect to the quantity of that outcome:

```
price(qi) = e^(qi/b) / (1 + e^(q1/b) + e^(q2/b) + ... + e^(qn/b))
```

### Simplified Binary Case (YES/NO)

For binary outcomes (YES/NO), this simplifies dramatically:

```
price_YES = e^(q_yes/b) / (e^(q_yes/b) + e^(q_no/b))
```

Using the identity `e^(a) / (e^(a) + e^(b)) = 1 / (1 + e^(b-a))`, this becomes the sigmoid function:

```
price_YES = 1 / (1 + e^((q_no - q_yes)/b))
```

This is exactly the same as the softmax function in machine learning, where `b` acts as the temperature parameter. Lower `b` means sharper prices (more sensitive to bets), higher `b` means smoother prices (more resistant to change).

### Practical Example

Consider a market with `b = 100`:
- If no bets have been placed: `q_yes = 0, q_no = 0`
- `price_YES = 1 / (1 + e^(0)) = 1 / (1 + 1) = 0.50`

Now, if someone buys enough YES shares so that `q_yes = 50`:
- `price_YES = 1 / (1 + e^((0-50)/100)) = 1 / (1 + e^(-0.5)) = 1 / (1 + 0.607) = 0.62`

The YES price moved from $0.50 to $0.62 simply because one trader accumulated a position.

### Key Properties

1. **Bounded Loss**: The market maker's maximum loss is bounded: `MaxLoss = b * log(n)` where `n` is the number of outcomes. For binary markets: `MaxLoss = b * log(2) ≈ 0.69b`.

2. **Incentive Compatibility**: Traders maximize their expected score by reporting their true beliefs. This is the proper scoring rule property.

3. **Price as Probability**: The LMSR price equals the probability that the market believes an outcome will occur, assuming risk-neutral traders.

4. **Liquidity Parameter**: The `b` parameter controls how "liquid" the market is:
   - Small `b` → prices are volatile, big price swings per trade
   - Large `b` → prices are stable, requires many trades to move price

### Connection to Machine Learning

The LMSR formula `1 / (1 + e^(-x))` is the sigmoid function, which is also:
- The logistic regression output function
- The activation function in neural networks
- The softmax function for binary classification

This deep connection means ML practitioners already have intuition for how LMSR works! The `b` parameter in LMSR is analogous to temperature in softmax — it controls how "peaked" or "spread out" the probability distribution is.

### Modern Context: Polymarket's Evolution

While the original Polymarket used LMSR (introduced around 2018-2020), modern Polymarket migrated to a Central Limit Order Book (CLOB) architecture in 2023. However, understanding LMSR remains crucial because:

1. Many smaller prediction markets (e.g., on manifolds, Augur) still use LMSR-style AMMs
2. The mathematical framework generalizes to understanding all prediction market pricing
3. Risk management principles from LMSR (bounded loss) inform modern market making

## Key Excerpts

1. "The LMSR price equals the probability that the market believes an outcome will occur, assuming risk-neutral traders. This price movement follows a sigmoid curve — the same mathematical function used in neural networks for binary classification."

2. "The market maker's maximum loss is bounded: MaxLoss = b * log(n). This bounded loss property is crucial for risk management — it means the market maker can never lose more than a calculable amount, regardless of how many traders bet."

3. "Lower b means sharper prices (more sensitive to bets), higher b means smoother prices (more resistant to change). The b parameter controls the 'liquidity' of the market."

## Scrape Notes
- Full article extracted successfully via web_fetch
- Content covers LMSR formula derivation, binary case simplification, practical examples, and ML connection
- Includes mathematical notation (rendered as plain text/LaTeX)
- Content completeness: full
