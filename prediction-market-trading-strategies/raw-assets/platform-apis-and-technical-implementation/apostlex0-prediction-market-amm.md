# Morpheus: Prediction Market AMM on Aptos

## Metadata
- **URL:** https://github.com/Apostlex0/PredictionMarket_AMM
- **Source:** GitHub
- **Type:** code
- **Author:** Apostlex0
- **Date Scraped:** 2026-04-01
- **Authority:** medium
- **Relevance:** medium

## Content

## Overview

Morpheus is an open-source implementation of Paradigm's Prediction Market Automated Market Maker (PM-AMM), built on the Aptos blockchain using the Move language. It addresses the shortcomings of traditional AMMs for prediction markets by providing a capital-efficient and mathematically sound framework for trading binary outcome tokens.

## Core Problem with Standard AMMs

Standard Constant Product Market Makers (CPMMs) with their x × y = k invariant are poorly suited for prediction markets:

**Guaranteed Loss at Expiration**: At expiration, one token becomes worthless. Arbitrageurs drain the valuable tokens from the pool, leaving LPs with a portfolio of zero-value assets.

**Inefficient Liquidity Profile**: CPMMs provide liquidity across an infinite price range, which is inefficient for outcome tokens priced between 0 and 1. They fail to account for changing volatility as markets approach expiration.

## PM-AMM Solution: Gaussian Score Dynamics

The PM-AMM uses a model called Gaussian score dynamics. This model assumes the outcome score (e.g., vote margin) follows Brownian motion, and the token price equals the probability the score exceeds a threshold. This is analogous to the Black-Scholes model for binary options.

### Static PM-AMM Invariant

The trading curve is defined by:

(y - x)Φ((y - x)/L) + Lφ((y - x)/L) - y = 0

Where:
- x = AMM reserve of YES token
- y = AMM reserve of NO token
- L = liquidity parameter (scales pool depth)
- Φ = standard normal CDF
- φ = standard normal PDF

This concentrates liquidity around 50% probability, withdrawing it from dangerous extreme price zones.

### Dynamic PM-AMM

Extends the static model by making the liquidity parameter a function of time: L_t = L_0√(T - t)

As expiration approaches, liquidity automatically decreases, reducing LP exposure during the highest-risk phase.

### Loss-vs-Rebalancing (LVR)

The key risk metric for PM-AMM. It quantifies value extracted by arbitrageurs trading against stale prices. Remarkably, for a dynamic PM-AMM, total expected LVR = V_0/2 — LPs can expect to lose exactly half their initial capital.

## Key Excerpts

1. "The PM-AMM uses Gaussian score dynamics — analogous to Black-Scholes for binary options — allowing quantitative, model-driven AMM design."

2. "Total expected LVR for a dynamic PM-AMM equals V_0/2 — LPs can expect to lose exactly half their initial capital over the market's lifetime."

3. "The PM-AMM concentrates liquidity around 50% probability and provides less liquidity at extreme probabilities (near 0% or 100%), rationally withdrawing from dangerous zones."

## Scrape Notes
- Content completeness: full (very detailed README with mathematical derivations)
- Excellent resource for understanding PM-AMM mechanism design
- Key reference for mechanism designers building prediction market AMMs
