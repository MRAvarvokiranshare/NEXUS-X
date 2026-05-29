import re
import qrcode

from rich.console import Console
from rich.panel import Panel

console = Console()


def username_checker():

    username = input("\nEnter Telegram username: ").replace("@", "")

    if re.match(r"^[a-zA-Z0-9_]{5,32}$", username):

        link = f"https://t.me/{username}"

        console.print(
            Panel.fit(
                f"""
Username: @{username}

Status: VALID
Length: {len(username)}

Telegram Link:
{link}
""",
                title="[bold cyan]Telegram Username Checker[/bold cyan]",
                border_style="green"
            )
        )

    else:

        console.print(
            Panel.fit(
                """
Invalid username.

Rules:
- Only letters
- Numbers
- Underscore
- 5 to 32 characters
""",
                border_style="red"
            )
        )


def link_analyzer():

    link = input("\nEnter Telegram link: ")

    if "t.me/" in link:

        username = link.split("/")[-1]

        console.print(
            Panel.fit(
                f"""
Telegram Link Analysis

Link:
{link}

Username:
@{username}

Status:
VALID TELEGRAM LINK
""",
                title="[bold cyan]Telegram Link Analyzer[/bold cyan]",
                border_style="cyan"
            )
        )

    else:

        console.print(
            Panel.fit(
                """
Invalid Telegram link.

Example:
https://t.me/telegram
""",
                border_style="red"
            )
        )


def qr_generator():

    data = input("\nEnter link or text: ")

    qr = qrcode.make(data)

    filename = "nexus_qr.png"

    qr.save(filename)

    console.print(
        Panel.fit(
            f"""
QR Code Generated Successfully

Saved As:
{filename}
""",
            title="[bold cyan]QR Generator[/bold cyan]",
            border_style="green"
        )
    )
