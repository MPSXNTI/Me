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
