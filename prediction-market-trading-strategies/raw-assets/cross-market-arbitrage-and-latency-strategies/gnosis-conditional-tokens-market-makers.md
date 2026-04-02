# Gnosis Conditional Tokens Market Makers

## Metadata
- **URL:** https://github.com/gnosis/conditional-tokens-market-makers
- **Source:** GitHub / Gnosis
- **Type:** code-documentation
- **Author:** Gnosis
- **Date Published:** Unknown (historical repo)
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Content

This repository contains reference implementations and research code from Gnosis related to Conditional Tokens Framework (CTF) market makers. The Conditional Tokens Framework is the technical foundation that Polymarket uses for its token mechanics.

### README Summary

The repository contains various implementations of market makers for conditional tokens. The key insight is that conditional tokens allow for the creation of "derivative" outcome tokens — for example, given a market "Who will win the election?", conditional tokens can create sub-markets like "If Candidate A wins, what will the vote margin be?"

The repository demonstrates:
- How LMSR-style market makers work with conditional tokens
- Implementation of various automated market maker designs for prediction markets
- Integration patterns with the Gnosis Conditional Tokens smart contracts

### Conditional Token Framework Overview

The CTF allows creating outcome tokens that are conditional on other outcomes. For example:
- Base market: "Candidate A wins election" → creates YES/NO tokens
- Conditional market: "If Candidate A wins, margin > 5%" → can be created by splitting YES tokens

This enables:
1. **Combinatorial markets**: Trading on related outcomes without needing separate liquidity for each combination
2. **Cross-market arbitrage**: Exploiting mispricings between logically related markets
3. **Efficient capital use**: One pool of liquidity can serve multiple related markets

### Market Maker Implementations Included

The repository contains mathematical models and reference implementations for:
- Logarithmic Market Scoring Rule (LMSR) for conditional tokens
- Market maker pricing formulas for nested conditional markets
- Capital efficiency analysis of various AMM designs

### Key Technical Points

1. **Collateral Vaults**: All positions are backed by collateral deposited into smart contract vaults. This ensures no fractional reserve and no counterparty risk.

2. **Atomic Settlement**: When a market resolves, winning tokens are redeemable for collateral atomically. No manual settlement process needed.

3. **Universal Settlers**: A key innovation is the concept of "universal settlers" — smart contracts that can settle any combination of conditional positions, enabling complex multi-leg arbitrage strategies.

## Key Excerpts

1. "The Conditional Tokens Framework enables combinatorial prediction markets where a single pool of liquidity can serve multiple logically related markets simultaneously."

2. "Universal settlers allow arbitrageurs to take positions across multiple related markets atomically, extracting mispricings that would otherwise persist."

## Scrape Notes
- **Content completeness:** partial (only the README file was extracted; source code files not included)
- **Note:** GitHub repo page navigation was limited; the readme.rst provided the most substantive content
