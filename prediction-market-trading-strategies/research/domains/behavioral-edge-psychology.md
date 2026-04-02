# Behavioral Edge & Market Psychology

**Domain Level:** Expert  
**Prerequisites:** Forecasting & Calibration, Portfolio Construction & Correlation Management  
**Feeds Into:** Strategy Integration & Performance Measurement  

---

## Overview

This domain covers cognitive biases in prediction markets, narrative-driven mispricing, crowd psychology, contrarian strategies, sentiment vs. information, and techniques for exploiting systematic biases. Mastering this material turns knowledge of market mechanics and quantitative modeling into a genuine trading edge by understanding *why* prices deviate from true probabilities.

---

## A) Key Concepts

### 1. Cognitive Biases in Prediction Markets

#### 1.1 Favorite-Longshot Bias
- **What:** Longshot outcomes are systematically overpriced (overbet) while favorites are underpriced (underbet). Returns decline as odds lengthen.
- **Why it matters:** The most well-documented and exploitable bias in prediction markets. Academic evidence spans horse racing, sports betting, and political markets.
- **Key research:** Snowberg & Wolfers (2010) "Explaining the Favorite-Long Shot Bias" found the bias is driven by probability misperception (consistent with Prospect Theory's probability weighting function) rather than risk-seeking preferences.
- **Relation:** Foundation for contrarian favorite-backing strategies.

#### 1.2 Overconfidence Bias
- **What:** Traders overestimate the precision of their knowledge and the size of their edge, leading to excessive position sizing and trading frequency.
- **Why it matters:** Creates liquidity (useful) but also generates systematic mispricing when overconfident traders move markets away from fair value.
- **Relation:** Interacts with disposition effect and sunk cost fallacy.

#### 1.3 Anchoring Bias
- **What:** Initial contract prices or early information disproportionately influence subsequent estimates. Traders adjust insufficiently from anchors.
- **Why it matters:** Market opening prices, poll numbers, or prior contract prices anchor expectations. New information gets underweighted relative to the anchor.
- **Relation:** Contributes to slow price discovery and status quo bias.

#### 1.4 Recency Bias
- **What:** Disproportionate weighting of recent events over base rates and historical patterns.
- **Why it matters:** After a political upset (e.g., Trump 2016), markets systematically overweight the probability of subsequent upsets. Recent news dominates over slower-moving fundamentals.
- **Relation:** Drives narrative-based mispricing and trend-following behavior.

#### 1.5 Confirmation Bias
- **What:** Selectively seeking, interpreting, and remembering information that confirms existing positions or beliefs.
- **Why it matters:** Traders holding a position become systematically worse at evaluating disconfirming evidence, leading to delayed exits and poor Bayesian updating.
- **Relation:** Reinforces disposition effect, sunk cost fallacy.

#### 1.6 Loss Aversion
- **What:** Losses feel roughly 2x as painful as equivalent gains feel good (Kahneman & Tversky). Traders avoid realizing losses even when rational to do so.
- **Why it matters:** Drives the disposition effect. Traders hold losing positions too long and exit winners too early.
- **Relation:** Core mechanism behind disposition effect, status quo bias.

### 2. Market-Level Behavioral Phenomena

#### 2.1 Herding Behavior
- **What:** Traders mimic the crowd's actions, abandoning independent analysis. Can be informational (believing others have better info) or reputational (fear of deviating from consensus).
- **Why it matters:** Creates momentum, overshooting, and bubbles in prediction market pricing. Drives prices away from fundamentals.
- **Relation:** Enables contrarian strategies; interacts with narrative bias.

#### 2.2 Crowd Psychology & Wisdom of Crowds
- **What:** Under proper conditions (diversity, independence, decentralization, aggregation mechanism), crowds produce accurate forecasts. When conditions break down (herding, information cascades), crowds become systematically wrong.
- **Key framework:** Surowiecki's four conditions for wise crowds. Prediction markets provide the aggregation mechanism but can fail on independence and diversity.
- **Relation:** Understanding when crowd wisdom fails is the foundation for identifying behavioral edges.

#### 2.3 Information Cascades
- **What:** Sequential decision-making where each person observes predecessors' actions and rationally ignores private information to follow the crowd. Fragile: a single piece of contradictory public information can reverse the cascade.
- **Why it matters:** Explains rapid, seemingly irrational price swings in thin prediction markets.
- **Relation:** Drives herding; creates contrarian opportunities.

### 3. Narrative and Sentiment

#### 3.1 Narrative Bias / Narrative Economics
- **What:** Compelling stories (hero CEO, hot sector, underdog candidate) influence beliefs more than statistical evidence. Humans are wired for narrative coherence, not probabilistic accuracy.
- **Key framework:** Robert Shiller's "Narrative Economics" - viral narratives drive economic events and market prices.
- **Why it matters:** Narrative-driven mispricing is one of the largest and most persistent inefficiencies in prediction markets. Political markets are especially susceptible.
- **Relation:** Interacts with confirmation bias and recency bias.

#### 3.2 Sentiment vs. Information
- **What:** Distinguishing between price movements driven by genuine new information versus shifts in trader sentiment/emotion. Informed trading improves price accuracy; sentiment trading creates noise and mispricing.
- **Why it matters:** Sentiment-driven prices revert to fundamentals. Information-driven prices do not. The ability to distinguish between the two is a core edge.
- **Relation:** Foundation for sentiment analysis and counter-narrative trading.

#### 3.3 Sentiment Analysis (NLP-Based)
- **What:** Using natural language processing to quantify market mood from news, social media, forums, and other text sources. Tools include FinBERT, GPT-based classifiers, and custom sentiment pipelines.
- **Why it matters:** Automated sentiment detection enables systematic identification of narrative-driven mispricing at scale.
- **Relation:** Bridges behavioral psychology with algorithmic/automated systems (prior domain).

### 4. Trading-Specific Behavioral Patterns

#### 4.1 Disposition Effect
- **What:** Selling winners too early ("lock in gains") and holding losers too long ("avoid realizing the loss"). One of the most robust findings in behavioral finance.
- **Why it matters:** Creates predictable patterns in how positions unwind. Losers are held past their rational exit point; winners are exited before full value is captured.
- **Relation:** Driven by loss aversion; exploitable via momentum strategies.

#### 4.2 Sunk Cost Fallacy
- **What:** Continuing to invest in a position because of past costs rather than future expected value.
- **Why it matters:** Traders double down on failing positions rather than cutting losses. Creates artificially slow price discovery on losing outcomes.
- **Relation:** Amplifies disposition effect and confirmation bias.

#### 4.3 Status Quo Bias
- **What:** Preference for the current state; resistance to updating positions even when new information warrants change.
- **Why it matters:** Contracts can remain mispriced longer than fundamentals justify because holders resist changing their positions.
- **Relation:** Interacts with anchoring and confirmation bias.

#### 4.4 Gambler's Fallacy and Hot Hand Fallacy
- **What:** Gambler's fallacy: believing that past independent events affect future probabilities (e.g., "due for a win"). Hot hand: believing streaks in random sequences are meaningful.
- **Why it matters:** Both distort probability estimates in sequential event markets.
- **Relation:** Fundamental probability misperceptions relevant to calibration.

### 5. Strategic Frameworks

#### 5.1 Contrarian Strategies
- **What:** Systematically taking positions opposite to prevailing market sentiment. Buying when the crowd is fearful, selling when euphoric.
- **Key requirements:** Independent probability estimation, emotional discipline, patience for convergence, position sizing for extended mispricing periods.
- **Why it matters:** The primary method for monetizing behavioral biases. Requires understanding which biases are driving current mispricing.
- **Relation:** Depends on all bias identification concepts above.

#### 5.2 Counter-Narrative Trading
- **What:** Identifying when a dominant market narrative lacks fundamental support and taking positions against it. Requires separating "the story" from objective data.
- **Why it matters:** Narratives can sustain mispricing for weeks or months. Counter-narrative trades have high expected value but require conviction and risk management.
- **Relation:** Combines narrative bias identification with contrarian execution.

#### 5.3 Bias Exploitation Framework
- **What:** A systematic process: (1) identify which bias is active, (2) estimate the magnitude of mispricing, (3) determine the catalyst for correction, (4) size the position, (5) manage the trade.
- **Why it matters:** Transforms ad-hoc bias observation into a repeatable trading strategy.
- **Relation:** Integrates all concepts in this domain into actionable methodology.

#### 5.4 Debiasing Techniques (Self)
- **What:** Methods to reduce the impact of cognitive biases on your own trading: pre-commitment devices, decision journals, checklists, base rate forcing, red teaming, outside view adoption.
- **Why it matters:** You cannot exploit others' biases if you are equally biased. Superforecasters (Tetlock) actively debias through structured thinking.
- **Relation:** Connects to calibration (prior domain) and metacognitive skills.

#### 5.5 Bias Journal / Live Tracking
- **What:** Maintaining a running log of observed bias instances in live markets: what bias was detected, what mispricing was estimated, what action was taken, what the outcome was.
- **Why it matters:** Builds pattern recognition over time. Creates a personal database of exploitable situations. Required for acceptance criteria.
- **Relation:** Core practice for ongoing skill development.

### 6. Superforecasting Psychology

#### 6.1 Foxes vs. Hedgehogs (Tetlock)
- **What:** "Foxes" draw on many perspectives and update frequently; "hedgehogs" see the world through one big idea. Foxes dramatically outperform hedgehogs at forecasting.
- **Relation:** Core mindset for prediction market trading.

#### 6.2 Active Open-Mindedness
- **What:** Deliberately seeking out disconfirming evidence, considering multiple scenarios, avoiding premature closure on a hypothesis.
- **Relation:** Antidote to confirmation bias.

#### 6.3 Probabilistic Thinking and Granularity
- **What:** Expressing beliefs as specific probabilities (not "likely" or "unlikely") and updating incrementally with new evidence.
- **Relation:** Connects to Bayesian reasoning (prior domain).

---

## B) Learning Resources

### Online Courses

1. **Behavioral Finance** - Duke University (Coursera)
   - URL: https://www.coursera.org/learn/duke-behavioral-finance
   - Platform: Coursera | Duration: ~12 hours
   - Covers biases, heuristics, and their impact on financial decisions. Solid foundation for understanding market psychology.

2. **Behavioral Economics and Public Policy** - IIMBx (edX)
   - URL: https://www.edx.org/course/behavioral-economics-and-public-policy
   - Platform: edX | Duration: ~6 weeks
   - Broader behavioral economics framework applicable to prediction market design and participant behavior.

3. **Financial Markets** - Robert Shiller, Yale (Coursera)
   - URL: https://www.coursera.org/learn/financial-markets-global
   - Platform: Coursera | Duration: ~33 hours
   - Shiller covers behavioral finance extensively, including narrative economics. Directly relevant to understanding market sentiment.

4. **Introduction to Polymarket / Prediction Markets** - Gate.com
   - URL: https://www.gate.com/learn/course/introduction-to-polymarket/understanding-prediction-markets-and-info-finance
   - Platform: Gate.com | Duration: Self-paced
   - Practical prediction market mechanics with behavioral considerations.

5. **Polymarket Trading Course**
   - URL: https://polymarketcourse.com/
   - Platform: Independent | Duration: Self-paced
   - Practical strategies for prediction market trading including psychology and bias management.

### Video Tutorials & Lectures

6. **Yale Courses: Behavioral Finance and the Role of Psychology (Lecture 11)**
   - URL: https://www.youtube.com/watch?v=XQNu1goMFcI
   - Academic lecture covering behavioral finance fundamentals from Yale's open courseware.

7. **J.P. Morgan: Trading Insights - Behavioral Biases and Their Impact**
   - URL: https://www.youtube.com/watch?v=p4L0ah54TS0
   - Professor Michelle Baddeley on loss aversion, anchoring, confirmation bias, herding, and how to mitigate or capitalize on them.

8. **Wharton Global Youth: Investing Workshop - Behavioral Finance**
   - URL: https://www.youtube.com/watch?v=T83m-ybE8O8
   - Overconfidence, confirmation bias, anchoring, loss aversion, availability heuristic explained with market examples.

9. **Inspired Money: Understanding Behavioral Finance Masterclass**
   - URL: https://www.youtube.com/watch?v=LmdZEyTTLVc
   - Panel with Colin Camerer and other experts. Covers fear/greed, myopic loss aversion, cognitive biases, and debiasing strategies.

10. **Patrick Boyle on Finance** (YouTube Channel)
    - URL: https://www.youtube.com/@PBoyleTV
    - Ex-hedge fund manager providing well-researched analysis that frequently covers behavioral finance angles on current market events.

### Books

11. **"Thinking, Fast and Slow"** - Daniel Kahneman
    - Relevant chapters: Prospect Theory, probability weighting, System 1/System 2, anchoring, availability heuristic, overconfidence
    - Difficulty: Intermediate | The foundational text for understanding cognitive biases in decision-making.

12. **"Superforecasting: The Art and Science of Prediction"** - Philip Tetlock & Dan Gardner
    - Relevant chapters: All - foxes vs hedgehogs, calibration, active open-mindedness, debiasing techniques
    - Difficulty: Intermediate | Directly applicable to prediction market trading psychology.

13. **"Misbehaving: The Making of Behavioral Economics"** - Richard Thaler
    - Relevant chapters: Endowment effect, loss aversion, mental accounting, "Econs vs Humans"
    - Difficulty: Beginner-Intermediate | Accessible introduction to how real people deviate from rational models.

14. **"The Wisdom of Crowds"** - James Surowiecki
    - Relevant chapters: Conditions for crowd wisdom, information cascades, group psychology
    - Difficulty: Beginner | Explains when and why crowds succeed or fail at aggregating information.

15. **"Narrative Economics"** - Robert Shiller
    - Relevant chapters: How viral narratives drive economic events and market pricing
    - Difficulty: Intermediate | Directly applicable to narrative-driven mispricing in prediction markets.

16. **"Beyond Greed and Fear"** - Hersh Shefrin
    - Relevant chapters: Heuristic-driven bias, frame dependence, inefficient markets
    - Difficulty: Advanced | Deep behavioral finance with market applications.

17. **"The Little Book of Behavioral Investing"** - James Montier
    - Relevant chapters: Overconfidence, loss aversion, confirmation bias, herding, practical debiasing
    - Difficulty: Intermediate | Concise, actionable, practice-oriented.

18. **"Trading in the Zone"** - Mark Douglas
    - Relevant chapters: Fear, greed, discipline, mental frameworks for consistent execution
    - Difficulty: Intermediate | Classic trading psychology focused on execution discipline.

### Documentation & Reference Materials

19. **Quantpedia: Systematic Edges in Prediction Markets**
    - URL: https://quantpedia.com/systematic-edges-in-prediction-markets/
    - Quantitative overview of exploitable biases including longshot bias, arbitrage, and information edges.

20. **Asterisk Magazine: Prediction Markets Have an Elections Problem**
    - URL: https://asteriskmag.com/issues/05/prediction-markets-have-an-elections-problem-jeremiah-johnson
    - Deep analysis of political prediction market biases with historical examples.

21. **Snowberg & Wolfers (2010): Explaining the Favorite-Long Shot Bias (NBER)**
    - URL: https://www.nber.org/system/files/working_papers/w15923/w15923.pdf
    - The foundational academic paper on favorite-longshot bias with empirical evidence.

22. **Yale Insights: Don't Trust the Political Prediction Markets**
    - URL: https://insights.som.yale.edu/insights/dont-trust-the-political-prediction-markets
    - Analysis of prediction market failures and biases in political forecasting.

23. **BoroMarket: Prediction Markets Psychology Guide**
    - URL: https://boromarket.ai/blog/prediction-markets-psychology-guide
    - Practical guide to psychological biases specific to prediction market trading.

### Interactive Exercises & Practice

24. **Good Judgment Open**
    - URL: https://www.gjopen.com/
    - Practice forecasting real-world events with feedback on calibration. The platform behind Tetlock's superforecasting research.

25. **Metaculus**
    - URL: https://www.metaculus.com/
    - Community forecasting platform with detailed scoring and calibration tracking. Practice identifying and overcoming biases in your own predictions.

26. **ClearthinkerOS Bias Detection Exercises**
    - URL: https://thedecisionlab.com/biases
    - The Decision Lab's comprehensive bias encyclopedia with examples and self-assessment tools.

### Podcasts & Audio

27. **Conversations with Tyler: Philip Tetlock on Superforecasting**
    - URL: https://conversationswithtyler.com/episodes/philip-e-tetlock/
    - Deep interview with Tetlock on forecasting psychology, biases, and prediction markets.

28. **Long Now Foundation: Philip Tetlock on Superforecasting**
    - URL: https://longnow.org/talks/02015-tetlock/
    - Extended talk on the science of prediction and the psychology of accurate forecasting.

### GitHub Repositories & Open Source

29. **SentiTrader** - Sentiment-based trading bot using Reddit/news NLP
    - URL: https://github.com/koralkulacoglu/SentiTrader
    - Study how sentiment analysis pipelines work for trading decisions.

30. **AITradingBot** - FinBERT-powered sentiment trading
    - URL: https://github.com/Matthew-Neba/AITradingBot
    - NLP sentiment analysis using FinBERT with Alpaca integration. Good reference for building sentiment-driven prediction market tools.

31. **Augur** - Decentralized prediction market protocol
    - URL: https://github.com/AugurProject/augur
    - Study the market mechanics and how behavioral patterns emerge in decentralized prediction markets.

32. **Awesome Prediction Market Tools**
    - URL: https://github.com/aarora4/Awesome-Prediction-Market-Tools
    - Curated list of prediction market tools, AI agents, analytics, and arbitrage resources.

### Community Resources

33. **r/PredictionMarkets** (Reddit)
    - URL: https://www.reddit.com/r/PredictionMarkets/
    - Active discussion of prediction market strategies, biases observed in live markets, and platform comparisons.

34. **r/BehavioralEconomics** (Reddit)
    - URL: https://www.reddit.com/r/BehavioralEconomics/
    - Academic and practical discussions of behavioral economics research.

35. **Polymarket Discord**
    - Active community discussing live Polymarket positions, biases, and strategies. Access via https://polymarket.com/.

36. **Metaculus Community Forums**
    - URL: https://www.metaculus.com/questions/
    - Discussion around forecasting methodology, calibration, and cognitive bias management.

---

## C) Learning Path

### Phase 1: Foundations of Behavioral Psychology (Week 1-2, ~15 hours)

**Concepts:** System 1/System 2 thinking, core cognitive biases (anchoring, availability, representativeness, overconfidence), loss aversion, Prospect Theory basics

**Activities:**
- Read Kahneman "Thinking, Fast and Slow" (Part 1-3)
- Take Duke Behavioral Finance course (first half)
- Watch Yale Behavioral Finance lecture
- Begin bias identification journal (even outside markets)

**Milestone:** Can name and define 10+ cognitive biases with market-relevant examples

### Phase 2: Market-Specific Biases (Week 3-4, ~15 hours)

**Concepts:** Favorite-longshot bias, herding, information cascades, disposition effect, sunk cost in trading, narrative bias, crowd wisdom conditions

**Activities:**
- Read Snowberg & Wolfers paper
- Read Surowiecki "The Wisdom of Crowds"
- Read Montier "The Little Book of Behavioral Investing"
- Study Quantpedia systematic edges article
- Watch J.P. Morgan behavioral biases video
- Analyze 3 historical prediction market mispricings (see examples below)

**Milestone:** Can identify which specific bias is driving a given mispricing in a live market

### Phase 3: Superforecasting & Debiasing (Week 5-6, ~12 hours)

**Concepts:** Fox vs. hedgehog mindset, active open-mindedness, probabilistic thinking, debiasing techniques, pre-commitment, red teaming, outside view

**Activities:**
- Read Tetlock "Superforecasting" (complete)
- Listen to Tetlock podcast interviews
- Sign up for Good Judgment Open and make 10+ forecasts
- Develop personal debiasing checklist
- Practice "consider the opposite" for each market position

**Milestone:** Calibration score on Good Judgment Open improves; can articulate a personal debiasing protocol

### Phase 4: Sentiment Analysis & Narrative Detection (Week 7-8, ~15 hours)

**Concepts:** Sentiment vs. information, NLP-based sentiment analysis, narrative economics, media influence, social media signals, counter-narrative identification

**Activities:**
- Read Shiller "Narrative Economics" (selected chapters)
- Study SentiTrader and AITradingBot GitHub repos
- Build a basic sentiment tracker for one prediction market topic
- Analyze 5 narrative-driven mispricings across Polymarket, Kalshi, etc.
- Watch Inspired Money masterclass

**Milestone:** Can run a basic sentiment analysis pipeline and distinguish sentiment-driven from information-driven price moves

### Phase 5: Strategy Development & Live Application (Week 9-10, ~15 hours)

**Concepts:** Contrarian strategies, counter-narrative trading, bias exploitation framework, bias journal methodology, position sizing for behavioral trades

**Activities:**
- Develop a complete bias exploitation strategy targeting favorite-longshot bias
- Paper trade the strategy on Polymarket or Kalshi for 2 weeks
- Maintain detailed bias journal with entries for each trade
- Read Douglas "Trading in the Zone" for execution psychology
- Review and refine strategy based on journal entries

**Milestone:** Complete strategy document with entry/exit criteria, position sizing rules, and initial performance data

### Phase 6: Integration & Mastery (Week 11-12, ~10 hours)

**Concepts:** Multi-bias detection in single markets, combining behavioral edge with quantitative models, continuous improvement, strategy refinement

**Activities:**
- Analyze portfolio-level behavioral edge across multiple markets simultaneously
- Integrate behavioral signals with quantitative models from prior domains
- Conduct retrospective analysis of bias journal
- Present findings: which biases were most exploitable, which strategies worked
- Prepare for Strategy Integration domain

**Milestone:** Documented behavioral edge strategy with live (paper or real) performance data, ready for integration with overall trading system

---

## D) Practical Exercises

### Beginner Exercises

1. **Bias Identification Drill**
   - Review 10 current Polymarket contracts. For each, identify at least one cognitive bias that could be influencing the current price. Write a one-paragraph analysis for each.
   - *Goal:* Build pattern recognition for bias detection.

2. **Anchoring Experiment**
   - Before looking at the current market price, estimate the probability of 5 different events independently. Then compare your estimates to market prices. Track how your estimates change after seeing the market price.
   - *Goal:* Experience anchoring firsthand and understand its magnitude.

3. **Historical Mispricing Case Studies**
   - **2016 US Election:** PredictIt and Betfair gave Clinton ~85% probability. Analyze which biases (herding, overconfidence in polling, narrative bias around "first woman president") contributed to mispricing.
   - **2020 US Election Post-Resolution:** Markets priced Trump at 10-15% weeks after Biden was declared winner. Analyze sunk cost fallacy, confirmation bias, and longshot bias.
   - **COVID-19 pandemic timing markets (2020):** Examine how recency bias and anchoring affected markets pricing pandemic duration and severity.

### Intermediate Exercises

4. **Favorite-Longshot Bias Backtest**
   - Collect historical data from Polymarket or PredictIt. Calculate returns for "favorites" (contracts >70 cents) vs. "longshots" (contracts <20 cents). Compute average returns by probability bucket.
   - *Goal:* Empirically verify the favorite-longshot bias exists in the markets you trade.

5. **Sentiment Tracker Build**
   - Build a simple Python script that scrapes Twitter/X, Reddit (r/PredictionMarkets), and news headlines for a specific prediction market topic. Classify sentiment as bullish/bearish/neutral. Track sentiment alongside price movements.
   - *Tools:* Python, VADER/FinBERT sentiment model, basic web scraping
   - *Goal:* Quantify the relationship between sentiment shifts and price movements.

6. **Contrarian Strategy Simulation**
   - Identify 5 markets where sentiment appears extreme (very high or very low volume in one direction). Take paper positions opposite to prevailing sentiment. Track outcomes over 2-4 weeks.
   - *Goal:* Test whether systematic contrarian positioning generates positive expected value.

### Advanced Exercises

7. **Bias Exploitation Strategy: Full Design**
   - Target: Favorite-longshot bias in political prediction markets
   - Components: (a) Screen for contracts with extreme odds (<10% or >90%), (b) Apply independent probability estimate using base rates and fundamentals, (c) Calculate edge (your estimate vs. market price), (d) Size position using Kelly criterion (from Risk Management domain), (e) Set pre-commitment exit rules
   - Document the complete strategy with entry/exit criteria, risk limits, and expected performance metrics.

8. **Live Bias Journal (Ongoing)**
   - Template for each entry: Date | Market | Contract | Current Price | Bias Detected | Your Estimate | Action Taken | Outcome | Lessons
   - Maintain for at least 30 entries over 4-6 weeks
   - Monthly review: which biases were most common, which were most exploitable, where did your own biases affect judgment
   - *Goal:* Build a personal database of behavioral edge opportunities.

9. **Narrative Decay Analysis**
   - Pick 3 prediction markets where a strong narrative drove prices in one direction (e.g., celebrity endorsement effect on political market, "hot hand" narrative on sports outcomes).
   - Track how long the narrative-driven mispricing persisted and what catalyst caused correction.
   - *Goal:* Develop intuition for narrative half-life and optimal entry timing for counter-narrative trades.

10. **Multi-Bias Confluence Detection**
    - Find a current prediction market contract where multiple biases may be active simultaneously (e.g., anchoring + narrative bias + herding).
    - Estimate the individual contribution of each bias to the mispricing.
    - Design a trade that exploits the combined effect.
    - *Goal:* Practice identifying and sizing trades when multiple behavioral factors create compounding mispricing.

---

## Historical Examples of Bias-Driven Mispricings

| Event | Biases Active | Mispricing | Outcome |
|---|---|---|---|
| 2016 US Presidential Election | Herding, overconfidence, narrative bias, anchoring to polls | Clinton at 85%+ across prediction markets | Trump won; massive correction |
| 2020 Post-Election Trump Contracts | Sunk cost, confirmation bias, longshot bias | Trump at 10-15% weeks after Biden declared winner | Contracts eventually resolved at 0 |
| Brexit Referendum 2016 | Status quo bias, anchoring, narrative ("Remain will win") | Remain at ~75% on election day | Leave won 52-48 |
| COVID-19 Duration Markets (2020) | Anchoring to SARS/H1N1 precedents, optimism bias | Markets initially priced pandemic as short-lived | Multi-year pandemic |
| Polymarket 2024 Election Cycle | Herding, narrative bias, potential manipulation | Pro-Trump bias diverged from polling averages | Demonstrated systematic platform-level sentiment bias |

---

## Applicability to Prediction Market Trading Strategy Mastery

This domain is the second-to-last in the mastery roadmap and represents the "soft edge" that complements the quantitative and systematic tools from prior domains. Specifically:

- **Connects to Forecasting & Calibration:** Debiasing techniques directly improve personal calibration scores
- **Connects to Quantitative Modeling:** Behavioral signals (sentiment, bias indicators) become features in quantitative models
- **Connects to Portfolio Construction:** Understanding correlation between behavioral-edge trades and systematic strategies improves portfolio-level risk management
- **Connects to Algorithmic Systems:** Sentiment analysis pipelines integrate with automated trading infrastructure
- **Feeds into Strategy Integration:** Behavioral edge becomes one of several alpha sources combined in the final strategy

The behavioral edge is often the highest-margin opportunity in prediction markets because most participants are retail traders influenced by the biases described here. Institutional and algorithmic participants who can systematically identify and exploit these biases capture significant value.
