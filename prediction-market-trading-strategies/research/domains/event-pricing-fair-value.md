# Event Pricing & Fair Value Estimation

Converting probabilities to prices, calibration, superforecasting techniques, reference classes, and model-based pricing.

**Prerequisites:** Probability & Statistics Foundations, Prediction Market Mechanics & Platforms
**Feeds into:** Edge Identification, Risk Management, Data Infrastructure, Quant Modeling

---

## A) Key Concepts

### 1. Probability-to-Price Conversion
The fundamental translation between a forecasted probability and a contract's fair price. In binary event contracts (paying $1 or $0), the fair price equals the probability of the event occurring. A 65% probability = $0.65 fair price. This is the foundational concept connecting forecasting skill to trading profit.

### 2. Implied Probability Extraction
Deriving the market's consensus probability from observed contract prices. For binary contracts: `Implied Probability = Contract Price`. For multi-outcome markets, you must account for overround (the sum of all outcome probabilities exceeding 100%) by normalizing. On platforms like Polymarket, the displayed price is typically the midpoint of the bid-ask spread (or last trade if spread > $0.10). Understanding the difference between raw price and true implied probability (after adjusting for fees, spread, and vig) is critical.

### 3. Risk-Neutral vs. Subjective Fair Value
- **Risk-neutral fair value:** The mathematically expected payoff given true probabilities, ignoring risk preferences. If P(event) = 0.60, fair value = $0.60.
- **Subjective fair value:** Adjusts the risk-neutral value for individual risk tolerance, capital constraints, opportunity cost, and information quality. A risk-averse trader might only buy at $0.55 even if they believe the true probability is 60%.

### 4. Calibration
The degree to which your predicted probabilities match actual outcome frequencies. If you assign 70% confidence to 100 different events, roughly 70 should actually occur for you to be well-calibrated. Calibration is distinct from resolution (how decisively you avoid 50/50 estimates). Both matter. Measured via calibration plots (reliability diagrams) and decomposition of the Brier score.

### 5. Brier Score and Proper Scoring Rules
The Brier score is the mean squared error between your probability forecast and the binary outcome: `BS = (1/N) * sum((forecast_i - outcome_i)^2)`. Range: 0 (perfect) to 1 (worst). It decomposes into:
- **Uncertainty:** Baseline difficulty of the forecasting task
- **Resolution:** How well your forecasts discriminate between outcomes
- **Reliability (Calibration):** How well your probabilities match observed frequencies

A strictly proper scoring rule incentivizes reporting your true beliefs. Other proper scoring rules include the logarithmic scoring rule (used on Metaculus) and the spherical scoring rule.

### 6. Superforecasting Techniques
The cognitive toolkit identified by Philip Tetlock's Good Judgment Project:
- **Fermi decomposition:** Break complex questions into estimable sub-problems
- **Inside vs. outside view balancing:** Combine situation-specific analysis with base rates from similar past events
- **Granular probability assignment:** Distinguish between 60%, 65%, and 70% rather than rounding to "likely"
- **Incremental belief updating:** Adjust probabilities continuously as new information arrives, calibrating the size of updates
- **Active open-mindedness:** Seek disconfirming evidence, entertain opposing views
- **Dragonfly eye perspective:** Synthesize information from multiple angles and sources

### 7. Reference Class Forecasting
Predicting outcomes by identifying a relevant class of similar historical events and using their distribution of outcomes as a starting point. Developed by Kahneman and Tversky to counter optimism bias. Three steps:
1. **Identify reference class:** Find a set of comparable past events
2. **Establish distribution:** Analyze the range of outcomes in that class
3. **Position and adjust:** Place the current event within the distribution, then adjust for unique factors

Critical for prediction markets: "What has historically happened in similar elections/economic events/etc.?"

### 8. Base Rate Analysis
The frequency of an event in a relevant population, before considering case-specific evidence. Example: "What percentage of incumbent presidents win re-election?" provides a base rate before analyzing the specific candidate. Base rates anchor your initial probability estimate; case-specific factors then adjust it up or down. Neglecting base rates (base rate neglect) is one of the most common forecasting errors.

