# 🧮 **Debug EXP Report — Planificación y Cálculo de Tiempos**

> Este documento explica el funcionamiento del script `debug_exp_report.py`, siguiendo el mismo formato explicativo y técnico de `example.md`.

---

## 📘 **Tabla de Contenidos**

- [1️⃣ Propósito](#1-propósito)  
- [2️⃣ Uso básico](#2-uso-básico)  
- [3️⃣ Estructura del código](#3-estructura-del-código)  
- [4️⃣ Ejemplo de ejecución](#4-ejemplo-de-ejecución)  
- [5️⃣ Explicación detallada de funciones](#5-explicación-detallada-de-funciones)  
- [6️⃣ Observaciones técnicas](#6-observaciones-técnicas)  
- [7️⃣ Salida esperada](#7-salida-esperada)  
- [8️⃣ Conclusión](#8-conclusión)

---

## 1️⃣ **Propósito**

El script `debug_exp_report.py` genera un **informe de depuración de experiencia (EXP)** mostrando:

- Cuántos **ciclos** son necesarios para alcanzar una meta total de experiencia.  
- El **tiempo mínimo y máximo** estimado para alcanzarla, según la duración de cada ciclo.  
- Un **detalle por checkpoint**, mostrando cuántos ciclos y tiempo acumulado requiere cada punto intermedio.

📈 Es ideal para analizar progresión de EXP en sistemas de niveles, juegos o simulaciones donde la ganancia por ciclo y los tiempos varían.

---

## 2️⃣ **Uso básico**

La función principal es:

```python
debug_exp_report(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None
)
```

Ejemplo básico:

```python
debug_exp_report(
    total_exp=57000,
    exp_per_cycle=60,
    min_sec_per_cycle=45,
    max_sec_per_cycle=60,
    detail_checkpoints=[1000, 2000, 3125, 6250, 10375]
)
```

📋 **Resultado:** imprime un informe con los totales, ciclos requeridos y una tabla detallada con tiempos mínimos y máximos por checkpoint.

---

## 3️⃣ **Estructura del código**

El script se organiza en cuatro bloques principales:

1. **Funciones auxiliares:**
   - `format_hms()` → Convierte segundos a formato `HH:MM:SS`.
   - `_format_thousands()` → Da formato con puntos a los miles (ej. `57.000`).
   - `_validate_inputs()` → Verifica los tipos y rangos válidos de los argumentos.

2. **Lógica de cálculo:**
   - `_compute_plan()` calcula los tiempos y ciclos según los parámetros dados.

3. **Función pública:**
   - `debug_exp_report()` ejecuta la validación, genera el plan y lo imprime.

4. **Casos de prueba al final del script:**
   ```python
   debug_exp_report(57000, 60, 45, 60, detail_checkpoints=[...])
   debug_exp_report(28875, 60, 45, 60, [15375, 13500])
   ```

---

## 4️⃣ **Ejemplo de ejecución**

```python
debug_exp_report(
    57000,        # total_exp
    60,           # exp_per_cycle
    45,           # min_sec_per_cycle
    60,           # max_sec_per_cycle
    [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375]
)
```

---

## 5️⃣ **Explicación detallada de funciones**

### 🧩 `format_hms(total_seconds: float) -> str`

Convierte un número de segundos a formato `HH:MM:SS` con ceros a la izquierda.  
Ejemplo: `3725 → "01:02:05"`

```python
def format_hms(total_seconds: float) -> str:
    s = int(round(total_seconds))
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"
```

---

### 🔢 `_format_thousands(n: int) -> str`

Da formato de miles con puntos:
```python
_format_thousands(57000)  # "57.000"
```

---

### 🧠 `_validate_inputs(...)`

Comprueba que todos los parámetros sean válidos:
- `int > 0` para EXP y tiempos.  
- `min_sec_per_cycle <= max_sec_per_cycle`.  
- Todos los checkpoints positivos.

Errores detectados lanzan `ValueError`.

---

### ⚙️ `_compute_plan(...)`

Realiza el cálculo del plan:

1. **Determina ciclos necesarios:**
   ```python
   cycles_needed = ceil(total_exp / exp_per_cycle)
   ```

2. **Calcula tiempos totales:**
   ```python
   total_min_seconds = cycles_needed * min_sec_per_cycle
   total_max_seconds = cycles_needed * max_sec_per_cycle
   ```

3. **Imprime resultados:**
   - EXP total
   - EXP por ciclo
   - Ciclos requeridos
   - Tiempos totales mínimo y máximo

4. **Tabla de checkpoints (si se especifican):**
   Para cada checkpoint:
   - Calcula ciclos = `ceil(checkpoint / exp_per_cycle)`
   - Tiempo mínimo = `ciclos * min_sec_per_cycle`
   - Tiempo máximo = `ciclos * max_sec_per_cycle`

   Cada fila incluye:
   - Checkpoint (EXP)
   - Ciclos hasta ese punto
   - Tiempo mínimo acumulado
   - Tiempo máximo acumulado

---

### 📊 `debug_exp_report(...)`

Es la función principal pública:

```python
def debug_exp_report(...):
    _validate_inputs(...)
    output = _compute_plan(...)
    print(output)
```

Su única salida es un **informe formateado en texto**.

---

## 6️⃣ **Observaciones técnicas**

- Usa `ceil()` para redondear hacia arriba los ciclos, garantizando que se cubra toda la EXP requerida.  
- Los tiempos se formatean siempre con dos dígitos por unidad (`HH:MM:SS`).  
- Los checkpoints duplicados se filtran internamente para evitar repeticiones.  
- No depende de librerías externas: solo `math` y `typing`.  
- Diseño modular para poder importarse y usarse como **módulo reutilizable**.

---

## 7️⃣ **Salida esperada**

Ejemplo resumido del primer bloque:

```
=== Debug EXP Report ===
total_exp: 57.000
exp_per_cycle: 60
Ciclos necesarios (ceil): 950

min_sec_per_cycle: 45
Tiempo total mínimo: 11:52:30

max_sec_per_cycle: 60
Tiempo total máximo: 15:48:20

  Checkpoint     Ciclos hasta aquí    Tiempo mínimo    Tiempo máximo
--------------------------------------------------------------------
        1.000                   17           00:12:45           00:17:00
        2.000                   34           00:25:30           00:34:00
        3.125                   53           00:39:45           00:53:00
        4.125                   69           00:51:45           01:09:00
        5.125                   86           01:04:30           01:26:00
        6.250                  105           01:18:45           01:45:00
        7.250                  121           01:30:45           02:01:00
        8.375                  140           01:45:00           02:20:00
        9.375                  157           01:57:45           02:37:00
       10.375                  173           02:09:45           02:53:00
```

---

## 8️⃣ **Conclusión**

El script `debug_exp_report.py` ofrece una herramienta práctica y precisa para:

- Calcular tiempos de progreso según tasas variables.  
- Obtener una tabla de referencia rápida para depuración o análisis de balanceo.  
- Integrarse fácilmente en sistemas de simulación, bots o herramientas de rendimiento.

---

✨ *Documentación adaptada por Proyecto Peluca — Estilo `example.md` (2025)* ✨
