@echo off
cd /d "%~dp0"
if exist .venv (
  call .venv\Scripts\activate.bat
  cmd /K
) else (
  echo [!] No existe el entorno .venv en este directorio.
  pause
)