### 9. Model-Based Pricing
Building quantitative models to estimate event probabilities from data inputs. Types include:
- **Statistical models:** Regression, logistic regression for binary outcomes
- **Ensemble models:** Combining multiple model outputs (polling averages, fundamentals models)
- **Bayesian models:** Updating prior distributions with incoming evidence
- **Machine learning models:** Random forests, neural networks for complex pattern recognition
- **Market-derived models:** Using prices from related markets as inputs

The model output becomes your fair value estimate, which you compare against market price.

### 10. Fee and Spread Adjustment
Converting a raw fair value estimate into a tradeable edge requires subtracting all friction costs:
- **Trading fees:** Kalshi charges up to ~2% of max profit; Polymarket International charges 2% on net winnings
- **Bid-ask spread cost:** Buying at ask and selling at bid means you lose the spread on round-trip trades
- **Funding/withdrawal fees:** Platform-specific deposit and withdrawal charges

**Edge = |Your Fair Value - Market Price| - Fees - (Spread / 2)**

A position is only worth taking if the edge exceeds zero after all costs.

### 11. Overround and Vig Analysis
In multi-outcome markets, the sum of implied probabilities for all outcomes often exceeds 100%. The excess (overround) represents the market maker's margin or structural inefficiency. Calculating the true implied probability requires removing overround through normalization methods (equal margin, odds ratio, Shin's method). Understanding which normalization is appropriate depends on the market structure.

### 12. Expected Value (EV) Calculation for Event Contracts
`EV = (P_win * Payout_win) + (P_lose * Payout_lose) - Cost`

For a binary contract bought at $0.40 where your estimated probability is 55%:
- EV = (0.55 * $1.00) + (0.45 * $0.00) - $0.40 = $0.15 (before fees)
- After ~2% fee on profit: EV = $0.15 - (0.55 * 0.60 * 0.02) ≈ $0.143

Positive EV trades are the goal, but variance management matters for survival.

### 13. Calibration Training Methods
Practical approaches to improve calibration:
- **Trivia-based calibration exercises:** Assign confidence intervals to factual questions, measure accuracy
- **Retrodiction:** Forecast already-resolved questions without peeking at answers
- **Forecasting tournaments:** Compete on platforms like Metaculus, Good Judgment Open
- **Calibration journaling:** Track all predictions with probabilities, review monthly

### 14. Bayesian Updating in Practice
Applying Bayes' theorem to update event probabilities:
`P(H|E) = P(E|H) * P(H) / P(E)`

In prediction markets: start with a prior (from base rates or reference classes), then update as new evidence arrives (polls, news, data releases). The key skill is calibrating the strength of evidence correctly: neither over-reacting to noise nor under-reacting to genuine signals.

### Concept Relationships
- **Calibration** and **Brier Score** are measurement tools that assess your **probability-to-price conversion** quality
- **Superforecasting techniques** and **reference class forecasting** are methods to improve calibration and produce better fair value estimates
- **Base rate analysis** feeds into **reference class forecasting** which feeds into **model-based pricing**
- **Fee and spread adjustment** converts raw fair value into actionable trading signals
- **EV calculation** combines your fair value estimate with market prices and costs to determine position attractiveness
- **Bayesian updating** is the mechanism by which all estimates improve over time with new information

### Cross-Domain Prerequisites
- **Edge Identification** depends on the ability to estimate fair value and compare against market price
- **Risk Management** requires understanding the uncertainty around your fair value estimates
- **Quant Modeling** builds directly on model-based pricing techniques
- **Data Infrastructure** supports the data collection needed for model-based pricing

---

## B) Learning Resources

### Online Courses

1. **Superforecasting Fundamentals** (Good Judgment / Thinkific)
   - URL: https://good-judgment.thinkific.com/courses/Superforecasting-Fundamentals
   - Platform: Thinkific (Good Judgment Inc.)
   - Duration: ~8 hours self-paced
   - Cost: Paid (free preview of calibration quizzes available)
   - Covers: Probabilistic reasoning, cognitive biases, calibration, Fermi estimation

