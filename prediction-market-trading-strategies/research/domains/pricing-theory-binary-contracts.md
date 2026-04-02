# Pricing Theory for Binary & Multi-Outcome Contracts

## Domain Overview

This domain covers the mathematical and conceptual foundations for pricing binary event contracts and multi-outcome markets used in prediction markets like Kalshi, Polymarket, and PredictIt. It bridges probability theory (completed domain) and financial fundamentals (completed domain) into actionable pricing frameworks. Mastery here is prerequisite for quantitative modeling, arbitrage strategies, and market making.

---

## A) Key Concepts

### 1. Fair Value Derivation from Probability Estimates

**Fair value** of a binary contract is the price at which neither buyer nor seller has an expected edge, assuming both agree on the probability of the event.

- **Formula:** `Fair Value = P(event) × Payout`
- For a standard $1-payout binary contract: `Fair Value = P(event)`
- A contract with a 65% probability of resolving YES has a fair value of $0.65

**Key insight for prediction markets:** Your edge exists when your estimated probability differs from the market-implied probability. If you estimate 70% but the market prices at 60 cents, the expected value of buying YES is positive.

### 2. Implied Probability Extraction

The process of converting market prices or odds back into probability estimates.

- **Binary contract (price $0 to $1):** Implied probability = contract price / max payout
- **Decimal odds:** Implied probability = 1 / decimal odds
- **Fractional odds (x/y):** Implied probability = y / (x + y)
- **American odds (positive, e.g. +150):** Implied probability = 100 / (odds + 100)
- **American odds (negative, e.g. -200):** Implied probability = |odds| / (|odds| + 100)

Implied probabilities from market prices include the market maker's edge or spread. True probabilities require removing the overround.

### 3. Overround (Vig/Juice) Calculation

The overround is the margin built into prices that causes implied probabilities across all outcomes to sum to more than 100%.

- **Formula:** `Overround = (Sum of all implied probabilities) - 1`
- **Example:** A binary market with YES at $0.55 and NO at $0.48 sums to 1.03, giving a 3% overround
- **Removing overround:** Divide each implied probability by the total sum to normalize back to 100%
- **Shin method:** More sophisticated approach that accounts for the presence of informed traders when removing overround

Lower overround = more efficient market = better value for traders. Platforms like Kalshi and Polymarket have varying overrounds depending on liquidity.

### 4. No-Arbitrage Pricing Principle

The foundational constraint that prevents risk-free profit. In prediction markets:

- **Binary market constraint:** Price(YES) + Price(NO) = Payout (typically $1)
- If YES costs $0.58 and NO costs $0.47, their sum is $1.05. Selling both guarantees $0.05 profit at settlement. Arbitrageurs eliminate these gaps.
- **Multi-outcome constraint:** Sum of all outcome prices = Payout
- No-arbitrage ensures market prices can be interpreted as probabilities

### 5. Risk-Neutral Pricing

Pricing derivatives (including binary options) under the assumption that investors are indifferent to risk.

- Replaces real-world probabilities with "risk-neutral" probabilities
- The price of a binary contract = discounted expected payoff under the risk-neutral measure
- In prediction markets with short durations, discounting is negligible, so price ≈ risk-neutral probability
- **N(d2)** in Black-Scholes represents the risk-neutral probability of a call finishing in-the-money

### 6. Time Decay (Theta) in Binary Contracts

Binary contracts are wasting assets; their time value erodes as expiration approaches.

- **Theta:** The rate at which a contract loses value per unit of time, all else equal
- Time decay accelerates near expiration (non-linear)
- **Out-of-the-money contracts:** Lose value as time passes without the event becoming more likely
- **In-the-money contracts:** Gain value as less time remains for the outcome to reverse
- **Theta edge:** Profit opportunity when market prices don't adequately reflect time decay
- **Key difference from traditional options:** Prediction market contracts often don't explicitly price theta, creating exploitable mispricings

### 7. Volatility and Binary Contract Pricing

- **Implied volatility:** The market's expectation of future price movement, extracted from option/contract prices
- **Log-odds volatility:** For prediction markets, volatility is often measured as daily changes in log-odds of the implied probability
- Higher volatility increases the value of out-of-the-money contracts (more chance of large moves)
- Volatility is non-stationary in prediction markets, depending on time to expiration and information arrival

### 8. Binary Options Pricing Models

#### Black-Scholes for Binary Options
- **Cash-or-nothing call:** `C = e^(-rT) × N(d2)` where d2 uses standard Black-Scholes parameters
- **Cash-or-nothing put:** `P = e^(-rT) × N(-d2)`
- Inputs: strike price, current underlying, volatility, risk-free rate, time to expiry

