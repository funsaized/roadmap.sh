# Kelly Criterion — Polymarket Bot Implementation

## Metadata
- **URL:** https://www.mintlify.com/joicodev/polymarket-bot/risk/kelly-criterion
- **Source:** Mintlify / joicodev
- **Type:** documentation
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Content

# Kelly Criterion — Polymarket Bot Implementation

## Overview

The Kelly criterion is a mathematical formula for optimal bet sizing in scenarios with known edge. It maximizes long-term logarithmic growth of capital while minimizing risk of ruin. The Polymarket Bot implements a fractional Kelly strategy to reduce variance and account for model uncertainty.

## Mathematical Foundation

### Full Kelly Formula

For a binary outcome (win/lose) with:
- p = probability of winning
- q = probability of losing = 1 - p
- b = net odds received on a win (profit / wager)

The optimal fraction of bankroll to wager is:

```
f* = (p × b - q) / b
```

### Simplified Form for Prediction Markets

Polymarket markets use decimal odds where:
- You pay q per share
- Winning shares pay $1.00
- Net profit per share = 1 - q

This gives b = (1 - q) / q, and substituting into the Kelly formula:

```
f* = (p - q) / (1 - q)
```

This is the core formula used in the PositionSizer implementation.

Note: The formula f* = (p - q) / (1 - q) assumes you're betting on the outcome priced at q. For NO bets (betting against the outcome), both p and q are inverted to 1 - p and 1 - q respectively.

## Why Fractional Kelly?

Full Kelly (using f* directly) maximizes long-term growth rate but has significant drawbacks:

1. **High variance**: Full Kelly can recommend very large bets (up to 100% of bankroll)
2. **Model error sensitivity**: Small errors in p estimation lead to substantial overbet
3. **Drawdown magnitude**: Aggressive sizing causes deeper and longer drawdowns

Fractional Kelly (α × f* where α < 1) trades some growth rate for:
- Lower variance
- Reduced sensitivity to model error
- Shallower drawdowns
- More psychologically tolerable equity curves

### Growth Rate Comparison

For α = 0.5 (half Kelly), the growth rate is approximately 75% of full Kelly, but the variance is only 25% of full Kelly. This is a favorable tradeoff for most scenarios.

The Polymarket Bot uses α values ranging from 0.10 to 0.40 depending on model accuracy (Brier score). Even at maximum aggression, the system never exceeds 40% of full Kelly.

## Implementation Details

### Side Determination

The bot determines which side of the market to bet based on the model's prediction:

```javascript
const side = p >= 0.5 ? 'YES' : 'NO'
```

- If p ≥ 0.5: Bet YES (the outcome will occur)
- If p < 0.5: Bet NO (the outcome will not occur)

### Probability Inversion for NO Bets

When betting NO, the effective probabilities are inverted:

```javascript
const pEff = side === 'YES' ? p : 1 - p
const qEff = side === 'YES' ? q : 1 - q
```

This ensures the Kelly formula is applied correctly from the perspective of the bet being placed.

### Edge Calculation

The Kelly fraction is only positive when an edge exists:

```
f* = (pEff - qEff) / (1 - qEff)
```

If f* ≤ 0, there is no edge, and the system returns a zero bet:

```javascript
if (fullKelly <= 0) {
  return { bet: 0, fullKelly, alpha: 0, fractionalKelly: 0, capped: false, side }
}
```

Negative Kelly fractions (pEff < qEff) indicate the market price is better than your model's estimate. The system correctly avoids betting in this scenario, as there is no perceived edge.

## Fractional Alpha Selection

The bot uses a **Brier-tiered alpha system** that maps model accuracy to fractional Kelly values:

| Brier Score | Alpha | Kelly Fraction |
|-------------|-------|----------------|
| < 0.18 (excellent) | 0.40 | 40% of full Kelly |
| 0.18 - 0.22 (good) | 0.25 | 25% of full Kelly |
| 0.22 - 0.26 (moderate) | 0.20 | 20% of full Kelly |
| > 0.26 (low accuracy) | 0.10 | 10% of full Kelly |
| < 100 predictions | 0.00 | No trading |

Lower Brier scores indicate better calibration and accuracy. The system uses higher alpha values when the model has proven accuracy, and conservative values when accuracy is unproven or degraded.

## Example Calculations

### Example 1: YES Bet with Edge

Given:
- Model prediction: p = 0.65
- Market price: q = 0.52
- Bankroll: $10,000
- Brier score: 0.20 → α = 0.25 (Tier 3)

Calculation:

```
Side: YES (p ≥ 0.5)
pEff: 0.65
qEff: 0.52
f*: (0.65 - 0.52) / (1 - 0.52) = 0.13 / 0.48 = 0.2708
α: 0.25
f_real: 0.25 × 0.2708 = 0.0677
Bet: 0.0677 × $10,000 = $677
```

Result: Bet $677 on YES (6.77% of bankroll)

### Example 2: NO Bet with Edge

Given:
- Model prediction: p = 0.30 (70% chance outcome does NOT occur)
- Market price: q = 0.45
- Bankroll: $10,000
- Brier score: 0.19 → α = 0.25 (Tier 3)

Calculation:

