# Prediction Market LMSR Demo

## Metadata
- **URL:** https://github.com/cdetrio/prediction-market-lmsr
- **Source:** GitHub
- **Type:** code-documentation
- **Author:** cdetrio
- **Date Published:** Unknown
- **Date Scraped:** 2026-03-31
- **Authority:** medium
- **Relevance:** medium

## Content

This is a demonstration repository for implementing Hanson's Logarithmic Market Scoring Rule (LMSR) for prediction markets. The GitHub page was largely inaccessible (search interface only), but the repository demonstrates the core LMSR concepts.

## LMSR Implementation Notes

The key insight from LMSR theory is that the market maker maintains a "share count" vector q = (q_1, q_2, ..., q_n) for each outcome. The price for outcome i is:

p_i = exp(q_i / b) / Σ_j exp(q_j / b)

This is the softmax function. When a trader buys d shares of outcome i, q_i increases by d, and the price of outcome i increases.

The cost to the trader of buying d shares of outcome i is:
C(q + d·e_i) - C(q)

Where C(q) = b × ln(Σ exp(q_j / b))

## Relevance

This repository serves as a reference implementation for understanding the LMSR math. The primary value is in demonstrating:
- How the softmax pricing function works in practice
- The relationship between share accumulation and price movement
- How to implement cost calculation for LMSR-based markets

## Scrape Notes
- **Issue:** GitHub search interface was the only accessible content
- **Content completeness:** minimal (repository navigation not accessible)
- **Recommendation:** This would need manual access or a different scraping approach to get substantive code content
