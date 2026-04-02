# Prediction Market AMM with Kelly Criterion and Position Sizing

## Metadata
- **URL:** https://github.com/Apostlex0/PredictionMarket_AMM
- **Source:** GitHub / Apostlex0
- **Type:** code/repository
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Content

# Prediction Market AMM with Kelly Criterion and Position Sizing

## Overview

This repository implements a prediction market automated market maker (AMM) with sophisticated position sizing based on the Kelly criterion. It includes complete mathematical derivations for optimal bet sizing, loss versus reversion (LVR) analysis, and practical trading strategies.

## Core Mathematics

### Binary Prediction Market Structure

In a binary prediction market:
- YES and NO shares always sum to $1.00 (P_YES + P_NO = $1.00)
- The market price represents the implied probability of the outcome
- Traders profit when their probability estimate is better than the market consensus

### The Edge Formula

Edge represents the difference between your estimated probability and the market price:

```
Edge = p_true - Market_Price
```

Where:
- p_true = your estimated true probability
- Market_Price = current market price (implied probability)

### Kelly Criterion Formula

The Kelly criterion determines the optimal fraction of bankroll to wager:

```
f* = (p × b - q) / b
```

Where:
- p = true probability (your forecast)
- q = 1 - p (probability of losing)
- b = net odds received (profit per unit bet)

### Simplified Form for Prediction Markets

For binary prediction markets where winning pays $1.00:

```
b = (1 - Market_Price) / Market_Price = (1 - q) / q
f* = (p - q) / (1 - q)
```

### Fractional Kelly

Full Kelly maximizes long-run growth but has high variance. Fractional Kelly (typically 0.25x to 0.5x) is recommended:

```
f_fractional = α × f*  where 0 < α ≤ 1
```

Common values:
- 0.25x Kelly (quarter Kelly): 75% of growth, 25% of variance
- 0.50x Kelly (half Kelly): 87.5% of growth, 50% of variance

## Position Sizing

### Bankroll Management

Never risk more than a small fraction of your bankroll on a single bet. Recommended maximum per bet:
- Conservative: 2-5% of bankroll
- Moderate: 5-10% of bankroll
- Aggressive: 10-20% of bankroll

### Kelly Sizing Example

Market price = $0.60 (60% implied probability)
Your estimated probability = 75%

```
b = (1 - 0.60) / 0.60 = 0.667
f* = (0.75 - 0.60) / (0.4) = 0.375

If using 0.5x fractional Kelly:
Position = 0.5 × 0.375 × Bankroll = 0.1875 × Bankroll
```

## Loss Versus Reversion (LVR)

LVR (Loss Versus Rebalancing) is the cost incurred by liquidity providers when arbitrageurs trade against the AMM.

### LVR Calculation

In a constant product AMM (x × y = k), when the true probability differs from the AMM price:

```
LVR = (p_true - p_AMM) × spread × Volume
```

The AMM always provides a bid at p_AMM - spread/2 and an ask at p_AMM + spread/2.

### Mitigating LVR

- Use tighter spreads in high-liquidity markets
- Adjust liquidity provision based on volatility
- Monitor adverse selection from informed traders
- Implement inventory skew controls

## Brier Score Connection

The Brier score measures calibration accuracy for probabilistic predictions:

```
Brier Score = (1/N) × Σ(predicted_probability - actual_outcome)²
```

In prediction market trading:
- Lower Brier score = better calibrated predictions
- Brier score can be used to adjust Kelly sizing dynamically
- If your Brier score degrades, reduce position sizes

### Brier-Adjusted Kelly

| Brier Score | Alpha (Fractional Kelly) |
|-------------|-------------------------|
| < 0.18      | 0.40 (40% of full Kelly)|
| 0.18 - 0.22 | 0.25 (25% of full Kelly)|
| 0.22 - 0.26 | 0.20 (20% of full Kelly)|
| > 0.26      | 0.10 (10% of full Kelly)|

## Code Implementation

### Kelly Fraction Calculation (Python)

```python
def kelly_fraction(p_true, market_price):
    """
    Calculate the Kelly fraction for a prediction market bet.
    
    Args:
        p_true: Your estimated true probability (0 to 1)
        market_price: Current market price (0 to 1)
    
    Returns:
        Kelly fraction (optimal bet as fraction of bankroll)
    """
    if p_true <= market_price:
        return 0.0  # No edge
    
    b = (1 - market_price) / market_price
    p_lose = 1 - p_true
    
    kelly = (p_true * b - p_lose) / b
    return max(0, kelly)

def fractional_kelly(p_true, market_price, alpha=0.5):
    """Apply fractional Kelly to reduce variance."""
    return alpha * kelly_fraction(p_true, market_price)

def position_size(bankroll, kelly_fraction, max_position_pct=0.2):
    """Calculate dollar position size."""
    return min(kelly_fraction * bankroll, max_position_pct * bankroll)
```

### Brier Score Calculator

```python
def brier_score(predictions, outcomes):
    """
    Calculate Brier score for a series of predictions and outcomes.
    
    Args:
        predictions: List of predicted probabilities
        outcomes: List of actual outcomes (0 or 1)
    
    Returns:
        Mean squared error (lower is better)
    """
    n = len(predictions)
    return sum((p - o) ** 2 for p, o in zip(predictions, outcomes)) / n
```

## Key Excerpts

1. "The Kelly formula f* = (p × b - q) / b gives the optimal fraction of bankroll to wager for maximum long-run geometric growth"
2. "Fractional Kelly (α × f*) trades 25-50% of growth rate for 50-75% reduction in variance, making it practical for real-world trading"
3. "LVR (Loss Versus Reversion) is the primary cost for AMM liquidity providers — the spread and adverse selection from informed traders determines profitability"
4. "Brier score measures calibration accuracy and can be used to dynamically adjust Kelly fraction sizing"
