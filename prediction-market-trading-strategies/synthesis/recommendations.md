# Recommendations: Prediction Market Trading Strategies

---

## Immediate Actions (Do Now)

### 1. Build a Fractional Kelly Position-Sizing Engine
**Priority:** Critical | **Based on:** kelly-criterion-polymarket-bot, prediction-market-amm-with-kelly, navnoorbawa-prediction-markets-math

Implement the production-tested fractional Kelly system with:
- Core formula: f* = (p - q) / (1 - q) for binary markets
- Brier-tiered alpha: α = 0.40 (Brier <0.18), 0.25 (0.18–0.22), 0.20 (0.22–0.26), 0.10 (>0.26)
- Drawdown modes: green (normal), yellow (0.5x alpha at 12%+ drawdown), red (halt)
- 3% fee adjustment for Polymarket wins
- Minimum 100 predictions before live trading
- Use the joicodev PositionSizer as reference implementation

### 2. Integrate Polymarket CLOB API
**Priority:** Critical | **Based on:** polymarket-clob-introduction, polymarket-docs, terrytrl100-polymarket-automated-mm

Set up programmatic access using:
- Python SDK (py-clob-client) or TypeScript SDK (@polymarket/clob-client)
- L1 auth (EIP-712) for credential derivation, L2 auth (HMAC-SHA256) for trading
- WebSocket connections for real-time order book monitoring
- Reference terrytrl100's poly-maker for production patterns (order management, cancellation logic, position merging)

### 3. Implement Cross-Platform Arbitrage Detection
**Priority:** High | **Based on:** navnoorbawa-prediction-markets-math

Build a monitor that:
- Tracks identical events across Polymarket and Kalshi
- Flags when YES(Platform A) + NO(Platform B) < $1.00
- Targets 1–3% risk-free returns per arbitrage cycle
- Accounts for platform fees, settlement delays, and capital lockup
- Starts with monitoring-only mode to measure opportunity frequency

### 4. Set Up Position Merging Infrastructure
**Priority:** High | **Based on:** terrytrl100-polymarket-automated-mm, warproxxx-poly-maker

Implement automated position merging (YES + NO → collateral recovery) with:
- Configurable threshold (start at $20 as in poly-maker)
- Capital efficiency tracking
- Integration with the Kelly engine for reinvestment decisions

---

## Strategic Considerations (Design Decisions)

### 5. Prioritize Directional Trading Over Market Making
**Rationale:** warproxxx-poly-maker, terrytrl100-polymarket-automated-mm, hummingbot-inventory-risk

Market making on Polymarket is intensely competitive and likely unprofitable without substantial capital (>$100K). Directional trading via Kelly criterion exploits informational edge rather than speed/capital edge. Focus system design on:
- Superior probability estimation (the alpha source)
- Position sizing (Kelly manages risk)
- Patient execution (avoid market impact)

Market making should only be considered for illiquid markets or as a liquidity provision strategy for markets where the agent has high-confidence probability estimates.

### 6. Design for Multi-Platform Architecture from Day One
**Rationale:** navnoorbawa-prediction-markets-math, gap-analysis

Even if starting with Polymarket only, architect the system with platform abstraction:
- Unified market representation (event + outcome + probability + platform)
- Platform-agnostic position tracking
- Cross-platform arbitrage as a first-class strategy
- Add Kalshi integration as the immediate next platform (CFTC-regulated, different user base, arbitrage opportunities)

### 7. Build the Probability Estimation Pipeline as the Core Differentiator
**Rationale:** gap-analysis (Section 1.7, 3.1), kelly-criterion-polymarket-bot

The entire collected research treats probability as exogenous. The autonomous agent's primary edge must come from superior probability estimation. Consider:
- LLM-based event analysis and probability generation
- Ensemble methods combining multiple model outputs
- Calibration tracking via Brier scores (already integrated with Kelly alpha)
- Base rate databases for common event types
- News/social media sentiment as probability adjustment signals

### 8. Account for PM-AMM's Potential Market Impact
**Rationale:** paradigm-pm-amm, apostlex0-prediction-market-amm

PM-AMM is not yet deployed on major platforms but represents the theoretical frontier. If adopted:
- LP risk becomes calculable (total LVR = V₀/2)
- Market making dynamics fundamentally change
- Arbitrage between PM-AMM and CLOB platforms creates new opportunities
- Design the system to handle both CLOB and AMM interfaces

---

## Further Research Priorities

### 9. [CRITICAL] AI/ML Probability Estimation Methods
**Gap:** No assets cover probability model construction
**Action:** Research LLM-based forecasting (ForecastBench), superforecasting techniques, ensemble methods, polling aggregation, and base rate analysis. This is the #1 research priority.

