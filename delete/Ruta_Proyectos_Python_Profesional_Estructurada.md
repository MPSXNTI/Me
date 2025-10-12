# Ruta de Proyectos en Python — Profesional / Estructurada

> 15 proyectos, organizados por niveles. Cada nivel está colapsable con <details> y <summary>.

<details>
  <summary>📘 Nivel 1 – Fundamentos del lenguaje</summary>


### Proyecto 1: Calculadora básica

**🎯 Objetivo**

Implementar operaciones aritméticas con validación de entrada y manejo de errores.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

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


### Proyecto 2: Adivina el número

**🎯 Objetivo**

El programa genera un número secreto; el usuario intenta adivinar con pistas incrementalmente.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

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


### Proyecto 3: Conversor de unidades

**🎯 Objetivo**

Conversor de temperaturas (C↔F) con interfaz de consola simple.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

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


### Proyecto 4: Contador de palabras

**🎯 Objetivo**

Lee un texto y muestra conteos y top de palabras más frecuentes.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

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


</details>

<details>
  <summary>📘 Nivel 2 – Estructuras y archivos</summary>


### Proyecto 5: Gestor de tareas (To-Do)

**🎯 Objetivo**

CRUD simple de tareas persistidas en JSON.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

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


### Proyecto 6: Agenda de contactos

**🎯 Objetivo**

Registro y búsqueda de contactos en CSV.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- DictWriter/DictReader para CSV.
- Encabezados definidos por constante.
- Búsqueda simple por cadena.

**🧱 Código base de inicio**

```python
import csv
from pathlib import Path

ARCHIVO = Path("contactos.csv")
CAMPOS = ["nombre", "telefono", "email"]

def guardar_contacto(contacto):
    existe = ARCHIVO.exists()
    with ARCHIVO.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        if not existe:
            writer.writeheader()
        writer.writerow(contacto)

def buscar_contactos(q):
    if not ARCHIVO.exists(): return []
    with ARCHIVO.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [r for r in reader if q.lower() in (r["nombre"]+r["email"]).lower()]

def main():
    while True:
        op = input("(n)uevo, (b)uscar, (s)alir: ").strip().lower()
        if op == "n":
            nombre = input("Nombre: "); tel = input("Teléfono: "); email = input("Email: ")
            guardar_contacto({"nombre": nombre, "telefono": tel, "email": email})
            print("Guardado.")
        elif op == "b":
            q = input("Buscar: "); resultados = buscar_contactos(q)
            for r in resultados: print(r)
        elif op == "s":
            break

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Exportar/Importar JSON
- Validación de email/teléfono
- Interfaz con Typer o argparse

---


### Proyecto 7: Analizador de texto (archivo)

**🎯 Objetivo**

Procesa un archivo .txt y entrega métricas y top palabras.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- Path.read_text con encoding.
- Regex para tokenizar.
- Counter para top 20.

**🧱 Código base de inicio**

```python
from collections import Counter
from pathlib import Path
import re

def tokens(path):
    texto = Path(path).read_text(encoding="utf-8", errors="ignore").lower()
    return re.findall(r"[\wáéíóúüñ]+", texto)

def main():
    archivo = input("Ruta del archivo .txt: ").strip()
    palabras = tokens(archivo)
    print(f"Total palabras: {len(palabras)}")
    for w, c in Counter(palabras).most_common(20):
        print(f"{w}: {c}")

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Soporte a múltiples archivos
- Reporte a Markdown
- CLI con opciones (ruta, top N)

---


</details>

<details>
  <summary>📘 Nivel 3 – Programas conectados (APIs/Librerías)</summary>


### Proyecto 8: Generador de contraseñas

**🎯 Objetivo**

Crea contraseñas seguras configurables.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- Módulo string para alfabetos.
- random.shuffle / choice.
- Parámetros opcionales y valores por defecto.

**🧱 Código base de inicio**

```python
import random, string

def generar(longitud=12, mayus=True, numeros=True, simbolos=True):
    base = list(string.ascii_lowercase)
    if mayus: base += list(string.ascii_uppercase)
    if numeros: base += list(string.digits)
    if simbolos: base += list("!@#$%^&*()-_=+[]{};:,.?/")
    random.shuffle(base)
    return "".join(random.choice(base) for _ in range(longitud))

if __name__ == "__main__":
    print(generar(16))
```

**🚀 Nivel Plus**

- Garantiza al menos un carácter de cada tipo
- Interfaz CLI con argparse
- Medidor de entropía

---


### Proyecto 9: Clima actual con API

**🎯 Objetivo**

Consulta OpenWeatherMap y muestra clima por ciudad.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- Variables de entorno para API key.
- Manejo de errores HTTP con raise_for_status.
- Parámetros de idioma y unidades.

**🧱 Código base de inicio**

```python
import os, requests

API_KEY = os.getenv("OPENWEATHER_API_KEY", "TU_API_KEY_AQUI")

def clima(ciudad="Santiago,CL"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": ciudad, "appid": API_KEY, "units": "metric", "lang": "es"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"{ciudad}: {temp}°C, {desc}")

if __name__ == "__main__":
    clima()
```

**🚀 Nivel Plus**

- Cache local por ciudad
- Geolocalización por coordenadas
- Soporte por países múltiples

---


### Proyecto 10: Buscador de sinónimos

**🎯 Objetivo**

Consulta una API gratuita (Datamuse) para obtener sinónimos.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- Construcción de URL dinámica.
- Límites y recortes en los resultados.
- Timeouts y control de errores.

**🧱 Código base de inicio**

