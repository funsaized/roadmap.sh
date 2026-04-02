# Prediction Market Mechanics & Platforms

## Domain Overview

This domain covers how prediction markets work, the contract types traded on them, the trading mechanisms that power them, a comparison of major platforms, and the regulatory landscape. Mastery here is foundational for all downstream domains: arbitrage strategies, information sourcing, market making, and algorithmic trading all depend on a solid understanding of platform mechanics.

---

## A) Key Concepts

### 1. Binary Contracts (Yes/No Contracts)
The most common prediction market contract type. A question is framed as yes/no (e.g., "Will Bitcoin exceed $100K by Dec 31?"). Contracts trade between $0.01 and $0.99, with the price representing the market-implied probability. Winning contracts pay $1.00; losing contracts pay $0.

**Relationship:** Foundation for all other contract types. Understanding binary pricing is prerequisite for multi-outcome and scalar contracts.

### 2. Multi-Outcome Contracts
Markets with more than two possible results (e.g., "Which team wins the NBA Finals?"). Each outcome trades as a separate contract. In a well-functioning market, all outcome prices sum to ~$1.00. Analyzing these requires assessing relative probabilities across many outcomes simultaneously.

**Relationship:** Extension of binary contracts. Introduces portfolio thinking and relative value assessment.

### 3. Scalar (Range) Contracts
Contracts linked to a continuous numerical range (e.g., "What will US inflation be?"). Defined by upper and lower bounds. Payout is proportional to where the actual outcome falls within the range, not winner-take-all. Uses "Long" and "Short" positions.

**Relationship:** More complex pricing than binary. Requires understanding of expected value calculations. Prerequisite for quantitative modeling domain.

### 4. Order Book Trading Mechanism
A real-time list of buy (bid) and sell (ask) orders at various price levels, matching buyers and sellers directly. Traders place limit orders at specific prices or market orders for immediate execution. Provides transparency into supply/demand via market depth.

**Key properties:**
- Tighter spreads in liquid markets
- Price discovery driven by individual order flow
- Requires sufficient active participants for efficiency
- Used by Kalshi, Polymarket, and Robinhood Derivatives

**Relationship:** Core to understanding how prices form. Prerequisite for market making and arbitrage domains.

### 5. Automated Market Maker (AMM)
Algorithm-based trading where traders interact with a liquidity pool rather than other traders. Price adjusts automatically based on token ratios in the pool using mathematical formulas (e.g., Logarithmic Market Scoring Rule / LMSR, constant product). Liquidity providers earn fees but face impermanent loss risk.

**Key properties:**
- Continuous liquidity regardless of participant count
- Mechanical price adjustment (not opinionated)
- Large trades cause significant price impact (slippage)
- Impermanent loss is especially problematic with binary outcome tokens

