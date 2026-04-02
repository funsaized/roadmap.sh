# Information Sources & Research Methods for Prediction Market Trading

## Overview

Building an information advantage in prediction markets requires knowing where to find reliable data, how to process it systematically, and how to separate meaningful signals from noise. This domain covers data sources by event category, structured research workflows, polling analysis, and techniques for developing a personal edge.

---

## Key Concepts

### 1. Resolution Criteria Analysis
Every prediction market contract has specific resolution criteria that determine the outcome. Misreading these is the most common source of loss for new traders. Before trading, read the exact resolution source (e.g., "BLS CPI-U release" vs. "core CPI"), check for rounding rules, and identify edge cases. Weather markets on Kalshi, for example, settle based on specific NWS station readings with particular rounding conventions.

### 2. Base Rate Estimation (Reference Class Forecasting)
Before diving into specifics, establish how often similar events have occurred historically. If you're trading on whether the Fed will cut rates at the next meeting, look at the historical frequency of rate cuts given similar economic conditions. This "outside view" anchors your estimate and prevents overreaction to recent news.

### 3. Signal vs. Noise in Polling Data
Not all polls are equal. Key distinctions:
- **Pollster quality**: Silver Bulletin (formerly FiveThirtyEight) publishes pollster ratings based on historical accuracy, methodology transparency, and partisan lean
- **Sample size and methodology**: Live-caller polls with large samples (1000+) generally outperform online opt-in panels
- **House effects**: Systematic biases specific to pollsters (e.g., consistently favoring one party by 2-3 points)
- **Aggregation over cherry-picking**: No single poll is reliable; aggregated averages weighted by quality reduce noise substantially
- **Herding**: Late-cycle polls sometimes converge artificially toward the consensus, reducing their independent information value

### 4. Data Source Tiering by Event Category
Organizing sources into tiers (primary/authoritative, secondary/analytical, tertiary/sentiment) helps prioritize research time. Primary sources are the actual data releases; secondary sources interpret them; tertiary sources reflect crowd sentiment.

### 5. Cross-Market Correlation Analysis
Related prediction markets often update at different speeds. If a strong jobs report drops, Fed rate markets may reprice within minutes while related inflation markets lag. Monitoring correlated markets provides early signals and potential arbitrage.

### 6. Fermi Estimation & Problem Decomposition
Borrowed from superforecasting methodology: break complex questions into smaller, estimable components. For "Will the US enter recession in 2026?", decompose into: What's the current GDP trend? What do leading indicators show? What's the base rate for recessions given current conditions? Combine sub-estimates for a more calibrated overall probability.

### 7. Bayesian Updating
Start with a prior probability (your base rate), then incrementally adjust as new evidence arrives. Superforecasters make many small updates rather than dramatic swings. Track your updates explicitly to avoid anchoring bias or overreaction.

### 8. Information Advantage Assessment
Before entering any trade, honestly evaluate: Do I know something the market doesn't? Is my model better? Am I faster? If the answer is "no" to all three, the expected value of trading is negative after fees. Categories where you have domain expertise or faster data access are where to focus.

---

## Data Sources by Event Category

### Politics & Elections

| Tier | Source | URL | What It Provides |
|------|--------|-----|-----------------|
| Primary | Silver Bulletin Polling Averages | https://www.natesilver.net/ | Weighted polling aggregates, pollster ratings, election models |
| Primary | 538 (ABC News) | https://projects.fivethirtyeight.com/polls/ | Polling database, historical averages |
| Primary | RealClearPolitics | https://www.realclearpolitics.com/epolls/latest_polls/ | Unweighted polling averages, head-to-head matchups |
| Secondary | Split Ticket | https://split-ticket.org/ | State-level election analysis, polling aggregation methodology |
| Secondary | Cook Political Report | https://www.cookpolitical.com/ | Race ratings, partisan voting index |
| Tertiary | Polymarket/Kalshi political markets | https://polymarket.com/ / https://kalshi.com/ | Market-implied probabilities for cross-reference |

### Economics & Federal Reserve

