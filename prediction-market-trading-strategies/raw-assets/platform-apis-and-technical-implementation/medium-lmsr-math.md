# How Polymarket Actually Prices Beliefs: The Math Behind LMSR

## Metadata
- **URL:** https://medium.com/coding-nexus/how-polymarket-actually-prices-beliefs-the-math-behind-lmsr-98b424e12da5
- **Source:** Coding Nexus (Medium)
- **Type:** article
- **Author:** Coding Nexus
- **Date Published:** Unknown
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Introduction to Prediction Markets and Binary Options

Prediction markets are platforms where participants can trade contracts based on the outcomes of future events. Each contract typically pays out $1 if a specific outcome occurs and $0 otherwise. The price of these contracts reflects the collective belief about the likelihood of that outcome.

Polymarket is one of the largest prediction markets today, offering trading on global events ranging from politics to sports to economics. Understanding how these markets determine prices is crucial for anyone looking to participate or build on top of them.

## Binary Options and Contract Structure

At their core, prediction market contracts function like binary options. When you buy a "Yes" contract for $0.60, you are essentially betting that the event will occur. If it does, you receive $1.00, netting $0.40 profit. If it doesn't, you lose your $0.60 stake.

This binary payoff structure means the price of a contract should theoretically equal the probability of the outcome occurring. A contract priced at $0.70 should imply a 70% chance of the event happening. However, in practice, prices can deviate from true probabilities due to trading dynamics, fees, and market sentiment.

## The Constant Product AMM Problem

Early prediction markets, including Polymarket before its 2023 upgrade, used Automated Market Makers (AMMs) based on the constant product formula (x × y = k). While simple to implement, this approach creates significant problems for binary outcome contracts.

Under constant product AMMs, liquidity is spread evenly across all possible prices. For a contract that will resolve to either $0 or $1, most of this liquidity ends up in regions that will never be reached. The AMM provides substantial liquidity at extreme prices (near $0 or $1) where the contract can never actually trade. This creates capital inefficiency and poor price discovery for the probabilities that matter most.

## The Logarithmic Market Scoring Rule (LMSR)

The Logarithmic Market Scoring Rule (LMSR), invented by economist Robin Hanson in 2003, provides a more elegant solution. Rather than spreading liquidity evenly, LMSR concentrates liquidity where it is most needed and most likely to be used.

The core concept is straightforward: the cost to move a contract's price depends on how far you move it and how much has already been traded. Moving from $0.50 to $0.51 costs less than moving from $0.80 to $0.81, because the latter region is more "specialized" and less frequently traded.

### How LMSR Pricing Works

The LMSR uses a mathematical formula that naturally concentrates liquidity around the 50% probability mark while still allowing trading at any price. The key parameter b (beta) controls how much liquidity exists in the system. A higher b means more liquidity and smaller price movements for a given trade.

The probability assigned to each outcome is calculated as:

```
p_i = exp(q_i / b) / Σ exp(q_j / b)
```

Where q_i is the number of shares outstanding for outcome i, and b is the liquidity parameter. This is mathematically equivalent to the softmax function commonly used in machine learning classifiers.

The cost function for purchasing shares is:

```
C = b × ln(Σ exp(q_i / b))
```

This ensures that buying shares becomes progressively more expensive as you accumulate more of them, preventing any single trader from monopolizing the market.

### Key Properties of LMSR

LMSR exhibits several important properties that make it well-suited for prediction markets:

**Information Aggregation**: The mechanism ensures that prices reflect the collective belief of all participants. When informed traders buy shares in an outcome, they push the price up, signaling their information to the market.

**Bounded Losses**: The market maker's maximum loss is bounded by b × ln(n), where n is the number of possible outcomes. This makes risk management tractable.

**Incentive Compatibility**: The logarithmic scoring rule is "proper" — meaning the optimal strategy is to report your true belief. This aligns incentives between the market maker and participants.

**Conditional Trading**: LMSR supports trading conditional contracts without affecting marginal probabilities. This is crucial for building complex prediction market structures.

## Transition to CLOB Architecture

Modern high-volume prediction markets like current Polymarket have moved away from pure LMSR to Central Limit Order Book (CLOB) architectures. CLOB systems match buyers and sellers directly, providing better price discovery and capital efficiency for liquid markets.

Under CLOB, the market price at any moment is simply the midpoint of the best bid and best offer. The spread between these represents the cost of immediate liquidity. This approach works well for active markets but requires sufficient trading volume to ensure tight spreads.

The hybrid approach combines off-chain order matching with on-chain settlement, capturing benefits of both systems. Users sign orders off-chain (reducing gas costs), trades execute instantly without blockchain confirmation, and settlement happens on-chain atomically.

## Practical Implications for Traders

Understanding LMSR mechanics helps traders identify opportunities. When the LMSR price diverges from your own probability estimate, there may be a tradeable opportunity. The convexity of the cost function means small price differences can represent significant probability mispricings.

For building on prediction markets, recognizing that LMSR pricing is equivalent to softmax helps in designing systems that interact intelligently with these markets. Machine learning practitioners already understand this math intuitively.

## Key Excerpts

1. "LMSR uses a mathematical formula that naturally concentrates liquidity around the 50% probability mark while still allowing trading at any price. The key parameter b controls how much liquidity exists in the system."

2. "The probability assigned to each outcome is calculated as: p_i = exp(q_i / b) / Σ exp(q_j / b). This is mathematically equivalent to the softmax function commonly used in machine learning classifiers."

3. "The market maker's maximum loss is bounded by b × ln(n), where n is the number of possible outcomes. This makes risk management tractable."

## Scrape Notes
- Content completeness: full
- Article provides detailed LMSR mathematical explanation with clear examples
- Highly relevant for understanding Polymarket's pricing mechanism transition from AMM to CLOB
