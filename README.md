
---

<details><summary>Readme.md</summary>

# 🐍 Kit de Entornos Python (Windows / CMD)

Este proyecto proporciona una colección de **scripts y guía** para configurar, gestionar y automatizar entornos virtuales de Python en **Windows usando la línea de comandos (CMD)** y **VS Code**.  
Está orientado a mantener entornos **limpios, reproducibles y seguros**, evitando errores comunes en Windows.

---

## Resumen rápido (Quickstart)

```cmd
# 1️⃣ Crear el entorno virtual
python -m venv .venv

# 2️⃣ Activar el entorno
.venv\Scripts\activate.bat

# 3️⃣ Desactivar el entorno
deactivate

# 4️⃣ Instalar dependencias
pip install -r requirements.txt

# 5️⃣ Listar paquetes instalados
pip list
```

---

## 📂 Contenido

| Archivo / Carpeta | Descripción |
|------------------|-------------|
| `requirements.txt` | Lista de dependencias del proyecto. |
| `Scripts CMD/setup_venv_from_requirements.cmd` | Crea el entorno virtual e instala dependencias. |
| `Scripts CMD/reset_venv_from_requirements.cmd` | Borra y recrea el entorno desde cero. |

---

## 📂 1. Estructura recomendada del proyecto

```text
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 └─ Scripts CMD/
     ├─ setup_venv_from_requirements.cmd
     └─ reset_venv_from_requirements.cmd
```

---

## 🧱 2. Crear y configurar el entorno paso a paso

### Cambiar la terminal por defecto a CMD (VS Code)

1. `Ctrl + Shift + P` → **Terminal: Select Default Profile**
2. Selecciona **Command Prompt (cmd)**
3. Cierra y reabre la terminal (`Ctrl + ñ`)

---

### 🔹 Abrir CMD y posicionarte en tu proyecto

```cmd
cd C:\Users\TuUsuario\Desktop\mi_proyecto
```

---

### 🔹 Verificar instalación de Python

```cmd
python --version
where python
```

Deberías ver:

- Una versión válida de Python  
- Rutas **que NO apunten a**:

```text
WindowsApps\python.exe
```

⚠️ Si aparece esa ruta, usa explícitamente:

reinstala Python desde **https://www.python.org**.

📌 **Motivo técnico**: los scripts usan `python` desde el `PATH`.

---

### 🔹 Crear el entorno virtual

```cmd
python -m venv .venv
```

---

### 🔹 Activar el entorno

```cmd
.venv\Scripts\activate.bat
```

Si todo va bien, el prompt mostrará:

```text
(.venv) C:\Users\TuUsuario\Desktop\mi_proyecto>
```

---

### 🔹 Verificar que VS Code usa el entorno correcto

```cmd
python --version
where python
```

La ruta debería apuntar a:

```text
.venv\Scripts\python.exe
```

---

### 🔹 Instalar dependencias

```cmd
pip install -r requirements.txt
```

> ℹ️ **Nota técnica**  
> Aunque aquí se muestre `pip install ...`, los scripts automatizados usan  
> `.\.venv\Scripts\python -m pip` para garantizar que las dependencias se  
> instalen siempre dentro del entorno virtual correcto.

---

## 🚀 3. Scripts CMD incluidos

Los scripts `.cmd` permiten automatizar la creación y reconstrucción del entorno virtual desde **Command Prompt (CMD)**.

| Script | Acción principal | Cuándo usarlo |
|------|------------------|--------------|
| `setup_venv_from_requirements.cmd` | Crea el entorno e instala dependencias. | Primera configuración o actualización. |
| `reset_venv_from_requirements.cmd` | Borra y recrea el entorno desde cero. | Entorno roto o limpieza total. |

---

## 🧱 4. Ejemplos de uso

Desde la raíz del proyecto, ejecuta:

```cmd
"Scripts CMD\setup_venv_from_requirements.cmd"
```

Para borrar y recrear el entorno:

```cmd
"Scripts CMD\reset_venv_from_requirements.cmd"
```

El script pedirá confirmación antes de eliminar el entorno virtual.
</details>

---
---

<details><summary>requirements.txt</summary>

```txt
requests==2.32.3
flask==3.0.3
pandas==2.2.3
reportlab==4.4.4
pillow==11.3.0
tzdata==2025.2
```
</details>

---
---

<details><summary>Scripts CMD</summary>

<details><summary>setup_venv_from_requirements.cmd</summary>

```cmd
@echo off

REM =================================================
REM  Script para CREAR y CONFIGURAR entorno virtual
REM =================================================

REM Ir a la raiz del proyecto
cd /d "%~dp0\.."

REM Directorio del entorno virtual
set VENV_DIR=.venv

echo [*] Verificando Python...
python --version || (
    echo [X] Python no esta disponible en el PATH
    pause
    exit /b 1
)

REM Crear entorno si no existe
if not exist "%VENV_DIR%" (
    echo [*] Creando entorno virtual en %VENV_DIR%
    python -m venv %VENV_DIR%

    if errorlevel 1 (
        echo [X] Error al crear el entorno virtual
        pause
        exit /b 1
    )
)

REM Verificar que el script de activacion exista
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo [X] No se puede activar el entorno virtual
    pause
    exit /b 1
)

echo [*] Activando entorno...
call %VENV_DIR%\Scripts\activate.bat

echo [*] Actualizando pip...
%VENV_DIR%\Scripts\python -m pip install --upgrade pip

if exist requirements.txt (
    echo [*] Instalando dependencias desde requirements.txt
    %VENV_DIR%\Scripts\python -m pip install -r requirements.txt
) else (
    echo [!] No se encontro requirements.txt en la raiz del proyecto
)

echo.
echo [*] Entorno configurado y activo
python --version
where python
pip list

cmd /K
```
</details>
<details><summary>reset_venv_from_requirements.cmd</summary>

```cmd
@echo off

REM =================================================
REM  Script para BORRAR y RECREAR entorno virtual
REM =================================================

REM Ir a la raiz del proyecto
cd /d "%~dp0\.."

set VENV_DIR=.venv

echo =================================================
echo  Script para BORRAR y RECREAR el entorno virtual
echo =================================================
echo.

set /p CONFIRM="Quieres borrar y recrear el entorno %VENV_DIR%? (S/N): "

if /I not "%CONFIRM%"=="S" (
    echo [!] Operacion cancelada por el usuario
    pause
    exit /b 0
)

echo [*] Verificando Python...
python --version || (
    echo [X] Python no esta disponible en el PATH
    pause
    exit /b 1
)

if exist "%VENV_DIR%" (
    echo [*] Eliminando entorno existente...
    rmdir /s /q "%VENV_DIR%"
)

echo [*] Creando entorno virtual nuevo...
python -m venv %VENV_DIR%

if errorlevel 1 (
    echo [X] Error al crear el entorno virtual
    pause
    exit /b 1
)

if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo [X] No se puede activar el entorno virtual
    pause
    exit /b 1
)

echo [*] Activando entorno...
call %VENV_DIR%\Scripts\activate.bat

echo [*] Actualizando pip...
%VENV_DIR%\Scripts\python -m pip install --upgrade pip

if exist requirements.txt (
    echo [*] Instalando dependencias desde requirements.txt...
    %VENV_DIR%\Scripts\python -m pip install -r requirements.txt
) else (
    echo [!] No se encontro requirements.txt en la raiz del proyecto
)

echo.
echo [*] Entorno recreado y activo
python --version
where python
pip list

cmd /K
```
</details>

</details>

---
