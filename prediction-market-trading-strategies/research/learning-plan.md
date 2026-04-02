# Prediction Market Trading Strategies — Mastery Roadmap

## Topic Overview & Scope

This roadmap covers the full knowledge stack required to trade prediction markets profitably and systematically. Scope includes: probability fundamentals, market mechanics (Kalshi, Polymarket, Metaculus, PredictIt), pricing theory, risk management, quantitative modeling, information aggregation, portfolio construction, and advanced strategies (arbitrage, market-making, event-driven trading). The goal is to move from "curious beginner" to "consistent edge trader" who can size positions, manage risk, and exploit mispricings across prediction market platforms.

---

## Learning Domains

### 1. [BEGINNER] Probability & Bayesian Reasoning
- **Prerequisites:** None
- **Difficulty:** Beginner
- **Key Concepts:** Frequentist vs Bayesian probability, conditional probability, Bayes' theorem, base rates, calibration, probability distributions, expected value, law of large numbers
- **Mastery Criteria:** Can convert between odds formats, apply Bayes' theorem to update beliefs given new evidence, pass a calibration test (Brier score < 0.25 on 50+ questions), and explain why base rate neglect leads to bad trades
- **Estimated Time:** 8-12 hours

### 2. [BEGINNER] Prediction Market Mechanics & Platforms
- **Prerequisites:** None
- **Difficulty:** Beginner
- **Key Concepts:** How prediction markets work (binary, multi-outcome, scalar), order books vs AMMs, platform comparison (Kalshi, Polymarket, Robinhood Derivatives, PredictIt, Metaculus), fee structures, settlement rules, regulatory landscape (CFTC), contract specifications, liquidity dynamics
- **Mastery Criteria:** Can explain the difference between order-book and AMM-based markets, compare fee/margin structures across 3+ platforms, identify which platform is best for a given event type, and place trades on at least 2 platforms
- **Estimated Time:** 6-10 hours

### 3. [BEGINNER] Financial Markets Fundamentals
- **Prerequisites:** None
- **Difficulty:** Beginner
- **Key Concepts:** Bid/ask spreads, order types (market, limit, stop), time value, liquidity, slippage, margin, leverage, basic options concepts (calls, puts, payoffs), market microstructure basics
- **Mastery Criteria:** Can explain bid-ask spread impact on P&L, choose appropriate order types for different scenarios, calculate break-even prices including fees, and describe how liquidity affects execution quality
- **Estimated Time:** 8-12 hours

### 4. [INTERMEDIATE] Forecasting & Calibration
- **Prerequisites:** 1 (Probability & Bayesian Reasoning)
- **Difficulty:** Intermediate
- **Key Concepts:** Superforecasting techniques (Tetlock), reference class forecasting, decomposition methods, inside vs outside view, calibration training, Brier scores, log scoring, tracking forecast accuracy, cognitive debiasing, wisdom of crowds
- **Mastery Criteria:** Can produce calibrated probability estimates (calibration curve within 10% of ideal), maintain a forecast journal with tracked accuracy, apply at least 3 decomposition techniques to a novel question, and achieve top-quartile Brier score on a forecasting tournament or practice set
- **Estimated Time:** 15-20 hours

### 5. [INTERMEDIATE] Pricing Theory for Binary & Multi-Outcome Contracts
- **Prerequisites:** 1 (Probability), 3 (Financial Fundamentals)
- **Difficulty:** Intermediate
- **Key Concepts:** Fair value of binary contracts, implied probability extraction, overround/vig calculation, no-arbitrage pricing, time decay in event contracts, pricing multi-outcome markets, Dutch book arguments, efficient market hypothesis applied to prediction markets
- **Mastery Criteria:** Can derive fair value for a binary contract given a probability estimate, calculate implied probabilities from market prices, identify when a market is mispriced relative to a model, and explain the Dutch book theorem and its practical implications
- **Estimated Time:** 10-15 hours

### 6. [INTERMEDIATE] Information Sources & Research Methods
- **Prerequisites:** 2 (Market Mechanics), 4 (Forecasting)
- **Difficulty:** Intermediate
- **Key Concepts:** OSINT for prediction markets, polling data interpretation (538-style), economic indicator tracking, weather/climate data sources, political fundamentals analysis, sports analytics basics, news flow analysis, social media sentiment, data APIs and scraping, building an information edge
- **Mastery Criteria:** Can identify 3+ high-quality data sources for each major event category (politics, economics, weather, sports), build a systematic research workflow for a new market, distinguish signal from noise in polling data, and demonstrate an information advantage on at least one market category
- **Estimated Time:** 12-18 hours

