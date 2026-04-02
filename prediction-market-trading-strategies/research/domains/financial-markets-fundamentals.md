# Financial Markets Fundamentals

> Domain 3 of 15 in the Prediction Market Trading Strategies mastery roadmap.
> Level: BEGINNER
> Prerequisites: None (parallel with Probability & Bayesian Reasoning and Prediction Market Mechanics)
> Feeds into: Pricing Theory for Binary & Multi-Outcome Contracts, Risk Management & Bankroll Strategy

---

## A) Key Concepts

### 1. Bid-Ask Spread
The difference between the highest price a buyer will pay (bid) and the lowest price a seller will accept (ask). In prediction markets, this spread is a direct transaction cost. Every time you cross the spread (buying at the ask or selling at the bid), you start at an immediate loss equal to the spread width.

**P&L Impact:** If you buy a Kalshi contract at 62¢ (ask) and the bid is 58¢, you are instantly 4¢ underwater per contract. The event probability must move in your favor by at least that 4¢ before you break even, not counting fees.

**Relationship to other concepts:** Spread width is driven by liquidity, volatility, and market maker behavior. Understanding spreads is prerequisite to calculating break-even prices and evaluating execution quality.

### 2. Order Types
Instructions sent to an exchange specifying how and when to execute a trade.

- **Market Order:** Executes immediately at the best available price. Guarantees fill, not price. Use when speed matters more than price (fast-moving events, high-liquidity markets).
- **Limit Order:** Sets a maximum buy price or minimum sell price. Guarantees price, not fill. Use when you have a target entry/exit and can wait. Critical in prediction markets where spreads can be wide.
- **Stop Order (Stop-Loss):** Triggers a market order when price hits a threshold. Used to cap losses on existing positions.
- **Stop-Limit Order:** Triggers a limit order (not market) at the stop price. More price control but risk of non-execution in fast markets.

**Prediction market relevance:** Most prediction market platforms (Kalshi, Polymarket) support limit orders. Placing limit orders (acting as a "maker") often incurs lower fees than crossing the spread (acting as a "taker").

### 3. Maker vs. Taker Dynamics
- **Maker:** Places a limit order that adds liquidity to the order book (rests on the book until matched). Lower fees on most platforms.
- **Taker:** Places an order that immediately matches against existing resting orders, removing liquidity. Higher fees.

**Prediction market specifics:** Kalshi charges taker fees of ~7% of expected value vs. ~1.75% for maker orders. Polymarket US charges 0.30% taker fee with 0.20% maker rebate.

### 4. Liquidity
The ease with which an asset can be bought or sold without significantly affecting its price. Measured by:
- **Depth:** Total volume of orders at various price levels in the order book.
- **Breadth:** How many price levels have meaningful order volume.
- **Resilience:** How quickly the order book replenishes after a large trade.

**Prediction market relevance:** Many prediction market contracts are thinly traded. Low liquidity means wider spreads, higher slippage, and difficulty entering or exiting large positions. Always check order book depth before sizing a trade.

### 5. Slippage
The difference between the expected execution price and the actual fill price. Occurs when:
- Market moves between order placement and execution
- Order size exceeds available liquidity at the best price
- Multiple price levels in the order book are consumed

**Types:** Positive slippage (better price than expected), negative slippage (worse price), zero slippage.

**Mitigation:** Use limit orders, trade during high-activity periods, reduce position size relative to available liquidity.

### 6. Transaction Costs & Fee Structures
All costs associated with executing a trade:
- **Platform trading fees** (Kalshi formula: `round_up(0.07 * C * P * (1-P))` for takers)
- **Deposit/withdrawal fees** (Kalshi: 2% debit card; Polymarket: gas fees for on-chain)
- **Spread cost** (implicit cost of crossing the bid-ask)
- **Slippage cost** (price impact of your order)

### 7. Break-Even Price Calculation
The price at which total gains equal total costs (purchase price + all fees + spread costs).

**Formula for prediction market contracts held to settlement:**
```
Total Cost = (Contracts * Entry Price) + Entry Fees + Exit Fees
Break-Even Probability = Total Cost / (Contracts * $1.00)
```

