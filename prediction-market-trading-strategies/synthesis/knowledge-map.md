# Knowledge Map: Prediction Market Trading Strategies

## Overview

This knowledge map inventories all unique concepts across 15 domains, organized by difficulty level and domain. Each concept includes its prerequisites and cross-domain connections.

---

## Section 1: Foundations (Beginner)

### Domain 1: Probability & Bayesian Reasoning
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 1.1 | Probability Fundamentals (sample spaces, events, axioms) | Basic algebra | Pricing Theory (no-arbitrage), All domains |
| 1.2 | Frequentist vs. Bayesian Interpretation | 1.1 | Forecasting (reference class), Quant Modeling |
| 1.3 | Conditional Probability & Independence | 1.1 | Arbitrage (correlated markets), Portfolio (correlation) |
| 1.4 | Bayes' Theorem (formula, odds form, sequential updating) | 1.3 | Forecasting (Bayesian updating), Info Sources, Quant Modeling |
| 1.5 | Base Rates & Base Rate Neglect | 1.4 | Forecasting (reference class), Behavioral Edge |
| 1.6 | Odds Formats & Conversion | 1.1 | Market Mechanics (platform comparison), Pricing Theory |
| 1.7 | Expected Value (EV) | 1.1 | Risk Management (Kelly), All trading domains |
| 1.8 | Probability Distributions (Bernoulli, Beta, Normal, etc.) | 1.1 | Quant Modeling (Monte Carlo), Portfolio (VaR) |
| 1.9 | Calibration & Brier Score | 1.4 | Forecasting (calibration training), Quant Modeling (scoring) |
| 1.10 | Proper Scoring Rules (Brier, Log Score) | 1.9 | Forecasting, Quant Modeling (model evaluation) |
| 1.11 | Common Probability Fallacies | 1.1 | Behavioral Edge (cognitive biases) |

### Domain 2: Prediction Market Mechanics & Platforms
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 2.1 | Binary Contracts (Yes/No) | None | Pricing Theory, All trading domains |
| 2.2 | Multi-Outcome Contracts | 2.1 | Pricing Theory (LMSR), Arbitrage (Dutch booking) |
| 2.3 | Scalar (Range) Contracts | 2.1 | Quant Modeling, Pricing Theory |
| 2.4 | Order Book Trading Mechanism | None | Market Making, Arbitrage, Algorithtic Systems |
| 2.5 | Automated Market Makers (AMM/LMSR) | None | Market Making, Pricing Theory |
| 2.6 | Liquidity & Market Depth | 2.4 | Market Making, Risk Management, Arbitrage |
| 2.7 | Bid-Ask Spread | 2.4 | Financial Fundamentals, Market Making |
| 2.8 | Order Types (Market, Limit, Maker/Taker) | 2.4 | Financial Fundamentals, Algorithmic Systems |
| 2.9 | Settlement & Resolution | 2.1 | Event-Driven Trading, Risk Management |
| 2.10 | Oracle Mechanisms (Decentralized) | 2.9 | Arbitrage (settlement risk) |
| 2.11 | Platform Comparison (Kalshi, Polymarket, PredictIt, Robinhood) | 2.1-2.8 | Arbitrage (cross-platform), All trading domains |
| 2.12 | CFTC Regulation & Legal Framework | None | Arbitrage (regulatory constraints), Risk Management |
| 2.13 | Price as Probability | 1.1, 2.1 | Pricing Theory, Forecasting |
| 2.14 | Contract Specifications & Resolution Criteria | 2.9 | Event-Driven Trading, Info Sources |

