# Executive Summary: Prediction Market Trading Strategies

**Research Compiled:** March 31, 2026
**Purpose:** Foundation for Autonomous Agentic Trading System Design
**Assets Analyzed:** 23 enriched sources across 6 research targets

---

## Overview

This research compendium synthesizes 23 enriched assets spanning academic papers, open-source codebases, platform documentation, and practitioner analyses to map the current landscape of prediction market trading strategies. The goal: identify viable approaches for building an autonomous agentic trading system targeting prediction markets in 2026.

## Key Findings

**1. Polymarket dominates the infrastructure landscape, but its CLOB architecture creates both opportunity and challenge.** Polymarket's 2023 migration from LMSR-based AMM to a hybrid-decentralized Central Limit Order Book fundamentally changed market microstructure (polymarket-clob-introduction, medium-lmsr-math). The CLOB enables sophisticated order strategies but demands low-latency infrastructure and sophisticated market-making logic that was unnecessary under AMM pricing.

**2. The Kelly criterion is the strongest consensus framework for position sizing.** Five independent sources converge on fractional Kelly (0.25x–0.5x full Kelly) as the optimal approach, with Brier-score-tiered alpha providing automatic risk adjustment based on model accuracy (kelly-criterion-polymarket-bot, navnoorbawa-prediction-markets-math, arxiv-kelly-prediction-markets, prediction-market-amm-with-kelly). Half Kelly delivers 75% of optimal growth at only 25% of the variance — a compelling tradeoff for autonomous systems.

**3. Cross-platform arbitrage offers 1–3% risk-free returns but remains underexploited.** Price divergences persist between Polymarket, Kalshi, and PredictIt due to retail-dominated participation, platform fragmentation, and thin liquidity (navnoorbawa-prediction-markets-math). These inefficiencies increased — not decreased — during high-volume periods like the 2024 US elections, contradicting efficient market assumptions.

**4. Market making on Polymarket is intensely competitive and likely unprofitable for new entrants.** The terrytrl100 and warproxxx poly-maker implementations reveal a stark reality: despite sophisticated reward optimization (maker reward formula S=((v-s)/v)²) and 95% cancellation reduction, the warproxxx fork explicitly warns "this bot is not profitable and will lose money" in the current market. Competition has compressed spreads beyond viability for capital-constrained operators.

**5. PM-AMM represents the theoretical frontier but is not yet deployed on major platforms.** Paradigm's PM-AMM introduces uniform LVR (Loss-vs-Rebalancing) and time-decaying liquidity — solving the fundamental flaw of CPMM guaranteed loss at binary resolution (paradigm-pm-amm, apostlex0-prediction-market-amm). However, the 50% expected capital loss to arbitrageurs (total LVR = V₀/2) means fees must substantially exceed this threshold for profitable LP operation.

## Major Themes

The research clusters around five primary themes: (1) the evolution of AMM pricing from LMSR to PM-AMM, (2) Kelly criterion as the unifying position-sizing framework, (3) Polymarket's technical infrastructure as the dominant trading venue, (4) behavioral biases creating exploitable inefficiencies, and (5) the gap between theoretical frameworks and production-ready autonomous systems.

## Critical Gaps

The most significant gap is the absence of AI/ML probability estimation models — multiple sources cover *how to size positions given a probability estimate* but none address *how to build superior probability models*. For an autonomous agent, the probability estimation pipeline is arguably more important than the execution layer. Additional gaps include: no backtesting frameworks or historical performance data, no coverage of multi-outcome markets (N>2), limited academic foundational papers, and no Kalshi API documentation.

## Recommendations

For an autonomous trading system, we recommend prioritizing: (1) a fractional Kelly position-sizing engine with Brier-score feedback, (2) cross-platform arbitrage detection between Polymarket and Kalshi as the lowest-risk entry strategy, (3) an LLM-augmented probability estimation pipeline as the primary source of edge, and (4) Polymarket CLOB API integration using their TypeScript or Python SDK. Market making should be deprioritized given current competitive dynamics unless substantial capital (>$100K) is available.

**Overall Confidence: 7/10** — Strong coverage of pricing mechanisms, position sizing, and platform infrastructure. Weakened by gaps in probability estimation, backtesting data, and multi-platform technical details.

---

*This summary is based exclusively on the 23 enriched assets collected during this research cycle. No external knowledge was used.*