**Example:** Buy 100 Yes contracts at 60¢ on Kalshi.
- Entry cost: $60.00
- Taker fee: round_up(0.07 * 100 * 0.60 * 0.40) = $1.68
- Total cost: $61.68
- Break-even if held to Yes resolution: 61.68% implied probability
- If selling before resolution, add exit fees + spread cost

### 8. Time Value of Money
A dollar today is worth more than a dollar in the future due to opportunity cost. Relevant to prediction markets because:
- Capital locked in a position cannot earn returns elsewhere
- Long-dated contracts (months away) tie up capital even if your probability estimate is correct
- The "carry cost" of holding a position should factor into expected value calculations

### 9. Margin and Leverage
- **Margin:** Collateral deposited to cover potential losses on a position.
- **Leverage:** Using borrowed capital or structured products to amplify exposure.

**Prediction market context:** Binary contracts are inherently leveraged: buying a 10¢ contract gives 10:1 payout if it resolves Yes. Most prediction market platforms do not offer traditional margin accounts, but the binary contract structure itself provides leverage. Understanding leverage helps assess risk/reward on low-probability contracts.

### 10. Basic Options Concepts (as analogies to prediction contracts)
Prediction market contracts share structural similarities with options:
- **Premium:** The price paid for a contract (analogous to options premium)
- **Strike/threshold:** The event condition that determines payout
- **Expiration:** When the contract resolves
- **Intrinsic value:** The portion of price reflecting current probability
- **Extrinsic/time value:** The portion reflecting uncertainty and time remaining
- **Binary payout:** Prediction contracts pay $1 or $0, similar to binary/digital options

### 11. Market Microstructure
The study of how markets operate at the mechanical level:
- **Price discovery:** How prices form from the interaction of orders
- **Order book dynamics:** How limit orders, cancellations, and fills shape the visible market
- **Information asymmetry:** Some traders have better information; market makers widen spreads to compensate for adverse selection risk
- **Market maker role:** Entities that provide continuous bid and ask quotes, earning the spread as compensation for inventory and adverse selection risk

### 12. Volatility
The degree of price variation over time.
- **Historical volatility:** Measured from past price movements
- **Implied volatility:** Derived from current market prices (in options markets)
- **Impact on spreads:** Higher volatility leads to wider spreads as market makers demand more compensation for risk
- **Impact on prediction markets:** Event-driven volatility spikes (news, polls) can rapidly change contract prices and liquidity conditions

### 13. Order Book and Price Levels
The order book is a real-time list of all open buy and sell orders at various prices:
- **Best bid/best ask:** The tightest prices, defining the current spread
- **Depth at each level:** Number of contracts available at each price
- **Reading the book:** Thick levels indicate strong support/resistance; thin books signal potential slippage

### Concept Relationship Map
```
Order Types --> Maker/Taker --> Fee Structures --> Break-Even Calculation
                    |                                      |
                    v                                      v
              Order Book --> Liquidity --> Slippage --> Total Trading Costs
                    |
                    v
           Market Microstructure --> Price Discovery --> Volatility
                    |
                    v
         Information Asymmetry --> Spread Dynamics
                    
Time Value of Money --> Capital Allocation --> Leverage/Margin
                    
Options Concepts --> Binary Contract Analogy --> Prediction Market Pricing
```

### Cross-Domain Prerequisites
- **Bid-ask spreads, fees, break-even** → directly feed Pricing Theory for Binary & Multi-Outcome Contracts
- **Liquidity, slippage, order types** → essential for Risk Management & Bankroll Strategy
- **Market microstructure, maker/taker** → foundation for Market Making & Liquidity Provision (advanced)
- **Leverage concepts** → support Portfolio Construction & Correlation Management

---

## B) Learning Resources

### Online Courses

1. **Coursera - Financial Markets (Yale, Robert Shiller)**
   - URL: https://www.coursera.org/learn/financial-markets-global
   - Platform: Coursera (free to audit)
   - Duration: ~33 hours
   - Covers: Market mechanics, risk, behavioral finance, market institutions
   - Relevance: Broad foundation; excellent for understanding why markets exist and how they function

