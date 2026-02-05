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