2. **Forecasting Analytics** (Statistics.com)
   - URL: https://www.statistics.com/courses/forecasting-analytics/
   - Platform: Statistics.com
   - Duration: 4 weeks
   - Cost: Paid
   - Covers: Regression, smoothing, autoregressive models, forecast evaluation

3. **Making Better Decisions** (Coursera / University of Pennsylvania)
   - URL: https://www.coursera.org/learn/wharton-decision-making
   - Platform: Coursera
   - Duration: ~12 hours
   - Cost: Free to audit
   - Covers: Decision analysis, probability assessment, cognitive biases, calibration

### Video Tutorials and Lectures

4. **Philip Tetlock: "Superforecasting" Talks**
   - Long Now Foundation talk: https://www.youtube.com/watch?v=xBXDTQdmNyw
   - Covers the core principles of superforecasting directly from the researcher

5. **Calibration and Scoring Rules Explained** (University of Virginia Library)
   - URL: https://library.virginia.edu/data/articles/a-brief-on-brier-scores
   - Written guide with visual explanations of Brier score decomposition

6. **Fermi Estimation Tutorial** (Brilliant.org)
   - URL: https://brilliant.org/wiki/fermi-estimate/
   - Interactive wiki with worked examples and practice problems

### Books

7. **"Superforecasting: The Art and Science of Prediction"** by Philip Tetlock & Dan Gardner
   - Relevant chapters: All (especially Ch. 4-8 on technique, Ch. 10 on calibration)
   - Difficulty: Beginner-Intermediate
   - The foundational text for prediction skill development

8. **"The Signal and the Noise"** by Nate Silver
   - Relevant chapters: Ch. 1-4 (prediction fundamentals), Ch. 8 (election forecasting), Ch. 12 (climate/weather)
   - Difficulty: Beginner-Intermediate
   - Excellent for understanding model-based forecasting across domains

9. **"Thinking, Fast and Slow"** by Daniel Kahneman
   - Relevant chapters: Part III (overconfidence, base rates, reference classes)
   - Difficulty: Intermediate
   - Essential background on cognitive biases affecting probability estimation

10. **"Prediction Machines"** by Ajay Agrawal, Joshua Gans, Avi Goldfarb
    - Relevant chapters: Ch. 3-5 (economics of prediction, valuing predictions)
    - Difficulty: Beginner-Intermediate
    - Framework for understanding prediction value in economic terms

11. **"How to Measure Anything"** by Douglas Hubbard
    - Relevant chapters: Ch. 5-7 (calibrated estimation, decomposition, Bayesian reasoning)
    - Difficulty: Intermediate
    - Practical calibration training exercises included

### Interactive Exercises and Practice

12. **Calibrate Your Judgment** (ClearerThinking.org)
    - URL: https://www.clearerthinking.org/tools/calibrate-your-judgment
    - Free interactive tool with thousands of calibration questions
    - Tracks progress over time; commissioned by Open Philanthropy

13. **Metaculus Forecasting Platform**
    - URL: https://www.metaculus.com/
    - Free prediction tournament platform with scoring and calibration feedback
    - Practice retrodictions on resolved questions for calibration training

14. **Good Judgment Open**
    - URL: https://goodjudgment.com/services/good-judgment-open/
    - Free public forecasting platform from Tetlock's team
    - Real geopolitical and economic questions with performance tracking

15. **Quantified Intuitions (QURI)**
    - URL: https://www.quantifiedintuitions.org/
    - Free calibration exercises and estimation practice tools from the Quantified Uncertainty Research Institute

### Documentation and Reference

16. **Wharton Primer on Prediction Markets**
    - URL: https://wifpr.wharton.upenn.edu/blog/a-primer-on-prediction-markets/
    - Academic overview of prediction market pricing theory

17. **Kalshi: How Are Prices Determined**
    - URL: https://help.kalshi.com/en/articles/13823836-how-are-prices-determined
    - Official documentation on Kalshi's pricing mechanics

18. **Polymarket: How Are Prices Calculated**
    - URL: https://help.polymarket.com/en/articles/13364488-how-are-prices-calculated
    - Official documentation on Polymarket's pricing methodology

