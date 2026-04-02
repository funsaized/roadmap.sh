# Conditional Token Framework (CTF) Overview

## Metadata
- **URL:** https://docs.polymarket.com/trading/ctf/overview
- **Source:** docs.polymarket.com
- **Type:** documentation
- **Author:** Polymarket
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Summary

Official Polymarket documentation on the Conditional Token Framework (CTF) — the ERC-1155 token standard underlying all Polymarket prediction markets. Covers token mechanics (YES/NO tokens), split/merge operations, market creation, liquidity provision, resolution mechanisms (Chainlink Oracle, UMA Optimistic Oracle), and smart contract architecture.

## Enrichment

### Topic Tags
- conditional-tokens
- smart-contracts
- market-infrastructure
- token-mechanics
- resolution-mechanisms
- ERC-1155

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**People:**
(none named)

**Organizations:**
- Polymarket — platform operator
- Gnosis — developed CTF standard
- Chainlink — oracle provider for crypto markets
- UMA — optimistic oracle for subjective outcomes

**Technologies:**
- Conditional Token Framework (CTF)
- ERC-1155 multi-token standard
- Polygon PoS — settlement chain
- USDC — collateral token
- Chainlink Oracle
- UMA Optimistic Oracle
- EIP-712 signed orders

**Concepts:**
- Binary resolution: YES=$1 / NO=$0
- Core invariant: P(YES) + P(NO) = $1.00
- Split and merge operations
- Atomic settlement
- Schelling-point incentive structure
- Dispute bond: 760 USDC
- Challenge period: 2 hours

**Data Points:**
- UMA bond: 760 USDC
- Challenge period: 2 hours on mainnet

### Cross-References
- **complements** → polymarket-clob-introduction (CLOB handles order matching; CTF handles token lifecycle)
- **complements** → polymarket-docs (landing page overview)
- **supports** → gensyn-lmsr (CTF provides the token layer for LMSR pricing)
- **supports** → navnoorbawa-prediction-markets-math (confirms YES+NO=$1 invariant)
- **cites** → gnosis-conditional-tokens-market-makers (Gnosis created the CTF standard)
