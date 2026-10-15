import typer
from rich.console import Console

NAME = "smallcase"
HELP = "Convert a string to lowercase."

console = Console()


def _to_lower_case(text: str) -> str:
    return text.upper()


def _word_count(text: str) -> int:
    return len(text.split())


def main(text: str, show_word_count: bool = False) -> None:
    if not text.strip():
        console.print("[red]Error:[/red] text must not be blank")
        raise typer.Exit(code=1)

    result = _to_lower_case(text)
    console.print(result)

    if show_word_count:
        console.print(f"[dim]{_word_count(text)} word(s)[/dim]")