### Domain 3: Financial Markets Fundamentals
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 3.1 | Bid-Ask Spread (detailed) | None | Market Making, Pricing Theory |
| 3.2 | Order Types (detailed: market, limit, stop, stop-limit) | None | Algorithmic Systems, Market Making |
| 3.3 | Maker vs. Taker Dynamics | 3.2 | Market Making, Platform fees |
| 3.4 | Liquidity (depth, breadth, resilience) | 3.1 | Market Making, Risk Management |
| 3.5 | Slippage | 3.4 | Arbitrage, Algorithmic Systems |
| 3.6 | Transaction Costs & Fee Structures | 3.1-3.5 | All trading domains |
| 3.7 | Break-Even Price Calculation | 3.6 | Pricing Theory, Risk Management |
| 3.8 | Time Value of Money | None | Pricing Theory (time decay), Portfolio |
| 3.9 | Margin & Leverage | None | Risk Management, Portfolio |
| 3.10 | Basic Options Concepts (analogy to prediction contracts) | None | Pricing Theory (binary options models) |
| 3.11 | Market Microstructure | 3.1-3.5 | Market Making, Algorithmic Systems |
| 3.12 | Volatility | 3.11 | Pricing Theory, Event-Driven Trading |
| 3.13 | Order Book & Price Levels | 3.1, 3.2 | Market Making, Algorithmic Systems |

---

## Section 2: Core Methods (Intermediate)

### Domain 4: Forecasting & Calibration
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 4.1 | Superforecasting Fundamentals (fox vs. hedgehog, triage) | 1.4, 1.5 | Behavioral Edge, Info Sources |
| 4.2 | Reference Class Forecasting (outside view, base rate estimation) | 1.5 | Info Sources, Event-Driven Trading |
| 4.3 | Decomposition Methods (Fermi, scenario trees, factor decomposition) | 1.7 | Quant Modeling, Event-Driven Trading |
| 4.4 | Inside vs. Outside View Integration | 4.2, 4.3 | All analysis domains |
| 4.5 | Calibration (overconfidence, calibration curves) | 1.9 | Quant Modeling (model calibration), Behavioral Edge |
| 4.6 | Scoring Rules (Brier decomposition, log score, CRPS) | 1.10 | Quant Modeling, Strategy Integration |
| 4.7 | Cognitive Debiasing (anchoring, confirmation, pre-mortem, red teaming) | 4.5 | Behavioral Edge, Strategy Integration |
| 4.8 | Wisdom of Crowds (aggregation, extremizing, cascades) | 1.4 | Behavioral Edge (herding), Market Mechanics |

### Domain 5: Pricing Theory for Binary & Multi-Outcome Contracts
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 5.1 | Fair Value Derivation from Probability | 1.7 | All trading domains |
| 5.2 | Implied Probability Extraction | 1.6, 2.13 | Arbitrage, Market Making |
| 5.3 | Overround (Vig) Calculation & Removal | 5.2 | Arbitrage, Market Making |
| 5.4 | No-Arbitrage Pricing Principle | 1.1, 5.1 | Arbitrage (Dutch booking) |
| 5.5 | Risk-Neutral Pricing | 5.1, 3.8 | Quant Modeling |
| 5.6 | Time Decay (Theta) in Binary Contracts | 5.1, 3.8 | Event-Driven Trading, Market Making |
| 5.7 | Volatility & Binary Contract Pricing | 3.12, 5.1 | Event-Driven Trading, Market Making |
| 5.8 | Binary Options Pricing Models (Black-Scholes, Binomial, Monte Carlo) | 5.5, 1.8 | Quant Modeling |
| 5.9 | Multi-Outcome Market Pricing | 2.2, 5.4 | Arbitrage, Market Making |
| 5.10 | LMSR (Logarithmic Market Scoring Rule) | 2.5, 5.9 | Market Making |
| 5.11 | Dutch Book Theorem | 1.1, 5.4 | Arbitrage |
| 5.12 | Mispricing Identification | 5.1-5.3 | All trading domains |
| 5.13 | Favorite-Longshot Bias | 5.12 | Behavioral Edge |
| 5.14 | Spread & Transaction Cost Impact on Fair Value | 3.6, 5.1 | All trading domains |

### Domain 6: Information Sources & Research Methods
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 6.1 | Resolution Criteria Analysis | 2.14 | Event-Driven Trading, Arbitrage |
| 6.2 | Base Rate Estimation for Markets | 4.2 | Forecasting, Quant Modeling |
| 6.3 | Signal vs. Noise in Polling Data | 4.1 | Event-Driven Trading, Behavioral Edge |
| 6.4 | Data Source Tiering by Event Category | None | All analysis domains |
| 6.5 | Cross-Market Correlation Analysis | 1.3, 2.11 | Arbitrage, Portfolio Construction |
| 6.6 | Systematic Research Workflow | 6.1-6.5 | Event-Driven Trading, Strategy Integration |
| 6.7 | Information Advantage Assessment | 6.6 | All trading domains |

