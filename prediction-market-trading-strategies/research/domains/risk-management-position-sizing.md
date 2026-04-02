# Risk Management & Position Sizing

## Domain Overview

Risk management and position sizing form the bridge between identifying profitable opportunities in prediction markets and actually extracting long-term profit from them. This domain covers the Kelly criterion, bankroll management, drawdown tolerance, ruin probability, and diversification across uncorrelated events. Without disciplined risk management, even traders with a genuine edge will eventually go broke.

**Prerequisites:** Probability & Statistics Foundations, Event Pricing & Fair Value Estimation
**Feeds into:** Portfolio Construction for Event Contracts

---

## A) Key Concepts

### 1. Kelly Criterion (Full Kelly)

The Kelly criterion is a formula that determines the optimal fraction of your bankroll to wager on a bet to maximize the long-term geometric growth rate of capital.

**Binary outcome formula:**
```
f* = (b × p - q) / b
```
Where:
- `f*` = fraction of bankroll to wager
- `b` = net odds (profit if win / stake)
- `p` = your estimated true probability of winning
- `q` = 1 - p (probability of losing)

**Prediction market simplified form:**
When a "Yes" share costs `c` and pays $1 on success:
```
f* = (p - c) / (1 - c)
```
Where `p` is your estimated probability and `c` is the share price (market-implied probability).

**Example:** You estimate 55% probability; market prices at $0.45 (45% implied). `f* = (0.55 - 0.45) / (1 - 0.45) = 0.10 / 0.55 ≈ 18.2%` of bankroll.

Kelly is the theoretical optimum for log-wealth maximization, but it assumes perfect probability estimates, which never exist in practice.

### 2. Fractional Kelly

A conservative modification where you bet a fixed fraction (typically 0.25x to 0.5x) of the full Kelly recommendation.

**Why use it:**
- Protects against estimation errors in `p` (the most dangerous input)
- Reduces variance and drawdowns substantially
- Half-Kelly achieves ~75% of full Kelly's growth rate with far less volatility
- Quarter-Kelly is common among professional bettors and quant funds

**Rule of thumb:** The less confident you are in your probability estimate, the smaller your Kelly fraction should be.

### 3. Bankroll Management

The discipline of treating your prediction market capital as a defined, separate pool with rules governing allocation.

**Core principles:**
- **Dedicated bankroll:** Money set aside exclusively for trading, separate from living expenses
- **Unit sizing:** Most practitioners bet 1-5% of bankroll per position; 2-3% is a common conservative target
- **Dynamic recalculation:** Adjust unit size as bankroll grows or shrinks (percentage-based, not fixed dollar)
- **Loss tracking:** Meticulous record of every position, entry price, exit, and outcome
- **No chasing:** Never increase size to "make back" losses

### 4. Risk of Ruin

The probability of losing your entire bankroll (or hitting some minimum threshold below which you cannot continue trading).

**Key factors affecting ruin probability:**
- **Bet size relative to bankroll:** Larger bets = exponentially higher ruin risk
- **Edge size:** Smaller edge = more vulnerable to variance
- **Number of bets:** More simultaneous large bets increase ruin risk
- **Probability estimation accuracy:** Overestimating your edge is the #1 cause of ruin

**Analytical formula (simplified for equal-sized bets):**
```
P(ruin) = ((1 - edge) / (1 + edge))^(bankroll / bet_size)
```

**Target:** Professional prediction market traders aim for ruin probability below 1% (0.01).

### 5. Drawdown and Drawdown Tolerance

**Drawdown:** The peak-to-trough decline in your bankroll before a new high is reached. Expressed as a percentage.

**Maximum drawdown (MDD):** The largest drawdown observed over a given period.

**Drawdown tolerance:** Your psychological and financial ability to withstand drawdowns without abandoning your strategy.

**Relationship to Kelly:**
- Full Kelly can produce drawdowns of 50%+ even with a positive edge
- Half Kelly typically limits max drawdown to ~25%
- Quarter Kelly keeps drawdowns more manageable (~12-15%)

### 6. Expected Value (EV) vs. Risk-Adjusted Return

**EV** alone is insufficient for position sizing. Two bets can have identical EV but wildly different risk profiles.

**Risk-adjusted metrics:**
- **Sharpe-like ratio for bets:** (Expected return) / (Standard deviation of returns)
- **Kelly growth rate:** The expected log-return, which naturally penalizes variance
- **Return per unit of risk:** Comparing opportunities on a risk-adjusted basis helps allocate capital efficiently

