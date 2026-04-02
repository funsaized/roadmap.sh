# Portfolio Construction & Correlation Management

**Domain Level:** Advanced
**Prerequisites:** Risk Management & Bankroll Strategy, Quantitative Modeling for Prediction Markets
**Feeds Into:** Behavioral Edge & Market Psychology, Strategy Integration & Performance Measurement

---

## A) Key Concepts

### 1. Modern Portfolio Theory (MPT) Adapted for Prediction Markets

**Mean-Variance Optimization (MVO):** The Markowitz framework for constructing portfolios that maximize expected return for a given risk level. In prediction markets, "assets" are event contracts with binary payoffs. The covariance matrix must be estimated differently than in equities since returns are bounded and discrete.

**Efficient Frontier for Binary Portfolios:** The set of optimal portfolios offering the highest expected return for each level of risk. With binary contracts, the frontier has distinct characteristics: returns are capped at contract payoff, and the distribution is Bernoulli rather than Gaussian. Constructing the frontier requires simulation or numerical methods rather than closed-form solutions.

**Risk-Free Rate Analog:** In prediction markets, the risk-free rate equivalent is the return from holding cash or investing in contracts trading near 0 or 100 (near-certain outcomes). This anchors Sharpe ratio calculations.

### 2. Correlation Estimation for Event Contracts

**Pairwise Event Correlation:** The statistical relationship between outcomes of different prediction market contracts. Unlike equity correlations derived from return time series, event correlations must be estimated from:
- Logical dependencies (e.g., "Party X wins presidency" and "Party X wins Senate" are positively correlated)
- Historical co-occurrence patterns
- Causal reasoning and domain expertise

**Implied Correlation:** Derived from market prices of related contracts. If individual event probabilities are known and a joint contract exists, the implied correlation can be backed out. Emerging in platforms like Polymarket through related market structures.

**Correlation Regimes:** Correlations between prediction market events are not static. During high-uncertainty periods (elections, crises), correlations between politically-linked markets spike. Understanding regime shifts is critical for portfolio stability.

**Correlation Matrix Construction:** Building a full NxN correlation matrix for a portfolio of N event contracts. Challenges include:
- Limited historical data for novel events
- Non-stationarity of correlations
- Ensuring the matrix is positive semi-definite

### 3. Portfolio-Level Kelly Criterion

**Single-Bet Kelly Review:** f* = (bp - q) / b, where b = odds, p = win probability, q = 1-p. Maximizes long-term geometric growth rate.

**Multi-Bet Kelly (Independent):** When holding multiple simultaneous independent bets, the optimal fraction for each bet is found by maximizing E[log(W)] across all possible outcome combinations. This is a 2^N optimization problem that requires numerical methods.

**Correlated Multi-Bet Kelly:** When bets are correlated, the joint probability distribution of outcomes must be specified. The optimization becomes:
- Maximize E[log(W)] = Σ P(outcome_i) * log(1 + Σ f_j * payoff_j(outcome_i))
- Subject to: Σ f_j <= 1, f_j >= 0

This requires specifying the full joint probability table and solving numerically (gradient descent, scipy.optimize, or similar).

**Fractional Kelly:** Betting a fraction (commonly 1/4 to 1/2) of the full Kelly amount. Reduces variance and drawdown risk at the cost of lower geometric growth. Especially important in prediction markets where probability estimates carry significant uncertainty.

### 4. Diversification Strategies

**Event Category Diversification:** Spreading positions across uncorrelated event types: politics, economics, sports, entertainment, weather, science. Research suggests portfolios of 8-12 uncorrelated events reduce volatility by ~40% while retaining ~85% of returns.

**Temporal Diversification:** Holding contracts with different expiration dates. Avoids concentration in a single resolution date where multiple correlated outcomes resolve simultaneously.

**Geographic/Domain Diversification:** Mixing domestic and international events, or spreading across different knowledge domains where your edge may vary.

**Platform Diversification:** Holding positions across multiple platforms (Kalshi, Polymarket, Metaculus, PredictIt) to reduce counterparty risk and access different market types.

### 5. Concentration Risk

