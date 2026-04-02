# Data Collection & Research Infrastructure for Prediction Market Trading

Prediction market trading strategies depend on reliable, high-quality data pipelines. This document covers the infrastructure layer: how to pull data from prediction markets and external economic sources, store it efficiently, validate it, and merge it into a research-ready dataset.

---

## A) Key Concepts

### API Authentication

**API Keys** are the simplest auth pattern. You include a key in a header or query parameter with each request. Prediction market APIs like Kalshi and Polymarket use API keys for higher rate limits. Store keys in environment variables, never hardcode them.

**OAuth 2.0** is used when an application acts on behalf of a user. Polymarket's trading API uses wallet signatures combined with API credentials. OAuth involves exchanging credentials for a short-lived access token, which expires and must be refreshed.

**JWT (JSON Web Tokens)** are stateless tokens issued after initial auth. The server validates the token on each request without querying a session store. Used extensively in modern web API auth flows.

**Best practice for prediction market APIs:**
- Use read-only public endpoints when possible (no auth needed for market data).
- Rotate keys if exposed.
- Use separate keys per environment (dev/staging/prod).
- Prefer POST-based auth over query param tokens to avoid URL logging.

### REST vs WebSocket

**REST API** follows a request-response cycle. Each call opens a connection, sends a request, receives a response, then closes. For prediction markets:
- Good for: fetching historical data, placing orders, querying market metadata.
- Limitation: not built for continuous streaming; polling is required for real-time updates.

**WebSocket** maintains a persistent, full-duplex connection. After an initial HTTP handshake the protocol upgrades to TCP, and both client and server can push messages freely. For prediction markets:
- Good for: live price feeds, order book updates, trade executions.
- Advantage: sub-second latency without polling overhead.
- Challenge: requires different error-handling logic since connections are long-lived.

**Polling strategies** for REST when WebSocket is unavailable:
- Short polling: fixed interval requests. Simple but wasteful if data rarely changes.
- Long polling: server holds the connection open until data is available or timeout. Reduces empty responses.
- Conditional requests: use `If-None-Match` (ETag) or `If-Modified-Since` headers. Server returns `304 Not Modified` when data unchanged, saving bandwidth and rate limit headroom.
- Exponential backoff: on 429 or 5xx responses, double the wait time between retries up to a maximum.

**Recommendation for prediction market trading:** Use WebSocket for live data, REST for historical queries and order management. Many platforms (Kalshi, Polymarket, OpticOdds) offer both.

### Rate Limiting

APIs enforce rate limits to prevent abuse. Common patterns:
- **Fixed window**: counts requests in a rolling time window (e.g., 100 req/min).
- **Token bucket**: allows bursts up to a limit, then refills at a steady rate.
- **Concurrent limit**: caps simultaneous connections.

Response to exceeding limits: HTTP `429 Too Many Requests` with a `Retry-After` header. Always respect this header rather than hammering the endpoint.

Polymarket's public endpoints generally do not require authentication and have generous but not unlimited rate limits. Kalshi's historical endpoints have separate limits from live endpoints.

### Historical Data Collection Pipelines

A prediction market data pipeline typically has these stages:

1. **Ingestion**: Pull data via REST API or subscribe via WebSocket. Record raw data immediately.
2. **Normalization**: Convert platform-specific schemas into a unified format (e.g., standardized timestamps, consistent column names, decimal probabilities vs. integer prices).
3. **Enrichment**: Join with external data (economic indicators, news sentiment, event metadata).
4. **Storage**: Write to a time-series store with appropriate partitioning and compression.
5. **Serving**: Expose data via an API or query layer for analysis and backtesting.

Tools for building pipelines in Python: `pandas` for manipulation, `SQLAlchemy` for database writes, `apache-airflow` or `dagster` for orchestration, `kafka` or `redis` for streaming buffers.

### Web Scraping (Ethical)

When APIs are insufficient, web scraping fills the gap. Key principles:

