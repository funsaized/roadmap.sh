# Polymarket Documentation

## Metadata
- **URL:** https://docs.polymarket.com/
- **Source:** Polymarket
- **Type:** documentation
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Overview

Build on the world's largest prediction market. Trade, integrate, and access real-time market data with the Polymarket API. The documentation covers Developer Quickstart, Core Concepts, API Reference, and SDKs.

## Developer Quickstart

Get started with code examples in TypeScript, Python, and Rust:

### TypeScript
```typescript
import { ClobClient, Side } from "@polymarket/clob-client";

const client = new ClobClient(host, chainId, signer, creds);

const order = await client.createAndPostOrder(
  { tokenID, price: 0.50, size: 10, side: Side.BUY },
  { tickSize: "0.01", negRisk: false }
);
```

### Python
```python
from py_clob_client.client import ClobClient
from py_clob_client.order_builder.constants import BUY

client = ClobClient(host, key=key, chain_id=chain_id, creds=creds)
order = client.create_and_post_order(
    OrderArgs(token_id=token_id, price=0.50, size=10, side=BUY),
    options={"tick_size": "0.01", "neg_risk": False}
)
```

### Rust
```rust
use polymarket_client_sdk::clob::{Client, Config};
use polymarket_client_sdk::clob::types::Side;
use polymarket_client_sdk::types::dec;

let client = Client::new(host, Config::default())?.authentication_builder(&signer).authenticate().await?;
let order = client.limit_order().token_id(token_id).price(dec!(0.50)).size(dec!(10)).side(Side::Buy).build().await?;
let signed = client.sign(&signer, order).await?;
let response = client.post_order(signed).await?;
```

## Documentation Sections

- **Quickstart**: Set up environment and make first API call
- **Core Concepts**: Markets, events, tokens, and trading mechanics
- **API Reference**: REST endpoints, WebSocket streams, authentication
- **SDKs**: Official Python, TypeScript, and Rust libraries
- **Builder Program**: Build apps on Polymarket and earn rewards
- **Help Desk**: Support, issues, and common questions
- **Status**: API uptime and service health

## Key Excerpts

1. "Build on the world's largest prediction market. APIs, SDKs, and tools for prediction market developers."

2. "The documentation includes official Python, TypeScript, and Rust libraries for faster development."

## Scrape Notes
- Content completeness: partial (landing page only, navigation content extracted)
- Good overview of available documentation sections
- Actual API details in sub-pages (CLOB introduction, CTF overview)