**Single-Position Concentration:** The risk of having too large a fraction of capital in one contract. A common guideline is limiting any single position to 1-5% of total bankroll.

**Thematic Concentration:** Multiple positions that appear diversified but are driven by the same underlying factor. Example: holding YES on "Fed raises rates," YES on "S&P drops 5%," and YES on "Housing starts decline" are all correlated through the same macro factor.

**Resolution Date Concentration:** Having many positions resolve on the same date (e.g., election night). Even if events seem independent, simultaneous resolution creates liquidity risk and potential for correlated surprises.

### 6. Position Limits and Sizing Rules

**Maximum Position Size:** Hard caps on individual contract exposure, typically 2-5% of total capital for high-conviction bets, 0.5-1% for speculative positions.

**Sector/Theme Limits:** Capping total exposure to correlated event clusters (e.g., no more than 15-20% in US election markets).

**Platform Limits:** Maximum capital deployed on any single platform to manage counterparty risk.

**Dynamic Position Limits:** Adjusting limits based on portfolio-level metrics. Tighten limits during drawdowns; relax slightly during strong performance periods.

### 7. Hedging Strategies

**Direct Hedging:** Taking an opposing position in a related market to reduce directional exposure. Example: if long YES on "Candidate A wins presidency" at 60c, hedge by going long YES on "Opposing party wins Senate" if negatively correlated with presidential outcome.

**Cross-Market Hedging:** Using positions on one platform to hedge exposure on another. Requires understanding basis risk between platforms.

**Delta-Neutral Construction:** Combining positions so the portfolio's expected P&L is near zero for small probability movements, profiting instead from resolution or volatility changes.

**Calendar Hedging:** Offsetting near-term event risk with longer-dated positions that benefit from the same underlying trend but resolve later.

### 8. Tail Risk Management

**Black Swan Events:** Low-probability, high-impact events that can devastate concentrated portfolios. In prediction markets, these manifest as contracts at 95-99c that resolve NO (or 1-5c contracts that resolve YES).

**Tail Risk Hedging:** Buying cheap out-of-consensus contracts as insurance. A contract at 3c has a 33:1 payoff if it resolves YES. Small allocations to tail-risk positions can protect against correlated portfolio shocks.

**Stress Testing:** Simulating portfolio performance under extreme scenarios: what if all positively correlated bets lose simultaneously? What if a platform fails?

**Value at Risk (VaR) for Binary Portfolios:** Estimating the maximum loss at a given confidence level. Requires Monte Carlo simulation accounting for correlations.

### 9. Portfolio Metrics and Performance Tracking

**Sharpe Ratio:** (Portfolio Return - Risk-Free Rate) / Standard Deviation of Returns. For prediction markets, calculate using realized P&L over rolling windows. Annualize appropriately based on resolution frequency.

**Maximum Drawdown (MDD):** The largest peak-to-trough decline in portfolio value. Critical for survival; a 50% drawdown requires a 100% gain to recover. Target MDD < 20% for sustainable trading.

**Return on Capital (ROC):** Total P&L divided by average capital deployed. Accounts for the opportunity cost of capital locked in positions.

**Sortino Ratio:** Like Sharpe but only penalizes downside volatility. More appropriate for prediction markets where upside "volatility" (winning bets) is desirable.

**Win Rate and Edge Tracking:** Percentage of resolved positions that were profitable, and the average edge (expected return per dollar risked). Track by event category to identify where your edge is strongest.

**Brier Score at Portfolio Level:** Aggregate calibration metric. Are your probability estimates (and therefore position sizes) well-calibrated across the portfolio?

### 10. Rebalancing

**Trigger-Based Rebalancing:** Rebalance when position weights drift beyond target ranges (e.g., if a 3% position grows to 6% due to probability movement).

**Calendar Rebalancing:** Periodic review (weekly/monthly) of portfolio composition, correlation assumptions, and exposure limits.

**Event-Driven Rebalancing:** Adjust positions when new information changes the correlation structure or expected probabilities of held contracts.

**Transaction Cost Awareness:** Prediction markets have bid-ask spreads and sometimes fees. Rebalancing too frequently erodes returns.

