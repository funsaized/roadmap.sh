# Arbitrage & Cross-Platform Strategies

**Domain Level:** Advanced (9 of 15)
**Prerequisites:** Market Mechanics, Pricing Theory, Risk Management
**Feeds Into:** Market Making, Algorithmic Systems

---

## A) Key Concepts

### 1. Cross-Platform Arbitrage Fundamentals

**Price Divergence Identification**
Different prediction market platforms (Polymarket, Kalshi, Robinhood Derivatives, Manifold) price the same real-world event differently due to varying user demographics, liquidity pools, fee structures, and information flow speeds. The core opportunity: buy YES on Platform A at $0.42 and NO on Platform B at $0.55, paying $0.97 total for a guaranteed $1.00 payout. Relates directly to: fee-adjusted calculations, execution risk.

**Implied Probability Comparison**
Each contract price represents an implied probability. When the same event's implied probability differs across platforms by more than the combined fee drag, an arbitrage exists. This is the detection mechanism that monitoring tools implement.

**Market Efficiency and Spread Compression**
As markets mature and more participants (especially bots) enter, spreads compress. Early-mover advantage matters. Understanding efficiency dynamics helps you assess which market pairs are most likely to present opportunities. Academic research documented $40M+ in arbitrage profits on Polymarket alone between April 2024 and April 2025.

### 2. Dutch Booking

**Dutch Book Definition**
A Dutch book exists when the implied probabilities for all mutually exclusive outcomes of an event sum to less than 100% (or equivalently, the cost to buy all outcome shares is less than $1.00). This guarantees profit regardless of which outcome occurs.

**Dutch Book Detection Formula**
For outcomes with decimal odds O_1, O_2, ..., O_n: calculate R = (1/O_1) + (1/O_2) + ... + (1/O_n). If R < 1, a Dutch book exists with profit margin (1 - R). If R > 1, the "house" has an edge.

**Optimal Stake Calculation**
To ensure equal profit across all outcomes with total investment T:
- Stake_i = ((1/O_i) / R) * T
This distributes capital proportionally so every outcome produces the same net return.

**Single-Market vs. Cross-Market Dutch Books**
Single-market Dutch books (YES + NO < $1.00 on one platform) are simpler but rarer and smaller. Cross-market Dutch books (assembling the complete outcome set across platforms) offer larger spreads but introduce execution and settlement risk.

### 3. Correlated Market Arbitrage (Combinatorial Arbitrage)

**Logical Dependency Between Markets**
Markets covering related events can be mispriced relative to each other. Example: if "Trump wins presidency" trades at 55% and "Republican wins presidency" at 50%, that violates the logical constraint P(Trump wins) <= P(Republican wins). This creates an exploitable position.

**Conditional Probability Constraints**
P(A|B) = P(A and B) / P(B). When market-implied probabilities violate these constraints, a portfolio of positions across the correlated markets guarantees profit. Identifying these requires semantic understanding of market questions, not just price monitoring.

**LLM-Assisted Dependency Detection**
Recent research uses large language models to identify conditional probability relationships between market questions that lack obvious lexical overlap. However, approximately 62% of LLM-detected dependencies fail to produce actionable arbitrage due to liquidity constraints and execution friction.

**Scalability Challenges**
Naive pairwise comparison across N markets requires O(N^2) checks. Practical combinatorial arbitrage systems use clustering, semantic similarity, and category-based filtering to reduce the search space.

### 4. Execution and Settlement Risk

**Leg Risk**
Cross-platform arbitrage requires executing trades on multiple platforms. If one leg fills but the other doesn't (price moved, insufficient liquidity, API failure), you're left with a directional bet instead of an arbitrage. This is the primary risk in cross-platform strategies.

**Resolution Criteria Mismatch**
Platforms may define "the same event" with subtle differences in resolution criteria, settlement dates, or data sources. A contract might settle YES on one platform and NO on another for what appears to be the same question. Always compare exact resolution rules before trading.

**Oracle Risk**
Decentralized platforms rely on oracles to determine outcomes. Oracle compromise, inaccurate data feeds, or resolution disputes can invalidate seemingly guaranteed payouts. Polymarket uses UMA's optimistic oracle; Kalshi uses internal resolution.

**Settlement Timing**
Different platforms settle at different speeds. On-chain resolution can take days or weeks, locking capital. Factor the time value of money into arbitrage calculations, especially for longer-dated events.

**Platform/Counterparty Risk**
Smart contract bugs, platform insolvency, regulatory action (see: Arizona criminal charges against Kalshi in March 2026), or rule changes can result in total loss of funds on one leg.

