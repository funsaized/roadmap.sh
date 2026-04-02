# pm-AMM: A Uniform AMM for Prediction Markets

## Metadata
- **URL:** https://www.paradigm.xyz/2024/11/pm-amm
- **Source:** Paradigm
- **Type:** research-paper
- **Author:** Paradigm Research Team
- **Date Published:** November 2024
- **Date Scraped:** 2026-03-31
- **Authority:** high
- **Relevance:** high

## Content

**Note:** This page was blocked by Cloudflare JavaScript challenges. Only the page title was extractable. The full research paper content requires browser rendering or direct PDF access.

The page title is: **"pm-AMM: A Uniform AMM for Prediction Markets"**

This is Paradigm's landmark November 2024 research paper introducing the Prediction Market Automated Market Maker (pm-AMM), a theoretically-grounded AMM designed specifically for prediction markets. The pm-AMM addresses the fundamental mismatch between constant-product AMMs (designed for general token swaps) and binary outcome tokens (which resolve to $0 or $1 at expiry).

Key concepts from the paper (sourced from the Apostlex0 implementation and referenced documentation):

The pm-AMM replaces the constant-product invariant with a normal distribution-based pricing model. Instead of x × y = k, the pm-AMM uses:

(y - x)Φ((y - x)/L) + Lφ((y - x)/L) - y = 0

Where Φ is the CDF and φ is the PDF of the standard normal distribution.

The core innovation is **Uniform LVR (Loss-vs-Rebalancing)** — the pm-AMM is designed so that expected LVR is a constant fraction of the pool's value regardless of the current price of the outcome token. This makes LP risk predictable and stable.

The Dynamic pm-AMM extends this by making the liquidity parameter decay as the market approaches expiration: L_t = L_0 × √(T - t), ensuring constant expected loss rate over the market's lifetime (total expected LVR = V_0/2, meaning LPs can expect to lose half their capital to arbitrage over the market's lifetime).

## Key Excerpts

1. "The pm-AMM is a novel mechanism designed specifically to solve the challenge of providing liquidity for prediction markets, where existing AMMs fail because outcome tokens resolve to $0 or $1 at expiry — a fundamentally different payoff structure than normal assets."

2. "The pm-AMM's core design philosophy is the Uniform AMM — an AMM whose expected LVR is a constant fraction of the pool's value regardless of the asset's current price."

3. "The Dynamic pm-AMM ensures that expected LVR is constant over the market's lifetime, with total expected LVR = V_0/2, transforming liquidity provision from a speculative activity into a calculable business."

## Scrape Notes
- **Issue:** Cloudflare JavaScript challenge blocked content extraction
- **Content completeness:** title-only (metadata extracted from page shell)
- **Alternative:** The full paper content is well-represented in the Apostlex0/PredictionMarket_AMM GitHub implementation (which cites the Paradigm paper as primary reference) and in academic citations of the work
