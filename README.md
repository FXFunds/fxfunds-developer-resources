# FXFunds — Developer Resources 🛠️

[![npm version](https://img.shields.io/npm/v/@fxfunds/developer-resources.svg)](https://www.npmjs.com/package/@fxfunds/developer-resources)
[![PyPI version](https://img.shields.io/pypi/v/fxfunds-developer-resources.svg)](https://pypi.org/project/fxfunds-developer-resources/)
[![Tests](https://github.com/FXFunds/fxfunds-developer-resources/actions/workflows/tests.yml/badge.svg)](https://github.com/FXFunds/fxfunds-developer-resources/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23482932.svg)](https://doi.org/10.5281/zenodo.23482932)
[![Docs](https://readthedocs.org/projects/fxfunds-developer-resources/badge/?version=latest)](https://fxfunds-developer-resources.readthedocs.io)

FXFunds Developer Resources provides technical documentation, approved development resources, API references, code examples and integration guidance for developers working with FXFunds-related tools and technologies.

**Official Website:** https://fxfunds.com/

> **Scope:** This repository covers FXFunds' **open-source** tools. They are standalone libraries that never hold private keys, sign transactions or move funds, and they **do not connect to FXFunds accounts**. No official FXFunds trading or account API is documented.

## Approved Packages

Every package below was confirmed live at version 1.0.0 on npm and PyPI on 2026-10-19.

| Project | npm | PyPI | CLI | DOI |
|---------|-----|------|-----|-----|
| [FXFunds Blockchain Technology](https://github.com/FXFunds/fxfunds-blockchain-technology) | [`@fxfunds/blockchain-technology`](https://www.npmjs.com/package/@fxfunds/blockchain-technology) | [`fxfunds-blockchain-technology`](https://pypi.org/project/fxfunds-blockchain-technology/) | `fxfunds-blockchain` | [23424646](https://doi.org/10.5281/zenodo.23424646) |
| [FXFunds Stablecoin Payments](https://github.com/FXFunds/fxfunds-stablecoin-payments) | [`@fxfunds/stablecoin-payments`](https://www.npmjs.com/package/@fxfunds/stablecoin-payments) | [`fxfunds-stablecoin-payments`](https://pypi.org/project/fxfunds-stablecoin-payments/) | `fxfunds-payments` | [23463811](https://doi.org/10.5281/zenodo.23463811) |
| [FXFunds Deposit and Withdrawal Guide](https://github.com/FXFunds/fxfunds-deposit-withdrawal-guide) | [`@fxfunds/deposit-withdrawal-guide`](https://www.npmjs.com/package/@fxfunds/deposit-withdrawal-guide) | [`fxfunds-deposit-withdrawal-guide`](https://pypi.org/project/fxfunds-deposit-withdrawal-guide/) | `fxfunds-dw` | [23464782](https://doi.org/10.5281/zenodo.23464782) |
| [FXFunds Platform FAQ](https://github.com/FXFunds/fxfunds-platform-faq) | [`@fxfunds/platform-faq`](https://www.npmjs.com/package/@fxfunds/platform-faq) | [`fxfunds-platform-faq`](https://pypi.org/project/fxfunds-platform-faq/) | `fxfunds-faq` | [23467990](https://doi.org/10.5281/zenodo.23467990) |
| [FXFunds Risk Disclosure Bot](https://github.com/FXFunds/fxfunds-risk-disclosures) | [`@fxfunds/risk-disclosures`](https://www.npmjs.com/package/@fxfunds/risk-disclosures) | [`fxfunds-risk-disclosures`](https://pypi.org/project/fxfunds-risk-disclosures/) | `fxfunds-risk` | [23470752](https://doi.org/10.5281/zenodo.23470752) |

## API Reference

| Project | Node.js API | Python API |
|---------|-------------|------------|
| FXFunds Blockchain Technology | `analyzeTransaction, toCSV, statusFor, NETWORKS` | `analyze_transaction, to_csv, status_for, NETWORKS` |
| FXFunds Stablecoin Payments | `verifyPayment, PaymentLedger, NETWORKS` | `verify_payment, PaymentLedger, NETWORKS` |
| FXFunds Deposit and Withdrawal Guide | `RequestTracker, validateRequest, GUIDE, TRANSITIONS, METHODS` | `RequestTracker, validate_request, GUIDE, TRANSITIONS, METHODS` |
| FXFunds Platform FAQ | `all, categories, byCategory, byStatus, get, search, format` | `all_questions, categories, by_category, by_status, get, search, format_answer` |
| FXFunds Risk Disclosure Bot | `documents, get, byStatus, byCategory, missing, summary, risks, risk, documentsForRisk, format` | `documents, get, by_status, by_category, missing, summary, risks, risk, documents_for_risk, format_document` |

Details for each function: [docs/api.md](docs/api.md).

## USDT Network Reference

| Network | Key | USDT contract / jetton master | Decimals | Fee token | Default confirmations | Explorer |
|---------|-----|-------------------------------|----------|-----------|-----------------------|----------|
| Ethereum (ERC20) | `erc20` | `0xdAC17F958D2ee523a2206206994597C13D831ec7` | 6 | ETH | 12 | https://etherscan.io |
| Tron (TRC20) | `trc20` | `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t` | 6 | TRX (energy and bandwidth) | 19 | https://tronscan.org |
| TON | `ton` | `EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs` | 6 | TON | 1 | https://tonviewer.com |

The packages check **formats** only. Your integration must confirm on-chain that a transfer is of the genuine USDT contract and to the right address. Guide: [docs/integration.md](docs/integration.md).

## This Package: Catalog and Validators

`@fxfunds/developer-resources` / `fxfunds-developer-resources` bundles the catalog above with address and transaction-hash format checks. It works offline.

```bash
npm install @fxfunds/developer-resources
pip install fxfunds-developer-resources
```

```bash
fxfunds-dev                                   # summary
fxfunds-dev projects                          # all FXFunds packages
fxfunds-dev project risk-disclosures          # one project, with install commands
fxfunds-dev networks                          # USDT networks
fxfunds-dev check-address trc20 TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
fxfunds-dev check-tx erc20 0x<64 hex> --json
```

```typescript
import { projects, network, isValidAddress, installCommands } from "@fxfunds/developer-resources";

console.log(projects().map((p) => p.npm));
console.log(network("tron")?.usdt_contract);
console.log(isValidAddress("erc20", "0xdAC17F958D2ee523a2206206994597C13D831ec7")); // true
console.log(installCommands("platform-faq"));
```

```python
from fxfunds_developer_resources import projects, network, is_valid_address, install_commands

print([p["pypi"] for p in projects()])
print(network("tron")["usdt_contract"])
print(is_valid_address("erc20", "0xdAC17F958D2ee523a2206206994597C13D831ec7"))  # True
print(install_commands("platform-faq"))
```

## Dataset

| File | Rows | Contents |
|------|------|----------|
| [`dataset/fxfunds_developer_packages.csv`](dataset/fxfunds_developer_packages.csv) | 10 | Every FXFunds npm and PyPI package with install command, import name, CLI, API, repository and DOI |
| [`dataset/fxfunds_usdt_networks.csv`](dataset/fxfunds_usdt_networks.csv) | 3 | USDT contract, decimals, fees, confirmations and address/hash patterns for each network |

Published on [Hugging Face](https://huggingface.co/datasets/FXFunds/developer-resources) and [Kaggle](https://www.kaggle.com/datasets/fxfunds/developer-resources). Notebook: [`kaggle/notebook.ipynb`](kaggle/notebook.ipynb). Both CSVs are generated from [`fxfunds_developer_resources/catalog.json`](fxfunds_developer_resources/catalog.json), and the tests check they match.

## Development Principles

- Use accurate installation commands and version requirements.
- Keep examples consistent with the released software.
- Never publish API credentials, private keys, seed phrases or account data.
- Clearly label experimental or unsupported features.
- Do not claim official approval or endorsement without authorisation.

## Links

| Platform | URL |
|----------|-----|
| Website | https://fxfunds.com/ |
| GitHub | https://github.com/FXFunds/fxfunds-developer-resources |
| NPM | https://www.npmjs.com/package/@fxfunds/developer-resources |
| PyPI | https://pypi.org/project/fxfunds-developer-resources/ |
| Hugging Face | https://huggingface.co/datasets/FXFunds/developer-resources |
| Kaggle | https://www.kaggle.com/datasets/fxfunds/developer-resources |
| Zenodo | https://zenodo.org/records/23482932 |
| Docs | https://fxfunds-developer-resources.readthedocs.io |
| Quora | https://fxfunds.quora.com/ |
| Pinterest | https://www.pinterest.com/fxfunds_1/ |
| Medium | https://medium.com/@FX_Funds |

## Disclaimer

These resources are for development and education. They are not financial advice and do not guarantee platform performance, transaction completion or regulatory status. Verify official information on https://fxfunds.com/.

## License

MIT — [FXFunds](https://fxfunds.com/)