**Relationship:** Contrasts with order books. Most major platforms have moved away from AMMs for prediction markets due to impermanent loss issues, but understanding AMMs matters for DeFi-based platforms and future innovations (e.g., Paradigm's pm-AMM research).

### 6. Liquidity and Market Depth
Liquidity measures how easily contracts can be bought/sold without significantly moving the price. Market depth shows the volume of orders at each price level in the order book. Low liquidity means wider spreads and higher execution costs.

**Relationship:** Critical for all trading strategies. Directly affects profitability of arbitrage, market making, and position sizing.

### 7. Bid-Ask Spread
The difference between the highest price a buyer is willing to pay (bid) and the lowest price a seller will accept (ask). Tighter spreads indicate more liquid, efficient markets. The spread represents a cost to takers and revenue opportunity for makers.

**Relationship:** Directly linked to fee structure analysis and market making strategies.

### 8. Order Types (Market, Limit, Maker/Taker)
- **Market orders:** Execute immediately at best available price (taker)
- **Limit orders:** Set a specific price; only execute when matched (can be maker)
- **Maker orders:** Add liquidity to the book (often lower or zero fees)
- **Taker orders:** Remove liquidity from the book (typically higher fees)

**Relationship:** Understanding order types is essential for fee optimization and execution strategy.

### 9. Settlement and Resolution
The process of finalizing contracts after an event concludes. Involves verifying the outcome against pre-defined resolution sources, then automatically paying out winners ($1) and zeroing losers ($0). Settlement rules vary by platform and must be read carefully before trading.

**Key aspects:**
- Resolution sources are specified upfront (official data providers, government reports)
- Settlement timing may lag the actual event
- Disputes can arise from ambiguous resolution criteria

**Relationship:** Prerequisite for understanding settlement risk and resolution edge in event-driven trading.

### 10. Oracle Mechanisms (Decentralized Markets)
Bridges that fetch, verify, and deliver real-world data to blockchain smart contracts for automated settlement. Examples: Chainlink, UMA Optimistic Oracle. Decentralized oracle networks distribute trust across multiple data sources and node operators. Include dispute resolution mechanisms for contested outcomes.

**Relationship:** Specific to blockchain-based platforms like Polymarket. Understanding oracles matters for assessing platform risk and settlement reliability.

### 11. Platform Comparison: Kalshi
- **Type:** CFTC-regulated Designated Contract Market (DCM)
- **Currency:** USD (bank transfer, debit card)
- **Trading mechanism:** Order book
- **Markets:** Politics, economics, sports, weather, culture
- **Fees:** Variable formula based on probability: `ceil(0.07 * C * P * (1-P))` for takers; `ceil(0.0175 * C * P * (1-P))` for makers; lower fees on S&P/Nasdaq markets
- **Settlement:** Automated, based on official resolution sources
- **Deposit/withdrawal:** ACH and wire free; debit card 2% fee
- **Key advantage:** Full US regulatory compliance; USD deposits; broad market categories
- **Key limitation:** Fee structure penalizes 50/50 contracts; US-only

### 12. Platform Comparison: Polymarket
- **Type:** Decentralized prediction market on Polygon blockchain (re-entered US market late 2025 via QCEX acquisition)
- **Currency:** USDC stablecoin
- **Trading mechanism:** Order book (CLOB); previously used AMM/LMSR but transitioned
- **Markets:** Politics, crypto, sports, global events, culture
- **Fees:** Dynamic taker fees varying by category (crypto ~1.80% peak, sports ~0.75%, politics ~1.00%); maker rebates (20-50%); geopolitical markets fee-free; 0% fee on profits
- **Settlement:** UMA Optimistic Oracle with dispute resolution
- **Deposit/withdrawal:** USDC via crypto wallet or MoonPay; no platform fees on deposits/withdrawals
- **Key advantage:** Deepest liquidity for political/global events; no profit fee; open API ecosystem
- **Key limitation:** Requires crypto wallet familiarity; dynamic fees can be complex

### 13. Platform Comparison: PredictIt
- **Type:** Not-for-profit research market (Victoria University of Wellington)
- **Currency:** USD
- **Trading mechanism:** Order book (simplified)
- **Markets:** US political and public affairs only
- **Fees:** 10% fee on net profits; 5% withdrawal fee; no deposit fee
- **Investment cap:** $3,500 per contract (raised from $850 in July 2025)
- **Settlement:** Based on official election/government results
- **Key advantage:** Simplest interface; focused on political markets
- **Key limitation:** High fee drag (10% profit + 5% withdrawal); limited market categories; lower liquidity

### 14. Platform Comparison: Robinhood Derivatives
- **Type:** CFTC-regulated via partnership with KalshiEx
- **Currency:** USD (integrated with Robinhood brokerage account)
- **Trading mechanism:** Order book
- **Markets:** Event contracts (via Kalshi infrastructure) plus futures
- **Fees:** $0.01/contract/side for event contracts; plus $0.02 NFA assessment + $0.01 exchange fee per contract/side; Gold members get discounted futures commissions
- **Settlement:** Exchange-level settlement through KalshiEx
- **Key advantage:** Lowest per-contract fees; familiar Robinhood UI; integrated with existing brokerage
- **Key limitation:** Newer platform; narrower market selection than standalone platforms

### 15. CFTC Regulation and Legal Framework
The Commodity Futures Trading Commission (CFTC) regulates prediction markets as event derivatives under the Commodity Exchange Act. Key developments:
- Kalshi won a federal court ruling (Oct 2024) allowing election contracts
- CFTC withdrew proposed ban on political/sports contracts
- Ongoing federal vs. state jurisdiction conflict (states argue prediction markets are gambling)
- CFTC initiated ANPRM (2026) for tailored prediction market regulation

**Relationship:** Understanding regulation determines which platforms you can legally use and which market types are available. Prerequisite for arbitrage (cross-platform legality) and risk management.

### 16. Price as Probability
The core information-theoretic principle: contract prices in prediction markets approximate the crowd's aggregated probability estimate. A contract at $0.65 implies a 65% probability. This is the bridge between prediction markets and Bayesian reasoning (completed domain).

**Relationship:** Direct connection to the Probability & Bayesian Reasoning domain. Foundation for all pricing and forecasting analysis.

### 17. Contract Specifications and Resolution Criteria
Every market has specific rules defining exactly how it resolves: the data source, the time window, edge cases, and what happens in ambiguous scenarios. Reading these before trading is critical because resolution rules, not common sense, determine payouts.

**Relationship:** Prerequisite for avoiding settlement surprises. Connects to event-driven trading and risk management.

---

## B) Learning Resources

### Online Courses

1. **Mastering Prediction Markets (DeFi Education)** - 90 minutes
   - Platform: Substack/self-hosted
   - URL: https://defieducation.substack.com/p/new-course-mastering-prediction-markets
   - Covers market design, payoff structures, resolution rules, regulatory landscape
   - Includes downloadable templates
   - Cost: Paid
   - Difficulty: Beginner-Intermediate

2. **Prediction Market Academy** - Self-paced
   - Platform: predictionmarketacademy.com
   - URL: https://predictionmarketacademy.com/
   - Covers introduction to event forecasting, portfolio building, correlation trading, economic indicators
   - Cost: Free guides + premium content
   - Difficulty: Beginner-Advanced

3. **Polymarket Trading Course** - Self-paced
   - Platform: polymarketcourse.com
   - URL: https://polymarketcourse.com/
   - Step-by-step system for spotting mispriced probabilities, risk-first bankroll sizing
   - Cost: Paid
   - Difficulty: Beginner-Intermediate

4. **Gate.io Learn: Introduction to Polymarket** - ~1 hour
   - Platform: Gate.io
   - URL: https://www.gate.com/learn/course/introduction-to-polymarket/understanding-prediction-markets-and-info-finance
   - Understanding prediction markets and information finance
   - Cost: Free
   - Difficulty: Beginner

5. **Marginal Revolution University: Prediction Markets** - ~15 minutes
   - Platform: MRU
   - URL: https://mru.org/courses/principles-economics-microeconomics/prediction-markets-election-forecasting
   - How prices convey information and predict future events
   - Cost: Free
   - Difficulty: Beginner

### Video Tutorials and Lectures

6. **"How to ACTUALLY Profit on Polymarket/Kalshi (FULL GUIDE)"** - YouTube
   - URL: https://www.youtube.com/watch?v=3jUI4pU2RtQ
   - Comprehensive beginner strategy guide

7. **"Full Prediction Markets Guide for Maximum Profits [Kalshi Beginner Tutorial]"** - YouTube
   - URL: https://www.youtube.com/watch?v=u3-g-CjEhNY
   - Kalshi-specific walkthrough with fee optimization

8. **"Complete Polymarket Trading Guide (Step-by-Step for Beginners)"** - YouTube
   - URL: https://www.youtube.com/watch?v=VLCopiRgb24
   - Polymarket setup, wallet connection, first trades

9. **"Live Trading Kalshi Prediction Markets! [Beginner-Friendly Guide]"** - YouTube
   - URL: https://www.youtube.com/watch?v=lmmgVZscZso
   - Real-time trading demonstration

### Books

10. **"Prediction Markets: Theory and Applications"** - Leighton Vaughan Williams
    - Publisher: Routledge
    - URL: https://www.routledge.com/Prediction-Markets-Theory-and-Applications/VaughanWilliams/p/book/9781138802902
    - Covers information aggregation, forecasting, policy applications
    - Difficulty: Intermediate-Advanced (academic)
    - Relevant chapters: All (focused textbook)

11. **"Prediction Markets: Fundamentals, Designs, and Applications"** - Luckner, Schröder, Slamka et al.
    - Publisher: Springer/Gabler
    - URL: https://books.google.com/books/about/Prediction_Markets.html?id=o9NUHFGAQjUC
    - Wisdom of crowds, market design, applications
    - Difficulty: Intermediate (academic)

12. **"The Wisdom of Crowds"** - James Surowiecki
    - Classic popular science book explaining why groups make better predictions than individuals
    - Difficulty: Beginner
    - Relevant chapters: Part I (The Wisdom of Crowds), Part II (especially chapters on markets)

### Documentation and Reference Materials

13. **Polymarket Official Documentation**
    - URL: https://docs.polymarket.com/
    - API reference, trading mechanics, market data, CLOB architecture
    - Essential for understanding Polymarket's technical infrastructure

14. **Kalshi Fee Schedule (PDF)**
    - URL: https://kalshi.com/docs/kalshi-fee-schedule.pdf
    - Official fee formulas and examples

15. **Kalshi Help Center: Fees**
    - URL: https://help.kalshi.com/en/articles/13823805-fees
    - Detailed fee explanations with examples

16. **Polymarket Trading Fees Documentation**
    - URL: https://docs.polymarket.com/trading/fees
    - Dynamic fee model explanation by category

17. **Wharton Primer on Prediction Markets**
    - URL: https://wifpr.wharton.upenn.edu/blog/a-primer-on-prediction-markets/
    - Academic primer on contract types, market designs, regulatory implications

18. **Corporate Finance Institute: Prediction Markets**
    - URL: https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/prediction-market/
    - Overview of market types, mechanisms, and functioning

19. **Chainlink: How Prediction Markets Work (Technical)**
    - URL: https://chain.link/article/how-prediction-markets-work-technical
    - Technical deep dive on smart contracts, oracles, and settlement

20. **Robinhood Derivatives Fee Schedule (PDF)**
    - URL: https://cdn.robinhood.com/assets/robinhood/legal/RHD_Fee_Schedule.pdf
    - Official fee documentation

### GitHub Repositories and Open-Source Projects

21. **Polymarket CLOB Client (Python)**
    - URL: https://github.com/polymarket/py-clob-client
    - Official Python client for Polymarket's order book API

22. **Polymarket Agents Framework**
    - URL: https://github.com/polymarket/agents
    - AI agent framework for building automated Polymarket traders (MIT License)

23. **Awesome Polymarket Tools**
    - URL: https://github.com/harish-garg/Awesome-Polymarket-Tools
    - Curated list of tools, bots, analytics, and resources

24. **Paradigm pm-AMM Research**
    - URL: https://www.paradigm.xyz/2024/11/pm-amm
    - Novel AMM design specifically for prediction markets (academic research)

### Podcasts and Audio

25. **Star Spangled Gamblers** - Pratik Chougule
    - URL: https://podcasts.apple.com/us/podcast/star-spangled-gamblers/id1437934639
    - Political prediction market analysis, platform news, trader interviews
    - Highly relevant for political market mechanics

26. **Prediction Market Movers**
    - URL: https://podcasts.apple.com/us/podcast/prediction-market-movers/id1840287346
    - Features platform founders and top traders; covers market structure

27. **Complex Systems Podcast: Prediction Markets (Stephen Grugett / Manifold)**
    - URL: https://www.complexsystemspodcast.com/episodes/prediction-markets-stephen-grugett/
    - Deep dive on market design with Manifold Markets co-founder

### Community Resources

28. **r/Kalshi** - Reddit
    - URL: https://www.reddit.com/r/Kalshi/
    - Active community discussing Kalshi strategies, fees, and platform updates

29. **r/Polymarket** - Reddit
    - URL: https://www.reddit.com/r/Polymarket/
    - Polymarket trading discussion, tools, and market analysis

30. **r/ManifoldMarkets** - Reddit
    - URL: https://www.reddit.com/r/ManifoldMarkets/
    - Discussion of play-money prediction markets (good for practice)

31. **Polymarket Discord**
    - Active community with channels for market discussion, API help, and strategy

32. **Kalshi Blog / Newsletter**
    - URL: https://news.kalshi.com/
    - Platform updates, trading guides, and market analysis

---

## C) Learning Path Within This Domain

### Phase 1: Foundations (3-5 hours)
**Goal:** Understand what prediction markets are and how contracts work

1. Watch MRU video on prediction markets (~15 min)
2. Read Wharton primer on prediction markets (~30 min)
3. Read CFI overview of prediction markets (~20 min)
4. Study binary contract mechanics: pricing, payoff, probability interpretation (~1 hr)
5. Learn multi-outcome and scalar contract types (~1 hr)
6. Read Chainlink technical article on how prediction markets work (~30 min)

**Milestone:** Can explain how a binary contract priced at $0.72 represents a 72% probability, describe how multi-outcome contracts sum to $1, and explain scalar contract payoff mechanics.

### Phase 2: Trading Mechanisms (3-4 hours)
**Goal:** Understand order books vs AMMs and their tradeoffs

1. Study order book mechanics: bids, asks, depth, matching (~1.5 hr)
2. Study AMM mechanics: liquidity pools, LMSR, constant product (~1.5 hr)
3. Compare order book vs AMM tradeoffs (spread, slippage, liquidity) (~30 min)
4. Read Paradigm pm-AMM paper for cutting-edge AMM research (~30 min)
5. Understand maker/taker dynamics and their fee implications (~30 min)

**Milestone:** Can explain why Polymarket moved from AMM to CLOB, describe impermanent loss in prediction market context, and identify which mechanism a given platform uses.

### Phase 3: Platform Deep Dives (4-6 hours)
**Goal:** Compare platforms and understand fee structures

1. Create accounts on Kalshi and Polymarket (~1 hr)
2. Study Kalshi fee schedule with worked examples (~1 hr)
3. Study Polymarket dynamic fee model by category (~1 hr)
4. Review PredictIt fee structure (10% profit + 5% withdrawal) (~30 min)
5. Review Robinhood Derivatives fee schedule (~30 min)
6. Build a comparison spreadsheet: fees for $100 trade at various probabilities across platforms (~1 hr)
7. Watch beginner tutorial videos for Kalshi and Polymarket (~1.5 hr)

**Milestone:** Can calculate exact fees for a given trade on each platform, identify the cheapest platform for a specific trade, and explain the fee advantage of maker vs taker orders.

### Phase 4: Regulation and Settlement (2-3 hours)
**Goal:** Understand the legal landscape and resolution mechanics

1. Read about CFTC regulation of event contracts (~45 min)
2. Study Kalshi v. CFTC court ruling and its implications (~30 min)
3. Understand federal vs state jurisdiction conflict (~30 min)
4. Study settlement processes: resolution sources, timing, disputes (~30 min)
5. Learn oracle mechanisms (UMA Optimistic Oracle, Chainlink) (~30 min)
6. Read resolution criteria for 5+ markets across platforms (~30 min)

**Milestone:** Can explain why some markets are legal on Kalshi but contested by states, describe how Polymarket resolves disputes via UMA oracle, and identify key resolution risks.

### Phase 5: Hands-On Trading (3-5 hours)
**Goal:** Execute real trades and build platform fluency

1. Fund Kalshi account with small amount ($25-50) and place 3+ trades using both market and limit orders (~1.5 hr)
2. Set up crypto wallet, acquire USDC, and place 3+ trades on Polymarket using limit orders (~1.5 hr)
3. Explore Polymarket API documentation and run basic data queries (~1 hr)
4. Compare execution experience: fees paid, fill speed, UX differences (~30 min)
5. Document lessons learned (~30 min)

**Milestone:** Have placed real trades on 2+ platforms, can demonstrate limit order placement, have calculated actual fees incurred, and can articulate UX/cost tradeoffs between platforms.

**Total estimated time: 15-23 hours**

---

## D) Practical Exercises

### Exercise 1: Contract Type Identification (Beginner, 30 min)
Browse Kalshi and Polymarket. Categorize 10 markets each as binary, multi-outcome, or scalar. For each, note the resolution source, settlement date, and current implied probability.

### Exercise 2: Fee Calculator Spreadsheet (Beginner, 1-2 hours)
Build a spreadsheet that calculates trading fees across Kalshi, Polymarket, PredictIt, and Robinhood Derivatives for:
- A $100 position at probabilities of 10%, 25%, 50%, 75%, 90%
- Both maker and taker orders where applicable
- Include withdrawal fees for PredictIt
- Visualize with a chart showing total cost by probability and platform

### Exercise 3: Order Book Analysis (Intermediate, 1 hour)
Pick 3 active markets on Kalshi or Polymarket. For each:
- Record the bid-ask spread at 3 different times of day
- Note the depth at the top 3 price levels
- Calculate the cost of filling a $500 market order vs a limit order
- Identify which markets have the tightest spreads and hypothesize why

### Exercise 4: Cross-Platform Price Comparison (Intermediate, 1-2 hours)
Find 5 events listed on both Kalshi and Polymarket. For each:
- Record the Yes/No prices on both platforms at the same time
- Calculate the price differential
- Determine if any arbitrage opportunity exists after accounting for fees on both sides
- Document the results and any patterns (which platform tends to price higher/lower?)

### Exercise 5: Resolution Criteria Deep Dive (Intermediate, 1 hour)
Pick 5 markets with complex or ambiguous resolution criteria. For each:
- Identify the exact resolution source
- Find edge cases that could cause unexpected resolution
- Determine if the market could resolve differently than a casual reader would expect
- Write up the risk assessment

### Exercise 6: Paper Trading Multi-Outcome Markets (Intermediate, 2-3 hours)
Track a multi-outcome market (e.g., "Who will win X?") over one week:
- Record all outcome prices daily
- Verify prices sum to ~$1.00 (or identify deviations)
- Identify when individual outcome prices moved significantly and correlate with news events
- Calculate what your P&L would have been if you had bought the eventual winner at various entry points

### Exercise 7: Platform UX Comparison Report (Beginner, 2 hours)
Create a structured comparison of Kalshi and Polymarket covering:
- Account creation process (time, KYC requirements)
- Funding methods and speed
- Market discovery and search
- Order placement workflow
- Position management and P&L tracking
- Mobile vs desktop experience
- Rate each dimension 1-5 and write a recommendation for which platform suits different trader profiles

### Exercise 8: API Exploration (Advanced, 2-3 hours)
Using the Polymarket Python CLOB client:
- Fetch current markets and prices for 3 categories
- Pull order book data for an active market
- Calculate mid-price, spread, and depth programmatically
- Save results to a CSV for later analysis
- This exercise builds the foundation for the Algorithmic Trading Systems domain

---

## Connections to Other Domains

| This Domain's Concept | Feeds Into Domain | How |
|---|---|---|
| Order book mechanics | Arbitrage & Cross-Platform Strategies | Understanding execution and spreads across platforms |
| Order book mechanics | Market Making & Liquidity Provision | Maker/taker dynamics, spread capture |
| Fee structures | Arbitrage & Cross-Platform Strategies | Fees determine arbitrage profitability thresholds |
| Platform comparison | Information Sources & Research Methods | Knowing where different event types are best covered |
| Settlement/resolution | Event-Driven & Catalyst Trading | Resolution risk assessment |
| Price as probability | Pricing Theory for Binary Contracts | Foundation for fair value calculation |
| Regulation | Risk Management & Bankroll Strategy | Regulatory risk as a portfolio consideration |
| API/technical infrastructure | Algorithmic & Automated Trading Systems | Programmatic trading capability |