| Tier | Source | URL | What It Provides |
|------|--------|-----|-----------------|
| Primary | FRED (Federal Reserve Economic Data) | https://fred.stlouisfed.org/ | 800,000+ economic time series, real-time data releases |
| Primary | BLS (Bureau of Labor Statistics) | https://www.bls.gov/ | CPI, employment, wages — the actual resolution sources for many markets |
| Primary | CME FedWatch Tool | https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html | Fed funds futures-implied rate probabilities |
| Secondary | Bloomberg Economic Calendar | https://www.bloomberg.com/markets/economic-calendar | Consensus estimates vs. actuals for data releases |
| Secondary | FOMC Meeting Minutes & Dot Plot | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | Forward guidance, committee member projections |
| Tertiary | Nick Timiraos (WSJ) / Fed commentary | https://x.com/NickTimiraos | Considered the "Fed whisperer"; his reporting often moves markets |

### Weather & Climate

| Tier | Source | URL | What It Provides |
|------|--------|-----|-----------------|
| Primary | NWS/NOAA Station Data | https://www.weather.gov/ | Official station readings used for market settlement |
| Primary | Weather Underground | https://www.wunderground.com/ | Hyperlocal personal weather station network, historical data |
| Secondary | ClimateSight | https://www.climatesight.app/ | Purpose-built for weather prediction market trading, guides and dashboards |
| Secondary | Weather.gov Hourly Forecasts | https://forecast.weather.gov/ | Granular hourly forecasts for temperature markets |
| Tertiary | European Centre for Medium-Range Weather Forecasts (ECMWF) | https://www.ecmwf.int/ | Gold-standard global weather models |

### Sports

| Tier | Source | URL | What It Provides |
|------|--------|-----|-----------------|
| Primary | Official League Stats (ESPN, NFL.com, NBA.com) | https://www.espn.com/ | Player stats, injury reports, schedules |
| Primary | SportsDataIO | https://sportsdata.io/ | Live data feeds, predictive engines, historical stats APIs |
| Secondary | FiveThirtyEight/538 Sports Models | https://projects.fivethirtyeight.com/ | ELO ratings, win probability models |
| Secondary | OddsMatrix | https://oddsmatrix.com/ | Real-time betting odds aggregation, line movement |
| Tertiary | Betting market consensus (DraftKings, FanDuel) | https://www.draftkings.com/ | Market-implied probabilities from sportsbooks |

---

## Systematic Research Workflow for a New Market

### Step 1: Read the Contract (5 min)
- Read resolution criteria word-by-word
- Identify the resolution source (which agency, which specific data point)
- Note edge cases, rounding rules, settlement timing

### Step 2: Establish the Base Rate (10 min)
- How often has this type of event occurred historically?
- Use FRED, historical records, or past market data
- This is your starting probability anchor

### Step 3: Identify Primary Data Sources (10 min)
- What data directly determines the outcome?
- Where is it published? When is it released?
- Set up alerts for release dates

### Step 4: Check Current Market Price & Volume (5 min)
- What does the market currently imply?
- Is there sufficient liquidity to trade?
- Check bid-ask spread (wide spreads = higher cost)

### Step 5: Compare Independent Estimates (15 min)
- Cross-reference market price against: polls, expert consensus, models, your base rate
- If they all agree, there's likely no edge
- If they diverge significantly, investigate why

### Step 6: Check Correlated Markets (5 min)
- Have related markets already moved?
- Cross-platform price comparison (Kalshi vs. Polymarket vs. Robinhood)
- Look for lagging prices that haven't adjusted to new info

### Step 7: Assess Your Edge (5 min)
- Information advantage? (access to faster/better data)
- Analytical advantage? (better model or domain expertise)
- Structural advantage? (lower fees, better execution)
- If no edge exists, don't trade

### Step 8: Size & Execute (5 min)
- Size position proportional to confidence and edge
- Use limit orders when possible (maker vs. taker fee advantage on Kalshi)
- Document entry rationale in a trading log

---

## Practical Exercises

### Exercise 1: Pollster Rating Deep-Dive
Visit Silver Bulletin's pollster ratings. Pick 5 pollsters covering a current election. For each, note their methodology, historical accuracy rating, and partisan lean. Then compare their latest results on the same race. Calculate the spread and identify which pollster is the outlier.

