from .vehiculo import Vehiculo

class Auto(Vehiculo):
    def mover(self) -> str:
        return f"Auto {self.marca} avanza a {self.velocidad} km/h."
