# pm-AMM: A Uniform AMM for Prediction Markets

## Metadata
- **URL:** https://www.paradigm.xyz/2024/11/pm-amm
- **Source:** paradigm.xyz
- **Type:** article
- **Date Published:** November 2024
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

The pm-AMM (prediction market Automated Market Maker) is a novel AMM designed specifically for prediction markets, introduced by Paradigm in November 2024. It aims to overcome the limitations of traditional AMMs, such as Uniswap's constant product market maker and the Logarithmic Market Scoring Rule (LMSR), when dealing with "outcome tokens." These tokens have a binary payoff (they resolve to $1 if an event occurs and $0 if it does not) and converge to a known value at a specific expiration time, a dynamic that conventional AMMs struggle to model effectively.

The pm-AMM paradigm leverages a "Gaussian score dynamics" model to understand how outcome token prices behave, drawing an analogy to the Black-Scholes model for binary options. There are two main types:

- **Static pm-AMM:** Provides uniform Loss-Versus-Rebalancing (LVR) across all prices at a given time.
- **Dynamic pm-AMM:** Extends the static model to address the time dimension. It reduces liquidity as the market approaches its expiration date, aiming to maintain a constant expected rate of LVR over the market's lifetime. This prevents LVR from increasing as expiration nears, which is a common issue with other AMMs.

The pm-AMM concentrates more liquidity around a 50% probability (i.e., when the token price is $0.50) and less at extreme price points (close to $0 or $1). This design is intended to make liquidity provision more predictable and less risky for liquidity providers (LPs).

The **uniform AMM paradigm** defines an AMM as "uniform" if its expected LVR is a constant fraction of the pool's value, irrespective of the asset's current price. This property is highly desirable for LPs as it stabilizes and regularizes their risk, enabling them to more accurately calculate their costs (LVR) and set appropriate trading fees for profitability.

**LMSR (Logarithmic Market Scoring Rule)** is a foundational mechanism for prediction markets. It operates as a cost-function-based market maker that ensures continuous liquidity and incentivizes traders to reveal their true beliefs. LMSR has strong theoretical guarantees, including bounded losses for the market maker. However, existing AMMs, including LMSR, generally do not exhibit uniform LVR for outcome tokens and can show significantly higher LVR when outcome token prices are at extreme probabilities (near 0 or 1).

**Loss-versus-Rebalancing (LVR)** is a crucial metric that quantifies the costs incurred by AMM liquidity providers due to adverse selection from arbitrageurs. It represents the potential loss for LPs compared to an idealized "rebalancing portfolio" that actively trades to maintain an optimal position. LVR is a form of Maximal Extractable Value (MEV), where arbitrageurs profit by exploiting stale prices in an AMM relative to other trading venues. The pm-AMM specifically aims to minimize LVR, thereby enhancing liquidity provision and improving returns for LPs.

## Key Excerpts

1. "The pm-AMM concentrates more liquidity around a 50% probability and less at extreme price points. This design is intended to make liquidity provision more predictable and less risky for liquidity providers (LPs)."

2. "LVR is a form of Maximal Extractable Value (MEV), where arbitrageurs profit by exploiting stale prices in an AMM relative to other trading venues. The pm-AMM specifically aims to minimize LVR."

3. "While constant geometric mean market makers (like Uniswap) are uniform AMMs for assets following geometric Brownian motion, they are not for assets, like prediction market outcome tokens, that follow Gaussian score dynamics. The static pm-AMM is designed to be a uniform AMM for these outcome tokens."

## Scrape Notes
- Full page content could not be extracted due to JS rendering (Cloudflare/access gate)
- Content reconstructed from web search results and related citations
- Paper also discussed in arxiv context (different from 2411.08972 which is a separate SODA'25 paper)