### 7. [INTERMEDIATE] Risk Management & Bankroll Strategy
- **Prerequisites:** 1 (Probability), 3 (Financial Fundamentals)
- **Difficulty:** Intermediate
- **Key Concepts:** Kelly criterion (full and fractional), bankroll management, risk of ruin, position sizing, correlation risk, drawdown management, expected value vs variance tradeoff, unit sizing, stop-loss strategies for event contracts, diversification across uncorrelated markets
- **Mastery Criteria:** Can calculate Kelly-optimal position sizes, explain why fractional Kelly is preferred in practice, build a position-sizing spreadsheet, set bankroll rules that keep risk of ruin below 1%, and demonstrate proper sizing on a portfolio of 10+ positions
- **Estimated Time:** 10-14 hours

### 8. [ADVANCED] Quantitative Modeling for Prediction Markets
- **Prerequisites:** 4 (Forecasting), 5 (Pricing Theory), 7 (Risk Management)
- **Difficulty:** Advanced
- **Key Concepts:** Building probability models (logistic regression, ensemble methods), backtesting prediction models, feature engineering for event outcomes, Monte Carlo simulation, model calibration and validation, combining models with market prices, Bayesian updating models, time-series analysis for evolving markets
- **Mastery Criteria:** Can build and backtest a quantitative model for at least one event category, demonstrate positive expected value in backtests, implement a Bayesian updating pipeline that adjusts predictions as new data arrives, and document model assumptions and limitations
- **Estimated Time:** 20-30 hours

### 9. [ADVANCED] Arbitrage & Cross-Platform Strategies
- **Prerequisites:** 2 (Market Mechanics), 5 (Pricing Theory), 7 (Risk Management)
- **Difficulty:** Advanced
- **Key Concepts:** Cross-platform arbitrage identification, correlated market arbitrage, multi-outcome arbitrage (Dutch booking), execution risk, settlement risk, fee-adjusted arbitrage calculations, speed of execution, API-based trading, monitoring tools, regulatory constraints on multi-platform trading
- **Mastery Criteria:** Can identify arbitrage opportunities across 2+ platforms, calculate fee-adjusted profit for cross-platform trades, build or use a monitoring tool that alerts on arbitrage windows, execute at least 3 profitable arbitrage trades, and document the risks (settlement, execution, regulatory)
- **Estimated Time:** 15-20 hours

### 10. [ADVANCED] Portfolio Construction & Correlation Management
- **Prerequisites:** 7 (Risk Management), 8 (Quantitative Modeling)
- **Difficulty:** Advanced
- **Key Concepts:** Portfolio theory applied to prediction markets, correlation estimation between event outcomes, hedging strategies, sector/theme concentration risk, tail risk management, rebalancing strategies, portfolio-level Kelly, exposure monitoring, max drawdown constraints
- **Mastery Criteria:** Can construct a diversified prediction market portfolio with explicit correlation assumptions, implement portfolio-level position limits, demonstrate hedging a concentrated position, and track portfolio-level metrics (Sharpe-equivalent, max drawdown, return on capital)
- **Estimated Time:** 12-18 hours

### 11. [ADVANCED] Market Making & Liquidity Provision
- **Prerequisites:** 5 (Pricing Theory), 7 (Risk Management), 9 (Arbitrage)
- **Difficulty:** Advanced
- **Key Concepts:** Market-making theory, bid-ask spread setting, inventory risk, adverse selection, providing liquidity on order-book platforms, AMM liquidity provision (Polymarket), impermanent loss, dynamic spread adjustment, automated market-making strategies
- **Mastery Criteria:** Can explain the market-maker's edge and risks, set up a basic market-making strategy on one platform, calculate expected P&L from spread capture vs adverse selection, and manage inventory risk over a multi-day period
- **Estimated Time:** 15-20 hours

### 12. [ADVANCED] Event-Driven & Catalyst Trading
- **Prerequisites:** 6 (Information Sources), 8 (Quantitative Modeling)
- **Difficulty:** Advanced
- **Key Concepts:** Trading around scheduled events (elections, economic releases, court decisions), pre-event positioning, volatility around catalysts, news-driven rapid repricing, building event playbooks, live trading during events, partial information trading, exit timing
- **Mastery Criteria:** Can build an event playbook for 3+ event types, demonstrate pre-event positioning with clear thesis, execute trades during live events with predefined triggers, and track P&L attribution to event-driven vs baseline strategies
- **Estimated Time:** 12-18 hours

### 13. [EXPERT] Algorithmic & Automated Trading Systems
- **Prerequisites:** 8 (Quantitative Modeling), 9 (Arbitrage), 11 (Market Making)
- **Difficulty:** Expert
- **Key Concepts:** API integration with prediction market platforms, automated signal generation, execution algorithms, monitoring and alerting, backtesting infrastructure, paper trading, production deployment, error handling and circuit breakers, latency optimization, regulatory compliance for automated trading
- **Mastery Criteria:** Can build and deploy an automated trading system that connects to at least one platform API, executes trades based on model signals, includes risk limits and circuit breakers, runs in production for 30+ days, and generates auditable logs
- **Estimated Time:** 30-40 hours

