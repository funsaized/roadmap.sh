# Edge Identification & Market Inefficiencies

## Domain Overview

This domain covers how to systematically find and exploit mispriced contracts in prediction markets. It builds on the probability foundations, market mechanics, microstructure, and fair value estimation covered in prior domains. The focus here is practical: scanning for mispricings, quantifying edge after fees, and recognizing structural patterns that create persistent opportunities.

---

## A) Key Concepts

### 1. Types of Edge

**Informational Edge**
- Possessing better or faster information than the market consensus
- Sources: domain expertise, proprietary data feeds, superior analytical models
- Decays quickly once information becomes public; speed matters
- Relationship: directly tied to fair value estimation skills from prior domain

**Analytical Edge**
- Superior models or frameworks for converting information into probability estimates
- Example: using causal trees, Monte Carlo simulations, or ensemble models that the market hasn't priced in
- More durable than pure informational edge since it relies on methodology
- Prerequisite for: portfolio construction, Kelly criterion sizing (later domains)

**Structural Edge**
- Exploiting market design flaws, fee asymmetries, or platform-specific quirks
- Examples: fee structure differences between Kalshi and Polymarket, contract design ambiguities, settlement rule nuances
- Often the most reliable and repeatable edge type
- Relationship: depends on deep knowledge of market mechanics (prior domain)

**Behavioral Edge**
- Profiting from systematic cognitive biases exhibited by other participants
- Examples: favorite-longshot bias, anchoring to current prices, herd behavior, recency bias
- Requires understanding crowd psychology and when the crowd is likely wrong
- Prerequisite for: contrarian strategy development

**Speed/Latency Edge**
- Acting on information faster than other market participants
- Ranges from manual reaction speed (reading news first) to automated bot execution in milliseconds
- Relevant for: latency arbitrage, event catalyst trading
- Relationship: ties into market microstructure (order flow, queue priority)

### 2. Inefficiency Sources

**Favorite-Longshot Bias**
- Empirically documented pattern: high-probability outcomes (favorites) are systematically underpriced, low-probability outcomes (longshots) are overpriced
- Participants overpay for lottery-like payoffs and undervalue likely outcomes
- Extensively studied by Snowberg & Wolfers (2010), documented across betting markets, prediction markets, and options
- Actionable: systematically buy favorites and sell longshots, adjusting for the magnitude of the bias
- One of the most robust and persistent inefficiencies

**Herd Mentality & Momentum Chasing**
- Participants follow each other's trades rather than forming independent views
- Creates self-reinforcing price movements disconnected from fundamentals
- Prices overshoot in both directions; the correction creates contrarian opportunities
- Related to: information cascades in microstructure theory

**Anchoring to Market Price**
- Traders treat current market price as an anchor for their own estimates
- Creates circular logic: "the market says 65%, so it's probably around 65%"
- Stale consensus persists even when new evidence should shift the price significantly
- Exploitable when you have an independent probability model

**Overconfidence & Dunning-Kruger Effects**
- Participants with surface-level knowledge trade aggressively on weak analysis
- Creates noise and temporary mispricings, especially in popular/viral markets
- The "dumb money" dynamic in retail-heavy prediction markets

**Recency Bias**
- Overweighting recent events when estimating probabilities
- Example: a politician's odds swing too far on a single bad debate performance
- Creates mean-reversion opportunities

**Loss Aversion & Disposition Effect**
- Traders hold losing positions too long and sell winners too early
- Creates predictable patterns in how prices adjust to new information
- Positions become "sticky" at certain price levels

### 3. Cross-Platform Arbitrage

**Inter-Market Arbitrage**
- Buying a YES contract on Platform A and a NO contract on Platform B (or vice versa) when combined cost < $1.00
- Example: If Kalshi prices Event YES at $0.45 and Polymarket prices Event NO at $0.50, buying both costs $0.95 with guaranteed $1.00 payout = $0.05 risk-free profit
- Must account for: fees on both platforms, settlement risk (oracle divergence), capital lockup cost

**Intra-Market Arbitrage**
- Within a single platform, when outcome prices for mutually exclusive events don't sum to $1.00
- Buy-all arbitrage: all outcomes sum to < $1.00; buy every outcome
- Sell-all arbitrage: all outcomes sum to > $1.00; sell every outcome
- Common in multi-outcome markets (e.g., "Who will win the primary?" with 10+ candidates)