**robots.txt**: Always check `domain.com/robots.txt` before scraping. It tells you which paths are disallowed. While not legally binding, violating it signals bad faith and weakens legal defenses. Respect `Crawl-delay` directives.

**Legal and ethical guidelines**:
- Review the website's Terms of Service. Some explicitly prohibit scraping.
- Identify your scraper with a descriptive `User-Agent` string including contact info.
- Implement rate limiting: add delays (1-3 seconds) between requests.
- Only collect data you need. Avoid harvesting personal information.
- Use official APIs when available; scraping is a fallback.
- For prediction markets, scraping aggregator sites (rather than the platforms themselves) is often safer and more practical.

**Python tools by use case**:
- Static pages: `requests` + `Beautiful Soup`
- JavaScript-heavy pages: `Playwright` or `Selenium`
- Large-scale crawling: `Scrapy` (built-in crawling, rate limiting, pipelines)
- Modern hybrid: `Crawlee for Python`, `httpx` for async fetching

### Economic Data Feeds (FRED, BLS, Census)

Prediction markets are often driven by macroeconomic outcomes. Tying market data to economic indicators requires integration with government data feeds.

**FRED (Federal Reserve Economic Data)**:
- Free API at `fred.stlouisfed.org/docs/api/fred/`
- Requires free API key
- Python library: `fredapi` (`pip install fredapi`), or `FedFred` for async support
- Covers: GDP, CPI, unemployment, interest rates, housing starts, consumer sentiment, and thousands of US and international series
- Data revisions: ALFRED (Archival FRED) tracks historical revisions

**BLS (Bureau of Labor Statistics)**:
- Public Data API at `bls.gov/developers/api_python_v2.htm`
- Version 2.0 requires free registration; 500 requests/day vs 25 for v1.0
- Supports batch queries: up to 50 series per POST request
- Python: `bls-data` package converts responses to Pandas DataFrames

**US Census Bureau**:
- API for demographic and economic surveys: `api.census.gov`
- Useful for election-related markets (turnout, county-level results)

**Data freshness vs cost tradeoff**:
- Daily economic data (CPI, unemployment) is sufficient for most prediction market strategies.
- Real-time indicators (initial jobless claims, daily Treasury flows) update more frequently.
- API calls cost nothing in compute but use rate limit headroom; balance polling frequency against how quickly you need to react to new information.

### Data Normalization

Prediction market data from different platforms uses different conventions:

| Platform | Price convention | Timestamp format |
|---|---|---|
| Kalshi | Integer cents (0-100) | Unix epoch |
| Polymarket | Decimal probability (0.0-1.0) | ISO 8601 |
| Betfair | Decimal odds | Unix epoch |

Normalization steps:
- Convert all prices to decimal probabilities (0.0-1.0).
- Standardize timestamps to UTC, stored as `TIMESTAMP WITH TIME ZONE` in PostgreSQL.
- Normalize event identifiers to a consistent slug format.
- Map outcome names to canonical values (e.g., "YES" / "NO" vs "1" / "0").

### Time-Series Storage

**PostgreSQL (vanilla)**: Works for small to medium datasets. Not optimized for high-volume time-series ingestion. Requires manual partitioning for large datasets.

**TimescaleDB** (PostgreSQL extension): Best choice for trading data. Key features:
- **Hypertables**: auto-partitioned tables by time; behaves like a single table but scales horizontally.
- **Columnar compression**: 10-20x storage reduction; critical for historical tick data.
- **Continuous aggregates**: pre-compute rollups (e.g., 1-minute OHLCV from second-level ticks) as materialized views.
- **Full SQL**: leverage existing PostgreSQL knowledge and tooling.
- Recommended for: trading tick data, order book snapshots, multi-market analytics.

**InfluxDB**: Purpose-built time-series DB. Strengths:
- Very high write throughput for pure metrics.
- Native compression (TSM format).
- Built-in retention policies.
- Weakness: limited relational capabilities; no joins, custom query language (InfluxQL/Flux). Good for: simple real-time monitoring dashboards.

