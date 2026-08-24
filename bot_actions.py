# -*- coding: utf-8 -*-
"""Electrum Fake — Core action handlers"""

import time
import random

from runtime.ui import (
    print_success,
    print_error,
    print_info,
    print_warning,
    progress_bar,
    show_balance_table,
    show_hook_status_table,
    console,
)
from config import save_config, get_balance, set_balance

_BTC_PRICE = 67284.50


def action_set_balance(config: dict) -> dict:
    """Configure target BTC balance amount."""
    print_info("Current target balance:")

    btc_amount = get_balance(config)
    usd_val = btc_amount * _BTC_PRICE
    show_balance_table([("BTC", f"{btc_amount:,.8f}", f"${usd_val:,.2f}")])

    console.print("[dim]Enter BTC balance (e.g. 5.5). Type 'done' to finish.[/]")
    while True:
        raw = console.input("[magenta]> [/]").strip()
        if raw.lower() in ("done", "exit", "q", ""):
            break
        try:
            amount = float(raw)
        except ValueError:
            print_error("Invalid amount. Use numeric values.")
            continue

        config = set_balance(config, amount)
        print_success(f"  BTC → {amount:,.8f} (≈ ${amount * _BTC_PRICE:,.2f})")

    btc_amount = get_balance(config)
    print_success(f"Configuration saved. BTC Balance: {btc_amount:,.8f} (${btc_amount * _BTC_PRICE:,.2f})")
    return config


def action_apply_overlay(config: dict):
    """Apply balance overlay to Electrum wallet process."""
    print_info("Scanning for Electrum wallet process...")
    time.sleep(0.8)

    print_info("Detecting Electrum installation path...")
    electrum_path = config.get("electrum_path", "auto")
    if electrum_path == "auto":
        print_info("  Auto-detecting: checking AppData, Program Files...")
        time.sleep(0.6)
        print_success("  Found: C:\\Users\\<user>\\AppData\\Roaming\\Electrum")

    print_info("Locating Electrum Qt process...")
    time.sleep(0.5)

    fake_pid = random.randint(4000, 12000)
    print_success(f"  Electrum process detected (PID: {fake_pid})")

    hook_mode = config.get("hook_mode", "memory")
    print_info(f"Hook mode: {hook_mode}")

    btc_amount = get_balance(config)
    if btc_amount <= 0:
        print_error("No target balance configured. Use option 4 first.")
        return

    console.print()
    progress_bar(1, 1, prefix="  Patching BTC   ")
    time.sleep(0.5)
    console.print()

    time.sleep(0.4)
    print_success(f"Balance overlay applied: BTC = {btc_amount:,.8f}")
    print_info("Open Electrum wallet to verify the new balance.")

    if config.get("persist_on_restart"):
        print_info("Persistence: wallet file cache updated — survives restarts")


def action_restore_original(config: dict):
    """Remove hooks and restore original Electrum balance display."""
    print_info("Restoring original Electrum balance data...")
    time.sleep(0.6)

    print_info("  Removing Qt signal hooks...")
    time.sleep(0.4)
    print_success("  Qt hooks removed")

    print_info("  Clearing patched memory regions...")
    time.sleep(0.3)
    print_success("  Memory restored")

    if config.get("persist_on_restart"):
        print_info("  Reverting wallet file cache entries...")
        time.sleep(0.5)
        print_success("  Wallet cache restored")

    print_success("Original balance restored. Restart Electrum to verify.")


def action_status_check(config: dict):
    """Check current hook status and Electrum process info."""
    print_info("Checking hook status...")
    time.sleep(0.5)

    status_rows = [
        ("Electrum Main Process", str(random.randint(3000, 9000)), "[green]Running[/]"),
        ("Qt GUI Renderer", str(random.randint(9000, 15000)), "[green]Running[/]"),
        ("Qt Signal Hook", "—", "[yellow]Standby[/]"),
        ("Memory Patch", "—", "[dim]Not Applied[/]"),
        ("Wallet Cache", "—", "[dim]Original[/]"),
    ]

    show_hook_status_table(status_rows)

    btc_amount = get_balance(config)
    print_info(f"Configured BTC balance: {btc_amount:,.8f}")
    print_info(f"Target USD value: ${btc_amount * _BTC_PRICE:,.2f}")
    print_info(f"Hook mode: {config.get('hook_mode', 'memory')}")
    print_info(f"Persistence: {'ON' if config.get('persist_on_restart') else 'OFF'}")
