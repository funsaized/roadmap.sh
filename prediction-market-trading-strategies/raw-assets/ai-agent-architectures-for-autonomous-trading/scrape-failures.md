# Scrape Failures — T-7: AI Agent Architectures for Autonomous Trading

## Failed URLs

### MUST-SCRAPE

1. **https://www.paradigm.xyz/2024/11/pm-amm**
   - Status: Failed (title-only retrieval)
   - Reason: Cloudflare anti-bot protection / JavaScript-rendered page
   - Content retrieved: Only the page title "pm-AMM: A Uniform AMM for Prediction Markets - Paradigm"
   - Impact: High — this is the foundational PM-AMM paper
   - Retry suggestion: Use direct PDF/arXiv version if available, or browser automation

2. **https://medium.com/coding-nexus/how-polymarket-actually-prices-beliefs-the-math-behind-lmsr-98b424e12da5**
   - Status: Partial (content truncated)
   - Reason: Medium paywall or content length limit — only ~1,175 chars extracted (intro + partial)
   - Content retrieved: First ~6 paragraphs (intro, problem statement, partial "Core Idea" section)
   - Impact: Medium — useful LMSR explanation but truncated
   - Retry suggestion: Use textise dot iitty, or fetch via RSS/institutional access

### SHOULD-SCRAPE

3. **https://www.quantvps.com/blog/market-making-in-prediction-markets**
   - Status: Failed (429 Too Many Requests)
   - Reason: Vercel rate limiting / Cloudflare bot protection
   - Retry suggestion: Wait and retry with User-Agent rotation

4. **https://github.com/cdetrio/prediction-market-lmsr** (raw README path)
   - Status: Failed (404 Not Found)
   - Reason: No README.md at main branch root (repo may use different structure)
   - Content retrieved: None — GitHub page loaded but content extraction yielded only navigation boilerplate
   - Impact: Low — alternative LMSR resources are available

5. **https://www.cs.cmu.edu/~sandholm/liquidity-sensitive%20automated%20market%20maker.teac.pdf**
   - Status: Failed (PDF binary, not text-extractable)
   - Reason: Raw PDF binary content returned; text extraction not available
   - Impact: Medium — Liquidity-Sensitive AMM paper by Sandholm et al.
   - Retry suggestion: Use arXiv version with text extraction, or fetch as base64

### Alternative Paths Attempted (also failed)

6. **https://raw.githubusercontent.com/gnosis/conditional-tokens-market-makers/main/README.md**
   - Status: 404 (file not at this path)

7. **https://raw.githubusercontent.com/cdetrio/prediction-market-lmsr/main/README.md**
   - Status: 404 (file not at this path)

## Summary

| URL | Category | Failure Reason | Impact |
|-----|----------|---------------|--------|
| paradigm.xyz/pm-amm | must-scrape | Cloudflare protection | High |
| medium.com/LMSR-math | must-scrape | Truncated/paywall | Medium |
| quantvps.com | should-scrape | 429 rate limit | Medium |
| cdetrio/prediction-market-lmsr | should-scrape | 404 / no content | Low |
| CMU PDF paper | should-scrape | Binary PDF, no text | Medium |

## Coverage Assessment

Successfully scraped: 8/14 URLs (57%)
Must-scrape success rate: 3/5 (60%) — meets minimum threshold
Total assets created: 8 markdown files
