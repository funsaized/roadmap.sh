# Quantitative Modeling for Prediction Markets

**Domain Level:** Advanced
**Prerequisites:** Forecasting & Calibration, Pricing Theory for Binary & Multi-Outcome Contracts, Risk Management & Bankroll Strategy

---

## A) Key Concepts

### 1. Probability Model Construction

**Base Rate Analysis**
Establishing a starting probability for an event using historical frequency of similar events. This is the foundation of any quantitative approach: before layering in current information, anchor to how often similar events have resolved in a given direction historically.

**Feature Engineering for Event Prediction**
Transforming raw data (polls, economic indicators, sentiment scores, historical outcomes) into predictive input variables. Domain-specific features are critical:
- Political events: poll aggregates, incumbency, economic conditions, house effects
- Sports: Elo ratings, injury reports, schedule strength, head-to-head records
- Financial/economic: leading indicators, yield curves, employment data

Features feed into probability models and Monte Carlo simulations as distributional inputs.

**Logistic Regression & Classification Models**
Using logistic regression, random forests, gradient boosting (XGBoost, LightGBM), or neural networks to output probability estimates for binary or multi-class event outcomes. These models map engineered features to a probability between 0 and 1.

**Ensemble Methods**
Combining multiple models (e.g., averaging a logistic regression with a gradient boosting model) to reduce variance and improve robustness. Ensemble approaches consistently outperform single models in forecasting competitions.

### 2. Bayesian Updating

**Prior Selection**
Choosing initial probability distributions before observing data. For binary events, the Beta distribution is a natural conjugate prior for Bernoulli likelihoods. Prior choice encodes domain knowledge: uninformative priors (Beta(1,1)) when uncertain, informative priors when historical data is available.

**Likelihood Functions**
Defining P(data|hypothesis) -- how likely the observed evidence is under each possible state of the world. The likelihood function is the core modeling challenge: it quantifies how new information (a poll, a trade, a news event) maps to probability updates.

**Posterior Computation**
Applying Bayes' theorem to combine prior and likelihood into updated beliefs. For conjugate pairs (Beta-Bernoulli), updates are analytical. For complex models, Markov Chain Monte Carlo (MCMC) sampling via tools like PyMC is required.

**Sequential/Iterative Updating**
The posterior from one update becomes the prior for the next. This creates a pipeline where each new piece of information refines the probability estimate. Essential for prediction markets where information arrives continuously.

**Bayesian Model Averaging**
When uncertain which model is correct, weight predictions from multiple models by their posterior probability of being the true model. Reduces model selection risk.

### 3. Monte Carlo Simulation

**Random Sampling from Distributions**
Drawing thousands of random samples from probability distributions assigned to uncertain input variables, then propagating these through a model to generate a distribution of outcomes rather than a single point estimate.

**Scenario Generation**
Each Monte Carlo iteration produces one possible scenario. The collection of scenarios provides a probability distribution over outcomes, enabling risk quantification and tail analysis.

**Variance Reduction Techniques**
Methods like Latin Hypercube Sampling, antithetic variates, and importance sampling that reduce the number of simulations needed for a given accuracy level.

**Correlation Modeling**
When multiple uncertain inputs are correlated (e.g., polling errors across states), the simulation must use correlated random draws (e.g., via Cholesky decomposition of a correlation matrix). Ignoring correlations leads to underestimated tail risks.

### 4. Model Calibration & Scoring

**Brier Score**
Mean squared error between predicted probabilities and actual outcomes: BS = mean((forecast - outcome)^2). Ranges 0 (perfect) to 1 (worst). Decomposes into reliability (calibration), resolution (ability to distinguish events), and uncertainty.

**Log Score (Log Loss)**
-[outcome * log(p) + (1-outcome) * log(1-p)]. Penalizes confident wrong predictions much more heavily than Brier score. Strictly proper scoring rule with roots in information theory.

**Proper Scoring Rules**
Scoring functions where the expected score is maximized when the forecaster reports their true belief. Both Brier and log scores are proper. Using improper scoring rules incentivizes distorting reported probabilities.

**Calibration Curves (Reliability Diagrams)**
Plotting predicted probabilities against observed frequencies. A well-calibrated model's curve lies on the diagonal. Deviations reveal systematic over/under-confidence.

