# Key Findings: Prediction Market Trading Strategies

**Total Findings:** 15
**Ranking:** By importance (critical → high → medium) and confidence (high → medium → low)

---

## Critical Findings

### 1. Fractional Kelly Criterion Is the Consensus Position-Sizing Framework
**Confidence:** High | **Sources:** 5

Five independent assets converge on fractional Kelly (α × f*) as the optimal position-sizing approach for prediction markets. The simplified formula f* = (p - q) / (1 - q) with Brier-tiered alpha (0.10–0.40) automatically scales positions based on model accuracy. Half Kelly (α=0.5) delivers 75% of optimal growth at 25% of the variance — a critical property for autonomous systems where probability estimates carry model uncertainty.

- kelly-criterion-polymarket-bot: Full production implementation with Brier-tiered alpha
- navnoorbawa-prediction-markets-math: Theoretical derivation with worked examples
- arxiv-kelly-prediction-markets: Academic backing via KL-divergence error analysis
- prediction-market-amm-with-kelly: Python implementation with bankroll management
- kelly-criterion-risk: Drawdown mode integration (yellow at 12%+, red for halt)

### 2. Polymarket's AMM→CLOB Migration Fundamentally Changed Market Microstructure
**Confidence:** High | **Sources:** 4

Polymarket's 2023 migration from LMSR-based AMM to a hybrid-decentralized CLOB shifted the competitive landscape. Under LMSR, the protocol was the market maker with bounded loss (b × ln(n)). Under CLOB, participants must provide their own liquidity, creating a competitive market-making environment where edge comes from speed, capital, and superior pricing rather than mechanism design.

- medium-lmsr-math: Documents the migration and its implications
- polymarket-clob-introduction: CLOB architecture details (EIP-712, HMAC-SHA256 auth)
- polymarket-ctf-overview: CTF token layer remains unchanged under CLOB
- navnoorbawa-prediction-markets-math: CLOB vs AMM comparative analysis

### 3. Cross-Platform Arbitrage Yields 1–3% Risk-Free Returns and Persists
**Confidence:** High | **Sources:** 3

Price divergences between Polymarket, Kalshi, and PredictIt create arbitrage opportunities of 1–3% per trade by buying YES on one platform and NO on another when combined cost < $1.00. Counter-intuitively, these inefficiencies *increased* during the 2024 US elections' final weeks, when volume was highest. Persistence factors: retail-dominated markets, platform fragmentation, thin liquidity, and high cross-platform latency.

- navnoorbawa-prediction-markets-math: Worked example — Polymarket YES $0.42 + Kalshi NO $0.56 = $0.98 → $0.02 profit (2.04%)
- medium-lmsr-math (arbitrage context): LMSR no-arbitrage invariant YES+NO=$1
- paradigm-pm-amm (arbitrage context): LVR quantifies arbitrage extraction from AMMs

### 4. Market Making on Polymarket Is Currently Unprofitable for Most Participants
**Confidence:** High | **Sources:** 3

Despite sophisticated optimization — maker reward formula S=((v-s)/v)², 95% cancellation reduction, position merging, and profitability scoring — competitive dynamics have compressed returns below viability. The warproxxx fork's explicit warning ("not profitable and will lose money") directly contradicts terrytrl100's more optimistic framing, with the divergence likely reflecting different capital levels and market conditions.

- terrytrl100-polymarket-automated-mm: Optimistic framing with reward optimization
- warproxxx-poly-maker: Explicit unprofitability warning
- hummingbot-inventory-risk: Inventory risk compounds the challenge

### 5. PM-AMM Solves CPMM's Guaranteed Loss But Introduces 50% Expected LVR
**Confidence:** High | **Sources:** 3

Paradigm's PM-AMM achieves uniform LVR (constant arbitrage cost regardless of price level) and time-decaying liquidity (L√(T-t)) that reduces exposure near binary resolution. This solves CPMM's guaranteed 100% loss at expiry. However, total expected LVR = V₀/2 means LPs lose 50% of initial capital to arbitrageurs over the market's lifetime, requiring fee income to substantially exceed this threshold.

- paradigm-pm-amm: Foundational paper with mathematical derivation
- apostlex0-prediction-market-amm: Morpheus implementation on Aptos
- paradigm-pm-amm-risk: LP risk quantification framework

---

## High-Priority Findings

### 6. The Probability Estimation Gap Is the Biggest Obstacle to Autonomous Trading
**Confidence:** High | **Sources:** gap-analysis + multiple

The research collection thoroughly covers position sizing (Kelly) and execution (CLOB API, market making) but has zero assets on probability estimation — the core capability an autonomous agent needs. No assets address: LLM-based forecasting, ensemble methods, polling aggregation, base rate analysis, or superforecasting techniques. This is the single biggest gap for building an autonomous system.

- gap-analysis: Section 3.1 (AI Agent Architectures) and Section 1.7 (AI/ML Probability Models)
- kelly-criterion-polymarket-bot: Assumes probability as input, doesn't generate it
- navnoorbawa-prediction-markets-math: Describes biases to exploit but not how to model probabilities

### 7. Behavioral Biases Create Systematic, Exploitable Mispricings
**Confidence:** Medium-High | **Sources:** 2

Two documented biases create persistent edge: longshot bias (retail overpays for events with P < 15%) and recency bias (prices overreact to recent news, showing negative autocorrelation in daily price changes). Volume distortions around events amplify these effects. An autonomous system could systematically fade extreme moves and sell overpriced longshots.

