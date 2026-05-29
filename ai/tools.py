import random
import string

from rich.console import Console
from rich.panel import Panel

console = Console()


def caption_generator():

    topic = input("\nEnter caption topic: ")

    captions = [

        f"{topic} ✨",
        f"New vibes with {topic} 🚀",
        f"Minimal. Clean. {topic}",
        f"{topic} — powered by NEXUS",
        f"Stay creative with {topic}",
        f"{topic} but better 🔥",
        f"Simple things. Big impact. {topic}",
        f"{topic} | Modern Digital Energy"
    ]

    result = random.choice(captions)

    console.print(
        Panel.fit(
            f"""
Generated Caption

{result}
""",
            title="[bold green]AI Caption Generator[/bold green]",
            border_style="green"
        )
    )


def password_generator():

    length = input("\nPassword length: ")

    try:

        length = int(length)

        chars = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(
            random.choice(chars)
            for _ in range(length)
        )

        console.print(
            Panel.fit(
                f"""
Generated Password

{password}
""",
                title="[bold cyan]Password Generator[/bold cyan]",
                border_style="cyan"
            )
        )

    except:

        console.print(
            Panel.fit(
                """
Invalid length.
""",
                border_style="red"
            )
        )