2. **Coursera - Market Microstructure**
   - URL: https://www.coursera.org/learn/market-microstructure
   - Platform: Coursera
   - Duration: ~12 hours
   - Covers: Price formation, liquidity, trading costs, algorithmic trading impact
   - Relevance: Directly covers order book dynamics, spreads, and market structure

3. **Khan Academy - Finance and Capital Markets**
   - URL: https://www.khanacademy.org/economics-finance-domain/core-finance
   - Platform: Khan Academy (free)
   - Duration: Self-paced (~15-20 hours for relevant sections)
   - Covers: Stocks, bonds, interest, options basics, money and banking
   - Relevance: Solid beginner-friendly foundation for time value, basic instruments

4. **Investopedia Academy - Become a Day Trader**
   - URL: https://academy.investopedia.com/products/become-a-day-trader
   - Platform: Investopedia (paid)
   - Duration: ~6 hours
   - Covers: Order types, chart reading, risk management, execution
   - Relevance: Practical order type usage and execution concepts

5. **Option Alpha - Options Trading for Beginners**
   - URL: https://optionalpha.com/learn/options-trading-for-beginners
   - Platform: Option Alpha (free)
   - Duration: Self-paced
   - Covers: Options basics, premium, time decay, leverage
   - Relevance: Understanding binary contract analogy through options lens

### Video Tutorials & Lectures

6. **MIT OpenCourseWare - Finance Theory I (Andrew Lo)**
   - URL: https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/
   - Platform: MIT OCW / YouTube
   - Duration: Full semester (~40 hours of lectures)
   - Covers: Time value of money, risk/return, market efficiency, options
   - Relevance: Rigorous academic treatment of core financial concepts

7. **Schwab - 3 Order Types: Market, Limit, and Stop Orders**
   - URL: https://www.schwab.com/learn/story/3-order-types-market-limit-and-stop-orders
   - Platform: Schwab Learning Center
   - Relevance: Clear, practical explainer of the three primary order types

8. **tastylive - Market Measures & Options Concepts**
   - URL: https://www.tastylive.com/shows/market-measures
   - Platform: tastylive (free streaming)
   - Covers: Options mechanics, probability of profit, time decay
   - Relevance: Data-driven approach to options concepts applicable to binary contracts

### Books

9. **"Trading and Exchanges: Market Microstructure for Practitioners" by Larry Harris**
   - Relevant chapters: Ch 1-6 (market structure, order types, spreads), Ch 13-15 (liquidity, volatility)
   - Difficulty: Intermediate
   - Why: The definitive practitioner text on market microstructure. Explains why spreads exist, how order matching works, and how different participants interact.

10. **"Market Microstructure in Practice" by Charles-Albert Lehalle and Sophie Laruelle**
    - Relevant chapters: Ch 1-3 (market design, electronic trading, order book)
    - Difficulty: Intermediate-Advanced
    - Why: Modern treatment covering electronic markets, HFT impact, and post-regulation landscape

11. **"Options, Futures, and Other Derivatives" by John C. Hull**
    - Relevant chapters: Ch 1-3 (intro, mechanics of futures/options), Ch 10-11 (trading strategies, binomial models)
    - Difficulty: Intermediate
    - Why: Gold standard for understanding options pricing concepts that map to prediction contract mechanics

12. **"The Intelligent Investor" by Benjamin Graham**
    - Relevant chapters: Ch 8 (market fluctuations), Ch 20 (margin of safety)
    - Difficulty: Beginner
    - Why: Foundational thinking about market behavior, margin of safety concept applicable to prediction market edge

### Documentation & Reference Materials

13. **Investopedia - Trading Skills Section**
    - URL: https://www.investopedia.com/trading-skills-and-essentials-4689654
    - Covers: Order types, spreads, slippage, margin, leverage explainers
    - Relevance: Encyclopedic reference for every concept in this domain

14. **SEC Investor.gov - Types of Orders**
    - URL: https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders
    - Relevance: Official regulatory explanation of order types

15. **Kalshi Fee Schedule**
    - URL: https://kalshi.com/docs/kalshi-fee-schedule.pdf
    - Relevance: Essential for calculating actual trading costs and break-even on Kalshi

