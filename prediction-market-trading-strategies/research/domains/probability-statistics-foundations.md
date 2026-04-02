# Probability & Statistics Foundations

> Domain 1 of 15 in the Prediction Market Trading Strategies mastery roadmap.
> Level: BEGINNER | Prerequisites: None | Unlocks: Market Microstructure, Event Pricing, Risk Management

---

## A) Key Concepts

### 1. Sample Spaces and Events
The foundation of all probability. A sample space is the set of all possible outcomes of an experiment; an event is a subset of outcomes you care about. In prediction markets, the sample space is the set of possible resolutions for a contract (e.g., "Yes" or "No" for a binary market).

### 2. Axioms of Probability (Kolmogorov Axioms)
Three rules that all probability measures must satisfy: non-negativity, normalization (total probability = 1), and additivity for mutually exclusive events. These axioms underpin every calculation you will do.

### 3. Conditional Probability
The probability of an event given that another event has occurred: P(A|B) = P(A ∩ B) / P(B). Critical for prediction markets because new information constantly changes the conditional landscape of event outcomes.

### 4. Bayes' Theorem
The formula for updating beliefs: P(H|E) = P(E|H) * P(H) / P(E). This is the single most important concept for prediction market traders. It provides a structured way to revise your probability estimate for an event when new evidence arrives (poll results, news, policy announcements).

### 5. Prior, Likelihood, and Posterior
- **Prior**: Your initial belief about an event's probability before new evidence.
- **Likelihood**: How probable the observed evidence is under each hypothesis.
- **Posterior**: Your updated belief after incorporating evidence.
These three components form the Bayesian updating cycle that prediction market traders use continuously.

### 6. Expected Value (EV)
EV = Σ (outcome_i × probability_i). The average payoff of a decision over many repetitions. A prediction market contract priced at $0.60 that you believe has a 75% chance of resolving "Yes" has an EV of 0.75 × $1.00 - 0.25 × $0.60 = $0.75 - $0.15... more precisely: EV = 0.75(1.00 - 0.60) + 0.25(0 - 0.60) = 0.75(0.40) - 0.25(0.60) = 0.30 - 0.15 = +$0.15 per contract. Positive EV trades are the foundation of profitable prediction market strategy.

### 7. Law of Large Numbers (LLN)
As you make more trades, your average realized return converges to the expected value. This justifies an EV-based strategy: individual trades can lose, but a large portfolio of +EV trades will be profitable.

### 8. Variance, Standard Deviation, and Volatility
Measures of how spread out outcomes are around the expected value. High variance means more uncertainty per trade. Understanding variance is essential for position sizing (Risk Management domain) and for evaluating whether a perceived edge is statistically significant.

### 9. Independence and Dependence
Two events are independent if knowing one tells you nothing about the other. Many prediction market errors come from treating correlated events as independent (e.g., related political outcomes). Recognizing dependence structures is critical for portfolio construction.

### 10. Joint and Marginal Probability
Joint probability P(A,B) describes the likelihood of two events co-occurring. Marginal probability is obtained by summing/integrating over the other variable. These concepts matter when trading correlated contracts (e.g., multiple election outcomes).

### 11. Binomial Distribution
Models the number of successes in n independent binary trials with constant probability p. Directly applicable to prediction markets: a binary contract resolves Yes/No, and a portfolio of similar contracts follows binomial-like dynamics.

### 12. Beta Distribution
A continuous distribution on [0,1] used to model uncertainty about a probability itself. The conjugate prior for binomial data in Bayesian analysis. When you want to express "I think this event has about 60% chance but I'm not very sure," the Beta distribution captures that uncertainty.

### 13. Normal (Gaussian) Distribution
The bell curve. Through the Central Limit Theorem, sums of many independent random variables converge to normal. Used for modeling continuous outcomes, confidence intervals, and hypothesis testing. Some prediction markets (distribution markets) explicitly model continuous outcomes.

### 14. Poisson Distribution
Models the count of events in a fixed interval when events occur independently at a constant rate. Useful for modeling rare events (e.g., number of major policy changes in a quarter).

