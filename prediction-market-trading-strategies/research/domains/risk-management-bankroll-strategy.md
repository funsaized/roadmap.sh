# Risk Management & Bankroll Strategy

## Domain Overview

This domain covers the mathematical and practical foundations for sizing positions, managing capital, and surviving long enough for your edge to compound in prediction markets. It bridges the gap between having a forecasting edge (covered in prior domains) and translating that edge into sustainable profit growth.

Core topics: Kelly criterion (full and fractional), bankroll management, risk of ruin, position sizing, correlation risk, drawdown management, EV vs variance tradeoff, and diversification.

---

## A) Key Concepts

### 1. Expected Value (EV) and Edge

**What it is:** The average profit per dollar wagered over many repetitions. Edge = your estimated probability minus the implied probability from market price.

**Formula:** `EV = (p × profit_if_win) - (q × loss_if_lose)` where `p` = your probability, `q = 1 - p`.

**Why it matters:** No position sizing strategy can save a negative-EV portfolio. Edge is the prerequisite for everything else in this domain.

**Relation to other concepts:** Feeds directly into Kelly formula as the numerator. Without accurate edge estimation (from the Forecasting & Calibration domain), all sizing calculations are garbage-in-garbage-out.

### 2. The Kelly Criterion (Full Kelly)

**What it is:** A formula that maximizes the long-term geometric growth rate of wealth by determining the optimal fraction of bankroll to wager.

**Formula for binary outcomes:** `f* = (bp - q) / b`
- `f*` = fraction of bankroll to bet
- `b` = net odds (profit per $1 risked; for a market price of $0.40 on an outcome you think is 60% likely, `b = 0.60/0.40 = 1.5`)
- `p` = your estimated true probability of winning
- `q` = 1 - p

**Equivalent formulation for prediction markets:** `f* = p - (q / b)` or more intuitively: `f* = p - (market_price / (1 - market_price))` when buying YES contracts.