**Platt Scaling & Isotonic Regression**
Post-hoc calibration methods that adjust model outputs to improve calibration without retraining the model. Platt scaling fits a logistic function; isotonic regression fits a non-decreasing step function.

### 5. Backtesting

**Walk-Forward Validation**
Testing a strategy on historical data by stepping through time: train on data up to time t, predict t+1, advance, repeat. Prevents look-ahead bias that infects naive train/test splits.

**Expected Value (EV) Calculation**
EV = P(win) * payout - P(loss) * cost. A positive EV strategy is profitable in expectation. Backtesting reveals whether a model identifies +EV opportunities consistently.

**Sharpe Ratio and Risk-Adjusted Returns**
Measuring not just returns but returns relative to volatility. A strategy with high returns but extreme variance may be inferior to a moderate-return, low-variance approach.

**Overfitting Detection**
Monitoring the gap between in-sample and out-of-sample performance. Techniques include cross-validation, regularization, and checking strategy performance across different time periods.

**Transaction Cost Modeling**
Incorporating realistic fees, spreads, slippage, and market impact into backtests. A strategy that looks profitable before costs may be unprofitable after.

### 6. Time-Series Analysis

**ARIMA/SARIMA Models**
Autoregressive Integrated Moving Average models for stationary/non-stationary time series. Used to model and forecast prediction market price movements and the temporal dynamics of underlying event indicators.

**GARCH Models**
Generalized Autoregressive Conditional Heteroskedasticity models for time-varying volatility. Useful for modeling how prediction market price volatility changes as events approach resolution.

**Exponential Smoothing (ETS)**
Weighted average methods where recent observations get more weight. Simple, robust, and effective as baseline forecasting models.

**Stationarity and Differencing**
Many time series techniques require stationarity. Testing (ADF test, KPSS test) and transforming data via differencing or log transforms is a prerequisite.

**Regime-Switching Models**
Models that allow different dynamics in different "regimes" (e.g., calm markets vs. volatile markets near event resolution). Hidden Markov Models are a common implementation.

### 7. Combining Models with Market Prices

**Edge Detection**
Comparing your model's probability estimate with the market's implied probability. An "edge" exists when |P_model - P_market| exceeds a threshold adjusted for transaction costs and uncertainty.

**Kelly Criterion Integration**
Using model-derived edges to size positions via Kelly (or fractional Kelly). The model output directly feeds the Kelly formula: f* = (bp - q) / b where b is odds, p is model probability, q = 1-p.

**Market Price as Information**
Treating the market price as another signal to incorporate into your model. The market aggregates the beliefs of all participants, making it a strong base rate that your model should beat only when you have a genuine informational advantage.

**Contrarian vs. Momentum Signals**
Quantitative frameworks for deciding when to trade against the market (mean reversion / overreaction) versus with it (momentum / underreaction to news).

### Concept Relationships

```
Feature Engineering → Probability Models → Bayesian Updating → Edge Detection
                                              ↓                      ↓
                                    Monte Carlo Simulation    Kelly Sizing
                                              ↓                      ↓
                                    Backtesting ← ← ← ← ← Position Management
                                              ↓
                                    Calibration & Scoring → Model Refinement
                                              ↓
                                    Time Series Analysis → Regime Detection
```

### Cross-Domain Prerequisites

- **Portfolio Construction** depends on: correlation modeling, ensemble outputs, Monte Carlo portfolio simulation
- **Event-Driven Trading** depends on: feature engineering for catalysts, Bayesian updating pipelines, time-series regime detection
- **Algorithmic Systems** depends on: backtesting frameworks, model-to-signal pipelines, automated Bayesian updating

---

## B) Learning Resources

### Online Courses