### Domain 7: Risk Management & Bankroll Strategy
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 7.1 | Expected Value & Edge | 1.7, 5.12 | All trading domains |
| 7.2 | Kelly Criterion (Full) | 7.1, 1.8 | Portfolio, Algorithmic Systems |
| 7.3 | Fractional Kelly | 7.2 | Portfolio, Behavioral Edge (psychological sustainability) |
| 7.4 | Risk of Ruin | 7.2 | Portfolio, Strategy Integration |
| 7.5 | Position Sizing Methods | 7.2-7.4 | All trading domains |
| 7.6 | Bankroll Management (segregation, unit sizing, dynamic adjustment) | 7.5 | Strategy Integration |
| 7.7 | Drawdown Management | 7.3, 7.4 | Portfolio, Behavioral Edge |
| 7.8 | EV vs. Variance Tradeoff (geometric mean penalty) | 7.1, 1.8 | Portfolio, Market Making |
| 7.9 | Correlation Risk | 1.3, 7.5 | Portfolio, Arbitrage |
| 7.10 | Diversification in Prediction Markets | 7.9 | Portfolio |

---

## Section 3: Advanced Strategies

### Domain 8: Quantitative Modeling
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 8.1 | Probability Model Construction (feature engineering, classification) | 4.3, 1.8 | Event-Driven Trading, Algorithmic Systems |
| 8.2 | Bayesian Updating Pipeline (priors, likelihood, posterior, PyMC) | 1.4, 8.1 | Event-Driven Trading, Algorithmic Systems |
| 8.3 | Monte Carlo Simulation (correlated draws, variance reduction) | 1.8, 8.1 | Portfolio (VaR, stress testing) |
| 8.4 | Model Calibration & Scoring (Platt scaling, isotonic regression) | 4.5, 4.6 | Algorithmic Systems |
| 8.5 | Backtesting (walk-forward, transaction costs, overfitting detection) | 8.1, 3.6 | Algorithmic Systems, Strategy Integration |
| 8.6 | Time-Series Analysis (ARIMA, GARCH, regime-switching) | 8.1 | Event-Driven Trading, Market Making |
| 8.7 | Combining Models with Market Prices (edge detection, contrarian/momentum) | 8.1, 5.12 | All trading domains |
| 8.8 | Ensemble Methods & Bayesian Model Averaging | 8.1, 8.2 | Strategy Integration |

### Domain 9: Arbitrage & Cross-Platform Strategies
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 9.1 | Cross-Platform Arbitrage (price divergence, implied probability comparison) | 2.11, 5.2 | Algorithmic Systems |
| 9.2 | Dutch Booking (detection, optimal stake) | 5.11, 9.1 | Market Making |
| 9.3 | Correlated Market Arbitrage (conditional probability violations, LLM detection) | 1.3, 5.4 | Quant Modeling |
| 9.4 | Execution & Settlement Risk (leg risk, oracle risk, platform risk) | 2.9, 2.10 | Risk Management, Algorithmic Systems |
| 9.5 | Fee-Adjusted Calculations (net profit, break-even spread) | 3.6, 9.1 | All trading domains |
| 9.6 | API Trading Infrastructure (REST, WebSocket, SDKs, rate limits) | 2.11 | Algorithmic Systems, Market Making |
| 9.7 | Monitoring & Alert Systems (real-time scanning, event matching) | 9.6 | Algorithmic Systems |
| 9.8 | Regulatory Constraints (CFTC, state law, cross-border, insider trading) | 2.12 | Strategy Integration |