### 11. Exposure Monitoring

**Real-Time P&L Tracking:** Monitoring mark-to-market portfolio value as contract prices move.

**Correlation Dashboard:** Tracking actual vs. assumed correlations as markets move and events resolve.

**Concentration Heatmap:** Visual representation of portfolio exposure by category, platform, resolution date, and theme.

**Alert Systems:** Automated notifications when position limits are breached, drawdown thresholds are hit, or correlation assumptions break down.

### Concept Relationships

```
MPT/MVO ──────────► Efficient Frontier
    │                     │
    ▼                     ▼
Correlation ──────► Portfolio-Level Kelly
Estimation              │
    │                    ▼
    ▼              Position Sizing
Diversification ◄──── & Limits
    │                    │
    ▼                    ▼
Concentration ────► Hedging Strategies
Risk                     │
    │                    ▼
    ▼              Tail Risk Mgmt
Rebalancing ◄────── │
    │                    │
    ▼                    ▼
Exposure ──────────► Performance Metrics
Monitoring              (Sharpe, MDD, ROC)
```

### Prerequisites for Other Domains

- **Behavioral Edge:** Understanding portfolio-level performance reveals where psychological biases cause systematic errors in position sizing and diversification
- **Strategy Integration:** Portfolio construction is the framework that unifies all individual strategies into a coherent trading operation

---

## B) Learning Resources

### Online Courses

1. **Investment Management with Python and Machine Learning Specialization** (EDHEC Business School via Coursera)
   - URL: https://www.coursera.org/specializations/investment-management-python-machine-learning
   - Platform: Coursera
   - Duration: ~4 months (8 hrs/week)
   - Covers: Portfolio optimization, risk management, advanced portfolio construction with Python
   - Relevance: Directly teaches MVO, risk budgeting, and portfolio analytics with code

2. **Portfolio and Risk Management** (University of Geneva via Coursera)
   - URL: https://www.coursera.org/learn/portfolio-risk-management
   - Platform: Coursera
   - Duration: ~12 hours
   - Covers: Portfolio theory, risk measures, diversification, hedging
   - Relevance: Solid theoretical foundation for adapting to prediction markets

3. **MIT OCW Finance Theory I - Portfolio Theory Lectures**
   - URL: https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/portfolio-theory/
   - Platform: MIT OpenCourseWare (free)
   - Duration: ~3 hours of video
   - Covers: Mean-variance analysis, portfolio optimization fundamentals
   - Relevance: Rigorous academic foundation

4. **Managing My Investments** (The Open University)
   - URL: https://www.open.edu/openlearn/money-business/managing-my-investments
   - Platform: OpenLearn (free)
   - Duration: ~8 hours
   - Covers: Portfolio theory application, risk-return tradeoffs
   - Relevance: Accessible introduction to portfolio concepts

### Video Tutorials and Lectures

5. **Kelly Criterion for Multiple Simultaneous Bets** (Vegapit)
   - URL: https://vegapit.com/article/numerically_solve_kelly_criterion_multiple_simultaneous_bets/
   - Format: Article with code examples
   - Covers: Numerical solution for multi-bet Kelly, mutually exclusive outcomes
   - Relevance: Directly applicable to prediction market portfolio sizing

6. **Kelly Criterion for Mutually Exclusive Outcomes** (Vegapit)
   - URL: https://vegapit.com/article/kelly-criterion-multiple-mutually-exclusive-outcomes/
   - Format: Technical article with Python code
   - Covers: Kelly optimization for multi-outcome prediction markets

7. **Prediction Markets and Implied Correlation** (Cheap Convexity Substack)
   - URL: https://cheapconvexity.substack.com/p/prediction-markets-and-implied-correlation
   - Format: Newsletter article
   - Covers: How to extract and use implied correlation from prediction market prices

8. **How to Use Prediction Markets as a Hedging Tool** (Uncover Substack)
   - URL: https://uncover.substack.com/p/how-to-use-prediction-markets-as
   - Format: Newsletter article
   - Covers: Practical hedging strategies using prediction market contracts

### Books