### 7. Monte Carlo Simulation

A computational technique that runs thousands of simulated betting sequences with random outcomes to estimate the distribution of possible portfolio paths.

**Applications in prediction market risk management:**
- Estimate probability of ruin over N bets
- Calculate expected drawdown distribution
- Stress-test a strategy under different edge assumptions
- Compare position sizing approaches (full Kelly vs. fractional vs. fixed)
- Model the impact of correlated losses

**Implementation basics:**
1. Define parameters: bankroll, bet sizes, win probabilities, payout ratios
2. Simulate thousands of random bet sequences
3. Track bankroll path for each simulation
4. Aggregate statistics: ruin rate, median final bankroll, max drawdown distribution, percentile outcomes

### 8. Correlation and Diversification Across Events

**Uncorrelated events:** Events whose outcomes have no statistical relationship (e.g., an election result and a sports outcome). Betting on uncorrelated events reduces portfolio variance.

**Correlated events:** Events that tend to resolve in the same direction (e.g., multiple markets about the same political party winning different races). Correlated bets concentrate risk.

**Diversification benefit:**
- For N uncorrelated bets of equal size, portfolio standard deviation scales as `1/sqrt(N)`
- Prediction markets offer natural diversification because many events are genuinely independent
- However, macro events (recessions, geopolitical crises) can create hidden correlations

**Practical application:**
- Map your positions by event category and identify correlation clusters
- Limit exposure to any single correlated cluster
- Seek genuinely independent events across sports, politics, economics, weather, etc.

### 9. Position Limits and Exposure Management

**Per-position limits:** Maximum percentage of bankroll allocated to any single market (typically 2-5% for conservative, up to 10% for high-conviction).

**Category exposure limits:** Maximum total allocation to correlated markets (e.g., no more than 15-20% in "US election" markets collectively).

**Platform-imposed limits:** Kalshi caps retail positions at $25,000 per market; Polymarket has similar accountability levels for regulated contracts.

**Gross vs. net exposure:** Track both your total capital at risk (gross) and your directional exposure (net) across all positions.

### 10. Bankroll Segmentation and Staking Plans

**Flat staking:** Equal bet size on every position. Simple, but doesn't optimize for edge differences.

**Proportional staking (Kelly-based):** Size each bet proportional to your estimated edge. More efficient but requires accurate edge estimates.

**Tiered staking:** Categorize bets into confidence tiers (high/medium/low) with different allocation percentages per tier.

**Bankroll segmentation:** Divide your total bankroll across different strategies or market categories with independent sub-bankrolls.

### 11. Simultaneous Kelly for Multiple Bets

When you have multiple open positions, the standard single-bet Kelly formula doesn't account for how they interact.

**Approaches:**
- **Independent Kelly:** Calculate Kelly for each bet independently, then scale down if total allocation exceeds 100%
- **Multivariate Kelly:** Solve a system of equations accounting for correlations (more accurate but computationally complex)
- **Practical heuristic:** Calculate individual Kelly fractions, then apply a global scaling factor so total exposure stays within risk limits

### 12. Gambler's Ruin Problem (Classical)

The mathematical foundation showing that a gambler with finite capital playing against an opponent with infinite capital (or a house edge) will eventually go broke with probability 1 if they never stop.

**Relevance:** Even small negative edges compound into certainty of ruin over long horizons. This underscores why confirming you have a genuine positive edge before sizing up is non-negotiable.

### Concept Relationships

```
Probability Estimation (from prior domains)
    ↓
Kelly Criterion (optimal sizing given edge)
    ↓
Fractional Kelly (practical conservative adjustment)
    ↓
Position Limits + Exposure Management (portfolio-level controls)
    ↓
Monte Carlo Simulation (validate ruin probability)
    ↓
Diversification (reduce variance via uncorrelated events)
    ↓
Bankroll Management (operational discipline tying it all together)
```

### Prerequisites for Other Domains

- **Portfolio Construction:** Requires Kelly sizing, correlation analysis, and position limit frameworks
- **Quantitative Modeling & Backtesting:** Risk metrics (Sharpe, drawdown, ruin probability) are outputs that backtesting must evaluate
- **Algorithmic Trading:** Automated systems need programmatic position sizing and risk checks

---