| Course | Platform | Cost | Duration | URL |
|--------|----------|------|----------|-----|
| Practical Time Series Analysis | Coursera (SUNY) | Free audit | ~30 hours | https://www.coursera.org/learn/practical-time-series-analysis |
| Bayesian Statistics: Time Series Analysis | Coursera (UC Santa Cruz) | Free audit | ~20 hours | https://www.coursera.org/learn/bayesian-statistics-time-series-analysis |
| Machine Learning for Trading Specialization | Coursera (Google Cloud/NYU) | Paid | ~60 hours | https://www.coursera.org/specializations/machine-learning-trading |
| MIT 14.384 Time Series Analysis | MIT OCW | Free | Full semester | https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/ |
| Penn State STAT 510: Applied Time Series | Penn State | Free | Full semester | https://online.stat.psu.edu/stat510/ |
| Quantitative Analysis for Prediction Markets | StartPolymarket | Free | Self-paced | https://startpolymarket.com/strategies/quantitative-analysis/ |

### Video Tutorials & Lectures

| Title | Platform | URL |
|-------|----------|-----|
| Bayesian Time Series Forecasting with PyMC (PyData 2022) | YouTube | https://www.youtube.com/watch?v=911d4A1U0BE |
| Monte Carlo Simulation Explained | YouTube | https://www.youtube.com/watch?v=tOuoZe8BytU |
| Probabilistic Programming and Bayesian Inference for Time Series | Medium/Video | https://medium.com/data-science/probabilistic-programming-and-bayesian-inference-for-time-series-analysis-and-forecasting-b5eb22114275 |
| Bayesian Statistics in Finance: A Trader's Guide | Interactive Brokers | https://www.interactivebrokers.com/campus/ibkr-quant-news/bayesian-statistics-in-finance-a-traders-guide-to-smarter-decisions/ |
| Systematic Edges in Prediction Markets | Quantpedia | https://quantpedia.com/systematic-edges-in-prediction-markets/ |

### Books

| Title | Author(s) | Relevant Chapters | Difficulty |
|-------|-----------|-------------------|------------|
| Forecasting: Principles and Practice (3rd ed.) | Rob Hyndman & George Athanasopoulos | Ch. 8-9 (ARIMA, Dynamic Regression), Ch. 12 (Advanced) | Intermediate. Free online: https://otexts.com/fpp3/ |
| Superforecasting: The Art and Science of Prediction | Philip Tetlock & Dan Gardner | All (calibration, Bayesian reasoning, model thinking) | Beginner-Intermediate |
| The Signal and the Noise | Nate Silver | Ch. 2 (Foxes vs. Hedgehogs), Ch. 8 (Bayes) | Beginner-Intermediate |
| Bayesian Data Analysis (3rd ed.) | Andrew Gelman et al. | Ch. 1-5 (Fundamentals), Ch. 6 (Model checking), Ch. 14 (Hierarchical) | Advanced |
| Machine Learning for Trading (2nd ed.) | Stefan Jansen | Ch. 10 (Bayesian ML), Ch. 8-9 (Time Series, ML for alpha) | Advanced. GitHub: https://stefan-jansen.github.io/machine-learning-for-trading/ |
| Prediction Markets: Theory and Applications | Leighton Vaughan Williams | All (market mechanics, trading, accuracy) | Intermediate |
| Time Series Analysis: Forecasting and Control | Box, Jenkins, Reinsel, Ljung | Ch. 3-6 (ARIMA theory and practice) | Advanced |

### Documentation & Reference Materials

| Resource | URL |
|----------|-----|
| PyMC Documentation & Examples | https://www.pymc.io/projects/examples/en/latest/time_series/Forecasting_with_structural_timeseries.html |
| scikit-learn Calibration Guide | https://scikit-learn.org/stable/modules/calibration.html |
| ArviZ (Bayesian model diagnostics) | https://python.arviz.org/ |
| Forecasting Wiki - Log Score | https://forecasting.wiki/wiki/Log_score |
| Wikipedia - Brier Score | https://en.wikipedia.org/wiki/Brier_score |
| Wikipedia - Scoring Rule | https://en.wikipedia.org/wiki/Scoring_rule |

### Interactive Exercises & Practice

| Resource | Type | URL |
|----------|------|-----|
| Kaggle Time Series Forecasting Course | Interactive notebooks | https://www.kaggle.com/learn/time-series |
| Metaculus (practice forecasting & calibration) | Live forecasting platform | https://www.metaculus.com/ |
| Good Judgment Open | Forecasting tournaments | https://www.gjopen.com/ |
| Quantopian Lectures (archived via QuantEcon) | Python notebooks | https://quantecon.org/lectures/ |

