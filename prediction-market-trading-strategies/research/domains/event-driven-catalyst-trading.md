# Event-Driven & Catalyst Trading

## Domain Overview

Event-driven catalyst trading focuses on profiting from price movements triggered by specific, identifiable events in prediction markets. Unlike baseline strategies that rely on persistent edges or market-making spreads, event-driven trading concentrates on discrete catalysts: elections, economic data releases, regulatory decisions, corporate actions, geopolitical developments, and other scheduled or breaking events. Mastery requires building structured playbooks, positioning before events with clear theses, executing during live events with predefined triggers, and attributing P&L to event-driven alpha versus baseline performance.

**Prerequisites from completed domains:** Information Sources & Research Methods (identifying catalysts early), Quantitative Modeling (building models for event pricing), Risk Management & Bankroll Strategy (sizing event positions), Pricing Theory (understanding how binary contracts reprice around events).

**Feeds into:** Strategy Integration & Performance Measurement (combining event-driven alpha with other strategy types).

---

## A) Key Concepts

### 1. Event Classification & Taxonomy

**Scheduled Events** — Events with known dates: elections, FOMC meetings, CPI releases, earnings reports, court rulings with set dates, regulatory deadlines. These allow pre-positioning and playbook preparation.

**Unscheduled Events (Breaking Catalysts)** — Unexpected developments: surprise resignations, natural disasters, policy announcements, geopolitical crises. Require reactive frameworks and fast execution.

