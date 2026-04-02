# Market Making & Liquidity Provision

> **Level:** Advanced
> **Prerequisites:** Pricing Theory for Binary Contracts, Risk Management & Bankroll Strategy, Arbitrage & Cross-Platform Strategies
> **Feeds into:** Algorithmic & Automated Trading Systems

---

## A) Key Concepts

### 1. Market Making Fundamentals

**Bid-Ask Spread**
The difference between the price a market maker will buy (bid) and sell (ask). This spread is the primary revenue source. In prediction markets, a maker might bid $0.48 on YES and offer $0.52, earning $0.04 per round-trip. Spread width balances profit potential against fill probability.

**Market Maker Edge**
The statistical expectation that spread capture exceeds losses from adverse selection and inventory depreciation. Edge = (spread revenue) - (adverse selection cost) - (inventory holding cost) - (operational costs). Positive edge requires disciplined quoting and risk controls.

**Liquidity Provision**
The act of placing resting orders on both sides of an order book, enabling other participants to trade without waiting for a counterparty. Deeper liquidity reduces slippage and attracts more volume, creating a positive feedback loop.

**Maker vs. Taker**
Makers add liquidity (resting limit orders); takers remove it (market orders or crossing limit orders). Most prediction platforms reward makers with reduced or zero fees (Kalshi charges zero maker fees) and sometimes explicit liquidity incentive payments.

### 2. Spread Setting & Pricing

**Reservation Price (Indifference Price)**
A market maker's personal fair value adjusted for current inventory. If holding excess long inventory, the reservation price drops below mid-market to encourage selling. Derived from the Avellaneda-Stoikov framework: `r = s - q * γ * σ² * (T - t)` where s = mid-price, q = inventory, γ = risk aversion, σ = volatility, T-t = time remaining.

**Optimal Spread Width**
Determined by volatility, order arrival intensity, risk aversion, and time to settlement. Higher volatility or lower order flow warrants wider spreads. The Avellaneda-Stoikov model provides: `δ = γσ²(T-t) + (2/γ) * ln(1 + γ/κ)` where κ = order arrival intensity.

**Dynamic Spread Adjustment**
Real-time spread modification based on changing conditions. Widen around news events, narrow during stable periods, tighten when inventory is balanced, widen when concentrated.

**Quote Skewing**
Asymmetrically adjusting bid and ask prices to manage inventory. If long, lower the ask (more aggressive selling) and raise the bid (less aggressive buying). This encourages the market to trade you back toward neutral.

### 3. Inventory Risk Management

**Inventory Risk**
The exposure to loss from holding a directional position. In prediction markets, this risk is amplified because contracts settle at $0 or $1. Holding the wrong side means total loss on that position, not just a percentage drawdown.

**Position Limits**
Hard caps on maximum inventory in any single contract or correlated set of contracts. Prevents catastrophic losses from single-event outcomes.

**Inventory Half-Life**
A target time to reduce inventory by 50%. Aggressive skewing and spread adjustment achieve this. As settlement approaches, the half-life should shrink, moving to flat positions before resolution.

**Delta-Neutral Market Making**
Hedging directional exposure by taking offsetting positions in correlated contracts, related markets, or complementary outcomes (e.g., hedging YES with the corresponding NO position or via a correlated contract on another platform).

**Settlement Risk Approaching Expiry**
As event resolution nears, binary outcomes become more certain. Contract prices approach $0 or $1, making inventory on the losing side worthless. Market makers must aggressively unwind positions well before settlement, widening spreads or pulling quotes entirely near expiry.

### 4. Adverse Selection

**Informed vs. Uninformed Flow**
Adverse selection occurs when market makers trade against counterparties with superior information. Informed traders buy YES just before positive news breaks, leaving the maker holding losing inventory.

**Toxicity Metrics**
Measuring order flow toxicity to detect informed trading. Metrics include VPIN (Volume-Synchronized Probability of Informed Trading), trade size distribution analysis, and comparing fill rates on bid vs. ask sides.

**Event-Driven Information Asymmetry**
Prediction markets have concentrated information events (election results, economic data releases, court rulings). Information asymmetry spikes around these events. Market makers should widen spreads or withdraw liquidity during high-asymmetry periods.

