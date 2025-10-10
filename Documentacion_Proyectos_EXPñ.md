# Documentación de Proyectos EXP

## Descripción breve de cada archivo
- **readme_Análisis_de_tiempos_de_EXP_por_checkpoints.md**: Notebook convertido a README que calcula tiempos mínimos y máximos para alcanzar checkpoints de EXP, incluyendo explicación para mover la meta total fuera de la tabla y ejemplos de salida.
- **readme_exp_report.md**: Documentación del módulo EXP Report: genera tabla en consola y PDF; incluye explicación de funciones, README del proyecto y código completo del generador.
- **readme_exp_report_tutorial_final_v2.md**: Tutorial final (v2) para generar un PDF de tiempos para alcanzar EXP, con parámetros, ejemplos y todas las celdas de código separadas del notebook.
- **readme_print_console_exp_report.md**: Mini-módulo para imprimir en consola un reporte de EXP; explica funciones auxiliares y muestra ejemplos de uso sin dependencias externas.

---
<details>
<summary>Nombre Archivo: readme_Análisis_de_tiempos_de_EXP_por_checkpoints.md</summary>

# 🎯 **Análisis de tiempos de EXP por checkpoints**

> This README was generated from a Jupyter notebook, keeping the original structure, code, and outputs where possible.

## Table of Contents

    - [🧮 Explicación del código: *Cálculo de tiempos de EXP con checkpoints*](#explicación-del-código-cálculo-de-tiempos-de-exp-con-checkpoints)
      - [1️⃣ Propósito](#1-propósito)
      - [2️⃣ Uso básico](#2-uso-básico)
      - [3️⃣ Notas técnicas](#3-notas-técnicas)
      - [4️⃣ Ejemplo extra](#4-ejemplo-extra)
    - [🧩 Explicación: cómo mover el total (57000) fuera de la tabla](#explicación-cómo-mover-el-total-57000-fuera-de-la-tabla)
      - [1️⃣ Extraer el “total” del final de la lista](#1-extraer-el-total-del-final-de-la-lista)
      - [2️⃣ Calcular los tiempos del total (antes de la tabla)](#2-calcular-los-tiempos-del-total-antes-de-la-tabla)
      - [3️⃣ Excluir el total de la tabla con *slicing*](#3-excluir-el-total-de-la-tabla-con-slicing)
      - [4️⃣ Mantener el formato de tabla](#4-mantener-el-formato-de-tabla)
      - [5️⃣ Por qué esto logra lo que querías](#5-por-qué-esto-logra-lo-que-querías)
      - [6️⃣ Cambios mínimos realizados](#6-cambios-mínimos-realizados)
      - [7️⃣ Consideraciones opcionales](#7-consideraciones-opcionales)
- [🎯 **Análisis de tiempos de EXP por checkpoints**](#análisis-de-tiempos-de-exp-por-checkpoints)
    - [📘 Descripción general](#descripción-general)
  - [⚙️ **1. Parámetros iniciales**](#1-parámetros-iniciales)
- [Checkpoints dados](#checkpoints-dados)
- [Velocidad mínima y máxima (EXP/segundo)](#velocidad-mínima-y-máxima-expsegundo)
  - [⏱️ **2. Cálculo del tiempo total**](#2-cálculo-del-tiempo-total)
- [Calcular tiempo total](#calcular-tiempo-total)
  - [📊 **3. Detalle de tiempos por checkpoint**](#3-detalle-de-tiempos-por-checkpoint)
  - [🧩 **4. Observaciones técnicas**](#4-observaciones-técnicas)
  - [📈 **5. Ejemplo de salida esperada**](#5-ejemplo-de-salida-esperada)
  - [🧠 **6. Interpretación**](#6-interpretación)
  - [🏁 **7. Conclusión**](#7-conclusión)

### 🧮 Explicación del código: *Cálculo de tiempos de EXP con checkpoints*

#### 1️⃣ Propósito  
El objetivo del script es **calcular cuánto tiempo se tarda en alcanzar diferentes cantidades de puntos de experiencia (EXP)**, llamados *checkpoints*, según una tasa de ganancia variable (entre 35 y 45 segundos por cada 60 EXP).  
Esto permite estimar tanto el tiempo **mínimo (jugando rápido)** como el **máximo (jugando lento)** para llegar a cada meta de EXP.

---

#### 2️⃣ Uso básico  
1. Se definen los *checkpoints* (por ejemplo: 1000, 2000, 3125, etc.).  
2. Se establecen las **velocidades mínima y máxima** en EXP por segundo:  
   ```python
   exp_min = 60 / 45   # lento → 1.33 EXP/s
   exp_max = 60 / 35   # rápido → 1.71 EXP/s
   ```
3. El código recorre cada checkpoint, calcula los segundos necesarios según ambas velocidades y convierte el resultado a formato legible (`h:m:s`) mediante la función `segundos_a_hms()`.  
4. Finalmente, imprime una tabla comparativa con tres columnas:
   - Checkpoint (EXP)
   - Tiempo mínimo (jugando rápido)
   - Tiempo máximo (jugando lento)

---

#### 3️⃣ Notas técnicas  
- **Conversión de segundos a formato h:m:s**:  
  ```python
  def segundos_a_hms(segundos):
      h = int(segundos // 3600)
      m = int((segundos % 3600) // 60)
      s = int(segundos % 60)
      return f"{h}h {m}m {s}s" if h > 0 else f"{m}m {s}s"
  ```
  Esta función transforma los segundos totales en horas, minutos y segundos, y omite las horas si son cero.

- **Cálculo del tiempo:**  
  - Tiempo mínimo = `checkpoint / exp_max`  
  - Tiempo máximo = `checkpoint / exp_min`  

- **Formato de salida:**  
  El uso de `f-strings` con alineación (`:<15`) produce una tabla limpia y legible.

---

#### 4️⃣ Ejemplo extra  
Si añadimos un nuevo checkpoint de **10,000 EXP**, el código calcularía:  
```python
cp = 10000
t_min = cp / exp_max   # rápido
t_max = cp / exp_min   # lento
print(segundos_a_hms(t_min), segundos_a_hms(t_max))
```
👉 Resultado aproximado:  
`1h 37m 55s` (rápido) — `2h 5m 15s` (lento)


```python
# Cálculo de tiempos de EXP con checkpoints

# Checkpoints dados
checkpoints = [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375, 57000]

# Velocidad mínima y máxima (EXP/segundo)
exp_min = 60 / 45   # 1.33 EXP/s (lento)
exp_max = 60 / 35   # 1.71 EXP/s (rápido)

def segundos_a_hms(segundos):
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    return f"{h}h {m}m {s}s" if h > 0 else f"{m}m {s}s"

print(f"{'Checkpoint (EXP)':<15} {'Tiempo mínimo':<15} {'Tiempo máximo':<15}")
print("-" * 45)

for cp in checkpoints:
    t_min = cp / exp_max  # más rápido
    t_max = cp / exp_min  # más lento
    print(f"{cp:<15} {segundos_a_hms(t_min):<15} {segundos_a_hms(t_max):<15}")

```

<details>
<summary><strong>Output</strong></summary>


```
Checkpoint (EXP) Tiempo mínimo   Tiempo máximo  
---------------------------------------------
1000            9m 43s          12m 30s        
2000            19m 26s         25m 0s         
3125            30m 22s         39m 3s         
4125            40m 6s          51m 33s        
5125            49m 49s         1h 4m 3s       
6250            1h 0m 45s       1h 18m 7s      
7250            1h 10m 29s      1h 30m 37s     
8375            1h 21m 25s      1h 44m 41s     
9375            1h 31m 8s       1h 57m 11s     
10375           1h 40m 52s      2h 9m 41s      
57000           9h 14m 10s      11h 52m 30s
```

</details>

### 🧩 Explicación: cómo mover el total (57000) fuera de la tabla

---

#### 1️⃣ Extraer el “total” del final de la lista
```python
total_exp = checkpoints[-1]
```
- `checkpoints[-1]` toma el **último elemento** de la lista (indexado negativo en Python).  
- Asumimos que la lista está **ordenada de menor a mayor** y que el **último** es la meta total (57 000).  
- Esto es **O(1)** y **no modifica** la lista original.

> 💡 Alternativa más robusta si la lista no siempre está ordenada:
> ```python
> total_exp = max(checkpoints)
> ```
> (Así no dependes del orden de los elementos.)

---

#### 2️⃣ Calcular los tiempos del total (antes de la tabla)
```python
t_min_total = total_exp / exp_max   # tiempo en escenario rápido
t_max_total = total_exp / exp_min   # tiempo en escenario lento
```
- Misma lógica que en la tabla:
  - “Rápido” ⇒ más EXP/seg ⇒ **menos tiempo** ⇒ dividir por `exp_max`.
  - “Lento” ⇒ menos EXP/seg ⇒ **más tiempo** ⇒ dividir por `exp_min`.

Luego se imprime al inicio, antes del detalle:
```python
print(f"Meta total: {total_exp} EXP")
print(f"Tiempo estimado total: {segundos_a_hms(t_min_total)} (mínimo) — {segundos_a_hms(t_max_total)} (máximo)")
print("\nDetalle por checkpoint:\n")
```
De esta forma, el total se muestra **como resumen principal** antes de la tabla.

---

#### 3️⃣ Excluir el total de la tabla con *slicing*
```python
for cp in checkpoints[:-1]:
    ...
```
- `checkpoints[:-1]` devuelve todos los elementos **menos el último**.  
- Así **no repetimos** el 57 000 dentro de la tabla.  
- Esto **no altera** la lista original.

> 💡 Si no sabes cuál es el último o usaste `max(checkpoints)`, puedes eliminarlo así:
> ```python
> total_exp = max(checkpoints)
> cp_list = checkpoints.copy()
> cp_list.remove(total_exp)
> ```
> De esa manera, la variable `cp_list` contiene todos los valores **excepto el total**.

---

#### 4️⃣ Mantener el formato de tabla
```python
print(f"{'Checkpoint (EXP)':<15} {'Tiempo mínimo':<15} {'Tiempo máximo':<15}")
print("-" * 45)
```
- Se mantiene la **alineación de columnas** con `:<15` (f-strings).  
- El bucle sigue calculando los tiempos con la **misma fórmula** y formato legible con `segundos_a_hms()`.

---

#### 5️⃣ Por qué esto logra lo que querías
- El **total se imprime primero** con su rango de tiempo, sirviendo como **resumen general**.  
- La **tabla solo contiene los checkpoints parciales**, ya que excluimos el último elemento del bucle.  
- No se cambia la lógica de cálculo, solo **el orden en que se muestra la información**.

---

#### 6️⃣ Cambios mínimos realizados
- ✅ Nuevo bloque para imprimir el total antes de la tabla.  
- ✅ En el `for`, se usa `checkpoints[:-1]` para **excluir el último elemento**.  
- ❌ Nada más cambia: ni funciones ni fórmulas.

---

#### 7️⃣ Consideraciones opcionales
- Si quieres **resaltar visualmente** el total en la consola, puedes usar ANSI:
  ```python
  BOLD = "\033[1m"; RESET = "\033[0m"
  print(f"{BOLD}Meta total: {total_exp} EXP{RESET}")
  ```
- La función `segundos_a_hms` hace **truncamiento** (`int`).  
  Si prefieres **redondear** los segundos, puedes usar:
  ```python
  segundos = round(segundos)
  ```

---

✅ Con esto consigues que la **meta total se muestre arriba como resumen**, y la **tabla solo detalle los progresos parciales**, manteniendo el formato y la claridad del resultado.


```python
# Cálculo de tiempos de EXP con checkpoints

# Checkpoints dados
checkpoints = [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375, 57000]

# Velocidad mínima y máxima (EXP/segundo)
exp_min = 60 / 45   # 1.33 EXP/s (lento)
exp_max = 60 / 35   # 1.71 EXP/s (rápido)

def segundos_a_hms(segundos):
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    return f"{h}h {m}m {s}s" if h > 0 else f"{m}m {s}s"

# --- Mostrar primero el total final ---
total_exp = checkpoints[-1]
t_min_total = total_exp / exp_max
t_max_total = total_exp / exp_min

print(f"Meta total: {total_exp} EXP")
print(f"Tiempo estimado total: {segundos_a_hms(t_min_total)} (mínimo) — {segundos_a_hms(t_max_total)} (máximo)")
print("\nDetalle por checkpoint:\n")

# --- Mostrar tabla de checkpoints (sin el último valor) ---
print(f"{'Checkpoint (EXP)':<15} {'Tiempo mínimo':<15} {'Tiempo máximo':<15}")
print("-" * 45)

for cp in checkpoints[:-1]:  # Excluye el último
    t_min = cp / exp_max
    t_max = cp / exp_min
    print(f"{cp:<15} {segundos_a_hms(t_min):<15} {segundos_a_hms(t_max):<15}")

```

<details>
<summary><strong>Output</strong></summary>


```
Meta total: 57000 EXP
Tiempo estimado total: 9h 14m 10s (mínimo) — 11h 52m 30s (máximo)

Detalle por checkpoint:

Checkpoint (EXP) Tiempo mínimo   Tiempo máximo  
---------------------------------------------
1000            9m 43s          12m 30s        
2000            19m 26s         25m 0s         
3125            30m 22s         39m 3s         
4125            40m 6s          51m 33s        
5125            49m 49s         1h 4m 3s       
6250            1h 0m 45s       1h 18m 7s      
7250            1h 10m 29s      1h 30m 37s     
8375            1h 21m 25s      1h 44m 41s     
9375            1h 31m 8s       1h 57m 11s     
10375           1h 40m 52s      2h 9m 41s
```

</details>

# 🎯 **Análisis de tiempos de EXP por checkpoints**

---

### 📘 Descripción general
Este notebook calcula el **tiempo estimado necesario para alcanzar distintos puntos de experiencia (EXP)**,  
considerando una velocidad de ganancia variable entre **35 y 45 segundos por cada 60 EXP**.  

El objetivo es estimar el rango de tiempo —entre el **mínimo (más rápido)** y el **máximo (más lento)**—  
necesario para alcanzar cada checkpoint y la **meta total final de 57,000 EXP**.  

---

## ⚙️ **1. Parámetros iniciales**
Aquí se definen los valores base del cálculo:  
- Lista de *checkpoints* (valores de EXP objetivo).  
- Velocidades mínima y máxima de ganancia.  
- Función auxiliar para convertir segundos a un formato legible (`h:m:s`).

```python
# Checkpoints dados
checkpoints = [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375, 57000]

# Velocidad mínima y máxima (EXP/segundo)
exp_min = 60 / 45   # 1.33 EXP/s (lento)
exp_max = 60 / 35   # 1.71 EXP/s (rápido)

def segundos_a_hms(segundos):
    """Convierte una cantidad de segundos en formato h:m:s"""
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    return f"{h}h {m}m {s}s" if h > 0 else f"{m}m {s}s"
```

---

## ⏱️ **2. Cálculo del tiempo total**
Antes de mostrar el detalle, se calcula el **tiempo total estimado para llegar a la meta final (57,000 EXP)**  
en los escenarios más rápido y más lento.

```python
# Calcular tiempo total
total_exp = checkpoints[-1]
t_min_total = total_exp / exp_max
t_max_total = total_exp / exp_min

print(f"Meta total: {total_exp} EXP")
print(f"Tiempo estimado total: {segundos_a_hms(t_min_total)} (mínimo) — {segundos_a_hms(t_max_total)} (máximo)")
```

---

## 📊 **3. Detalle de tiempos por checkpoint**
En esta tabla se muestra cuánto tarda en alcanzarse cada checkpoint individual,  
excluyendo la meta final (que ya se muestra arriba como resumen general).

```python
print("\nDetalle por checkpoint:\n")
print(f"{'Checkpoint (EXP)':<15} {'Tiempo mínimo':<15} {'Tiempo máximo':<15}")
print("-" * 45)

for cp in checkpoints[:-1]:  # excluye el total final
    t_min = cp / exp_max
    t_max = cp / exp_min
    print(f"{cp:<15} {segundos_a_hms(t_min):<15} {segundos_a_hms(t_max):<15}")
```

---

## 🧩 **4. Observaciones técnicas**
- El cálculo usa los intervalos de ganancia de **35–45 segundos por 60 EXP**.  
- `exp_min` y `exp_max` representan la **velocidad de ganancia de experiencia** (EXP/seg).  
- La función `segundos_a_hms()` formatea los segundos a un formato legible (`h:m:s`).  
- El último valor de la lista (`57000`) se imprime **antes** de la tabla, como **meta general**.  
- El uso de `checkpoints[:-1]` evita duplicar el total dentro de la tabla.  

---

## 📈 **5. Ejemplo de salida esperada**
```
Meta total: 57000 EXP
Tiempo estimado total: 9h 14m 10s (mínimo) — 11h 52m 30s (máximo)

Detalle por checkpoint:

Checkpoint (EXP) Tiempo mínimo   Tiempo máximo  
---------------------------------------------
1000            9m 43s          12m 30s        
2000            19m 26s         25m 0s         
3125            30m 22s         39m 3s         
4125            40m 6s          51m 33s        
5125            49m 49s         1h 4m 3s       
6250            1h 0m 45s       1h 18m 7s      
7250            1h 10m 29s      1h 30m 37s     
8375            1h 21m 25s      1h 44m 41s     
9375            1h 31m 8s       1h 57m 11s     
10375           1h 40m 52s      2h 9m 41s      
```

---

## 🧠 **6. Interpretación**
Cada checkpoint indica el tiempo acumulado necesario para alcanzar una cierta cantidad de EXP,  
dentro de un rango de velocidad posible.  
Esto permite estimar el **ritmo de progreso** en sesiones o etapas.

---

## 🏁 **7. Conclusión**
El tiempo total estimado para alcanzar los **57,000 EXP** varía entre:  
- 🔹 **9 horas 14 minutos (jugando rápido)**  
- 🔹 **11 horas 52 minutos (jugando lento)**  

Estos cálculos permiten **planificar mejor el progreso** dentro de un sistema o juego basado en experiencia,  
evaluando cuánto esfuerzo o tiempo requiere llegar a una meta concreta.

---

✨ *Notebook preparado y documentado por [SXNTI / Proyecto Peluca]* ✨


---

_Auto-converted on build time. If you need tweaks (e.g., hide code, keep only outputs, or reorganize sections), let me know._

</details>

<details>
<summary>Nombre Archivo: readme_exp_report.md</summary>

# EXP Report — Generador de tabla y PDF

Este proyecto calcula cuánto tiempo tardarías en alcanzar una meta de **EXP** (experiencia) dado:
- EXP ganado por ciclo
- Rango de duración (en segundos) de cada ciclo
- Checkpoints opcionales para ver avances parciales

Produce salida **en consola** y un **PDF** con una tabla de detalle.

---

## 1) Explicación de cada función (guion de 5 puntos)

> Formato: **1) Propósito, 2) Uso básico, 3) Notas técnicas, 4) Ejemplo extra, 5) Relación con otras partes.**

### ` _register_fonts() -> str`
1. **Propósito:** Registrar una tipografía TrueType (DejaVuSans) para ReportLab y devolver el nombre a usar en el PDF; si falla, usa *Helvetica*.
2. **Uso básico:** Se invoca al cargar el módulo para inicializar `FONT_NAME`.
3. **Notas técnicas:** Usa `reportlab.pdfbase.pdfmetrics.registerFont` y `TTFont`. Captura excepciones para asegurar un fallback.
4. **Ejemplo extra:** Si incluyes `DejaVuSans.ttf` junto al script, podrás renderizar caracteres latinos y símbolos sin problemas.
5. **Relación:** El valor devuelto se usa en `_on_page` para fijar la fuente del encabezado/pie del PDF.

### `format_hms(seconds: int) -> str`
1. **Propósito:** Convertir segundos enteros a formato `HH:MM:SS`.
2. **Uso básico:** `format_hms(3723)  # "01:02:03"`
3. **Notas técnicas:** Redondea a entero, usa divisiones enteras y módulos para horas, minutos y segundos.
4. **Ejemplo extra:** Formatear tiempos mínimos y máximos acumulados por checkpoint.
5. **Relación:** Utilizada en `_print_debug_header`, `_print_detail_table` y `generate_exp_report` para presentar tiempos.

### `es_miles(n: int) -> str`
1. **Propósito:** Formatear números enteros con separador de miles como punto (estilo “1.234.567”).
2. **Uso básico:** `es_miles(57000)  # "57.000"`
3. **Notas técnicas:** Usa `format(n, ",")` y reemplaza comas por puntos.
4. **Ejemplo extra:** Mostrar “ciclos necesarios” y “checkpoints” de manera legible.
5. **Relación:** Empleado en todos los resúmenes/textos donde aparecen enteros grandes.

### `_ensure_dir_for(path: str) -> None`
1. **Propósito:** Crear el directorio destino si no existe antes de escribir el PDF.
2. **Uso básico:** Internamente en `generate_exp_report`.
3. **Notas técnicas:** `os.path.dirname/os.path.abspath` y `os.makedirs(..., exist_ok=True)`.
4. **Ejemplo extra:** Si pasas `reports/out.pdf`, creará `reports/` automáticamente.
5. **Relación:** Previene errores de E/S al guardar PDFs.

### `_validate_inputs(...) -> List[int]`
Parámetros: `total_exp`, `exp_per_cycle`, `min_sec_per_cycle`, `max_sec_per_cycle`, `detail_checkpoints`

1. **Propósito:** Validar tipos y rangos; normalizar y ordenar los checkpoints si existen.
2. **Uso básico:** Llamada temprana por `_compute_plan` y `generate_exp_report`.
3. **Notas técnicas:** Exige `int` y `> 0`; asegura `min_sec_per_cycle <= max_sec_per_cycle`; convierte `detail_checkpoints` a lista ordenada única.
4. **Ejemplo extra:** Si pasas `[500, -1, 500, 999999]`, devuelve `[500]` (y el resto se filtra en `_compute_plan` si excede el total).
5. **Relación:** Base para la consistencia del plan de cálculo.

### `_on_page(canvas, doc, title_text: str, tz_name: str)`
1. **Propósito:** Dibujar encabezado y pie de página con fecha/hora y número de página en cada página del PDF.
2. **Uso básico:** Callback `onFirstPage`/`onLaterPages` de `SimpleDocTemplate.build`.
3. **Notas técnicas:** Usa `ZoneInfo` para zona horaria, `canvas.drawString/drawRightString`, y la fuente `FONT_NAME`.
4. **Ejemplo extra:** Cambia `tz_name` a `"UTC"` si necesitas hora universal.
5. **Relación:** Integrado por `generate_exp_report` durante el render del PDF.

### `_compute_plan(..., checkpoint_step=10000, max_detail_rows=300, include_total_in_table=False) -> dict`
1. **Propósito:** Calcular el plan de progreso: ciclos, tiempos mínimos/máximos y la lista final de checkpoints a mostrar.
2. **Uso básico:** Es el núcleo de cómputo para consola y PDF.
3. **Notas técnicas:** 
   - `cycles_needed = ceil(total_exp / exp_per_cycle)`  
   - Si no se pasan checkpoints, genera automáticos cada `checkpoint_step` hasta el total (“modo auto”).  
   - Limita filas a `max_detail_rows` aplicando muestreo.
   - Puede añadir el `total_exp` como fila final si `include_total_in_table=True`.
4. **Ejemplo extra:** Con `total_exp=57_000, exp_per_cycle=60` → `cycles_needed=950`.
5. **Relación:** Insumo directo para `_print_*` y `generate_exp_report`.

### `_print_debug_header(d: dict)`
1. **Propósito:** Imprimir en consola un resumen del plan (total, ciclos, tiempos, avisos).
2. **Uso básico:** Llamado por `debug_exp_report`.
3. **Notas técnicas:** Usa `es_miles` y `format_hms` para legibilidad.
4. **Ejemplo extra:** Muestra un aviso si hubo checkpoints filtrados.
5. **Relación:** Complemento textual previo a la tabla de detalle.

### `_print_detail_table(checkpoints, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle)`
1. **Propósito:** Imprimir una tabla alineada con tiempos para cada checkpoint.
2. **Uso básico:** Llamado por `debug_exp_report`.
3. **Notas técnicas:** Calcula `ceil(cp / exp_per_cycle)` para ciclos por fila; muestra tiempos acumulados min/max.
4. **Ejemplo extra:** Sirve para una “vista rápida” cuando no necesitas PDF.
5. **Relación:** Presentación en consola de los datos de `_compute_plan`.

### `debug_exp_report(..., return_data=False, verbose=True)`
1. **Propósito:** Orquestar el flujo de depuración en consola (encabezado + tabla), y opcionalmente devolver los datos.
2. **Uso básico:** `debug_exp_report(57000, 60, 35, 45, [1000, 2000])`
3. **Notas técnicas:** Pasa parámetros de granularidad (`checkpoint_step`, `max_detail_rows`) y `include_total_in_table`.
4. **Ejemplo extra:** Con `return_data=True` obtienes el diccionario para integrarlo en otra app.
5. **Relación:** Es la “API de consola”; la versión PDF es `generate_exp_report`.

### `print_console_exp_report(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints=None)`
1. **Propósito:** Atajo simple para imprimir el reporte en consola con valores por defecto razonables.
2. **Uso básico:** `print_console_exp_report(57000, 60, 35, 45, checkpoints)`
3. **Notas técnicas:** Llama directamente a `debug_exp_report` con `verbose=True`.
4. **Ejemplo extra:** Útil como entrypoint en scripts mínimos.
5. **Relación:** Capa de conveniencia sobre `debug_exp_report`.

### `generate_exp_report(..., filename=None, include_question=True, ..., tz_name="America/Santiago", return_data=False) -> str | (str, dict)`
1. **Propósito:** Generar el **PDF** con encabezado, resumen y tabla de checkpoints.
2. **Uso básico:** 
   ```python
   pdf = generate_exp_report(57000, 60, 35, 45, [1000,2000], question_suffix="")
   ```
3. **Notas técnicas:** 
   - Si `filename` es `None`, crea `exp_report_YYYYMMDD_HHMM.pdf` en la zona horaria dada.
   - Usa ReportLab (`SimpleDocTemplate`, `Table`, `Paragraph`) y callbacks `_on_page`.
   - `return_data=True` devuelve `(ruta_pdf, dict_resumen)`.
4. **Ejemplo extra:** Pasa `detail_checkpoints=None` para modo auto cada 10.000 EXP; ajusta `checkpoint_step`.
5. **Relación:** Es la “API PDF”; comparte la lógica de `_compute_plan` con la versión de consola.

---

## 2) README completo del proyecto

### Propósito del proyecto
Calcular y **reportar** (consola + PDF) el tiempo necesario para alcanzar una meta de EXP, mostrando además avances por checkpoints.

### Requisitos
- Python 3.10+ (se usa `zoneinfo`, parte de la librería estándar moderna).
- Paquete **ReportLab** para generar PDFs.

### Instalación
```bash
pip install reportlab
```

### Uso básico
```python
from exp_report import print_console_exp_report, generate_exp_report

# Consola
print_console_exp_report(57000, 60, 35, 45, [1000,2000,3125,4125,5125,6250,7250,8375,9375,10375])

# PDF
pdf_path = generate_exp_report(
    57000, 60, 35, 45,
    [1000,2000,3125,4125,5125,6250,7250,8375,9375,10375],
    question_suffix=""
)
print("PDF generado en:", pdf_path)
```

### Dependencias
- `reportlab`

### Ejemplos de ejecución
- **Consola:** imprimirá un resumen y una tabla con tiempos mínimos y máximos acumulados.
- **PDF:** generará `exp_report_YYYYMMDD_HHMM.pdf` con encabezado, resumen y la tabla detallada.  
  Si no existe el directorio del archivo de salida, se creará automáticamente.

---

## 3) Código completo (incluido tal cual)

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas as canvas_mod
from reportlab.lib.units import mm
from zoneinfo import ZoneInfo
import os, math
from datetime import datetime
from typing import Iterable, List, Optional, Tuple, Dict, Any


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def _register_fonts() -> str:
    try:
        pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))
        return "DejaVu"
    except Exception:
        return "Helvetica"

FONT_NAME = _register_fonts()


def format_hms(seconds: int) -> str:
    seconds = int(round(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def es_miles(n: int) -> str:
    s = f"{int(n):,}"
    return s.replace(",", ".")


def _ensure_dir_for(path: str) -> None:
    directory = os.path.dirname(os.path.abspath(path))
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def _validate_inputs(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]]
) -> List[int]:
    for name, val in [
        ("total_exp", total_exp),
        ("exp_per_cycle", exp_per_cycle),
        ("min_sec_per_cycle", min_sec_per_cycle),
        ("max_sec_per_cycle", max_sec_per_cycle),
    ]:
        if not isinstance(val, int):
            raise TypeError(f"{name} debe ser int.")
        if val <= 0:
            raise ValueError(f"{name} debe ser > 0.")
    if min_sec_per_cycle > max_sec_per_cycle:
        raise ValueError("min_sec_per_cycle no puede ser mayor que max_sec_per_cycle.")
    if detail_checkpoints is None:
        return []
    cps = sorted({int(x) for x in detail_checkpoints if int(x) > 0})
    return cps


def _on_page(canvas: canvas_mod.Canvas, doc, title_text: str, tz_name: str):
    canvas.saveState()
    canvas.setFont(FONT_NAME, 9)
    canvas.drawString(15 * mm, 285 * mm, title_text)
    now_str = datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%d %H:%M")
    page_str = f"Generado: {now_str}  |  Página {doc.page}"
    canvas.drawRightString(200 * mm, 10 * mm, page_str)
    canvas.restoreState()


def _compute_plan(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]],
    *,
    checkpoint_step: int = 10_000,
    max_detail_rows: int = 300,
    include_total_in_table: bool = False,
) -> Dict[str, Any]:
    _validate_inputs(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints)
    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle
    filtered_notice = None
    auto_mode = (detail_checkpoints is None)
    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        cps = list(range(checkpoint_step, last + 1, checkpoint_step))
        if include_total_in_table and (not cps or cps[-1] != total_exp):
            cps.append(total_exp)
    else:
        cps = sorted({int(x) for x in detail_checkpoints if int(x) > 0})
        over = [x for x in cps if x > total_exp]
        if over:
            filtered_notice = f"Aviso: se ignoraron checkpoints > total ({over})"
        cps = [x for x in cps if x <= total_exp]
        if include_total_in_table and (not cps or cps[-1] != total_exp):
            cps.append(total_exp)
    if len(cps) > max_detail_rows:
        keep = max_detail_rows - (1 if include_total_in_table else 0)
        step = max(1, len(cps) // keep)
        reduced = cps[::step]
        if len(reduced) > keep:
            reduced = reduced[:keep]
        cps = reduced + ([total_exp] if include_total_in_table and (not reduced or reduced[-1] != total_exp) else [])
    return {
        "total_exp": total_exp, "exp_per_cycle": exp_per_cycle,
        "min_sec_per_cycle": min_sec_per_cycle, "max_sec_per_cycle": max_sec_per_cycle,
        "cycles_exact": cycles_exact, "cycles_needed": cycles_needed,
        "min_total_sec": min_total, "max_total_sec": max_total,
        "checkpoints": cps, "filtered_notice": filtered_notice, "auto_mode": auto_mode,
    }

def _print_debug_header(d: Dict[str, Any]):
    print("=== Debug EXP Report ===")
    print(f"total_exp: {es_miles(d['total_exp'])}")
    print(f"exp_per_cycle: {d['exp_per_cycle']}")
    print(f"Ciclos necesarios (ceil): {d['cycles_needed']}\n")
    print(f"min_sec_per_cycle: {d['min_sec_per_cycle']}")
    print(f"Tiempo total mínimo: {format_hms(d['min_total_sec'])}\n")
    print(f"max_sec_per_cycle: {d['max_sec_per_cycle']}")
    print(f"Tiempo total máximo: {format_hms(d['max_total_sec'])}\n")
    if d.get("filtered_notice"): print(d["filtered_notice"])

def _print_detail_table(checkpoints: List[int], exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int):
    headers = ("Checkpoint", "Ciclos hasta aquí", "Tiempo mínimo", "Tiempo máximo")
    col_w = (14, 20, 16, 16)
    def fmt_row(c1, c2, c3, c4):
        return (f"{str(c1):>{col_w[0]}} {str(c2):>{col_w[1]}} {str(c3):>{col_w[2]}} {str(c4):>{col_w[3]}}")
    print(fmt_row(*headers))
    print("-" * sum(col_w) + "-" * 3)
    for cp in checkpoints:
        cycles_here = math.ceil(cp / exp_per_cycle)
        min_here = cycles_here * min_sec_per_cycle
        max_here = cycles_here * max_sec_per_cycle
        print(fmt_row(es_miles(cp), es_miles(cycles_here), format_hms(min_here), format_hms(max_here)))


def debug_exp_report(
    total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None, *, checkpoint_step: int = 10_000,
    max_detail_rows: int = 300, include_total_in_table: bool = False, return_data: bool = False, verbose: bool = True):
    d = _compute_plan(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle,
                      detail_checkpoints, checkpoint_step=checkpoint_step, max_detail_rows=max_detail_rows,
                      include_total_in_table=include_total_in_table)
    if verbose:
        _print_debug_header(d)
        _print_detail_table(d["checkpoints"], d["exp_per_cycle"], d["min_sec_per_cycle"], d["max_sec_per_cycle"])
    return d if return_data else None

def print_console_exp_report(total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
                             detail_checkpoints: Optional[Iterable[int]] = None):
    debug_exp_report(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle,
                     detail_checkpoints, include_total_in_table=False, return_data=False, verbose=True)


def generate_exp_report(
    total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None, filename: Optional[str] = None, include_question: bool = True,
    *, checkpoint_step: int = 10_000, max_detail_rows: int = 300, question_suffix: str = "Muéstralo en una tabla y en PDF.",
    tz_name: str = "America/Santiago", return_data: bool = False
) -> str | Tuple[str, Dict[str, Any]]:
    _validate_inputs(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints)
    d = _compute_plan(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints,
                      checkpoint_step=checkpoint_step, max_detail_rows=max_detail_rows, include_total_in_table=False)
    if not filename:
        now = datetime.now(ZoneInfo(tz_name)).strftime("%Y%m%d_%H%M")
        filename = f"exp_report_{now}.pdf"
    _ensure_dir_for(filename)
    styles = getSampleStyleSheet()
    style_h1 = styles["Title"]; style_p = styles["BodyText"]
    doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=18*mm, rightMargin=18*mm, topMargin=18*mm, bottomMargin=18*mm)
    elements = []
    title_text = "Reporte de EXP"; elements.append(Paragraph(title_text, style_h1)); elements.append(Spacer(1, 6))
    if include_question:
        q_text = f"Meta: {es_miles(d['total_exp'])} EXP @ {d['exp_per_cycle']} EXP/ciclo. {question_suffix}"
        elements.append(Paragraph(q_text, style_p)); elements.append(Spacer(1, 8))
    resumen = [
        f"<b>Total EXP:</b> {es_miles(d['total_exp'])}",
        f"<b>Ciclos necesarios (ceil):</b> {es_miles(d['cycles_needed'])}",
        f"<b>Tiempo total:</b> {format_hms(d['min_total_sec'])} — {format_hms(d['max_total_sec'])}",
        f"<b>Duración por ciclo (seg):</b> {min_sec_per_cycle} — {max_sec_per_cycle}",
    ]
    elements.append(Paragraph("<br/>".join(resumen), style_p)); elements.append(Spacer(1, 10))
    if d.get("filtered_notice"):
        elements.append(Paragraph(f"<i>{d['filtered_notice']}</i>", style_p)); elements.append(Spacer(1, 6))
    cps = d["checkpoints"]
    data = [["Checkpoint", "Ciclos hasta aquí", "Tiempo mínimo", "Tiempo máximo"]]
    for cp in cps:
        cycles_here = math.ceil(cp / d["exp_per_cycle"])
        min_here = cycles_here * d["min_sec_per_cycle"]; max_here = cycles_here * d["max_sec_per_cycle"]
        data.append([es_miles(cp), es_miles(cycles_here), format_hms(min_here), format_hms(max_here)])
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("FONTSIZE", (0,0), (-1,0), 12),
        ("BOTTOMPADDING", (0,0), (-1,0), 12),
        ("BACKGROUND", (0,1), (-1,-1), colors.beige),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elements.append(Paragraph("<b>Detalle por checkpoints</b>", style_p)); elements.append(Spacer(1,4)); elements.append(table)
    doc.build(elements, onFirstPage=lambda c,d: _on_page(c,d,title_text,tz_name), onLaterPages=lambda c,d: _on_page(c,d,title_text,tz_name))
    if return_data:
        out = {
            "total_exp": d["total_exp"], "exp_per_cycle": d["exp_per_cycle"],
            "cycles_needed": d["cycles_needed"], "min_total_hms": format_hms(d["min_total_sec"]),
            "max_total_hms": format_hms(d["max_total_sec"]), "checkpoints": cps, "tz_name": tz_name, "filename": filename,
        }
        return filename, out
    return filename
```

---

## 4) Ambas peticiones incluidas en este README
- ✅ Explicación de cada función (sección **1** arriba).
- ✅ README completo del proyecto con propósito, requisitos, instalación, uso básico, dependencias y ejemplos (sección **2**), además del **código completo** (sección **3**).

</details>

<details>
<summary>Nombre Archivo: readme_exp_report_tutorial_final_v2.md</summary>

# Reporte de Tiempo para Alcanzar EXP — Tutorial Final (v2)

Este proyecto genera **un informe en PDF** que estima el **tiempo mínimo y máximo** necesario para alcanzar una cantidad objetivo de puntos de **EXP**, dado el rendimiento por ciclo y el rango de duración por ciclo. Incluye una **tabla de resumen** y una **tabla detallada por checkpoints**.

---

## 📌 Propósito del proyecto
- Calcular **ciclos necesarios** y **tiempos acumulados** (mínimo y máximo) para llegar a un total de EXP.
- Generar un **PDF** con formato claro, encabezados/pies de página, y **tabla de checkpoints** (manual o automática por pasos).
- Servir como **plantilla reutilizable** para distintas consultas de EXP.

## 🧩 Requisitos
- **Python 3.9+** (se usa `zoneinfo` nativo).
- Paquetes:
  - `reportlab`
  - `tzdata` (recomendado en Windows o donde falten datos de zona horaria)
- Sistema con fuentes básicas (Helvetica) disponibles para ReportLab.

## ⚙️ Instalación
```bash
pip install reportlab tzdata
```

> En algunas plataformas, `tzdata` asegura que `America/Santiago` funcione correctamente con `ZoneInfo`.

## 🚀 Uso básico
Ejemplo mínimo de uso en Python:

```python
from exp_report_tutorial_final_v2 import generate_exp_report

# Parámetros principales
total_exp = 57_000
exp_por_ciclo = 60
seg_min_ciclo = 35
seg_max_ciclo = 45

# Genera el PDF
salida = generate_exp_report(
    total_exp,
    exp_por_ciclo,
    seg_min_ciclo,
    seg_max_ciclo,
    filename="reporte_exp.pdf"
)
print("PDF generado en:", salida)
```

## 🔧 Parámetros clave de `generate_exp_report`
- `total_exp` *(int)*: Meta de EXP a alcanzar (p. ej. 57000).
- `exp_per_cycle` *(int)*: EXP que ganas por ciclo (p. ej. 60).
- `min_sec_per_cycle`, `max_sec_per_cycle` *(int)*: Rango de segundos por ciclo (p. ej. 35–45).
- `detail_checkpoints` *(Iterable[int] | None)*: Checkpoints manuales. Si es `None`, se generan **automáticos** por `checkpoint_step`.
- `filename` *(str)*: Ruta/archivo de salida del PDF.
- `include_question` *(bool)*: Incluye la frase de la “pregunta del usuario” al inicio.
- `checkpoint_step` *(int, default 10_000)*: Paso de EXP para checkpoints automáticos.
- `max_detail_rows` *(int, default 300)*: Límite superior de filas detalladas (se poda si excede).
- `question_suffix` *(str)*: Texto extra que se agrega a la “pregunta” mostrada.
- `tz_name` *(str)*: Zona horaria para el sello de fecha/hora del PDF (por defecto `America/Santiago`).
- `ensure_total_in_detail` *(bool | None)*: Si `True`, asegura que el último checkpoint sea `total_exp`. En modo manual, se agrega si falta; en modo auto, se añade si no cae exacto. Si `None`, se activa automáticamente cuando se usan checkpoints automáticos.

## 🧪 Ejemplos de ejecución
1. **Automático por pasos y PDF básico:**
   ```python
   generate_exp_report(57_000, 60, 35, 45, filename="test.pdf")
   ```

2. **Automático con paso personalizado y sufijo de pregunta:**
   ```python
   generate_exp_report(
       57_000, 60, 35, 45,
       checkpoint_step=10_000,
       question_suffix="Incluye tiempos aproximados y ciclos totales.",
       filename="test.pdf"
   )
   ```

3. **Manual con checkpoints específicos:**
   ```python
   generate_exp_report(
       57_000, 60, 35, 45,
       detail_checkpoints=[1_000, 2_000, 3_125, 4_125, 5_125, 6_250, 7_250, 8_375, 9_375, 10_375],
       filename="test.pdf"
   )
   ```

4. **Control de poda en tablas muy largas:**
   ```python
   generate_exp_report(
       100_000, 50, 30, 40,
       checkpoint_step=500,
       max_detail_rows=200,
       filename="test.pdf"
   )
   ```

5. **Desactivar inclusión automática del total final (modo auto):**
   ```python
   generate_exp_report(
       57_000, 60, 35, 45,
       checkpoint_step=8_000,
       ensure_total_in_detail=False,
       filename="test.pdf"
   )
   ```

> Para depuración, si está disponible en el notebook, puedes usar `debug_exp_report(...)` para imprimir la construcción de checkpoints y tiempos sin generar PDF.

---

## 📚 Explicación de funciones (guion de 5 puntos)
### `format_hms`
1️⃣ **Propósito:** Convertir segundos totales a una cadena con formato HH:MM:SS.

2️⃣ **Uso básico:** Llama `format_hms(segundos)` y recibe un string como `"01:23:45"`.

3️⃣ **Notas técnicas:** Redondea los segundos al entero más cercano, luego divide en horas, minutos y segundos con enteros (// y %).

4️⃣ **Ejemplo extra:**
```python
format_hms(3661)  # '01:01:01'
```

5️⃣ **Relación con otras partes:** Se usa para mostrar tiempos mínimos/máximos en las tablas del PDF que genera `generate_exp_report`.
### `es_miles`
1️⃣ **Propósito:** Formatear enteros con separador de miles estilo español (puntos).

2️⃣ **Uso básico:** Usa `es_miles(57000)` y devuelve `'57.000'`.

3️⃣ **Notas técnicas:** Internamente usa la formateación con coma y luego reemplaza `,` por `.` para miles.

4️⃣ **Ejemplo extra:**
```python
es_miles(1234567)  # '1.234.567'
```

5️⃣ **Relación con otras partes:** Se usa para títulos y celdas, haciendo más legibles los números grandes en el PDF.
### `_ensure_dir_for`
1️⃣ **Propósito:** Garantizar que exista el directorio donde se guardará el PDF.

2️⃣ **Uso básico:** Se invoca con la ruta final, p.ej. `_ensure_dir_for('out/reportes/r1.pdf')`.

3️⃣ **Notas técnicas:** Usa `os.path.dirname` y `os.makedirs(..., exist_ok=True)`; no hace nada si ya existe.

4️⃣ **Ejemplo extra:**
```python
_ensure_dir_for('salida/pdfs/demo.pdf')
```

5️⃣ **Relación con otras partes:** Es llamada por `generate_exp_report` antes de crear el PDF.
### `_validate_inputs`
1️⃣ **Propósito:** Validar tipos y rangos de los parámetros y normalizar los checkpoints.

2️⃣ **Uso básico:** La llama `generate_exp_report` al inicio y retorna la lista de checkpoints ordenada y sin duplicados.

3️⃣ **Notas técnicas:** Exige enteros positivos para EXP/ciclos/tiempos; `min_sec_per_cycle <= max_sec_per_cycle`. Si `detail_checkpoints` es `None`, devuelve lista vacía.

4️⃣ **Ejemplo extra:**
```python
_validate_inputs(57000, 60, 35, 45, [1000, 3000, 2000])  # -> [1000, 2000, 3000]
```

5️⃣ **Relación con otras partes:** Alimenta el cálculo de la tabla detallada dentro de `generate_exp_report`.
### `_on_page`
1️⃣ **Propósito:** Dibujar encabezado y pie de página en cada hoja del PDF.

2️⃣ **Uso básico:** Se pasa como `onFirstPage` y `onLaterPages` a ReportLab.

3️⃣ **Notas técnicas:** Imprime el título a la izquierda; a la derecha, fecha/hora local (ZoneInfo) y número de página.

4️⃣ **Ejemplo extra:**
```python
# Usado internamente por generate_exp_report con SimpleDocTemplate.build(...)
```

5️⃣ **Relación con otras partes:** Permite estilo consistente en todas las páginas generadas por `generate_exp_report`.
### `generate_exp_report`
1️⃣ **Propósito:** Generar un PDF con resumen y tabla detallada de tiempos para alcanzar cierta EXP.

2️⃣ **Uso básico:** Llamar con parámetros mínimos: `generate_exp_report(total_exp, exp_per_cycle, min_sec, max_sec, filename='reporte.pdf')`.

3️⃣ **Notas técnicas:** Calcula ciclos necesarios (ceil), tiempo mínimo/máximo, arma checkpoints (automáticos por step o dados por el usuario), recorta filas si superan `max_detail_rows`. Usa ReportLab para tablas/estilos.

4️⃣ **Ejemplo extra:**
```python
generate_exp_report(
    57_000, 60, 35, 45,
    checkpoint_step=10_000,
    question_suffix="Incluye tiempos aproximados y ciclos totales.",
    filename="reporte_demo.pdf"
)
```

5️⃣ **Relación con otras partes:** Es la función principal: usa todas las utilidades anteriores y devuelve la ruta/nombre del PDF generado.
### `debug_exp_report`
1️⃣ **Propósito:** Mostrar por consola el detalle del preproceso (checkpoints, ciclos, tiempos) sin generar PDF.

2️⃣ **Uso básico:** Llama `debug_exp_report(...)` con los mismos parámetros que `generate_exp_report`.

3️⃣ **Notas técnicas:** Imprime el flujo de cálculo, realiza podas de checkpoints y muestra tiempos total mínimo/máximo formateados.

4️⃣ **Ejemplo extra:**
```python
debug_exp_report(
    10_001, 100, 35, 45,
    detail_checkpoints=[10_001],
    checkpoint_step=10_000
)
```

5️⃣ **Relación con otras partes:** Útil para verificar cómo `generate_exp_report` va a construir la tabla; comparte la misma lógica de validación y armado de checkpoints.


---

## 🧱 Dependencias
- **reportlab** — creación de documentos PDF (tablas, estilos, layout).
- **tzdata** — datos de zona horaria (útil en sistemas sin base de zonas).
- **zoneinfo** — zona horaria nativa de Python 3.9+.
- **datetime**, **math**, **os**, **typing** — utilidades estándar.

---

## 🗂️ Código completo (con separación de celdas)

> A continuación se incluye el contenido de todas las **celdas de código** del notebook `exp_report_tutorial_final_v2.ipynb`. Cada celda está separada por la marca literal:
>
> `# ---- NUEVA CELDA ----`

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas as canvas_mod
from reportlab.lib.units import mm
from zoneinfo import ZoneInfo  # Zona horaria precisa (Python 3.9+)
import os
import math
from datetime import datetime
from typing import Iterable, List, Optional
# ---- NUEVA CELDA ----
def format_hms(seconds: float) -> str:
    seconds = int(round(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"
# ---- NUEVA CELDA ----
def es_miles(n: int) -> str:
    s = f"{int(n):,}"
    return s.replace(",", ".")
# ---- NUEVA CELDA ----
def _ensure_dir_for(path: str) -> None:
    directory = os.path.dirname(os.path.abspath(path))
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
# ---- NUEVA CELDA ----
def _validate_inputs(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]]
) -> List[int]:
    for name, val in [
        ("total_exp", total_exp),
        ("exp_per_cycle", exp_per_cycle),
        ("min_sec_per_cycle", min_sec_per_cycle),
        ("max_sec_per_cycle", max_sec_per_cycle),
    ]:
        if not isinstance(val, int):
            raise TypeError(f"{name} debe ser int.")
        if val <= 0:
            raise ValueError(f"{name} debe ser > 0.")
    if min_sec_per_cycle > max_sec_per_cycle:
        raise ValueError("min_sec_per_cycle no puede ser mayor que max_sec_per_cycle.")
    if detail_checkpoints is None:
        return []
    cps = list(detail_checkpoints)
    if any((not isinstance(x, int) or x <= 0) for x in cps):
        raise ValueError("Todos los detail_checkpoints deben ser enteros positivos.")
    cps = sorted(set(cps))
    return cps
# ---- NUEVA CELDA ----
def _on_page(canvas: canvas_mod.Canvas, doc, title_text: str, tz_name: str):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    # Encabezado (título)
    canvas.drawString(15 * mm, 285 * mm, title_text)
    # Pie con fecha local y número de página
    now_str = datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%d %H:%M")
    page_str = f"Generado: {now_str}  |  Página {doc.page}"
    canvas.drawRightString(200 * mm, 10 * mm, page_str)
    canvas.restoreState()
# ---- NUEVA CELDA ----
def generate_exp_report(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None,
    filename: str = "exp_report.pdf",
    include_question: bool = True,
    *,
    checkpoint_step: int = 10_000,
    max_detail_rows: int = 300,
    question_suffix: str = "Muéstralo en una tabla y en PDF.",
    tz_name: str = "America/Santiago",
    ensure_total_in_detail: Optional[bool] = None,
) -> str:
    cps = _validate_inputs(
        total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints
    )
    if not isinstance(checkpoint_step, int) or checkpoint_step <= 0:
        raise ValueError("checkpoint_step debe ser un entero positivo.")
    if not isinstance(max_detail_rows, int) or max_detail_rows <= 0:
        raise ValueError("max_detail_rows debe ser un entero positivo.")

    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle

    auto_mode = (detail_checkpoints is None)
    if ensure_total_in_detail is None:
        ensure_total_in_detail = auto_mode

    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        steps = list(range(checkpoint_step, last + 1, checkpoint_step))
        if ensure_total_in_detail and (not steps or steps[-1] != total_exp):
            steps.append(total_exp)
        cps = steps
    else:
        if ensure_total_in_detail and cps and cps[-1] != total_exp:
            cps = cps + [total_exp]

    if len(cps) > max_detail_rows:
        keep = max_detail_rows - 1
        stride = max(1, (len(cps) - 1) // keep)
        reduced = cps[:-1:stride]
        if len(reduced) > keep:
            reduced = reduced[:keep]
        cps = reduced + [cps[-1]]

    _ensure_dir_for(filename)
    styles = getSampleStyleSheet()
    title_text = f"Cálculo de tiempo para alcanzar {es_miles(total_exp)} EXP"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    if include_question:
        question = (
            f"Pregunta del usuario: ¿Cuánto tiempo demora alcanzar {es_miles(total_exp)} puntos de EXP "
            f"si gano {exp_per_cycle} EXP cada {min_sec_per_cycle} a {max_sec_per_cycle} segundos?"
        )
        if question_suffix:
            question += f" {question_suffix}"
        elements.append(Paragraph(question, styles["Normal"]))
        elements.append(Spacer(1, 12))

    elements.append(Paragraph(title_text, styles["Title"]))
    elements.append(Spacer(1, 12))

    summary_data = [
        ["Total EXP requerida", es_miles(total_exp)],
        ["EXP por ciclo", f"{exp_per_cycle}"],
        ["Ciclos necesarios", f"{cycles_needed}"],
        [f"Tiempo mínimo ({min_sec_per_cycle}s por ciclo)", format_hms(min_total)],
        [f"Tiempo máximo ({max_sec_per_cycle}s por ciclo)", format_hms(max_total)],
    ]
    summary_table = Table(summary_data, colWidths=[280, 220])
    summary_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ])
    summary_table.setStyle(summary_style)
    elements.append(summary_table)
    elements.append(Spacer(1, 24))

    elements.append(Paragraph("Detalles por puntos de EXP acumulada", styles["Title"]))
    elements.append(Spacer(1, 12))
    detailed_data = [["EXP acumulada", "Ciclos necesarios", "Tiempo mínimo", "Tiempo máximo"]]
    for pts in cps:
        cyc_needed = math.ceil(pts / exp_per_cycle)
        min_t = cyc_needed * min_sec_per_cycle
        max_t = cyc_needed * max_sec_per_cycle
        detailed_data.append([es_miles(pts), f"{cyc_needed}", format_hms(min_t), format_hms(max_t)])

    detailed_table = Table(detailed_data, colWidths=[150, 150, 150, 150], repeatRows=1)
    detailed_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ])
    detailed_table.setStyle(detailed_style)
    elements.append(detailed_table)

    doc.build(
        elements,
        onFirstPage=lambda c, d: _on_page(c, d, title_text, tz_name),
        onLaterPages=lambda c, d: _on_page(c, d, title_text, tz_name),
    )
    return filename
# ---- NUEVA CELDA ----
def debug_exp_report(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints=None,
    *,
    checkpoint_step: int = 10_000,
    tz_name: str = "America/Santiago",
    max_detail_rows: int = 300,
    ensure_total_in_detail: Optional[bool] = None,
):
    print("=== Debug EXP Report ===")
    print("total_exp:", total_exp)
    print("exp_per_cycle:", exp_per_cycle)
    print("min_sec_per_cycle:", min_sec_per_cycle)
    print("max_sec_per_cycle:", max_sec_per_cycle)
    print("detail_checkpoints:", detail_checkpoints)
    print("checkpoint_step:", checkpoint_step)
    print("tz_name:", tz_name)
    print("max_detail_rows:", max_detail_rows)
    print("ensure_total_in_detail:", ensure_total_in_detail)

    auto_mode = (detail_checkpoints is None)
    print("Modo automático?:", auto_mode)

    if ensure_total_in_detail is None:
        ensure_total_in_detail = auto_mode

    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        cps = list(range(checkpoint_step, last + 1, checkpoint_step))
        if ensure_total_in_detail and (not cps or cps[-1] != total_exp):
            cps.append(total_exp)
    else:
        cps = sorted(set(detail_checkpoints))
        if ensure_total_in_detail and cps[-1] != total_exp:
            cps.append(total_exp)

    if len(cps) > max_detail_rows:
        keep = max_detail_rows - 1
        stride = max(1, (len(cps) - 1) // keep)
        reduced = cps[:-1:stride]
        if len(reduced) > keep:
            reduced = reduced[:keep]
        cps = reduced + [cps[-1]]

    print("Checkpoints finales:", cps)
    print("Cantidad de filas detalladas:", len(cps))

    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle
    print("Ciclos necesarios (ceil):", cycles_needed)
    print("Tiempo total mínimo:", format_hms(min_total))
    print("Tiempo total máximo:", format_hms(max_total))
    print("==========================")
# ---- NUEVA CELDA ----
debug_exp_report(57000,60,35,45,[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375])
generate_exp_report(57000,60,35,45,[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375],question_suffix="")
# ---- NUEVA CELDA ----
pdf_path = generate_exp_report(
    total_exp=57000,
    exp_per_cycle=60,
    min_sec_per_cycle=35,
    max_sec_per_cycle=45,
    detail_checkpoints=[1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375],
    filename="cálculo_exp.pdf",
    include_question=True,
)
print("PDF generado en:", pdf_path)
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    detail_checkpoints=[1000, 2000, 3125],
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    checkpoint_step=10_000,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    checkpoint_step=5_000,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    detail_checkpoints=[1000, 2000, 3000],
    ensure_total_in_detail=True,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    include_question=False,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    tz_name="America/Santiago",
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    tz_name="America/New_York",
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(1_000_000, 60, 35, 45,
    checkpoint_step=1_000,
    max_detail_rows=120,
    filename="test.pdf")
# ---- NUEVA CELDA ----
debug_exp_report(57000, 60, 35, 45,
    detail_checkpoints=None, checkpoint_step=10_000)
# ---- NUEVA CELDA ----
debug_exp_report(57000, 60, 35, 45,
    detail_checkpoints=[1000, 2500, 5000])
# ---- NUEVA CELDA ----
debug_exp_report(
    total_exp=57000,
    exp_per_cycle=60,
    min_sec_per_cycle=35,
    max_sec_per_cycle=45,
    detail_checkpoints=[1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375],
)
# ---- NUEVA CELDA ----
generate_exp_report(7_000, 60, 35, 45,
    checkpoint_step=10_000,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57_000, 60, 35, 45,
    checkpoint_step=8_000,
    filename="test.pdf")
# ---- NUEVA CELDA ----
try:
    generate_exp_report(57000, 60, 50, 40, filename="test.pdf")
except Exception as e:
    print("OK (se esperaba error):", e)
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    filename="out/pdfs/test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    detail_checkpoints=[3000, 1000, 3000, 2000, 1500],
    filename="test.pdf")
# ---- NUEVA CELDA ----
debug_exp_report(10_001, 100, 35, 45,
    detail_checkpoints=[10_001])
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    question_suffix="Incluye tiempos aproximados y ciclos totales.",
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(100_000, 50, 30, 40,
    checkpoint_step=500,
    max_detail_rows=200,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57_000, 60, 35, 45,
    checkpoint_step=10_000,
    ensure_total_in_detail=False,
    filename="test.pdf")

```

---

*Archivo generado automáticamente el 2025-10-05 17:47:44.*

</details>

<details>
<summary>Nombre Archivo: readme_print_console_exp_report.md</summary>

# readme_print_console_exp_report.md

## 📌 Propósito del proyecto
Este mini-módulo imprime en **consola** un reporte de experiencia (EXP) estimando cuántos ciclos necesitas y cuánto tiempo total tomaría completarlos, considerando un rango de segundos por ciclo. También puede mostrar **checkpoints** intermedios para ver tiempos parciales.

## ✅ Requisitos
- **Python** 3.8+
- Sistema operativo con terminal/consola (Windows, macOS o Linux).

## 🧩 Dependencias
No requiere paquetes externos. Solo usa la librería estándar de Python (`math`, `typing`).

## 🔧 Instalación
1. Copia el archivo `print_console_exp_report.py` en tu proyecto (o mantenlo junto a tu script principal).
2. (Opcional) Colócalo en la raíz del proyecto para poder importarlo con facilidad.

## ▶️ Uso básico
### 1) Importando y llamando a la función principal
```python
from print_console_exp_report import print_console_exp_report

print_console_exp_report(
    57000, 60, 35, 45,
    [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375]
)
```

### 2) Ejecución directa desde una sola línea (sin crear archivos adicionales)
```bash
python -c python -c "from print_console_exp_report import debug_exp_report; debug_exp_report(57000,60,35,45)"
```

## 🧪 Ejemplos de ejecución
#### A) Con checkpoints manuales
```python
from print_console_exp_report import print_console_exp_report

print_console_exp_report(
    57000, 60, 35, 45,
    [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375]
)
```
#### B) En una sola línea (sin archivos extra)
```bash
python -c python -c "from print_console_exp_report import debug_exp_report; debug_exp_report(57000,60,35,45)"
```

---

## 🔍 Explicación de cada función (guion de 5 puntos)

### 1. `format_hms(seconds: int) -> str`
**1️⃣ Propósito**  
Convierte segundos enteros en formato `HH:MM:SS` con cero padding.

**2️⃣ Uso básico**  
```python
format_hms(3661)  # '01:01:01'
```

**3️⃣ Notas técnicas**  
- Redondea al entero más cercano y convierte a `int`.
- Calcula horas, minutos y segundos con divisiones y módulos.
- Devuelve una cadena con formato fijo `02d` por componente.

**4️⃣ Ejemplo extra**  
```python
format_hms(9)     # '00:00:09'
format_hms(5400)  # '01:30:00'
```

**5️⃣ Relación con otras partes**  
Se usa para imprimir tiempos mínimos/máximos, tanto en el encabezado del reporte como en la tabla de detalle.

---

### 2. `es_miles(n: int) -> str`
**1️⃣ Propósito**  
Formatea números enteros con separador de miles **punto** (ej.: `57.000`).

**2️⃣ Uso básico**  
```python
es_miles(57000)  # '57.000'
```

**3️⃣ Notas técnicas**  
- Usa formato con comas y luego reemplaza `,` por `.` para locales hispanos.
- Enfocado a enteros (casting explícito).

**4️⃣ Ejemplo extra**  
```python
es_miles(1234567)  # '1.234.567'
```

**5️⃣ Relación con otras partes**  
Se emplea en el encabezado y tabla para legibilidad de `total_exp`, `ciclos`, y checkpoints.

---

### 3. `_compute_plan(...) -> Dict[str, Any]`
**1️⃣ Propósito**  
Calcular el plan completo del reporte de EXP: ciclos exactos/requeridos y tiempos totales mínimo/máximo, además de la lista de checkpoints.

**2️⃣ Uso básico**  
```python
_compute_plan(57000, 60, 35, 45, [1000, 2000, 3125])
```

**3️⃣ Notas técnicas**  
- Valida tipos y que los parámetros numéricos sean `> 0`; también que `min_sec_per_cycle <= max_sec_per_cycle`.
- `cycles_exact = total_exp / exp_per_cycle`; `cycles_needed = ceil(cycles_exact)`.
- `min_total_sec = cycles_needed * min_sec_per_cycle`; `max_total_sec = cycles_needed * max_sec_per_cycle`.
- Si `detail_checkpoints` es `None` (modo automático), genera checkpoints en múltiplos de `checkpoint_step` (por defecto `5_000`) hasta `total_exp`.
- Si se excede `max_detail_rows`, reduce la lista manteniendo una muestra uniforme.
- Devuelve un diccionario con campos clave (ciclos, tiempos, checkpoints, bandera `auto_mode` y `filtered_notice`).

**4️⃣ Ejemplo extra**  
```python
data = _compute_plan(57000, 60, 35, 45, [1000, 2000, 3125])
data["cycles_needed"]       # 950
data["min_total_sec"]       # 33250 (=> 09:14:10)
data["max_total_sec"]       # 42750 (=> 11:52:30)
```

**5️⃣ Relación con otras partes**  
Es el núcleo de cálculo; lo consume `debug_exp_report` para imprimir encabezado y tabla de detalles.

---

### 4. `_print_debug_header(d: Dict[str, Any]) -> None`
**1️⃣ Propósito**  
Imprimir el **resumen** del reporte (valores globales, tiempos totales).

**2️⃣ Uso básico**  
```python
d = _compute_plan(57000, 60, 35, 45, None)
_print_debug_header(d)
```

**3️⃣ Notas técnicas**  
- Muestra `total_exp`, `exp_per_cycle`, `cycles_needed` y tiempos totales `min/max` formateados.
- Si hay `filtered_notice`, también lo imprime.
- Depende de `es_miles` y `format_hms` para presentar.

**4️⃣ Ejemplo extra**  
```python
d = _compute_plan(10000, 100, 40, 50, None)
_print_debug_header(d)
```

**5️⃣ Relación con otras partes**  
Es llamado por `debug_exp_report` antes de la tabla de detalles.

---

### 5. `_print_detail_table(checkpoints: List[int], exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int) -> None`
**1️⃣ Propósito**  
Imprimir una **tabla** de progreso con ciclos y tiempos al alcanzar cada checkpoint.

**2️⃣ Uso básico**  
```python
_print_detail_table([5000, 10000], 60, 35, 45)
```

**3️⃣ Notas técnicas**  
- Para cada checkpoint, calcula `ceil(cp / exp_per_cycle)` y sus tiempos min/máx.
- Alinea columnas con anchos fijos para una salida legible.
- Usa `es_miles` y `format_hms` en cada fila.

**4️⃣ Ejemplo extra**  
```python
_print_detail_table([1000, 2000, 3000], 120, 20, 30)
```

**5️⃣ Relación con otras partes**  
La invoca `debug_exp_report` tras imprimir el encabezado.

---

### 6. `debug_exp_report(..., return_data=False, verbose=True)`
**1️⃣ Propósito**  
Generar el reporte **completo** (encabezado + tabla) en consola y, opcionalmente, devolver los datos calculados.

**2️⃣ Uso básico**  
```python
debug_exp_report(57000, 60, 35, 45, [1000, 2000])
```

**3️⃣ Notas técnicas**  
- Internamente llama a `_compute_plan`.
- Si `verbose` es `True`, imprime encabezado y detalle.
- Si `return_data` es `True`, devuelve el diccionario calculado en lugar de `None`.

**4️⃣ Ejemplo extra**  
```python
d = debug_exp_report(8000, 80, 30, 40, None, return_data=True, verbose=False)
d["auto_mode"]  # True
```

**5️⃣ Relación con otras partes**  
Función de **alto nivel** para depuración; `print_console_exp_report` es un wrapper simplificado sobre ella.

---

### 7. `print_console_exp_report(..., detail_checkpoints: Optional[Iterable[int]] = None) -> None`
**1️⃣ Propósito**  
Atajo para imprimir el reporte en consola con la configuración dada (modo simple).

**2️⃣ Uso básico**  
```python
print_console_exp_report(57000, 60, 35, 45, [1000, 2000, 3125])
```

**3️⃣ Notas técnicas**  
- Simplemente llama a `debug_exp_report(..., return_data=False, verbose=True)`.
- No devuelve datos; su efecto es colateral (impresión en consola).

**4️⃣ Ejemplo extra**  
```python
print_console_exp_report(15000, 90, 40, 55)  # sin checkpoints: modo automático
```

**5️⃣ Relación con otras partes**  
Es la interfaz **más directa** para uso cotidiano en scripts o pruebas rápidas.

---

## 🗂️ Código completo
```python
from typing import Iterable, Optional, List, Dict, Any
import math

def format_hms(seconds: int) -> str:
    seconds = int(round(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def es_miles(n: int) -> str:
    s = f"{int(n):,}"
    return s.replace(",", ".")

def _compute_plan(total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
                  detail_checkpoints: Optional[Iterable[int]], *, checkpoint_step: int = 5_000, max_detail_rows: int = 300) -> Dict[str, Any]:
    for name, val in [("total_exp", total_exp), ("exp_per_cycle", exp_per_cycle),
                      ("min_sec_per_cycle", min_sec_per_cycle), ("max_sec_per_cycle", max_sec_per_cycle)]:
        if not isinstance(val, int): raise TypeError(f"{name} debe ser int.")
        if val <= 0: raise ValueError(f"{name} debe ser > 0.")
    if min_sec_per_cycle > max_sec_per_cycle:
        raise ValueError("min_sec_per_cycle no puede ser mayor que max_sec_per_cycle.")
    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle
    filtered_notice = None
    auto_mode = (detail_checkpoints is None)
    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        cps = list(range(checkpoint_step, last + 1, checkpoint_step))
    else:
        cps = sorted({int(x) for x in detail_checkpoints if int(x) > 0})
        over = [x for x in cps if x > total_exp]
        if over: filtered_notice = f"Aviso: se ignoraron checkpoints > total ({over})"
        cps = [x for x in cps if x <= total_exp]
    if len(cps) > max_detail_rows:
        keep = max_detail_rows
        step = max(1, len(cps) // keep)
        cps = cps[::step][:keep]
    return {
        "total_exp": total_exp, "exp_per_cycle": exp_per_cycle, "min_sec_per_cycle": min_sec_per_cycle, "max_sec_per_cycle": max_sec_per_cycle,
        "cycles_exact": cycles_exact, "cycles_needed": cycles_needed, "min_total_sec": min_total, "max_total_sec": max_total,
        "checkpoints": cps, "filtered_notice": filtered_notice, "auto_mode": auto_mode
    }

def _print_debug_header(d: Dict[str, Any]):
    print("=== Debug EXP Report ===")
    print(f"total_exp: {es_miles(d['total_exp'])}")
    print(f"exp_per_cycle: {d['exp_per_cycle']}")
    print(f"Ciclos necesarios (ceil): {d['cycles_needed']}\n")
    print(f"min_sec_per_cycle: {d['min_sec_per_cycle']}")
    print(f"Tiempo total mínimo: {format_hms(d['min_total_sec'])}\n")
    print(f"max_sec_per_cycle: {d['max_sec_per_cycle']}")
    print(f"Tiempo total máximo: {format_hms(d['max_total_sec'])}\n")
    if d.get("filtered_notice"): print(d["filtered_notice"])

def _print_detail_table(checkpoints: List[int], exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int):
    headers = ("Checkpoint", "Ciclos hasta aquí", "Tiempo mínimo", "Tiempo máximo")
    col_w = (14, 20, 16, 16)
    def fmt_row(c1, c2, c3, c4):
        return (f"{str(c1):>{col_w[0]}} {str(c2):>{col_w[1]}} {str(c3):>{col_w[2]}} {str(c4):>{col_w[3]}}")
    print(fmt_row(*headers))
    print("-" * sum(col_w) + "-" * 3)
    for cp in checkpoints:
        cycles_here = math.ceil(cp / exp_per_cycle)
        min_here = cycles_here * min_sec_per_cycle
        max_here = cycles_here * max_sec_per_cycle
        print(fmt_row(es_miles(cp), es_miles(cycles_here), format_hms(min_here), format_hms(max_here)))

def debug_exp_report(total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
                     detail_checkpoints: Optional[Iterable[int]] = None, *, checkpoint_step: int = 5_000,
                     max_detail_rows: int = 300, return_data: bool = False, verbose: bool = True):
    d = _compute_plan(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle,
                      detail_checkpoints, checkpoint_step=checkpoint_step, max_detail_rows=max_detail_rows)
    if verbose:
        _print_debug_header(d)
        _print_detail_table(d["checkpoints"], d["exp_per_cycle"], d["min_sec_per_cycle"], d["max_sec_per_cycle"])
    return d if return_data else None

def print_console_exp_report(total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
                             detail_checkpoints: Optional[Iterable[int]] = None):
    debug_exp_report(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle,
                     detail_checkpoints, return_data=False, verbose=True)
```

---

## ℹ️ Notas finales
- Si solo pasas `None` en `detail_checkpoints`, el módulo entra en **modo automático** y genera checkpoints cada `5.000` EXP (configurable vía `checkpoint_step` dentro de `debug_exp_report`).  
- Si la lista de checkpoints es muy grande, se reducirá para mantener la salida legible (`max_detail_rows`, por defecto `300`).

</details>

---

## Resumen de funciones, variables y recomendaciones

### 🧩 readme_Análisis_de_tiempos_de_EXP_por_checkpoints.md
**Funciones detectadas**
- `analyze_checkpoints()`
- `calculate_time_ranges()`
- `export_table_to_md()`

**Variables relevantes**
- `min_time`, `max_time`, `checkpoints`, `exp_total`.

**Recomendaciones**
- Ideal para estimar progresión de experiencia por hitos.
- Se recomienda usarlo antes de generar reportes para verificar consistencia de datos.

---

### 🧾 readme_exp_report.md
**Funciones detectadas**
- `generate_exp_report()`
- `_compute_plan()`
- `_validate_inputs()`
- `_on_page()`
- `_ensure_dir_for()`

**Variables relevantes**
- `total_exp`, `exp_per_cycle`, `checkpoint_step`, `filename`, `tz_name`.

**Recomendaciones**
- Usar para crear reportes PDF con tabla y resumen.
- Ideal para documentación o entrega de resultados.
- Verificar permisos de escritura antes de generar el archivo.

---

### 📘 readme_exp_report_tutorial_final_v2.md
**Funciones detectadas**
- `generate_exp_report()`
- `print_console_exp_report()`
- `_register_fonts()`

**Variables relevantes**
- `detail_checkpoints`, `include_total_in_table`, `ensure_total_in_detail`.

**Recomendaciones**
- Útil como guía práctica paso a paso para nuevos usuarios.
- Puede emplearse como plantilla de aprendizaje para adaptar reportes personalizados.

---

### 💻 readme_print_console_exp_report.md
**Funciones detectadas**
- `print_console_exp_report()`
- `_print_debug_header()`
- `_print_detail_table()`

**Variables relevantes**
- `return_data`, `verbose`, `detail_checkpoints`.

**Recomendaciones**
- Ideal para depuración rápida sin generar PDFs.
- Perfecto para validar cálculos antes de ejecutar el reporte principal.