**Oracle/Resolution Divergence Risk**
- Different platforms may resolve the same real-world event differently due to varying resolution criteria
- Example: one platform resolves on official government data, another on media reports
- Must read resolution rules carefully before assuming cross-platform parity
- The hidden risk in otherwise "risk-free" arbitrage

**Fee-Adjusted Edge Calculation**
- Raw edge = (1.00 - combined cost of YES + NO across platforms)
- Executable edge = raw edge - (fee on platform A + fee on platform B) - slippage estimate - opportunity cost of capital
- Kalshi: tiered per-contract fees (varies by volume)
- Polymarket: 0.1% taker fee or 2% on net profits from winning contracts
- A 3-5 cent raw spread can easily become unprofitable after fees

**Capital Efficiency Considerations**
- Cross-platform arb requires capital parked on multiple platforms simultaneously
- Annualized return depends on both the spread size and the time to settlement
- A 5% spread that resolves in 3 days is much better than 5% that resolves in 6 months
- Relates to: time value of money, opportunity cost analysis

### 4. Stale Pricing

**Definition & Mechanism**
- Contract price reflects an old transaction and hasn't updated to incorporate new information
- Most common in low-liquidity markets, niche events, or outside peak trading hours
- The gap between current price and true value is the exploitable edge

**Latency Arbitrage**
- Acting on publicly available information (e.g., a news break, a data release) before the prediction market price adjusts
- Automated bots scan news feeds and execute trades within milliseconds
- Manual traders can still exploit this in less popular markets where bot coverage is thin
- Documented case: MIT quant exploiting a 0.3-second window in prediction market pricing

**Stale Limit Orders**
- Resting limit orders from traders who aren't monitoring the market become pickoff targets
- When news breaks, existing limit orders at old prices become free money for fast actors
- Relates to: order book dynamics from microstructure domain

**Cross-Market Staleness**
- When a faster reference market (e.g., futures, forex) moves but a correlated prediction market hasn't updated
- Example: CPI data drops, bond futures move instantly, but the "Will CPI exceed X%?" contract on Kalshi lags by seconds to minutes

### 5. Event Catalysts

**Scheduled Events**
- Known dates: economic data releases (CPI, jobs report, GDP), elections, earnings, court rulings, FOMC decisions
- Pre-event: position for expected volatility or directional move based on your model
- Post-event: trade the gap between actual outcome and how the market reacts
- Calendar-driven, repeatable strategy

**Unscheduled Events**
- Breaking news: geopolitical crises, surprise resignations, natural disasters, policy announcements
- Requires real-time news monitoring infrastructure
- Edge comes from speed of reaction and quality of on-the-fly analysis
- Higher variance, higher potential reward

**Expectation vs. Reality Framework**
- Markets price in expectations, not raw news
- "Good news" can cause a price drop if expectations were higher
- Edge comes from modeling expectations accurately and trading the gap between expectation and reality
- Example: market prices 70% chance of Fed rate cut; your model says 85% based on recent data; buy YES

**Event-Driven Volatility Patterns**
- Prediction market implied volatility tends to follow patterns around scheduled events
- Prices often compress pre-event (uncertainty) and expand post-event (resolution)
- Understanding these patterns enables better entry/exit timing

### 6. Contrarian Signals

**Sentiment Extremes**
- When market consensus reaches extreme levels (>90% or <10%), the remaining probability is often underpriced
- Overly crowded trades create asymmetric opportunities for the contrarian
- Monitoring: whale tracker data, social media sentiment, market position data

**Overreaction to News**
- Markets overshoot on breaking news due to panic or euphoria
- The initial move is often followed by a partial reversion
- Strategy: wait for the initial spike, then fade the overreaction
- Requires discipline and a pre-defined framework for "how far is too far"

**Thin Market Manipulation**
- In low-liquidity markets, a single large trade can move the price significantly
- This creates temporary mispricings that revert once normal trading resumes
- Contrarian signal: sudden price move on thin volume without corresponding news

**Narrative Divergence**
- When popular narrative diverges from data-driven analysis
- Example: media narrative says "Candidate X is collapsing" but polling averages show stability
- Edge comes from trusting your model over the crowd's story

### 7. Systematic Scanning & Quantification

**Building a Scanning Pipeline**
- Automated monitoring of multiple platforms for price discrepancies
- Tools: API access to Kalshi, Polymarket, PredictIt; aggregator platforms
- Alert thresholds: trigger when raw spread exceeds fee + minimum profit target

