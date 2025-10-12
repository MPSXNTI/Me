# Ruta de Proyectos en Python — v1 (Amigable/Conversacional)

¡Bienvenido/a! 💙 Esta guía contiene **5 mini-proyectos** perfectos para agarrar ritmo con Python.
Cada proyecto trae su **objetivo**, una **descripción interactiva**, **pistas** para ayudarte,
un **código base** para arrancar rápido, y un **reto “Nivel Plus”** para subir de nivel.

Sugerencia: crea una carpeta `proyectos_python/` y guarda cada proyecto en su propia subcarpeta con un `main.py`.

---

## Proyecto 1: Calculadora básica

**🎯 Objetivo**

Implementar operaciones aritméticas con validación de entrada y manejo de errores.

**🧩 Descripción interactiva**

- Vamos a construirlo paso a paso ✅
- Prueba, rompe cosas y vuelve a intentar 😄
- Mantén funciones pequeñas y fáciles de probar.

**💡 Pistas**

- Usa funciones por operación y un diccionario para mapear símbolos.
- Valida entradas numéricas con un bucle y try/except.
- Evita división por cero con una comprobación temprana.

**🧱 Código base de inicio**

```python
def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplica(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b

OPERACIONES = {"+": suma, "-": resta, "*": multiplica, "/": divide}

def leer_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def main():
    a = leer_float("Primer número: ")
    b = leer_float("Segundo número: ")
    op = input("Operación (+, -, *, /): ").strip()
    func = OPERACIONES.get(op)
    if not func:
        print("Operación no soportada.")
        return
    try:
        resultado = func(a, b)
        print(f"Resultado: {round(resultado, 2)}")
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Historial a archivo
- Operaciones encadenadas
- Soporte de potencia y raíz

---

## Proyecto 2: Adivina el número

**🎯 Objetivo**

El programa genera un número secreto; el usuario intenta adivinar con pistas incrementalmente.

**🧩 Descripción interactiva**

- Vamos a construirlo paso a paso ✅
- Prueba, rompe cosas y vuelve a intentar 😄
- Mantén funciones pequeñas y fáciles de probar.

**💡 Pistas**

- Usa random.randint(1, 100).
- Cuenta intentos y ofrece pistas 'más grande/pequeño'.
- Valida que la entrada sea int.

**🧱 Código base de inicio**

```python
import random

def main():
    objetivo = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            intento = int(input("Adivina un número (1-100): "))
        except ValueError:
            print("Por favor ingresa un número entero.")
            continue
        intentos += 1
        if intento == objetivo:
            print(f"¡Correcto! Lo lograste en {intentos} intentos.")
            break
        print("Más grande" if intento < objetivo else "Más pequeño")

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Añade niveles de dificultad
- Registra puntajes
- Límite de tiempo por intento

---

## Proyecto 3: Conversor de unidades

**🎯 Objetivo**

Conversor de temperaturas (C↔F) con interfaz de consola simple.

**🧩 Descripción interactiva**

- Vamos a construirlo paso a paso ✅
- Prueba, rompe cosas y vuelve a intentar 😄
- Mantén funciones pequeñas y fáciles de probar.

**💡 Pistas**

- Separa funciones c_to_f y f_to_c.
- Normaliza entradas (upper/strip).
- Redondea a 2 decimales.

**🧱 Código base de inicio**

```python
def c_to_f(c): return c * 9/5 + 32
def f_to_c(f): return (f - 32) * 5/9

def main():
    print("Conversor de temperatura")
    unidad = input("Convierte a (C/F): ").strip().upper()
    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("Ingresa un número válido.")
        return
    if unidad == "F":
        print(f"{valor} °C -> {round(c_to_f(valor), 2)} °F")
    elif unidad == "C":
        print(f"{valor} °F -> {round(f_to_c(valor), 2)} °C")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Añade más unidades (longitud, masa)
- Integra menú interactivo
- Pruebas unitarias básicas

---

## Proyecto 4: Contador de palabras

**🎯 Objetivo**

Lee un texto y muestra conteos y top de palabras más frecuentes.

**🧩 Descripción interactiva**

- Vamos a construirlo paso a paso ✅
- Prueba, rompe cosas y vuelve a intentar 😄
- Mantén funciones pequeñas y fáciles de probar.

**💡 Pistas**

- Usa regex para tokenizar con tildes.
- Counter.most_common para el top.
- Permite al usuario elegir top N.

**🧱 Código base de inicio**

```python
import re
from collections import Counter

def limpiar_texto(t):
    return re.findall(r"[\wáéíóúüñ]+", t.lower())

def main():
    texto = input("Ingresa un texto: ")
    palabras = limpiar_texto(texto)
    print(f"Número de palabras: {len(palabras)}")
    conteo = Counter(palabras).most_common(10)
    print("Top 10 palabras:")
    for w, c in conteo:
        print(f"{w}: {c}")

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Exporta resultados a CSV
- Excluye stopwords
- Gráfica de frecuencias

---

## Proyecto 5: Gestor de tareas (To-Do)

**🎯 Objetivo**

CRUD simple de tareas persistidas en JSON.

**🧩 Descripción interactiva**

- Vamos a construirlo paso a paso ✅
- Prueba, rompe cosas y vuelve a intentar 😄
- Mantén funciones pequeñas y fáciles de probar.

**💡 Pistas**

- Pathlib para manejo de archivos.
- JSON con indentado para legibilidad.
- Estructura de bucle de comandos.

**🧱 Código base de inicio**

```python
import json
from pathlib import Path

ARCHIVO = Path("tareas.json")

def cargar():
    if ARCHIVO.exists():
        return json.loads(ARCHIVO.read_text(encoding="utf-8"))
    return []

def guardar(tareas):
    ARCHIVO.write_text(json.dumps(tareas, ensure_ascii=False, indent=2), encoding="utf-8")

def agregar(tareas, desc):
    tareas.append({"desc": desc, "done": False})

def listar(tareas):
    for i, t in enumerate(tareas, 1):
        estado = "✅" if t["done"] else "⏳"
        print(f"{i}. {estado} {t['desc']}")

def completar(tareas, idx):
    tareas[idx]["done"] = True

def main():
    tareas = cargar()
    while True:
        cmd = input("(a)gregar, (l)istar, (c)ompletar, (q)uitar, (x) salir: ").strip().lower()
        if cmd == "a":
            desc = input("Descripción: ").strip()
            if desc: agregar(tareas, desc); guardar(tareas)
        elif cmd == "l":
            listar(tareas)
        elif cmd == "c":
            try:
                idx = int(input("Índice a completar: ")) - 1
                completar(tareas, idx); guardar(tareas)
            except Exception:
                print("Índice inválido.")
        elif cmd == "q":
            try:
                idx = int(input("Índice a eliminar: ")) - 1
                tareas.pop(idx); guardar(tareas)
            except Exception:
                print("Índice inválido.")
        elif cmd == "x":
            break
        else:
            print("Comando no reconocido.")

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Agregar fechas límite
- Filtro por estado
- Persistencia en SQLite

---