### GitHub Repositories

| Repository | Description | URL |
|------------|-------------|-----|
| pydiction | Python framework for prediction market trading | https://github.com/quantike/pydiction |
| Polymarket Agents | AI agents for autonomous prediction market trading | https://github.com/polymarket/agents |
| PredictOS | Open-source framework for prediction market bots | https://github.com/PredictionXBT/PredictOS |
| NautilusTrader | Rust-native backtesting engine with Polymarket integration | https://github.com/nautechsystems/nautilus_trader |
| Machine Learning for Trading | Companion code for Stefan Jansen's book | https://github.com/stefan-jansen/machine-learning-for-trading |
| PyMC Examples | Official PyMC example notebooks | https://github.com/pymc-devs/pymc-examples |

### Community Resources

| Community | Platform | URL |
|-----------|----------|-----|
| r/algotrading | Reddit | https://www.reddit.com/r/algotrading/ |
| r/QuantFinance | Reddit | https://www.reddit.com/r/QuantFinance/ |
| Metaculus Community | Forum | https://www.metaculus.com/questions/ |
| PyMC Discourse | Forum | https://discourse.pymc.io/ |
| Quantpedia Blog | Articles | https://quantpedia.com/ |

---

## C) Learning Path

### Phase 1: Foundations (Weeks 1-2, ~20 hours)

**Milestone: Build a basic probability model for one event category**

1. **Feature Engineering Fundamentals** (5 hours)
   - Study feature engineering principles for event prediction
   - Practice creating features from raw data (polls, historical outcomes)
   - Build a feature pipeline for one event category (elections or sports)

2. **Classification Models for Probability Estimation** (8 hours)
   - Implement logistic regression for binary event prediction
   - Train gradient boosting (XGBoost/LightGBM) models
   - Learn proper probability output calibration

3. **Calibration & Scoring Basics** (7 hours)
   - Implement Brier score and log loss calculations
   - Build calibration curves / reliability diagrams
   - Apply Platt scaling to improve model calibration
   - **Checkpoint:** Model outputs well-calibrated probabilities for historical events

### Phase 2: Bayesian Methods (Weeks 3-4, ~25 hours)

**Milestone: Working Bayesian updating pipeline**

4. **Bayesian Updating Theory & Practice** (10 hours)
   - Implement Beta-Bernoulli conjugate updating from scratch in Python
   - Build sequential updating pipeline that processes new information
   - Compare prior, likelihood, and posterior visually

5. **Probabilistic Programming with PyMC** (10 hours)
   - Work through PyMC tutorials for time series forecasting
   - Build a PyMC model for an event category
   - Use MCMC sampling for posterior inference

6. **Bayesian Model Comparison** (5 hours)
   - Implement Bayesian model averaging
   - Compare Bayesian vs. frequentist approaches on same data
   - **Checkpoint:** Pipeline that ingests new data and outputs updated probabilities with uncertainty intervals

### Phase 3: Simulation & Time Series (Weeks 5-6, ~25 hours)

**Milestone: Monte Carlo simulation producing actionable probability distributions**

7. **Monte Carlo Simulation** (10 hours)
   - Build a Monte Carlo simulator for election/sports outcomes
   - Implement correlated random draws for multi-factor events
   - Apply variance reduction techniques
   - Generate probability distributions and confidence intervals

8. **Time-Series Analysis for Prediction Markets** (10 hours)
   - Fit ARIMA models to prediction market price series
   - Implement GARCH for volatility modeling
   - Study regime-switching dynamics near event resolution

9. **Ensemble Methods & Model Combination** (5 hours)
   - Combine multiple model outputs (averaging, stacking)
   - Weight models by recent performance
   - **Checkpoint:** Ensemble model that combines Bayesian, ML, and simulation approaches

### Phase 4: Backtesting & Edge Detection (Weeks 7-8, ~20 hours)

**Milestone: Backtested strategy showing positive EV**

10. **Backtesting Framework** (10 hours)
    - Build walk-forward backtesting system
    - Incorporate transaction costs and realistic execution
    - Calculate EV, Sharpe ratio, and drawdown metrics

