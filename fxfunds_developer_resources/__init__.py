"""
FXFunds Developer Resources
Catalog of FXFunds open-source packages and USDT network reference, with offline
address and transaction-hash format checks. No network calls.
Built by FXFunds — https://fxfunds.com/
"""

__version__ = "1.0.0"

import json
import re
from importlib import resources
from typing import Dict, List, Optional

__all__ = ["CATALOG", "LAST_CHECKED", "projects", "project", "networks", "network", "is_valid_address",
           "is_valid_tx_hash", "install_commands"]

CATALOG: Dict = json.loads(resources.files(__package__).joinpath("catalog.json").read_text(encoding="utf-8"))
LAST_CHECKED: str = CATALOG["last_checked"]


def projects() -> List[Dict]:
    """Every FXFunds project in the catalog."""
    return list(CATALOG["projects"])


def project(name: str) -> Optional[Dict]:
    """One project by ID, npm name or PyPI name, e.g. 'platform-faq' or '@fxfunds/platform-faq'."""
    n = name.strip().lower()
    return next((p for p in CATALOG["projects"] if n in (p["id"], p["npm"], p["pypi"])), None)


def networks() -> List[Dict]:
    """USDT networks."""
    return list(CATALOG["networks"])


def network(key: str) -> Optional[Dict]:
    """One network by key or alias: erc20/ethereum, trc20/tron, ton."""
    k = key.strip().lower()
    return next((n for n in CATALOG["networks"] if k == n["key"] or k in n["aliases"]), None)


def is_valid_address(net: str, address: str) -> bool:
    """True if the address has the right format for the network. Does not prove the address exists."""
    n = network(net)
    return bool(n and re.fullmatch(n["address_pattern"].strip("^$"), address.strip()))


def is_valid_tx_hash(net: str, tx_hash: str) -> bool:
    """True if the transaction hash has the right format for the network. Does not prove it exists."""
    n = network(net)
    return bool(n and re.fullmatch(n["hash_pattern"].strip("^$"), tx_hash.strip()))


def install_commands(name: str) -> Optional[Dict]:
    """npm and pip install commands for a project."""
    p = project(name)
    return {"npm": f"npm install {p['npm']}", "pypi": f"pip install {p['pypi']}"} if p else None
