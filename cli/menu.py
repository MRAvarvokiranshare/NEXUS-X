from rich.console import Console
from rich.table import Table

console = Console()

def show_menu():

    table = Table(title="NEXUS Modules")

    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Module", style="white")
    table.add_column("Description", style="green")

    table.add_row(
        "1",
        "Telegram Username Checker",
        "Validate Telegram usernames"
    )

    table.add_row(
        "2",
        "Telegram Link Analyzer",
        "Analyze Telegram links"
    )

    table.add_row(
        "3",
        "QR Generator",
        "Generate QR codes"
    )

    table.add_row(
        "4",
        "Instagram Profile Analyzer",
        "Analyze Instagram usernames"
    )

    table.add_row(
        "5",
        "AI Caption Generator",
        "Generate social captions"
    )

    table.add_row(
        "6",
        "IP Lookup",
        "IP & domain information"
    )

    table.add_row(
        "7",
        "Password Generator",
        "Generate secure passwords"
    )

    table.add_row(
        "8",
        "JSON Formatter",
        "Format & validate JSON"
    )

    table.add_row(
        "9",
        "GitHub Repo Analyzer",
        "Analyze GitHub repositories"
    )

    table.add_row(
        "0",
        "Exit",
        "Close NEXUS"
    )

    console.print(table)
