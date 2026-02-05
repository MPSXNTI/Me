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