#### Binomial Tree Model
- Discrete-time lattice tracing possible price paths
- Work backward from expiration to derive fair value
- More intuitive for understanding step-by-step probability evolution
- Converges to Black-Scholes in the continuous-time limit

#### Monte Carlo Simulation
- Simulate thousands of paths for the underlying event/price
- Count frequency of contract paying out
- Fair value = average discounted payoff
- Flexible for complex or path-dependent contracts

### 9. Multi-Outcome Market Pricing

Markets with more than two outcomes (e.g., "Who will win the election?" with 5+ candidates).

- **Constraint:** All outcome prices must sum to the total payout
- **Complete market:** Every possible outcome has a tradeable contract
- **Incomplete market:** Not all states are spanned, requiring assumptions for pricing

### 10. Logarithmic Market Scoring Rule (LMSR)

Robin Hanson's LMSR is the dominant automated market maker for prediction markets.

- **Cost function:** `C(q) = b × ln(Σ e^(qi/b))` where qi = outstanding shares for outcome i, b = liquidity parameter
- **Price for outcome i:** `pi = e^(qi/b) / Σ e^(qj/b)` (softmax function)
- **Properties:**
  - Prices always sum to 1 (coherent probabilities)
  - Bounded worst-case loss for market maker = b × ln(n) where n = number of outcomes
  - Continuous liquidity without order book
  - Incentive-compatible for risk-neutral traders
- **Liquidity parameter b:** Controls price sensitivity. Small b = volatile prices from small trades. Large b = stable prices requiring large trades to move.

### 11. Dutch Book Theorem

A **Dutch book** is a set of bets that guarantees a loss for one party regardless of outcomes.

