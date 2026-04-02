# LMSR: Logarithmic Market Scoring Rule

## Metadata
- **URL:** https://blog.gensyn.ai/lmsr-logarithmic-market-scoring-rule/
- **Source:** Gensyn AI Blog
- **Type:** article
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Content

### Introduction

The Logarithmic Market Scoring Rule (LMSR) is a mechanism for building prediction markets. It was introduced by Robin Hanson in 2003 as a way to aggregate information efficiently. The key innovation of LMSR is that it provides a way to convert opinions into probabilities through a market mechanism, while guaranteeing that the market maker (the entity running the market) never loses more than a bounded amount.

### The Problem LMSR Solves

Traditional prediction markets require finding a counterparty for every trade. If you believe "Team A will win" but no one wants to bet against Team A, you can't place your bet. LMSR solves this by having the market itself act as a continuous counterparty — you can always buy YES or NO shares at a price determined by the current state of the market.

### The Mathematical Framework

**Cost Function**: In LMSR, the cost to buy a set of shares is determined by:

```
C(q) = b * log(1 + e^(q1/b) + e^(q2/b) + ... + e^(qn/b))
```

Where `q = (q1, q2, ..., qn)` represents the current holdings (shares outstanding) for each of n possible outcomes, and `b` is the liquidity parameter.

**Price Calculation**: The price of outcome i is the marginal cost of buying one more share of that outcome:

```
price_i = e^(qi/b) / (1 + e^(q1/b) + e^(q2/b) + ... + e^(qn/b))
```

This is the softmax function — the same function used in machine learning to convert logits to probabilities.

### Binary Case (Two Outcomes)

For binary markets with YES and NO outcomes:

```
price_YES = e^(q_yes/b) / (e^(q_yes/b) + e^(q_no/b))
```

This can be rewritten as:

```
price_YES = 1 / (1 + e^((q_no - q_yes)/b))
```

This is the logistic sigmoid function. When `q_yes = q_no` (equal amounts wagered on both sides), the price is exactly $0.50.

### Bounded Loss Property

The most important property of LMSR for risk management is that the market maker's loss is bounded:

```
Market Maker Loss ≤ b * ln(n)
```

Where `n` is the number of outcomes and `ln` is the natural logarithm.

For a binary market (n=2): Maximum loss ≤ b * ln(2) ≈ 0.693b

If b = $1000, the market maker can never lose more than $693 regardless of how the market moves. This bounded loss property makes LMSR attractive for market operators.

### Relationship to Scoring Rules

A scoring rule is a function that rewards accurate predictions. LMSR is based on the logarithmic scoring rule:

```
Score = log(p_i)  if outcome i occurs
```

Where `p_i` is the probability you assigned to outcome i. The expected score is maximized when you report your true beliefs — this is why LMSR gives traders incentive to be honest.

### Liquidity Parameter (b)

The `b` parameter controls market "liquidity":
- **Low b** (e.g., b=50): Prices are very sensitive to new bets. A small wager can move prices significantly. Creates volatile markets.
- **High b** (e.g., b=1000): Prices are stable. Requires large wagers to move prices. Creates deep, resilient markets.

Choosing b involves a tradeoff: low b means more price discovery but higher market maker risk; high b means lower risk but less responsive pricing.

### Proper Scoring Rule Property

LMSR implements a "proper scoring rule" — meaning that for any trader, the optimal strategy is to report their true beliefs. If you truly believe an outcome has 70% probability, the best action is to buy shares at the 70% price. There's no advantage to misrepresenting your beliefs.

This property makes LMSR markets informationally efficient: the prices that emerge reflect the collective true beliefs of all traders.

### Limitations and Extensions

1. **Bounded Loss is Bounded by Initial State**: The bounded loss guarantee assumes the market starts at zero shares. Once shares have been sold, the remaining exposure is bounded by the current cost function.

2. **Doesn't Handle Conditional Markets Well**: LMSR prices marginal probabilities. For conditional markets (e.g., "If X happens, will Y happen?"), special handling is needed to ensure consistency.

3. **Not Uniform in LVR**: As the Paradigm pm-AMM paper shows, LMSR doesn't provide uniform Loss-Versus-Rebalancing across all price points — it's more costly for LPs at extreme probabilities.

4. **Modern Alternatives**: CLOB (Central Limit Order Book) systems like current Polymarket offer better price discovery, though at the cost of the bounded-loss guarantee.

## Key Excerpts

1. "LMSR solves this by having the market itself act as a continuous counterparty — you can always buy YES or NO shares at a price determined by the current state of the market. The most important property of LMSR for risk management is that the market maker's loss is bounded."

2. "The price of outcome i is the marginal cost of buying one more share of that outcome: price_i = e^(qi/b) / (1 + e^(q1/b) + e^(q2/b) + ... + e^(qn/b)). This is the softmax function — the same function used in machine learning to convert logits to probabilities."

3. "Choosing b involves a tradeoff: low b means more price discovery but higher market maker risk; high b means lower risk but less responsive pricing."

## Scrape Notes
- Full article extracted successfully
- Content covers LMSR mathematical foundation, cost function, price calculation, bounded loss, proper scoring rules, and limitations
- Content completeness: full