### 5. Fee-Adjusted Calculations

**Fee Structure Comparison**
- Polymarket: maker orders often 0% fee, taker orders ~1-2%
- Kalshi: transaction fees 0.7-1.2% on expected earnings
- Robinhood Derivatives: commission-free but wider spreads
Fee structures differ not just in percentage but in what they're applied to (trade value vs. profit vs. settlement).

**Net Arbitrage Profit Formula**
Net Profit = $1.00 - (Cost_Platform_A + Cost_Platform_B) - Fee_A - Fee_B - Gas/Transfer_Costs
Only proceed when Net Profit > 0 after ALL costs including blockchain gas fees (for Polymarket), wire/ACH fees, and currency conversion costs.

**Break-Even Spread Calculation**
Minimum required price divergence = Fee_A + Fee_B + Slippage_Estimate + Transfer_Costs. If the observed spread is below this threshold, the opportunity is unprofitable.

**Slippage Modeling**
Large orders move prices. Estimate slippage by examining order book depth on both platforms. The executable spread at your desired size may be significantly narrower than the top-of-book spread.

### 6. API Trading Infrastructure

**Platform APIs**
- **Polymarket CLOB API:** REST + WebSocket. Three services: CLOB (trading), Gamma (market discovery), Data (positions/history). EIP-712 signed orders, HMAC-SHA256 auth. SDKs in TypeScript, Python, Rust. Rate limits: 100 public requests/min, 60 orders/min.
- **Kalshi API:** REST + WebSocket. RSA-PSS authentication. Token expiry every 30 minutes. SDKs available. Demo environment for testing. Endpoints: /markets, /events, /orders, /portfolio.

**Unified APIs and Aggregators**
- **Dome:** YC-backed unified API for multiple prediction markets. Multi-language SDKs, real-time streaming.
- **pmxt (Prediction Market Exchange Toolkit):** Unified API for Polymarket + Kalshi. Enables near-simultaneous execution across platforms.

**Order Types for Arbitrage**
Fill-or-Kill (FOK) orders are preferred for arbitrage: the entire order fills at the specified price or is cancelled entirely, preventing partial fills that leave you with unhedged exposure.

**WebSocket Feeds**
Real-time order book monitoring via WebSocket connections is essential for detecting opportunities. REST polling introduces latency that can miss fleeting spreads.

**Infrastructure Requirements**
Low-latency VPS (ideally colocated near exchange servers), reliable network connectivity, credential rotation, IP whitelisting, and circuit breakers for abnormal conditions.

### 7. Monitoring and Alert Systems

**Real-Time Price Scanning**
Continuously compare prices across platforms for matched events. Requires event matching (mapping the same question across platforms with different naming conventions) and normalization of price data.

**Alert Thresholds**
Configure minimum profitable spread thresholds per platform pair, accounting for fees. Only alert when net expected profit exceeds a configurable minimum (e.g., $0.02 per contract after all costs).

**Event Matching Algorithms**
Automated systems must match events across platforms that may describe the same outcome differently. Approaches range from simple string matching to NLP-based semantic similarity.

**Dashboard and Logging**
Track all detected opportunities, execution attempts, fill rates, actual vs. expected profit, and missed opportunities for strategy refinement.

### 8. Regulatory Constraints

**CFTC Jurisdiction**
The CFTC claims exclusive jurisdiction over event contracts traded on designated contract markets (DCMs). Kalshi operates as a CFTC-regulated DCM. The regulatory landscape is actively evolving with a new ANPRM (March 2026) soliciting public comment through April 30, 2026.

**State Gambling Laws**
State regulators contest CFTC preemption. Arizona filed criminal charges against Kalshi (March 2026). Traders must understand the legal status of prediction markets in their jurisdiction.

**Cross-Border Considerations**
Polymarket's offshore operations serve non-US users differently from US users. Capital movement across platforms may trigger reporting requirements. KYC/AML compliance varies by platform.

**Insider Trading**
CFTC has issued advisories and pursued enforcement actions related to informed trading in prediction markets. Trading on material non-public information carries legal risk.

**Tax Implications**
Prediction market profits are taxable. Cross-platform strategies generate complex tax reporting needs (different 1099 forms, USDC on-chain transactions, etc.).

---

### Concept Relationship Map

```
Cross-Platform Price Divergence
    ├── Dutch Booking (complete outcome coverage)
    ├── Correlated Market Arbitrage (conditional probability violations)
    └── Both require:
        ├── Fee-Adjusted Calculations (profitability filter)
        ├── Execution Risk Management (leg risk, slippage)
        ├── API Trading Infrastructure (speed, reliability)
        ├── Monitoring Systems (detection, alerting)
        └── Regulatory Awareness (legal constraints)
```