19. **Karl Whelan: Prediction Markets and Fees**
    - URL: https://www.karlwhelan.com/sports-betting-prediction-markets-fees/
    - Academic analysis of how fees distort implied probabilities

### GitHub Repositories

20. **Prediction Market Research Tools**
    - Quantpedia systematic edges: https://quantpedia.com/systematic-edges-in-prediction-markets/
    - Research and data on systematic trading edges in prediction markets

21. **Metaculus Prediction Resources**
    - URL: https://www.metaculus.com/help/prediction-resources/
    - Curated list of forecasting tools, guides, and research papers

### Community Resources

22. **r/Superforecasters** and **r/Kalshi** (Reddit)
    - Subreddits for forecasting methodology discussion and prediction market trading
    - URL: https://www.reddit.com/r/Kalshi/

23. **LessWrong Forecasting Tag**
    - URL: https://www.lesswrong.com/tag/forecasting-and-prediction
    - High-quality community discussions on calibration, scoring rules, and forecasting methodology

24. **Forecasting Research Institute (Substack)**
    - URL: https://forecastingresearch.substack.com/
    - Research publications on Brier scoring, calibration metrics, and forecasting improvement

### Podcasts

25. **Rationally Speaking Podcast** (Julia Galef)
    - Episodes on forecasting, calibration, and superforecasting with guests like Tetlock
    - URL: https://rationally-speaking.simplecast.com/

26. **The Scout Mindset** discussions (Julia Galef)
    - Related to forecasting mindset and truth-seeking; complements Superforecasting
    - Available on major podcast platforms

---

## C) Learning Path

### Phase 1: Foundations of Probability Pricing (Week 1-2, ~15 hours)

**Concepts:** Probability-to-price conversion, implied probability extraction, risk-neutral vs. subjective fair value

