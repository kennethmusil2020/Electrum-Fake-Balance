# -*- coding: utf-8 -*-
"""Configuration loader for Electrum Fake — config.json"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

_DEFAULTS = {
    "electrum_path": "auto",
    "target_balance": {
        "BTC": 5.23471,
    },
    "display_currency": "USD",
    "persist_on_restart": True,
    "auto_update_prices": True,
    "hook_mode": "memory",
    "restore_on_exit": False,
}


def load_config() -> dict:
    """Load configuration from config.json with defaults fallback."""
    config_path = BASE_DIR / "config.json"
    if not config_path.exists():
        save_config(_DEFAULTS)
        return dict(_DEFAULTS)

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        merged = dict(_DEFAULTS)
        merged.update(data)
        return merged
    except (json.JSONDecodeError, IOError):
        return dict(_DEFAULTS)


def save_config(config: dict):
    """Save configuration to config.json."""
    config_path = BASE_DIR / "config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


def get_balance(config: dict) -> float:
    """Return target BTC balance."""
    return config.get("target_balance", {}).get("BTC", 0.0)


def set_balance(config: dict, amount: float) -> dict:
    """Set BTC balance and save."""
    config["target_balance"] = {"BTC": amount}
    save_config(config)
    return config
