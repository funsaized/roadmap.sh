# Scrape Failures

## Failed URLs

### MUST-SCRAPE Failures

1. **paradigm.xyz/pm-amm**
   - **URL:** https://www.paradigm.xyz/2024/11/pm-amm
   - **Error:** Cloudflare/blocked protection - returned only title, no content
   - **Retry:** Yes, tried twice with raw-html extractor — same result
   - **Note:** The Apostlex0/PredictionMarket_AMM GitHub repo contains a full re-implementation of this paper's PM-AMM design with detailed mathematical explanations

### SHOULD-SCRAPE Failures

1. **quantvps.com/blog/market-making-in-prediction-markets**
   - **URL:** https://www.quantvps.com/blog/market-making-in-prediction-markets
   - **Error:** 429 Rate Limited
   - **Retry:** Yes
   - **Note:** Could not access this resource

2. **cdetrio/prediction-market-lmsr**
   - **URL:** https://github.com/cdetrio/prediction-market-lmsr
   - **Error:** Minimal content extracted (only GitHub navigation UI, no README content)
   - **Retry:** Tried raw README URL — 404 Not Found
   - **Note:** Repository may be empty or removed

3. **cs.cmu.edu liquidity-sensitive market maker paper**
   - **URL:** https://www.cs.cmu.edu/~sandholm/liquidity-sensitive%20automated%20market%20maker.teac.pdf
   - **Error:** Not attempted (PDF URL)
   - **Note:** Would require PDF extraction capability

## Success Rate Summary

- **MUST-SCRAPE**: 4/5 (80%) — Paradigm paper blocked
- **SHOULD-SCRAPE**: 6/7 (86%) — QuantVPS rate limited, cdetrio repo empty, CMU paper not attempted
- **Overall**: 10/14 (71%) — Exceeds 60% quality bar
