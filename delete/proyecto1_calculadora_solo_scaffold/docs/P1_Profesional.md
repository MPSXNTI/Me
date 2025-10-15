# Proyecto 1 — Calculadora básica (Profesional / Estructurada)

## 🎯 Objetivo
Diseñar una calculadora en consola que soporte **suma, resta, multiplicación y división** con **validación de entradas** y **manejo explícito de errores**.

## 🧩 Requisitos (Definición)
- Entrada: dos operandos numéricos tipo `float`, un operador: `+ - * /`.
- Salida: resultado numérico redondeado a 2 decimales.
- Debe manejar: división por cero, operación no soportada, entradas inválidas.

## 📐 Criterios de diseño
- Funciones puras por operación (`add`, `sub`, `mul`, `div`) y un **dispatcher** (dict) para mapear operadores.
- CLI mínima en `main()` separada de la lógica de dominio.
- **Pruebas unitarias** con `pytest` que definan el comportamiento esperado.

## 💡 Pistas (sin spoilers)
- Centraliza la captura de errores en `main()`.
- Valida la operación antes de invocar la función.
- Redondea al final del flujo, no dentro de cada operación.

## 🧱 Código base de inicio (scaffold — incompleto a propósito)
```python
# src/calc.py
from typing import Callable, Dict

Number = float

def add(a: Number, b: Number) -> Number:
    raise NotImplementedError("Implementa la suma")

def sub(a: Number, b: Number) -> Number:
    raise NotImplementedError("Implementa la resta")

def mul(a: Number, b: Number) -> Number:
    raise NotImplementedError("Implementa la multiplicación")

def div(a: Number, b: Number) -> Number:
    """Divide a / b.
    Debe lanzar ZeroDivisionError si b == 0.
    """
    raise NotImplementedError("Implementa la división")

DISPATCH: Dict[str, Callable[[Number, Number], Number]] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
```

```python
# src/cli.py
from .calc import DISPATCH
from typing import Optional

def parse_float(prompt: str) -> float:
    # TODO: validar/repreguntar hasta recibir un float válido
    raise NotImplementedError

def main() -> None:
    # TODO: flujo de consola orientado a errores controlados
    # 1) leer a, b
    # 2) leer operador
    # 3) resolver vía DISPATCH
    # 4) imprimir resultado redondeado a 2 decimales
    raise NotImplementedError

if __name__ == "__main__":
    main()
```

## ✅ Pruebas unitarias (fallarán al inicio)
```python
# tests/test_calc.py
import pytest
from src.calc import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(4, 2.5) == 10

def test_div_normal():
    assert div(10, 4) == 2.5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
```
**Ejecución de pruebas**
```bash
pytest -q
```

## 🚀 Nivel Plus
- Soporta potencia `^` y raíz `√` (con validación de dominio).
- Añade un modo **historial** que escriba operaciones en `historial.txt`.
- Integra un parámetro `--round=N` en CLI para configurar decimales.