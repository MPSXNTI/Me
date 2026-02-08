
---

<details><summary>Doc</summary>

<details><summary>README_Entorno_Python_VSCode.md</summary>

# 🐍 README — Entorno de Python en VS Code (Windows CMD)

¡Bienvenido! 👋  
Esta guía te acompaña paso a paso para crear, configurar y usar un **entorno virtual de Python (`.venv`)** en **VS Code usando Windows CMD**.  
Además, incluye scripts listos para automatizar tareas comunes y consejos para mantener tu entorno limpio y rápido.  

---

## ⚡ 1. Resumen rápido (Quickstart)

Si ya sabes lo básico, estos son los comandos esenciales 👇

```cmd
# 1️⃣ Ubícate en tu carpeta de proyecto
cd C:\ruta\de\tu\proyecto

# 2️⃣ Crea el entorno virtual
python -m venv .venv

# 3️⃣ Activa el entorno
.venv\Scripts\activate.bat

# 4️⃣ Desactivar el entorno
deactivate or .venv\Scripts\deactivate.bat

# 5️⃣ Instala dependencias (si tienes requirements.txt)
pip install -r requirements.txt

# 6️⃣ Abre VS Code con ese entorno activo
code .
```

---

## 🧱 2. Crear y configurar el entorno paso a paso

### 🔹 Abrir CMD y posicionarte en tu proyecto
```cmd
cd C:\Users\TuUsuario\Desktop\python
```

### 🔹 Verificar instalación de Python
```cmd
python --version
where python
```
Deberías ver rutas hacia tu instalación de Python.

### 🔹 Crear el entorno virtual
```cmd
python -m venv .venv
```

### 🔹 Activar el entorno
```cmd
.venv\Scripts\activate.bat
```
Si todo va bien, el prompt mostrará algo así:
```
(.venv) C:\Users\TuUsuario\Desktop\python>
```

### 🔹 Desactivar el entorno
```cmd
.venv\Scripts\deactivate.bat
```
```cmd
deactivate
```

### 🔹 Instalar dependencias
```cmd
pip install requests
```

---

## 🧩 3. Configurar correctamente VS Code

### Seleccionar el intérprete de Python
1. Presiona `Ctrl + Shift + P`
2. Escribe **Python: Select Interpreter**
3. Selecciona `.venv\Scripts\python.exe`  
   (si no aparece, usa *Enter Interpreter Path → Find...*)

### Cambiar la terminal por defecto a CMD
1. `Ctrl + Shift + P` → **Terminal: Select Default Profile**
2. Elige **Command Prompt (cmd)**
3. Cierra y reabre la terminal con `Ctrl + ñ`

### Verificar que VS Code usa el entorno correcto
```cmd
python --version
where python
```
Debería apuntar a:  
`.venv\Scripts\python.exe` ✅

---

## 🧯 4. Solución rápida de errores comunes

| Problema | Causa probable | Solución |
|-----------|----------------|-----------|
| `'python' no se reconoce` | Python no está en PATH | Reinstala y marca **Add Python to PATH** |
| PowerShell muestra errores | Estás usando la terminal equivocada | Cambia a **CMD** |
| `.venv` no existe | No se creó aún | Ejecuta `python -m venv .venv` |
| Dependencias no instaladas | Falta `requirements.txt` | Crea uno con `pip freeze > requirements.txt` |
| El analizador de VS Code da errores raros | Lenguaje desactualizado | `Python: Restart Language Server` o `Developer: Reload Window` |

---

## ⚙️ 5. Scripts CMD para automatizar tu entorno

Una vez que domines los pasos manuales, puedes usar estos **scripts .cmd** para hacerlo más rápido ⚡

| Script | Acción principal | Cuándo usarlo |
|--------|------------------|----------------|
| `setup_venv_from_requirements.cmd` | Crea y configura `.venv` desde `requirements.txt`. | Primera vez o al actualizar dependencias. |
| `reset_venv_from_requirements.cmd` | Elimina y recrea el entorno desde cero. | Si el entorno está roto o quieres empezar limpio. |
| `provision_and_open_venv.cmd` | Crea, instala y abre una terminal con `.venv` activo. | Para iniciar rápido y trabajar al instante. |
| `open_venv_here.cmd` | Abre una CMD con el entorno ya activado. | Si ya existe `.venv` y solo quieres usarlo. |

📁 **Ubícalos en la raíz del proyecto:**
```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```

---

## 💡 6. Tips y buenas prácticas

