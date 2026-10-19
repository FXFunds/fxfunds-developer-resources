"""Command-line interface: fxfunds-dev / python -m fxfunds_developer_resources"""
import json
import sys

from . import CATALOG, install_commands, is_valid_address, is_valid_tx_hash, network, networks, project, projects


def main(argv=None) -> None:
    argv = list(sys.argv[1:] if argv is None else argv)
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    cmd = args[0] if args else None
    a1 = args[1] if len(args) > 1 else ""
    a2 = args[2] if len(args) > 2 else ""

    def out(data, text):
        print(json.dumps(data, indent=2, ensure_ascii=False) if as_json else text)

    if cmd == "projects":
        out(projects(), "\n".join(f"{p['id']:<26} {p['npm']:<34} {p['pypi']}" for p in projects()))
    elif cmd == "project":
        p = project(a1)
        if not p:
            out(None, "No matching project. Run: fxfunds-dev projects")
        else:
            cmds = install_commands(a1)
            out({**p, "install": cmds},
                f"{p['name']} {p['version']}\n{p['description']}\n\n{cmds['npm']}\n{cmds['pypi']}\n"
                f"CLI: {p['cli']}\nRepository: {p['repository']}\nDOI: 10.5281/zenodo.{p['doi']}")
    elif cmd == "networks":
        out(networks(), "\n".join(f"{n['key']:<6} {n['name']:<18} {n['usdt_contract']}" for n in networks()))
    elif cmd == "network":
        n = network(a1)
        out(n, "No matching network. Use erc20, trc20 or ton." if not n else
            f"{n['name']}\nUSDT: {n['usdt_contract']} ({n['decimals']} decimals)\nFees: {n['fee_token']}\n"
            f"Address: {n['address_format']}\nHash: {n['hash_format']}\n"
            f"Default confirmations: {n['default_confirmations']}\nExplorer: {n['explorer']}")
    elif cmd in ("check-address", "check-tx"):
        ok = (is_valid_address if cmd == "check-address" else is_valid_tx_hash)(a1, a2)
        kind = "address" if cmd == "check-address" else "transaction hash"
        out({"network": a1, "value": a2, "valid_format": ok},
            f"{'Valid' if ok else 'Invalid'} {kind} format for {a1}." + (" Format only; confirm on-chain." if ok else ""))
        if not ok:
            sys.exit(1)
    else:
        if as_json:
            print(json.dumps({"projects": len(projects()), "networks": len(networks()),
                              "last_checked": CATALOG["last_checked"]}, indent=2))
            return
        print(f"\n{CATALOG['title']} — last checked {CATALOG['last_checked']}")
        print("=" * 60)
        print(f"  Projects: {len(projects())} (npm and PyPI)   Networks: {', '.join(n['key'] for n in networks())}")
        print("\nUsage:")
        print("  fxfunds-dev projects")
        print("  fxfunds-dev project platform-faq")
        print("  fxfunds-dev networks")
        print("  fxfunds-dev network tron")
        print("  fxfunds-dev check-address <erc20|trc20|ton> <address>")
        print("  fxfunds-dev check-tx <erc20|trc20|ton> <hash>")
        print("  add --json to any command")
        print(f"\n{CATALOG['note']} Official website: {CATALOG['official_website']}\n")


if __name__ == "__main__":
    main()