### 15. Central Limit Theorem (CLT)
The distribution of sample means approaches a normal distribution as sample size grows, regardless of the underlying distribution. Justifies using normal-based confidence intervals and hypothesis tests.

### 16. Statistical Inference: Frequentist vs. Bayesian
Two paradigms for drawing conclusions from data. Frequentist methods use p-values and confidence intervals. Bayesian methods use priors and posteriors. For prediction markets, Bayesian reasoning is more natural because you continuously update beliefs, but frequentist tools (hypothesis testing) help evaluate whether a historical edge is real.

### 17. Hypothesis Testing and p-Values
A framework for deciding whether observed data is consistent with a null hypothesis. Useful for backtesting prediction market strategies: "Is my 55% hit rate on political markets significantly better than 50%, or could it be luck?"

### 18. Confidence Intervals
A range of values that likely contains the true parameter. When estimating the "true" probability of an event from historical base rates, confidence intervals quantify your uncertainty.

### 19. Base Rate and Base Rate Neglect
The base rate is the unconditional probability of an event in a reference class. Base rate neglect (ignoring how common something is in general) is one of the most common cognitive errors in prediction markets. Anchoring to base rates and then updating with Bayes' theorem is a winning approach.

### 20. Calibration
A forecaster is well-calibrated if events they assign 70% probability to actually occur about 70% of the time. Calibration is the gold standard for prediction accuracy and directly determines profitability in prediction markets.

### 21. Brier Score and Log Score
Proper scoring rules that measure forecast accuracy. Brier score = mean of (forecast - outcome)^2. Log score = mean of log(forecast for actual outcome). Both reward calibration and penalize overconfidence. Understanding these helps evaluate your own prediction track record.

### 22. Kelly Criterion (Introduction)
f* = (bp - q) / b, where b is odds, p is your estimated probability, q = 1-p. Determines the optimal fraction of bankroll to wager for maximum long-run growth. Connects probability estimation directly to bet sizing. (Explored fully in Risk Management domain.)

### Concept Relationships
```
Axioms → Conditional Probability → Bayes' Theorem → Prior/Likelihood/Posterior
                                                          ↓
Sample Spaces → Independence/Dependence → Joint/Marginal Probability
                                                          ↓
Distributions (Binomial, Beta, Normal, Poisson) → Expected Value → Kelly Criterion
                                                          ↓
CLT → Statistical Inference → Hypothesis Testing → Confidence Intervals
                                                          ↓
Base Rates → Calibration → Brier/Log Score
```

### Cross-Domain Prerequisites
- **Expected Value, Variance** → Risk Management & Position Sizing
- **Bayes' Theorem, Conditional Probability** → Event Pricing & Fair Value Estimation
- **Distributions (Binomial, Beta, Normal)** → Quantitative Modeling & Backtesting
- **Independence/Dependence, Joint Probability** → Portfolio Construction
- **Calibration, Scoring Rules** → Performance Tracking & Continuous Improvement
- **Base Rates, Statistical Inference** → Edge Identification & Market Inefficiencies

---

## B) Learning Resources

### Online Courses

1. **Harvard Stat 110: Probability** (edX / YouTube)
   - URL: https://www.edx.org/learn/probability/harvard-university-introduction-to-probability
   - Platform: edX (free audit) + full YouTube lecture series
   - Duration: ~15 weeks, 5-10 hrs/week
   - Notes: Gold standard intro probability course. Covers combinatorics, conditional probability, distributions, Bayes, expected value. Taught by Joe Blitzstein.

2. **MIT 18.05: Introduction to Probability and Statistics** (MIT OCW)
   - URL: https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
   - Platform: MIT OpenCourseWare (free)
   - Duration: ~12 weeks self-paced
   - Notes: Covers probability, Bayesian inference, frequentist inference, hypothesis testing. Includes lecture notes, problem sets, exams with solutions.

3. **MIT 6.041: Probabilistic Systems Analysis and Applied Probability** (MIT OCW)
   - URL: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
   - Platform: MIT OpenCourseWare (free)
   - Duration: ~14 weeks
   - Notes: More rigorous treatment. Covers conditioning, independence, random variables, limit theorems, Bayesian inference. Full video lectures.

