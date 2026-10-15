import typer
from rich.console import Console

NAME = "palindrome"
HELP = "Check whether a string is a palindrome."

console = Console()


def _reverse(text: str) -> str:
    return text[::-1]


def _check(text: str) -> bool:
    text = text.lower()
    newtext = ""
    for char in text:
        if char in "abcdefghijklmnopqrstuvwxyz":
            newtext += char
    return newtext == _reverse(newtext)


def _format_result(text: str, is_palindrome: bool) -> str:
    verdict = "is" if is_palindrome else "is not"
    return f'"{text}" {verdict} a palindrome'


def main(text: str, verbose: bool = False) -> None:
    if not text:
        console.print("[red]Error:[/red] text must not be empty")
        raise typer.Exit(code=1)

    is_palindrome = _check(text)

    if verbose:
        console.print(_format_result(text, is_palindrome))
    else:
        console.print(is_palindrome)
