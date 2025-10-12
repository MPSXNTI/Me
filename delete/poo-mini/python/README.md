# Mini‑proyecto POO — Python

## Objetivo
Aplicar POO con **encapsulamiento, herencia y polimorfismo** y cubrirlo con **pruebas unitarias**.

## Estructura
```
python/
  vehiculos/
    __init__.py
    vehiculo.py
    auto.py
    bicicleta.py
  tests/
    test_vehiculos.py
  main.py
  README.md
```

## Pasos guiados
1) **Encapsulamiento**: completa campos privados y propiedades en `vehiculo.py`.
2) **Herencia**: implementa `Auto` y `Bicicleta` en sus archivos.
3) **Polimorfismo**: crea una colección heterogénea en `main.py` y llama `mover()`.
4) **Pruebas**: ejecuta los tests.
5) **Extensión** (opcional): agrega `Patinete` con su propia lógica.

## Comandos
```bash
# Ejecutar
python3 main.py

# Pruebas (unittest)
python3 -m unittest -v
# o solo carpeta
python3 -m unittest discover -s tests -p "test_*.py" -v
```
