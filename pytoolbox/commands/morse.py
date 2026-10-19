import typer
from rich.console import Console

NAME = "morse"
HELP = "Encode and decode Morse code."

console = Console()

morse_signs = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ": ": "---...",
    "; ": "-.-.-.",
    "=": "-...-",
    "+ ": ".-.-.",
    "- ": "-....-",
    "_ ": "..--.-",
    '"': ".-..-.",
    "$ ": "...-..-",
    "@ ": ".--.-.",
}


reverse_morse = {morse: character for character, morse in morse_signs.items()}


def encode(text: str) -> str:
    final_word = ""

    for character in text.upper():
        if character not in morse_signs:
            raise ValueError(f"Invalid character: {character}")

        for chr_morse, morse in morse_signs.items():
            if character == chr_morse:
                final_word += morse + " "

    return final_word.strip()


def decode(text: str) -> str:
    final_text = ""
    text_arr = text.split()

    for i in range(len(text_arr)):
        if text_arr[i] not in reverse_morse:
            raise ValueError(f"Invalid Morse code: {text_arr[i]}")

        if text_arr[i] in reverse_morse:
            final_text += reverse_morse[text_arr[i]]

    return final_text


def main(
    text: str,
    decode_mode: bool = typer.Option(False, "--decode"),
) -> None:
    try:
        if decode_mode:
            console.print(decode(text))
        else:
            console.print(encode(text))

    except ValueError as error:
        console.print(f"Error: {error}")
        raise typer.Exit(code=1) from None
