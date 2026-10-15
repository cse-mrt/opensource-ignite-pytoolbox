import typer
from rich.console import Console

NAME = "unitconvert"
HELP = "converts between common units"

console = Console()

units={"km":0,"mi":0,"m":0,"c":1,"f":1,"g":2,"kg":2,"lb":2}

def _is_available(unit_1,unit_2)-> bool:
    units_=["km","mi","m","c","f","g","kg","lb"]
    return (unit_1 in units_) and (unit_2 in units_)


def _is_matching(unit_1,unit_2)->bool:
    return units[unit_1]==units[unit_2]


def _convert(value,unit_1,unit_2)->bool:
    _type=units[unit_1]
    U=unit_1
    V=unit_2
    
    if _type==0:
        if U=="km" and V=="m":
            return value*1000
        if U=="km" and V=="mi":
            return value*0.62137
        if U=="m" and V=="km":
            return value/1000
        if U=="m" and V=="mi":
            return value/1609.34
        if U=="mi" and V=="km":
            return value*1.60934
        if U=="mi" and V=="m":
            return value*1609.34

    if _type==1:
        if U=="c" and V=="f":
            return value*(9/5)+32
        if U=="f" and V=="c":
            return (value-32)*5/9
        
    if _type==2:
        if U=="kg" and V=="g":
            return value*1000
        if U=="kg" and V=="lb":
            return value*2.20462
        if U=="g" and V=="kg":
            return value/1000
        if U=="g" and V=="lb":
            return value/453.592
        if U=="lb" and V=="kg":
            return value/2.20462
        if U=="lb" and V=="g":
            return value*453.592
    

def main(value:float,unit_1:str,unit_2:str)->None:
    if value<=0 and not (unit_1=="c" or unit_1=="f"):
        console.print(f"[red]Error:[/red] value must be greater than [red]0[/red]")
        raise typer.Exit(code=1)
    
    if not _is_available(unit_1,unit_2):
        console.print("[red]Error:[/red] invalid unit found")
        raise typer.Exit(code=1)
    
    if not _is_matching(unit_1,unit_2):
        console.print("[red]Error:[/red] units does not match")
        raise typer.Exit(code=1)
    
    converted_value=_convert(value,unit_1,unit_2)
    int_,frac_=list(map(int,str(converted_value).split('.')))
    if frac_==0:
        converted_value=int_
    else:
        converted_value=round(converted_value,2)
    
    if units[unit_2]==1:unit_2=unit_2.upper()
    
    console.print(f"[yellow]{converted_value}[/yellow][bold]{unit_2}[/bold]")
    