16. **Polymarket Trading Fees Documentation**
    - URL: https://docs.polymarket.com/trading/fees
    - Relevance: Fee structure for Polymarket, including maker/taker dynamics

### Interactive Exercises & Practice

17. **Investopedia Stock Simulator**
    - URL: https://www.investopedia.com/simulator/
    - Type: Paper trading with $100k virtual cash
    - Covers: Market orders, limit orders, stop orders, options
    - Relevance: Practice placing different order types and observing execution behavior

18. **CME Group Market Simulator**
    - URL: https://www.cmegroup.com/trading/trading-simulator.html
    - Type: Futures/options paper trading
    - Relevance: Practice with derivatives that share structural similarities to prediction contracts

19. **Kalshi Paper Trading (Demo Mode)**
    - URL: https://kalshi.com (sign up for demo)
    - Type: Practice prediction market trading
    - Relevance: Direct experience with prediction market order books, spreads, and fee impacts

### Community Resources

20. **r/Trading** - https://www.reddit.com/r/Trading/
    - General trading discussion, order execution, platform comparison

21. **r/predictit and r/Kalshi** - https://www.reddit.com/r/Kalshi/
    - Prediction market specific trading discussions

22. **Quant StackExchange** - https://quant.stackexchange.com/
    - Technical Q&A on market microstructure, execution, and quantitative trading

23. **Elite Trader Forums** - https://www.elitetrader.com/et/
    - Active community discussing order types, execution quality, and trading mechanics

### GitHub Repositories

24. **orderbook (Python)** - https://github.com/dyn4mik3/OrderBook
    - Simple order book implementation to understand matching engines

25. **Lobster Data** - https://lobsterdata.com/
    - High-frequency limit order book data for academic study of microstructure

---

## C) Learning Path Within This Domain

### Phase 1: Core Market Mechanics (Week 1, ~8-10 hours)
**Concepts:** Order types, bid-ask spread, order book basics

1. Read Investopedia articles on market orders, limit orders, stop orders
2. Watch Schwab order types explainer
3. Complete Khan Academy: Stocks and Bonds module
4. Practice on Investopedia Simulator: place 20+ trades using different order types
5. **Milestone:** Can explain when to use each order type and predict which will fill faster

### Phase 2: Liquidity, Slippage & Spreads (Week 2, ~8-10 hours)
**Concepts:** Liquidity measurement, slippage causes/mitigation, spread dynamics, maker/taker

1. Start Coursera Market Microstructure course (first 3 modules)
2. Read Harris "Trading and Exchanges" chapters 1-6
3. Study Kalshi and Polymarket order books in real-time (observe spread patterns)
4. **Milestone:** Can identify liquid vs. illiquid prediction markets by examining the order book; can estimate slippage for a given order size

### Phase 3: Costs, Fees & Break-Even (Week 3, ~6-8 hours)
**Concepts:** Fee structures, break-even calculation, total cost of trading

1. Study Kalshi fee schedule and Polymarket fee documentation
2. Build a spreadsheet: calculate break-even probabilities for contracts at various prices and sizes on both platforms
3. Compare total costs: maker vs. taker, different contract prices, different position sizes
4. **Milestone:** Can calculate the exact break-even probability for any given trade on Kalshi or Polymarket, including all fees

### Phase 4: Time Value, Options Analogies & Leverage (Week 4, ~6-8 hours)
**Concepts:** Time value of money, options basics (premium, intrinsic/extrinsic value, time decay), leverage in binary contracts, margin

1. MIT OCW Finance Theory I: lectures on time value and options basics
2. Option Alpha beginner course (first 3 modules)
3. Read Hull chapters 1-3 on derivatives mechanics
4. Map options concepts to prediction market contracts (binary options analogy)
5. **Milestone:** Can explain why a 60¢ prediction contract 6 months out is priced differently than one expiring tomorrow, even if both reflect the same underlying probability estimate

### Phase 5: Market Microstructure Deep Dive (Week 5, ~6-8 hours)
**Concepts:** Price discovery, information asymmetry, market maker role, volatility impact on spreads