4. **Khan Academy: Statistics & Probability**
   - URL: https://www.khanacademy.org/math/statistics-probability
   - Platform: Khan Academy (free)
   - Duration: Self-paced, ~30-40 hours total
   - Notes: Best for filling gaps. Interactive exercises with instant feedback. Covers basics through hypothesis testing.

5. **Bayesian Statistics: From Concept to Data Analysis** (University of California, Santa Cruz via Coursera)
   - URL: https://www.coursera.org/learn/bayesian-statistics
   - Platform: Coursera (free audit)
   - Duration: ~4 weeks, 3-5 hrs/week
   - Notes: Focused Bayesian course. Covers Bayes' theorem, conjugate priors, credible intervals, predictive distributions.

6. **TraderMath: Fundamentals of Probability and Statistics**
   - URL: https://www.tradermath.org/courses
   - Platform: TraderMath (paid)
   - Duration: Self-paced
   - Notes: Designed specifically for traders. Covers probability, distributions, expected value, and statistical reasoning in trading contexts.

### Video Tutorials and Lecture Series

7. **Harvard Stat 110 YouTube Playlist** (34 lectures)
   - URL: https://stat110.hsites.harvard.edu/youtube
   - ~50 hours of lectures. The companion to the edX course and Blitzstein/Hwang textbook.

8. **3Blue1Brown: Bayes' Theorem** (YouTube)
   - URL: https://www.youtube.com/watch?v=HZGCoVF3YvM
   - ~18 min. Best visual intuition for Bayes' theorem available. Watch before formal study.

9. **3Blue1Brown: But what is a probability distribution?** (YouTube)
   - URL: https://www.youtube.com/watch?v=8idr1WZ1A7Q
   - Visual explanation of continuous distributions and PDFs.

10. **StatQuest with Josh Starmer** (YouTube channel)
    - URL: https://www.youtube.com/c/joshstarmer
    - Dozens of short, clear explainers on probability, distributions, Bayesian stats, hypothesis testing, p-values. Excellent for reinforcing individual concepts.

### Books

11. **"Introduction to Probability" by Joseph K. Blitzstein and Jessica Hwang**
    - Chapters: All (companion to Stat 110)
    - Difficulty: Beginner-Intermediate
    - Free PDF available at: https://projects.iq.harvard.edu/stat110/home
    - Notes: Covers everything in this domain. Excellent problems with solutions.

12. **"Thinking in Bets" by Annie Duke**
    - Chapters: All
    - Difficulty: Beginner
    - Notes: Not a math textbook. Builds the mindset of thinking probabilistically and making decisions under uncertainty. Directly applicable to prediction market psychology.

13. **"The Signal and the Noise" by Nate Silver**
    - Chapters: 1-8 most relevant
    - Difficulty: Beginner
    - Notes: Real-world forecasting examples. Covers Bayesian thinking, calibration, and why most predictions fail. Essential context for prediction markets.

14. **"Superforecasting" by Philip Tetlock and Dan Gardner**
    - Chapters: All
    - Difficulty: Beginner-Intermediate
    - Notes: How elite forecasters think. Covers base rates, Bayesian updating, calibration, and the techniques that beat prediction markets. Must-read.

15. **"Statistical Rethinking" by Richard McElreath**
    - Chapters: 1-6 for this domain
    - Difficulty: Intermediate
    - Notes: Bayesian statistics with practical R/Stan examples. Builds deep intuition for Bayesian reasoning.

16. **"All of Statistics" by Larry Wasserman**
    - Chapters: 1-12
    - Difficulty: Intermediate-Advanced
    - Notes: Concise, comprehensive reference covering probability, inference, and statistical models. Good for those with calculus background.

17. **"Fifty Challenging Problems in Probability" by Frederick Mosteller**
    - Difficulty: Beginner-Intermediate
    - Notes: Short, fun probability puzzles with solutions. Great for building intuition.

### Interactive Exercises and Practice

18. **Brilliant.org: Probability Fundamentals & Probability and Chance**
    - URL: https://brilliant.org/courses/probability-fundamentals/
    - Platform: Brilliant (free tier + paid)
    - Notes: Interactive, puzzle-driven learning. Covers outcome spaces, counting, independence, Bayes' Rule, simulations.