**Recommendation for prediction market research**: Use **TimescaleDB** as the primary store. It handles the relational complexity of joining market data with event metadata while providing the time-series performance needed for backtesting.

### Data Warehousing

For larger research operations, a data warehouse separates analytical workloads from transactional systems:
- **ClickHouse**: column-oriented, excellent for aggregations over billions of rows.
- **DuckDB**: embeddable analytical DB; great for local research on CSV/Parquet files.
- **Snowflake/BigQuery**: cloud data warehouses for team collaboration and large-scale backtests.

For a solo researcher or small team: start with TimescaleDB + TimescaleDB continuous aggregates. Graduate to a dedicated warehouse when query load impacts live trading performance.

### ETL Pipelines

ETL (Extract, Transform, Load) is the backbone of a research database:

- **Extract**: Pull from APIs (REST/WebSocket) or load from file exports (CSV, Parquet, S3).
- **Transform**: Clean, normalize, deduplicate, compute derived fields (e.g., implied probability from bid-ask mid, volume-weighted prices).
- **Load**: Write to TimescaleDB hypertables, update continuous aggregates.

Python ETL libraries:
- `pandas`: the workhorse for transformation logic.
- `SQLAlchemy`: database writes with connection pooling.
- `dagster`: modern orchestration with data quality checks, backfill support, and asset-based pipelines.
- `apache-airflow`: industry standard for workflow orchestration.
- `meltano`: ELT pipeline tool focused on data extraction from SaaS APIs.

### Data Quality Validation

Trading strategies are only as good as the data feeding them. Key validation checks:

**Completeness**:
- Detect gaps in time-series using `df.reindex()` and check for missing timestamps.
- Log gap duration and decide whether to backfill or discard.

**Outlier detection**:
- Z-score: flag values beyond 3 standard deviations.
- IQR method: values below `Q1 - 1.5 * IQR` or above `Q3 + 1.5 * IQR`.
- Isolation Forest (sklearn): detects multivariate anomalies in price/volume joint distributions.
- `PyOD` library: 30+ outlier detection algorithms in one package.

**Schema validation**:
- `pandera`: define DataFrame schemas with type and range checks; integrates with CI/CD.
- `ydata_quality`: comprehensive data quality reports.

**Missing data strategies for trading**:
- **Forward fill (ffill)**: carry last known price forward. Appropriate for illiquid markets with infrequent updates.
- **Interpolation**: linear or time-weighted interpolation between known values.
- **Drop**: if a market resolves and is inactive for extended periods, consider dropping it from certain analyses.

### Merging Market Data with External Sources

Prediction markets respond to real-world events. Correlating market prices with external signals strengthens research:

1. **Join on event date**: align market resolution dates with economic release calendars.
2. **Sentiment features**: use news headline embeddings as features in market direction models.
3. **Feature store pattern**: maintain a separate table of external features (FRED series, poll aggregates) that can be joined to market data via a shared date or event key.
4. **Late binding**: external data often arrives with a lag (e.g., official GDP revision). Use late-binding views that recompute joins when updated data arrives rather than overwriting raw data.

### Backfill Strategies

Backfilling populates historical data when a pipeline is new or recovering from failure.

Key strategies:
- **Unique constraints**: enforce unique (market_id, timestamp) to prevent duplicate inserts on re-runs.
- **Idempotent writes**: design pipeline runs so re-executing produces the same result.
- **Batch processing**: fetch data in chunks (e.g., 90-day windows) to respect API pagination and rate limits.
- **Pre-backfill validation**: check data type compatibility before inserting into schema; schema drift is a common pipeline failure cause.
- **Atomic merges**: use `INSERT ... ON CONFLICT DO UPDATE` (PostgreSQL upsert) to handle both inserts and updates cleanly.
- **Off-peak execution**: schedule backfills during hours when API rate limits are less contended.

