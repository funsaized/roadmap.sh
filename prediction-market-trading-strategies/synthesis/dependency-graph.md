# Dependency Graph: Prediction Market Trading Strategies

## Domain-Level Dependencies

```
BEGINNER TIER
┌─────────────────────┐  ┌──────────────────────────┐  ┌──────────────────────────┐
│ 1. Probability &    │  │ 2. Prediction Market     │  │ 3. Financial Markets     │
│    Bayesian Reasoning│  │    Mechanics & Platforms  │  │    Fundamentals          │
└────────┬────────────┘  └────────────┬─────────────┘  └────────────┬─────────────┘
         │                            │                              │
         ├──────────────┐             │                              │
         │              │             │                              │
         ▼              ▼             ▼                              ▼
INTERMEDIATE TIER
┌─────────────────┐  ┌────────────────────────┐  ┌──────────────────────────┐
│ 4. Forecasting & │  │ 5. Pricing Theory for  │  │ 6. Information Sources   │
│    Calibration   │  │    Binary Contracts    │◄─┤    & Research Methods    │
└────────┬────────┘  └────────────┬───────────┘  └──────────────────────────┘
         │                        │                          ▲
         │              ┌─────────┤                          │
         │              │         │                          │
         ▼              ▼         ▼                          │
┌─────────────────────────────────────┐                      │
│ 7. Risk Management & Bankroll      │──────────────────────►│
│    Strategy                        │                       │
└────────┬────────────────────┬──────┘
         │                    │
ADVANCED TIER                 │
         ▼                    ▼
┌──────────────────┐  ┌────────────────────┐  ┌──────────────────────────┐
│ 8. Quantitative  │  │ 9. Arbitrage &     │  │ 10. Portfolio            │
│    Modeling      │  │    Cross-Platform   │  │     Construction         │
└────────┬─────────┘  └────────┬───────────┘  └────────────┬─────────────┘
         │                     │                            │
         │                     ▼                            │
         │            ┌──────────────────┐                  │
         │            │ 11. Market Making │                  │
         │            │     & Liquidity   │                  │
         │            └────────┬─────────┘                  │
         │                     │                            │
         ▼                     │                            │
┌──────────────────────────┐   │                            │
│ 12. Event-Driven &       │◄──┘                            │
│     Catalyst Trading     │                                │
└────────┬─────────────────┘                                │
         │                                                  │
EXPERT TIER                                                 │
         ▼                                                  ▼
┌──────────────────────────┐  ┌──────────────────────────┐
│ 13. Algorithmic &        │  │ 14. Behavioral Edge &    │
│     Automated Systems    │  │     Market Psychology    │
└────────┬─────────────────┘  └────────┬─────────────────┘
         │                             │
         └──────────────┬──────────────┘
                        ▼
         ┌──────────────────────────────┐
         │ 15. Strategy Integration &   │
         │     Performance Measurement  │
         └──────────────────────────────┘
```

## Detailed Edge List (Domain-to-Domain)