## B) Learning Resources

### Online Courses

1. **Zerodha Varsity: Kelly's Criterion** (Free)
   - URL: https://zerodha.com/varsity/chapter/kellys-criterion/
   - Platform: Zerodha Varsity
   - Duration: ~2 hours
   - Covers Kelly criterion with practical trading examples

2. **QuantInsti: Monte Carlo Simulation** (Free blog + paid courses)
   - URL: https://blog.quantinsti.com/monte-carlo-simulation/
   - Platform: QuantInsti
   - Duration: ~3 hours for the free material
   - Python-based Monte Carlo for risk estimation

3. **Coursera: Investment Management with Python and Machine Learning** (Paid)
   - URL: https://www.coursera.org/specializations/investment-management-python-machine-learning
   - Platform: Coursera (EDHEC Business School)
   - Duration: ~4 months (part-time)
   - Covers portfolio risk, drawdown analysis, Monte Carlo methods

4. **PyQuant News: Risk of Ruin Guide** (Free)
   - URL: https://www.pyquantnews.com/free-python-resources/understanding-and-managing-risk-of-ruin
   - Platform: PyQuant News
   - Duration: ~1.5 hours
   - Python implementation of risk of ruin calculations

### Video Tutorials

5. **Tastylive: Kelly Criterion Explained** (Free)
   - URL: https://www.tastylive.com/news-insights/kelly-criterion-explained-smarter-position-sizing-traders
   - Platform: Tastylive
   - Duration: ~30 minutes
   - Practical walkthrough of Kelly for position sizing

6. **YouTube: Kelly Criterion - Ed Thorp's Approach** (Free)
   - URL: https://www.youtube.com/watch?v=IgtvMRSQCXY
   - Duration: ~20 minutes
   - Historical and mathematical background

7. **Kaggle: Monte Carlo Simulation in Sports Betting** (Free, interactive)
   - URL: https://www.kaggle.com/code/haraldschellnast/monte-carlo-simulation-in-sports-betting
   - Platform: Kaggle Notebooks
   - Duration: ~2 hours (hands-on)
   - Runnable Python notebook with Monte Carlo for betting

### Books

8. **"Fortune's Formula" by William Poundstone**
   - Relevant chapters: All (narrative history of Kelly criterion)
   - Difficulty: Beginner-Intermediate
   - The definitive popular account of Kelly criterion development and application

9. **"The Kelly Capital Growth Investment Criterion" edited by MacLean, Thorp, and Ziemba**
   - URL: https://www.edwardothorp.com/books/kelly-capital-growth-investment-criterion/
   - Relevant chapters: Parts I-III (theory), Part IV (applications)
   - Difficulty: Advanced
   - Comprehensive academic collection of papers on Kelly criterion

10. **"A Man for All Markets" by Edward O. Thorp**
    - Relevant chapters: Ch. 6-10 (applying mathematical edge), Ch. 25-27 (risk management)
    - Difficulty: Intermediate
    - First-person account of applying Kelly to blackjack and financial markets

11. **"The Mathematics of Gambling" by Edward O. Thorp**
    - Relevant chapters: Ch. on bankroll requirements and ruin probability
    - Difficulty: Intermediate
    - Compact mathematical treatment of gambling risk management

12. **"Quantitative Trading" by Ernest Chan**
    - Relevant chapters: Ch. 6 (Money and Risk Management)
    - Difficulty: Intermediate-Advanced
    - Practical Kelly criterion for algorithmic trading with code examples

### Documentation and Reference Materials

13. **Wikipedia: Kelly Criterion**
    - URL: https://en.wikipedia.org/wiki/Kelly_criterion
    - Comprehensive mathematical derivation and variants

14. **Wikipedia: Risk of Ruin**
    - URL: https://en.wikipedia.org/wiki/Risk_of_ruin
    - Formal treatment of ruin probability formulas

15. **BettorEdge: Using Kelly Criterion with Prediction Markets**
    - URL: https://www.bettoredge.com/post/using-kelly-criterion-with-predicition-markets
    - Prediction-market-specific Kelly walkthrough

16. **Quantified Strategies: Risk of Ruin in Trading**
    - URL: https://www.quantifiedstrategies.com/risk-of-ruin-in-trading/
    - Practical risk of ruin calculator and explanation

