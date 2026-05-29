from rich.console import Console
from rich.panel import Panel

console = Console()

def show_banner():
    banner = """
NEXUS v1.0
Modern Developer & Social Toolkit
"""

    console.print(
        Panel.fit(
            banner,
            border_style="cyan",
            title="[bold white]NEXUS[/bold white]",
        )
    )