| From | To | Relationship |
|------|-----|-------------|
| Probability & Bayesian Reasoning | Forecasting & Calibration | Bayes' theorem enables updating; calibration builds on probability foundations |
| Probability & Bayesian Reasoning | Pricing Theory | Probability axioms underpin no-arbitrage pricing and fair value derivation |
| Probability & Bayesian Reasoning | Risk Management | EV and distributions feed Kelly criterion and position sizing |
| Prediction Market Mechanics | Information Sources | Platform knowledge directs where to research |
| Prediction Market Mechanics | Arbitrage | Platform comparison reveals cross-platform opportunities |
| Financial Markets Fundamentals | Pricing Theory | Spreads, fees, and market microstructure inform contract pricing |
| Financial Markets Fundamentals | Risk Management | Liquidity and slippage constrain position sizing |
| Forecasting & Calibration | Information Sources | Research methods depend on forecasting framework |
| Forecasting & Calibration | Quantitative Modeling | Calibration and scoring rules become model evaluation tools |
| Forecasting & Calibration | Behavioral Edge | Debiasing links directly to recognizing market biases |
| Pricing Theory | Quantitative Modeling | Pricing models (Black-Scholes, LMSR) become modeling tools |
| Pricing Theory | Arbitrage | No-arbitrage and Dutch book theory enable arb detection |
| Pricing Theory | Market Making | LMSR, spread mechanics, and overround inform quoting |
| Information Sources | Event-Driven Trading | Data sources and research workflow feed catalyst identification |
| Risk Management | Quantitative Modeling | Kelly and position sizing constrain model outputs |
| Risk Management | Arbitrage | Risk of ruin and correlation risk bound arbitrage capital |
| Risk Management | Portfolio Construction | Individual sizing scales to portfolio-level allocation |
| Risk Management | Market Making | Position limits and drawdown management protect MM operations |
| Quantitative Modeling | Portfolio Construction | Correlation models and simulations drive portfolio optimization |
| Quantitative Modeling | Event-Driven Trading | Feature engineering and Bayesian updating power catalyst models |
| Quantitative Modeling | Algorithmic Systems | Backtesting frameworks and model pipelines become system components |
| Arbitrage | Market Making | Arb detection informs inventory management and spread strategy |
| Arbitrage | Algorithmic Systems | API infrastructure and monitoring tools become building blocks |
| Portfolio Construction | Behavioral Edge | Portfolio tracking reveals psychological biases |
| Portfolio Construction | Strategy Integration | Portfolio framework unifies all strategies |
| Market Making | Algorithmic Systems | MM strategies are primary automated system use case |
| Event-Driven Trading | Strategy Integration | Event alpha combines with other strategy returns |
| Algorithmic Systems | Strategy Integration | Production systems enable measurable multi-strategy operations |
| Behavioral Edge | Strategy Integration | Behavioral alpha becomes one of several alpha sources |

## Concept-Level Critical Prerequisites

These concept-to-concept dependencies represent the most important prerequisite chains:

### Chain 1: Probability → Edge Detection
```
Probability Fundamentals → Bayes' Theorem → Base Rates → Expected Value
→ Fair Value Derivation → Implied Probability → Mispricing Identification → Edge Detection
```

### Chain 2: Calibration → Position Sizing
```
Calibration & Brier Score → Scoring Rules → Probability Model Construction
→ Model Calibration → Edge Estimation → Kelly Criterion → Fractional Kelly → Position Sizing
```

### Chain 3: Market Mechanics → Automated Trading
```
Order Book Mechanism → Order Types → Maker/Taker → Liquidity → Bid-Ask Spread
→ Platform APIs → Signal Pipeline → Backtesting → Paper Trading → Production Deployment
```

### Chain 4: Risk → Portfolio
```
EV & Edge → Kelly Criterion → Risk of Ruin → Correlation Risk → Diversification
→ Portfolio-Level Kelly → Position Limits → Hedging → Tail Risk → Portfolio Metrics
```

### Chain 5: Behavioral → Contrarian
```
Cognitive Biases → Favorite-Longshot Bias → Narrative Bias → Herding
→ Sentiment Analysis → Contrarian Strategies → Bias Exploitation Framework
```

## Estimated Hours by Domain

| Domain | Estimated Hours | Cumulative |
|--------|:--------------:|:----------:|
| 1. Probability & Bayesian Reasoning | 45 | 45 |
| 2. Prediction Market Mechanics | 19 | 64 |
| 3. Financial Markets Fundamentals | 39 | 103 |
| 4. Forecasting & Calibration | 67 | 170 |
| 5. Pricing Theory | 44 | 214 |
| 6. Information Sources | 30 | 244 |
| 7. Risk Management & Bankroll | 32 | 276 |
| 8. Quantitative Modeling | 90 | 366 |
| 9. Arbitrage & Cross-Platform | 85 | 451 |
| 10. Portfolio Construction | 75 | 526 |
| 11. Market Making | 90 | 616 |
| 12. Event-Driven Trading | 95 | 711 |
| 13. Algorithmic Systems | 150 | 861 |
| 14. Behavioral Edge | 82 | 943 |
| 15. Strategy Integration | 60 | 1003 |
| **Total** | **1003** | |