### Exercise 2: FRED Data Challenge
Pick an upcoming economic market on Kalshi (e.g., next month's CPI). Use FRED to pull the last 24 months of that indicator. Calculate the historical mean, standard deviation, and the implied probability range for each market bracket. Compare to the market's current pricing.

### Exercise 3: Resolution Criteria Edge Case Hunt
Browse 10 active markets across Kalshi and Polymarket. For each, read the resolution criteria and try to find an ambiguity or edge case. Document at least 3 where the resolution could be surprising to casual traders.

### Exercise 4: Cross-Platform Price Comparison
Pick 5 identical or near-identical markets on both Kalshi and Polymarket. Record prices simultaneously. Calculate the implied probability difference. Account for fees on each platform. Determine if any spread is large enough to represent a real arbitrage opportunity.

### Exercise 5: Build a Research Checklist
Using the systematic workflow above, build a personal research checklist template. Then apply it to 3 different market categories (one political, one economic, one weather). Time yourself and note where you spent the most time.

---

## Learning Resources

### Books
1. **"Superforecasting: The Art and Science of Prediction"** by Philip Tetlock & Dan Gardner
   - https://www.penguinrandomhouse.com/books/227815/superforecasting-by-philip-e-tetlock-and-dan-gardner/
   - The foundational text on prediction accuracy, Fermi estimation, Bayesian updating, and the cognitive traits of top forecasters. Essential reading.

2. **"The Signal and the Noise"** by Nate Silver
   - https://www.penguinrandomhouse.com/books/305826/the-signal-and-the-noise-by-nate-silver/
   - Deep exploration of separating meaningful data from randomness across domains including elections, weather, and economics.

### Online Articles & Guides
3. **"How I Actually Research a Prediction Market"** — Reddit r/prediction_market101
   - https://www.reddit.com/r/prediction_market101/comments/1s58r55/how_i_actually_research_a_prediction_market/
   - Practitioner walkthrough of a real research workflow covering resolution criteria, base rates, and edge assessment.

4. **Kalshi Blog: "10 Commandments of Superforecasting"**
   - https://news.kalshi.com/p/10-commandments-of-superforecasting
   - Distillation of Tetlock's principles applied specifically to prediction market trading.

5. **Quantpedia: "Systematic Edges in Prediction Markets"**
   - https://quantpedia.com/systematic-edges-in-prediction-markets/
   - Academic-quality analysis of where systematic mispricings exist in event contract markets and how to exploit them.

### Video
6. **Nate Silver: Separating Signal from Noise (YouTube)**
   - https://www.youtube.com/watch?v=rV5Gicb66WA
   - Lecture on the core principles of his analytical methodology, applied to elections and prediction markets.

### Tools & Platforms
7. **FRED (Federal Reserve Economic Data)**
   - https://fred.stlouisfed.org/
   - Free access to 800,000+ economic datasets. Essential for researching any economics-related prediction market.

8. **Silver Bulletin Pollster Ratings**
   - https://www.natesilver.net/
   - Comprehensive pollster evaluation system. Critical for anyone trading political prediction markets.

9. **ClimateSight Weather Market Guide**
   - https://www.climatesight.app/weather-prediction-market-strategies/
   - Purpose-built resource for weather prediction market trading strategies, data sources, and common pitfalls.

---

## Learning Path

| Order | Topic | Resources | Time Estimate |
|-------|-------|-----------|---------------|
| 1 | Superforecasting Foundations | Read "Superforecasting" (Book #1), Kalshi blog post (#4) | 1 week |
| 2 | Signal vs. Noise & Polling Analysis | Read "The Signal and the Noise" (Book #2), Watch Silver lecture (#6) | 1 week |
| 3 | Data Source Mapping by Category | Explore FRED (#7), Silver Bulletin (#8), ClimateSight (#9) | 3-4 days |
| 4 | Research Workflow Practice | Apply systematic workflow to 3 live markets, do Exercise #5 | 3-4 days |
| 5 | Resolution Criteria & Edge Cases | Do Exercise #3, read Reddit walkthrough (#3) | 2-3 days |
| 6 | Cross-Market Analysis & Arbitrage | Read Quantpedia article (#5), do Exercise #4 | 3-4 days |
| 7 | Build Personal Research System | Combine learnings into personal checklist + data source library | 2-3 days |

**Total estimated time: 4-5 weeks** (part-time, ~1 hour/day)

---

## Acceptance Criteria Mapping

| Criterion | Where Covered |
|-----------|--------------|
| 3+ quality data sources per major event category | Data Sources section: 3-6 tiered sources each for Politics, Economics, Weather, Sports |
| Systematic research workflow for a new market | 8-step workflow with time estimates |
| Distinguish signal from noise in polling data | Key Concept #3, Book #2, Video #6 |
| Information advantage on at least one category | Key Concept #8, Exercise #2 (economics via FRED), Exercise #1 (politics via pollster ratings) |
