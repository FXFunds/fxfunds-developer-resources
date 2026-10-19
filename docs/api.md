# API Reference

All packages are version 1.0.0, run on Node.js 18+ and Python 3.8+ (3.9+ for the FAQ and risk packages), and make no calls to FXFunds systems.

## FXFunds Developer Resources (this package)

| Node.js | Python | Returns |
|---------|--------|---------|
| `projects()` | `projects()` | Every FXFunds project in the catalog |
| `project(id)` | `project(id)` | One project by ID, npm name or PyPI name |
| `networks()` | `networks()` | USDT networks |
| `network(key)` | `network(key)` | One network by key or alias (`erc20`/`ethereum`, `trc20`/`tron`, `ton`) |
| `isValidAddress(net, addr)` | `is_valid_address(net, addr)` | Address format check |
| `isValidTxHash(net, hash)` | `is_valid_tx_hash(net, hash)` | Transaction-hash format check |
| `installCommands(id)` | `install_commands(id)` | npm and pip install commands |
| `CATALOG`, `LAST_CHECKED` | same | Raw data |

Format checks do not prove a transfer happened or that a token is genuine USDT.

## FXFunds Blockchain Technology

Read-only USDT transaction signal analyzer: address and hash checks, confirmation depth, fee efficiency, settlement speed and data completeness scores.

| | Node.js | Python |
|---|---|---|
| Install | `npm install @fxfunds/blockchain-technology` | `pip install fxfunds-blockchain-technology` |
| Import | `require("@fxfunds/blockchain-technology")` | `import fxfunds_blockchain_technology` |
| API | `analyzeTransaction, toCSV, statusFor, NETWORKS` | `analyze_transaction, to_csv, status_for, NETWORKS` |
| CLI | `fxfunds-blockchain` | `fxfunds-blockchain` |

Repository: https://github.com/FXFunds/fxfunds-blockchain-technology · DOI: [10.5281/zenodo.23424646](https://doi.org/10.5281/zenodo.23424646)

## FXFunds Stablecoin Payments

Read-only USDT payment verification: matches transactions to payment requests, tracks confirmations, blocks duplicate credits and keeps a ledger.

| | Node.js | Python |
|---|---|---|
| Install | `npm install @fxfunds/stablecoin-payments` | `pip install fxfunds-stablecoin-payments` |
| Import | `require("@fxfunds/stablecoin-payments")` | `import fxfunds_stablecoin_payments` |
| API | `verifyPayment, PaymentLedger, NETWORKS` | `verify_payment, PaymentLedger, NETWORKS` |
| CLI | `fxfunds-payments` | `fxfunds-payments` |

Repository: https://github.com/FXFunds/fxfunds-stablecoin-payments · DOI: [10.5281/zenodo.23463811](https://doi.org/10.5281/zenodo.23463811)

## FXFunds Deposit and Withdrawal Guide

Deposit and withdrawal tracking: request validation, status flow, plain-language status guide, audit trail and reconciliation. Tracking only.

| | Node.js | Python |
|---|---|---|
| Install | `npm install @fxfunds/deposit-withdrawal-guide` | `pip install fxfunds-deposit-withdrawal-guide` |
| Import | `require("@fxfunds/deposit-withdrawal-guide")` | `import fxfunds_deposit_withdrawal_guide` |
| API | `RequestTracker, validateRequest, GUIDE, TRANSITIONS, METHODS` | `RequestTracker, validate_request, GUIDE, TRANSITIONS, METHODS` |
| CLI | `fxfunds-dw` | `fxfunds-dw` |

Repository: https://github.com/FXFunds/fxfunds-deposit-withdrawal-guide · DOI: [10.5281/zenodo.23464782](https://doi.org/10.5281/zenodo.23464782)

## FXFunds Platform FAQ

24 platform questions with verification labels, sources and last-checked dates; offline keyword search.

| | Node.js | Python |
|---|---|---|
| Install | `npm install @fxfunds/platform-faq` | `pip install fxfunds-platform-faq` |
| Import | `require("@fxfunds/platform-faq")` | `import fxfunds_platform_faq` |
| API | `all, categories, byCategory, byStatus, get, search, format` | `all_questions, categories, by_category, by_status, get, search, format_answer` |
| CLI | `fxfunds-faq` | `fxfunds-faq` |

Repository: https://github.com/FXFunds/fxfunds-platform-faq · DOI: [10.5281/zenodo.23467990](https://doi.org/10.5281/zenodo.23467990)

## FXFunds Risk Disclosure Bot

Official document register and risk categories: which risk disclosures and legal documents have been located and what to check for each risk.

| | Node.js | Python |
|---|---|---|
| Install | `npm install @fxfunds/risk-disclosures` | `pip install fxfunds-risk-disclosures` |
| Import | `require("@fxfunds/risk-disclosures")` | `import fxfunds_risk_disclosures` |
| API | `documents, get, byStatus, byCategory, missing, summary, risks, risk, documentsForRisk, format` | `documents, get, by_status, by_category, missing, summary, risks, risk, documents_for_risk, format_document` |
| CLI | `fxfunds-risk` | `fxfunds-risk` |

Repository: https://github.com/FXFunds/fxfunds-risk-disclosures · DOI: [10.5281/zenodo.23470752](https://doi.org/10.5281/zenodo.23470752)