11. **Edge Detection & Position Sizing** (5 hours)
    - Compare model probabilities to historical market prices
    - Define edge thresholds accounting for costs and uncertainty
    - Integrate Kelly criterion for position sizing

12. **Model Validation & Documentation** (5 hours)
    - Test for overfitting across time periods
    - Document all model assumptions and limitations
    - Write up model specification and performance report
    - **Checkpoint:** Complete backtest report showing positive EV with documented assumptions

---

## D) Practical Exercises

### Beginner Exercises

1. **Base Rate Calculator**
   Build a Python script that takes an event category (e.g., "incumbent party wins US presidential election") and computes the historical base rate from a dataset. Compare this base rate to current market prices.

2. **Brier Score Tracker**
   Download historical Metaculus or Polymarket resolution data. Calculate your own Brier score and compare it to the market's. Visualize calibration curves.

3. **Simple Bayesian Updater**
   Implement a Beta-Bernoulli updater that starts with a prior, processes a sequence of poll results as binary signals, and plots the evolving posterior distribution.

### Intermediate Exercises

4. **Election Probability Model**
   Build a logistic regression model that predicts election outcomes using features like polling averages, economic indicators, and incumbency. Train on historical data, evaluate with Brier score, and compare predictions to prediction market prices.

5. **Monte Carlo Election Simulator**
   Extend the election model into a Monte Carlo simulation that accounts for correlated polling errors across states/districts. Generate win probability distributions and compare to market consensus.

6. **Bayesian Updating Pipeline**
   Build an end-to-end pipeline that:
   - Starts with a prior from base rates
   - Ingests new data (polls, news sentiment scores) as it arrives
   - Updates the posterior using PyMC
   - Outputs a probability with credible intervals
   - Compares to the current market price and flags edges

### Advanced Exercises

7. **Full Backtesting System**
   Build a walk-forward backtester for prediction market strategies:
   - Pull historical market data from Polymarket or Kalshi APIs
   - Run your probability model at each time step
   - Simulate trades when edge > threshold
   - Calculate cumulative PnL, Sharpe ratio, max drawdown
   - Include transaction costs and slippage

8. **Model Calibration Workshop**
   Take a poorly calibrated model (e.g., a neural network outputting overconfident probabilities). Apply Platt scaling and isotonic regression. Measure improvement in Brier score and calibration curves. Document when each method works best.

9. **Multi-Model Ensemble with Bayesian Model Averaging**
   Build 3+ different models for the same event category (logistic regression, random forest, Bayesian). Implement Bayesian model averaging to combine them. Backtest the ensemble vs. individual models and document the improvement.

10. **Time-Series Regime Detection**
    Fit a Hidden Markov Model to prediction market price series for a recurring event category. Identify "calm" vs. "volatile" regimes. Test whether trading signals differ by regime and document findings.

### Capstone Project

**End-to-End Quantitative Prediction Market System**

Build a complete system that:
1. Scrapes or fetches data for one event category
2. Engineers features from raw data
3. Trains multiple probability models
4. Combines models via ensemble/BMA
5. Runs Monte Carlo simulations for uncertainty
6. Implements Bayesian updating as new information arrives
7. Backtests the strategy on historical data
8. Outputs: probability estimates, edge vs. market, suggested position sizes, performance metrics
9. Documents all assumptions, limitations, and model specifications

This capstone satisfies all four acceptance criteria:
- Build and backtest a model for one event category ✓
- Show positive expected value in backtests ✓
- Implement Bayesian updating pipeline ✓
- Document model assumptions and limitations ✓

---

## Applicability to Prediction Market Trading

This domain is the quantitative engine that powers systematic prediction market trading. Everything built here feeds directly into:

- **Portfolio Construction:** model outputs and correlations drive portfolio optimization
- **Event-Driven Trading:** feature engineering and Bayesian updating enable rapid response to catalysts
- **Algorithmic Systems:** backtesting frameworks and model pipelines become the core of automated trading systems
- **Strategy Integration:** calibrated models with documented performance become components in the overall strategy stack

Without strong quantitative modeling, prediction market trading reduces to gut feel and gambler's fallacy. This domain provides the mathematical foundation for edge detection, position sizing, and systematic profitability.