1. Complete Coursera Market Microstructure course
2. Read Harris chapters 13-15 on liquidity and price discovery
3. Analyze 3-5 prediction market events: track how spreads, depth, and prices change around news events
4. **Milestone:** Can describe the market maker's role, explain why spreads widen before major events, and identify adverse selection risk in prediction markets

### Total Estimated Time: 34-44 hours over 5 weeks

---

## D) Practical Exercises

### Beginner Exercises

**Exercise 1: Order Type Drill**
Open the Investopedia Simulator. For one week, only use market orders on Monday, only limit orders on Tuesday-Wednesday, and stop orders on Thursday-Friday. Log every trade: expected price, actual fill price, slippage experienced. Write a 1-page summary comparing execution quality across order types.

**Exercise 2: Spread Tracking Journal**
Pick 5 prediction market contracts on Kalshi (varying liquidity). Record bid, ask, spread, and depth at the same time each day for one week. Categorize each as tight (<3¢), medium (3-8¢), or wide (>8¢). Note what market events correlate with spread changes.

**Exercise 3: Break-Even Calculator**
Build a spreadsheet that takes inputs: platform (Kalshi/Polymarket), number of contracts, entry price, maker or taker. Output: total fees, total cost, break-even probability, required price move to profit $X. Test with 10 different scenarios.

### Intermediate Exercises

**Exercise 4: Liquidity Impact Analysis**
For a given prediction market event, simulate what would happen if you tried to buy 10, 50, 100, and 500 contracts. Using the visible order book, calculate the average fill price and total slippage for each size. Chart the relationship between order size and execution cost.

**Exercise 5: Cost Comparison Matrix**
Compare the total cost of the same trade across multiple platforms (Kalshi, Polymarket, Robinhood event contracts). Include: spread cost, trading fees, deposit/withdrawal fees, and any other costs. Determine which platform is cheapest for different trade sizes and probabilities.

**Exercise 6: Time Value Exercise**
Find two prediction market contracts for the same underlying event but with different resolution dates (e.g., "Will X happen by June?" vs. "Will X happen by December?"). Compare prices. Calculate the implied time premium. Determine if the longer-dated contract offers better or worse expected value considering opportunity cost.

### Advanced Exercises

**Exercise 7: Market Microstructure Case Study**
Choose a major prediction market event (e.g., election, Fed decision). Collect order book snapshots every hour for 48 hours around the event. Document: how spreads changed, when depth increased/decreased, price discovery patterns, and any evidence of informed trading (large orders moving the market ahead of news).

**Exercise 8: Trading Cost Optimizer**
Design and back-test a rule-based system for order placement: use maker orders when spread > X, market orders when spread < Y, and never trade when depth < Z. Apply these rules to historical prediction market data and calculate the total fee savings vs. always using market orders.

**Exercise 9: Binary Options vs. Prediction Contracts**
Compare a binary options contract from a traditional broker with an equivalent prediction market contract. Map: premium structure, payout, fees, time decay, and implied probability. Write up the similarities and differences, noting where traditional options theory applies and where it breaks down for prediction markets.

### Real-World Application Projects

**Project A: Personal Trading Cost Audit**
Review your last 20 prediction market trades. For each, calculate: spread cost at entry, fees paid, slippage (if any), total transaction cost as percentage of position. Identify your costliest trades and determine what you could have done differently.

**Project B: Optimal Position Sizing Model**
Given a fixed bankroll, build a model that determines optimal position size considering: available liquidity (from order book depth), expected slippage curve, fee structure, and target profit. The model should output the position size where marginal cost of the next contract exceeds marginal expected value.

---

## Applicability to Prediction Market Trading Strategies

This domain provides the mechanical foundation for everything that follows in the roadmap. Without understanding how orders execute, what they cost, and how liquidity shapes your P&L, even the best probability estimates and forecasting models will underperform due to execution drag.

Key connections:
- **Pricing Theory** requires understanding of spreads and fees to assess whether a contract is truly mispriced
- **Risk Management** depends on knowing your actual execution costs and slippage exposure
- **Arbitrage strategies** are only viable when cross-platform cost differentials exceed total transaction costs
- **Market Making** is built entirely on bid-ask spread management and inventory risk concepts from this domain
- **Algorithmic Trading** requires programmatic understanding of order types, order book depth, and execution optimization