- Un entorno por proyecto 💼  
- Mantén tu `requirements.txt` actualizado y versionado.  
- Usa `reset_venv_from_requirements.cmd` para limpiar conflictos de versiones.  
- Divide dependencias: `requirements.txt` (producción) y `requirements-dev.txt` (desarrollo).  
- Si trabajas en varios proyectos, puedes tener `.venv_api`, `.venv_test`, etc.

---

## 🧠 7. Conceptos clave rápidos

| Concepto | Descripción |
|-----------|-------------|
| **Entorno virtual (`.venv`)** | Espacio aislado con sus propias dependencias. |
| **Activar entorno** | `.venv\Scripts\activate.bat` |
| **Desactivar entorno** | `deactivate` o `.venv\Scripts\deactivate.bat` |
| **Instalar dependencias** | `pip install -r requirements.txt` |

---

## 🚀 8. Consejo final

Crea tus entornos siempre dentro del proyecto, mantenlos versionados con `requirements.txt`, y usa los scripts cuando quieras ahorrar tiempo.  
Así tendrás entornos **limpios, reproducibles y sin dolores de cabeza** 😄

---

🔗 **Documentación completa de los scripts CMD:**  
Consulta [README_Scripts_CMD.md](./README_Scripts_CMD.md)

---

© 2025 – Guía práctica unificada basada en documentación técnica y experiencia en VS Code + Python.

</details>

<details><summary>README_Scripts_CMD.md</summary>

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
 ├─ Scripts CMD/
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
Scripts CMD\setup_venv_from_requirements.cmd

# Reiniciar el entorno desde cero
Scripts CMD\reset_venv_from_requirements.cmd

# Crear y abrir entorno activo automáticamente
Scripts CMD\provision_and_open_venv.cmd

# Abrir entorno ya existente
Scripts CMD\open_venv_here.cmd
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

🔙 **Volver a la guía principal:** [README_Entorno_Python_VSCode.md](./README_Entorno_Python_VSCode.md)

---

© 2025 – Guía técnica complementaria.  
Creada para acompañar al archivo **README_Entorno_Python_VSCode.md** y facilitar la automatización de entornos virtuales.

</details>

<details><summary>requirements_example.txt</summary>

```txt
flask==3.0.3
pandas==2.2.3
reportlab==4.4.4
pillow==11.3.0
tzdata==2025.2
```
</details>

</details>

---
---

<details><summary>Scripts CMD</summary>

<details><summary>open_venv_here.cmd</summary>

```cmd
@echo off
cd /d "%~dp0"
if exist .venv (
  call .venv\Scripts\activate.bat
  cmd /K
) else (
  echo [!] No existe el entorno .venv en este directorio.
  pause
)
```
</details>

<details><summary>provision_and_open_venv.cmd</summary>

```cmd
@echo off
cd /d "%~dp0"
if not exist ".venv" (
  echo [*] Creando entorno virtual...
  python -m venv .venv
)

echo [*] Activando entorno...
call .venv\Scripts\activate.bat

echo [*] Actualizando pip...
python -m pip install --upgrade pip

if exist requirements.txt (
  echo [*] Instalando dependencias desde requirements.txt...
  pip install -r requirements.txt
) else (
  echo [!] No se encontro requirements.txt en este directorio
)

echo [*] Entorno listo y activo en .venv
cmd /K
```
</details>

<details><summary>reset_venv_from_requirements.cmd</summary>

```cmd
@echo off
cd /d "%~dp0"
set VENV_DIR=.venv

echo =================================================
echo  Script para BORRAR y RECREAR el entorno virtual
echo =================================================
echo.

set /p CONFIRM="¿Quieres borrar y recrear el entorno %VENV_DIR%? (S/N): "

if /I "%CONFIRM%"=="S" (
    echo [*] Eliminando entorno existente...
    rmdir /s /q "%VENV_DIR%"

    echo [*] Creando entorno nuevo en %VENV_DIR%...
    python -m venv %VENV_DIR%

    echo [*] Activando entorno...
    call %VENV_DIR%\Scripts\activate.bat

    echo [*] Actualizando pip...
    python -m pip install --upgrade pip

    if exist requirements.txt (
        echo [*] Instalando dependencias desde requirements.txt...
        pip install -r requirements.txt
    ) else (
        echo [!] No se encontro requirements.txt en este directorio
    )

    echo.
    echo [*] Entorno recreado y activado correctamente.
    python --version
    where python
    pip list

    cmd /K
) else (
    echo [!] Cancelado por el usuario.
    pause
)
```
</details>

<details><summary>setup_venv_from_requirements.cmd</summary>

