import typer
from rich.console import Console

NAME = "hexrgb"
HELP = "Convert a hexadecimal color code to RGB values, or vice versa."

console = Console()

def hex_to_rgb(colour):
    colour = colour.lstrip("#")

    if len(colour) != 6:
        console.print("[red]Error:[/red] color must contain 6 hexadecimal digits")
        raise typer.Exit(code=1)    

    red = int(colour[0:2], 16)
    green = int(colour[2:4], 16)
    blue = int(colour[4:6], 16)

    console.print(f"R={red} G={green} B={blue}")