19. **Metaculus** (prediction platform for calibration practice)
    - URL: https://www.metaculus.com/
    - Notes: Make forecasts on real-world questions, track your calibration curve over time. The best free tool for developing forecasting skill.

20. **Good Judgment Open** (forecasting tournament)
    - URL: https://www.gjopen.com/
    - Notes: Practice forecasting against a community. Track your Brier score. Directly builds the calibration skills needed for prediction markets.

21. **Kaggle: Probability and Statistics with Python**
    - URL: https://www.kaggle.com/code/hassanamin/probability-and-statistics-with-python
    - Notes: Hands-on notebook with coin flip simulations, Bernoulli trials, normal PDF exercises.

### Documentation and Reference Materials

22. **Stanford CS109: Python for Probability**
    - URL: https://web.stanford.edu/class/archive/cs/cs109/cs109.1192/handouts/pythonForProbability.html
    - Notes: Quick reference for implementing probability concepts in Python using SciPy.

23. **SciPy Statistical Functions Documentation**
    - URL: https://docs.scipy.org/doc/scipy/reference/stats.html
    - Notes: Reference for all probability distributions and statistical tests in Python.

24. **Cultivate Labs: Bayesian Reasoning and Prediction Markets**
    - URL: https://www.cultivatelabs.com/posts/bayesian-reasoning-and-prediction-markets
    - Notes: Applied article connecting Bayesian reasoning directly to prediction market trading.

### GitHub Repositories

25. **calebmadrigal/probability-with-python**
    - URL: https://github.com/calebmadrigal/probability-with-python
    - Notes: Python notebooks solving probability problems including Monte Carlo estimation.

26. **mvelezg99/probability-statistics-python**
    - URL: https://github.com/mvelezg99/probability-statistics-python
    - Notes: Jupyter notebooks covering distributions, confidence intervals, hypothesis testing.

27. **Nixtla/fpp3-python**
    - URL: https://github.com/Nixtla/fpp3-python
    - Notes: Python adaptation of "Forecasting: Principles and Practice" textbook.

### Community Resources

28. **r/PredictionMarkets** (Reddit)
    - URL: https://www.reddit.com/r/PredictionMarkets/
    - Notes: Active community discussing strategies, platforms, and probability concepts.

29. **r/statistics** (Reddit)
    - URL: https://www.reddit.com/r/statistics/
    - Notes: Good for asking questions about statistical methods and getting reading recommendations.

30. **Quantitative Finance Stack Exchange**
    - URL: https://quant.stackexchange.com/
    - Notes: Q&A for quantitative analysis, probability, and trading-related statistics.

---

## C) Learning Path

### Phase 1: Probability Foundations (Weeks 1-3, ~20 hours)
**Concepts:** Sample spaces, axioms, counting, conditional probability, independence
**Resources:** Khan Academy probability module OR Blitzstein Ch. 1-4 + Stat 110 lectures 1-10
**Milestone:** Can solve conditional probability word problems without formulas sheet

### Phase 2: Bayes' Theorem Deep Dive (Weeks 3-4, ~12 hours)
**Concepts:** Bayes' theorem, prior/likelihood/posterior, base rates, Bayesian updating
**Resources:** 3Blue1Brown Bayes video → Blitzstein Ch. 2 (Bayes section) → Coursera Bayesian Stats Week 1-2 → Cultivate Labs article
**Milestone:** Can take a news headline and formally update a prior probability for a prediction market contract

### Phase 3: Random Variables and Distributions (Weeks 4-6, ~18 hours)
**Concepts:** Discrete/continuous random variables, PMF/PDF/CDF, expected value, variance, binomial, beta, normal, Poisson
**Resources:** Blitzstein Ch. 3-5 + Stat 110 lectures 11-20 → StatQuest distribution videos → Brilliant exercises
**Milestone:** Given a prediction market scenario, can identify the appropriate distribution and calculate EV