**Key properties:**
- Maximizes log-utility (geometric growth rate)
- Bet size is proportional to edge magnitude
- Returns 0 or negative when you have no edge (don't bet)
- Assumes you know the true probability exactly (you don't)

**Prerequisites for other domains:** Foundation for portfolio construction, multi-market strategies, and automated trading systems.

### 3. Fractional Kelly

**What it is:** Betting a fixed fraction (typically 25-50%) of the full Kelly amount. Half-Kelly is most common.

**Why it's preferred in practice:**
1. **Estimation error buffer:** You never know the true probability. Overbetting (betting more than true Kelly) is far more destructive than underbetting. Fractional Kelly provides margin of safety.
2. **Drawdown reduction:** Full Kelly has ~50% chance of a 50% drawdown at some point. Half-Kelly reduces this to ~12.5%. Quarter-Kelly brings it below 1%.
3. **Volatility reduction:** Half-Kelly captures ~75% of the growth rate with ~50% of the volatility. The Sharpe ratio actually improves.
4. **Psychological sustainability:** Smaller swings make it possible to stick with the strategy through losing streaks.

**Rule of thumb:** If your confidence in probability estimates is moderate, use quarter-Kelly. If you have strong calibration data, half-Kelly. Never go above full Kelly.

### 4. Risk of Ruin

**What it is:** The probability that your bankroll hits zero (or a predefined "bust" threshold) before reaching a target.

**Simplified formula (equal bet sizes):** `RoR = ((1 - edge) / (1 + edge))^(capital_units)`
where `capital_units = bankroll / amount_risked_per_bet`.

**Key insight:** Risk of ruin decreases *exponentially* as you reduce position size. Going from 5% risk per bet to 2% doesn't halve your ruin risk; it reduces it by orders of magnitude.

**Target:** Professional bettors and traders target risk of ruin below 1%, often below 0.1%.

**Relation to other concepts:** Risk of ruin is the survival constraint that upper-bounds your Kelly fraction. It connects to drawdown management as its continuous analog.

### 5. Position Sizing

**What it is:** The broader discipline of determining how much capital to allocate to each individual trade or market position.

**Methods beyond Kelly:**
- **Fixed percentage:** Risk a constant % of current bankroll per trade (e.g., 1-2%). Simple, robust, doesn't require probability estimates.
- **Fixed dollar amount:** Risk a set dollar amount. Doesn't scale with bankroll growth or shrinkage.
- **Volatility-adjusted:** Size positions inversely proportional to their expected volatility. More volatile markets get smaller allocations.
- **Kelly-based:** Use the Kelly formula with fractional adjustment.

**Prediction market specifics:** Binary contracts have bounded loss (you can't lose more than your stake), which simplifies position sizing vs. leveraged instruments. But you still need to manage total portfolio exposure.

### 6. Bankroll Management

**What it is:** The overarching discipline of segregating, protecting, and growing a dedicated pool of capital for prediction market trading.

**Core principles:**
- **Segregation:** Trading capital is separate from living expenses. Never risk money you need.
- **Unit sizing:** Define a standard "unit" (typically 1-3% of bankroll). All positions are expressed in units.
- **Dynamic adjustment:** As bankroll grows/shrinks, unit size adjusts proportionally (this is built into Kelly naturally).
- **Stop-loss rules:** Define maximum drawdown tolerance (e.g., reduce position sizes by 50% if bankroll drops 20% from peak).
- **Withdrawal rules:** Only withdraw from profits above the starting bankroll to preserve compound growth.

### 7. Drawdown Management

**What it is:** Strategies for limiting and recovering from peak-to-trough declines in bankroll.

**Key metrics:**
- **Maximum drawdown:** The largest percentage drop from a peak to subsequent trough.
- **Recovery time:** How long it takes to return to the prior peak after a drawdown.
- **Drawdown duration:** Total time spent below the prior peak.

**Strategies:**
- **Fractional Kelly:** The primary defense. Quarter-Kelly keeps max drawdown manageable.
- **Drawdown-triggered deleveraging:** Reduce bet sizes when in a drawdown (e.g., cut to half-Kelly if down 15%).
- **Correlation monitoring:** Drawdowns accelerate when correlated positions move against you simultaneously.
- **Risk-constrained Kelly:** Variant that maximizes growth rate subject to a maximum acceptable drawdown probability.

**Relation:** Drawdown management is where theory meets psychology. The best strategy is one you can actually follow through a losing streak.

### 8. EV vs Variance Tradeoff

**What it is:** The fundamental tension between maximizing expected returns and minimizing the volatility of those returns.

**Key insight:** The geometric mean return (what actually compounds) equals the arithmetic mean minus half the variance: `G ≈ μ - σ²/2`. Higher variance directly reduces compound growth even with the same average return.

**Implications for prediction markets:**
- A portfolio of many small-edge bets with low variance will compound faster than a few high-edge bets with high variance.
- This mathematically justifies diversification even when individual positions have different edge sizes.
- Kelly criterion inherently optimizes this tradeoff by maximizing log-wealth (which penalizes variance).

### 9. Correlation Risk

**What it is:** The risk that multiple positions in your portfolio are exposed to the same underlying factor, causing them to win or lose together.

**Examples in prediction markets:**
- Multiple election markets that all depend on the same candidate's performance
- Economic indicator markets that move together during macro shocks
- Platform-specific risks (regulatory action affecting all markets on one platform)

**Impact on position sizing:** If you have N correlated positions, your effective exposure is much larger than the sum of individual position sizes suggests. Naive Kelly applied to each position independently will overbet the portfolio.

**Mitigation:**
- **Correlation-adjusted Kelly:** Use multivariate Kelly that accounts for the covariance matrix of outcomes.
- **Exposure caps per factor:** Limit total capital exposed to any single underlying theme (e.g., max 15% on US election-related markets).
- **Stress testing:** Ask "what happens if all my correlated positions lose simultaneously?"

### 10. Diversification in Prediction Markets

**What it is:** Spreading capital across uncorrelated or weakly-correlated markets to reduce portfolio variance without sacrificing expected return.

**Dimensions of diversification:**
- **Event type:** Politics, sports, economics, science, entertainment
- **Time horizon:** Mix short-term (days/weeks) and long-term (months) positions
- **Direction:** Balance YES and NO positions across the portfolio
- **Platform:** Spread across Kalshi, Polymarket, Robinhood Derivatives to reduce platform risk
- **Geography:** US, international, global events

**Relation to Kelly:** The multi-asset Kelly criterion naturally diversifies by allocating smaller fractions to each of many uncorrelated bets. A diversified portfolio of 20+ uncorrelated small-edge bets can grow faster with less risk than a concentrated portfolio of 3-5 high-edge bets.

### Concept Dependency Map

```
EV & Edge (prerequisite: Forecasting & Calibration domain)
  └─→ Kelly Criterion (Full)
       ├─→ Fractional Kelly
       │    └─→ Drawdown Management
       ├─→ Risk of Ruin
       └─→ Position Sizing
            ├─→ Bankroll Management
            ├─→ Correlation Risk
            │    └─→ Diversification
            └─→ EV vs Variance Tradeoff
```

**Cross-domain prerequisites:**
- **For Portfolio Construction domain:** Kelly criterion, correlation risk, diversification
- **For Automated Trading domain:** Position sizing algorithms, dynamic bankroll adjustment
- **For Behavioral & Psychological domain:** Drawdown management, fractional Kelly (psychological sustainability)

---

## B) Learning Resources

### Online Courses

1. **QuantInsti: Risk-Constrained Kelly Criterion** (Blog + Code Tutorial)
   - URL: https://blog.quantinsti.com/risk-constrained-kelly-criterion/
   - Platform: QuantInsti (free blog post with Python code)
   - Duration: ~2 hours to work through
   - Focus: Kelly criterion with explicit drawdown constraints, Python implementation

2. **Quantpedia: Beware of Excessive Leverage - Introduction to Kelly and Optimal F**
   - URL: https://quantpedia.com/beware-of-excessive-leverage-introduction-to-kelly-and-optimal-f/
   - Platform: Quantpedia (free article)
   - Duration: ~1 hour
   - Focus: Comparing Kelly to Optimal F, practical leverage management

3. **CQF Institute: What is the Kelly Criterion?**
   - URL: https://www.cqf.com/blog/quant-finance-101/what-is-the-kelly-criterion
   - Platform: Certificate in Quantitative Finance (free intro article)
   - Duration: ~30 minutes
   - Focus: Quant finance perspective on Kelly, good for building mathematical intuition

### Video Tutorials & Lectures

4. **Tastylive: Kelly Criterion Explained - Smarter Position Sizing for Traders**
   - URL: https://www.tastylive.com/news-insights/kelly-criterion-explained-smarter-position-sizing-traders
   - Platform: Tastylive (free video + article)
   - Duration: ~20 minutes
   - Focus: Practical application for active traders, EV calculation, drawdown context

5. **Ole Peters - Ergodicity Economics and the Kelly Criterion** (YouTube lectures)
   - Search: "Ole Peters ergodicity economics Kelly criterion" on YouTube
   - Platform: Various conference recordings
   - Duration: ~1-2 hours across multiple talks
   - Focus: Deep theoretical foundation for why geometric growth (Kelly) beats arithmetic optimization

6. **MIT OpenCourseWare 18.S096: Topics in Mathematics with Applications in Finance**
   - URL: https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/
   - Platform: MIT OCW (free)
   - Duration: Select Lectures 18-20 on portfolio theory and risk (~3 hours)
   - Focus: Mathematical portfolio theory, mean-variance optimization, risk management foundations

### Books

7. **"Fortune's Formula" by William Poundstone**
   - Difficulty: Beginner-Intermediate (narrative nonfiction)
   - Relevant chapters: All (the entire book covers Kelly criterion history and applications)
   - Why: The definitive popular account of Kelly criterion, from Bell Labs to Wall Street. Essential context for understanding why this math matters.

8. **"The Kelly Capital Growth Investment Criterion" by Edward O. Thorp, Leonard C. MacLean, William T. Ziemba (editors)**
   - Difficulty: Advanced
   - Relevant chapters: Parts I-III (theory), Part IV (practical applications)
   - Why: The academic bible of Kelly criterion. Contains the original papers plus decades of extensions. Reference when you need rigorous proofs.

9. **"Beat the Market" by Edward O. Thorp**
   - Difficulty: Intermediate
   - Relevant chapters: Chapters on position sizing and risk management
   - Why: Thorp pioneered applying Kelly to financial markets. His practical insights on fractional Kelly and risk management are directly applicable.

10. **"Trading and Exchanges" by Larry Harris**
    - Difficulty: Intermediate-Advanced
    - Relevant chapters: Chapters on risk management, position limits, and portfolio management
    - Why: Comprehensive coverage of market microstructure risk management principles.

11. **"The Mathematics of Gambling" by Edward O. Thorp**
    - Difficulty: Intermediate
    - Why: Foundational text connecting probability theory to practical bankroll management.

### Documentation & Reference Materials

12. **Wikipedia: Kelly Criterion**
    - URL: https://en.wikipedia.org/wiki/Kelly_criterion
    - Focus: Comprehensive mathematical treatment, multi-asset generalization, proofs

13. **Pinnacle Betting Resources: Kelly Criterion Series**
    - Part 1: https://www.pinnacle.com/betting-resources/en/betting-strategy/how-to-use-kelly-criterion-for-betting/2bt2lk6k2qwq7qj8
    - Part 2 (Fractional Kelly): https://www.pinnacle.com/betting-resources/en/betting-strategy/revisiting-the-kelly-criterion-part-2-fractional-kelly/gbd27z9nljvgflgg
    - Part 3 (Generalized Kelly): https://www.pinnacle.com/betting-resources/en/betting-strategy/the-real-kelly-criterion-a-critical-analysis-of-the-popular-staking-method/hzkjtfcb3knyn9cj
    - Focus: Excellent practical series covering basic through generalized Kelly, with betting-specific examples

14. **QuantStart: Money Management via the Kelly Criterion**
    - URL: https://www.quantstart.com/articles/Money-Management-via-the-Kelly-Criterion/
    - Focus: Algorithmic trading perspective, portfolio allocation, rebalancing frequency

15. **Interactive Brokers: The Risk-Constrained Kelly Criterion**
    - URL: https://www.interactivebrokers.com/campus/ibkr-quant-news/the-risk-constrained-kelly-criterion-from-the-foundations-to-trading-part-i/
    - Focus: Drawdown-constrained variant of Kelly, professional trading context

### GitHub Repositories & Open Source

16. **keeks - Bankroll allocation strategies in Python**
    - URL: https://github.com/wdm0006/keeks
    - Focus: Kelly, fractional Kelly, drawdown-adjusted Kelly implementations. Includes simulation tools.

17. **bet-optimizer - Kelly Criterion bet sizing**
    - URL: https://github.com/subodh101/bet-optimizer
    - Focus: Simple Python package for calculating optimal bet sizes using Kelly.

18. **The-Kelly-Criterion - Jupyter Notebook walkthrough**
    - URL: https://github.com/1kc2/The-Kelly-Criterion
    - Focus: Interactive notebook covering Kelly theory and practical application.

19. **real_kelly-mutually_exclusive_outcomes - Generalized Kelly for multi-outcome markets**
    - URL: https://github.com/BettingIsCool/real_kelly-mutually_exclusive_outcomes-
    - Focus: Kelly sizing for mutually exclusive outcomes (futures bets, multi-way markets).

### Community Resources

20. **r/algotrading** (Reddit)
    - URL: https://reddit.com/r/algotrading
    - Focus: Discussions on Kelly criterion implementation, position sizing algorithms

21. **r/algobetting** (Reddit)
    - URL: https://reddit.com/r/algobetting
    - Focus: Kelly criterion for betting markets, bankroll management strategies

22. **Quant StackExchange: Kelly Criterion tag**
    - URL: https://quant.stackexchange.com/questions/tagged/kelly-criterion
    - Focus: Technical Q&A on multi-asset Kelly, correlation handling, implementation details

23. **r/predictionmarkets** (Reddit)
    - URL: https://reddit.com/r/predictionmarkets
    - Focus: Platform-specific strategies, bankroll management discussions

---

## C) Learning Path

### Phase 1: Foundations (Week 1, ~8 hours)

**Concepts:** EV & Edge, Basic Kelly Formula, Bankroll Management basics

**Activities:**
1. Read "Fortune's Formula" (or at minimum chapters 1-8) for context and intuition (~4 hours)
2. Read Wikipedia Kelly criterion article for mathematical grounding (~1 hour)
3. Work through CQF Institute intro article (~30 min)
4. Watch Tastylive Kelly criterion video (~30 min)
5. Hand-calculate Kelly sizes for 10 example prediction market scenarios (~2 hours):
   - Market price $0.30, your estimate 45%
   - Market price $0.60, your estimate 70%
   - Market price $0.50, your estimate 55%
   - (etc., varying edge magnitude and market price)

**Milestone:** Can calculate full Kelly bet size for any binary prediction market position from memory. Understand why negative Kelly means "don't bet."

### Phase 2: Practical Risk Management (Week 2, ~10 hours)

**Concepts:** Fractional Kelly, Risk of Ruin, Drawdown Management

**Activities:**
1. Read Pinnacle series (all 3 parts) on Kelly criterion (~2 hours)
2. Read QuantStart article on money management via Kelly (~1 hour)
3. Read Interactive Brokers risk-constrained Kelly article (~1 hour)
4. Clone the `keeks` GitHub repo and run simulations comparing full Kelly, half-Kelly, and quarter-Kelly over 1000 bet sequences (~3 hours):
   - Measure: growth rate, max drawdown, risk of ruin
   - Vary: edge magnitude, number of bets, probability estimation error
5. Build a risk-of-ruin calculator in Python or a spreadsheet (~2 hours)
6. Calculate the bankroll needed to maintain <1% risk of ruin across 10+ simultaneous positions (~1 hour)

**Milestone:** Can explain (with simulation data) why half-Kelly typically beats full Kelly in practice. Can calculate risk of ruin for a given position sizing strategy.

### Phase 3: Portfolio-Level Risk (Week 3, ~8 hours)

**Concepts:** Correlation Risk, Diversification, EV vs Variance Tradeoff, Multi-Asset Kelly

**Activities:**
1. Read the generalized Kelly article from Pinnacle (Part 3) deeply (~1 hour)
2. Study the Quant StackExchange thread on Kelly for correlated bets (~1 hour)
3. Clone `real_kelly-mutually_exclusive_outcomes-` and study the algorithm (~2 hours)
4. Build a correlation matrix for a sample prediction market portfolio (~2 hours):
   - Identify which markets share underlying factors
   - Group markets by correlation cluster
   - Apply exposure caps per cluster
5. Build a position-sizing spreadsheet (see Practical Exercises below) (~2 hours)

**Milestone:** Can construct a diversified prediction market portfolio with correlation-aware position sizing. Can explain the geometric mean penalty from variance.

### Phase 4: Integration & Stress Testing (Week 4, ~6 hours)

**Concepts:** Full system integration, Monte Carlo simulation, dynamic adjustment

**Activities:**
1. Read QuantInsti risk-constrained Kelly article and implement in Python (~2 hours)
2. Build a Monte Carlo simulator for your portfolio strategy (~2 hours):
   - Simulate 10,000 paths of 200+ bet sequences
   - Measure: terminal wealth distribution, max drawdown distribution, ruin probability
   - Test with probability estimation errors of ±5%, ±10%
3. Develop personal trading rules document (~2 hours):
   - Maximum per-position size
   - Maximum per-factor exposure
   - Drawdown response protocol
   - Rebalancing frequency

**Milestone:** Have a complete, tested position-sizing system with documented rules. Risk of ruin < 1% confirmed via simulation across 10+ positions.

---

## D) Practical Exercises

### Exercise 1: Kelly Calculator (Beginner, ~1 hour)

Build a calculator (spreadsheet or code) that takes:
- **Inputs:** Your estimated probability, market price, bankroll size
- **Outputs:** Full Kelly fraction, half-Kelly fraction, quarter-Kelly fraction, dollar amount for each, expected growth rate for each

Test with these scenarios:
| Your Estimate | Market Price | Edge |
|:---:|:---:|:---:|
| 60% | $0.45 | +15% |
| 40% | $0.30 | +10% |
| 75% | $0.65 | +10% |
| 55% | $0.50 | +5% |
| 45% | $0.50 | -5% (no bet) |

### Exercise 2: Position-Sizing Spreadsheet (Intermediate, ~3 hours)

Build a spreadsheet with these columns:
- Market name
- Your probability estimate
- Market price (implied probability)
- Edge (your estimate minus market)
- Kelly fraction (full, half, quarter)
- Correlation group (tag each market)
- Allocated capital (dollar amount)
- Max exposure per correlation group
- Running total exposure
- Risk of ruin estimate

**Requirements:**
- Auto-calculates Kelly for each position
- Enforces per-group exposure caps (e.g., 15% max per correlation cluster)
- Enforces total portfolio exposure cap (e.g., never more than 60% of bankroll deployed)
- Flags when adding a position would breach limits
- Recalculates dynamically as bankroll changes

### Exercise 3: Monte Carlo Risk Simulator (Intermediate-Advanced, ~4 hours)

Write a Python script that:
1. Takes a portfolio of N positions with (probability, market_price, correlation_group)
2. Simulates 10,000 portfolio paths over 200 bet resolutions
3. Introduces probability estimation error (±5%, ±10%)
4. Measures and plots:
   - Terminal wealth distribution (histogram)
   - Drawdown distribution
   - Risk of ruin at various thresholds (0%, 20%, 50% of initial bankroll)
   - Growth rate at full Kelly vs half-Kelly vs quarter-Kelly

**Use the `keeks` library or build from scratch with NumPy.**

### Exercise 4: Historical Backtest (Advanced, ~5 hours)

Using resolved prediction market data (Polymarket, Metaculus, or PredictIt historical data):
1. Apply your calibration model from the Forecasting domain to generate probability estimates
2. Calculate Kelly-optimal position sizes for each market
3. Simulate portfolio growth using fractional Kelly (half and quarter)
4. Measure actual risk of ruin, max drawdown, and growth rate
5. Compare to a naive "flat bet" strategy (equal size on every +EV market)

### Exercise 5: Drawdown Recovery Protocol (Intermediate, ~2 hours)

Design and document a personal drawdown management protocol:
1. Define drawdown thresholds (e.g., -10%, -20%, -30% from peak)
2. Define actions at each threshold (reduce position sizes, stop new positions, review all open positions)
3. Define recovery criteria (what conditions must be met to resume normal sizing)
4. Backtest the protocol against your Monte Carlo simulator: does it improve risk-adjusted returns?

### Exercise 6: Correlated Portfolio Stress Test (Advanced, ~3 hours)

Create a portfolio of 15+ prediction market positions across at least 4 event categories. Then:
1. Identify all correlation links (which markets depend on common factors)
2. Model the worst-case scenario: all correlated positions in the same cluster lose simultaneously
3. Calculate portfolio loss under worst-case for each cluster
4. Adjust position sizes so no single cluster can cause more than 10% portfolio drawdown
5. Verify total risk of ruin stays below 1%

---

## Applicability to Prediction Market Trading Strategies

This domain is the bridge between theory and profit. Without proper risk management:
- A 60% forecaster who overbets will go broke faster than a 52% forecaster with proper sizing
- Correlated election markets can wipe out an entire quarter of gains in one night
- The psychological toll of large drawdowns causes strategy abandonment, which is the real risk of ruin

**Direct connections to overall mastery roadmap:**
- **From Forecasting & Calibration:** Your calibration accuracy directly determines Kelly sizing accuracy. Overconfidence = overbetting = ruin.
- **From Pricing Theory:** Understanding market microstructure tells you when your edge is real vs. a liquidity artifact.
- **To Portfolio Construction (upcoming):** This domain provides the mathematical toolkit for portfolio-level capital allocation.
- **To Behavioral Psychology (upcoming):** Fractional Kelly and drawdown protocols are as much about managing your own behavior as managing money.
- **To Automated Trading (upcoming):** Position sizing algorithms from this domain become core components of any trading bot.
