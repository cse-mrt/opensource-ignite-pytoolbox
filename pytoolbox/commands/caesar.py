import typer
from rich.console import Console

NAME = "caesar"
HELP = "Shifts the letters of the word."

console = Console()

def _caesar_cipher(text: str, shift: int) -> str:
    newText: str = ""
    # note: works only for lowercase letters for now
    for index, letter in enumerate(text):
        # console.print(index, letter, ord(letter), ord(letter) + 3, chr(( (ord(letter)- 97 + shift)%26 + 97)) )
        newText += chr(( (ord(letter)- 97 + shift)%26 + 97))
    return newText
        


def main(text: str, shift: int = 0) -> None:
    if text == "":
        console.print("[red]Error:[/red] text must not be empty")
        raise typer.Exit(code=1)

    result = _caesar_cipher(text, shift)
    console.print(result)
    