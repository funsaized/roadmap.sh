# Cross-Reference Map — Prediction Market Trading Strategies

## Relationship Types
- **supports** — Asset A provides evidence backing claims in Asset B
- **contradicts** — Asset A presents a different perspective from Asset B
- **extends** — Asset A goes deeper on a topic mentioned in Asset B
- **cites** — Asset A references same primary source as Asset B
- **complements** — Assets A and B together give a complete picture

---

## By Source Asset

### gensyn-lmsr (LMSR: Logarithmic Market Scoring Rule)
| Relationship | Target | Description |
|---|---|---|
| extends → | paradigm-pm-amm | PM-AMM is presented as evolution beyond LMSR |
| complements | medium-lmsr-math | Different explanation of same LMSR math + Python code |
| complements | polymarket-ctf-overview | CTF is token layer; LMSR is pricing layer |
| cites | cdetrio-prediction-market-lmsr | Both implement Hanson's LMSR |
| supports | navnoorbawa-prediction-markets-math | Confirms LMSR as foundational mechanism |

### paradigm-pm-amm (PM-AMM: Uniform AMM for Prediction Markets)
| Relationship | Target | Description |
|---|---|---|
| extends | gensyn-lmsr | PM-AMM solves LMSR limitations |
| supports | apostlex0-prediction-market-amm | Morpheus directly implements this paper |
| contradicts | gnosis-conditional-tokens-market-makers | CPMM approach has guaranteed loss at expiry |
| complements | hummingbot-inventory-risk | PM-AMM's time-decay addresses inventory risk |

### apostlex0-prediction-market-amm (Morpheus PM-AMM on Aptos)
| Relationship | Target | Description |
|---|---|---|
| extends | paradigm-pm-amm | Direct implementation of Paradigm paper |
| extends | gensyn-lmsr | PM-AMM evolves beyond LMSR |
| contradicts | gnosis-conditional-tokens-market-makers | Different AMM approach (PM-AMM vs CPMM) |
| complements | hummingbot-inventory-risk | Time-decay addresses inventory risk near expiry |
| complements | terrytrl100-polymarket-automated-mm | Different approach: CLOB MM vs AMM |

### polymarket-ctf-overview (Conditional Token Framework)
| Relationship | Target | Description |
|---|---|---|
| complements | polymarket-clob-introduction | CLOB handles orders; CTF handles tokens |
| complements | polymarket-docs | Landing page points to this detail |
| supports | gensyn-lmsr | CTF provides token layer for LMSR pricing |
| supports | navnoorbawa-prediction-markets-math | Confirms YES+NO=$1 invariant |
| cites | gnosis-conditional-tokens-market-makers | Gnosis created CTF standard |

### polymarket-clob-introduction (CLOB API)
| Relationship | Target | Description |
|---|---|---|
| complements | polymarket-ctf-overview | CLOB handles orders; CTF handles tokens |
| complements | polymarket-docs | Overview points to this detail |
| supports | terrytrl100-polymarket-automated-mm | Bot uses this API |
| supports | warproxxx-poly-maker | Bot uses this API |
| supports | navnoorbawa-prediction-markets-math | Describes CLOB mechanics in theory |

### navnoorbawa-prediction-markets-math (Binary Options + Kelly + Arbitrage)
| Relationship | Target | Description |
|---|---|---|
| extends | kelly-criterion-polymarket-bot | Provides theoretical framework for Kelly implementation |
| extends | gensyn-lmsr | Covers LMSR theory referenced here |
| supports | polymarket-ctf-overview | Confirms CTF mechanics |
| supports | polymarket-clob-introduction | Confirms CLOB architecture |
| complements | hummingbot-inventory-risk | Behavioral patterns create inventory risks |
| complements | medium-lmsr-math | LMSR in code detail |
| complements | paradigm-pm-amm | Discusses AMM limitations PM-AMM solves |

### kelly-criterion-polymarket-bot (Fractional Kelly Implementation)
| Relationship | Target | Description |
|---|---|---|
| extends | navnoorbawa-prediction-markets-math | Implements Kelly theory from article |
| extends | prediction-market-amm-with-kelly | Same formula, different implementation |
| complements | arxiv-kelly-prediction-markets | Academic theory vs practical implementation |
| supports | hummingbot-inventory-risk | Position sizing is risk management |
| complements | terrytrl100-polymarket-automated-mm | Different strategy: MM spread vs Kelly edge |

