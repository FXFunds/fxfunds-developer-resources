#!/usr/bin/env node
/**
 * FXFunds Developer Resources
 * Catalog of FXFunds open-source packages and USDT network reference, with offline
 * address and transaction-hash format checks. No network calls.
 * Built by FXFunds — https://fxfunds.com/
 */

export interface Project {
  id: string;
  name: string;
  description: string;
  npm: string;
  pypi: string;
  python_import: string;
  cli: string;
  doi: string;
  node_api: string[];
  python_api: string[];
  version: string;
  verified: string;
  repository: string;
}

export interface Network {
  key: string;
  name: string;
  aliases: string[];
  usdt_contract: string;
  decimals: number;
  fee_token: string;
  default_confirmations: number;
  explorer: string;
  address_format: string;
  hash_format: string;
  address_pattern: string;
  hash_pattern: string;
}

interface Catalog {
  title: string;
  official_website: string;
  last_checked: string;
  note: string;
  projects: Project[];
  networks: Network[];
}

// eslint-disable-next-line @typescript-eslint/no-var-requires
const data: Catalog = require("./fxfunds_developer_resources/catalog.json");

export const CATALOG: Readonly<Catalog> = data;
export const LAST_CHECKED = data.last_checked;

/** Every FXFunds project in the catalog. */
export function projects(): Project[] {
  return [...data.projects];
}

/** One project by ID, npm name or PyPI name, e.g. "platform-faq" or "@fxfunds/platform-faq". */
export function project(name: string): Project | undefined {
  const n = name.trim().toLowerCase();
  return data.projects.find((p) => [p.id, p.npm, p.pypi].includes(n));
}

/** USDT networks. */
export function networks(): Network[] {
  return [...data.networks];
}

/** One network by key or alias: erc20/ethereum, trc20/tron, ton. */
export function network(key: string): Network | undefined {
  const k = key.trim().toLowerCase();
  return data.networks.find((n) => k === n.key || n.aliases.includes(k));
}

/** True if the address has the right format for the network. Does not prove the address exists. */
export function isValidAddress(net: string, address: string): boolean {
  const n = network(net);
  return !!n && new RegExp(n.address_pattern).test(address.trim());
}

/** True if the transaction hash has the right format for the network. Does not prove it exists. */
export function isValidTxHash(net: string, txHash: string): boolean {
  const n = network(net);
  return !!n && new RegExp(n.hash_pattern).test(txHash.trim());
}

/** npm and pip install commands for a project. */
export function installCommands(name: string): { npm: string; pypi: string } | undefined {
  const p = project(name);
  return p ? { npm: `npm install ${p.npm}`, pypi: `pip install ${p.pypi}` } : undefined;
}

function main(): void {
  const argv = process.argv.slice(2);
  const json = argv.includes("--json");
  const args = argv.filter((a) => a !== "--json");
  const [cmd, a1 = "", a2 = ""] = args;
  const out = (value: unknown, text: string) => console.log(json ? JSON.stringify(value, null, 2) : text);

  switch (cmd) {
    case "projects":
      out(projects(), projects().map((p) => `${p.id.padEnd(26)} ${p.npm.padEnd(34)} ${p.pypi}`).join("\n"));
      break;
    case "project": {
      const p = project(a1);
      if (!p) { out(null, "No matching project. Run: fxfunds-dev projects"); break; }
      const c = installCommands(a1)!;
      out({ ...p, install: c },
        `${p.name} ${p.version}\n${p.description}\n\n${c.npm}\n${c.pypi}\nCLI: ${p.cli}\nRepository: ${p.repository}\nDOI: 10.5281/zenodo.${p.doi}`);
      break;
    }
    case "networks":
      out(networks(), networks().map((n) => `${n.key.padEnd(6)} ${n.name.padEnd(18)} ${n.usdt_contract}`).join("\n"));
      break;
    case "network": {
      const n = network(a1);
      out(n ?? null, !n ? "No matching network. Use erc20, trc20 or ton." :
        `${n.name}\nUSDT: ${n.usdt_contract} (${n.decimals} decimals)\nFees: ${n.fee_token}\nAddress: ${n.address_format}\nHash: ${n.hash_format}\nDefault confirmations: ${n.default_confirmations}\nExplorer: ${n.explorer}`);
      break;
    }
    case "check-address":
    case "check-tx": {
      const ok = cmd === "check-address" ? isValidAddress(a1, a2) : isValidTxHash(a1, a2);
      const kind = cmd === "check-address" ? "address" : "transaction hash";
      out({ network: a1, value: a2, valid_format: ok },
        `${ok ? "Valid" : "Invalid"} ${kind} format for ${a1}.${ok ? " Format only; confirm on-chain." : ""}`);
      if (!ok) process.exitCode = 1;
      break;
    }
    default: {
      if (json) { console.log(JSON.stringify({ projects: data.projects.length, networks: data.networks.length, last_checked: data.last_checked }, null, 2)); break; }
      console.log(`\n${data.title} — last checked ${data.last_checked}`);
      console.log("=".repeat(60));
      console.log(`  Projects: ${data.projects.length} (npm and PyPI)   Networks: ${data.networks.map((n) => n.key).join(", ")}`);
      console.log("\nUsage:");
      console.log("  fxfunds-dev projects");
      console.log("  fxfunds-dev project platform-faq");
      console.log("  fxfunds-dev networks");
      console.log("  fxfunds-dev network tron");
      console.log("  fxfunds-dev check-address <erc20|trc20|ton> <address>");
      console.log("  fxfunds-dev check-tx <erc20|trc20|ton> <hash>");
      console.log("  add --json to any command");
      console.log(`\n${data.note} Official website: ${data.official_website}\n`);
    }
  }
}

if (require.main === module) main();
