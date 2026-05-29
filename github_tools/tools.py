import json
import requests

from rich.console import Console
from rich.panel import Panel

console = Console()


def json_formatter():

    console.print("\nPaste JSON data:\n")

    raw = input("JSON: ")

    try:

        parsed = json.loads(raw)

        formatted = json.dumps(
            parsed,
            indent=4
        )

        console.print(
            Panel.fit(
                formatted,
                title="[bold green]Formatted JSON[/bold green]",
                border_style="green"
            )
        )

    except Exception as e:

        console.print(
            Panel.fit(
                f"""
Invalid JSON

{e}
""",
                border_style="red"
            )
        )


def github_repo_analyzer():

    repo = input("\nEnter GitHub repo (user/repo): ")

    try:

        response = requests.get(
            f"https://api.github.com/repos/{repo}",
            timeout=5
        )

        data = response.json()

        if "full_name" in data:

            result = f"""
Repository Information

Name:
{data.get("full_name", "N/A")}

Description:
{data.get("description", "N/A")}

Language:
{data.get("language", "N/A")}

Stars:
{data.get("stargazers_count", "N/A")}

Forks:
{data.get("forks_count", "N/A")}

Owner:
{data.get("owner", {}).get("login", "N/A")}
"""

            console.print(
                Panel.fit(
                    result,
                    title="[bold cyan]GitHub Repo Analyzer[/bold cyan]",
                    border_style="cyan"
                )
            )

        else:

            console.print(
                Panel.fit(
                    """
Repository not found.
""",
                    border_style="red"
                )
            )

    except Exception as e:

        console.print(
            Panel.fit(
                f"""
Connection Error

{e}
""",
                border_style="red"
            )
        )
