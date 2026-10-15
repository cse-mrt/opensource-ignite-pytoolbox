import typer
from rich.console import Console
import re

NAME = "titlecase"
HELP = "Convert a string to title case."

console = Console()


def _to_title_case(text: str) -> str:
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), text)


def _word_count(text: str) -> int:
    return len(text.split())


def main(text: str, show_word_count: bool = False) -> None:
    if not text.strip():
        console.print("[red]Error:[/red] text must not be blank")
        raise typer.Exit(code=1)

    result = _to_title_case(text)
    console.print(result)

    if show_word_count:
        console.print(f"[dim]{_word_count(text)} word(s)[/dim]")
