# Source Catalog: Market Making and AMM Mechanisms

## Research Focus
LMSR, CPMM, order book dynamics, spread management, inventory risk, AMM design for binary outcome contracts

---

## MUST SCRAPE (Critical Sources)

### 1. pm-AMM: A Uniform AMM for Prediction Markets
- **URL:** https://www.paradigm.xyz/2024/11/pm-amm
- **Title:** pm-AMM: A Uniform AMM for Prediction Markets
- **Source type:** paper/article
- **Authority:** high
- **Relevance:** high
- **Content preview:** Paradigm's detailed paper introducing the pm-AMM (prediction market AMM) designed specifically for binary outcome tokens. Addresses Loss-vs-Rebalancing (LVR), Gaussian score dynamics, and achieves uniform LVR across all price points. Compares to CPMM and LMSR.
- **Scrape notes:** Well-structured article from Paradigm. Key source for AMM comparison and pm-AMM design rationale.

### 2. How Polymarket Actually Prices Beliefs: The Math Behind LMSR
- **URL:** https://medium.com/coding-nexus/how-polymarket-actually-prices-beliefs-the-math-behind-lmsr-98b424e12da5
- **Title:** How Polymarket Actually Prices Beliefs: The Math Behind LMSR
- **Source type:** article
- **Authority:** medium
- **Relevance:** high
- **Content preview:** Detailed explanation of LMSR mathematical formulation including cost function C(q) = b * ln(Σ e^(qi/b)), price function p_i(q) = e^(qi/b) / Σ e^(qj/b), and Python implementation code. Directly addresses binary outcome pricing.
- **Scrape notes:** Contains working Python code for LMSR implementation. Good for pseudocode/reference implementation.

### 3. Gnosis Conditional Tokens Market Makers (GitHub)
- **URL:** https://github.com/gnosis/conditional-tokens-market-makers
- **Title:** gnosis/conditional-tokens-market-makers: AMM Smart Contracts for Conditional Tokens Markets
- **Source type:** code
- **Authority:** high
- **Relevance:** high
- **Content preview:** Smart contracts implementing FixedProductMarketMaker (CPMM) and LMSR for Gnosis Conditional Token Framework. Powers Polymarket's underlying AMM infrastructure. Contains MarketMaker.sol and related contracts.
- **Scrape notes:** GitHub repo with Solidity code. Key for implementation details of both CPMM and LMSR market makers.

### 4. LMSR: Logarithmic Market Scoring Rule
- **URL:** https://blog.gensyn.ai/lmsr-logarithmic-market-scoring-rule/
- **Title:** LMSR: Logarithmic Market Scoring Rule Explained
- **Source type:** article
- **Authority:** medium
- **Relevance:** high
- **Content preview:** Comprehensive explanation of LMSR mechanism including cost function, price derivation, liquidity parameter b, and implementation considerations. Covers bounded loss b*ln(n) for market makers.
- **Scrape notes:** Clear explanations with diagrams. Good secondary source for LMSR formulation.

### 5. Polymarket CTF Overview (Official Documentation)
- **URL:** https://docs.polymarket.com/trading/ctf/overview
- **Title:** Conditional Token Framework - Polymarket Documentation
- **Source type:** documentation
- **Authority:** high
- **Relevance:** high
- **Content preview:** Official documentation on Polymarket's Conditional Token Framework (ERC-1155 tokens). Explains Split/Merge/Redeem operations, token identifiers, and how binary Yes/No outcomes are represented on-chain.
- **Scrape notes:** Primary documentation source. Well-structured with code examples.

---

## SHOULD SCRAPE (Valuable Sources)

### 6. PredictionMarket_AMM - pm-AMM Implementation on Aptos
- **URL:** https://github.com/Apostlex0/PredictionMarket_AMM
- **Title:** High-fidelity implementation of Paradigm's pm-AMM on Aptos
- **Source type:** code
- **Authority:** medium
- **Relevance:** high
- **Content preview:** Open-source implementation of Paradigm's pm-AMM on the Aptos blockchain using Move language. Focuses on capital efficiency for trading binary outcome tokens.
- **Scrape notes:** Reference implementation for pm-AMM. Useful for understanding implementation details beyond the Paradigm paper.

