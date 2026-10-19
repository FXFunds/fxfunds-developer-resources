# Integration Guide

## USDT Networks

| Network | Key | USDT contract / jetton master | Decimals | Fee token | Default confirmations | Explorer |
|---------|-----|-------------------------------|----------|-----------|-----------------------|----------|
| Ethereum (ERC20) | `erc20` | `0xdAC17F958D2ee523a2206206994597C13D831ec7` | 6 | ETH | 12 | https://etherscan.io |
| Tron (TRC20) | `trc20` | `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t` | 6 | TRX (energy and bandwidth) | 19 | https://tronscan.org |
| TON | `ton` | `EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs` | 6 | TON | 1 | https://tonviewer.com |

| Network | Address format | Hash format |
|---------|----------------|-------------|
| Ethereum (ERC20) | 0x + 40 hex | 0x + 64 hex |
| Tron (TRC20) | T + 33 Base58 | 64 hex |
| TON | EQ/UQ + 46 Base64url, or raw 0: + 64 hex | 64 hex or 44 Base64 |

Default confirmations are the reference defaults used by the FXFunds open-source tools. They are configurable and are not FXFunds platform rules.

## Typical Flow

1. Validate the request: [`@fxfunds/deposit-withdrawal-guide`](https://www.npmjs.com/package/@fxfunds/deposit-withdrawal-guide) checks method, network, amount and destination.
2. Check address and hash formats with this package or [`@fxfunds/blockchain-technology`](https://www.npmjs.com/package/@fxfunds/blockchain-technology).
3. Fetch the transaction from your own node or explorer API, then confirm the token contract, recipient and amount.
4. Match it to the payment request with [`@fxfunds/stablecoin-payments`](https://www.npmjs.com/package/@fxfunds/stablecoin-payments) until it reaches your confirmation threshold.
5. Record the status change and reconcile.

## Security

- Never put private keys, seed phrases, API secrets or account credentials in code, issues or examples.
- Store publishing tokens only in GitHub Actions secrets, or use trusted publishing.
- Treat every address and amount from users as untrusted input.
- Confirm the token contract on-chain; look-alike tokens can share the USDT name.

## What Is Not Available

No official FXFunds trading, account or payment API was found on publicly readable pages at the last check (2026-10-19). Do not build against unofficial endpoints. If FXFunds publishes an API, it will be added here with its official URL.