**Hard Catalysts vs. Soft Catalysts** — Hard catalysts have definitive resolution (merger closes or doesn't). Soft catalysts shift probability gradually (polling trends, leaked documents). Trading approaches differ: hard catalysts suit binary positioning; soft catalysts suit incremental scaling.

**Recurring vs. One-Off Events** — Recurring events (monthly jobs reports, quarterly earnings) allow historical pattern analysis. One-off events (specific referendums, novel regulatory decisions) require first-principles reasoning.

*Relationship:* Event classification determines which playbook to use, how to size positions, and what historical data is relevant.

### 2. Event Playbook Construction

**Pre-Event Checklist** — Structured template covering: event identification, timing, market expectations (consensus), historical reaction patterns, current market pricing (implied probability), available contracts, liquidity assessment, and position sizing rules.

**Scenario Analysis** — Mapping possible outcomes to expected price movements. For binary contracts: what does the market price move to under outcome A vs. outcome B? For multi-outcome: how do correlated contracts shift?

**Entry/Exit Rules** — Predefined triggers for entering positions (e.g., "enter long YES at $0.45 if polling average exceeds 52%") and exiting (profit targets, stop-losses, time-based exits).

**Risk Parameters** — Maximum position size per event, maximum portfolio exposure to correlated events, drawdown limits that trigger position reduction.

*Relationship:* Playbooks operationalize the other concepts into repeatable processes. They connect scenario analysis to position sizing to exit timing.

### 3. Pre-Event Positioning

**Thesis Development** — Forming a directional view based on research that diverges from market consensus. Requires identifying where market-implied probability differs from your assessed probability.

**Probability Gap Identification** — Finding contracts where your estimated probability meaningfully exceeds the market price (or vice versa). The edge equals (your probability minus market probability) times potential payout.

**Timing of Entry** — Entering too early ties up capital; entering too late means the edge has been priced in. Optimal entry balances information advantage against opportunity cost.

**Scaling Into Positions** — Rather than full-size entry at one price, scaling in as confirming information arrives reduces risk of being wrong on initial thesis.

**Hedging with Correlated Contracts** — Using related markets to reduce directional risk. Example: long on "Fed cuts rates" while short on "S&P up 2% this month" if your thesis is dovish Fed but bearish equities.

*Relationship:* Pre-event positioning is where thesis meets execution. It depends on probability gap identification (from Pricing Theory domain) and connects to risk management for sizing.

### 4. Live Event Trading

**Real-Time Information Processing** — Consuming and interpreting data as it arrives during live events (election night returns, press conference statements, economic data releases). Speed of interpretation matters.

**Predefined Triggers** — "If X happens, execute Y." Examples: "If exit polls show candidate A above 55% in swing state, buy YES to 0.80." Removes emotional decision-making during fast-moving events.

**Overreaction and Mean Reversion** — Markets frequently overreact to initial data points during live events, then correct. Early election returns from non-representative precincts, preliminary economic data subject to revision, initial headline readings of complex announcements.

**Latency and Execution** — In fast-moving markets, execution speed matters. Understanding platform order types, API capabilities, and market microstructure affects realized prices versus intended prices.

**Partial Information Trading** — Making decisions with incomplete data. Early vote counts represent a fraction of total votes; initial jobless claims are one data point. Bayesian updating in real-time: how much should each new data point shift your prior?

*Relationship:* Live event trading is the highest-intensity phase. It requires all prior concepts (playbook, pre-event positioning, scenario analysis) plus real-time execution skills.

### 5. News-Driven Repricing

**Information Cascade Dynamics** — How news propagates through prediction markets. First movers capture the largest price displacement; subsequent traders push prices to new equilibrium.

**Signal vs. Noise Filtering** — Distinguishing genuinely market-moving news from noise. A poll with a 4-point swing matters; a pundit's opinion may not. Evaluating source credibility, sample quality, and novelty of information.

**Speed of Incorporation** — How quickly prediction markets price in new information. Research shows prediction markets incorporate information faster than polls but may lag behind insiders or API-connected traders.

**Narrative vs. Data** — Markets sometimes trade on narrative shifts rather than data changes. Recognizing when price movement is narrative-driven (and potentially reversible) versus data-driven (and likely persistent).

*Relationship:* News-driven repricing connects Information Sources domain knowledge to real-time trading execution.

### 6. Volatility Around Catalysts

**Implied Volatility Equivalent in Prediction Markets** — While prediction markets don't have traditional implied volatility, the rate of price oscillation and bid-ask spread widening near events serves an analogous function.

**Volatility Compression and Expansion** — Before known events, prices may stabilize as participants wait. During and after events, prices move rapidly. This pattern creates opportunities for those positioned ahead of the volatility expansion.

**Time Decay Dynamics** — As event resolution approaches, contracts with high certainty accelerate toward 0 or 1. Contracts with genuine uncertainty maintain mid-range prices longer. Understanding this "theta-like" behavior helps with entry timing.

**Volatility as Edge** — Periods of high volatility create wider mispricings and more opportunities. Strategies that perform well in volatile environments (quick in-and-out trades, straddle-like multi-contract positions) differ from those that suit calm markets.

*Relationship:* Volatility dynamics determine optimal position timing and sizing. They connect to Pricing Theory (how contracts behave near expiry) and Risk Management (how to size positions when volatility is elevated).

### 7. Exit Timing and Position Management

**Profit Target Exits** — Setting target prices at which to close positions. If you bought YES at $0.40 expecting it to reach $0.75, exiting at $0.72 captures most of the edge while avoiding the risk of reversal.

**Time-Based Exits** — Closing positions after a predetermined period regardless of P&L. Prevents capital from being tied up in stale positions.

**Trailing Exits** — Adjusting exit levels as positions move in your favor to lock in gains while allowing further upside.

**Stop-Loss Discipline** — Closing losing positions at predefined levels. Critical in event-driven trading where a wrong thesis can lead to rapid losses.

**Post-Event Drift** — After initial event repricing, prices sometimes continue drifting in the same direction as the market fully digests implications. Deciding whether to hold through drift or exit on initial move.

*Relationship:* Exit timing directly impacts realized P&L and connects to Risk Management and Portfolio Construction.

### 8. P&L Attribution for Event-Driven Strategies

**Event Alpha vs. Baseline Returns** — Separating P&L generated by event-driven positions from returns earned through non-event strategies (market making, arbitrage, long-term holds).

**Alpha Decay Curve** — Measuring P&L by time since event (per-minute or per-hour attribution). Shows how quickly edge is captured and whether holding longer adds or destroys value.

**Win Rate and Expectancy by Event Type** — Tracking which event types produce consistent profits. Elections may have 65% win rate while economic data may have 55%. This informs future capital allocation.

**Slippage Attribution** — How much of theoretical edge is lost to execution costs (spread, market impact, platform fees). High-speed events may have significant slippage.

**Risk-Adjusted Returns** — Comparing event-driven Sharpe ratio to baseline strategies. Event-driven may have higher raw returns but also higher variance.

*Relationship:* P&L attribution is the feedback loop. It connects all other concepts back to measurable performance and feeds into Strategy Integration domain.

### 9. Event-Specific Market Microstructure

**Liquidity Dynamics Around Events** — Liquidity typically decreases just before major events (market makers pull quotes) and surges during/after. Understanding this pattern affects execution quality.

**Order Book Behavior** — How the order book changes near event resolution. Resting orders may be pulled; aggressive orders may sweep the book.

**Platform-Specific Behavior** — Kalshi, Polymarket, and other platforms have different order types, fee structures, and settlement mechanics that affect event trading execution.

**Resolution Criteria Edge** — Contracts resolve based on specific criteria (which data source, which time, what definition). Understanding exact resolution criteria can provide an edge when headline data differs from resolution data.

*Relationship:* Market microstructure knowledge is operational infrastructure that enables all other concepts to function in practice.

### 10. Behavioral Patterns in Event Markets

**Favorite-Longshot Bias** — Prediction market participants tend to overvalue low-probability outcomes and undervalue high-probability outcomes near events.

**Recency Bias in Event Assessment** — Over-weighting recent events or trends when estimating probabilities. The most recent poll or the last similar event gets too much weight.

**Anchoring to Initial Prices** — Traders anchor to the price they first saw a contract at, making them slow to update as fundamentals change.

**Emotional Spikes** — Geopolitical or politically charged events create emotional trading that produces mispricings. The "Nothing Ever Happens" strategy exploits the tendency for geopolitical crises to resolve less dramatically than feared.

*Relationship:* Behavioral patterns create the mispricings that event-driven strategies exploit. Understanding biases helps identify which events are most likely to produce tradeable edges.

---

## B) Learning Resources

### Online Courses

1. **Quantra (QuantInsti) — Event Driven Trading Strategies Course**
   - URL: https://quantra.quantinsti.com/course/event-driven-trading-strategies
   - Platform: Quantra
   - Duration: ~8-10 hours
   - Cost: Paid (part of subscription)
   - Coverage: Backtesting event-driven strategies, seasonal patterns, Python implementation, volatility-based allocation
   - Relevance: Directly applicable; teaches systematic event-driven strategy construction

2. **Wall Street Prep — Hedge Fund Training**
   - URL: https://www.wallstreetprep.com/knowledge/event-driven-investing/
   - Platform: Wall Street Prep
   - Duration: Self-paced module within broader program
   - Cost: Paid
   - Coverage: Event-driven investing fundamentals, merger arbitrage, distressed securities
   - Relevance: Conceptual foundation for event-driven thesis development

3. **Harvard DCE — Hedge Funds: History, Strategies, and Practice**
   - URL: https://coursebrowser.dce.harvard.edu/course/hedge-funds-history-strategies-and-practice/
   - Platform: Harvard Extension
   - Duration: Semester-long course
   - Cost: Paid (university course)
   - Coverage: Event-driven strategies within broader hedge fund strategy context
   - Relevance: Academic rigor and theoretical framework

4. **CFA Institute — Event-Driven Strategies (Level 2 Curriculum)**
   - URL: https://analystprep.com/study-notes/cfa-level-2/event-driven-strategies-merger-arbitrage/
   - Platform: AnalystPrep (study notes for CFA curriculum)
   - Duration: 5-8 hours for this topic area
   - Cost: Free (study notes); CFA program is paid
   - Coverage: Merger arbitrage mechanics, risk factors, strategy evaluation
   - Relevance: Rigorous analytical framework for event-driven strategy assessment

### Video Tutorials & Lectures

5. **SMB Training — Using Catalysts for Short-Term Trading**
   - URL: https://www.youtube.com/watch?v=aVVJgXZBDas
   - Platform: YouTube
   - Duration: ~15 minutes
   - Coverage: Identifying catalyst stocks, reaction trading, news-driven setups
   - Relevance: Practical catalyst identification methodology

6. **Event-Driven Investing Playbook with Asif Suria (Inside Arbitrage)**
   - URL: https://www.youtube.com/watch?v=y02huZpcB1s
   - Platform: YouTube
   - Duration: ~60 minutes
   - Coverage: Diversified event-driven strategies, merger arbitrage, spin-offs, real-world case studies
   - Relevance: Practitioner perspective with actionable playbook approach

7. **Event-Driven Strategies Explained (Various)**
   - URL: https://www.youtube.com/watch?v=Qb5LmZIrtbg
   - Platform: YouTube
   - Duration: ~20 minutes
   - Coverage: Overview of event-driven hedge fund strategies, positioning around corporate events
   - Relevance: Conceptual framework for adapting traditional event-driven approaches to prediction markets

8. **BNP Paribas — Deep Dive into Event-Driven Strategies**
   - URL: https://wealthmanagement.bnpparibas/en/insights/video-podcast-hubs/podcasts-hub/deep-dive-into-event-driven-strategies-within-hedge-funds.html
   - Platform: BNP Paribas Wealth Management
   - Duration: ~30 minutes
   - Coverage: Professional hedge fund event-driven approach, M&A arbitrage
   - Relevance: Institutional-grade perspective on event-driven framework

### Books

9. **"The Event-Driven Edge in Investing" by Asif Suria** (2024)
   - Relevant chapters: All (focused entirely on event-driven strategies)
   - Difficulty: Intermediate
   - Coverage: Merger arbitrage, insider activity tracking, stock buybacks, spin-offs, six special situation strategies
   - Relevance: Most current and comprehensive book on event-driven investing

10. **"You Can Be a Stock Market Genius" by Joel Greenblatt** (1997)
    - Relevant chapters: Chapters on spin-offs, mergers, restructurings, rights offerings
    - Difficulty: Beginner-Intermediate
    - Coverage: Classic special situations and event-driven approach
    - Relevance: Foundational thinking on exploiting corporate events; adaptable to prediction market catalysts

11. **"Superforecasting: The Art and Science of Prediction" by Philip Tetlock & Dan Gardner** (2015)
    - Relevant chapters: Chapters on updating beliefs, calibration, and real-time forecasting
    - Difficulty: Intermediate
    - Coverage: How the best forecasters process information and update during events
    - Relevance: Directly applicable to live-event Bayesian updating in prediction markets

12. **"The Signal and the Noise" by Nate Silver** (2012)
    - Relevant chapters: Chapters on election forecasting, economic predictions, weather forecasting
    - Difficulty: Beginner-Intermediate
    - Coverage: Distinguishing signal from noise in forecasting, model-based prediction
    - Relevance: Framework for evaluating information quality during event-driven trading

### Documentation & Reference Materials

13. **Kalshi — How Prediction Markets Work**
    - URL: https://news.kalshi.com/p/how-prediction-markets-work
    - Coverage: Platform mechanics, contract types, resolution criteria
    - Relevance: Understanding the platform you'll trade on

14. **Polymarket Docs — Polymarket 101**
    - URL: https://docs.polymarket.com/polymarket-101
    - Coverage: Platform mechanics, USDC settlement, order types
    - Relevance: Understanding decentralized prediction market execution

15. **Quantpedia — Systematic Edges in Prediction Markets**
    - URL: https://quantpedia.com/systematic-edges-in-prediction-markets/
    - Coverage: Data-driven analysis of prediction market inefficiencies and systematic strategies
    - Relevance: Quantitative evidence for event-driven edges

16. **RavenPack — Event Trading Using Market Response**
    - URL: https://www.ravenpack.com/research/event-trading-using-market-response
    - Coverage: NLP-based event detection, market response patterns, alpha decay curves
    - Relevance: Professional-grade event detection and P&L attribution methodology

### Interactive Exercises & Practice

17. **Kalshi Practice Trading**
    - URL: https://kalshi.com
    - Coverage: Live prediction market trading with real money (start small)
    - Relevance: Direct practice of event-driven strategies in prediction markets

18. **Polymarket Active Trading**
    - URL: https://polymarket.com
    - Coverage: Decentralized prediction market with deep liquidity on political/economic events
    - Relevance: Primary practice platform for event-driven prediction market trading

19. **Metaculus Forecasting Platform**
    - URL: https://metaculus.com
    - Coverage: Free forecasting platform where you can practice probability estimation on events
    - Relevance: Practice Bayesian updating and calibration without financial risk

### Podcasts & Audio

20. **Event Driven Insights Podcast**
    - URL: https://podcasts.apple.com/us/podcast/event-driven-insights/id1820100884
    - Platform: Apple Podcasts
    - Coverage: Shareholder yield, spin-offs, economic event analysis
    - Relevance: Ongoing education in event-driven strategy thinking

21. **Oppenheimer — Event Driven Strategies Explained**
    - URL: https://oppenheimer.podbean.com/e/event-driven-strategies-explained/
    - Platform: Podbean
    - Coverage: Professional asset manager perspective on event-driven investing
    - Relevance: Institutional framework and current market application

22. **Breaking News to Trading Moves**
    - URL: https://rss.com/podcasts/breaking-news-to-trading-moves/
    - Platform: RSS.com
    - Coverage: Translating daily news into trade setups
    - Relevance: Practical news-to-trade workflow

### GitHub Repositories

23. **Awesome Prediction Market Tools (aarora4)**
    - URL: https://github.com/aarora4/Awesome-Prediction-Market-Tools
    - Coverage: Curated list of prediction market tools, bots, analytics, APIs
    - Relevance: Comprehensive resource directory for building event-driven trading infrastructure

24. **Polymarket Alpha Bot (chainstacklabs)**
    - URL: https://github.com/chainstacklabs/polymarket-alpha-bot
    - Coverage: LLM-powered trading opportunity detection on Polymarket
    - Relevance: Example of AI-assisted event-driven strategy implementation

25. **Kalshi Quant TeleBot (yllvar)**
    - URL: https://github.com/yllvar/Kalshi-Quant-TeleBot
    - Coverage: Quantitative trading bot for Kalshi with risk management
    - Relevance: Example of automated event-driven execution on regulated platform

26. **Prediction Market Analysis (Jon-Becker)**
    - URL: https://github.com/jon-becker/prediction-market-analysis
    - Coverage: Data collection, analysis, and storage for Polymarket/Kalshi
    - Relevance: Framework for building event-driven backtesting infrastructure

27. **Washington Post elex-live-model**
    - URL: https://github.com/washingtonpost/elex-live-model
    - Coverage: Live election night vote estimation model
    - Relevance: Real-time event modeling applicable to election-night prediction market trading

### Community Resources

28. **r/PredictionMarkets (Reddit)**
    - URL: https://reddit.com/r/PredictionMarkets
    - Coverage: Discussion of strategies, platform comparison, event analysis
    - Relevance: Active community sharing event-driven insights

29. **r/Kalshi (Reddit)**
    - URL: https://reddit.com/r/Kalshi
    - Coverage: Platform-specific strategies, event contract discussion
    - Relevance: Kalshi-specific event trading discussion

30. **Polymarket Discord**
    - URL: Available via polymarket.com
    - Coverage: Real-time trader discussion, market analysis
    - Relevance: Live event trading community and sentiment gauge

---

## C) Learning Path

### Phase 1: Foundations of Event-Driven Thinking (Week 1-2, ~15 hours)

**Concepts:** Event Classification & Taxonomy, News-Driven Repricing, Behavioral Patterns in Event Markets

**Activities:**
- Read "You Can Be a Stock Market Genius" (Greenblatt) for foundational event-driven thinking
- Watch Asif Suria's Event-Driven Investing Playbook video
- Study Wall Street Prep event-driven investing overview
- Classify 20 recent prediction market events into the taxonomy (scheduled/unscheduled, hard/soft catalyst, recurring/one-off)

**Milestone:** Can classify any prediction market event by type and explain expected market behavior patterns for each type.

### Phase 2: Playbook Construction (Week 3-4, ~20 hours)

**Concepts:** Event Playbook Construction, Pre-Event Positioning, Scenario Analysis

**Activities:**
- Build playbooks for three event types: (1) U.S. economic data release (CPI/jobs), (2) Election/political event, (3) Regulatory decision
- Each playbook includes: pre-event checklist, scenario mapping, entry/exit rules, risk parameters
- Study the Quantra Event Driven Trading Strategies course
- Read "The Event-Driven Edge in Investing" (Suria) for real-world playbook examples
- Practice on Metaculus to calibrate probability estimates for upcoming events

**Milestone:** Three complete, documented event playbooks ready for live use. Each has explicit entry triggers, position sizing rules, and exit criteria.

### Phase 3: Live Event Execution (Week 5-7, ~25 hours)

**Concepts:** Live Event Trading, Partial Information Trading, Volatility Around Catalysts, Exit Timing

**Activities:**
- Read "Superforecasting" (Tetlock) chapters on real-time updating
- Study Kalshi and Polymarket platform mechanics (docs)
- Paper trade 5+ live events using your playbooks (track all decisions and reasoning)
- Study the elex-live-model repo for election-night modeling approach
- Practice real-time Bayesian updating: for each live event, record your prior, each update, and final posterior
- Execute small real-money trades on 2-3 events with strict position limits

**Milestone:** Completed 5+ paper trades and 2+ real trades with documented decision logs. Can demonstrate pre-event positioning with clear thesis and execute during live events with predefined triggers.

### Phase 4: Microstructure & Advanced Execution (Week 8-9, ~15 hours)

**Concepts:** Event-Specific Market Microstructure, Resolution Criteria Edge, Latency and Execution

**Activities:**
- Study order book behavior around events on Kalshi/Polymarket
- Analyze liquidity patterns: measure spread widening before events and liquidity surges after
- Explore GitHub repos (Polymarket Alpha Bot, Kalshi Quant TeleBot) for automated execution approaches
- Identify 3+ cases where resolution criteria created edge vs. headline interpretation
- Practice limit order placement during volatile events

**Milestone:** Can describe platform-specific microstructure patterns and demonstrate how resolution criteria knowledge creates trading edge.

### Phase 5: P&L Attribution & Strategy Refinement (Week 10-12, ~20 hours)

**Concepts:** P&L Attribution, Alpha Decay Curve, Risk-Adjusted Returns, Win Rate by Event Type

**Activities:**
- Build a tracking spreadsheet/system: tag every trade as event-driven or baseline
- Calculate win rate, expectancy, and Sharpe ratio by event type
- Construct alpha decay curves for your trades: at what point after event resolution did you capture most of your P&L?
- Study RavenPack's event trading research for professional attribution methodology
- Listen to Event Driven Insights podcast for ongoing strategy refinement
- Compare event-driven P&L to your baseline (non-event) strategies
- Identify your best and worst event types; adjust capital allocation accordingly

**Milestone:** Full P&L attribution report showing event-driven vs. baseline performance, broken down by event type. Clear evidence of which events produce consistent alpha.

---

## D) Practical Exercises

### Beginner Exercises

**Exercise 1: Event Calendar Construction**
Build a monthly event calendar for prediction markets. Include: FOMC dates, CPI releases, jobs reports, upcoming elections, regulatory deadlines, major court decisions. For each, note the current market-implied probability and your initial assessment. Tools: Kalshi event listing, economic calendar (e.g., forexfactory.com), government websites.

**Exercise 2: Historical Event Analysis**
Pick 5 past events that moved prediction markets significantly (e.g., 2024 U.S. election, Fed rate decisions, Supreme Court rulings). For each: what was the market price before, during, and after? How quickly did the market reprice? What information drove the repricing? Use Polymarket/Kalshi historical data.

**Exercise 3: Bias Identification Drill**
Review 10 current prediction market contracts. For each, identify potential behavioral biases affecting pricing: favorite-longshot bias, recency bias, narrative-driven pricing, emotional spikes. Write a one-paragraph assessment of whether each contract is over or underpriced and why.

### Intermediate Exercises

**Exercise 4: Build Three Event Playbooks**
Create complete playbooks for:
- **Economic Data Release** (e.g., next CPI report): Consensus estimate, range of outcomes, historical market reactions to beats/misses, entry trigger, position size, exit rules
- **Election Event** (e.g., upcoming state/national election): Polling averages, key swing factors, early-return interpretation framework, live-event triggers, post-result drift assessment
- **Regulatory Decision** (e.g., FDA approval, CFTC ruling): Timeline, probable outcomes, stakeholder positions, contract identification, entry/exit framework

**Exercise 5: Paper Trade Live Events**
Using your playbooks, paper trade at least 5 live events over 4-6 weeks. For each trade, document:
- Pre-event thesis and entry price
- Live event observations and any adjustments
- Exit timing and reasoning
- Final P&L
- Post-mortem: what you got right, what you missed, what you'd change

**Exercise 6: Cross-Platform Price Comparison**
During 3 events, simultaneously monitor contract prices on Kalshi and Polymarket (or other platforms). Document price divergences, time to convergence, and whether cross-platform information provided directional signals.

### Advanced Exercises

**Exercise 7: Build a P&L Attribution System**
Create a spreadsheet or simple application that:
- Tags each trade as event-driven or baseline
- Tracks entry/exit times relative to event timing
- Calculates per-event-type metrics: win rate, average return, max drawdown, Sharpe ratio
- Generates an alpha decay curve (P&L captured at T+1min, T+5min, T+1hr, T+1day)
- Compares event-driven returns to overall portfolio returns

**Exercise 8: Live Event Execution Challenge**
Trade at least 3 events with real money (small position sizes). Requirements:
- Enter position before event with documented thesis
- Have predefined triggers for live adjustments
- Execute exit within predefined parameters
- Complete full post-mortem with P&L attribution
- Compare actual execution to playbook plan

**Exercise 9: Event Playbook Optimization**
After 10+ completed event trades, analyze your data to:
- Identify which event types produce the best risk-adjusted returns
- Determine optimal entry timing (how far before the event)
- Measure how much of your edge was captured in the first N minutes vs. held positions
- Adjust playbooks based on empirical evidence
- Write a "strategy memo" summarizing findings and updated approach

### Expert-Level Project

**Exercise 10: Automated Event Detection and Alert System**
Build a system that:
- Monitors economic calendars and news feeds for upcoming events
- Cross-references with available prediction market contracts
- Calculates implied probability from current contract prices
- Alerts when probability gaps exceed a threshold vs. your model's estimate
- Logs all alerts and subsequent price movements for strategy evaluation

Use GitHub repos (Prediction Market Analysis, Awesome Prediction Market Tools) as starting points. Python with Kalshi/Polymarket APIs.

---

## Applicability to Prediction Market Trading Strategies Mastery

Event-driven catalyst trading is the bridge between analytical skill (probability assessment, quantitative modeling) and realized profit. While other domains teach you to identify edges, this domain teaches you to capture them in the highest-alpha moments: around events. Mastery here means you can:

1. Systematically identify and categorize trading opportunities from the event calendar
2. Build and refine playbooks that convert analysis into executable trades
3. Maintain discipline during the emotional intensity of live events
4. Measure and attribute your performance to continuously improve

This domain feeds directly into Strategy Integration & Performance Measurement, where event-driven alpha is combined with baseline strategies for overall portfolio performance.