- navnoorbawa-prediction-markets-math: Documents longshot bias, recency bias, volume distortions
- hummingbot-inventory-risk: Trending markets (bias-driven) create asymmetric fill rates

### 8. The LMSR→PM-AMM Evolution Represents a Complete Pricing Mechanism Lineage
**Confidence:** High | **Sources:** 5

The research traces a clear evolution: Hanson's LMSR (2002) → Gnosis CTF AMMs → Polymarket CLOB (2023) → Paradigm PM-AMM (2024). Each step solved specific problems: LMSR solved the liquidity bootstrapping problem; CTF standardized token mechanics; CLOB enabled competitive pricing; PM-AMM addresses LP risk with uniform LVR. Understanding this lineage is essential for system design.

- gensyn-lmsr: LMSR foundations and bounded loss
- gnosis-conditional-tokens-market-makers: CTF standard implementation
- medium-lmsr-math: LMSR↔softmax equivalence and Python code
- paradigm-pm-amm: PM-AMM as the next evolution
- apostlex0-prediction-market-amm: PM-AMM production implementation

### 9. Polymarket's Technical Stack Enables Programmatic Trading via Three SDKs
**Confidence:** High | **Sources:** 4

Polymarket provides comprehensive API access: two-tier auth (L1 EIP-712 for credentials, L2 HMAC-SHA256 for trading), three wallet types (EOA, POLY_PROXY, GNOSIS_SAFE), and SDKs in TypeScript, Python, and Rust. The non-custodial design means the operator cannot execute unauthorized trades. WebSocket connections enable real-time order book monitoring.

- polymarket-clob-introduction: Full API architecture and authentication
- polymarket-docs: SDK quickstart and code examples
- terrytrl100-polymarket-automated-mm: Production bot using the API
- warproxxx-poly-maker: Another bot implementation using same API

### 10. Inventory Risk Is Amplified in Prediction Markets Due to Binary Resolution
**Confidence:** High | **Sources:** 3

Unlike traditional markets where assets can gradually converge, prediction market positions jump to exactly $0 or $1 at resolution. This makes inventory management uniquely critical — there is no gradual exit. Five mitigation strategies are documented: inventory skew, filled order delay (300s), hanging orders, ping pong, and one-sided spread adjustment. PM-AMM's time-decay provides theoretical mitigation at the AMM level.

- hummingbot-inventory-risk: Five mitigation strategies detailed
- paradigm-pm-amm-risk: PM-AMM time-decay as structural mitigation
- warproxxx-poly-maker: Position merging as practical mitigation

---

## Medium-Priority Findings

### 11. Platform Accuracy Varies Significantly — PredictIt 93% vs Polymarket 67% (2024 Elections)
**Confidence:** Low | **Sources:** 1

A single study of the 2024 US elections found substantial accuracy divergence: PredictIt 93%, Kalshi 78%, Polymarket 67%. However, this is one study on one event type. The accuracy gap may create arbitrage opportunities if it persists, but requires validation across more events and time periods.

- navnoorbawa-prediction-markets-math: Platform accuracy comparison data

### 12. The Softmax/LMSR Equivalence Bridges ML and Market Design
**Confidence:** High | **Sources:** 2

LMSR's pricing function is mathematically equivalent to the softmax function used in neural networks, with the liquidity parameter b acting as temperature. This creates a direct bridge between machine learning and market mechanism design, potentially enabling ML-native approaches to market making.

- gensyn-lmsr: Formal equivalence with Bregman divergences
- medium-lmsr-math: Python implementation demonstrating equivalence

### 13. The Gnosis CTF Standard Underpins Multiple Platforms
**Confidence:** High | **Sources:** 3

Gnosis's Conditional Token Framework (ERC-1155) is the foundational token standard used by Polymarket and implemented by other platforms. Understanding split/merge operations, collateralization, and resolution mechanics is prerequisite for any autonomous trading system operating across CTF-based markets.

- polymarket-ctf-overview: CTF mechanics in Polymarket context
- gnosis-conditional-tokens-market-makers: Original Gnosis implementation (134 stars, 57 forks)
- navnoorbawa-prediction-markets-math: CTF in theoretical framework

### 14. Drawdown-Adjusted Position Sizing Prevents Catastrophic Loss Spirals
**Confidence:** High | **Sources:** 2

Beyond fractional Kelly, production systems implement drawdown modes: green (normal trading), yellow (0.5x alpha multiplier at 12%+ drawdown), and red (complete halt). This creates a feedback loop where losses automatically reduce position sizes, preventing the tail-risk scenarios that theoretical Kelly underweights.

- kelly-criterion-polymarket-bot: Drawdown mode implementation
- kelly-criterion-risk: Drawdown as risk management layer

### 15. Open-Source Market Making Bots Provide Viable Starting Points But Require Significant Enhancement
**Confidence:** Medium | **Sources:** 3

Three open-source MM bots exist: terrytrl100/polymarket-automated-mm (Polymarket, sophisticated), warproxxx/poly-maker (Polymarket, realistic profitability assessment), and manifoldmarkets/market-maker (Manifold, simple EMA-based). These provide architecture templates but none incorporate probability estimation, cross-platform awareness, or adaptive strategy selection needed for autonomous operation.

- terrytrl100-polymarket-automated-mm: Most sophisticated, reward-optimized
- warproxxx-poly-maker: Most realistic about profitability
- manifold-market-maker: Simplest reference architecture

---

*All findings derived exclusively from the 23 enriched assets in this research collection.*
