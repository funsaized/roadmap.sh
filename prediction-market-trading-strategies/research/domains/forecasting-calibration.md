# Forecasting & Calibration

**Domain Level:** INTERMEDIATE
**Prerequisites:** Probability & Bayesian Reasoning
**Feeds Into:** Information Sources & Research Methods, Quantitative Modeling for Prediction Markets, Behavioral Edge & Market Psychology

---

## A) Key Concepts

### 1. Superforecasting Fundamentals

**Superforecasters and the Good Judgment Project**
The Good Judgment Project (GJP), led by Philip Tetlock and Barbara Mellers, was a multi-year IARPA-funded forecasting tournament that identified individuals ("superforecasters") who consistently outperformed intelligence analysts with access to classified data. Superforecasters share specific cognitive habits rather than domain expertise: active open-mindedness, probabilistic thinking, and disciplined belief updating.

**Fox vs. Hedgehog Mindset**
Tetlock's framework distinguishes hedgehogs (one big theory, high confidence, poor calibration) from foxes (many small strategies, comfortable with ambiguity, better calibration). Prediction market traders benefit from fox-like thinking: drawing on multiple models and information sources rather than committing to a single narrative.

**Triage: Choosing Where to Forecast**
Not all questions are equally forecastable. Superforecasters focus on the "Goldilocks zone" where effort pays off. Questions that are too easy (base rates dominate) or too chaotic (true randomness) should be deprioritized. In prediction markets, this translates to identifying contracts where your research edge is highest.

### 2. Reference Class Forecasting

**The Outside View**
Coined by Kahneman and Tversky, the outside view involves anchoring your estimate to how a class of similar past events resolved rather than reasoning from the specifics of the current case. For prediction markets, this means asking "What percentage of similar geopolitical events/elections/policy changes historically resulted in X?" before adjusting for specifics.

**Base Rate Estimation**
The starting probability derived from the reference class. Effective forecasters identify the most relevant reference class, extract base rates, then adjust. Getting the base rate right is often more important than sophisticated inside-view analysis.

**Reference Class Selection Problem**
Choosing the right reference class is itself a judgment call. Selecting too broad a class washes out relevant signal; too narrow and you lack statistical power. Skilled forecasters test multiple reference classes and triangulate.

### 3. Decomposition Methods

**Fermi Estimation**
Breaking complex questions into smaller, estimable components. Named after physicist Enrico Fermi. For prediction markets: decompose "Will X happen?" into sub-questions like "What conditions must hold?" and estimate each probability separately, then combine.

**Scenario Tree Decomposition**
Map out mutually exclusive and collectively exhaustive pathways to an outcome. Assign probabilities to each branch and sum to get the total probability. Forces you to consider specific mechanisms rather than vague impressions.

**Factor Decomposition**
Identify the key causal factors that influence an outcome and estimate each factor's direction and magnitude. Combine using a structured framework (weighted average, multiplicative model, etc.).

**Question Decomposition Protocol**
A structured approach: (1) Clarify the question precisely, (2) Identify what would need to be true for yes/no, (3) Break into sub-questions, (4) Estimate each, (5) Combine, (6) Sanity check against the outside view.

### 4. Inside vs. Outside View Integration

**Anchoring and Adjustment**
Start with the outside view (base rate) as your anchor, then adjust based on inside-view evidence. Research shows most people adjust insufficiently from anchors. Effective forecasters make larger adjustments when inside-view evidence is strong and specific.

**Synthesis Protocol**
A practical workflow: (1) Establish base rate from reference class, (2) List factors that make this case different, (3) Estimate the direction and magnitude of each adjustment, (4) Apply adjustments incrementally, (5) Compare final estimate against both views.

### 5. Calibration

**What Calibration Means**
A forecaster is calibrated when events they assign X% probability to actually occur X% of the time. Perfect calibration means the reliability diagram (calibration curve) matches the diagonal. Calibration is necessary but not sufficient for good forecasting; you also need resolution (discrimination).

**Overconfidence and Underconfidence**
Overconfidence is the most common calibration failure: assigning extreme probabilities (90%+) too frequently. Underconfidence means clustering around 50% even when evidence supports stronger claims. Both reduce forecasting value and prediction market profitability.