```python
import requests

def sinonimos(palabra):
    url = f"https://api.datamuse.com/words?rel_syn={palabra}&lang=es"
    r = requests.get(url, timeout=10); r.raise_for_status()
    return [item["word"] for item in r.json()]

if __name__ == "__main__":
    q = input("Palabra: ").strip()
    print(sinonimos(q)[:20])
```

**🚀 Nivel Plus**

- Añade antónimos/definiciones
- Exporta a CSV
- Interfaz gráfica simple (tkinter)

---


</details>

<details>
  <summary>📘 Nivel 4 – Datos y visualización</summary>


### Proyecto 11: Analizador de gastos personales

**🎯 Objetivo**

Carga un CSV, agrupa por categoría y grafica.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- Asegura tipos numéricos con to_numeric.
- groupby + sum + sort_values.
- Gráfico de barras con etiquetas.

**🧱 Código base de inicio**

```python
import pandas as pd
import matplotlib.pyplot as plt

def main():
    ruta = input("Ruta CSV de gastos: ")
    df = pd.read_csv(ruta)
    # Se esperan columnas: categoria, monto, fecha
    df["monto"] = pd.to_numeric(df["monto"], errors="coerce").fillna(0)
    por_cat = df.groupby("categoria")["monto"].sum().sort_values(ascending=False)
    print(por_cat)
    por_cat.plot(kind="bar")
    plt.title("Gasto por categoría")
    plt.xlabel("Categoría"); plt.ylabel("Monto")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Agrupa por mes
- Dashboard con Streamlit
- Exporta gráficos a PNG

---


### Proyecto 12: Estadísticas de texto

**🎯 Objetivo**

Calcula métricas básicas y palabras frecuentes.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- Regex para tokenización.
- Series de pandas para conteos.
- Medidas como longitud media.

**🧱 Código base de inicio**

```python
import pandas as pd
import re

def palabras(texto):
    return re.findall(r"[\wáéíóúüñ]+", texto.lower())

def main():
    t = input("Texto: ")
    ws = palabras(t)
    s = pd.Series(ws)
    print("Total palabras:", len(ws))
    print("Longitud media:", s.str.len().mean())
    print("Más comunes:")
    print(s.value_counts().head(10))

if __name__ == "__main__":
    main()
```

**🚀 Nivel Plus**

- Lee desde archivo
- Nube de palabras
- Stopwords y stemming

---


</details>

<details>
  <summary>📘 Nivel 5 – Proyectos combinados/avanzados</summary>


### Proyecto 13: Mini juego Piedra, Papel o Tijera

**🎯 Objetivo**

Juego por rondas con marcador.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- Diccionario de reglas GANA_A.
- Validación de opciones.
- Marcador acumulado.

**🧱 Código base de inicio**

```python
import random

OPCIONES = ("piedra", "papel", "tijera")
GANA_A = {"piedra": "tijera", "tijera": "papel", "papel": "piedra"}

def jugar(rondas=3):
    jugador_pts = pc_pts = 0
    for _ in range(rondas):
        jug = input("Elige (piedra/papel/tijera): ").strip().lower()
        if jug not in OPCIONES:
            print("Opción inválida."); continue
        pc = random.choice(OPCIONES)
        print(f"PC eligió: {pc}")
        if jug == pc: print("Empate")
        elif GANA_A[jug] == pc: print("¡Ganaste!"); jugador_pts += 1
        else: print("Perdiste"); pc_pts += 1
    print(f"Marcador final -> Tú: {jugador_pts} | PC: {pc_pts}")

if __name__ == "__main__":
    jugar(5)
```

**🚀 Nivel Plus**

- Modo torneo
- Historial a archivo
- Modo multijugador local

---


### Proyecto 14: Chatbot básico

**🎯 Objetivo**

Respuestas basadas en reglas simples.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- Normalización de entradas.
- Búsqueda por inclusión de palabras clave.
- Ciclo interactivo de conversación.

**🧱 Código base de inicio**

```python
REGLAS = {
    "hola": "¡Hola! ¿En qué puedo ayudarte?",
    "adios": "¡Hasta luego!",
    "ayuda": "Puedo responder saludos y despedidas por ahora."
}

def responder(msg):
    m = msg.lower().strip()
    for k, v in REGLAS.items():
        if k in m:
            return v
    return "No entendí, ¿puedes reformular?"

if __name__ == "__main__":
    while True:
        txt = input("> ")
        if txt.lower() in ("salir", "exit", "quit"):
            break
        print(responder(txt))
```

**🚀 Nivel Plus**

- Persistencia de contexto
- Archivo de intenciones YAML/JSON
- Interfaz web con Flask/FastAPI

---


### Proyecto 15: Organizador automático de archivos

**🎯 Objetivo**

Ordena archivos por extensión en carpetas.

**🧩 Descripción interactiva**

- Entrada/salida bien definidas.
- Validaciones necesarias.
- Flujo de ejecución claro (funciones pequeñas y testeables).

**💡 Pistas**

- pathlib para iterar archivos.
- shutil.move para mover.
- Reglas en diccionario.

**🧱 Código base de inicio**

```python
import shutil
from pathlib import Path

REGLAS = {
    ".jpg": "imagenes",
    ".png": "imagenes",
    ".pdf": "documentos",
    ".txt": "texto",
    ".csv": "datos",
}

def organizar(origen="."):
    p = Path(origen)
    for archivo in p.iterdir():
        if archivo.is_file():
            ext = archivo.suffix.lower()
            destino = REGLAS.get(ext, "otros")
            (p / destino).mkdir(exist_ok=True)
            shutil.move(str(archivo), str(p / destino / archivo.name))

if __name__ == "__main__":
    organizar(".")
```

**🚀 Nivel Plus**

- Reglas configurables por YAML
- Logs y dry-run
- Watcher en tiempo real (watchdog)

---


</details>
