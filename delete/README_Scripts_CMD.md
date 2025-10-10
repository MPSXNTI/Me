# ⚙️ README — Scripts CMD para entornos virtuales de Python

Bienvenido 👋  
Este documento explica en detalle cómo funcionan y cómo usar los **scripts CMD** que automatizan la creación y manejo de entornos virtuales de Python (`.venv`) en **Windows**.  
Están diseñados para funcionar perfectamente con **VS Code + CMD**, evitando configuraciones manuales repetitivas.

---

## 🚀 1. ¿Qué son estos scripts?

Son archivos `.cmd` (o `.bat`) que ejecutan automáticamente comandos de Python y `pip` desde la terminal de **Command Prompt (CMD)**.  
Te permiten crear, reiniciar o abrir tu entorno virtual en segundos ⚡

---

## 📂 2. Estructura recomendada del proyecto

```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 ├─ scripts/
 │   ├─ setup_venv_from_requirements.cmd
 │   ├─ reset_venv_from_requirements.cmd
 │   ├─ provision_and_open_venv.cmd
 │   └─ open_venv_here.cmd
 ├─ README_Entorno_Python_VSCode.md
 └─ README_Scripts_CMD.md
```

> 💡 Consejo: guarda todos los scripts dentro de la carpeta `scripts/` o en la raíz, según prefieras.

---

## 🧩 3. Descripción de cada script

| Script | Acción principal | Cuándo usarlo |
|--------|------------------|----------------|
| `setup_venv_from_requirements.cmd` | Crea y configura el entorno desde `requirements.txt`. | Primera vez o al actualizar dependencias. |
| `reset_venv_from_requirements.cmd` | Borra y recrea el entorno desde cero. | Cuando el entorno está roto o quieres empezar limpio. |
| `provision_and_open_venv.cmd` | Crea el entorno (si no existe), instala dependencias y abre una terminal activa. | Cuando quieres empezar a trabajar rápido. |
| `open_venv_here.cmd` | Abre una CMD con el entorno ya activado. | Si el entorno ya existe y solo necesitas usarlo. |

---

## 🧱 4. Ejemplos de uso

Abre una terminal **CMD** dentro del proyecto y ejecuta:

```cmd
# Crear entorno e instalar dependencias
scripts\setup_venv_from_requirements.cmd

# Reiniciar el entorno desde cero
scripts\reset_venv_from_requirements.cmd

# Crear y abrir entorno activo automáticamente
scripts\provision_and_open_venv.cmd

# Abrir entorno ya existente
scripts\open_venv_here.cmd
```

> ⚠️ Asegúrate de ejecutar desde **CMD**, no PowerShell.  
> Si usas VS Code, cambia el perfil de terminal a **Command Prompt (cmd)**.

---

## 🧯 5. Solución de problemas comunes

| Problema | Causa probable | Solución |
|-----------|----------------|-----------|
| `python` no se reconoce | Python no está agregado al PATH. | Reinstala Python marcando **Add Python to PATH**. |
| Error “requirements.txt no encontrado” | El archivo no existe o está en otra ruta. | Crea uno con `pip freeze > requirements.txt` o muévelo a la raíz del proyecto. |
| No se crea `.venv` | El script no tiene permisos o hay error en Python. | Verifica que Python esté instalado correctamente y ejecuta el script como administrador. |
| PowerShell muestra errores de ejecución | Estás usando PowerShell. | Cambia a CMD desde *Terminal: Select Default Profile → Command Prompt*. |

---

## 🧠 6. Cómo personalizar los scripts

Puedes abrir cualquier `.cmd` con un editor de texto (como VS Code) y modificar rutas o comandos según tus necesidades.  
Por ejemplo, puedes cambiar el nombre del entorno:

```cmd
python -m venv .entorno_dev
```

O agregar instalación de paquetes personalizados:

```cmd
pip install -r requirements.txt
pip install black flake8 pytest
```

---

## 💡 7. Consejos avanzados

- Crea versiones separadas: `requirements.txt` (producción) y `requirements-dev.txt` (desarrollo).  
- Usa `reset_venv_from_requirements.cmd` para limpiar conflictos de dependencias.  
- Añade comentarios en tus scripts (`REM Este comando crea el entorno...`).  
- Puedes ejecutar un script con doble clic desde el Explorador de archivos.  

---

## 🧭 8. Recursos útiles

- 📘 Documentación oficial de Python: https://docs.python.org/3/library/venv.html  
- 📘 Documentación de VS Code (extensión de Python): https://code.visualstudio.com/docs/python/python-tutorial  
- 📘 Cómo usar CMD en Windows: https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/cmd

---

© 2025 – Guía técnica complementaria.  
Creada para acompañar al archivo **README_Entorno_Python_VSCode.md** y facilitar la automatización de entornos virtuales.
