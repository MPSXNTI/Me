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
deactivate or .venv\Scripts\deactivate.bat
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
