# Mini‑proyecto guiado POO (Python + Java + C++)

Objetivo: practicar **Encapsulamiento → Herencia → Polimorfismo → Pruebas** en tres lenguajes.

## Hitos sugeridos (2–3h total)

### Hito 1 — Encapsulamiento
- Revisa `Vehiculo` en cada lenguaje.
- Asegura validación de `delta` (no negativo) y que la velocidad no sea < 0.
- Ejecuta pruebas: deberían fallar si rompes las invariantes.

### Hito 2 — Herencia
- Implementa `Auto` y `Bicicleta` con su propia cadena de salida en `mover()`.
- Asegura que las clases derivadas NO dupliquen lógica de `Vehiculo`.

### Hito 3 — Polimorfismo
- Crea una colección heterogénea de `Vehiculo` y llama `mover()` para cada uno.
- Comprueba que cada subclase responda distinto.

### Hito 4 — Pruebas unitarias
- Python: `unittest`
- Java: JUnit 5 (Maven)
- C++: test runner minimalista con macros

### Hito 5 — Extensión (opcional)
- Agrega `Patinete` con una regla extra: si velocidad < 5 → `empujar()` antes de `mover()`.
- Escribe tests para la nueva clase en los tres lenguajes.

## Rutas de cada proyecto
- `python/README.md`
- `java/README.md`
- `cpp/README.md`
