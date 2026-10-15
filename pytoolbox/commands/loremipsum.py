import typer
from rich.console import Console

NAME = "loremipsum"
HELP = "Print N words of placeholder lorem ipsum text."

console = Console()

LOREM_WORDS = (
    "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod "
    "tempor incididunt ut labore et dolore magna aliqua ut enim ad minim "
    "veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
    "commodo consequat duis aute irure dolor in reprehenderit in voluptate "
    "velit esse cillum dolore eu fugiat nulla pariatur excepteur sint "
    "occaecat cupidatat non proident sunt in culpa qui officia deserunt "
    "mollit anim id est laborum"
).split()


def main(
    words: int = typer.Option(10, "--words", "-w", help="Number of words to generate."),
) -> None:
    if words <= 0:
        console.print("")
        return
    generated = " ".join(LOREM_WORDS[i % len(LOREM_WORDS)] for i in range(words))
    console.print(generated)
