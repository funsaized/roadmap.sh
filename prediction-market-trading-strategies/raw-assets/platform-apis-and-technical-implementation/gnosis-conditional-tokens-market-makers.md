# Conditional Tokens Market Makers

## Metadata
- **URL:** https://github.com/gnosis/conditional-tokens-market-makers
- **Source:** GitHub (Gnosis)
- **Type:** code
- **Author:** Gnosis
- **Date Scraped:** 2026-04-01
- **Authority:** high
- **Relevance:** high

## Content

## Overview

Automated Market Maker (AMM) smart contracts for Conditional Tokens Markets. All smart contracts are released under the LGPL 3.0 license. These contracts implement various market maker strategies for the Gnosis Conditional Tokens Framework.

## About

This repository contains smart contract implementations for different automated market maker strategies designed specifically for prediction markets and conditional token markets. The core insight is that standard AMMs (like constant product market makers) are poorly suited for binary outcome tokens, which resolve to either $0 or $1 at a known future time.

## Repository Structure

The repository is organized into several key directories:

- **contracts/**: Core smart contract implementations for various AMM strategies
- **docs/**: Documentation and mathematical descriptions of the market maker mechanisms
- **migrations/**: Migration scripts for deploying contracts
- **test/**: Comprehensive test suites for all contracts
- **.eslintrc.js**: JavaScript linting configuration
- **truffle.js**: Truffle framework configuration
- **package.json**: Node.js dependencies and scripts

## Key Market Maker Strategies

### Fixed Product Market Maker (FPMM)

The FPMM is a simple extension of the constant product formula adapted for conditional tokens. It maintains the invariant that the product of token supplies remains constant, but adds fee collection mechanisms.

### LMSR Market Maker

The Logarithmic Market Scoring Rule (LMSR) implementation from Robin Hanson. This market maker provides liquidity based on the softmax of outstanding shares, creating natural price discovery.

### Fixed Odds Market Maker

A market maker that allows setting fixed odds for specific outcomes, similar to traditional sports betting. Useful for markets where specific probability estimates are known in advance.

## Architecture

The contracts follow a modular architecture:

1. **Oracle Interface**: Contracts interact with oracles to determine market resolution
2. **Conditional Tokens**: The Gnosis Conditional Tokens contracts handle token minting and redemption
3. **Market Maker Logic**: Separate contracts implement different pricing algorithms
4. **Fee Management**: Integrated fee collection and distribution

## Documentation

The `docs/` directory contains detailed explanations of the mathematical foundations of each market maker, including derivations of pricing formulas, proofs of convergence, and analysis of worst-case loss bounds.

## Key Excerpts

1. "Standard AMMs like constant product (x × y = k) are poorly suited for binary outcome tokens which resolve to either $0 or $1 at a known future time."

2. "The FPMM maintains the invariant that the product of token supplies remains constant, but adds fee collection mechanisms."

## Scrape Notes
- Content completeness: partial (GitHub README only, no deep code content)
- Rich documentation directory exists with mathematical descriptions
- Primary value is architectural understanding of AMM designs for conditional tokens
