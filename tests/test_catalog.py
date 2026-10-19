"""Tests for FXFunds Developer Resources. catalog.json is the single source; everything else must match it."""
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

import fxfunds_developer_resources as dev

ROOT = Path(__file__).resolve().parent.parent
CATALOG = json.loads((ROOT / "fxfunds_developer_resources" / "catalog.json").read_text(encoding="utf-8"))
PROJECTS, NETWORKS = CATALOG["projects"], CATALOG["networks"]

VALID = {
    "erc20": ("0xdAC17F958D2ee523a2206206994597C13D831ec7", "0x" + "ab" * 32),
    "trc20": ("TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t", "cd" * 32),
    "ton": ("EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs", "ef" * 32),
}
INVALID_ADDRESSES = ["", "0x123", "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6", "EQshort", "not-an-address"]


def rows(name):
    with open(ROOT / "dataset" / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_catalog_structure():
    ids = [p["id"] for p in PROJECTS]
    assert len(ids) == len(set(ids)) == 5
    for p in PROJECTS:
        assert p["npm"] == f"@fxfunds/{p['id']}" and p["pypi"] == f"fxfunds-{p['id']}"
        assert p["python_import"] == p["pypi"].replace("-", "_")
        assert p["node_api"] and p["python_api"] and p["doi"].isdigit()
    assert [n["key"] for n in NETWORKS] == ["erc20", "trc20", "ton"]


def test_datasets_match_catalog():
    pkgs = rows("fxfunds_developer_packages.csv")
    assert len(pkgs) == 2 * len(PROJECTS)
    for r in pkgs:
        p = dev.project(r["project"])
        assert r["package"] == p[r["registry"]] and r["version"] == p["version"] and r["cli"] == p["cli"]
    nets = rows("fxfunds_usdt_networks.csv")
    assert [r["key"] for r in nets] == [n["key"] for n in NETWORKS]
    for r, n in zip(nets, NETWORKS):
        assert r["usdt_contract"] == n["usdt_contract"] and r["address_pattern"] == n["address_pattern"]


def test_readme_and_docs_list_every_package():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    api = (ROOT / "docs" / "api.md").read_text(encoding="utf-8")
    for p in PROJECTS:
        for text in (readme, api):
            assert p["npm"] in text and p["pypi"] in text and p["cli"] in text, p["id"]
    for n in NETWORKS:
        assert n["usdt_contract"] in readme


def test_validators():
    for net, (addr, tx) in VALID.items():
        assert dev.is_valid_address(net, addr), net
        assert dev.is_valid_tx_hash(net, tx), net
        for bad in INVALID_ADDRESSES:
            assert not dev.is_valid_address(net, bad), (net, bad)
    assert not dev.is_valid_address("erc20", VALID["trc20"][0])
    assert not dev.is_valid_tx_hash("erc20", "ab" * 32)
    assert dev.is_valid_address("tron", VALID["trc20"][0])
    assert not dev.is_valid_address("bitcoin", VALID["erc20"][0])


def test_lookup():
    assert dev.project("@fxfunds/platform-faq")["id"] == "platform-faq"
    assert dev.project("FXFUNDS-RISK-DISCLOSURES")["cli"] == "fxfunds-risk"
    assert dev.project("nope") is None
    assert dev.network("Ethereum")["key"] == "erc20"
    assert dev.install_commands("risk-disclosures") == {"npm": "npm install @fxfunds/risk-disclosures",
                                                        "pypi": "pip install fxfunds-risk-disclosures"}


def test_python_cli():
    run = lambda *a: subprocess.run([sys.executable, "-m", "fxfunds_developer_resources", *a],
                                    capture_output=True, text=True)
    out = run("check-address", "trc20", VALID["trc20"][0], "--json")
    assert out.returncode == 0 and json.loads(out.stdout)["valid_format"] is True
    assert run("check-address", "erc20", "0x123").returncode == 1
    assert json.loads(run("project", "platform-faq", "--json").stdout)["install"]["pypi"] == "pip install fxfunds-platform-faq"


@pytest.mark.skipif(shutil.which("node") is None or not (ROOT / "index.js").exists(),
                    reason="Build the Node.js package first: npm ci && npm run build")
def test_node_matches_python():
    cases = [[net, v] for net, pair in VALID.items() for v in pair] + [[net, b] for net in VALID for b in INVALID_ADDRESSES]
    script = ("const f=require('./index.js');const c=JSON.parse(process.argv[1]);"
              "console.log(JSON.stringify({a:c.map(x=>f.isValidAddress(x[0],x[1])),h:c.map(x=>f.isValidTxHash(x[0],x[1])),"
              "p:f.projects().map(p=>p.id),n:f.network('tron').key,i:f.installCommands('platform-faq')}))")
    node = json.loads(subprocess.run(["node", "-e", script, json.dumps(cases)], cwd=ROOT, capture_output=True,
                                     text=True, check=True).stdout)
    assert node["a"] == [dev.is_valid_address(n, v) for n, v in cases]
    assert node["h"] == [dev.is_valid_tx_hash(n, v) for n, v in cases]
    assert node["p"] == [p["id"] for p in dev.projects()]
    assert node["n"] == "trc20" and node["i"] == dev.install_commands("platform-faq")