```cmd
@echo off
setlocal enableextensions enabledelayedexpansion
REM Ruta del entorno (por defecto .venv)
set VENV_DIR=.venv

if not exist "%VENV_DIR%" (
  echo [*] Creando entorno virtual en %VENV_DIR%
  python -m venv %VENV_DIR%
)

echo [*] Activando entorno
call %VENV_DIR%\Scripts\activate.bat

echo [*] Actualizando pip
python -m pip install --upgrade pip

if exist requirements.txt (
  echo [*] Instalando dependencias desde requirements.txt
  pip install -r requirements.txt
) else (
  echo [!] No se encontro requirements.txt en el directorio actual
)

echo [*] Listo. Entorno activo en %VENV_DIR%
python --version
where python
pip list
endlocal
```
</details>

</details>

---
---

<details><summary>README.md</summary>

# 🐍 Kit de Entornos Python (Windows / CMD)

Este proyecto proporciona una colección de **scripts y guías** para configurar, gestionar y automatizar entornos virtuales de Python en **Windows usando la línea de comandos (CMD)** y **VSCode**.  
Ideal para desarrolladores que desean mantener entornos limpios, reproducibles y rápidos de activar.

---

## 📂 Contenido

| Archivo / Carpeta | Descripción |
|--------------------|-------------|
| `Doc/README_Entorno_Python_VSCode.md` | Guía detallada sobre cómo integrar entornos virtuales con **Visual Studio Code**. |
| `Doc/README_Scripts_CMD.md` | Explicación técnica de los scripts CMD disponibles, sus parámetros y ejemplos de uso. |
| `Doc/requirements_example.txt` | Ejemplo de archivo `requirements.txt` para instalar dependencias rápidamente en un entorno virtual. |
| `Scripts CMD/open_venv_here.cmd` | Abre el entorno virtual (`.venv`) en la carpeta actual, útil para pruebas o trabajo directo. |
| `Scripts CMD/provision_and_open_venv.cmd` | Crea (si no existe), activa el entorno virtual y lo abre automáticamente. |
| `Scripts CMD/reset_venv_from_requirements.cmd` | Elimina el entorno actual y lo reconstruye desde el archivo `requirements.txt`. |
| `Scripts CMD/setup_venv_from_requirements.cmd` | Crea un entorno virtual nuevo e instala las dependencias desde `requirements.txt`. |

---

## 🗺️ Mapa del Proyecto

```
Kit de Entornos Python (Windows - CMD)
├── Doc/
│   ├── README_Entorno_Python_VSCode.md
│   ├── README_Scripts_CMD.md
│   └── requirements.txt
└── Scripts CMD/
    ├── open_venv_here.cmd
    ├── provision_and_open_venv.cmd
    ├── reset_venv_from_requirements.cmd
    └── setup_venv_from_requirements.cmd
```

---

## 🧭 Uso rápido paso a paso

1. **Clona o descarga** este repositorio.  
   ```bash
   git clone https://github.com/usuario/Kit-Entornos-Python-CMD.git
   cd "Kit de Entornos Python (Windows - CMD)"
   ```

2. **Verifica tu instalación de Python.**  
   ```bash
   python --version
   ```

3. **Crea o configura el entorno virtual automáticamente.**  
   Ejecuta en CMD dentro de la carpeta del proyecto:
   ```bash
   Scripts CMD\setup_venv_from_requirements.cmd
   ```
   Este script creará un entorno `.venv` e instalará las dependencias de `requirements.txt`.

4. **Activa el entorno virtual manualmente (si prefieres hacerlo tú).**
   ```bash
   .venv\Scripts\activate
   ```

5. **Instala dependencias adicionales si las necesitas.**
   ```bash
   pip install paquete_ejemplo
   pip freeze > requirements.txt
   ```

6. **Abre el entorno directamente en VSCode.**
   - Ejecuta `Scripts CMD\open_venv_here.cmd`  
   - O abre VSCode y selecciona el intérprete del entorno virtual (`.venv`).

7. **Reinicia el entorno (opcional).**
   Si quieres limpiar y reconstruir el entorno desde cero:
   ```bash
   Scripts CMD\reset_venv_from_requirements.cmd
   ```

---

## ✅ Recomendación

1. Instala **Python 3.10+** y verifica que el comando `python` esté disponible en CMD.  
2. Abre el proyecto en **VSCode** y asegúrate de que el intérprete apunte al entorno virtual deseado.  
3. Usa los scripts CMD para crear y manejar entornos fácilmente.  
4. Mantén actualizado tu `requirements.txt` para replicar entornos sin conflictos.  

---

## 🧪 Comandos básicos de verificación

```bash
# Verificar versión de Python
python --version

# Crear entorno virtual (manual)
python -m venv .venv

# Activar entorno en CMD
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Listar paquetes instalados
pip list
```

</details>

---