**Speed Advantage and Stale Quotes**
Faster participants pick off stale quotes when news breaks. Market makers need mechanisms to quickly update or cancel orders when material information arrives.

### 5. Automated Market Maker (AMM) Models

**Logarithmic Market Scoring Rule (LMSR)**
Robin Hanson's cost-function-based AMM for prediction markets. The cost function C = b * ln(Σ e^(q_i/b)) determines prices as partial derivatives. The parameter b controls liquidity depth: larger b = more liquidity but higher worst-case loss for the operator. Prices always sum to 1 across all outcomes, maintaining coherent probabilities.

**Constant Product Market Maker (CPMM)**
The x*y=k formula used by Uniswap and similar DEXs. Not ideal for prediction markets because it doesn't enforce the constraint that outcome tokens must sum to $1, leading to impermanent loss issues.

**Portfolio Management AMM (pm-AMM)**
Paradigm's research design tailored for prediction markets. Addresses the unique dynamics of binary outcome tokens approaching settlement, managing the liquidity provider's risk profile as events resolve.

**Impermanent Loss in Prediction Markets**
When LPs deposit into AMM pools for prediction markets, price divergence as outcomes become clearer creates losses compared to simply holding. As a contract approaches resolution (price moving toward $0 or $1), impermanent loss can become extreme and permanent. This is why many prediction platforms (Polymarket, Kalshi) have moved to order-book models.

### 6. Order Book vs. AMM Architecture

**Central Limit Order Book (CLOB)**
Used by Polymarket (after transitioning from AMM) and Kalshi. Traders place limit orders at specific prices. More capital-efficient and allows professional market-making strategies.

**Polymarket's Unified Order Book**
YES and NO orders are mirrored: a buy-YES at $0.60 automatically creates a sell-NO at $0.40, maintaining the $1.00 constraint. Liquidity rewards incentivize tight quotes near the midpoint.

**Kalshi's Order Book**
Traditional CLOB with maker fee exemption and a Liquidity Incentive Program. Resting orders scored every second based on size and proximity to best bid/ask. Dedicated Market Maker Program for institutional participants.

### 7. Market Making P&L Analysis

**Expected P&L from Spread Capture**
Revenue = (half-spread) * (number of round-trips). If quoting $0.48/$0.52, half-spread = $0.02. With 100 round-trips/day = $2.00/day per contract type.

**Adverse Selection Cost**
Loss from informed flow = (probability of informed trade) * (expected price move) * (trade size). If 20% of flow is informed and moves price by $0.05 on average: cost = 0.20 * 0.05 * volume.

**Net P&L Formula**
Net = Spread Revenue - Adverse Selection Cost - Inventory Holding Cost - Fees + Liquidity Rewards

**Sharpe Ratio for Market Making**
Daily P&L Sharpe = mean(daily P&L) / std(daily P&L). Good MM strategies target Sharpe > 2.0 before accounting for catastrophic settlement risk.

### 8. Platform-Specific Market Making

**Kalshi Market Making**
- Zero maker fees, liquidity incentive program
- API with Python SDK and WebSocket streaming
- Demo/paper trading environment for testing
- Market Maker Program with enhanced limits and access
- Event contracts on weather, economics, politics

**Polymarket Market Making**
- CLOB with unified YES/NO order book
- Daily liquidity rewards for competitive quotes
- REST API and SDK for programmatic access
- Crypto-native (USDC settlement on Polygon)
- Higher volume markets attract more competition

### Concept Relationships

```
Spread Setting ──────► Inventory Management
     │                        │
     ▼                        ▼
Adverse Selection ◄──── Quote Skewing
     │                        │
     ▼                        ▼
Dynamic Spreads ─────► Settlement Risk
     │
     ▼
LMSR / AMM Models ──► Order Book Architecture
                              │
                              ▼
                    Platform-Specific MM
                              │
                              ▼
                    P&L Analysis & Optimization
```

### Prerequisites for Other Domains
- **Algorithmic Systems:** Market making strategies provide the core logic that algorithmic systems automate at scale
- **Strategy Integration:** MM P&L analysis feeds into overall performance measurement

---

