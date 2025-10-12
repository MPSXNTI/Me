from vehiculos.auto import Auto
from vehiculos.bicicleta import Bicicleta
from typing import List
from vehiculos.vehiculo import Vehiculo

def demo() -> None:
    flota: List[Vehiculo] = [Auto("Toyota"), Bicicleta("Trek")]
    flota[0].acelerar(50)
    flota[1].acelerar(20)
    for v in flota:
        print(v.mover())

if __name__ == "__main__":
    demo()