```
Side: NO (p < 0.5)
pEff: 1 - 0.30 = 0.70 (effective prob of NO winning)
qEff: 1 - 0.45 = 0.55 (price of NO)
f*: (0.70 - 0.55) / (1 - 0.55) = 0.15 / 0.45 = 0.3333
α: 0.25
f_real: 0.25 × 0.3333 = 0.0833
Bet: 0.0833 × $10,000 = $833
```

Result: Bet $833 on NO (8.33% of bankroll)

### Example 3: No Edge (Market Efficient)

Given:
- Model prediction: p = 0.55
- Market price: q = 0.56 (market implies higher probability)
- Bankroll: $10,000
- Brier score: 0.18 → α = 0.40 (Tier 4)

Calculation:

```
Side: YES (p ≥ 0.5)
pEff: 0.55
qEff: 0.56
f*: (0.55 - 0.56) / (1 - 0.56) = -0.01 / 0.44 = -0.0227
```

Result: f* < 0 → No edge → Bet $0 (no trade)

### Example 4: Drawdown Adjustment (Yellow Mode)

Given:
- Model prediction: p = 0.68
- Market price: q = 0.50
- Bankroll: $9,200 (down from HWM of $10,500)
- Drawdown: (10,500 - 9,200) / 10,500 = 12.38% → Yellow mode
- Brier score: 0.17 → α_base = 0.40 (Tier 4)
- Yellow adjustment: alphaMultiplier = 0.5

Calculation:

```
Side: YES
pEff: 0.68
qEff: 0.50
f*: (0.68 - 0.50) / (1 - 0.50) = 0.18 / 0.50 = 0.36
α_base: 0.40
α_adjusted: 0.40 × 0.5 = 0.20 (yellow mode cuts alpha in half)
f_real: 0.20 × 0.36 = 0.072
Bet: 0.072 × $9,200 = $662
```

Result: Bet $662 on YES (7.2% of bankroll), reduced from $1,324 if in green mode

## Risk of Ruin

One of the Kelly criterion's key properties is that it never risks total ruin (assuming f* < 1 and infinite divisibility of capital). The bankroll approaches zero asymptotically but never reaches it.

However, practical constraints introduce ruin risk:
1. **Minimum bet size**: minBetUsd creates a floor below which trading stops
2. **Model error**: Incorrect p estimates can lead to overbetting
3. **Non-ergodic outcomes**: Sequential betting can amplify losses during streaks

The fractional Kelly approach mitigates these risks by reducing bet sizes.

## Expected Growth Rate

For a single bet, the expected logarithmic growth is:

```
E[log(bankroll)] = p × log(1 + b × f) + q × log(1 - f)
```

Full Kelly maximizes this quantity. Fractional Kelly (α × f*) reduces the growth rate but also reduces variance, making the actual realized growth more stable.

## Brier Score Connection to P&L

The Brier score measures calibration accuracy:

```
Brier Score = mean((predicted_probability - actual_outcome)²)
```

In the Polymarket Bot:
- Lower Brier score = better calibration = higher alpha multiplier
- Brier score is tracked over rolling windows (typically last 100+ predictions)
- If Brier score degrades, the system automatically reduces position sizes
- This creates a feedback loop: poor predictions → low alpha → small positions → limited losses

## Assumptions and Limitations

### Assumptions

1. **Independent outcomes**: Each bet is independent (no correlation)
2. **Known probabilities**: p is accurately estimated
3. **Binary payoffs**: Win or lose, no partial outcomes
4. **Infinite divisibility**: Can bet any fraction of bankroll
5. **No fees**: Original Kelly assumes zero transaction costs

### Polymarket Adjustments

1. **3% fee on wins**: Accounted for in recordTrade()
2. **Minimum bet size**: minBetUsd creates discrete rather than continuous sizing
3. **Maximum bet cap**: maxBetPct prevents single bets from dominating bankroll
4. **Model uncertainty**: Brier-tiered alpha adjusts for estimation error

### When Kelly Fails

1. **Model miscalibration**: If p systematically overestimates probabilities, Kelly will overbet
2. **Correlated outcomes**: Betting on related markets violates independence assumption
3. **Non-stationary edge**: If p accuracy degrades over time, historical Brier may lag reality
4. **Black swans**: Extreme outcomes outside the model's training distribution

## Key Excerpts

1. "For prediction markets: f* = (p - q) / (1 - q) where p is your probability estimate and q is the market price. If f* ≤ 0, no edge exists."
2. "Half Kelly (α=0.5) achieves 75% of full Kelly's growth rate but only 25% of its variance — the most favorable tradeoff for practical trading."
3. "The Brier-tiered alpha system maps calibration quality to fractional Kelly: < 0.18 Brier → α=0.40; > 0.26 Brier → α=0.10. This creates adaptive risk management based on model accuracy."
4. "The Kelly criterion never risks total ruin (f* < 1), but practical constraints (minimum bet size, model error, non-ergodic outcomes) require fractional Kelly for real-world robustness."

## Further Reading

- Kelly, J. L. (1956). "A New Interpretation of Information Rate". Bell System Technical Journal.
- Thorp, E. O. (1969). "Optimal Gambling Systems for Favorable Games". Review of the International Statistical Institute.
- MacLean, L. C., Thorp, E. O., & Ziemba, W. T. (2011). The Kelly Capital Growth Investment Criterion. World Scientific.