**Calibration Curve (Reliability Diagram)**
A plot of predicted probability vs. observed frequency, grouped into bins. Points above the diagonal indicate underconfidence; below indicates overconfidence. The acceptance criterion for this domain is estimates within 10% of the ideal diagonal curve.

**Calibration Training**
Systematic practice: make many probability assessments, get feedback, analyze patterns, adjust. Tools like ClearerThinking's Calibrate Your Judgment and Metaculus retrodictions provide structured environments for this.

### 6. Scoring Rules

**Brier Score**
The mean squared error between your probability forecast and the binary outcome: BS = (1/N) * sum((forecast - outcome)^2). Ranges from 0 (perfect) to 2 (worst possible). A Brier score of 0.25 equals random guessing on binary events. The acceptance criterion is achieving top-quartile Brier scores on practice sets.

**Brier Score Decomposition**
BS = Reliability - Resolution + Uncertainty. Reliability measures calibration error (lower is better). Resolution measures your ability to separate outcomes (higher is better). Uncertainty is fixed by the base rate. This decomposition tells you whether to work on calibration or discrimination.

**Log Score (Logarithmic Scoring Rule)**
Penalizes confident wrong predictions much more heavily than the Brier score. Log score = -log(probability assigned to the outcome that occurred). Strictly proper: incentivizes honest reporting.

**Continuous Ranked Probability Score (CRPS)**
Used for continuous distributions rather than binary outcomes. Measures the integrated squared difference between the forecast CDF and the step function at the observed value.

**Proper Scoring Rules**
A scoring rule is "proper" if the forecaster maximizes their expected score by reporting their true beliefs. Both Brier and log scores are strictly proper. This matters for prediction markets because market prices under proper scoring reflect genuine beliefs.

### 7. Cognitive Debiasing

**Anchoring Bias**
Over-reliance on initial information. Mitigate by generating multiple anchors from different reference classes before settling on an estimate.

**Confirmation Bias**
Seeking evidence that supports existing beliefs. Counter by actively searching for disconfirming evidence and assigning a "devil's advocate" role.

**Availability Heuristic**
Overweighting easily recalled events (dramatic, recent, vivid). Counter by consulting base rate data rather than relying on examples that come to mind.

**Overconfidence Bias**
Assigning extreme probabilities too frequently. Counter through calibration training and tracking your hit rates at different confidence levels.

**Pre-Mortem Analysis**
Imagine the forecast failed spectacularly, then reason backward to identify why. Surfaces risks that optimistic forward-looking analysis misses.

**Red Teaming**
Assign an independent group to challenge the primary forecast. In a solo context, systematically argue against your own position before finalizing.

**Consider-the-Opposite**
Deliberately generate reasons why your forecast might be wrong. Research shows this single technique significantly reduces overconfidence.

### 8. Wisdom of Crowds

**Conditions for Crowd Wisdom**
James Surowiecki identified four conditions: diversity of opinion, independence of judgment, decentralization, and a mechanism for aggregation. When these hold, crowd aggregates consistently beat individual experts.