### arxiv-kelly-prediction-markets (Academic Kelly Paper)
| Relationship | Target | Description |
|---|---|---|
| supports | kelly-criterion-polymarket-bot | Theoretical backing for implementation |
| supports | navnoorbawa-prediction-markets-math | Academic complement to practitioner analysis |
| extends | prediction-market-amm-with-kelly | Academic depth on Kelly mathematics |

### terrytrl100-polymarket-automated-mm (Poly-Maker Bot)
| Relationship | Target | Description |
|---|---|---|
| extends | warproxxx-poly-maker | Same codebase lineage, more optimization |
| supports | hummingbot-inventory-risk | Implements inventory management concepts |
| complements | polymarket-clob-introduction | Uses documented CLOB API |
| complements | polymarket-ctf-overview | Uses CTF for position merging |
| complements | manifold-market-maker | Simpler MM bot for different platform |

### warproxxx-poly-maker (Poly-Maker Fork)
| Relationship | Target | Description |
|---|---|---|
| extends | terrytrl100-polymarket-automated-mm | Same codebase lineage |
| contradicts | terrytrl100-polymarket-automated-mm | Warns about unprofitability vs optimistic framing |
| supports | hummingbot-inventory-risk | Confirms inventory risk importance |

### medium-lmsr-math (LMSR Math with Python)
| Relationship | Target | Description |
|---|---|---|
| complements | gensyn-lmsr | Different perspective on same LMSR math |
| supports | navnoorbawa-prediction-markets-math | Confirms LMSR foundations |
| cites | cdetrio-prediction-market-lmsr | Another LMSR implementation |
| complements | polymarket-clob-introduction | Covers post-LMSR CLOB architecture |

### hummingbot-inventory-risk (Inventory Risk Guide)
| Relationship | Target | Description |
|---|---|---|
| supports | apostlex0-prediction-market-amm | PM-AMM time-decay addresses this risk |
| supports | terrytrl100-polymarket-automated-mm | Practical implementation of concepts |
| supports | warproxxx-poly-maker | Position merging reduces exposure |
| complements | kelly-criterion-polymarket-bot | Position sizing manages risk |
| extends | paradigm-pm-amm | PM-AMM provides theoretical risk framework |

### manifold-market-maker (Manifold MM Bot)
| Relationship | Target | Description |
|---|---|---|
| complements | terrytrl100-polymarket-automated-mm | Simpler bot, different platform |
| complements | warproxxx-poly-maker | Another reference implementation |
| supports | hummingbot-inventory-risk | Implements spread-capture strategy |

### gnosis-conditional-tokens-market-makers (Gnosis CTF AMM)
| Relationship | Target | Description |
|---|---|---|
| supports | polymarket-ctf-overview | Polymarket built on this standard |
| complements | apostlex0-prediction-market-amm | Different AMM approach |
| supports | gensyn-lmsr | Implements LMSR-based AMM |

### polymarket-docs (Documentation Overview)
| Relationship | Target | Description |
|---|---|---|
| complements | polymarket-clob-introduction | Points to detailed CLOB docs |
| complements | polymarket-ctf-overview | Points to token framework docs |

### cdetrio-prediction-market-lmsr (LMSR Demo)
| Relationship | Target | Description |
|---|---|---|
| supports | gensyn-lmsr | Implements same LMSR theory |
| supports | medium-lmsr-math | Another LMSR implementation |

### prediction-market-amm-with-kelly (PM-AMM + Kelly Code)
| Relationship | Target | Description |
|---|---|---|
| complements | kelly-criterion-polymarket-bot | JS vs Python implementation |
| extends | apostlex0-prediction-market-amm | Same repo, Kelly-focused |
| supports | navnoorbawa-prediction-markets-math | Implements same formulas |

---

## Statistics

- **Total cross-reference relationships:** 58
- **Most cross-referenced asset:** navnoorbawa-prediction-markets-math (7 relationships as source, 6 as target)
- **Most connected cluster:** LMSR ↔ PM-AMM ↔ CTF (pricing mechanism evolution)
- **Key bridging assets:** hummingbot-inventory-risk (connects theory to practice), navnoorbawa-prediction-markets-math (connects all major themes)
