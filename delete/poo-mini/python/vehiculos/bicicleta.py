from .vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def mover(self) -> str:
        return f"Bici {self.marca} pedalea a {self.velocidad} km/h."