17. **Kalshi Contract Terms (CFTC-regulated position limits)**
    - URL: https://kalshi-public-docs.s3.amazonaws.com/contract_terms/POLITICALECONOMICEVENTS.pdf
    - Official position limit documentation for event contracts

### Interactive Exercises and Practice

18. **Kaggle Monte Carlo Notebook** (referenced above)
    - URL: https://www.kaggle.com/code/haraldschellnast/monte-carlo-simulation-in-sports-betting
    - Runnable Python notebook

19. **TradeSearcher Kelly Criterion Simulator**
    - URL: https://tradesearcher.ai/tools/kelly-criterion-simulator
    - Interactive web tool for Kelly calculation

20. **Towards Data Science: Monte Carlo Simulation in Python**
    - URL: https://towardsdatascience.com/how-to-create-a-monte-carlo-simulation-using-python-c24634a0978a/
    - Step-by-step Python tutorial

### GitHub Repositories

21. **Kelly Portfolio Optimization (FaridSoroush)**
    - URL: https://github.com/FaridSoroush/Kelly-Portfolio-Optimization
    - Python implementation of Kelly for portfolio allocation

22. **Kelly Criterion Portfolio Optimizer (TxmJxhn)**
    - URL: https://github.com/TxmJxhn/Kelly-Criterion-Portfolio-Optimizer
    - Portfolio-level Kelly optimization tool

23. **Real Kelly for Independent Concurrent Outcomes (BettingIsCool)**
    - URL: https://github.com/BettingIsCool/real_kelly-independent_concurrent_outcomes-
    - Handles simultaneous Kelly for multiple independent bets

24. **The Kelly Criterion Jupyter Notebook (1kc2)**
    - URL: https://github.com/1kc2/The-Kelly-Criterion/blob/main/The%20Kelly%20Criterion.ipynb
    - Educational notebook with derivations and simulations

25. **Kelly Criterion (coreych)**
    - URL: https://github.com/coreych/kelly-criterion
    - Clean Python implementation

### Community Resources

26. **r/sportsbook** - Bankroll management and Kelly discussions
    - URL: https://www.reddit.com/r/sportsbook/
27. **r/algotrading** - Position sizing and risk management for automated strategies
    - URL: https://www.reddit.com/r/algotrading/
28. **Polymarket Discord** - Active community discussing prediction market risk
29. **Kalshi community forums** - Platform-specific position management discussions
30. **Quantified Strategies Blog**
    - URL: https://www.quantifiedstrategies.com/
    - Regular articles on risk management and Kelly

### Podcasts

31. **Flirting with Models (Corey Hoffstein)** - Portfolio risk management episodes
    - Available on major podcast platforms
32. **Chat with Traders** - Episodes on position sizing and bankroll management
    - URL: https://chatwithtraders.com/

---

## C) Learning Path

### Phase 1: Foundations (Week 1, ~8 hours)
**Concepts:** Bankroll management basics, risk of ruin concept, gambler's ruin problem

- Read BettorEdge Kelly article for prediction market context
- Read Wikipedia: Risk of Ruin for mathematical background
- Read "Fortune's Formula" (or first 5 chapters minimum)
- **Milestone:** Can explain why a positive-edge bettor can still go broke

### Phase 2: Kelly Criterion Deep Dive (Week 2, ~10 hours)
**Concepts:** Full Kelly formula, derivation intuition, Kelly for binary prediction markets, limitations of Kelly

- Complete Zerodha Varsity Kelly chapter
- Watch Tastylive Kelly video
- Work through Wikipedia Kelly criterion mathematical derivation
- Practice Kelly calculations on paper with prediction market scenarios
- **Milestone:** Can calculate Kelly-optimal position size for any prediction market contract given your estimated probability and market price

### Phase 3: Fractional Kelly and Practical Sizing (Week 3, ~8 hours)
**Concepts:** Fractional Kelly, staking plans, position limits, exposure management

- Read Quantified Strategies articles on Kelly dangers and alternatives
- Study Kalshi/Polymarket position limit documentation
- Design a personal staking plan with position and category limits
- **Milestone:** Have a written risk management rulebook for your own trading

### Phase 4: Monte Carlo Simulation (Week 4, ~12 hours)
**Concepts:** Monte Carlo methods, simulating bankroll paths, estimating ruin probability empirically

