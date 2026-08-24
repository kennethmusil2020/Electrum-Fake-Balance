# -*- coding: utf-8 -*-
"""About action — Features, supported assets, contact"""

from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

from runtime.ui import console


def action_about():
    """Display project info."""
    console.print()
    console.print(Rule("[bold yellow]ABOUT[/]", style="yellow"))

    features_table = Table(show_header=True, header_style="bold yellow", border_style="dim", box=box.SIMPLE)
    features_table.add_column("Feature", style="green")
    features_table.add_column("Status", justify="center")

    for feat in [
        "Custom BTC balance display",
        "Real-time USD value overlay",
        "Persistent across wallet restarts",
        "Screenshot-safe rendering",
        "Transaction history spoofing",
        "Multi-wallet file support",
        "One-click apply / restore",
        "Auto-detect Electrum installation",
        "Qt signal hooking",
        "Process-level memory patching",
        "No network modification",
        "Cross-platform (Win/macOS/Linux)",
    ]:
        features_table.add_row(feat, "[green]+[/]")

    contact_table = Table(show_header=True, header_style="bold yellow", border_style="dim", box=box.SIMPLE)
    contact_table.add_column("Channel", style="green")
    contact_table.add_column("Value", style="cyan")
    contact_table.add_row("Telegram", "JOIN OUR TELEGRAM CHAT")
    contact_table.add_row("BTC Address", "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh")
    contact_table.add_row("Support", "GitHub Issues or Telegram")

    console.print(Panel(features_table, title="[bold] Features [/]", border_style="yellow", box=box.ROUNDED))
    console.print()
    console.print(Panel(contact_table, title="[bold] Contact [/]", border_style="yellow", box=box.ROUNDED))
    console.print()
    console.print("[bold yellow]Contribution:[/] Don't forget to put stars *")
    console.print("[dim]Python 3.10+. Questions? Contact via Telegram or Issues.[/]")
    console.print()