**Kalshi historical data**: approximately last 3 months available via dedicated historical endpoints. Older data may require alternative sources.

**Polymarket historical data**: `PolymarketData` provides complete historical datasets including 1-minute order book snapshots via API, S3, or Python SDK. Third-party services like `Bitquery` provide GraphQL access to on-chain Polymarket data (typically ~7-day retention for realtime datasets).

### Event Cataloging and Market Metadata

A well-structured event catalog enables downstream research:

- **Event resolution criteria**: unambiguous rules for how the market resolves. This is critical for backtesting, as ambiguous criteria lead to disputed outcomes.
- **Resolution source**: the oracle or data provider that verifies the outcome (e.g., "Associated Press", "CFTC", "Official NCAA").
- **Categorization**: tag events by type (election, economic indicator, weather, sports) and region.
- **Temporal metadata**: market open/close times, trading halt windows, resolution date vs. event date.
- **Market structure**: binary vs. categorical vs. scalar markets; each requires different analysis approaches.

Schema for an event catalog table:
```sql
CREATE TABLE events (
    event_id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    category VARCHAR(100),
    resolution_criteria TEXT NOT NULL,
    resolution_source TEXT,
    start_date TIMESTAMPTZ NOT NULL,
    end_date TIMESTAMPTZ NOT NULL,
    resolution_date TIMESTAMPTZ,
    status VARCHAR(50) NOT NULL DEFAULT 'active',
    tags JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## B) Learning Resources

### 1. Polymarket API Documentation
**Type:** Official API docs | **URL:** https://docs.polymarket.com/api-reference/introduction
Covers Gamma API (market metadata), Data API (user data), CLOB API (order book and historical prices via `/prices-history`), and WebSocket API. Public endpoints require no auth. The `/prices-history` endpoint is the primary tool for building historical price datasets with filters for market, time range, and aggregation interval.

### 2. Kalshi API Documentation
**Type:** Official API docs | **URL:** https://docs.kalshi.com/getting_started/historical_data
REST API docs covering market data, order management, and WebSocket streaming. Historical data is partitioned separately from live data and accessible through dedicated endpoints. Public endpoints available for market data exploration. Includes Python integration examples with pandas.

### 3. FRED API Official Documentation
**Type:** Official API docs | **URL:** https://fred.stlouisfed.org/docs/api/fred/
Complete reference for the Federal Reserve Economic Data API. Free API key registration. Covers all endpoint categories: series observations, categories, releases, sources. Essential for pulling US macroeconomic indicators to correlate with prediction market prices.

### 4. "Python for Data Analysis" (Wes McKinney)
**Type:** Book | **URL:** https://wesmckinney.com/book/
The definitive reference on pandas, NumPy, and data manipulation in Python. Chapters 10-12 cover time-series handling, which directly applies to building OHLCV datasets from prediction market price feeds. Available free online.

### 5. Scrapy Documentation
**Type:** Official docs + tutorial | **URL:** https://scrapy.org/
Full-featured Python web scraping framework. Built-in crawling, request scheduling, rate limiting, middleware, and data pipelines. Essential when APIs are insufficient and you need to collect data from prediction market news sites, polling aggregators, or forum discussions. The tutorial walks through building a complete scraper.

### 6. TimescaleDB Documentation
**Type:** Official docs | **URL:** https://docs.timescale.com/
Installation, hypertables, compression, continuous aggregates, and user-defined procedures. The "Getting Started" guide covers hypertable creation and shows how continuous aggregates dramatically speed up aggregations over historical data. The hypertable-by-symbol partitioning pattern is directly applicable to multi-market trading data.

### 7. Dagster Documentation — Data Pipelines with Python
**Type:** Official docs + tutorial | **URL:** https://dagster.io/guides/data-pipelines-with-python-6-frameworks-quick-tutorial
Modern Python-first orchestration framework. Asset-based pipelines let you define data dependencies explicitly; backfill support is first-class. Better suited for research pipelines than Airflow for teams that want type safety and testable data assets.

### 8. "Designing Data-Intensive Applications" (Kleppmann)
**Type:** Book | **URL:** https://dataintensive.net/
Covers data modeling, storage engines (B-tree vs LSM-tree), data warehousing, batch vs. stream processing, and consistency models. Chapters 3-8 provide the conceptual foundation for building robust data infrastructure. Available as audiobook. Not free but considered essential reading for anyone building data systems.

### 9. BLS API Python Integration Guide
**Type:** Official developer guide | **URL:** https://www.bls.gov/developers/api_python_v2.htm
Official BLS instructions for using their Public Data API v2 with Python. Covers registration, making POST requests, handling the JSON response format, and batch queries for multiple series. The companion `bls-data` package on PyPI automates the DataFrame conversion.

### 10. PyOD (Python Outlier Detection) Documentation
**Type:** Open source library docs | **URL:** https://www.pyod.ini.org/ (project page: https://github.com/yzhao062/pyod)
Comprehensive toolkit with 30+ outlier detection algorithms including Isolation Forest, LOF, KNN, and neural network-based methods. Includes a unified API and examples for detecting anomalies in multivariate financial data. Install via `pip install pyod`.

---

## C) Learning Path

### Phase 1: Foundation (Weeks 1-2)

**Goal**: Pull live and historical data from a prediction market API and store it in a local database.

| Step | Topic | Time | Resources |
|---|---|---|---|
| 1 | API fundamentals: REST vs WebSocket, HTTP methods, headers, status codes | 3 hours | REST vs WebSocket section above + https://restfulapi.net |
| 2 | Get a Polymarket API key (free) and explore `/prices-history` endpoint | 2 hours | https://docs.polymarket.com/api-reference/markets/get-prices-history |
| 3 | Write a Python script using `requests` to fetch 30 days of historical prices for one market and save to CSV | 3 hours | Polymarket docs above |
| 4 | Install PostgreSQL + TimescaleDB; create a hypertable for price data | 3 hours | https://docs.timescale.com/ |
| 5 | Modify script to upsert data into TimescaleDB instead of CSV | 3 hours | SQLAlchemy + psycopg2 docs |
| 6 | Set up a WebSocket subscription for live price updates and write a basic streamer that writes to the DB | 4 hours | Polymarket WebSocket docs |

**Cumulative time**: ~18 hours

### Phase 2: External Data Integration (Weeks 3-4)

**Goal**: Automatically fetch economic indicators and merge them with market price data.

| Step | Topic | Time | Resources |
|---|---|---|---|
| 1 | Register for FRED API key; install `fredapi`; pull CPI and unemployment rate series | 3 hours | https://pypi.org/project/fredapi/ |
| 2 | Register for BLS API; install `bls-data`; pull initial jobless claims | 2 hours | https://www.bls.gov/developers/api_python_v2.htm |
| 3 | Design a PostgreSQL schema with a `macro_indicators` table and `market_prices` table joined on date | 3 hours | Prediction market schema above |
| 4 | Write a daily ETL script that pulls new FRED/BLS data and upserts into the DB | 4 hours | ETL section above |
| 5 | Write a Jupyter notebook that joins market prices with macro indicators and produces a simple correlation analysis | 4 hours | Pandas merge/join documentation |

**Cumulative time**: ~16 hours

### Phase 3: Data Quality and Reliability (Week 5)

**Goal**: Build a pipeline that validates, cleans, and handles failures gracefully.

| Step | Topic | Time | Resources |
|---|---|---|---|
| 1 | Add completeness checks: detect gaps in price series, log missing timestamps | 3 hours | pandas reindex + isnull |
| 2 | Implement outlier detection on price data using IQR and Z-score | 3 hours | PyOD + https://github.com/yzhao062/pyod |
| 3 | Add retry logic with exponential backoff to API calls | 2 hours | Python `tenacity` library |
| 4 | Write a backfill script that handles the full historical range for a market in 90-day chunks | 4 hours | Backfill strategies section above |
| 5 | Add `pandera` schema validation to your pipeline to catch type/dtype mismatches | 3 hours | https://pandera.readthedocs.io/ |

**Cumulative time**: ~15 hours

### Phase 4: Production Pipeline (Weeks 6-7)

**Goal**: Orchestrate everything into a reliable, monitored pipeline.

| Step | Topic | Time | Resources |
|---|---|---|---|
| 1 | Install Dagster; define assets for market data, macro data, and joined datasets | 4 hours | https://dagster.io/guides/data-pipelines-with-python-6-frameworks-quick-tutorial |
| 2 | Configure Dagster schedules to run ingestion daily and backfill on demand | 3 hours | Dagster scheduling docs |
| 3 | Set up Grafana or Superset dashboards over TimescaleDB for price visualization | 4 hours | Grafana + TimescaleDB integration docs |
| 4 | Implement alerting on pipeline failures (missing data > X hours, outlier spike) | 3 hours | Dagster alerts + PagerDuty/Slack webhook |
| 5 | Write a data dictionary / README documenting the schema, lineage, and freshness of each table | 2 hours | Standard data docs practice |

**Cumulative time**: ~16 hours

**Total estimated time**: ~65 hours (roughly 9-10 weeks at 7 hours/week, or 5 weeks full-time)

---

## D) Practical Exercises

### Exercise 1: Build a Polymarket Price History Collector

**Goal**: Collect 90 days of historical price data for 10 Polymarkets and store in TimescaleDB.

**Instructions**:
1. Choose 10 active Polymarkets across different categories (politics, economics, sports).
2. Use the `/prices-history` endpoint: `GET https://clob.polymarket.com/prices-history?market_id=<id>&interval=1d`
3. Write a Python script that iterates over your market list, fetches data, and upserts into a `market_prices` hypertable with columns: `market_id`, `timestamp`, `outcome_prices` (JSONB), `volume`.
4. Schedule it to run daily via cron or Dagster.
5. Verify with a query: count of records per market, date range coverage, gap detection.