### 7. Polymarket Automated Market Maker Bot
- **URL:** https://github.com/terrytrl100/polymarket-automated-mm
- **Title:** Automated liquidity provision bot for Polymarket
- **Source type:** code
- **Authority:** medium
- **Relevance:** high
- **Content preview:** Bot that automates liquidity provision on Polymarket by maintaining orders on both sides with configurable parameters. Includes real-time order book monitoring and position management.
- **Scrape notes:** Working bot implementation. Good for understanding practical market making on Polymarket.

### 8. Manifold Markets Market Maker Bot
- **URL:** https://github.com/manifoldmarkets/market-maker
- **Title:** Market making bot for Manifold prediction markets
- **Source type:** code
- **Authority:** medium
- **Relevance:** medium
- **Content preview:** TypeScript market-making bot that calculates EMA and variance of probabilities to place orders above and below current market price. Uses Manifold API.
- **Scrape notes:** Good example of prediction market API integration and strategy implementation.

### 9. Market Making in Prediction Markets
- **URL:** https://www.quantvps.com/blog/market-making-in-prediction-markets
- **Title:** Market Making in Prediction Markets - A Complete Guide
- **Source type:** article
- **Authority:** medium
- **Relevance:** high
- **Content preview:** Detailed guide covering spread management, inventory risk, dynamic pricing algorithms, Stoikov model adaptation, position limits, hedging strategies, and circuit breakers for prediction markets.
- **Scrape notes:** Practical guide with risk management strategies. Good complement to theoretical AMM sources.

### 10. Binary Outcome AMM Design
- **URL:** https://navnoorbawa.substack.com/p/the-math-of-prediction-markets-binary
- **Title:** The Math of Prediction Markets - Binary Outcomes
- **Source type:** article
- **Authority:** low
- **Relevance:** high
- **Content preview:** Explains mathematical foundations for binary outcome prediction markets, including constant product formulas, price discovery, and AMM design trade-offs.
- **Scrape notes:** Stack Exchange/Substack format. Accessible explanation of binary outcome math.

### 11. Liquidity-Sensitive Automated Market Maker (CMU)
- **URL:** https://www.cs.cmu.edu/~sandholm/liquidity-sensitive%20automated%20market%20maker.teac.pdf
- **Title:** Liquidity-Sensitive Automated Market Maker
- **Source type:** paper
- **Authority:** high
- **Relevance:** high
- **Content preview:** Academic paper by Tuomas Sandholm and colleagues on liquidity-sensitive AMMs that adjust spreads based on market conditions. Extension of LMSR with dynamic liquidity parameters.
- **Scrape notes:** Academic paper from Carnegie Mellon. Important for advanced AMM design considerations.

### 12. Poly-Maker: Polymarket Market Making Bot
- **URL:** https://github.com/warproxxx/poly-maker
- **Title:** Fork of Polymarket automated market maker
- **Source type:** code
- **Authority:** medium
- **Relevance:** medium
- **Content preview:** Fork of polymarket-automated-mm with modules for data management, position merging, and statistics tracking. Reference implementation (author notes may not be profitable in current market).
- **Scrape notes:** Alternative implementation approach. Useful for comparison with terrytrl100 bot.

### 13. Hummingbot: What is Inventory Risk?
- **URL:** https://hummingbot.org/blog/what-is-inventory-risk/
- **Title:** Inventory Risk in Market Making
- **Source type:** article
- **Authority:** medium
- **Relevance:** high
- **Content preview:** General explanation of inventory risk in market making, applicable to prediction markets. Covers adverse selection, position management, and risk mitigation strategies.
- **Scrape notes:** General market making concepts apply to prediction markets. Good for foundational understanding.

### 14. Arbitrage and Loss-Vs-Rebalancing in PM-AMM
- **URL:** https://ethereum.stackexchange.com/
- **Title:** Ethereum Stack Exchange (references to AMM LVR)
- **Source type:** discussion
- **Authority:** medium
- **Relevance:** medium
- **Content preview:** Community discussions on impermanent loss, LVR, and AMM design for prediction markets. References to pm-AMM and specific challenges with binary outcome tokens.
- **Scrape notes:** Community Q&A format. Good for understanding practical challenges.

