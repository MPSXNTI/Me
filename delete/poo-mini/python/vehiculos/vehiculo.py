from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca: str):
        self._marca = marca          # convención "protegido"
        self._velocidad = 0

    @property
    def marca(self) -> str:
        return self._marca

    @property
    def velocidad(self) -> int:
        return self._velocidad

    def acelerar(self, delta: int) -> None:
        if delta < 0:
            raise ValueError("delta debe ser >= 0")
        self._velocidad += delta

    def frenar(self, delta: int) -> None:
        if delta < 0:
            raise ValueError("delta debe ser >= 0")
        self._velocidad = max(0, self._velocidad - delta)

    @abstractmethod
    def mover(self) -> str:
        ...