**Acceptance**: The pipeline runs without manual intervention, handles API errors gracefully, and produces a queryable dataset with 90+ days of history for all 10 markets.

---

### Exercise 2: Merge Market Data with FRED Economic Indicators

**Goal**: Build a combined dataset that correlates prediction market probabilities with macroeconomic releases.

**Instructions**:
1. Pull CPI (series ID: CPIAUCSL) and unemployment rate (series ID: UNRATE) from FRED using `fredapi`.
2. Store them in a `macro_indicators` table with columns: `series_id`, `date`, `value`, `updated_at`.
3. For a set of economic-event markets (e.g., "Will CPI exceed X% by Y date?"), join the market's price time series with the corresponding macro series.
4. Compute rolling 7-day and 30-day correlations between market probability and the macro indicator.
5. Visualize the relationship in a plot (matplotlib or Plotly).

**Acceptance**: A Jupyter notebook that shows a correlation chart with clear methodology documented. The joined dataset is persisted in TimescaleDB for future analysis.

---

### Exercise 3: Build an Ethical Web Scraper for Poll Aggregators

**Goal**: Scrape polling data from a public aggregator (e.g., FiveThirtyEight or similar) to enrich election market analysis.

**Instructions**:
1. Identify a public polling data source. Check `robots.txt` and the site's Terms of Service.
2. Use `Scrapy` to build a spider that extracts: poll date, candidate/choice, poll result, sample size, pollster.
3. Store scraped data in a `poll_data` table with source, URL, and scraped_at timestamp.
4. Implement polite scraping: set `Crawl-delay` from robots.txt, add 2-second delay between requests, use a descriptive User-Agent.
5. Join poll data with your Polymarket/Kalshi election market prices by event date.