### Prerequisites for Downstream Domains

- **Market Making:** Understanding arbitrage mechanics is foundational to market making, where you provide liquidity and profit from spreads. Arbitrage detection helps market makers manage inventory risk.
- **Algorithmic Systems:** API trading infrastructure, real-time monitoring, and automated execution developed here are the building blocks for full algorithmic trading systems.

---

## B) Learning Resources

### Online Courses

1. **"Algorithmic Trading & Quantitative Analysis Using Python"** - Udemy
   - URL: https://www.udemy.com/course/algorithmic-trading-quantitative-analysis-using-python/
   - Platform: Udemy | Duration: ~12 hours | Cost: Paid (~$20-50 on sale)
   - Relevance: Covers order execution, API integration, and building trading bots. Apply concepts to prediction market APIs.

2. **"Financial Markets"** by Robert Shiller - Yale/Coursera
   - URL: https://www.coursera.org/learn/financial-markets-global
   - Platform: Coursera | Duration: ~33 hours | Cost: Free to audit
   - Relevance: Module on futures and derivatives markets. Provides theoretical grounding for understanding arbitrage pricing theory.

3. **"Cryptocurrency and Blockchain: An Introduction to Digital Currencies"** - Wharton/Coursera
   - URL: https://www.coursera.org/learn/wharton-cryptocurrency-blockchain-introduction-digital-currency
   - Platform: Coursera | Duration: ~10 hours | Cost: Free to audit
   - Relevance: Understanding blockchain settlement, smart contracts, and DeFi mechanics used by Polymarket.

### Video Tutorials and Lectures

4. **"How Prediction Market Arbitrage Works (Polymarket vs Kalshi)"** - Trevor Lasn
   - URL: https://www.trevorlasn.com/blog/how-prediction-market-polymarket-kalshi-arbitrage-works
   - Type: Blog + walkthrough | Duration: ~30 min read
   - Covers practical mechanics of cross-platform arbitrage with fee calculations.

5. **"I Built a Bot to Automate Risk-Free Arbitrage"** - Reddit r/algotrading discussion
   - URL: https://www.reddit.com/r/algotrading/comments/1qebxud/i_built_a_bot_to_automate_riskfree_arbitrage/
   - Type: Community discussion | Duration: ~20 min read
   - Real practitioner experiences, implementation details, and pitfalls encountered.

6. **"Automating the Prediction Market Arb"** - Reddit r/algotrading
   - URL: https://www.reddit.com/r/algotrading/comments/1qbq7j1/automating_the_prediction_market_arb/
   - Type: Community discussion | Duration: ~15 min read
   - Technical discussion on automation approaches, API quirks, and latency considerations.

### Books

7. **"Trading and Exchanges: Market Microstructure for Practitioners"** by Larry Harris
   - Publisher: Oxford University Press | Difficulty: Advanced
   - Relevant Chapters: Ch. 7 (Arbitrageurs), Ch. 9 (Execution), Ch. 19 (Market Manipulation)
   - The definitive text on market microstructure, directly applicable to understanding order books and execution in prediction markets.

8. **"Algorithmic Trading: Winning Strategies and Their Rationale"** by Ernest Chan
   - Publisher: Wiley | Difficulty: Intermediate-Advanced
   - Relevant Chapters: Ch. 1-3 (backtesting, execution), Ch. 7 (statistical arbitrage)
   - Practical framework for building and evaluating automated trading strategies.

9. **"The Wisdom of Crowds"** by James Surowiecki
   - Publisher: Anchor Books | Difficulty: Beginner
   - Relevant Chapters: Part 1 (how prediction markets aggregate information)
   - Background on why prediction markets work and when they fail, informing where arbitrage opportunities arise.

### Documentation and Reference Materials

10. **Polymarket API Documentation**
    - URL: https://docs.polymarket.com/api-reference/introduction
    - Official docs for CLOB, Gamma, and Data APIs. Essential reference for building trading tools.

11. **Kalshi API Documentation**
    - URL: https://docs.kalshi.com/welcome
    - Official developer docs with REST/WebSocket endpoints, authentication, and SDKs.

12. **Polymarket Python CLOB Client**
    - URL: https://github.com/Polymarket/py-clob-client
    - Official Python SDK for Polymarket CLOB. Well-documented with examples for order placement and market data retrieval.