- **Theorem:** If your subjective probabilities violate probability axioms (don't sum to 1, are negative, etc.), a clever counterparty can construct a Dutch book against you
- **Converse:** If probabilities are coherent (satisfy axioms), no Dutch book is possible
- **Practical implications:**
  - Arbitrageurs exploit incoherent market prices (Dutch book opportunities)
  - Market design should prevent persistent Dutch books
  - Your personal probability estimates must be coherent to avoid systematic losses
  - Cross-market Dutch books exist when the same event is priced differently on multiple platforms

### 12. Mispricing Identification

Comparing your model's fair value to market price to find trading opportunities.

- **Edge = Your estimated probability - Market implied probability**
- **Kelly criterion** determines optimal bet size given your edge (covered in Risk Management domain)
- **Sources of mispricing:**
  - Stale prices (low liquidity, slow information incorporation)
  - Overround not removed by participants
  - Behavioral biases (favorite-longshot bias, recency bias)
  - Time decay not reflected in prices
  - Cross-platform inconsistencies

### 13. Favorite-Longshot Bias

Systematic tendency for longshots (low-probability events) to be overpriced and favorites (high-probability events) to be underpriced.

- Well-documented in horse racing, sports betting, and prediction markets
- Creates persistent mispricing opportunities for disciplined traders
- Related to risk-seeking behavior for small-probability gains

### 14. Spread and Transaction Costs

- **Bid-ask spread:** Difference between best buy and sell prices; represents the cost of immediacy
- **Impact on fair value:** Effective fair value for a trader must account for entry and exit costs
- **Breakeven calculation:** Need sufficient edge to overcome round-trip transaction costs

### Concept Relationship Map

```
Probability Estimates → Fair Value Derivation → Mispricing Identification
                    ↓                                    ↑
         Implied Probability ← Market Prices ← No-Arbitrage Constraint
                    ↓                                    ↑
         Overround Calculation                    Dutch Book Theorem
                                                         ↑
Risk-Neutral Pricing → Binary Options Models → Multi-Outcome Pricing → LMSR
                    ↓
              Time Decay (Theta) ↔ Volatility
```

### Cross-Domain Prerequisites

These concepts feed directly into downstream domains:
- **Quantitative Modeling:** Fair value derivation, pricing models, LMSR math
- **Arbitrage Strategies:** No-arbitrage pricing, Dutch book theorem, mispricing identification
- **Market Making:** LMSR, spread mechanics, multi-outcome pricing, overround

---

## B) Learning Resources

### Online Courses

1. **Prediction Market Arbitrage (Hanguk Quant)**
   - URL: https://lectures.hangukquant.com/courses/prediction-market-arbitrage
   - Platform: Hanguk Quant Lectures
   - Duration: ~4 hours
   - Focus: Python-based arbitrage system for prediction markets, pricing mechanics
   - Cost: Paid

2. **Mastering Prediction Markets (DeFi Education)**
   - URL: https://defieducation.substack.com/p/new-course-mastering-prediction-markets
   - Platform: Substack / DeFi Education
   - Duration: ~6 hours
   - Focus: Frameworks for evaluating bets, resolution rules, platform architecture
   - Cost: Paid

3. **Financial Engineering and Risk Management (Columbia University on Coursera)**
   - URL: https://www.coursera.org/learn/financial-engineering-1
   - Platform: Coursera
   - Duration: ~8 weeks (3-5 hrs/week)
   - Focus: Binomial model, no-arbitrage pricing, risk-neutral pricing, options pricing
   - Cost: Free to audit

4. **Options Pricing Models (Khan Academy)**
   - URL: https://www.khanacademy.org/economics-finance-domain/core-finance/derivative-securities
   - Platform: Khan Academy
   - Duration: ~3 hours
   - Focus: Put-call parity, Black-Scholes intuition, binomial models
   - Cost: Free

5. **Marginal Revolution University: Prediction Markets**
   - URL: https://mru.org/courses/principles-economics-microeconomics/prediction-markets-election-forecasting
   - Platform: MRU
   - Duration: ~30 minutes
   - Focus: How prediction market prices convey information, Iowa Electronic Markets
   - Cost: Free

### Video Tutorials & Lectures

6. **"How Polymarket Actually Prices Beliefs: The Math Behind LMSR"**
   - URL: https://medium.com/coding-nexus/how-polymarket-actually-prices-beliefs-the-math-behind-lmsr-98b424e12da5
   - Type: Technical article with math walkthrough
   - Focus: LMSR cost function, softmax pricing, liquidity parameter

7. **Stony Brook Lecture: Prediction Market Design**
   - URL: https://www3.cs.stonybrook.edu/~skiena/691/lectures/lecture11.pdf
   - Type: University lecture slides (PDF)
   - Focus: Market scoring rules, LMSR, combinatorial markets

8. **Stanford OR Final: Automated Market Makers**
   - URL: https://web.stanford.edu/class/msande310/ORfinal.pdf
   - Type: Academic paper/project
   - Focus: LMSR implementation, comparison with order books

9. **Implementing Hanson's Market Maker (Oddhead Blog)**
   - URL: http://blog.oddhead.com/2006/10/30/implementing-hansons-market-maker/
   - Type: Technical blog post
   - Focus: Step-by-step LMSR implementation guide

10. **Binary Options and Implied Distributions (CodeArmo)**
    - URL: https://www.codearmo.com/python-tutorial/binary-options-and-implied-distributions
    - Type: Tutorial with Python code
    - Focus: Binary option pricing, implied distributions, Monte Carlo methods

### Books

11. **"The Economics of Prediction Markets" (various authors, Handbook chapters)**
    - Relevant chapters: Market design, scoring rules, information aggregation
    - Difficulty: Intermediate-Advanced
    - Note: Academic handbook chapters available through university libraries

12. **"Options, Futures, and Other Derivatives" by John C. Hull**
    - Relevant chapters: Ch. 13 (Binomial Trees), Ch. 15 (Black-Scholes-Merton), Ch. 26 (Exotic Options including binary)
    - Difficulty: Intermediate
    - The standard reference for derivatives pricing theory

13. **"Superforecasting" by Philip Tetlock & Dan Gardner**
    - Relevant chapters: Calibration, probability assessment
    - Difficulty: Beginner-Intermediate
    - Focus: How to form better probability estimates (input to pricing)

14. **"Trading and Exchanges" by Larry Harris**
    - Relevant chapters: Market microstructure, spread determination, market making
    - Difficulty: Intermediate
    - Focus: Understanding the mechanics behind bid-ask spreads and market pricing

15. **"Prediction Markets" by Leighton Vaughan Williams (ed.)**
    - Full book on prediction market theory and practice
    - Difficulty: Intermediate-Advanced
    - Covers Dutch books, scoring rules, market design

### Documentation & Reference Materials

16. **Stanford Encyclopedia of Philosophy: Dutch Book Arguments**
    - URL: https://plato.stanford.edu/entries/dutch-book/
    - Focus: Rigorous treatment of Dutch book theorem, philosophical foundations

17. **Wikipedia: Prediction Markets**
    - URL: https://en.wikipedia.org/wiki/Prediction_market
    - Focus: Overview, types, history, accuracy research

18. **Cultivate Labs: How LMSR Works**
    - URL: https://www.cultivatelabs.com/crowdsourced-forecasting-guide/how-does-logarithmic-market-scoring-rule-lmsr-work
    - Focus: Accessible explanation of LMSR with examples

19. **Smarkets: How to Calculate Implied Probability**
    - URL: https://help.smarkets.com/hc/en-gb/articles/214058369-How-to-calculate-implied-probability-in-betting
    - Focus: Practical guide to implied probability from a real exchange

20. **Hanson's Original LMSR Paper**
    - URL: https://www.researchgate.net/publication/2837599_Logarithmic_Market_Scoring_Rules_for_Modular_Combinatorial_Information_Aggregation
    - Focus: The foundational paper on LMSR mechanism

### Interactive Exercises & Practice

21. **Binary Option Pricing Notebooks (GitHub: xinyexu/Binary-Option-Pricing)**
    - URL: https://github.com/xinyexu/Binary-Option-Pricing
    - Type: Jupyter notebooks
    - Focus: Analytical, binomial, and Monte Carlo pricing for binary options

22. **Option Pricing Model Implementation (GitHub: hongwai1920)**
    - URL: https://github.com/hongwai1920/Implement-Option-Pricing-Model-using-Python
    - Type: Jupyter notebooks
    - Focus: Black-Scholes, binomial tree, Monte Carlo for various option types including binary

23. **Binomial Option Pricing (GitHub: ivganev)**
    - URL: https://github.com/ivganev/binomial-option-pricing
    - Type: Python notebook
    - Focus: Binomial model with convergence to Black-Scholes

24. **Overround Calculator**
    - URL: https://overroundcalculator.com/
    - Type: Online tool
    - Focus: Practice calculating overround from real odds

### Community Resources

25. **r/predictit and r/polymarket (Reddit)**
    - URL: https://reddit.com/r/predictit and https://reddit.com/r/polymarket
    - Focus: Active communities discussing mispricing, strategy, arbitrage

26. **Quant StackExchange**
    - URL: https://quant.stackexchange.com/
    - Focus: Technical Q&A on options pricing, risk-neutral valuation, binary options

27. **LessWrong: Prediction Markets**
    - URL: https://www.lesswrong.com/tag/prediction-markets
    - Focus: Rationalist community with deep analysis of prediction market theory

28. **Flashbots Collective: Arbitrage in Prediction Markets**
    - URL: https://collective.flashbots.net/t/arbitrage-in-prediction-markets-strategies-impact-and-open-questions/5198
    - Focus: Technical discussion of arbitrage strategies and Dutch book exploitation

29. **Moontower Meta: Prediction Market Arbitrage Using Option Chains**
    - URL: https://moontowermeta.com/prediction-market-arbitrage-using-option-chains-to-find-mispriced-bets/
    - Focus: Cross-market pricing analysis between options and prediction markets

30. **Alpha in Academia: Modeling Prediction Markets as Exotic Options**
    - URL: https://alphainacademia.substack.com/p/modeling-prediction-markets-as-exotic
    - Focus: Treating prediction market contracts as exotic binary options for pricing

---

## C) Learning Path Within This Domain

### Phase 1: Foundations (Week 1, ~8 hours)
**Concepts:** Fair value derivation, implied probability extraction, overround calculation

- Start with Khan Academy options pricing basics
- Read Smarkets implied probability guide
- Practice converting between odds formats and probabilities
- Use overround calculator with real market data from Kalshi/Polymarket
- **Milestone:** Can look at any prediction market and instantly calculate implied probabilities and overround

### Phase 2: No-Arbitrage Framework (Week 2, ~8 hours)
**Concepts:** No-arbitrage pricing, Dutch book theorem, risk-neutral pricing

- Read Stanford Encyclopedia entry on Dutch book arguments
- Work through Columbia Coursera no-arbitrage module
- Study how YES + NO must sum to payout
- **Milestone:** Can identify Dutch book opportunities in multi-outcome markets and explain why coherent probabilities matter

### Phase 3: Pricing Models (Weeks 3-4, ~12 hours)
**Concepts:** Black-Scholes for binary options, binomial tree model, Monte Carlo simulation, volatility

- Work through CodeArmo binary options tutorial with Python
- Complete GitHub notebooks (xinyexu/Binary-Option-Pricing)
- Implement binomial tree for a binary contract from scratch
- Run Monte Carlo simulations for contract pricing
- **Milestone:** Can price a binary contract using three different methods and explain when each is appropriate

### Phase 4: Multi-Outcome & LMSR (Week 5, ~8 hours)
**Concepts:** Multi-outcome pricing, LMSR, liquidity parameter

- Read Hanson's LMSR paper
- Study Cultivate Labs LMSR guide
- Read "How Polymarket Prices Beliefs" article
- Implement a simple LMSR market maker in Python
- **Milestone:** Can explain and implement LMSR pricing, understand how the liquidity parameter affects price sensitivity

### Phase 5: Applied Mispricing (Week 6, ~8 hours)
**Concepts:** Time decay, favorite-longshot bias, mispricing identification, spread/transaction costs

- Read Alpha in Academia piece on modeling prediction markets as exotic options
- Study Moontower Meta cross-market pricing analysis
- Build a spreadsheet or script that compares your probability estimates to market prices, accounting for overround and transaction costs
- **Milestone:** Can systematically scan markets for mispricings, quantify your edge, and determine if it exceeds transaction costs

### Total Estimated Time: 6 weeks, ~44 hours

---

## D) Practical Exercises

### Beginner Exercises

1. **Implied Probability Worksheet**
   - Take 10 current Kalshi or Polymarket contracts
   - Calculate implied probabilities for all outcomes
   - Compute the overround for each market
   - Rank markets by efficiency (lowest overround)

2. **Dutch Book Detection**
   - Find a multi-outcome market (e.g., "Who will be the next president?" or "What will GDP growth be?")
   - Check if outcome prices sum to exactly $1.00
   - If they don't, calculate the guaranteed profit from buying/selling all outcomes
   - Factor in transaction fees to determine if the arbitrage is actually profitable

3. **Odds Format Conversion Drill**
   - Convert 20 sets of odds between decimal, fractional, American, and probability formats
   - Build a Python function that converts between all formats

### Intermediate Exercises

4. **Binary Contract Pricer**
   - Build a Python script that prices binary contracts using:
     - Direct probability input
     - Black-Scholes adapted for cash-or-nothing options
     - Binomial tree (at least 50 steps)
     - Monte Carlo simulation (10,000+ paths)
   - Compare outputs across methods and explain discrepancies

5. **Overround Removal Comparison**
   - Take a multi-outcome market with significant overround
   - Remove overround using: (a) proportional method, (b) Shin method, (c) logarithmic method
   - Compare the "true" probabilities from each method
   - Discuss which method is most appropriate and why

6. **Time Decay Analysis**
   - Track a prediction market contract daily for 2+ weeks
   - Plot the contract price over time
   - Calculate daily theta (change in price with no new information)
   - Compare observed theta to theoretical theta from a binary options model

### Advanced Exercises

7. **LMSR Market Simulator**
   - Implement a full LMSR automated market maker in Python
   - Support 2-10 outcomes
   - Allow simulated traders to buy/sell shares
   - Track market maker's P&L
   - Experiment with different liquidity parameters (b)
   - Verify that prices always sum to 1

8. **Cross-Platform Mispricing Scanner**
   - Build a tool that pulls prices from multiple prediction market platforms (Kalshi, Polymarket, PredictIt)
   - Identify the same or equivalent events across platforms
   - Flag price discrepancies that exceed transaction costs on both platforms
   - Calculate expected profit from exploiting each discrepancy

9. **Model vs. Market Backtesting**
   - Select 50+ resolved prediction market contracts
   - For each, record the market price at various time points before resolution
   - Build a simple model (even just calibrated base rates) to estimate probabilities
   - Compare your model's Brier score to the market's implied probabilities
   - Identify systematic patterns where your model outperforms the market

10. **Full Pricing Pipeline**
    - Given a real upcoming event (election, economic release, sports outcome):
      - Estimate probability using your own research and calibration
      - Pull current market prices from 2+ platforms
      - Calculate implied probabilities and overround
      - Determine your edge (if any)
      - Size a hypothetical position using Kelly criterion
      - Track to resolution and evaluate your process

---

## Applicability to Prediction Market Trading Strategies

This domain is the analytical engine of the entire roadmap. Every trading strategy depends on the ability to:
- Convert market prices to probabilities (implied probability extraction)
- Compare market probabilities to your own estimates (mispricing identification)
- Understand market structure costs (overround, spread)
- Ensure your positions are coherent (Dutch book avoidance)
- Model how contract values change over time (time decay)

Without solid pricing theory, all downstream strategies (arbitrage, market making, algorithmic trading) operate without a foundation. This domain transforms you from a "gut feel" trader into a quantitative one.
