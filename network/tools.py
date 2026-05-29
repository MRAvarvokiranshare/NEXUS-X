import requests

from rich.console import Console
from rich.panel import Panel

console = Console()


def ip_lookup():

    target = input("\nEnter IP or domain: ")

    try:

        response = requests.get(
            f"http://ip-api.com/json/{target}",
            timeout=5
        )

        data = response.json()

        if data["status"] == "success":

            result = f"""
IP Information

IP:
{data.get("query", "N/A")}

Country:
{data.get("country", "N/A")}

Region:
{data.get("regionName", "N/A")}

City:
{data.get("city", "N/A")}

ISP:
{data.get("isp", "N/A")}

Timezone:
{data.get("timezone", "N/A")}
"""

            console.print(
                Panel.fit(
                    result,
                    title="[bold cyan]IP Lookup[/bold cyan]",
                    border_style="cyan"
                )
            )

        else:

            console.print(
                Panel.fit(
                    """
Invalid IP or domain.
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