## B) Learning Resources

### Online Courses

1. **"Financial Markets Microstructure" - Coursera (HEC Paris)**
   - URL: https://www.coursera.org/learn/financial-markets-microstructure
   - Platform: Coursera
   - Duration: ~12 hours
   - Covers order-driven markets, market making, inventory models, information-based trading

2. **"Algorithmic Trading & Quantitative Analysis Using Python" - Udemy**
   - URL: https://www.udemy.com/course/algorithmic-trading-quantitative-analysis-using-python/
   - Platform: Udemy
   - Duration: ~10 hours
   - Includes market-making strategy development and backtesting

3. **"Hummingbot Botcamp" - Hummingbot Foundation**
   - URL: https://hummingbot.org/botcamp/
   - Platform: Hummingbot
   - Duration: Self-paced (4-6 weeks)
   - Hands-on market making bot development with mentorship

### Video Tutorials & Lectures

4. **"Market Microstructure" - MIT OpenCourseWare (Lecture Series)**
   - URL: https://www.youtube.com/results?search_query=MIT+market+microstructure+lecture
   - Topics: Order flow, market making theory, adverse selection models

5. **"Prediction Markets with the Kalshi API (Python Tutorial)"**
   - URL: https://www.youtube.com/watch?v=E2mgWN4ReqQ
   - Covers API setup, data collection, WebSocket streaming for Kalshi

6. **"Hummingbot Pure Market Making Strategy" - Hummingbot YouTube**
   - URL: https://www.youtube.com/watch?v=7eHiMPRBQLQ
   - Practical walkthrough of setting up an automated market making bot

7. **"Understanding Market Makers" - Patrick Boyle (YouTube)**
   - URL: https://www.youtube.com/results?search_query=patrick+boyle+market+makers
   - Accessible explanation of market making economics and mechanics

### Books

8. **"Trading and Exchanges: Market Microstructure for Practitioners" - Larry Harris**
   - Relevant chapters: Parts on dealers, spread determinants, liquidity
   - Difficulty: Intermediate
   - The foundational text on how markets actually work

9. **"Market Microstructure Theory" - Maureen O'Hara**
   - Relevant chapters: Inventory models, information-based models, price dynamics
   - Difficulty: Advanced
   - Academic treatment of the theoretical foundations

10. **"Algorithmic Trading: Winning Strategies and Their Rationale" - Ernest Chan**
    - Relevant chapters: Market making strategies, statistical arbitrage
    - Difficulty: Intermediate-Advanced
    - Practical algorithmic implementation perspective

11. **"Market Microstructure in Practice" - Charles-Albert Lehalle & Sophie Laruelle**
    - Relevant chapters: Electronic market making, optimal execution
    - Difficulty: Advanced
    - Bridges theory and modern electronic trading practice

12. **"Advances in Financial Machine Learning" - Marcos Lopez de Prado**
    - Relevant chapters: Microstructural features, VPIN, order flow toxicity
    - Difficulty: Advanced
    - Cutting-edge quantitative methods for market microstructure

### Documentation & Reference Materials

13. **Kalshi API Documentation**
    - URL: https://docs.kalshi.com/
    - Official API docs with Python SDK examples, WebSocket specs, market data endpoints

14. **Polymarket Documentation - Market Makers**
    - URL: https://docs.polymarket.com/market-makers/overview
    - Overview of Polymarket's CLOB, liquidity rewards, and API access for market makers

15. **Polymarket Order Book Documentation**
    - URL: https://docs.polymarket.com/trading/orderbook
    - Technical details of the unified YES/NO order book architecture

16. **Hummingbot Documentation - Pure Market Making**
    - URL: https://hummingbot.org/strategies/v1-strategies/pure-market-making/
    - Configuration parameters, spread settings, inventory management features

17. **Cultivate Labs - LMSR Guide**
    - URL: https://www.cultivatelabs.com/crowdsourced-forecasting-guide/how-does-logarithmic-market-scoring-rule-lmsr-work
    - Clear walkthrough of LMSR mechanics with examples

18. **Avellaneda-Stoikov Paper (Original)**
    - URL: https://people.orie.cornell.edu/sfs33/LimitOrderBook.pdf
    - The foundational academic paper on optimal market making with inventory risk