9. **"Active Portfolio Management" by Richard Grinold & Ronald Kahn**
   - Relevant Chapters: Chs 2-4 (risk models, alpha construction), Ch 14 (portfolio construction)
   - Difficulty: Advanced
   - Relevance: Gold standard for quantitative portfolio construction, adaptable to prediction markets

10. **"Quantitative Portfolio Management" by Michael Isichenko**
    - Relevant Chapters: Chs on risk models, portfolio optimization, performance measurement
    - Difficulty: Advanced
    - Relevance: Modern quantitative approach with practical implementation details

11. **"Fortune's Formula" by William Poundstone**
    - Relevant Chapters: Full book (history and application of Kelly criterion)
    - Difficulty: Intermediate (narrative style)
    - Relevance: Essential context for Kelly criterion in portfolio management and betting

12. **"The Kelly Capital Growth Investment Criterion" by Edward O. Thorp et al.**
    - Relevant Chapters: Papers on multi-asset Kelly, fractional Kelly, practical applications
    - Difficulty: Advanced
    - Relevance: Definitive academic collection on portfolio-level Kelly

13. **"Advances in Portfolio Construction and Implementation" by Stephen Satchell**
    - Relevant Chapters: Chs on correlation modeling, tail risk, rebalancing
    - Difficulty: Expert
    - Relevance: Advanced techniques for correlation management

### Documentation and Reference Materials

14. **Riskfolio-Lib Documentation**
    - URL: https://riskfolio-lib.readthedocs.io/
    - Covers: Portfolio optimization including Kelly criterion, risk parity, hierarchical risk parity
    - Relevance: Ready-to-use Python library for implementing portfolio optimization

15. **Where Prediction Markets Fit in Portfolios** (Investing.com)
    - URL: https://www.investing.com/analysis/where-prediction-markets-fit-in-portfolios-200674040
    - Format: Analysis article
    - Covers: Portfolio allocation frameworks incorporating prediction markets

16. **Prediction Market Trading Strategy Guide** (PredictionNews)
    - URL: https://predictionnews.com/learn/trading-strategy/
    - Format: Guide
    - Covers: Practical strategy including portfolio diversification for prediction markets

17. **Advanced Prediction Market Trading Strategies** (MetaMask)
    - URL: https://metamask.io/news/advanced-prediction-market-trading-strategies
    - Format: Article
    - Covers: Advanced strategies including portfolio-level thinking for prediction markets

### Interactive Exercises and Practice

18. **Riskfolio-Lib GitHub Repository**
    - URL: https://github.com/dcajasn/Riskfolio-Lib
    - What: Python library with example notebooks for portfolio optimization
    - Relevance: Hands-on portfolio construction with Kelly criterion support

19. **Kelly Criterion Jupyter Notebook**
    - URL: https://github.com/1kc2/The-Kelly-Criterion
    - What: Interactive notebook exploring Kelly criterion mathematics
    - Relevance: Build intuition for multi-asset Kelly through code

20. **Kelly Portfolio Optimization Project**
    - URL: https://github.com/FaridSoroush/Kelly-Portfolio-Optimization
    - What: Comparison of Kelly vs MVO strategies with Python code
    - Relevance: Directly applicable implementation patterns

21. **QuantStack Exchange: Kelly for Correlated Bets**
    - URL: https://quant.stackexchange.com/questions/68297/kelly-criterion-for-multiple-simultaneous-correlated-bets
    - What: Detailed Q&A with mathematical derivations
    - Relevance: Reference for implementing correlated Kelly

### Community Resources

22. **r/predictit** and **r/Polymarket** (Reddit)
    - URL: https://reddit.com/r/predictit and https://reddit.com/r/Polymarket
    - Portfolio construction discussions, strategy sharing

23. **r/algotrading** (Reddit)
    - URL: https://reddit.com/r/algotrading
    - Quantitative portfolio optimization discussions

24. **Two Plus Two Forums - Probability Section**
    - URL: https://forumserver.twoplustwo.com/25/probability/
    - Kelly criterion and betting portfolio discussions

25. **Quantpedia**
    - URL: https://quantpedia.com/
    - Research on portfolio strategies including concentration risk analysis

---