**Edge Quantification Framework**
- Thesis price (your model's output) vs. market price = theoretical edge
- Theoretical edge minus fees, spread, slippage = executable edge
- Executable edge times position size times win probability = expected profit
- Track actual vs. expected over time to validate your edge is real

**Edge Decay & Monitoring**
- Edges shrink as markets become more efficient or as other traders discover the same pattern
- Continuous monitoring of your strategy's hit rate and average edge
- When metrics decline, the inefficiency may be closing

**Concept Prerequisite Map for Other Domains:**
- Edge quantification framework → Portfolio construction & Kelly sizing
- Behavioral biases understanding → Risk management (recognizing your own biases)
- Event catalyst analysis → Trading execution & timing
- Arbitrage mechanics → Automated trading systems
- Contrarian signals → Position management & exit strategies

---

## B) Learning Resources

### Online Courses

1. **"Systematic Edges in Prediction Markets" - Quantpedia**
   - URL: https://quantpedia.com/systematic-edges-in-prediction-markets/
   - Platform: Quantpedia (research article/guide)
   - Duration: ~2 hours reading + implementation
   - Type: Research-grade overview of arbitrage and bias-based edges
   - Difficulty: Intermediate

2. **"Behavioral Finance" - Duke University (Coursera)**
   - URL: https://www.coursera.org/learn/duke-behavioral-finance
   - Platform: Coursera
   - Duration: ~12 hours
   - Covers: Cognitive biases, herd behavior, overconfidence, loss aversion
   - Difficulty: Beginner-Intermediate

3. **"Financial Markets" - Yale (Coursera, Robert Shiller)**
   - URL: https://www.coursera.org/learn/financial-markets-global
   - Platform: Coursera
   - Duration: ~33 hours
   - Covers: Market efficiency, behavioral finance, speculation
   - Difficulty: Beginner-Intermediate

4. **"Algorithmic Trading and Finance Models with Python, R, and Stata" - Udemy**
   - URL: https://www.udemy.com/course/algorithmic-trading-quantitative-analysis-using-python/
   - Platform: Udemy
   - Duration: ~10 hours
   - Covers: Building trading signals, backtesting, systematic scanning
   - Difficulty: Intermediate

### Video Tutorials & Lectures

5. **"How Prediction Markets Work" - Manifold Markets YouTube Channel**
   - URL: https://www.youtube.com/@ManifoldMarkets
   - Type: YouTube channel with tutorials on market mechanics and edge finding
   - Duration: Various (5-30 min each)

6. **"The Complete Polymarket Playbook: Finding Real Edges" - Medium/YouTube discussions**
   - URL: https://medium.com/thecapital/the-complete-polymarket-playbook-finding-real-edges-in-the-9b-prediction-market-revolution-a2c1d0a47d9d
   - Type: Long-form guide with practical strategies
   - Duration: ~30 min read

7. **"An MIT Quant Found a 0.3-Second Loophole in Prediction Markets" - Coinmonks**
   - URL: https://medium.com/coinmonks/an-mit-quant-found-a-0-3-second-loophole-in-prediction-markets-and-built-a-bot-to-exploit-it-dd95b0bfa457
   - Type: Case study on latency arbitrage
   - Duration: ~15 min read

8. **"Arbitrage in Prediction Markets" - Flashbots Collective**
   - URL: https://collective.flashbots.net/t/arbitrage-in-prediction-markets-strategies-impact-and-open-questions/5198
   - Type: Technical discussion on arbitrage strategies and open questions
   - Duration: ~20 min read

### Books

9. **"The Wisdom of Crowds" by James Surowiecki**
   - Relevant chapters: Ch. 1-4 (when crowds are wise and when they fail)
   - Difficulty: Beginner
   - Key takeaway: Understanding when markets aggregate well vs. when biases take over

10. **"Handbook of Sports and Lottery Markets" edited by Hausch & Ziemba**
    - Relevant chapters: Snowberg & Wolfers on favorite-longshot bias
    - Difficulty: Advanced (academic)
    - Key takeaway: Rigorous empirical evidence on persistent market biases

11. **"Thinking, Fast and Slow" by Daniel Kahneman**
    - Relevant chapters: Ch. 10-13 (heuristics and biases), Ch. 24-26 (prospect theory)
    - Difficulty: Intermediate
    - Key takeaway: Foundation for understanding behavioral biases that create mispricings

12. **"Superforecasting: The Art and Science of Prediction" by Philip Tetlock & Dan Gardner**
    - Relevant chapters: Ch. 4-7 (calibration, updating, foxes vs. hedgehogs)
    - Difficulty: Beginner-Intermediate
    - Key takeaway: How to build better probability models that consistently beat the market

13. **"Trading and Exchanges: Market Microstructure for Practitioners" by Larry Harris**
    - Relevant chapters: Ch. 8-12 (informed traders, uninformed traders, parasitic strategies)
    - Difficulty: Intermediate-Advanced
    - Key takeaway: Understanding how edge manifests in order flow and market structure

### Documentation & Reference Materials

14. **Kalshi API Documentation**
    - URL: https://trading-api.readme.io/reference/getmarkets
    - Type: Official API docs for programmatic market scanning
    - Use: Building automated scanning tools

15. **Polymarket Developer Docs**
    - URL: https://docs.polymarket.com/
    - Type: Official API and contract documentation
    - Use: Cross-platform data access for arbitrage detection

16. **Interactive Brokers - Arbitrage in Prediction Markets (Glossary)**
    - URL: https://www.interactivebrokers.com/campus/glossary-terms/arbitrage-prediction-markets/
    - Type: Concise reference on arbitrage mechanics
    - Duration: ~5 min read

17. **"Price Misalignment in Prediction Markets" - Academic Paper**
    - URL: https://researchdmr.com/files/PriceMisalignment.pdf
    - Type: Research paper on systematic mispricings
    - Difficulty: Advanced

### Interactive Exercises & Practice

18. **Manifold Markets (Play Money)**
    - URL: https://manifold.markets/
    - Type: Free play-money prediction market for practicing edge identification
    - Use: Test strategies without financial risk; track your calibration

19. **Metaculus**
    - URL: https://www.metaculus.com/
    - Type: Forecasting platform with scoring and calibration tracking
    - Use: Practice probability estimation and identify when your models diverge from consensus

20. **Prediction Market Arbitrage Scanner (Eventarb)**
    - URL: https://eventarb.com/
    - Type: Free cross-platform arbitrage calculator
    - Use: Real-time practice identifying and sizing arbitrage opportunities

### Podcasts & Audio

21. **"Prediction Markets" episodes on Odd Lots (Bloomberg)**
    - Platform: Bloomberg Podcasts / Apple Podcasts / Spotify
    - Type: Regular coverage of prediction market developments and trading strategies
    - Duration: 30-45 min per episode

22. **"Star Spangled Gamblers" by Keendawg**
    - URL: https://starspangledgamblers.com/
    - Type: Newsletter + podcast focused on political prediction market trading
    - Duration: Weekly episodes, 30-60 min

### GitHub Repositories

23. **prediction-market-arbitrage-bot by realfishsam**
    - URL: https://github.com/realfishsam/prediction-market-arbitrage-bot
    - Type: Python bot for cross-platform arbitrage (Polymarket + Kalshi)
    - Use: Study the codebase to understand scanning and execution logic

24. **Awesome-Prediction-Market-Tools by aarora4**
    - URL: https://github.com/aarora4/Awesome-Prediction-Market-Tools
    - Type: Curated list of prediction market tools, APIs, and resources
    - Use: Discover additional tools for edge identification

25. **polymarket-arbitrage-bot by Trum3it**
    - URL: https://github.com/Trum3it/polymarket-arbitrage-bot
    - Type: Rust-based intra-market arbitrage bot for Polymarket
    - Use: Study execution logic and real-time market monitoring patterns

26. **ArbiDex by dulvinsipsara**
    - URL: https://github.com/dulvinsipsara/ArbiDex
    - Type: Fuzzy logic matching for cross-market arbitrage on Manifold
    - Use: Learn market matching techniques

### Community Resources

27. **r/PredictionMarkets (Reddit)**
    - URL: https://www.reddit.com/r/PredictionMarkets/
    - Active discussion of strategies, platform comparisons, edge identification

28. **r/algotrading (Reddit)**
    - URL: https://www.reddit.com/r/algotrading/
    - Relevant threads on prediction market arbitrage bots and systematic strategies

29. **Polymarket Discord**
    - Active community discussing market analysis, edge, and platform updates

30. **Star Spangled Gamblers Discord / Community**
    - URL: https://starspangledgamblers.com/
    - Community focused on political prediction market trading strategies

---

## C) Learning Path

### Phase 1: Foundations of Edge (Week 1-2, ~15 hours)

**Milestone: Can define each type of edge and explain why mispricings occur**

1. Read Quantpedia "Systematic Edges in Prediction Markets" article
2. Read "The Wisdom of Crowds" chapters 1-4
3. Read "Thinking, Fast and Slow" chapters 10-13 (biases that create edge)
4. Start Coursera "Behavioral Finance" course (Duke)
5. Checkpoint: Write a 1-page summary of 5 types of edge with prediction market examples

### Phase 2: Bias Identification & Behavioral Edge (Week 3-4, ~15 hours)

**Milestone: Can identify favorite-longshot bias and other behavioral patterns in live markets**

1. Read Snowberg & Wolfers paper on favorite-longshot bias (from Handbook of Sports and Lottery Markets or NBER)
2. Read "Superforecasting" chapters 4-7 on calibration
3. Practice on Metaculus: make 50+ forecasts and review calibration
4. Analyze 10 live prediction markets for evidence of behavioral biases
5. Checkpoint: Document 3 specific markets where you identified behavioral mispricing, with your model vs. market price

### Phase 3: Arbitrage Mechanics (Week 5-6, ~15 hours)

**Milestone: Can calculate fee-adjusted arbitrage spreads and identify intra/inter-market opportunities**

1. Read Interactive Brokers arbitrage glossary and Flashbots collective discussion
2. Study the Kalshi and Polymarket API documentation
3. Use Eventarb to scan for current cross-platform opportunities
4. Walk through the realfishsam arbitrage bot codebase
5. Build a simple spreadsheet scanner: input prices from two platforms, output fee-adjusted edge
6. Checkpoint: Identify 3 real arbitrage opportunities (can be historical) with full fee-adjusted P&L calculation

### Phase 4: Stale Pricing & Latency Exploitation (Week 7-8, ~12 hours)

**Milestone: Can detect stale prices and understand latency arbitrage mechanics**

1. Read the "MIT quant 0.3-second loophole" case study
2. Study cross-market staleness patterns (correlating economic data releases with prediction market price movements)
3. Read relevant chapters from Harris "Trading and Exchanges" on informed vs. uninformed traders
4. Monitor 5 markets around a scheduled economic data release; document price lag
5. Checkpoint: Write a post-mortem on one event catalyst, documenting the timeline of information arrival vs. price adjustment

### Phase 5: Event Catalysts & Contrarian Strategy (Week 9-10, ~12 hours)

**Milestone: Can build an event calendar, identify contrarian opportunities, and execute a thesis-driven trade**

1. Build a personal event catalyst calendar for the next 30 days
2. Read the "Complete Polymarket Playbook" guide
3. Practice on Manifold Markets: take 10 contrarian positions with documented reasoning
4. Study 5 historical sentiment extremes and their eventual resolution
5. Checkpoint: Document a complete trade thesis: event catalyst identified, probability model built, edge quantified, position sized, and outcome tracked

### Phase 6: Systematic Scanning & Integration (Week 11-12, ~15 hours)

**Milestone: Have a working scanning pipeline and quantified edge tracking system**

1. Build or configure an automated scanning tool (using APIs + GitHub repos as reference)
2. Create an edge tracking spreadsheet/database: log every trade with thesis price, market price, fees, and outcome
3. Backtest one strategy (e.g., favorite-longshot exploitation) over historical data
4. Review and refine: calculate actual hit rate vs. expected, identify strategy decay signals
5. Checkpoint: Present a portfolio of 20+ tracked trades with aggregate statistics (win rate, average edge, Sharpe-equivalent, edge decay over time)

**Total estimated time: 12 weeks, ~84 hours**

---

## D) Practical Exercises

### Beginner Exercises

**Exercise 1: Bias Safari**
- Visit Polymarket, Kalshi, and Manifold Markets
- Find 5 markets where you suspect behavioral mispricing
- For each: note the current price, your estimated fair value, and which bias you think explains the gap
- Track outcomes over 2 weeks
- Difficulty: Beginner | Time: 3 hours + 2 weeks tracking

**Exercise 2: Arbitrage Calculator**
- Build a spreadsheet with columns: Platform A Price (YES), Platform B Price (NO), Raw Spread, Platform A Fee, Platform B Fee, Net Edge, Annualized Return (given days to settlement)
- Populate with 10 real market pairs from Kalshi and Polymarket
- Identify which (if any) are profitable after fees
- Difficulty: Beginner | Time: 2 hours

**Exercise 3: News Reaction Timer**
- Pick a scheduled economic data release (CPI, jobs report, etc.)
- Monitor a related prediction market contract before, during, and after the release
- Record: exact time of data publication, time of first market price change, magnitude of change, time to stabilization
- Write up your observations on information latency
- Difficulty: Beginner | Time: 2 hours per event

### Intermediate Exercises

**Exercise 4: Favorite-Longshot Backtest**
- Collect historical data from Manifold Markets or Polymarket (API or CSV exports)
- Group resolved markets by implied probability buckets (0-10%, 10-20%, ..., 90-100%)
- Compare implied probability to actual resolution rate per bucket
- Quantify the bias: where do markets consistently over/under-estimate?
- Difficulty: Intermediate | Time: 6-8 hours

**Exercise 5: Cross-Platform Arbitrage Bot (Prototype)**
- Using the Kalshi and Polymarket APIs, write a script that:
  1. Fetches matching markets on both platforms
  2. Calculates fee-adjusted spreads
  3. Flags opportunities above a threshold
- Don't auto-execute; just alert
- Reference: realfishsam's GitHub repo for structure
- Difficulty: Intermediate | Time: 10-15 hours

**Exercise 6: Event Catalyst Journal**
- For 30 days, maintain a daily log:
  - What events occurred today that affected prediction markets?
  - Which markets moved? By how much?
  - Was the move an overreaction or underreaction?
  - Would a pre-event position have been profitable?
- Review at end of 30 days for patterns
- Difficulty: Intermediate | Time: 15-20 min/day for 30 days

### Advanced Exercises

**Exercise 7: Contrarian Strategy Backtest**
- Identify 20 historical markets where consensus exceeded 90% (or dropped below 10%)
- Track the final resolution vs. the extreme consensus price
- Calculate: if you systematically bet against the extreme consensus, what was your return?
- Factor in fees and position sizing
- Difficulty: Advanced | Time: 8-10 hours

**Exercise 8: Multi-Edge Portfolio Simulation**
- Combine 3 edge types (arbitrage + bias exploitation + event catalysts) into a simulated portfolio
- Allocate capital across strategies using Kelly criterion (from later domain, or simplified version)
- Run over 3 months of live paper trading on Manifold Markets
- Track per-strategy and aggregate performance
- Compare to a baseline "buy the consensus" strategy
- Difficulty: Advanced | Time: 20+ hours over 3 months

**Exercise 9: Edge Decay Analysis**
- Pick one specific inefficiency pattern (e.g., intra-market arbitrage on multi-outcome markets)
- Collect data on how quickly the arbitrage closes after it appears
- Plot: edge size vs. time to closure over 50+ observations
- Analyze: is the edge getting faster to close over time? (market efficiency increasing?)
- Difficulty: Advanced | Time: 15-20 hours

### Real-World Application Projects

**Project A: Personal Edge Dashboard**
- Build a dashboard (web app or Jupyter notebook) that:
  - Pulls live data from 2+ prediction market APIs
  - Calculates intra-market arbitrage opportunities
  - Flags contracts where your model price diverges from market by >5%
  - Tracks your edge quantification over time
- Stack: Python + Streamlit or Next.js + API integrations

**Project B: Event-Driven Alert System**
- Create a system that:
  - Monitors an economic calendar API for upcoming events
  - Maps events to relevant prediction market contracts
  - Sends alerts when a relevant event is N minutes away
  - Post-event: tracks market reaction speed and magnitude
- Stack: Python + scheduling + notification (Telegram bot or similar)

**Project C: Bias Quantification Research Paper**
- Conduct original research on a specific bias in prediction markets
- Collect data from Polymarket or Manifold API
- Apply statistical tests to quantify the bias
- Write up findings in academic-style format
- Potential publication: submit to Journal of Prediction Markets or share on prediction market forums

---

## Applicability to Overall Mastery Goal

Edge identification is the core skill that separates profitable prediction market traders from the crowd. This domain connects to every other domain in the mastery roadmap:

- **Probability & Statistics** provides the mathematical tools for building fair value models
- **Market Mechanics** tells you where to look for structural inefficiencies
- **Microstructure & Order Flow** explains how edges manifest in the order book
- **Fair Value Estimation** gives you the "thesis price" to compare against market price
- **Portfolio Construction** (upcoming) determines how much to allocate to each identified edge
- **Risk Management** (upcoming) protects you when your edge estimate is wrong
- **Automated Trading** (upcoming) scales your edge identification through systematic scanning
- **Psychology & Discipline** (upcoming) prevents you from becoming the behavioral edge that others exploit

Without the ability to identify and quantify edge, all other skills are academic. This domain is where theory becomes profit.
