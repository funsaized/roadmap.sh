# Entity Index — Prediction Market Trading Strategies

## People

| Entity | Role | Referenced In |
|--------|------|---------------|
| Robin Hanson | LMSR inventor (2002/2003) | gensyn-lmsr, medium-lmsr-math, cdetrio-prediction-market-lmsr, navnoorbawa-prediction-markets-math |
| Ciamac Moallemi | PM-AMM co-author (Paradigm/Columbia) | paradigm-pm-amm, apostlex0-prediction-market-amm |
| Dan Robinson | PM-AMM co-author (Paradigm) | paradigm-pm-amm, apostlex0-prediction-market-amm |
| Navnoor Bawa | Quantitative researcher, prediction market analysis | navnoorbawa-prediction-markets-math |
| Bernhard Meister | Academic researcher, Kelly criterion in prediction markets | arxiv-kelly-prediction-markets |
| J.L. Kelly Jr. | Original Kelly criterion paper (1956) | kelly-criterion-polymarket-bot, prediction-market-amm-with-kelly |
| E.O. Thorp | Optimal gambling systems (1969) | kelly-criterion-polymarket-bot |
| Paul Sztorc | Truthcoin creator | cdetrio-prediction-market-lmsr |
| Warren Buffett | Quoted on risk | hummingbot-inventory-risk |
| CodePulse | Medium article author on LMSR math | medium-lmsr-math |
| terrytrl100 | Polymarket MM bot author | terrytrl100-polymarket-automated-mm |
| warproxxx | Poly-maker fork maintainer | warproxxx-poly-maker |
| Apostlex0 | Morpheus PM-AMM implementation | apostlex0-prediction-market-amm |
| @defiance_cr | Original poly-maker author | terrytrl100-polymarket-automated-mm |
| joicodev | Polymarket bot developer (Kelly impl) | kelly-criterion-polymarket-bot |

## Organizations

| Entity | Type | Referenced In |
|--------|------|---------------|
| Polymarket | Prediction market platform | polymarket-ctf-overview, polymarket-clob-introduction, polymarket-docs, navnoorbawa-prediction-markets-math, terrytrl100-polymarket-automated-mm, warproxxx-poly-maker, medium-lmsr-math |
| Paradigm | Crypto research firm | paradigm-pm-amm, apostlex0-prediction-market-amm, gensyn-lmsr |
| Gnosis | CTF developer | gnosis-conditional-tokens-market-makers, polymarket-ctf-overview, navnoorbawa-prediction-markets-math |
| Kalshi | CFTC-regulated prediction exchange | navnoorbawa-prediction-markets-math |
| PredictIt | Prediction market platform | navnoorbawa-prediction-markets-math |
| Hummingbot | Market making bot framework | hummingbot-inventory-risk |
| Manifold Markets | Prediction market platform | manifold-market-maker |
| Gensyn AI | AI/ML research company | gensyn-lmsr |
| Coding Nexus | Medium publication | medium-lmsr-math |
| UMA | Optimistic oracle provider | polymarket-ctf-overview, navnoorbawa-prediction-markets-math |
| Chainlink | Oracle provider | polymarket-ctf-overview |
| CFTC | US regulatory body | navnoorbawa-prediction-markets-math |
| DC Circuit Court | Regulatory decision maker | navnoorbawa-prediction-markets-math |
| Chainsecurity | Smart contract auditor | polymarket-clob-introduction |
| Columbia University | Academic institution (Moallemi) | paradigm-pm-amm |

## Technologies