**Acceptance**: The spider runs without generating errors, respects robots.txt, and produces a clean CSV/DB table of poll results that can be joined to market data.

---

### Exercise 4: Build a Backfill Pipeline with Idempotent Upserts

**Goal**: Demonstrate reliable historical data recovery when backfilling after a pipeline outage.

**Instructions**:
1. Simulate a 7-day pipeline outage by deleting the most recent 7 days of records from your `market_prices` table.
2. Write a backfill script that:
   - Queries the API for the missing date range per market
   - Uses PostgreSQL `INSERT ... ON CONFLICT (market_id, timestamp) DO UPDATE` for idempotent writes
   - Logs each run with start time, end time, records written, and duplicates skipped
3. Run the backfill script and verify all deleted records are recovered without duplicates.
4. Add a Dagster backfill asset that can be triggered for arbitrary date ranges.

**Acceptance**: After backfill, the total row count equals the original row count + deleted rows, with zero duplicates (enforced by unique constraint + upsert logic).

---

### Exercise 5: Data Quality Dashboard

**Goal**: Build a monitoring layer that surfaces data quality issues before they contaminate research.

**Instructions**:
1. Define a set of data quality checks on your `market_prices` table:
   - Null probability values (0.0 < p < 1.0 is always expected)
   - Duplicate (market_id, timestamp) pairs
   - Stale data: no update in > 6 hours for active markets
   - Price jump > 3 standard deviations from 30-day rolling mean