### Phase 4: Statistical Inference (Weeks 6-8, ~16 hours)
**Concepts:** CLT, hypothesis testing, confidence intervals, p-values, frequentist vs. Bayesian inference
**Resources:** MIT 18.05 Bayesian and frequentist inference modules → Blitzstein Ch. 7-10 → Khan Academy hypothesis testing
**Milestone:** Can evaluate whether a historical prediction market track record shows statistically significant skill

### Phase 5: Applied Forecasting and Calibration (Weeks 8-10, ~15 hours)
**Concepts:** Calibration, Brier score, log score, base rate reasoning, Kelly criterion intro
**Resources:** Superforecasting (book) → Metaculus (practice) → Good Judgment Open → Signal and the Noise Ch. 1-4
**Milestone:** Have made 50+ forecasts on Metaculus with a visible calibration curve; can calculate Brier score by hand

### Total Estimated Time: 8-10 weeks, ~80 hours

---

## D) Practical Exercises

### Beginner Exercises

1. **Coin and Dice Problems**
   Calculate probabilities for compound events (e.g., "probability of at least 2 heads in 5 flips"). Use Python to simulate and verify.

2. **Bayes' Theorem News Update**
   Pick a current prediction market contract (e.g., on Kalshi or Polymarket). Write down your prior probability. Find a news article related to the event. Formally apply Bayes' theorem to calculate your posterior. Compare to the market price.

3. **Base Rate Research**
   For 5 different prediction market categories (elections, sports, economic indicators, policy, weather), research and document historical base rates. Example: "What percentage of incumbent US senators win re-election?"

### Intermediate Exercises

4. **EV Calculator**
   Build a Python script that takes your probability estimate and the current market price, then calculates expected value, optimal Kelly fraction, and expected log-growth.

5. **Distribution Fitting**
   Take historical data for a prediction market category (e.g., how often monthly jobs reports beat expectations). Fit a binomial/beta distribution to the data. Use the fitted distribution to price a new contract.

6. **Calibration Tracking Spreadsheet**
   Create a spreadsheet or Python notebook that logs your predictions with probabilities, tracks outcomes, and plots a calibration curve. Use it for at least 30 predictions.

7. **Hypothesis Testing on Market Edge**
   Simulate 200 prediction market trades where your "true" hit rate is 55%. Run a hypothesis test to see how often you'd conclude (at p < 0.05) that you have real skill vs. the market.

### Advanced Exercises

8. **Bayesian Updating Simulation**
   Model a political election contract. Start with a Beta(5,5) prior (50/50 uncertainty). Simulate polls arriving one at a time and update the posterior after each. Plot how the distribution sharpens over time.

9. **Correlation and Joint Probability Analysis**
   Find 3-5 related prediction market contracts (e.g., "Party X wins Senate" and "Party X wins Presidency"). Estimate their joint probability structure. Calculate whether the market prices are consistent with each other.

10. **Forecasting Tournament**
    Participate in Good Judgment Open or Metaculus for 4 weeks. Make at least 50 predictions. At the end, calculate your Brier score, compare to the community median, and analyze your calibration curve. Write a 1-page reflection on where your predictions were most/least accurate and why.

### Real-World Application Projects

11. **Prediction Market Fair Value Model**
    Pick an upcoming event with a prediction market contract. Build a simple probability model using base rates + Bayesian updates from 3 information sources. Compare your fair value estimate to the market price. Track the outcome.

12. **Monte Carlo Simulation for Prediction Portfolio**
    Create a portfolio of 10 prediction market positions. Use Monte Carlo simulation (10,000 runs) to estimate the distribution of portfolio returns. Calculate expected return, variance, probability of loss, and 5th percentile outcome.

---

## Applicability to Prediction Market Trading

This domain is the bedrock of everything that follows. Every subsequent domain in the roadmap depends on solid probability and statistics:

- **You cannot identify edge** without knowing how to calculate expected value and compare it to market price.
- **You cannot update beliefs rationally** without Bayes' theorem.
- **You cannot size positions** without understanding variance and the Kelly criterion.
- **You cannot evaluate your own performance** without calibration analysis and scoring rules.
- **You cannot build quantitative models** without understanding distributions and statistical inference.

Master this domain thoroughly before moving to Market Mechanics or any intermediate topics. Time invested here pays compound returns across every other domain.
