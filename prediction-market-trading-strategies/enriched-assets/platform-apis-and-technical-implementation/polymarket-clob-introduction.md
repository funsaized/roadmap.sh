# Polymarket CLOB API Introduction

## Metadata
- **URL:** https://docs.polymarket.com/developers/CLOB/introduction
- **Source:** Polymarket Documentation
- **Type:** documentation
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Summary

Official API documentation for Polymarket's hybrid-decentralized CLOB. Covers two-tier authentication (L1 EIP-712, L2 HMAC-SHA256), three wallet types (EOA, POLY_PROXY, GNOSIS_SAFE), REST API headers, and SDK availability in TypeScript, Python, and Rust. Critical reference for building automated trading systems.

## Enrichment

### Topic Tags
- Polymarket-API
- CLOB
- authentication
- SDK
- trading-infrastructure
- smart-contracts

### Content Depth
reference

### Temporal Relevance
current

### Entities

**Organizations:**
- Polymarket — API provider
- Chainsecurity — Exchange contract auditor

**Technologies:**
- CLOB (Central Limit Order Book)
- EIP-712 signatures
- HMAC-SHA256
- Polygon settlement
- TypeScript SDK (@polymarket/clob-client)
- Python SDK (py-clob-client)
- Rust SDK (polymarket-client-sdk)
- ethers.js (Wallet)

**Concepts:**
- L1 authentication: EIP-712 for credential derivation
- L2 authentication: HMAC-SHA256 for trading operations
- Non-custodial: operator cannot set prices or execute unauthorized trades
- Atomic on-chain settlement
- Three wallet types: EOA (0), POLY_PROXY (1), GNOSIS_SAFE (2)

### Cross-References
- **complements** → polymarket-ctf-overview (CLOB handles orders; CTF handles tokens)
- **complements** → polymarket-docs (overview pointing to this detail)
- **supports** → terrytrl100-polymarket-automated-mm (bot uses this API)
- **supports** → warproxxx-poly-maker (bot uses this API)
- **supports** → navnoorbawa-prediction-markets-math (describes CLOB mechanics in theory)