### 14. [EXPERT] Behavioral Edge & Market Psychology
- **Prerequisites:** 4 (Forecasting), 10 (Portfolio Construction)
- **Difficulty:** Expert
- **Key Concepts:** Cognitive biases in prediction markets (anchoring, recency, availability), narrative-driven mispricing, crowd psychology, contrarian strategies, identifying when markets are driven by sentiment vs information, long-shot bias, favorite-longshot bias, herding behavior, exploiting systematic biases
- **Estimated Time:** 10-15 hours
- **Mastery Criteria:** Can identify 5+ systematic biases present in prediction market pricing, build a strategy that explicitly targets one behavioral bias, demonstrate historical examples of bias-driven mispricings, and maintain a bias journal tracking instances in live markets

### 15. [EXPERT] Strategy Integration & Performance Measurement
- **Prerequisites:** 10 (Portfolio Construction), 12 (Event-Driven), 13 (Algorithmic Systems), 14 (Behavioral Edge)
- **Difficulty:** Expert
- **Key Concepts:** Multi-strategy portfolio management, performance attribution, Sharpe ratio and alternatives for prediction markets, tax implications, regulatory compliance, scaling strategies, capital allocation across strategies, reviewing and improving systems, building a trading journal, compounding and reinvestment
- **Mastery Criteria:** Can run a multi-strategy prediction market operation with clear performance attribution, achieve positive risk-adjusted returns over 90+ days of tracked trading, maintain a comprehensive trading journal, produce a quarterly performance review with actionable improvements, and articulate a personal trading philosophy
- **Estimated Time:** 20-30 hours

---

## Dependency Graph

```
1. Probability ─────────┬──> 4. Forecasting ──────────┬──> 8. Quant Modeling ────┬──> 10. Portfolio ──────> 15. Integration
                        │                              │                         │
                        │   ┌──> 5. Pricing ───────────┤──> 9. Arbitrage ────────┤──> 11. Market Making ──> 13. Algo Systems
                        │   │                          │                         │                              │
2. Market Mechanics ────┼───┤                          ├──> 6. Info Sources ─────┤──> 12. Event-Driven ────────┤
                        │   │                          │                         │                              │
3. Financial Fundamentals┘  └──> 7. Risk Management ───┘                        └──> 14. Behavioral Edge ─────┘
                                                                                                               │
                                                                                                               v
                                                                                                        15. Strategy Integration
```

### Prerequisite Relationships (flat list):
- 1 -> 4, 5, 7
- 2 -> 6, 9
- 3 -> 5, 7
- 4 -> 6, 8, 14
- 5 -> 8, 9, 11
- 6 -> 12
- 7 -> 8, 9, 10, 11
- 8 -> 10, 12, 13
- 9 -> 11, 13
- 10 -> 14, 15
- 11 -> 13
- 12 -> 15
- 13 -> 15
- 14 -> 15

---

## Cross-Cutting Themes

1. **Calibration & Intellectual Honesty:** Every domain requires honest assessment of uncertainty. From basic probability to expert strategy integration, calibration is the meta-skill.
2. **Edge Identification & Exploitation:** The core question across all domains: "Where is my edge, and how do I exploit it without it decaying?"
3. **Risk-Reward Tradeoff:** Position sizing, bankroll management, and variance control appear in every domain from beginner to expert.
4. **Data-Driven Decision Making:** Quantitative rigor, backtesting, and evidence-based reasoning thread through forecasting, modeling, and strategy evaluation.
5. **Platform & Regulatory Awareness:** Fee structures, settlement rules, and regulatory constraints affect every trading strategy and must be considered at every level.
6. **Psychological Discipline:** Managing emotions, avoiding tilt, maintaining process over outcome thinking, and recognizing your own biases.

---

## Research Priorities

1. **Start with the three foundation domains in parallel** (Probability, Market Mechanics, Financial Fundamentals) as they have no prerequisites.
2. **Forecasting & Calibration is the highest-leverage intermediate domain** — it unlocks 4 downstream domains and is the core differentiator for prediction market traders.
3. **Risk Management is the safety-critical path** — without it, all other knowledge leads to ruin. Prioritize it alongside or immediately after foundations.
4. **Quantitative Modeling is the gateway to advanced strategies** — it's the most time-intensive domain and the bottleneck for algorithmic approaches.
5. **Strategy Integration is the capstone** — only meaningful after significant experience in multiple advanced domains.