### 15. LMSR Prediction Market Implementation (GitHub)
- **URL:** https://github.com/cdetrio/prediction-market-lmsr
- **Title:** LMSR prediction market implementation
- **Source type:** code
- **Authority:** low
- **Relevance:** high
- **Content preview:** Another LMSR implementation reference. Alternative code example for educational purposes.
- **Scrape notes:** Supplementary code reference. Good for comparison with other LMSR implementations.

---

## NICE TO HAVE (Supplementary Sources)

### 16. Binary Outcomes: Constant Product Market Maker
- **URL:** https://www.emergentmind.com/topics/constant-product-market-maker
- **Title:** CPMM for Binary Outcomes
- **Source type:** article
- **Authority:** low
- **Relevance:** medium
- **Content preview:** Explains how constant product formula x*y=k applies to binary outcome prediction markets, including advantages and disadvantages of using CPMM for outcome tokens.
- **Scrape notes:** Conceptual explanation. Good for understanding CPMM limitations in prediction markets.

### 17. Manifold API Documentation
- **URL:** https://docs.manifold.markets/api
- **Title:** Manifold Markets API Documentation
- **Source type:** documentation
- **Authority:** high
- **Relevance:** medium
- **Content preview:** Official API documentation for Manifold prediction markets. Includes endpoints for market data, order placement, and bot authentication.
- **Scrape notes:** API reference. Useful for understanding how prediction market APIs work.

### 18. GitHub - mushtaq96/prediction-market-LMSR
- **URL:** https://github.com/mushtaq96/prediction-market-LMSR-
- **Title:** Prediction Market LMSR Implementation
- **Source type:** code
- **Authority:** low
- **Relevance:** medium
- **Content preview:** Python implementation of LMSR prediction market with web interface. Good reference for educational implementations.
- **Scrape notes:** Simple implementation. Good for understanding LMSR basics.

### 19. Polymarket CLOB Market Making Guide
- **URL:** https://docs.polymarket.com/market-makers/inventory
- **Title:** Polymarket Market Makers - Inventory Management
- **Source type:** documentation
- **Authority:** high
- **Relevance:** high
- **Content preview:** Official Polymarket guide on inventory management for market makers. Covers position tracking, risk management, and operational best practices.
- **Scrape notes:** Official documentation on MM operations. Good for practical implementation guidance.

### 20. Polymarket Python CLOB Client
- **URL:** https://github.com/Polymarket/py-clob-client
- **Title:** Python client for Polymarket CLOB API
- **Source type:** code
- **Authority:** high
- **Relevance:** medium
- **Content preview:** Official Python SDK for interacting with Polymarket's Central Limit Order Book. Includes order submission, cancellation, and market data retrieval.
- **Scrape notes:** Official SDK. Essential for building Polymarket market making bots.

---

## Source Summary

| Priority | Count | Top Source Types |
|----------|-------|------------------|
| Must Scrape | 5 | paper (1), article (2), code (1), documentation (1) |
| Should Scrape | 10 | code (4), article (4), paper (1), discussion (1) |
| Nice to Have | 5 | documentation (2), code (2), article (1) |
| **Total** | **20** | **paper (2), article (8), code (8), documentation (3), discussion (1)** |

## Key Domains Represented
- paradigm.xyz (1) - AMM research paper
- medium.com (2) - Technical articles
- github.com (8) - Code implementations
- docs.polymarket.com (2) - Official documentation
- quantvps.com (1) - Practical guides
- cs.cmu.edu (1) - Academic paper
- hummingbot.org (1) - Risk management
- manifold.markets (1) - Alternative platform
- ethresear.ch references via paradigm.xyz

## Scraping Priority Notes
1. Start with Paradigm pm-AMM paper for AMM comparison framework
2. Then fetch LMSR formulation sources (gensyn.ai, medium article)
3. Fetch Gnosis smart contract code for implementation details
4. Fetch Polymarket documentation for CTF understanding
5. Then proceed to bot implementations and practical guides