2. Implement checks as Python functions using `pandas` and `psycopg2`.
3. Run checks after each pipeline run and log results.
4. Create a simple Grafana dashboard (or Streamlit app) showing: record count over time, null count per market, last update timestamp per market, outlier flag count.

**Acceptance**: The dashboard runs on a 1-hour refresh cycle and flags at least one data quality issue in your current dataset that you then fix.

---

## Summary: Acceptance Criteria Checklist

This domain document supports a research infrastructure that satisfies the overall workflow acceptance criteria:

| Criterion | How This Doc Addresses It |
|---|---|
| Has a working pipeline collecting historical prediction market data | Exercises 1 and 4 cover Polymarket API ingestion, TimescaleDB storage, and backfill with upsert logic |
| Can merge market data with external sources | Exercise 2 covers FRED/BLS integration; the event cataloging section covers join keys and late-binding patterns |
| Has 3+ months of stored data | The backfill strategy section explains how to accumulate historical data; PolymarketData and Kalshi historical endpoints provide the source data |

## Quick-Reference Cheat Sheet

```
# Install core packages
pip install requests pandas sqlalchemy psycopg2-binary \
  timescaledb fredapi bls-data pyod pandera scrapy dagster

# Quick FRED fetch
from fredapi import Fred
fred = Fred(api_key_file='~/.fred_api_key')
cpi = fred.get_series('CPIAUCSL')

# Quick Polymarket prices-history
import requests
url = "https://clob.polymarket.com/prices-history"
params = {"market_id": "12345", "interval": "1d"}
r = requests.get(url, params=params).json()

# TimescaleDB hypertable (run once)
CREATE TABLE market_prices (
    time        TIMESTAMPTZ NOT NULL,
    market_id   TEXT NOT NULL,
    yes_price   NUMERIC(8, 4),
    no_price    NUMERIC(8, 4),
    volume      NUMERIC(18, 2)
);
SELECT create_hypertable('market_prices', 'time', chunk_time_interval => '1 day');
CREATE UNIQUE INDEX ON market_prices (market_id, time);

# Idempotent upsert
INSERT INTO market_prices (time, market_id, yes_price, no_price, volume)
VALUES ('2026-01-15', 'mkt-123', 0.65, 0.35, 10000)
ON CONFLICT (market_id, time) DO UPDATE SET
    yes_price = EXCLUDED.yes_price,
    no_price  = EXCLUDED.no_price,
    volume    = EXCLUDED.volume;
```

---

*Last updated: 2026-04-01*
*Next steps: Integrate Kalshi API data alongside Polymarket; add WebSocket-based live price streamer; explore Bitquery GraphQL API for extended Polymarket history*
