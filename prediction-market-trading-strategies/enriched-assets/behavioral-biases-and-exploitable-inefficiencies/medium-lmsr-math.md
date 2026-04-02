# How Polymarket Actually Prices Beliefs: The Math Behind LMSR

## Metadata
- **URL:** https://medium.com/coding-nexus/how-polymarket-actually-prices-beliefs-the-math-behind-lmsr-98b424e12da5
- **Source:** Coding Nexus (Medium)
- **Type:** article
- **Author:** CodePulse
- **Date Published:** March 7, 2026
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** high

## Summary

Technical walkthrough of LMSR pricing with Python implementation code. Explains the softmax/LMSR equivalence, the liquidity parameter as temperature, bounded market maker loss, and Polymarket's historical AMM→CLOB migration in 2023. Includes working Python LMSR class implementation.

## Enrichment

### Topic Tags
- LMSR
- Python-implementation
- softmax-equivalence
- price-discovery
- Polymarket-history

### Content Depth
intermediate

### Temporal Relevance
current

### Entities

**People:**
- Robin Hanson — LMSR inventor (2003)
- CodePulse — article author

**Organizations:**
- Polymarket — platform discussed
- Coding Nexus — publisher

**Technologies:**
- LMSR (Python implementation)
- Softmax function
- ERC-1155 tokens
- Gnosis CTF
- NumPy

**Concepts:**
- Cost function: C(q) = b × ln(Σ exp(q_i/b))
- Price function = softmax: p_i = exp(q_i/b) / Σ exp(q_j/b)
- Temperature parameter b = liquidity parameter
- Bounded risk: MaxLoss ≤ b × ln(n)
- Proper scoring rule alignment
- Conditional probability preservation
- Polymarket AMM→CLOB migration (2023)

### Cross-References
- **complements** → gensyn-lmsr (different perspective on same LMSR math)
- **supports** → navnoorbawa-prediction-markets-math (confirms LMSR foundations)
- **cites** → cdetrio-prediction-market-lmsr (another LMSR implementation)
- **complements** → polymarket-clob-introduction (covers post-LMSR CLOB architecture)
