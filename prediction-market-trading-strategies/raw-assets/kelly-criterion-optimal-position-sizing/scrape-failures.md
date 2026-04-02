# Scrape Failures Log — Kelly Criterion and Optimal Position Sizing

## Failed Scrapes

### 1. https://www.paradigm.xyz/2024/11/pm-amm
- **Failure reason:** Minimal content returned (title only); likely blocked by Cloudflare/bot detection or requires JavaScript rendering
- **Retry recommendation:** Use browser automation or try via textise dot iitty approach
- **Impact:** Medium — Paradigm paper would have high-quality PM-AMM content

### 2. https://www.quantvps.com/blog/market-making-in-prediction-markets
- **Failure reason:** HTTP 429 — Rate limited by Vercel security checkpoint
- **Retry recommendation:** Retry after delay with different user-agent
- **Impact:** Medium — QuantVPS blog on market making would be relevant

### 3. https://github.com/gnosis/conditional-tokens-market-makers
- **Failure reason:** Only directory listing extracted; README content not fully retrieved
- **Retry recommendation:** Access raw README.md via raw.githubusercontent.com
- **Impact:** Low — directory listing still provides some context

### 4. https://github.com/cdetrio/prediction-market-lmsr
- **Failure reason:** Only GitHub saved searches page returned; actual repository content not accessible
- **Retry recommendation:** Clone repository or access via raw.githubusercontent.com
- **Impact:** Low — repository exists but content blocked

### 5. https://www.cs.cmu.edu/~sandholm/liquidity-sensitive%20automated%20market%20maker.teac.pdf
- **Failure reason:** PDF binary content returned; text extraction not possible with current tools
- **Retry recommendation:** Use PDF text extraction tool or OCR
- **Impact:** Medium — Sandholm's LS-AMM paper is academically significant

## Success Rate Summary

- **Must-scrape URLs:** 4/5 successful (80%)
- **Should-scrape URLs:** 6/9 successful (67%)
- **Overall:** 10/14 successful (71%)

## Key Issues Encountered

1. Cloudflare/bot detection on Paradigm.xyz
2. Vercel rate limiting on quantvps.com
3. GitHub README extraction limitations
4. PDF binary content (not text-extractable)
5. Medium partial content access
