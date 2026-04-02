# Scrape Failures

## Target: Risk Management for Prediction Market Portfolios
## Slug: risk-management-for-prediction-market-portfolios

### Failed URLs

1. **quantvps.com/blog/market-making-in-prediction-markets**
   - Status: 429 (Rate Limited)
   - Issue: Vercel security checkpoint blocked access
   - Retry possible: Yes, with delay

2. **cdetrio/prediction-market-lmsr (GitHub)**
   - Status: Partial
   - Issue: Repository shows only "Saved searches" — likely deleted or private
   - Retry possible: No (repo appears to no longer exist)

3. **CMU paper (Liquidity-Sensitive Automated Market Maker)**
   - Status: Failed
   - Issue: URL format `cs.cmu.edu/~sandholm/liquidity-sensitive%20automated%20market%20maker.teac.pdf` could not be accessed
   - Retry possible: Unknown (URL may be outdated)

4. **paradigm.xyz/2024/11/pm-amm**
   - Status: Partial
   - Issue: Page content requires JS rendering (Cloudflare/access gate). Title extracted via search, content reconstructed from web search results
   - Retry possible: With browser automation tool

### Notes
- All MUST-SCRAPE URLs were addressed (Paradigm paper has content reconstructed from search)
- All failures are documented above
- 11 of ~15 URLs successfully scraped (73% success rate)
- Total assets created: 11 markdown files