### 10. [CRITICAL] Kalshi API Technical Documentation
**Gap:** No Kalshi API docs despite being a major platform and arbitrage target
**Action:** Scrape Kalshi developer documentation, authentication patterns, order types, and settlement mechanics. Essential for cross-platform arbitrage.

### 11. [HIGH] Backtesting Framework and Historical Data
**Gap:** No backtesting code or historical performance data
**Action:** Build or find a prediction market backtesting framework. Collect historical price/resolution data from Polymarket and Kalshi. Validate Kelly and arbitrage strategies against real data before live deployment.

### 12. [HIGH] Portfolio-Level Risk Management
**Gap:** Only individual position/bet risk covered
**Action:** Research portfolio VaR for prediction markets, correlation between markets (e.g., political events cluster), maximum drawdown limits across all positions, and diversification strategies. Kelly alone doesn't prevent correlated losses.

### 13. [HIGH] Multi-Outcome Market Strategies
**Gap:** All content focuses on binary (YES/NO) markets
**Action:** Research LMSR for N>2 outcomes, combinatorial market strategies, and conditional market approaches. Multi-outcome markets may have less competition and more inefficiency.

### 14. [MEDIUM] Oracle Dispute and Resolution Risk Analysis
**Gap:** UMA oracle described but no failure analysis
**Action:** Analyze historical UMA disputes on Polymarket, dispute rates, manipulation attempts, and resolution delays. Critical for risk management near market resolution.

### 15. [MEDIUM] Transaction Cost and Fee Optimization
**Gap:** Minimal coverage of gas costs and fee impact
**Action:** Quantify Polygon gas costs, Polymarket fee schedules (3% on wins confirmed), and their impact on strategy profitability at different capital levels. Determine minimum viable capital for each strategy.

### 16. [MEDIUM] Academic Foundational Papers
**Gap:** Only one academic paper abstract scraped
**Action:** Obtain Hanson (2002/2003) LMSR papers, Arrow-Debreu securities theory, Manski (2006) on interpretation, Wolfers & Zitzewitz survey. These provide theoretical grounding for the system.

---

## Monitoring Targets (Watch Ongoing)

### 17. PM-AMM Platform Adoption
Monitor whether Polymarket, Kalshi, or new platforms adopt PM-AMM. This would fundamentally change market-making economics and create transitional arbitrage opportunities.

### 18. Polymarket Competition Intensity
Track spread compression, maker reward changes, and bot population growth. If spreads continue tightening, market making becomes even less viable; if new reward programs launch, temporary opportunities may emerge.

### 19. Regulatory Developments
Track CFTC decisions on prediction market regulation, especially after the October 2024 DC Circuit ruling allowing Kalshi political contracts. Regulatory changes could open new markets or restrict existing ones.

### 20. Cross-Platform Arbitrage Window Frequency
Build monitoring to measure: how often arbitrage windows open, average window duration, average return per window, and whether frequency is increasing or decreasing. This data is essential for deciding whether to operationalize the arbitrage strategy.

### 21. LLM Forecasting Accuracy Benchmarks
Track ForecastBench and similar benchmarks for LLM prediction accuracy. As models improve, the probability estimation pipeline becomes more viable and the system's edge grows.

---

## Summary Matrix

| # | Recommendation | Type | Priority | Confidence |
|---|---|---|---|---|
| 1 | Fractional Kelly engine | Immediate | Critical | High |
| 2 | Polymarket CLOB API | Immediate | Critical | High |
| 3 | Cross-platform arbitrage detection | Immediate | High | High |
| 4 | Position merging | Immediate | High | High |
| 5 | Directional over market making | Strategic | Critical | High |
| 6 | Multi-platform architecture | Strategic | High | High |
| 7 | Probability estimation pipeline | Strategic | Critical | High |
| 8 | PM-AMM readiness | Strategic | Medium | Medium |
| 9 | AI/ML probability research | Research | Critical | High |
| 10 | Kalshi API docs | Research | Critical | High |
| 11 | Backtesting framework | Research | High | High |
| 12 | Portfolio risk management | Research | High | Medium |
| 13 | Multi-outcome strategies | Research | High | Medium |
| 14 | Oracle risk analysis | Research | Medium | Medium |
| 15 | Fee optimization | Research | Medium | High |
| 16 | Academic papers | Research | Medium | High |
| 17 | PM-AMM adoption | Monitor | Medium | - |
| 18 | Competition intensity | Monitor | High | - |
| 19 | Regulatory changes | Monitor | High | - |
| 20 | Arbitrage frequency | Monitor | High | - |
| 21 | LLM forecasting benchmarks | Monitor | Medium | - |

---

*21 recommendations derived from 23 enriched assets and gap analysis. All recommendations grounded in specific source evidence.*
