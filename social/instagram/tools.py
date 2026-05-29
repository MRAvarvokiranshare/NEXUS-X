import re

from rich.console import Console
from rich.panel import Panel

console = Console()


def instagram_analyzer():

    username = input("\nEnter Instagram username: ").replace("@", "")

    if re.match(r"^[a-zA-Z0-9._]{1,30}$", username):

        link = f"https://instagram.com/{username}"

        console.print(
            Panel.fit(
                f"""
Instagram Profile Analysis

Username:
@{username}

Status:
VALID USERNAME

Length:
{len(username)}

Profile Link:
{link}
""",
                title="[bold magenta]Instagram Analyzer[/bold magenta]",
                border_style="magenta"
            )
        )

    else:

        console.print(
            Panel.fit(
                """
Invalid Instagram username.

Rules:
- Letters
- Numbers
- Dot
- Underscore
- Max 30 characters
""",
                border_style="red"
            )
        )
