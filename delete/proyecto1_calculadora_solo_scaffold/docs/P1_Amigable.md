# 🐍 Proyecto 1 — Calculadora básica (Amigable / Conversacional)

¡Vamos a armar tu primera calculadora en consola! 🌟  
La idea es que construyas tú la lógica — yo te dejo el esqueleto 🧱 para que lo completes.

## 🎯 Objetivo
Pedir dos números y un operador (`+ - * /`) y mostrar el resultado (con 2 decimales), cuidando los errores comunes.

## 🧩 Descripción interactiva
- Pregunta por **dos números** y por la **operación**.
- Si algo no cuadra (ej. “abc”), **repregunta**.
- Ante división por cero, **explica el error** y vuelve a intentar.

## 💡 Pistas útiles
- Crea funciones `add`, `sub`, `mul`, `div` y un diccionario que haga de “router” de operaciones.
- Maneja los errores en `main()` (¡y mantén la lógica limpia y simple!).
- Redondea al final: `round(resultado, 2)`.

## 🧱 Código base de inicio (incompleto a propósito)
```python
# src/calc.py
def add(a, b):
    # TODO: suma
    raise NotImplementedError

def sub(a, b):
    # TODO: resta
    raise NotImplementedError

def mul(a, b):
    # TODO: multiplicación
    raise NotImplementedError

def div(a, b):
    # TODO: división (lanza ZeroDivisionError si b == 0)
    raise NotImplementedError

DISPATCH = {"+": add, "-": sub, "*": mul, "/": div}
```

```python
# src/cli.py
from .calc import DISPATCH

def parse_float(prompt):
    # TODO: pedir y validar un float. Reintenta si falla.
    raise NotImplementedError

def main():
    # TODO: arma el flujo: leer números y operador, calcular, imprimir
    raise NotImplementedError

if __name__ == "__main__":
    main()
```

## ✅ Pruebas (empezarán fallando y eso está bien)
```python
# tests/test_calc.py
import pytest
from src.calc import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
```
Ejecuta:
```bash
pytest -q
```

## 🚀 Nivel Plus
- Agrega `^` (potencia) y `√` (raíz).
- Crea un **historial** de operaciones en un archivo.
- Permite configurar cuántos decimales mostrar.