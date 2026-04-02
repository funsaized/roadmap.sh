# Mastering Prediction Market Trading Strategies

A practitioner's roadmap to building and operating autonomous or semi-autonomous trading systems on prediction markets — covering market mechanics, position sizing, arbitrage, risk management, and AI-driven trading agents.

## Usage

Open `roadmap.html` in any modern browser (Chrome, Firefox, Safari, Edge). No server or build step required.

### Features

- **Progress tracking** — Check off topics as you complete them. Progress is saved in your browser's localStorage.
- **Detail panel** — Click any topic node to see its description, key concepts, sub-topics, prerequisites, and curated learning resources.
- **Search & filter** — Use the search bar to find topics by name or concept. Filter by difficulty level (beginner/intermediate/advanced/expert).
- **Section collapse** — Click section headers to collapse/expand sections.
- **Prerequisite navigation** — Click prerequisite links in the detail panel to jump to the referenced topic.
- **Prerequisite locking** — Topics with unfinished prerequisites show a lock icon. Complete prerequisites first to unlock them.

## Statistics

| Metric | Value |
|---|---|
| Total topics | 150 |
| Learning resources | 23 |
| Unique sources | 16 |
| Edges | 231 |
| Sections | 13 |
| Difficulty levels | 4 (beginner, intermediate, advanced, expert) |

## Table of Contents

### 1. [Beginner] Probability & Bayesian Reasoning
None — starts here. Frequentist vs Bayesian probability, conditional probability, Bayes' theorem, base rates, calibration, probability distributions, expected value, law of large numbers.

### 2. [Beginner] Prediction Market Mechanics & Platforms
None. How prediction markets work (binary, multi-outcome, scalar), order books vs AMMs, platform comparison (Kalshi, Polymarket, Metaculus, PredictIt, Manifold), fee structures, settlement rules, regulatory landscape (CFTC).

### 3. [Beginner] Financial Markets Fundamentals
None. Bid/ask spreads, order types (market, limit, stop), time value, liquidity, slippage, margin, leverage, basic options concepts, market microstructure basics.

### 4. [Intermediate] Forecasting & Calibration
Prerequisites: Probability & Bayesian Reasoning. Superforecasting techniques, reference class forecasting, decomposition methods, inside vs outside view, calibration training, Brier scores, log scoring, tracking forecast accuracy, wisdom of crowds.

### 5. [Intermediate] Pricing Theory for Binary & Multi-Outcome Contracts
Prerequisites: Probability, Financial Fundamentals. Fair value of binary contracts, implied probability extraction, overround/vig calculation, no-arbitrage pricing, time decay in event contracts, Dutch book arguments, EMH applied to prediction markets.

### 6. [Intermediate] Information Sources & Research Methods
Prerequisites: Market Mechanics, Forecasting. OSINT for prediction markets, polling data interpretation, economic indicator tracking, weather/climate data, political fundamentals, sports analytics, news flow analysis, data APIs and scraping, building an information edge.

### 7. [Intermediate] Risk Management & Bankroll Strategy
Prerequisites: Probability, Financial Fundamentals. Kelly criterion (full and fractional), bankroll management, risk of ruin, position sizing, correlation risk, drawdown management, unit sizing, stop-loss strategies for event contracts.

### 8. [Advanced] Quantitative Modeling for Prediction Markets
Prerequisites: Forecasting, Pricing Theory, Risk Management. Building probability models (logistic regression, ensemble methods), backtesting, feature engineering for event outcomes, Monte Carlo simulation, Bayesian updating pipelines, time-series analysis for evolving markets.

### 9. [Advanced] Arbitrage & Cross-Platform Strategies
Prerequisites: Market Mechanics, Pricing Theory, Risk Management. Cross-platform arbitrage identification, correlated market arbitrage, multi-outcome arbitrage (Dutch booking), execution risk, settlement risk, fee-adjusted arbitrage calculations, API-based trading, monitoring tools.

### 10. [Advanced] Portfolio Construction & Correlation Management
Prerequisites: Risk Management, Quantitative Modeling. Portfolio theory applied to prediction markets, correlation estimation between event outcomes, hedging strategies, sector/theme concentration risk, tail risk management, rebalancing strategies, portfolio-level Kelly, exposure monitoring.

### 11. [Advanced] Market Making & Liquidity Provision
Prerequisites: Pricing Theory, Risk Management, Arbitrage. Market-making theory, bid-ask spread setting, inventory risk, adverse selection, providing liquidity on order-book platforms, AMM liquidity provision (Polymarket), dynamic spread adjustment, automated market-making strategies.

### 12. [Advanced] Event-Driven & Catalyst Trading
Prerequisites: Information Sources, Quantitative Modeling. Trading around scheduled events (elections, economic releases, court decisions), pre-event positioning, volatility around catalysts, news-driven rapid repricing, building event playbooks, live trading during events, exit timing.

### 13. [Expert] Algorithmic & Automated Trading Systems
Prerequisites: Quantitative Modeling, Arbitrage, Market Making. API integration with prediction market platforms, automated signal generation, execution algorithms, monitoring and alerting, backtesting infrastructure, paper trading, production deployment, error handling and circuit breakers, latency optimization, regulatory compliance.

## File Structure

```
roadmap.html                              # Interactive roadmap (open in browser)
README.md                                 # This file
architecture/roadmap-final.json           # Source data (150 nodes, 231 edges, 23 resources)
architecture/layout-spec.md               # Layout design specification
```

## Generated

2026-04-02
