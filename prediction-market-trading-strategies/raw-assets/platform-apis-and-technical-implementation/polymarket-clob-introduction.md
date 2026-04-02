# Polymarket CLOB API Introduction

## Metadata
- **URL:** https://docs.polymarket.com/developers/CLOB/introduction
- **Source:** Polymarket Documentation
- **Type:** documentation
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Overview

Polymarket's CLOB (Central Limit Order Book) is a hybrid-decentralized trading system — off-chain order matching with on-chain settlement via the Exchange contract (audited by Chainsecurity). All trading is non-custodial. Orders are EIP-712 signed messages, and matched trades settle atomically on Polygon. The operator cannot set prices or execute unauthorized trades.

## Authentication

Two levels of authentication:

**L1**: EIP-712 signature (private key) — used to derive API credentials
**L2**: HMAC-SHA256 (API credentials) — used for trading operations (orders, cancellations, queries)

You use your private key once to derive L2 credentials (API key, secret, passphrase).

### TypeScript Derivation
```typescript
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers";

const signer = new Wallet(process.env.PRIVATE_KEY);
const tempClient = new ClobClient("https://clob.polymarket.com", 137, signer);
const apiCreds = await tempClient.createOrDeriveApiKey();
```

### Python Derivation
```python
from py_clob_client.client import ClobClient
temp_client = ClobClient("https://clob.polymarket.com", key=private_key, chain_id=137)
api_creds = temp_client.create_or_derive_api_creds()
```

## Signature Types

| Wallet Type | ID | When to Use | Funder Address |
|---|---|---|---|
| EOA | 0 | Standalone wallet — you pay your own gas | Your EOA wallet address |
| POLY_PROXY | 1 | Polymarket account via Magic Link (email/Google) | Your proxy wallet address |
| GNOSIS_SAFE | 2 | Polymarket account via browser wallet (MetaMask, Rabby) or embedded wallet (Privy, Turnkey) | Your proxy wallet address |

## REST API Headers

### L1 Headers (deriving credentials)
- `POLY_ADDRESS`: Your wallet address
- `POLY_SIGNATURE`: EIP-712 signature
- `POLY_TIMESTAMP`: Unix timestamp
- `POLY_NONCE`: Request nonce

### L2 Headers (all trading operations)
- `POLY_ADDRESS`: Your wallet address
- `POLY_SIGNATURE`: HMAC-SHA256 signature of the request
- `POLY_TIMESTAMP`: Unix timestamp
- `POLY_API_KEY`: Your API key
- `POLY_PASSPHRASE`: Your API passphrase

Note: Even with L2 authentication, methods that create orders still require the user's private key for EIP-712 order payload signing.

## SDKs Available

- **TypeScript**: npm install @polymarket/clob-client
- **Python**: pip install py-clob-client
- **Rust**: cargo add polymarket-client-sdk

## Documentation Sections

- **Quickstart**: Place your first order end-to-end
- **Orderbook**: Reading orderbook, prices, spreads, midpoints
- **Orders**: Order types, tick sizes, creating, cancelling, querying
- **Fees**: Fee structure, fee-enabled markets, maker rebates
- **Gasless Transactions**: Execute onchain operations without paying gas
- **CTF Tokens**: Split, merge, and redeem outcome tokens
- **Bridge**: Deposit and withdraw funds across chains

## Key Excerpts

1. "All trading is non-custodial. Orders are EIP-712 signed messages, and matched trades settle atomically on Polygon. The operator cannot set prices or execute unauthorized trades."

2. "Two levels of authentication: L1 (EIP-712) for deriving credentials, L2 (HMAC-SHA256) for all trading operations."

3. "Three wallet types: EOA (type 0), POLY_PROXY via Magic Link (type 1), GNOSIS_SAFE via browser/embedded wallet (type 2)."

## Scrape Notes
- Content completeness: full
- Excellent reference for Polymarket CLOB API authentication and structure
- Critical for building autonomous trading systems on Polymarket
