import typer
from rich.console import Console

NAME = "slugify"
HELP = "Slugify a text."

console = Console()

def main(text: str) -> None:
    slugified = ""
    for c in text:
        if c.isalnum():
            slugified += c.lower()
        elif c == " ":
            slugified += "-"

    console.print(slugified)