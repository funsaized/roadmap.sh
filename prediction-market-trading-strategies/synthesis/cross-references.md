# Cross-References: How Domains Relate and Reinforce Each Other

## Overview

This document maps the interconnections between all 15 domains, showing how concepts from one domain appear in, reinforce, or are prerequisites for concepts in other domains. Understanding these connections enables integrated learning and reveals how mastery in one area amplifies performance in others.

---

## Cross-Cutting Themes

Six themes weave through every domain. Each theme manifests differently depending on the domain context.

### 1. Calibration & Intellectual Honesty
- **Probability (D1):** Brier score, calibration curves, proper scoring rules
- **Forecasting (D4):** Calibration training, overconfidence correction, calibration plots
- **Quant Modeling (D8):** Model calibration via Platt scaling and isotonic regression
- **Behavioral Edge (D14):** Recognizing overconfidence bias in self and others
- **Strategy Integration (D15):** Portfolio-level Brier score tracking

### 2. Edge Identification & Exploitation
- **Pricing Theory (D5):** Mispricing identification, fair value vs. market price
- **Info Sources (D6):** Information advantage assessment
- **Quant Modeling (D8):** Edge detection from model vs. market
- **Arbitrage (D9):** Cross-platform price divergence as structural edge
- **Behavioral Edge (D14):** Cognitive biases as systematic mispricing source
- **Market Making (D11):** Spread capture as market-neutral edge

### 3. Risk-Reward Tradeoff
- **Probability (D1):** EV and variance concepts
- **Risk Management (D7):** Kelly criterion, EV vs. variance, geometric mean penalty
- **Portfolio (D10):** Efficient frontier, Sharpe optimization
- **Market Making (D11):** Spread revenue vs. adverse selection cost
- **Strategy Integration (D15):** Risk-adjusted metrics across strategies

### 4. Data-Driven Decision Making
- **Forecasting (D4):** Reference class data, base rates, decomposition
- **Info Sources (D6):** Tiered data sources, systematic research workflow
- **Quant Modeling (D8):** Feature engineering, model training, backtesting
- **Event-Driven (D12):** Event playbooks, P&L attribution
- **Algorithmic Systems (D13):** Signal pipelines, automated data processing

### 5. Platform & Regulatory Awareness
- **Market Mechanics (D2):** Platform comparison, CFTC regulation
- **Arbitrage (D9):** Cross-platform execution, regulatory constraints
- **Market Making (D11):** Platform-specific incentive programs
- **Algorithmic Systems (D13):** API integration, rate limits
- **Strategy Integration (D15):** Tax compliance, platform risk

### 6. Psychological Discipline
- **Forecasting (D4):** Cognitive debiasing, pre-mortem analysis
- **Risk Management (D7):** Fractional Kelly for psychological sustainability
- **Event-Driven (D12):** Predefined triggers to remove emotion
- **Behavioral Edge (D14):** Self-awareness of biases, trading journal
- **Strategy Integration (D15):** Emotional state tracking, style drift detection

---

## Domain Pair Connections (Bidirectional)

### Probability (D1) ↔ Forecasting (D4)
- Bayes' theorem is the engine of forecasting updates
- Calibration (D4) validates probability estimates (D1)
- Base rate neglect (D1) motivates reference class forecasting (D4)
- Scoring rules (D1) measure forecasting quality (D4)

### Probability (D1) ↔ Pricing Theory (D5)
- Probability axioms enforce no-arbitrage constraints
- EV calculations derive fair value
- Odds conversion connects probability to market prices
- Dutch book theorem links coherent probability to pricing

### Market Mechanics (D2) ↔ Arbitrage (D9)
- Platform differences create arbitrage opportunities
- Order book mechanics determine execution feasibility
- Fee structures set arbitrage profitability thresholds
- Settlement differences introduce leg risk

### Forecasting (D4) ↔ Behavioral Edge (D14)
- Cognitive debiasing (D4) is defense against the biases exploited in D14
- Superforecaster traits (D4) are the antidote to market-level biases (D14)
- Calibration quality determines whether behavioral trades are sized correctly

### Pricing Theory (D5) ↔ Market Making (D11)
- LMSR pricing model is a market making mechanism
- Spread mechanics from D5 become revenue model in D11
- Overround calculation informs spread setting
- Time decay affects inventory holding decisions

### Risk Management (D7) ↔ Portfolio Construction (D10)
- Kelly criterion (D7) scales to portfolio-level Kelly (D10)
- Correlation risk (D7) becomes correlation matrix construction (D10)
- Diversification principles (D7) become portfolio structure (D10)
- Drawdown management (D7) becomes tail risk management (D10)

### Quant Modeling (D8) ↔ Algorithmic Systems (D13)
- Models (D8) produce signals that systems (D13) execute
- Backtesting (D8) validates strategies that systems (D13) deploy
- Feature engineering (D8) feeds signal pipelines (D13)
- Calibration tools (D8) monitor system health (D13)

### Event-Driven (D12) ↔ Info Sources (D6)
- Data sources (D6) identify catalysts (D12)
- Research workflow (D6) becomes pre-event playbook prep (D12)
- Signal vs. noise analysis (D6) drives live event interpretation (D12)
- Resolution criteria analysis (D6) creates edge in event trading (D12)

