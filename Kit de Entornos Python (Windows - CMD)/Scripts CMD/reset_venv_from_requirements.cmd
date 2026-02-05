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
