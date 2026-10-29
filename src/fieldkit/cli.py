import sys
from rich.console import Console
from fieldkit.uncertainty import Measurement

console = Console()

def main():
    console.print("[bold green]FieldKit CLI Tool v0.1.0[/bold green]")
    console.print("Motor de cálculo científico inicializado.")

    # Ejemplo de cálculo rápido
    m1 = Measurement(10.5, 0.2)
    m2 = Measurement(5.2, 0.1)
    res = m1 + m2
    console.print(f"Cálculo de muestra: ({m1}) + ({m2}) = [bold cyan]{res}[/bold cyan]")

if __name__ == "__main__":
    main()
