
---

<details><summary>Readme.md</summary>

# 🐍 Kit de Entornos Python (Windows / CMD)

Este proyecto proporciona una colección de **scripts y guía** para configurar, gestionar y automatizar entornos virtuales de Python en **Windows usando la línea de comandos (CMD)** y **VSCode**.  
Ideal para desarrolladores que desean mantener entornos limpios, reproducibles y rápidos de activar.

---

## Resumen rápido (Quickstart)

```cmd
# 1️⃣ Crea el entorno virtual
python -m venv .venv

# 2️⃣ Activa el entorno
.venv\Scripts\activate.bat

# 3️⃣ Desactivar el entorno
deactivate

# 4️⃣ Instala dependencias (si tienes requirements.txt)
pip install -r requirements.txt

# 5️⃣ Listar paquetes instalados
pip list
```

---

## 📂 Contenido

| Archivo / Carpeta | Descripción |
|--------------------|-------------|
| `requirements.txt` | Ejemplo de archivo `requirements.txt` para instalar dependencias rápidamente en un entorno virtual. |
| `Scripts CMD/setup_venv_from_requirements.cmd` | Crea un entorno virtual nuevo e instala las dependencias desde `requirements.txt`. |
| `Scripts CMD/reset_venv_from_requirements.cmd` | Elimina el entorno actual y lo reconstruye desde el archivo `requirements.txt`. |

---

## 📂 1. Estructura recomendada del proyecto

```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 └─ Scripts CMD/
     ├─ setup_venv_from_requirements.cmd
     └─ reset_venv_from_requirements.cmd
```

---

## 🧱 2. Crear y configurar el entorno paso a paso

### Cambiar la terminal por defecto a CMD
1. `Ctrl + Shift + P` → **Terminal: Select Default Profile**
2. Elige **Command Prompt (cmd)**
3. Cierra y reabre la terminal con `Ctrl + ñ`

### 🔹 Abrir CMD y posicionarte en tu proyecto
```cmd
cd C:\Users\TuUsuario\Desktop\mi_proyecto
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
(.venv) C:\Users\TuUsuario\Desktop\mi_proyecto>
```

### Verificar que VS Code usa el entorno correcto
```cmd
python --version
where python
```
Debería apuntar a:  
`.venv\Scripts\python.exe` ✅

### 🔹 Instalar dependencias
```cmd
pip install -r requirements.txt
```

---

## 🚀 3. ¿Qué son estos scripts?

Son archivos `.cmd` (o `.bat`) que ejecutan automáticamente comandos de Python y `pip` desde la terminal de **Command Prompt (CMD)**.  
Te permiten crear, reiniciar o abrir tu entorno virtual en segundos ⚡

| Script | Acción principal | Cuándo usarlo |
|--------|------------------|----------------|
| `setup_venv_from_requirements.cmd` | Crea y configura el entorno desde `requirements.txt`. | Primera vez o al actualizar dependencias. |
| `reset_venv_from_requirements.cmd` | Borra y recrea el entorno desde cero. | Cuando el entorno está roto o quieres empezar limpio. |

---

## 🧱 4. Ejemplos de uso

Abre una terminal **CMD** dentro del proyecto y ejecuta:

```cmd
# Crear entorno e instalar dependencias
"Scripts CMD\setup_venv_from_requirements.cmd"

# Reiniciar el entorno desde cero
"Scripts CMD\reset_venv_from_requirements.cmd"
```
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

REM Ir a la raiz del proyecto
cd /d "%~dp0\.."

REM Directorio del entorno virtual
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

REM Ir a la raiz del proyecto
cd /d "%~dp0\.."

set VENV_DIR=.venv

echo =================================================
echo  Script para BORRAR y RECREAR el entorno virtual
echo =================================================
echo.

set /p CONFIRM="Quieres borrar y recrear el entorno %VENV_DIR%? (S/N): "

if /I "%CONFIRM%"=="S" (

    if exist "%VENV_DIR%" (
        echo [*] Eliminando entorno existente...
        rmdir /s /q "%VENV_DIR%"
    ) else (
        echo [!] No existe un entorno previo, se creara uno nuevo
    )

    echo [*] Creando entorno virtual nuevo...
    python -m venv %VENV_DIR%

    echo [*] Activando entorno...
    call %VENV_DIR%\Scripts\activate.bat

    echo [*] Actualizando pip...
    python -m pip install --upgrade pip

    if exist requirements.txt (
        echo [*] Instalando dependencias desde requirements.txt...
        pip install -r requirements.txt
    ) else (
        echo [!] No se encontro requirements.txt en la raiz del proyecto
    )

    echo.
    echo [*] Entorno recreado y activo
    python --version
    where python
    pip list

    cmd /K
) else (
    echo [!] Operacion cancelada por el usuario
    pause
)
```
</details>

</details>

---