### GitHub Repositories & Open Source

19. **Hummingbot - Open Source Market Making Bot**
    - URL: https://github.com/hummingbot/hummingbot
    - Full-featured Python framework for market making across CEX/DEX platforms

20. **nikhilnd/kalshi-market-making**
    - URL: https://github.com/nikhilnd/kalshi-market-making
    - Market making strategy for Kalshi S&P 500 daily close markets, integrates Kalshi API

21. **Apostlex0/PredictionMarket_AMM**
    - URL: https://github.com/Apostlex0/PredictionMarket_AMM
    - AMM implementation for prediction markets, useful for understanding AMM mechanics

22. **Gnosis PM LMSR Documentation**
    - URL: https://gnosis-pm-js.readthedocs.io/en/v1.3.0/lmsr-primer.html
    - Technical primer on implementing LMSR for prediction markets

### Community Resources

23. **r/algotrading** - Reddit
    - URL: https://www.reddit.com/r/algotrading/
    - Active discussions on market making strategies, backtesting, and API integrations

24. **Hummingbot Discord**
    - URL: https://discord.hummingbot.io/
    - Community support for market making bot development

25. **Quant StackExchange - Market Making Tag**
    - URL: https://quant.stackexchange.com/questions/tagged/market-making
    - Technical Q&A on spread models, inventory management, adverse selection

26. **Kalshi Community & Blog**
    - URL: https://news.kalshi.com/
    - Articles on market making, limit orders, and liquidity programs on Kalshi

### Podcasts & Audio

27. **"Chat With Traders" Podcast**
    - URL: https://chatwithtraders.com/
    - Episodes featuring professional market makers and HFT practitioners

28. **"Flirting with Models" - Corey Hoffstein**
    - URL: https://www.thinknewfound.com/podcast
    - Quantitative strategy discussions including market microstructure topics

---

## C) Learning Path Within This Domain

### Phase 1: Market Making Theory (Week 1-2, ~15 hours)

**Concepts:** Bid-ask spread, maker/taker roles, market maker edge, liquidity provision basics

**Activities:**
- Read Harris "Trading and Exchanges" chapters on dealers and spreads
- Watch introductory market making videos (Patrick Boyle)
- Study Kalshi's blog posts on makers/takers and limit orders
- Complete Coursera "Financial Markets Microstructure" first 4 modules

**Milestone:** Can explain why market makers exist, how they profit, and what risks they face

### Phase 2: Spread Setting & Inventory Models (Week 3-4, ~20 hours)

**Concepts:** Reservation price, Avellaneda-Stoikov model, optimal spread width, quote skewing, inventory risk

**Activities:**
- Read the Avellaneda-Stoikov paper
- Study O'Hara's inventory-based models chapter
- Work through spread calculation exercises with real market data
- Implement reservation price calculator in Python

**Milestone:** Can calculate optimal bid/ask quotes given inventory, volatility, and risk parameters

### Phase 3: Adverse Selection & Information (Week 5, ~10 hours)

**Concepts:** Informed vs. uninformed flow, toxicity metrics, event-driven asymmetry, speed risk

**Activities:**
- Read O'Hara's information-based models
- Study VPIN and flow toxicity from Lopez de Prado
- Analyze order flow patterns around major prediction market events
- Build a simple toxicity indicator

**Milestone:** Can identify and measure adverse selection risk in order flow data

### Phase 4: AMM Models & Architecture (Week 6, ~10 hours)

**Concepts:** LMSR, CPMM, impermanent loss, order book vs. AMM tradeoffs, pm-AMM

**Activities:**
- Read the Hanson LMSR paper and Cultivate Labs guide
- Study Gnosis PM LMSR documentation
- Compare Polymarket (CLOB) vs. historical AMM implementation
- Calculate impermanent loss scenarios for prediction market LP positions

**Milestone:** Can explain when AMMs vs. order books are appropriate and calculate LMSR prices

### Phase 5: Platform-Specific Implementation (Week 7-8, ~20 hours)

**Concepts:** Kalshi API, Polymarket API, order management, paper trading, live deployment