### Arbitrage (D9) ↔ Algorithmic Systems (D13)
- API infrastructure (D9) becomes system foundation (D13)
- Monitoring tools (D9) become alerting systems (D13)
- Execution logic (D9) becomes order management (D13)
- Risk controls (D9) become circuit breakers (D13)

### Behavioral Edge (D14) ↔ Event-Driven (D12)
- Behavioral patterns (D14) create event-day mispricings (D12)
- Emotional spikes around events create contrarian opportunities
- Narrative bias (D14) is strongest during high-profile events (D12)
- Favorite-longshot bias (D14) is most exploitable pre-event (D12)

---

## Reinforcement Loops

### Loop 1: Forecast → Trade → Attribution → Improve
```
Forecasting (D4) → produces probability estimates
  → Pricing Theory (D5) → identifies mispricings
    → Risk Management (D7) → sizes positions
      → Event-Driven (D12) → executes trades
        → Strategy Integration (D15) → measures performance
          → [feeds back to Forecasting (D4) for improvement]
```

### Loop 2: Model → System → Monitor → Refine
```
Quant Modeling (D8) → builds prediction models
  → Algorithmic Systems (D13) → deploys automated execution
    → Monitoring & Alerting (D13.6) → detects anomalies
      → Backtesting (D8.5) → validates refinements
        → [feeds back to Quant Modeling for iteration]
```

### Loop 3: Bias Detection → Contrarian → Attribution → Pattern Library
```
Behavioral Edge (D14) → detects market bias
  → Contrarian Strategy (D14.5) → positions against bias
    → P&L Attribution (D15.2) → measures if bias was real
      → Bias Journal (D14.8) → records pattern
        → [feeds back to improve bias detection]
```

---

## Concept Overlap Matrix

Concepts that appear across multiple domains (primary domain listed first):

| Concept | Appears In | Notes |
|---------|-----------|-------|
| Expected Value (EV) | D1, D5, D7, D8, D12, D15 | Foundation concept; different applications per domain |
| Bayes' Theorem / Updating | D1, D4, D8, D12 | Theory (D1), Practice (D4), Automation (D8), Real-time (D12) |
| Calibration | D1, D4, D8, D14, D15 | Definition (D1), Training (D4), Model (D8), Self (D14), Portfolio (D15) |
| Bid-Ask Spread | D2, D3, D5, D9, D11 | Basics (D2/D3), Pricing impact (D5), Cost (D9), Revenue (D11) |
| Kelly Criterion | D7, D8, D10, D13, D15 | Theory (D7), Sizing (D8), Portfolio (D10), Automated (D13), Allocation (D15) |
| Liquidity | D2, D3, D9, D11, D12 | Definition (D2/D3), Constraint (D9), Provision (D11), Dynamics (D12) |
| Favorite-Longshot Bias | D5, D12, D14 | Pricing pattern (D5), Event pattern (D12), Behavioral source (D14) |
| Overround / Vig | D1, D2, D5, D9 | Theory (D1), Platform (D2), Calculation (D5), Arb threshold (D9) |
| Order Book / Microstructure | D2, D3, D11, D12, D13 | Basics (D2/D3), MM operations (D11), Event dynamics (D12), API (D13) |
| Platform APIs | D2, D9, D11, D13 | Overview (D2), Arb infra (D9), MM infra (D11), Full systems (D13) |
| Correlation | D1, D7, D8, D9, D10 | Theory (D1), Risk (D7), Modeling (D8), Multi-market (D9), Portfolio (D10) |
| Drawdown | D7, D10, D13, D15 | Individual (D7), Portfolio (D10), Circuit breaker (D13), Metric (D15) |
| Scoring Rules (Brier/Log) | D1, D4, D8, D15 | Definition (D1), Training (D4), Model eval (D8), Performance (D15) |
| Cognitive Biases | D1, D4, D12, D14 | Fallacies (D1), Debiasing (D4), Event patterns (D12), Exploitation (D14) |
| Resolution / Settlement | D2, D6, D9, D12 | Mechanics (D2), Criteria analysis (D6), Risk (D9), Edge (D12) |

---

## Synergy Map: Which Domains Amplify Each Other

High-synergy pairs (mastering both together yields more than the sum of parts):

1. **Forecasting + Behavioral Edge:** Knowing your own biases makes you a better forecaster; knowing common biases makes you a better trader
2. **Pricing Theory + Market Making:** Fair value estimation is half of market making; spread mechanics complete it
3. **Quant Modeling + Algorithmic Systems:** Models without automation are slow; automation without models is blind
4. **Risk Management + Portfolio Construction:** Position sizing without portfolio context is incomplete; portfolio without position sizing is reckless
5. **Info Sources + Event-Driven Trading:** Research workflow directly powers event playbooks; live event interpretation depends on source quality
6. **Arbitrage + Algorithmic Systems:** Manual arb is too slow; automated arb needs proper infrastructure
7. **Behavioral Edge + Forecasting:** The ultimate edge: exploit others' biases while minimizing your own
