from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def show_banner():
    banner_text = """
[bold red]██╗      ██████╗  █████╗ ██████╗ ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗[/bold red]
[bold red]██║     ██╔═══██╗██╔══██╗██╔══██╗██║██╔════╝██╔═══   ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗[/bold red]
[bold red]██║     ██║   ██║███████║██║  ██║██║███████╗██║      ███████║   ██║   ██║   ██║██████╔╝[/bold red]
[bold red]██║     ██║   ██║██╔══██║██║  ██║██║╚════██║██║     ║██╔══██║   ██║   ██║   ██║██╔══██╗[/bold red]
[bold red]███████╗╚██████╔╝██║  ██║██████╔╝██║███████║╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║[/bold red]
[bold red]╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝[/bold red]

[bold cyan]Red Team Payload Generator & Obfuscation Framework[/bold cyan]
[dim]🔐 Advanced AV/EDR Evasion & Adversary Simulation Toolkit[/dim]
"""
    
    panel = Panel(
        Text(banner_text, justify="center"),
        border_style="red",
        box=box.DOUBLE,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print("[bold yellow]⚠️  For authorized Red Team operations and educational use only![/bold yellow]\n") 