13. **LessWrong: "Arbitrage of Prediction Markets"**
    - URL: https://www.lesswrong.com/posts/4Rrkdz9eRL5HtH6cc/arbitrage-of-prediction-markets
    - Theoretical treatment of prediction market arbitrage with mathematical rigor.

### Interactive Exercises and Practice

14. **Kalshi Demo Environment**
    - URL: https://demo.kalshi.com (accessible via Kalshi developer portal)
    - Paper trading environment to test API integrations and strategies without real money.

15. **Polymarket (small position practice)**
    - URL: https://polymarket.com
    - Start with $10-50 to practice live execution, understand slippage, and observe order book dynamics firsthand.

### GitHub Repositories

16. **polymarket-kalshi-btc-arbitrage-bot**
    - URL: https://github.com/CarlosIbCu/polymarket-kalshi-btc-arbitrage-bot
    - Rust-based bot targeting BTC price markets across Polymarket and Kalshi. Study the architecture for cross-platform execution.

17. **OctoBot-Prediction-Market**
    - URL: https://github.com/Drakkar-Software/OctoBot-Prediction-Market
    - Open-source Polymarket trading bot. Supports copy trading and arbitrage strategies.

18. **prediction-market-arbitrage-bot (realfishsam)**
    - URL: https://github.com/realfishsam/prediction-market-arbitrage-bot
    - Cross-platform arbitrage detection and execution tool.

19. **Awesome-Prediction-Market-Tools**
    - URL: https://github.com/aarora4/Awesome-Prediction-Market-Tools
    - Curated list of analytics, APIs, dashboards, bots, and utilities for prediction markets.

20. **ArbiDex**
    - URL: https://github.com/dulvinsipsara/ArbiDex
    - Dashboard for detecting mismatches in Manifold markets using fuzzy logic. Good reference for building monitoring tools.

### Community Resources

21. **r/algotrading** - Reddit
    - URL: https://www.reddit.com/r/algotrading/
    - Active community discussing automated prediction market trading, arbitrage strategies, and bot development.

22. **r/arbitragebetting** - Reddit
    - URL: https://www.reddit.com/r/arbitragebetting/
    - Focused on arbitrage across betting and prediction platforms. Practical tips and opportunity sharing.

23. **Kalshi Discord**
    - URL: Available via https://docs.kalshi.com (developer section)
    - Official developer community for API support and strategy discussion.

24. **Polymarket Discord**
    - URL: Available via https://discord.gg/polymarket
    - Community discussions on market analysis, trading strategies, and platform updates.

### Research Papers

25. **"Arbitrage in Prediction Markets"** - IMDEA Networks
    - URL: https://dspace.networks.imdea.org/bitstream/handle/20.500.12761/1941/AFT_Polymarket_Arbitrage_Arxiv.pdf
    - Academic study documenting $40M+ in arbitrage profits on Polymarket. Covers both market rebalancing and combinatorial arbitrage.

26. **"Combinatorial Arbitrage in Prediction Markets"** - Navnoor Bawa
    - URL: https://navnoorbawa.substack.com/p/combinatorial-arbitrage-in-prediction
    - Deep dive into correlated market arbitrage, LLM-assisted dependency detection, and practical execution challenges.

---

## C) Learning Path

### Phase 1: Foundations (Week 1-2, ~15 hours)

**Concepts:** Price divergence identification, implied probability comparison, Dutch book theory, fee structures
**Activities:**
- Read LessWrong arbitrage article and Trevor Lasn walkthrough
- Study Dutch book detection formula and stake calculation
- Compare fee structures across Polymarket, Kalshi, Robinhood
- Manual exercise: Find 5 events listed on multiple platforms, calculate implied probabilities and fee-adjusted spreads

**Milestone:** Can manually identify whether a cross-platform opportunity is profitable after fees.

### Phase 2: API Integration (Week 3-4, ~20 hours)

**Concepts:** Platform APIs, order types, WebSocket feeds, authentication
**Activities:**
- Set up Polymarket Python SDK (py-clob-client) and connect to market data
- Set up Kalshi API access and test with demo environment
- Build a simple script that pulls prices for the same event from both platforms
- Implement FOK order logic

**Milestone:** Working code that fetches real-time prices from both Polymarket and Kalshi for matched events.

### Phase 3: Monitoring and Detection (Week 5-6, ~20 hours)

**Concepts:** Event matching, alert thresholds, real-time scanning, break-even calculations
**Activities:**
- Build or extend an event matching system across platforms
- Implement fee-adjusted profit calculator
- Set up WebSocket-based monitoring with configurable alert thresholds
- Study existing open-source tools (Eventarb, Polytrage, ArbiDex) for architectural patterns

