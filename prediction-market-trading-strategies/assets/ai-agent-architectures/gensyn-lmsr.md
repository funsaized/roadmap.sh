# LMSR: Logarithmic Market Scoring Rule

## Metadata
- **URL:** https://blog.gensyn.ai/lmsr-logarithmic-market-scoring-rule/
- **Source:** gensyn.ai/blog
- **Type:** article
- **Author:** Gensyn AI
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Summary

Comprehensive technical explanation of the Logarithmic Market Scoring Rule (LMSR), the mathematical engine powering prediction markets. Covers the cost function, pricing formula, incentive compatibility, information aggregation, and connections to machine learning (softmax function). Explains why LMSR solves the liquidity problem in niche prediction markets and discusses limitations addressed by newer mechanisms like PM-AMM.

## Enrichment

### Topic Tags
- LMSR
- automated-market-maker
- price-discovery
- mathematical-foundations
- liquidity-provision
- information-aggregation
- machine-learning-connections

### Content Depth
deep-dive

### Temporal Relevance
evergreen

### Entities

**People:**
- Robin Hanson — formalized LMSR in 2002

**Organizations:**
- Gensyn AI — author/publisher
- Paradigm — referenced for Dynamic PM-AMM (2024)

**Technologies:**
- LMSR (Logarithmic Market Scoring Rule)
- Dynamic PM-AMM
- Softmax function
- Bregman divergences

**Concepts:**
- Cost function: b × ln(1 + e^(q/b))
- Sigmoid pricing: Price(YES) = 1/(1 + e^(-q/b))
- Incentive compatibility
- Information aggregation
- Bounded loss: b × ln(n)
- Price discovery through crowdsourcing
- Maximum likelihood estimation

**Data Points:**
- LMSR formalized in 2002
- Worst-case AMM loss capped at b × ln(n)
- PM-AMM introduced by Paradigm in November 2024

### Cross-References
- **extends** → paradigm-pm-amm (PM-AMM builds on LMSR foundations)
- **complements** → medium-lmsr-math (alternative LMSR explanation with Python code)
- **complements** → polymarket-ctf-overview (CTF is the token layer; LMSR is the pricing layer)
- **cites** → cdetrio-prediction-market-lmsr (another LMSR implementation)
- **supports** → navnoorbawa-prediction-markets-math (confirms LMSR as foundational mechanism)