### Domain 10: Portfolio Construction & Correlation Management
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 10.1 | Modern Portfolio Theory Adapted (MVO, efficient frontier for binary) | 7.8, 8.3 | Strategy Integration |
| 10.2 | Correlation Estimation for Events (pairwise, implied, regimes) | 7.9, 1.3 | Risk Management, Arbitrage |
| 10.3 | Portfolio-Level Kelly Criterion (multi-bet, correlated) | 7.2, 10.2 | Algorithmic Systems |
| 10.4 | Diversification Strategies (category, temporal, geographic, platform) | 7.10 | Strategy Integration |
| 10.5 | Concentration Risk (single-position, thematic, resolution date) | 10.2, 10.4 | Risk Management |
| 10.6 | Position Limits & Sizing Rules | 7.5, 10.5 | Market Making, Algorithmic Systems |
| 10.7 | Hedging Strategies (direct, cross-market, delta-neutral, calendar) | 10.2, 5.7 | Market Making, Event-Driven Trading |
| 10.8 | Tail Risk Management (stress testing, VaR for binary portfolios) | 8.3, 10.2 | Risk Management |
| 10.9 | Portfolio Metrics (Sharpe, Sortino, MDD, ROC, Brier at portfolio level) | 10.1 | Strategy Integration |
| 10.10 | Rebalancing (trigger-based, calendar, event-driven, cost-aware) | 10.6, 10.9 | Strategy Integration |
| 10.11 | Exposure Monitoring (real-time P&L, correlation dashboard, alerts) | 10.9, 9.7 | Algorithmic Systems |

### Domain 11: Market Making & Liquidity Provision
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 11.1 | Market Making Fundamentals (spread capture, maker edge) | 3.1, 3.3 | Algorithmic Systems |
| 11.2 | Spread Setting (Avellaneda-Stoikov, reservation price, dynamic adjustment) | 11.1, 3.12 | Algorithmic Systems |
| 11.3 | Quote Skewing (inventory-driven asymmetric quoting) | 11.2 | Risk Management |
| 11.4 | Inventory Risk Management (position limits, half-life, delta-neutral) | 7.5, 11.3 | Risk Management, Portfolio |
| 11.5 | Adverse Selection (informed vs. uninformed flow, toxicity metrics, VPIN) | 3.11, 11.1 | Behavioral Edge, Algorithmic Systems |
| 11.6 | AMM Models (LMSR, CPMM, pm-AMM, impermanent loss) | 5.10, 2.5 | Pricing Theory |
| 11.7 | Order Book vs. AMM Architecture | 2.4, 2.5 | Platform Mechanics |
| 11.8 | Market Making P&L Analysis (spread revenue, adverse selection cost, Sharpe) | 11.1-11.5 | Strategy Integration |
| 11.9 | Platform-Specific MM (Kalshi incentives, Polymarket rewards) | 2.11, 11.1 | Algorithmic Systems |
| 11.10 | Settlement Risk in Market Making | 2.9, 11.4 | Event-Driven Trading |

### Domain 12: Event-Driven & Catalyst Trading
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 12.1 | Event Classification & Taxonomy (scheduled/unscheduled, hard/soft, recurring/one-off) | 6.4 | Info Sources |
| 12.2 | Event Playbook Construction (checklists, scenario analysis, entry/exit rules) | 12.1, 4.3 | Strategy Integration |
| 12.3 | Pre-Event Positioning (thesis, probability gaps, timing, scaling, hedging) | 5.12, 7.5 | Portfolio, Risk Management |
| 12.4 | Live Event Trading (real-time info processing, predefined triggers, overreaction) | 12.2, 1.4 | Algorithmic Systems, Behavioral Edge |
| 12.5 | News-Driven Repricing (cascades, signal vs. noise, speed, narrative vs. data) | 6.3, 4.8 | Behavioral Edge, Info Sources |
| 12.6 | Volatility Around Catalysts (compression/expansion, time decay, volatility as edge) | 5.7, 3.12 | Pricing Theory, Market Making |
| 12.7 | Exit Timing & Position Management (profit targets, trailing, stop-loss, post-event drift) | 7.7, 12.3 | Risk Management |
| 12.8 | P&L Attribution for Event-Driven (alpha vs. baseline, decay curves, win rate by type) | 12.1-12.7 | Strategy Integration |
| 12.9 | Event Market Microstructure (liquidity dynamics, resolution criteria edge) | 3.11, 6.1 | Market Making |
| 12.10 | Behavioral Patterns in Event Markets (favorite-longshot, recency, anchoring, emotional spikes) | 5.13, 12.4 | Behavioral Edge |

---