**Activities:**
- Set up Kalshi API access and run paper trading
- Build a basic market making bot using Kalshi Python SDK
- Study nikhilnd/kalshi-market-making for strategy patterns
- Install and configure Hummingbot for a test exchange
- Backtest strategy against historical prediction market data

**Milestone:** Have a working market making bot on Kalshi paper trading with P&L tracking

### Phase 6: P&L Analysis & Multi-Day Management (Week 9-10, ~15 hours)

**Concepts:** Net P&L decomposition, Sharpe ratio, settlement risk, multi-day inventory management, liquidity rewards optimization

**Activities:**
- Build P&L attribution model (spread capture vs. adverse selection vs. inventory cost)
- Run bot for 5+ days on paper trading, analyze daily results
- Implement settlement risk rules (position reduction as expiry approaches)
- Optimize for platform liquidity reward programs
- Stress test against historical volatile events

**Milestone:** Can decompose P&L into components, demonstrate positive expected value, and manage multi-day inventory lifecycle

---

## D) Practical Exercises

### Exercise 1: Spread Calculator (Beginner)
Build a Python function that takes mid-price, inventory, volatility, risk aversion parameter, and time to settlement, then outputs optimal bid and ask prices using the Avellaneda-Stoikov reservation price formula. Test with various inventory levels and observe how quotes shift.

### Exercise 2: LMSR Price Simulator (Beginner-Intermediate)
Implement the LMSR cost function for a binary prediction market. Simulate a sequence of trades and plot how prices evolve. Experiment with different liquidity parameter (b) values and calculate the market maker's worst-case loss.

### Exercise 3: Order Flow Analysis (Intermediate)
Download historical trade data from Kalshi or Polymarket. Classify trades as buyer-initiated or seller-initiated. Calculate the proportion of "informed" trades around known news events. Measure how spreads should widen during high-information periods.

### Exercise 4: Paper Trading Market Maker (Intermediate)
Using the Kalshi demo API, build a bot that:
- Maintains two-sided quotes on a selected market
- Adjusts spreads based on inventory level
- Implements position limits
- Logs every quote update and fill
- Calculates running P&L

Run for at least 3 days and analyze results.

### Exercise 5: Adverse Selection Measurement (Intermediate-Advanced)
For your paper trading bot, calculate:
- What percentage of fills were followed by adverse price movement?
- Average adverse move size per fill
- Compare this cost against spread revenue
- Implement a simple flow toxicity filter and measure improvement

### Exercise 6: Multi-Market Inventory Manager (Advanced)
Extend the paper trading bot to quote on 3-5 correlated markets simultaneously. Implement cross-contract inventory management:
- Track aggregate directional exposure
- Implement portfolio-level position limits
- Use correlations between contracts to manage net risk
- Generate a daily risk report

### Exercise 7: Settlement Countdown Strategy (Advanced)
Build logic that adjusts market making behavior as settlement approaches:
- Progressively reduce position limits (e.g., halve every day in final week)
- Widen spreads as time-to-settlement decreases
- Implement a hard cutoff to pull all quotes N hours before resolution
- Backtest against historical settlements to measure effectiveness

### Exercise 8: Full P&L Attribution (Advanced)
After running your bot for 1-2 weeks (paper or small live), decompose total P&L:
- Spread capture revenue
- Adverse selection losses
- Inventory mark-to-market changes
- Fee savings / liquidity rewards earned
- Calculate daily Sharpe ratio
- Identify which markets/times were most profitable

---

## Applicability to Prediction Market Trading

Market making is one of the most consistent profit strategies in prediction markets when executed with discipline. Unlike directional betting (which requires being right about outcomes), market making profits from providing liquidity regardless of which side wins, as long as inventory is managed properly.

Key connections to the overall mastery roadmap:
- **From Pricing Theory:** Fair value estimates form the center of your quotes
- **From Risk Management:** Position sizing and bankroll allocation prevent catastrophic losses
- **From Arbitrage:** Cross-platform price discrepancies create additional MM opportunities
- **To Algorithmic Systems:** MM strategies are the primary use case for prediction market trading bots
- **To Strategy Integration:** MM P&L streams combine with directional and arbitrage returns in portfolio management