**Milestone:** Monitoring tool that alerts when profitable cross-platform opportunities appear.

### Phase 4: Execution and Risk (Week 7-8, ~15 hours)

**Concepts:** Leg risk, slippage modeling, resolution criteria verification, settlement timing
**Activities:**
- Execute small cross-platform trades ($5-20 per position) to understand real execution dynamics
- Document resolution criteria differences for at least 5 matched events
- Build slippage estimation from order book depth data
- Implement basic risk controls (max position size, daily loss limit)

**Milestone:** Successfully executed 3+ cross-platform arbitrage trades with documented P&L and risk assessment.

### Phase 5: Advanced Strategies (Week 9-10, ~15 hours)

**Concepts:** Combinatorial arbitrage, correlated markets, conditional probability constraints, regulatory awareness
**Activities:**
- Read IMDEA research paper on Polymarket arbitrage
- Study combinatorial arbitrage with conditional probability analysis
- Review current CFTC regulatory framework and state law developments
- Analyze tax implications of cross-platform trading

**Milestone:** Can identify correlated market mispricings and articulate regulatory constraints affecting strategy execution.

---

## D) Practical Exercises

### Exercise 1: Manual Arbitrage Scanner (Beginner)
**Task:** Create a spreadsheet tracking 10 events across Polymarket and Kalshi. For each, record YES/NO prices on both platforms, calculate implied probabilities, fee-adjusted costs, and net profit/loss for a hypothetical $100 position.
**Goal:** Internalize fee-adjusted profitability calculations.

### Exercise 2: Dutch Book Detector (Beginner-Intermediate)
**Task:** Write a Python script that takes a list of outcome prices for a multi-outcome market and determines whether a Dutch book exists. Calculate optimal stake allocation for a $500 budget.
**Goal:** Automate Dutch book detection math.

### Exercise 3: API Price Fetcher (Intermediate)
**Task:** Build a Python application that connects to both Polymarket (via py-clob-client) and Kalshi APIs. Fetch real-time prices for at least 3 matched events. Output a table showing platform, event, YES price, NO price, and cross-platform spread.
**Goal:** Working familiarity with both platform APIs.

### Exercise 4: Real-Time Arbitrage Monitor (Intermediate-Advanced)
**Task:** Extend Exercise 3 with WebSocket connections for real-time price updates. Implement an event matching algorithm (start with exact string match on event titles, then add fuzzy matching). Alert when fee-adjusted spread exceeds $0.02.
**Goal:** Functional monitoring tool for live arbitrage detection.

### Exercise 5: Simulated Cross-Platform Execution (Advanced)
**Task:** Using Kalshi's demo environment and small real positions on Polymarket ($5-10), execute 3 cross-platform arbitrage trades. For each trade, document:
- Entry prices and timestamps on both platforms
- Fees paid on each leg
- Fill quality (slippage from quoted price)
- Resolution criteria comparison
- Settlement timing
- Actual P&L vs. expected P&L
**Goal:** Experience real execution friction and document practical challenges.

### Exercise 6: Correlated Market Analyzer (Advanced)
**Task:** Identify 5 pairs of logically related markets on Polymarket (e.g., "X wins primary" and "X wins general election"). Verify conditional probability constraints. Flag any violations and calculate the theoretical arbitrage position.
**Goal:** Apply combinatorial arbitrage concepts to real markets.

### Exercise 7: Full Arbitrage Bot (Expert)
**Task:** Build an end-to-end arbitrage bot that: (1) monitors prices via WebSocket, (2) detects opportunities above configurable threshold, (3) executes FOK orders on both platforms, (4) logs all trades with timestamps, fill prices, and fees, (5) implements circuit breakers for API failures and abnormal price movements.
**Goal:** Production-ready (paper trading) arbitrage system.

---

## Applicability to Overall Mastery Goal

This domain is the bridge between theoretical pricing knowledge (domains 1-8) and the automated systems that comprise advanced prediction market trading (domains 10-15). Mastering cross-platform arbitrage develops:

- **Practical API fluency** needed for algorithmic trading (Domain 13)
- **Risk assessment skills** that inform market making (Domain 11)
- **Execution infrastructure** reusable across all automated strategies
- **Regulatory awareness** critical for sustainable operation
- **Fee and slippage modeling** applicable to every trading strategy

The monitoring tools and execution frameworks built here become the foundation for more complex strategies: market making requires similar real-time infrastructure, portfolio construction needs cross-platform position tracking, and algorithmic systems extend the automated execution patterns developed in arbitrage.