- Complete Kaggle Monte Carlo notebook (hands-on)
- Follow Towards Data Science Python tutorial
- Build your own Monte Carlo simulator for prediction market positions
- **Milestone:** Can run Monte Carlo simulations and report ruin probability, median outcome, and drawdown distribution

### Phase 5: Diversification and Multi-Bet Management (Week 5, ~8 hours)
**Concepts:** Correlation between events, simultaneous Kelly, portfolio-level risk, category exposure

- Study GitHub repos for multi-bet Kelly (BettingIsCool, FaridSoroush)
- Map correlation structure across prediction market categories
- Extend your Monte Carlo simulator to handle correlated positions
- **Milestone:** Can construct a diversified prediction market portfolio with ruin probability below 1%

### Phase 6: Integration and Stress Testing (Week 6, ~6 hours)
**Concepts:** Combining all elements, stress testing under adverse scenarios, edge deterioration

- Stress test your framework with pessimistic assumptions (edge 50% smaller than estimated)
- Backtest position sizing against historical prediction market data if available
- Review and refine your risk management rulebook
- **Milestone:** Complete risk management system ready for live trading

**Total estimated time: 6 weeks, ~52 hours**

---

## D) Practical Exercises

### Exercise 1: Kelly Calculator (Beginner)
Build a Python function that takes your estimated probability and market price as inputs and returns:
- Full Kelly fraction
- Half Kelly fraction
- Quarter Kelly fraction
- Dollar amount to bet for each, given a bankroll

Test with 10 different prediction market scenarios varying from small edge (2%) to large edge (20%).

### Exercise 2: Risk of Ruin Spreadsheet (Beginner)
Create a spreadsheet that calculates analytical risk of ruin given:
- Bankroll size
- Bet size (as % of bankroll)
- Win rate
- Average payout ratio

Show how ruin probability changes as bet size increases from 1% to 25% of bankroll.

### Exercise 3: Monte Carlo Bankroll Simulator (Intermediate)
Write a Python script that:
1. Simulates 10,000 paths of 500 bets each
2. Tracks bankroll evolution for each path
3. Calculates: ruin rate, median final bankroll, 5th/95th percentile outcomes, maximum drawdown distribution
4. Plots 50 sample paths and a histogram of final bankrolls
5. Compare results for full Kelly, half Kelly, and quarter Kelly sizing

### Exercise 4: Correlation Impact Analysis (Intermediate)
Take a hypothetical portfolio of 10 prediction market positions. Simulate outcomes under three scenarios:
1. All events fully independent (correlation = 0)
2. Half the events correlated in pairs (correlation = 0.5)
3. All events correlated (correlation = 0.8)

Measure how ruin probability and max drawdown change across scenarios.

### Exercise 5: Personal Risk Management Framework (Advanced)
Design a complete risk management system for prediction market trading:
- Define your bankroll and maximum acceptable drawdown
- Set per-position limits (Kelly fraction, max allocation)
- Set per-category exposure limits
- Build a Monte Carlo model to verify ruin probability < 1%
- Document everything in a trading plan

### Exercise 6: Edge Sensitivity Analysis (Advanced)
Using your Monte Carlo simulator, analyze what happens to your portfolio if your actual edge is:
- 100% of estimated (base case)
- 75% of estimated
- 50% of estimated
- 25% of estimated
- 0% (no edge at all)

Plot ruin probability and expected growth rate as a function of edge accuracy. This demonstrates why fractional Kelly is essential in practice.

### Exercise 7: Real Market Application (Advanced)
Pick 5 active markets on Kalshi or Polymarket. For each:
1. Estimate your probability using research methods from prior domains
2. Calculate Kelly-optimal position
3. Apply your fractional Kelly and position limit rules
4. Run a Monte Carlo simulation of the combined portfolio
5. Document your position sizes, rationale, and expected risk metrics

---

## Applicability to Prediction Market Trading Mastery

This domain is the critical control layer that prevents a profitable strategy from blowing up. Key connections:

- **From prior domains:** Probability estimation (Domain 1) feeds the `p` parameter in Kelly; fair value estimation (Domain 4) determines your edge; edge identification (Domain 5) tells you where to deploy capital
- **To future domains:** Portfolio Construction (Domain 8) builds on the risk framework developed here; backtesting (Domain 9) uses these risk metrics as evaluation criteria; algorithmic trading (Domain 12) automates the position sizing rules you design here

Without mastering risk management, every other skill in this roadmap becomes academic. This is where theory meets capital preservation.
