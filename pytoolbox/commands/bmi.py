import math

import typer
from rich.console import Console

NAME = "bmi"
HELP = "Calculate Body Mass Index from height in meters and weight in kilograms."

console = Console()


def main(
    height: float = typer.Option(..., help="Height in meters."),
    weight: float = typer.Option(..., help="Weight in kilograms."),
) -> None:
    if not math.isfinite(height) or height <= 0:
        console.print("[red]Error:[/red] height must be a positive, finite number of meters")
        raise typer.Exit(code=1)

    if not math.isfinite(weight) or weight <= 0:
        console.print("[red]Error:[/red] weight must be a positive, finite number of kilograms")
        raise typer.Exit(code=1)

    bmi = weight / (height**2)
    console.print(f"{bmi:.2f}")
