# Morpheus: PM-AMM Implementation on Aptos

## Metadata
- **URL:** https://github.com/Apostlex0/PredictionMarket_AMM
- **Source:** github.com/Apostlex0
- **Type:** code/documentation
- **Author:** Apostlex0
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Summary

High-fidelity open-source implementation of Paradigm's PM-AMM on the Aptos blockchain using Move. Implements both static and dynamic PM-AMM with Gaussian score dynamics, normal CDF pricing, uniform LVR, and time-decaying liquidity. Includes complete mathematical derivations, modular contract architecture, and comparison tables against CPMM and LMSR.

## Enrichment

### Topic Tags
- PM-AMM
- smart-contracts
- automated-market-maker
- Aptos-blockchain
- Move-language
- liquidity-provision
- LVR-analysis

### Content Depth
deep-dive

### Temporal Relevance
current

### Entities

**People:**
- Ciamac Moallemi — co-author of PM-AMM paper (Paradigm)
- Dan Robinson — co-author of PM-AMM paper (Paradigm)

**Organizations:**
- Paradigm — research origin of PM-AMM
- Apostlex0 — implementation author (Morpheus)

**Technologies:**
- PM-AMM (Prediction Market AMM)
- Aptos blockchain
- Move programming language
- Normal CDF/PDF pricing
- Fixed-point arithmetic (64.64)
- ERC-1155 (referenced as comparison)

**Concepts:**
- Static PM-AMM invariant: (y-x)Φ((y-x)/L) + Lφ((y-x)/L) - y = 0
- Dynamic PM-AMM: time-decaying L·√(T-t)
- Uniform LVR: constant fraction of pool value regardless of price
- Total expected LVR = V₀/2
- Liquidity fingerprints — concentrated at 50% probability
- Mint pair: 1-to-1 collateralization
- Single-metric LP: desired_value_increase

**Data Points:**
- PM-AMM paper: November 2024 (Paradigm)
- Total expected LVR over lifetime = V₀/2 (50% of initial capital)

### Cross-References
- **extends** → paradigm-pm-amm (direct implementation of the Paradigm paper)
- **extends** → gensyn-lmsr (PM-AMM is the next evolution beyond LMSR)
- **contradicts** → gnosis-conditional-tokens-market-makers (different AMM approach — CPMM vs PM-AMM)
- **complements** → hummingbot-inventory-risk (PM-AMM's time-decay addresses inventory risk near expiry)
- **complements** → terrytrl100-polymarket-automated-mm (different approach: CLOB market making vs AMM)