**Aggregation Methods**
Simple averaging, median, trimmed mean, extremized mean, and performance-weighted averaging. More sophisticated methods (e.g., Metaculus's aggregation algorithm) weight forecasters by track record and recency.

**Extremizing**
Shifting an aggregate forecast away from 50% because individual forecasters tend to be underconfident. If the average says 65%, the true probability may be closer to 75%. The optimal extremizing factor depends on the crowd's information overlap.

**Prediction Markets as Aggregation Mechanisms**
Markets aggregate information through prices. The connection between crowd wisdom and prediction markets is direct: market prices represent the crowd's probability estimate, incentivized by real stakes.

**Information Cascades and Herding**
When crowd members observe others' judgments (violating independence), cascades can form where early signals dominate regardless of quality. Prediction markets partially mitigate this because contrarian positions are rewarded when correct.

### Concept Relationships

The concepts form a natural hierarchy:
- **Foundation:** Calibration concepts + scoring rules provide the measurement framework
- **Techniques:** Reference class forecasting, decomposition, and inside/outside view are the core forecasting methods
- **Enhancement:** Cognitive debiasing improves individual technique application
- **Scaling:** Wisdom of crowds and aggregation extend individual forecasting to group contexts
- **Integration:** Superforecasting ties everything together as a practiced discipline

### Cross-Domain Prerequisites

These concepts feed directly into:
- **Information Sources & Research Methods:** Knowing what to look for and how to weight evidence
- **Quantitative Modeling:** Brier decomposition, scoring rules, and calibration curves are mathematical foundations for model evaluation
- **Behavioral Edge & Market Psychology:** Cognitive debiasing and understanding crowd dynamics create trading advantages

---

## B) Learning Resources

### Online Courses

1. **Good Judgment Superforecasting Fundamentals** (Good Judgment Inc.)
   - URL: https://goodjudgment.com/services/online-training/
   - Platform: Good Judgment
   - Duration: ~8-10 hours self-paced
   - Cost: Paid
   - Notes: Co-developed by Philip Tetlock. Covers probabilistic reasoning, calibration, cognitive biases, and the superforecasting framework. The most authoritative course on this topic.

2. **Estimation Calibration: Make Your Forecasts More Reliable** (Pluralsight)
   - URL: https://www.pluralsight.com/courses/estimation-calibration-reliable-forecasts
   - Platform: Pluralsight
   - Duration: ~2 hours
   - Cost: Paid (subscription)
   - Notes: Focused on applying Structured Expert Judgment (SEJ) method. Covers calibration scores and information scores.

3. **Thinking & Making Decisions Under Uncertainty** (edX / various)
   - URL: https://www.edx.org/learn/decision-making
   - Platform: edX
   - Duration: ~6-8 weeks
   - Cost: Free to audit
   - Notes: Decision theory foundations applicable to forecasting.

### Video Tutorials and Lectures

4. **Philip Tetlock - Superforecasting (Long Now Foundation)**
   - URL: https://www.youtube.com/watch?v=pedNak4S9IE
   - Duration: ~1.5 hours
   - Notes: Tetlock explains calibration measurement, forecasting tournament methodology, and the qualities of superforecasters. Essential viewing.

5. **Philip Tetlock on Superforecasting - EconTalk (12/19/2015)**
   - URL: https://www.youtube.com/watch?v=xh0XC7OCjwk
   - Duration: ~1 hour
   - Notes: Discussion on assessing probabilities, limits of precision, and practical application of superforecasting principles.

6. **More Accurately Predicting the Future - 80,000 Hours Podcast with Philip Tetlock**
   - URL: https://www.youtube.com/watch?v=3pn8fDU-LD8
   - Duration: ~2.5 hours
   - Notes: Deep dive into 40 years of forecasting research, applying the methods to career and personal decisions.

7. **Philip Tetlock on Forecasting and Foraging as a Fox - Conversations with Tyler**
   - URL: https://conversationswithtyler.com/episodes/philip-e-tetlock/
   - Duration: ~1 hour
   - Notes: Discussion of fox vs. hedgehog thinking, what we want from forecasters, and accuracy measurement.

### Books

8. **Superforecasting: The Art and Science of Prediction** - Philip Tetlock & Dan Gardner
   - Relevant chapters: All (especially Ch. 1-4 on methodology, Ch. 5-8 on techniques, Ch. 9-10 on teams and the future)
   - Difficulty: Beginner-Intermediate
   - Notes: THE foundational text for this domain. Covers every core concept from decomposition to calibration to debiasing. Read cover to cover.

9. **The Scout Mindset: Why Some People See Things Clearly and Others Don't** - Julia Galef
   - Relevant chapters: Parts I-III on motivated reasoning vs. accuracy-seeking
   - Difficulty: Beginner
   - Notes: Focuses on the psychological prerequisites for good calibration: seeing things as they are rather than as you wish. Complements Tetlock's work.

10. **Expert Political Judgment: How Good Is It? How Can We Know?** - Philip Tetlock
    - Relevant chapters: Ch. 2-4 on hedgehog vs. fox thinking, Ch. 5-7 on calibration measurement
    - Difficulty: Advanced
    - Notes: The academic predecessor to Superforecasting. More rigorous, more data-heavy. For those who want the full research foundation.

11. **The Wisdom of Crowds** - James Surowiecki
    - Relevant chapters: Part I on conditions for crowd wisdom, Part II on applications
    - Difficulty: Beginner
    - Notes: Foundational text on crowd aggregation. Directly relevant to understanding prediction market price formation.

12. **Thinking, Fast and Slow** - Daniel Kahneman
    - Relevant chapters: Ch. 10-12 on heuristics, Ch. 19-24 on overconfidence and the outside view
    - Difficulty: Intermediate
    - Notes: The cognitive psychology foundation for understanding why calibration is hard and which biases most distort forecasts.

13. **Noise: A Flaw in Human Judgment** - Daniel Kahneman, Olivier Sibony, Cass Sunstein
    - Relevant chapters: Parts II-IV on sources of noise in judgment
    - Difficulty: Intermediate
    - Notes: Complements bias-focused debiasing by addressing variability (noise) in judgments. Relevant to understanding why aggregation works.

### Interactive Exercises and Practice Platforms

14. **Calibrate Your Judgment** (ClearerThinking.org)
    - URL: https://www.clearerthinking.org/post/2019/10/16/practice-making-accurate-predictions-with-our-new-tool
    - Cost: Free
    - Notes: Interactive web tool with thousands of questions. Tracks calibration over time. Best free tool for building calibration skills from scratch.

15. **Metaculus**
    - URL: https://www.metaculus.com/
    - Cost: Free
    - Notes: Active forecasting platform with community predictions, calibration tracking, and resolved questions for retrodiction practice. Essential for ongoing calibration training.

16. **Good Judgment Open**
    - URL: https://goodjudgment.com/services/good-judgment-open/
    - Cost: Free
    - Notes: Public forecasting tournaments with detailed performance feedback. The platform that identified superforecasters. Great for competitive practice.

17. **PredictionBook**
    - URL: https://predictionbook.com/
    - Cost: Free
    - Notes: Lightweight personal prediction tracker. Log predictions, set review dates, track calibration over time. Good for maintaining a forecast journal.

18. **Confido Institute**
    - URL: https://confido.institute/confido-for/personal-forecasting-and-calibration.html
    - Cost: Free
    - Notes: Personal forecasting and calibration tools. Tracks calibration curves across topics. Supports group practice.

### Documentation and Reference Materials

19. **LessWrong: Scoring Rules**
    - URL: https://www.lesswrong.com/w/scoring-rules
    - Notes: Comprehensive wiki entry on proper scoring rules, Brier score, log score, and their properties.

20. **LessWrong: Inside/Outside View**
    - URL: https://www.lesswrong.com/w/inside-outside-view
    - Notes: Detailed explanation with examples and links to Kahneman/Tversky research.

21. **Wikipedia: Reference Class Forecasting**
    - URL: https://en.wikipedia.org/wiki/Reference_class_forecasting
    - Notes: Good overview of the methodology with citations to Flyvbjerg's work on project forecasting.

22. **Wikipedia: Brier Score**
    - URL: https://en.wikipedia.org/wiki/Brier_score
    - Notes: Mathematical definition, decomposition formula, and properties.

23. **Farnam Street: Ten Commandments for Superforecasters**
    - URL: https://fs.blog/ten-commandments-for-superforecasters/
    - Notes: Concise summary of Tetlock's practical guidelines.

24. **Cultivate Labs: What Is a Brier Score?**
    - URL: https://www.cultivatelabs.com/crowdsourced-forecasting-guide/what-is-a-brier-score-and-how-is-it-calculated
    - Notes: Practical guide to Brier score calculation with examples.

### Podcasts and Audio

25. **Rationally Speaking Podcast - Episode 145: Superforecasting with Philip Tetlock**
    - URL: http://rationallyspeakingpodcast.org/past-episodes/
    - Notes: Julia Galef interviews Tetlock on intellectual virtues and habits of mind for better forecasting.

26. **80,000 Hours Podcast - Philip Tetlock on Forecasting**
    - URL: https://80000hours.org/podcast/episodes/philip-tetlock-forecasting-research/
    - Notes: 2.5-hour deep dive into forecasting research and practical applications.

### GitHub Repositories and Open-Source Projects

27. **uncertainty-calibration** (Python)
    - URL: https://pypi.org/project/uncertainty-calibration/
    - Notes: Measure calibration error, compute confidence intervals via bootstrap, and recalibrate models. Useful for building your own calibration analysis tools.

28. **pycalibration**
    - URL: https://github.com/devmotion/pycalibration
    - Notes: Python interface for estimating calibration errors (ECE, SKCE) and running calibration hypothesis tests.

29. **forecast-tools**
    - URL: https://github.com/TomMonks/forecast-tools
    - Notes: Naive forecast benchmarks and metrics for evaluating prediction intervals. Good for building evaluation frameworks.

### Community Resources

30. **r/Superforecasting** (Reddit)
    - URL: https://www.reddit.com/r/Superforecasting/
    - Notes: Community discussion of forecasting techniques, calibration practice, and tournament results.

31. **LessWrong Community**
    - URL: https://www.lesswrong.com/
    - Notes: Active discussions on calibration, scoring rules, and rationality techniques. Search "calibration" for dozens of relevant posts.

32. **Effective Altruism Forum - Forecasting Tag**
    - URL: https://forum.effectivealtruism.org/topics/forecasting
    - Notes: High-quality posts on forecasting methodology, calibration training, and prediction market analysis.

33. **Metaculus Discord**
    - URL: https://discord.gg/metaculus
    - Notes: Community of active forecasters discussing techniques, question analysis, and calibration strategies.

---

## C) Learning Path

### Phase 1: Foundations (Weeks 1-2, ~15 hours)

**Milestone: Understand what calibration means and why it matters**

1. Read *Superforecasting* chapters 1-6 (8 hours)
2. Complete ClearerThinking "Calibrate Your Judgment" initial assessment (2 hours)
3. Read Farnam Street's "Ten Commandments" article (30 min)
4. Watch Philip Tetlock Long Now Foundation talk (1.5 hours)
5. Read LessWrong entries on scoring rules and inside/outside view (2 hours)
6. Set up accounts on Metaculus and PredictionBook (1 hour)

**Checkpoint:** Can you explain what a Brier score is, what calibration means, and why the outside view matters?

### Phase 2: Core Techniques (Weeks 3-4, ~15 hours)

**Milestone: Apply decomposition and reference class forecasting to real questions**

1. Read *Superforecasting* chapters 7-12 (5 hours)
2. Practice Fermi estimation: do 20 Fermi problems (3 hours)
3. Make 15+ forecasts on Metaculus using decomposition (4 hours)
4. Read *Thinking, Fast and Slow* chapters on heuristics and overconfidence (3 hours)
5. Study the Brier score decomposition formula and work through examples (2 hours)

**Checkpoint:** Can you decompose a novel forecasting question into 3+ sub-questions and combine them into a probability estimate?

### Phase 3: Calibration Training (Weeks 5-6, ~15 hours)

**Milestone: Achieve calibration within 10% of the ideal curve**

1. Complete 200+ questions on ClearerThinking calibration tool (5 hours)
2. Maintain daily forecast journal in PredictionBook: 3-5 predictions per day (5 hours across 2 weeks)
3. Analyze your calibration curve: identify over/underconfidence patterns (2 hours)
4. Read *The Scout Mindset* (3 hours)
5. Review and score resolved Metaculus predictions (2 hours)

**Checkpoint:** Is your calibration curve within 10% of the diagonal at each bin? Do you have a running forecast journal with 30+ tracked predictions?

### Phase 4: Debiasing and Crowd Wisdom (Weeks 7-8, ~12 hours)

**Milestone: Consistently apply debiasing techniques and understand aggregation**

1. Read *The Wisdom of Crowds* (4 hours)
2. Practice pre-mortem and consider-the-opposite on 10 forecasts (3 hours)
3. Compare your forecasts to Metaculus community medians: analyze divergences (2 hours)
4. Read about extremizing and performance-weighted aggregation (1 hour)
5. Attempt a practice set of 50+ binary questions and compute your Brier score (2 hours)

**Checkpoint:** Is your Brier score in the top quartile for your practice set? Can you identify which debiasing techniques most improved your accuracy?

### Phase 5: Integration and Prediction Market Application (Week 9-10, ~10 hours)

**Milestone: Apply forecasting framework to live prediction market contracts**

1. Select 10 active prediction market contracts on Kalshi or similar platform (1 hour)
2. For each: apply full forecasting protocol (outside view, decomposition, debiasing) and document in journal (5 hours)
3. Compare your estimates to market prices: identify where you have edge (2 hours)
4. Review *Noise* for understanding judgment variability in market contexts (2 hours)

**Checkpoint:** Do you have a documented forecasting process that you apply consistently? Can you articulate where and why your estimates differ from market prices?

### Total Estimated Time: 65-70 hours over 10 weeks

---

## D) Practical Exercises

### Beginner Exercises

**Exercise 1: Calibration Baseline Assessment**
Complete 100 questions on ClearerThinking's Calibrate Your Judgment tool. Record your initial calibration curve. This is your baseline to improve against.

**Exercise 2: Daily Prediction Journal**
Start a prediction journal (using PredictionBook or a spreadsheet). Each day, record 3 predictions about events that will resolve within 1-4 weeks. Assign a probability (not just yes/no). Review weekly.

**Exercise 3: Reference Class Identification**
Pick 5 current prediction market questions. For each, identify 3 possible reference classes, look up the base rates, and note how they differ. Practice selecting the most appropriate reference class.

### Intermediate Exercises

**Exercise 4: Fermi Decomposition Practice**
Take 10 questions from Metaculus that are currently open. For each, practice Fermi decomposition:
- Break into 3-5 sub-questions
- Estimate each sub-question
- Combine into a final probability
- Compare to the community median
- Document your decomposition and reasoning

**Exercise 5: Pre-Mortem Analysis**
Select 5 forecasts you feel most confident about. For each, write a "pre-mortem": imagine it's 6 months later and your forecast was wrong. What happened? What did you miss? Adjust your probability if the pre-mortem revealed genuine risks.

**Exercise 6: Brier Score Tracker**
Build a spreadsheet (or Python script) that tracks your forecasts and computes:
- Running Brier score
- Calibration component
- Resolution component
- Calibration curve by decile
Track at least 50 resolved binary forecasts.

### Advanced Exercises

**Exercise 7: Comparative Scoring Analysis**
Take a set of 30+ resolved forecasts. Score them using both Brier and log scoring rules. Compare the results. Where do the scores diverge? What does this tell you about your forecasting patterns (e.g., are you making confident wrong predictions that the log score penalizes more)?

**Exercise 8: Crowd vs. Individual Analysis**
On Metaculus, identify 20 questions where your forecast diverged significantly from the community aggregate. After resolution, analyze: when was the crowd right and you wrong? When were you right and the crowd wrong? What patterns emerge?

**Exercise 9: Full Forecasting Protocol on Live Markets**
Select 5 active prediction market contracts. For each, apply the complete protocol:
1. Define the question precisely
2. Identify reference class and base rate (outside view)
3. Decompose into sub-questions (minimum 3)
4. Apply inside-view adjustments
5. Run pre-mortem and consider-the-opposite
6. Assign final probability
7. Compare to market price
8. Document everything in your journal
9. Track resolution and score

**Exercise 10: Extremizing Experiment**
Take 20 resolved questions from Metaculus where community predictions were available. Compute:
- The simple average of community predictions
- The extremized average (shift away from 50% by a factor of 1.5)
- Your individual predictions
Compare Brier scores across all three. Does extremizing improve the aggregate? How do you compare?

### Real-World Application Projects

**Project A: Prediction Market Edge Finder**
Build a systematic process for scanning prediction market contracts, applying your forecasting framework, and identifying contracts where your estimate diverges from the market price by more than 10 percentage points. Maintain a portfolio of these "edge" positions and track P&L over time.

**Project B: Monthly Calibration Report**
At the end of each month, generate a calibration report from your forecast journal:
- Total forecasts made and resolved
- Brier score for the month
- Calibration curve
- Most overconfident and underconfident predictions
- Lessons learned and adjustment plan for next month

---

## Applicability to Prediction Market Trading

This domain is the bridge between theoretical probability knowledge (Domain 1) and practical trading execution. Calibration directly determines profitability: a miscalibrated trader who thinks 70% when the true probability is 55% will systematically overpay for contracts. The decomposition and debiasing techniques provide the analytical framework for identifying when market prices are wrong, which is the fundamental source of trading edge.

Every subsequent domain in this roadmap depends on the ability to produce well-calibrated probability estimates. Risk management requires accurate probability inputs. Quantitative modeling requires calibrated training data. Behavioral edge comes from understanding where others are miscalibrated. Strategy integration requires reliable self-assessment of forecasting accuracy across domains.
