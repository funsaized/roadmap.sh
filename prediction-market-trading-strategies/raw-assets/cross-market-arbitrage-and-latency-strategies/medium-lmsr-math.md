# How Polymarket Actually Prices Beliefs: The Math Behind LMSR

## Metadata
- **URL:** https://medium.com/coding-nexus/how-polymarket-actually-prices-beliefs-the-math-behind-lmsr-98b424e12da5
- **Source:** Coding Nexus (Medium)
- **Type:** article
- **Author:** Coding Nexus
- **Date Published:** Unknown
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** high

## Content

This article provides a detailed technical walkthrough of how Polymarket uses the Logarithmic Market Scoring Rule (LMSR) for price discovery, with accompanying Python implementation code.

## The Core Invariant: P_YES + P_NO = $1.00

Prediction market contracts are binary options with payoffs of either $1.00 or $0.00. On Polymarket, each market creates two ERC-1155 tokens (YES and NO) via the Gnosis Conditional Tokens Framework. The foundational pricing invariant is:

**P_YES + P_NO = $1.00**

This is enforced by the contract logic — if you hold 1 YES token and 1 NO token, you can always redeem them for exactly $1.00 at settlement. Any violation of this sum creates an arbitrage opportunity.

## Logarithmic Market Scoring Rule (LMSR)

The LMSR, invented by Robin Hanson in 2003, is an automated market maker that provides continuous liquidity without requiring a traditional order book. The key equations:

**Cost Function:**
C(q) = b × ln(Σ exp(q_i / b))

**Price for outcome i:**
p_i = exp(q_i/b) / Σ_j exp(q_j/b)

Where:
- q_i = number of shares outstanding for outcome i
- b = liquidity parameter (higher b = more liquidity, smoother prices)
- The price function IS the softmax function — a direct connection to machine learning

## Python Implementation

The article provides a clean Python implementation:

```python
import numpy as np

class LMSR:
    def __init__(self, b=10, n_outcomes=2):
        self.b = b
        self.q = np.zeros(n_outcomes)
    
    def cost(self):
        return self.b * np.log(np.sum(np.exp(self.q / self.b)))
    
    def price(self, outcome=None):
        exp_q = np.exp(self.q / self.b)
        p = exp_q / np.sum(exp_q)
        if outcome is not None:
            return p[outcome]
        return p
    
    def buy(self, outcome, amount):
        p_before = self.price(outcome)
        self.q[outcome] += amount
        p_after = self.price(outcome)
        return p_before, p_after, self.cost()
```

## Connection to Machine Learning

The LMSR price function IS the softmax activation function used in neural networks:

- softmax(x)_i = exp(x_i) / Σ_j exp(x_j)
- LMSR price p_i = exp(q_i/b) / Σ_j exp(q_j/b)

This means every ML practitioner already understands the fundamental pricing mechanism of LMSR-based prediction markets. The liquidity parameter b is the temperature parameter — lower b = sharper distribution (more extreme probabilities), higher b = smoother distribution.

## Liquidity and Price Sensitivity

With LMSR, prices respond to trading activity in a bounded, predictable way:

- Buying shares increases q_i for that outcome
- This increases exp(q_i/b), raising p_i
- The price impact is logarithmic — diminishing returns on large purchases
- The cost function ensures bounded worst-case loss for the market maker: MaxLoss ≤ b × ln(n) where n = number of outcomes

## Key Properties

1. **Proper Scoring Rule Alignment**: LMSR implements the logarithmic scoring rule, which is proper — the market maker's expected cost is minimized when prices reflect true probabilities.

2. **Conditional Probability Preservation**: Unlike some market mechanisms, LMSR betting on conditional probabilities does not affect marginal probabilities — crucial for combinatorial markets.

3. **Bounded Risk**: The market maker's maximum loss is bounded by b × ln(n), regardless of how traders bet. This makes LMSR suitable for markets where the operator wants capped exposure.

## Historical Context

Polymarket originally launched with LMSR (as a CPMM-style AMM). In 2023, Polymarket migrated from AMM to CLOB (Central Limit Order Book) architecture for superior price discovery and capital efficiency. However, the LMSR mathematical framework remains foundational to understanding prediction market pricing mechanics, and many other prediction market platforms continue to use LMSR or variants.

## Key Excerpts

1. "The LMSR price function IS the softmax function — a direct bridge between prediction market mechanics and machine learning. Understanding one helps you understand the other."

2. "The liquidity parameter b controls how much each share purchase moves the price. A higher b means more shares must be bought to move the price by a given amount — this is exactly the 'temperature' parameter in softmax."

3. "The core invariant P_YES + P_NO = $1.00 creates the fundamental no-arbitrage condition. Any deviation from this sum creates a risk-free profit opportunity."

## Scrape Notes
- **Content completeness:** partial (article content was partially extracted; full code examples and detailed derivations may be truncated)
- **Note:** Medium sometimes applies paywalls for logged-out users; the technical content was accessible