## C) Learning Path

### Phase 1: Portfolio Theory Foundations (Week 1-2, ~15 hours)

**Concepts:** Mean-variance optimization, efficient frontier, risk-return tradeoff, diversification principles

**Activities:**
- Watch MIT OCW Portfolio Theory lectures (3 hrs)
- Complete Coursera Portfolio and Risk Management course (12 hrs)
- Read Fortune's Formula chapters on Kelly history

**Milestone:** Can explain MPT, draw an efficient frontier, and calculate portfolio variance from a covariance matrix

### Phase 2: Correlation for Prediction Markets (Week 3-4, ~12 hours)

**Concepts:** Event correlation estimation, implied correlation, correlation regimes, correlation matrix construction

**Activities:**
- Study the Cheap Convexity article on implied correlation
- Work through correlation estimation exercises using historical Polymarket/Kalshi data
- Build a correlation matrix for 10+ prediction market contracts using logical reasoning and historical data

**Milestone:** Can construct a correlation matrix for a set of prediction market contracts with justified assumptions for each pairwise correlation

### Phase 3: Portfolio-Level Kelly Criterion (Week 5-6, ~15 hours)

**Concepts:** Multi-bet Kelly, correlated Kelly, fractional Kelly, numerical optimization

**Activities:**
- Study Vegapit articles on multi-bet Kelly (2 hrs)
- Work through the Kelly Criterion Jupyter Notebook (3 hrs)
- Implement correlated multi-bet Kelly optimizer in Python (10 hrs)
- Read selected papers from "The Kelly Capital Growth Investment Criterion"

**Milestone:** Can compute optimal position sizes for a portfolio of 5+ correlated prediction market bets using numerical optimization

### Phase 4: Position Limits, Hedging, and Risk Controls (Week 7-8, ~12 hours)

**Concepts:** Position sizing rules, concentration risk, hedging strategies, tail risk management

**Activities:**
- Design a position limit framework for your prediction market portfolio
- Practice hedging exercises: construct hedged positions for concentrated bets
- Implement tail risk stress testing via Monte Carlo simulation
- Study VaR calculation for binary portfolios

**Milestone:** Can implement portfolio-level position limits, demonstrate hedging a concentrated position, and run stress tests

### Phase 5: Performance Tracking and Rebalancing (Week 9-10, ~10 hours)

**Concepts:** Sharpe ratio, drawdown, ROC, Sortino ratio, rebalancing triggers, exposure monitoring

**Activities:**
- Build a portfolio tracking dashboard (spreadsheet or Python)
- Implement automated rebalancing alerts
- Backtest portfolio construction rules on historical prediction market data
- Calculate all key metrics on a sample portfolio

**Milestone:** Can track portfolio Sharpe, drawdown, ROC, and demonstrate trigger-based rebalancing

### Phase 6: Integration and Live Practice (Week 11-12, ~10 hours)

**Concepts:** Full portfolio management workflow, real-time monitoring, continuous improvement

**Activities:**
- Manage a paper-trading portfolio across 8-12 uncorrelated prediction market events
- Apply all position limits, hedging rules, and rebalancing triggers
- Review and adjust correlation assumptions as events resolve
- Generate weekly portfolio performance reports

**Milestone:** Can manage a diversified prediction market portfolio end-to-end with documented performance metrics

**Total Estimated Time: 10-12 weeks, ~75 hours**

---

## D) Practical Exercises

### Exercise 1: Build a Correlation Matrix (Beginner)
**Task:** Select 10 active prediction market contracts across 3+ categories. For each pair, estimate the correlation coefficient (-1 to +1) with written justification. Validate that the resulting matrix is positive semi-definite.
**Skills practiced:** Correlation estimation, domain reasoning, matrix properties

### Exercise 2: Multi-Bet Kelly Optimizer (Intermediate)
**Task:** Implement a Python function that takes a vector of probabilities, a vector of market prices, and a correlation matrix, then computes optimal Kelly fractions using scipy.optimize.minimize. Test with:
- 3 independent bets
- 3 correlated bets (correlation = 0.5)
- 5 bets with mixed correlations
Compare full Kelly vs half Kelly allocation sizes and expected growth rates.
**Skills practiced:** Numerical optimization, Kelly criterion, Python implementation