## Section 4: Expert Integration

### Domain 13: Algorithmic & Automated Trading Systems
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 13.1 | Platform API Integration (REST, WebSocket, auth, rate limits, SDKs) | 9.6 | All automated domains |
| 13.2 | Signal Generation & Strategy Execution (pipeline, event-driven architecture) | 8.7, 13.1 | Quant Modeling |
| 13.3 | Backtesting Infrastructure (historical data, walk-forward, transaction costs, overfitting) | 8.5 | Strategy Integration |
| 13.4 | Paper Trading (simulation, realistic fills, performance tracking) | 13.3 | Strategy Integration |
| 13.5 | Production Deployment (infrastructure, CI/CD, config management, logging) | 13.4 | Strategy Integration |
| 13.6 | Monitoring & Alerting (dashboards, metrics, anomaly detection) | 13.5, 10.11 | Strategy Integration |
| 13.7 | Risk Limits & Circuit Breakers (position limits, loss limits, kill switch, watchdog) | 7.5, 13.5 | Risk Management |
| 13.8 | Latency & Performance (async, data structures, network optimization) | 13.1 | Market Making |

### Domain 14: Behavioral Edge & Market Psychology
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 14.1 | Cognitive Biases in Markets (favorite-longshot, overconfidence, anchoring, recency, confirmation, loss aversion) | 1.11, 4.7 | All domains |
| 14.2 | Market-Level Phenomena (herding, crowd psychology, information cascades) | 4.8, 14.1 | Event-Driven Trading, Market Making |
| 14.3 | Narrative Bias & Sentiment vs. Information | 6.3, 14.1 | Event-Driven Trading, Quant Modeling |
| 14.4 | Trading-Specific Patterns (disposition effect, sunk cost, status quo, gambler's fallacy) | 14.1 | Risk Management, Strategy Integration |
| 14.5 | Contrarian Strategies | 14.1-14.4 | Event-Driven Trading, Portfolio |
| 14.6 | Counter-Narrative Trading | 14.3, 14.5 | Event-Driven Trading |
| 14.7 | Bias Exploitation Framework (identify, estimate, catalyst, size, manage) | 14.1-14.6 | Strategy Integration |
| 14.8 | Debiasing Techniques (self: pre-commitment, journals, checklists, red teaming) | 4.7 | Forecasting, Strategy Integration |
| 14.9 | Sentiment Analysis (NLP, FinBERT, automated pipelines) | 14.3 | Algorithmic Systems |
| 14.10 | Superforecasting Psychology (active open-mindedness, probabilistic granularity) | 4.1 | Forecasting |

### Domain 15: Strategy Integration & Performance Measurement
| # | Concept | Prerequisites | Cross-Domain Links |
|---|---------|--------------|-------------------|
| 15.1 | Multi-Strategy Management (correlation, lifecycle, operational independence) | 10.1, 13.5 | All domains |
| 15.2 | Performance Attribution (strategy, market/event-type, timing, sizing, platform) | 10.9, 12.8 | All domains |
| 15.3 | Risk-Adjusted Metrics (Sharpe, Sortino, Calmar, Profit Factor, Expectancy, R-Multiple) | 10.9 | All domains |
| 15.4 | Capital Allocation Across Strategies (equal, risk-parity, Kelly-weighted, performance-based) | 7.2, 10.3, 15.2 | Portfolio, Risk Management |
| 15.5 | Trading Journal Design & Maintenance | None | All domains |
| 15.6 | Quarterly Strategy Review & Optimization | 15.1-15.5 | All domains |
| 15.7 | Tax & Compliance | 9.8 | Arbitrage, Platform Mechanics |
| 15.8 | Continuous Improvement & Edge Decay Monitoring | 15.2, 15.6 | All domains |

---

## Concept Statistics

- **Total unique concepts:** 156
- **Beginner concepts:** 38
- **Intermediate concepts:** 42
- **Advanced concepts:** 48
- **Expert concepts:** 28
- **Domains:** 15
- **Cross-cutting themes:** Calibration & Intellectual Honesty, Edge Identification & Exploitation, Risk-Reward Tradeoff, Data-Driven Decision Making, Platform & Regulatory Awareness, Psychological Discipline