1. Read Kalshi and Polymarket pricing documentation (resources #17, #18)
2. Read Wharton primer on prediction markets (resource #16)
3. Practice converting between probabilities and prices on live markets
4. **Milestone:** Given any prediction market contract, can explain the implied probability and identify the bid-ask midpoint

### Phase 2: Calibration Fundamentals (Week 2-3, ~15 hours)

**Concepts:** Calibration, Brier score, proper scoring rules, calibration training

1. Read UVA Brier score guide (resource #5)
2. Complete 200+ questions on ClearerThinking calibration tool (resource #12)
3. Start "Superforecasting" book, chapters 1-5 (resource #7)
4. **Milestone:** Achieve <15% miscalibration on ClearerThinking tool; can calculate and interpret Brier scores

### Phase 3: Superforecasting Techniques (Week 3-5, ~20 hours)

**Concepts:** Superforecasting techniques, Fermi decomposition, reference class forecasting, base rate analysis, Bayesian updating

1. Finish "Superforecasting" book, chapters 6-12 (resource #7)
2. Read relevant chapters of "Thinking, Fast and Slow" (resource #9)
3. Practice Fermi estimation on Brilliant.org (resource #6)
4. Register on Metaculus and make 20+ forecasts (resource #13)
5. Study reference class forecasting methodology
6. **Milestone:** Can decompose a complex event into Fermi sub-problems, identify appropriate reference classes, and apply base rates

### Phase 4: Model-Based Pricing (Week 5-7, ~20 hours)

**Concepts:** Model-based pricing, EV calculation, Bayesian updating in practice

1. Read "The Signal and the Noise" relevant chapters (resource #8)
2. Read "How to Measure Anything" chapters 5-7 (resource #11)
3. Build a simple model for a live prediction market (e.g., election or economic event)
4. Compare model output to market prices, calculate EV
5. **Milestone:** Can build a basic quantitative model that produces probability estimates for an event category

### Phase 5: Edge Identification Through Fair Value (Week 7-8, ~15 hours)

**Concepts:** Fee and spread adjustment, overround analysis, EV calculation for event contracts

1. Study Karl Whelan's fee analysis (resource #19)
2. Map out complete fee structures for Kalshi and Polymarket
3. Build a spreadsheet that computes: fair value, implied probability, spread cost, fees, and net edge
4. Identify 5+ live contracts where your model disagrees with market price
5. **Milestone:** Can identify mispricing exceeding fees plus spread on live markets; has a working edge-calculation framework

### Total Estimated Time: 8 weeks, ~85 hours

---

## D) Practical Exercises

### Beginner Exercises

1. **Implied Probability Calculator**
   Pick 10 live contracts on Kalshi or Polymarket. For each, extract the implied probability from the Yes/No prices. Calculate the overround. Determine the "true" implied probability after removing overround. Document the spread and fees.

2. **Calibration Boot Camp**
   Complete the full ClearerThinking.org calibration training (200+ questions minimum). Record your calibration curve. Identify whether you tend toward overconfidence or underconfidence and at which probability ranges.

3. **Base Rate Lookup Exercise**
   For 5 active prediction markets (e.g., "Will X win the election?", "Will GDP growth exceed Y%?"), research the historical base rate. How often has the comparable event occurred? How does the base rate compare to the current market price?

### Intermediate Exercises

4. **Fermi Decomposition of a Live Market**
   Choose a prediction market question. Decompose it into 3-5 sub-questions using Fermi estimation. Estimate each sub-question independently, then combine into an overall probability. Compare your estimate to the market price. Write up your reasoning.

5. **Reference Class Analysis Project**
   Select an event category (e.g., "Will a sitting senator lose re-election?"). Build a reference class of the last 20+ similar events. Calculate the base rate, distribution of outcomes, and any trend. Use this as your prior for a current market.

6. **Brier Score Tracking Journal**
   Make 50 predictions on Metaculus or Good Judgment Open over 4 weeks. Track your Brier score, calibration, and resolution. After 4 weeks, analyze: where were you miscalibrated? What types of questions were hardest?

### Advanced Exercises

7. **Model-Based Fair Value Engine**
   Build a Python/spreadsheet model for a specific event category (e.g., election outcomes, economic indicators). Input: historical data, current indicators. Output: probability estimate. Compare to market prices daily for 2 weeks. Track model accuracy vs. market accuracy.

8. **Full Edge Analysis Pipeline**
   For 10 live prediction market contracts:
   - Estimate fair value using your best method
   - Extract market implied probability
   - Calculate bid-ask spread cost
   - Calculate all applicable fees
   - Compute net edge: `Edge = |Fair Value - Market Price| - Spread/2 - Fees`
   - Rank by edge size
   - Paper-trade the top 3 positions

9. **Cross-Platform Arbitrage Scanner**
   Compare prices for the same event across Kalshi, Polymarket, and any other platforms. Calculate whether arbitrage opportunities exist after accounting for all fees, spreads, and withdrawal costs on both sides. Document findings over one week.

10. **Bayesian Update Tracker**
    Pick a prediction market with a long time horizon (months). Document your initial prior and reasoning. Each week, identify new evidence, apply Bayesian updating, and record your updated probability. Compare to market movement. At resolution, evaluate your update quality.

### Real-World Applications

- **Daily pricing practice:** Every morning, estimate fair value for 3 active prediction markets before checking prices. Track accuracy.
- **News-driven repricing:** When a major news event occurs, immediately estimate how it should shift relevant market probabilities, then check actual market movement.
- **Portfolio fair value dashboard:** Maintain a live spreadsheet of all positions with your fair value estimates, market prices, and current edge for each.
- **Prediction journal for EventTide:** Use these techniques to inform analytics and dashboarding for the EventTide prediction market project.

---

## Applicability to Overall Mastery Goal

Event pricing and fair value estimation is the bridge between theoretical probability knowledge and practical trading profit. Without the ability to accurately estimate fair value and compare it against market prices (adjusted for costs), no trading strategy can be consistently profitable. This domain directly enables:

- **Edge Identification:** You cannot find edges without a fair value estimate to compare against
- **Risk Management:** Understanding uncertainty around your fair value determines position sizing
- **Quantitative Modeling:** Model-based pricing is the quantitative backbone of systematic trading
- **Every downstream domain:** Portfolio construction, algorithmic trading, market making, and arbitrage all require fair value estimation as input
