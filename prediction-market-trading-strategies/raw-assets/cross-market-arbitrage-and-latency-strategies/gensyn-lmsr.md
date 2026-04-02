# LMSR: Logarithmic Market Scoring Rule

## Metadata
- **URL:** https://blog.gensyn.ai/lmsr-logarithmic-market-scoring-rule/
- **Source:** Gensyn.ai Blog
- **Type:** article
- **Author:** Gensyn.ai
- **Date Published:** Unknown
- **Date Scraped:** 2026-03-31
- **Authority:** medium-high
- **Relevance:** high

## Content

This article provides a comprehensive explanation of the Logarithmic Market Scoring Rule (LMSR), the foundational automated market maker mechanism for prediction markets, invented by Robin Hanson in 2003.

## The Problem LMSR Solves

Traditional markets need both buyers and sellers to agree on a price. In prediction markets, finding this agreement is especially difficult because the "commodity" being traded (information about future events) is hard to value. The LMSR solves this by having a single market maker that always provides a quote — eliminating the need to find a counterparty.

## The LMSR Mechanism

The LMSR is an automated market maker that:
1. **Always provides a quote** — traders can always buy or sell at the displayed price
2. **Has bounded worst-case loss** — the market maker's maximum loss is capped
3. **Implements proper scoring rules** — prices reflect the market's best estimate of true probabilities

### Mathematical Framework

**State Variables:**
- q_i = number of shares outstanding for outcome i
- b = liquidity parameter (controls how much prices move per trade)
- n = number of possible outcomes

**Cost Function (what you pay to buy shares):**
C(q) = b × ln(Σ exp(q_i / b))

**Market Price (probability estimate) for outcome i:**
p_i = exp(q_i/b) / Σ_j exp(q_j/b)

This is the softmax function — identical to the activation function used in neural networks.

**Net Cost of a Trade:**
When buying d shares of outcome i:
Net Cost = C(q + d × e_i) - C(q)
= b × ln(Σ exp(q_j/b)) - b × ln(Σ exp((q_j + d × δ_ij)/b))

## Intuition Behind the Formula

The LMSR can be understood through the lens of **proper scoring rules** from probability theory:

- A scoring rule rewards a forecaster based on the reported probability and the actual outcome
- The **logarithmic scoring rule** rewards: log(p_i) when outcome i occurs
- This is a "proper" scoring rule — it maximizes expected reward when you report your true belief
- The LMSR implements this scoring rule as a market mechanism

## The Liquidity Parameter b

The parameter b controls market maker aggressiveness:
- **High b** → More liquid, prices less sensitive to trades, larger maximum loss for market maker
- **Low b** → Less liquid, prices more sensitive, smaller maximum loss

**Maximum Loss Bound:**
MaxLoss ≤ b × ln(n)

For a binary market (n=2): MaxLoss ≤ b × ln(2) ≈ 0.693b
For a 10-outcome market: MaxLoss ≤ b × ln(10) ≈ 2.303b

## Example: Binary Market

Consider a binary market with b = 10:
- Initially: q_YES = 0, q_NO = 0
- Price of YES: p_YES = exp(0)/[exp(0) + exp(0)] = 0.5
- Price of NO: p_NO = 0.5

After buying 10 shares of YES:
- q_YES = 10, q_NO = 0
- p_YES = exp(10/10)/[exp(10/10) + exp(0)] = e^1/(e^1 + 1) ≈ 0.731
- Cost paid = b × ln(2 × exp(1)) - b × ln(2) = 10 × ln(e) = 10

The trader paid $10 for 10 shares that pay $1 each if YES wins — this is a fair bet at 73.1% implied probability.

## LMSR in Practice: Polymarket

Polymarket uses conditional tokens (via Gnosis CTF) with LMSR pricing:
- YES and NO tokens are created as ERC-1155 tokens
- The AMM pricing follows the LMSR softmax formula
- Traders can always trade at the displayed price without finding a counterparty

## Limitations of LMSR

1. **Revenue generation**: The market maker earns money from trades, but the relationship between volume and revenue is non-linear
2. **Capital efficiency**: The LMSR requires locking capital proportional to b × n, which can be substantial
3. **Static liquidity**: Liquidity is distributed across all outcomes equally — LMSR doesn't concentrate liquidity where it's most needed
4. **Migration to CLOB**: Polymarket migrated from LMSR to CLOB in 2023 for better price discovery, though the LMSR math remains foundational

## Relationship to Machine Learning

The LMSR price formula IS the softmax function:
- ML softmax: softmax(x)_i = exp(x_i) / Σ_j exp(x_j)
- LMSR price: p_i = exp(q_i/b) / Σ_j exp(q_j/b)

This deep connection means:
- ML practitioners already understand the fundamental pricing mechanism
- Temperature scaling in ML (for calibrating model outputs) is identical to adjusting b in LMSR
- The LMSR can be interpreted as a neural network where share counts are activations

## Key Excerpts

1. "The LMSR's price function IS the softmax function — the same function used in neural network classification layers. The liquidity parameter b is equivalent to the temperature parameter in ML."

2. "The LMSR has bounded worst-case loss: MaxLoss ≤ b × ln(n), meaning the market maker always knows their maximum exposure regardless of trader behavior."

3. "Because LMSR implements a proper scoring rule, the market naturally converges to accurate probability estimates as traders with superior information buy shares, moving prices toward true probabilities."

## Scrape Notes
- **Content completeness:** full (article was fully accessible and well-structured)
- **Note:** Gensyn blog is a technical blog focused on AI/ML and DeFi; the article had excellent mathematical content
