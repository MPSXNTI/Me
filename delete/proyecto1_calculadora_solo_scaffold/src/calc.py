from typing import Callable, Dict

Number = float

def add(a: Number, b: Number) -> Number:
    raise NotImplementedError("Implementa la suma")

def sub(a: Number, b: Number) -> Number:
    raise NotImplementedError("Implementa la resta")

def mul(a: Number, b: Number) -> Number:
    raise NotImplementedError("Implementa la multiplicación")

def div(a: Number, b: Number) -> Number:
    """Divide a / b. Debe lanzar ZeroDivisionError si b == 0."""
    raise NotImplementedError("Implementa la división")

DISPATCH: Dict[str, Callable[[Number, Number], Number]] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}