### Exercise 3: Position Limit Framework (Intermediate)
**Task:** Design and document a complete position limit framework including:
- Maximum single position size (% of bankroll)
- Maximum sector/theme exposure
- Maximum platform exposure
- Maximum same-day resolution exposure
- Rules for when limits can be adjusted
Apply this framework to a hypothetical $10,000 portfolio with 15 positions.
**Skills practiced:** Risk management, portfolio rules, concentration risk

### Exercise 4: Hedging a Concentrated Position (Intermediate)
**Task:** You hold a large YES position (5% of portfolio) on "Fed raises rates in June" at 65c. Identify 3 potential hedging contracts, estimate their correlation with your position, calculate the hedge ratio, and demonstrate the expected P&L in 4 scenarios: (a) Fed raises + hedges lose, (b) Fed raises + hedges win, (c) Fed holds + hedges lose, (d) Fed holds + hedges win.
**Skills practiced:** Hedging mechanics, correlation reasoning, scenario analysis

### Exercise 5: Portfolio Dashboard (Advanced)
**Task:** Build a portfolio tracking system (Python or spreadsheet) that:
- Tracks all open positions with entry price, current price, and size
- Calculates mark-to-market P&L
- Computes rolling Sharpe ratio (30-day, 90-day)
- Tracks maximum drawdown
- Shows concentration by category, platform, and resolution date
- Generates rebalancing alerts when positions breach limits
**Skills practiced:** Performance measurement, monitoring systems, analytics

### Exercise 6: Stress Testing and Tail Risk (Advanced)
**Task:** Using Monte Carlo simulation (10,000 trials), stress test a portfolio of 10 prediction market positions:
- Simulate outcomes using assumed correlations
- Calculate the distribution of portfolio returns
- Find the 1% and 5% VaR
- Identify which correlation assumptions have the largest impact on tail risk
- Add 2 tail-risk hedge positions and re-run the simulation
**Skills practiced:** Monte Carlo methods, VaR, tail risk, simulation

### Exercise 7: Full Portfolio Backtest (Expert)
**Task:** Using historical resolved prediction market data (Polymarket, Kalshi, or PredictIt), backtest a portfolio strategy:
- Apply Kelly sizing with estimated correlations
- Enforce position limits
- Rebalance weekly
- Track all performance metrics
- Compare results against: (a) equal-weight portfolio, (b) no position limits, (c) full Kelly vs half Kelly
Write a report analyzing the results.
**Skills practiced:** Backtesting, strategy evaluation, performance attribution

### Real-World Application

**Live Portfolio Management Project:**
Deploy a real (small stakes) or paper-trading portfolio on Kalshi or Polymarket:
1. Start with 8-12 uncorrelated positions across different categories
2. Size using fractional Kelly (quarter or half)
3. Enforce your position limit framework
4. Track performance daily in your dashboard
5. Rebalance weekly based on trigger rules
6. Generate monthly performance reports
7. After 3 months, analyze: What was your Sharpe? Max drawdown? Were your correlation assumptions accurate? Where did your edge come from?

---

## Applicability to Prediction Market Trading Mastery

Portfolio construction is the bridge between having individual market insights and running a sustainable trading operation. Without it, even accurate forecasters can go broke through concentration risk, correlated losses, and poor position sizing. This domain synthesizes everything from the prior modules (probability, pricing, risk management, quantitative modeling) into a coherent portfolio-level framework.

Key connections:
- **From Risk Management:** Individual position sizing rules scale up to portfolio-level Kelly and position limits
- **From Quantitative Modeling:** Model outputs (probability estimates) become inputs to the portfolio optimizer
- **From Arbitrage:** Cross-platform positions create counterparty exposure that portfolio construction must account for
- **To Strategy Integration:** The portfolio framework is the container for all strategies; performance measurement at the portfolio level reveals which strategies actually contribute value
- **To Behavioral Edge:** Portfolio-level tracking reveals psychological biases in your trading (overconcentration in familiar categories, underhedging winners, etc.)