| Entity | Category | Referenced In |
|--------|----------|---------------|
| LMSR (Logarithmic Market Scoring Rule) | Pricing mechanism | gensyn-lmsr, medium-lmsr-math, cdetrio-prediction-market-lmsr, navnoorbawa-prediction-markets-math |
| PM-AMM (Prediction Market AMM) | Pricing mechanism | paradigm-pm-amm, apostlex0-prediction-market-amm |
| Conditional Token Framework (CTF) | Token standard | polymarket-ctf-overview, gnosis-conditional-tokens-market-makers, navnoorbawa-prediction-markets-math |
| ERC-1155 | Token standard | polymarket-ctf-overview, navnoorbawa-prediction-markets-math |
| CLOB (Central Limit Order Book) | Trading infrastructure | polymarket-clob-introduction, navnoorbawa-prediction-markets-math, terrytrl100-polymarket-automated-mm |
| EIP-712 | Signature standard | polymarket-clob-introduction, polymarket-ctf-overview |
| Polygon PoS | Settlement chain | polymarket-ctf-overview, polymarket-clob-introduction |
| USDC | Collateral token | polymarket-ctf-overview |
| UMA Optimistic Oracle | Resolution mechanism | polymarket-ctf-overview, navnoorbawa-prediction-markets-math |
| Chainlink Oracle | Price feed | polymarket-ctf-overview |
| Softmax function | ML/pricing connection | gensyn-lmsr, medium-lmsr-math |
| Bregman divergences | Mathematical framework | gensyn-lmsr |
| Kelly criterion | Position sizing | kelly-criterion-polymarket-bot, navnoorbawa-prediction-markets-math, arxiv-kelly-prediction-markets, prediction-market-amm-with-kelly |
| Brier score | Calibration metric | kelly-criterion-polymarket-bot, prediction-market-amm-with-kelly |
| Aptos blockchain | Smart contract platform | apostlex0-prediction-market-amm |
| Move language | Smart contract language | apostlex0-prediction-market-amm |
| Hummingbot framework | MM bot platform | hummingbot-inventory-risk |
| Manifold API | Prediction market API | manifold-market-maker |
| Google Sheets API | Configuration management | terrytrl100-polymarket-automated-mm, warproxxx-poly-maker |
| WebSocket | Real-time data | terrytrl100-polymarket-automated-mm, warproxxx-poly-maker |
| TypeScript SDK | Polymarket SDK | polymarket-clob-introduction, polymarket-docs |
| Python SDK | Polymarket SDK | polymarket-clob-introduction, polymarket-docs |
| Rust SDK | Polymarket SDK | polymarket-clob-introduction, polymarket-docs |
| Truffle framework | Smart contract dev | gnosis-conditional-tokens-market-makers |
| Solidity | Smart contract language | gnosis-conditional-tokens-market-makers |
| UV package manager | Python tooling | warproxxx-poly-maker |
| Truthcoin | Prediction market system | cdetrio-prediction-market-lmsr |

## Key Concepts

| Concept | Description | Referenced In |
|---------|-------------|---------------|
| YES + NO = $1.00 invariant | Core pricing invariant for binary markets | navnoorbawa-prediction-markets-math, polymarket-ctf-overview, medium-lmsr-math |
| Loss-vs-Rebalancing (LVR) | Cost metric for AMM liquidity providers | paradigm-pm-amm, apostlex0-prediction-market-amm, prediction-market-amm-with-kelly |
| Inventory risk | Risk of holding wrong-side assets | hummingbot-inventory-risk, warproxxx-poly-maker |
| Fractional Kelly | Risk-adjusted position sizing (α × f*) | kelly-criterion-polymarket-bot, navnoorbawa-prediction-markets-math, prediction-market-amm-with-kelly |
| Longshot bias | Retail overpays for low-probability outcomes | navnoorbawa-prediction-markets-math |
| Recency bias | Price overreaction to recent news | navnoorbawa-prediction-markets-math |
| Cross-platform arbitrage | Exploiting price differences between platforms | navnoorbawa-prediction-markets-math |
| Position merging | Combining YES+NO→collateral | terrytrl100-polymarket-automated-mm, warproxxx-poly-maker |
| Maker rewards | Fee incentives for liquidity provision | terrytrl100-polymarket-automated-mm |
| Uniform AMM principle | LVR constant across all prices | paradigm-pm-amm, apostlex0-prediction-market-amm |
| Information aggregation | Prices reflect collective beliefs | gensyn-lmsr |
| Incentive compatibility | Truthful reporting is optimal | gensyn-lmsr |
| Bounded market maker loss | Max loss = b × ln(n) | gensyn-lmsr, medium-lmsr-math |
| Dynamic time-decay | Liquidity reduces as expiry approaches | paradigm-pm-amm, apostlex0-prediction-market-amm |

## Statistics Summary

- **Total unique people:** 15
- **Total unique organizations:** 15
- **Total unique technologies:** 27
- **Total unique concepts:** 14
- **Grand total unique entities:** 71
