# README — Entorno Virtual en VS Code (Windows CMD)

## 1. Propósito
Guía práctica para crear y configurar un **entorno virtual de Python (`.venv`)** en **VS Code usando Windows CMD**.  
Aprenderás a:
- Crear, activar y desactivar un entorno virtual.  
- Instalar y administrar dependencias con `pip`.  
- Configurar VS Code para usar correctamente `.venv`.  
- Resolver errores comunes del analizador y la terminal.

---

## 2. Preparación del entorno

### Abrir CMD y ubicarse en el proyecto
```cmd
cd C:\Users\TuUsuario\Desktop\python
```

### Verificar instalación de Python
```cmd
python --version
where python
```
Deberías ver rutas hacia tu instalación de Python.  

---

## 3. Crear y activar el entorno virtual
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

Si todo va bien, tu prompt mostrará:
```
(.venv) C:\Users\TuUsuario\Desktop\python>
```

---

## 4. Instalar dependencias dentro del entorno
Ejemplo:
```cmd
pip install requests
```

---

## 5. Comprobar que VS Code usa el entorno
```cmd
python --version
where python
```
Debe apuntar a:
```
.venv\Scripts\python.exe
```

---

## 6. Desactivar el entorno virtual

Cuando termines de trabajar, puedes **desactivar el entorno** de dos formas equivalentes:

**Opción 1 — Comando integrado de Python**
```cmd
deactivate
```

**Opción 2 — Script directo del entorno**
```cmd
.venv\Scripts\deactivate.bat
```

Tras esto, el prefijo `(.venv)` desaparecerá del prompt, indicando que volviste al entorno global.

---

## 7. Configurar VS Code

**Seleccionar el intérprete:**
- `Ctrl+Shift+P` → `Python: Select Interpreter`.
- Elige `.venv\Scripts\python.exe`.

**Cambiar terminal por defecto a CMD:**
- `Ctrl+Shift+P` → `Terminal: Select Default Profile`.
- Selecciona **Command Prompt (cmd)**.
- Cierra y reabre la terminal (`Ctrl+ñ`).

---

## 8. Solución de errores comunes

**Reiniciar analizador de Python:**
- `Ctrl+Shift+P` → `Python: Restart Language Server`.
- O `Ctrl+Shift+P` → `Developer: Reload Window`.

**Reiniciar la terminal:**
- Cierra con 🗑️ → abre una nueva → reactiva el entorno:
  ```cmd
  .venv\Scripts\activate.bat
  ```

**Forzar selección manual del intérprete:**
1. `Ctrl+Shift+P` → `Python: Select Interpreter`
2. `Enter Interpreter Path` → `Find...`
3. Busca:
   ```
   C:\Users\TuUsuario\Desktop\python\.venv\Scripts\python.exe
   ```

---

## 9. Notas rápidas
- Los bloques de código están pensados para **CMD**, no para celdas de Python.  
- Si ves el error *ExecutionPolicy*, estás en PowerShell: cambia la terminal a CMD.  
- `.venv` se guarda localmente y no debe subirse a GitHub.  
