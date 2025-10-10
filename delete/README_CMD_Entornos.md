# ⚙️ Scripts CMD para entornos virtuales de Python en Windows (VS Code + CMD)

Esta guía práctica reúne los **4 scripts principales** para crear, resetear y abrir entornos virtuales en Windows, junto con consejos avanzados para su uso en **VS Code**.

---

## 🚀 Scripts incluidos

| Script | Acción principal | Cuándo usarlo |
|--------|------------------|----------------|
| `setup_venv_from_requirements.cmd` | Crea y configura el entorno desde `requirements.txt`. | Primera vez o al actualizar dependencias. |
| `reset_venv_from_requirements.cmd` | Borra y recrea el entorno desde cero. | Cuando el entorno está roto o quieres empezar limpio. |
| `provision_and_open_venv.cmd` | Provisiona y deja la terminal abierta con `.venv` activo. | Para iniciar rápido y trabajar al instante. |
| `open_venv_here.cmd` | Abre una CMD con el entorno ya activado. | Si ya existe `.venv` y solo quieres usarlo. |

---

## ✅ Requisitos previos

- **Python 3.x** instalado y agregado al **PATH**.  
- Ejecutar siempre desde **CMD**, no PowerShell.  
- (Opcional) `requirements.txt` en la raíz del proyecto.  
- VS Code con la extensión oficial de Python.

---

## 📂 Estructura recomendada del proyecto

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

## 🧠 Conceptos clave

- **Entorno virtual (`.venv`)** → Espacio aislado de dependencias.  
- **Activar entorno** → `.venv\Scripts\activate.bat`  
- **Instalar paquetes** → `pip install -r requirements.txt`  
- **Desactivar** → `deactivate` o `.venv\Scripts\deactivate.bat`

---

## 🧭 Uso rápido

| Situación | Script sugerido |
|------------|----------------|
| Primera instalación | `setup_venv_from_requirements.cmd` |
| Entorno roto o desactualizado | `reset_venv_from_requirements.cmd` |
| Quiero trabajar ahora mismo | `provision_and_open_venv.cmd` |
| Solo abrir el entorno | `open_venv_here.cmd` |

---

## 🧯 Solución rápida de errores

| Problema | Causa posible | Solución |
|-----------|----------------|-----------|
| `'python' no se reconoce` | Python no está en PATH | Reinstala marcando **Add Python to PATH** |
| PowerShell muestra errores | Terminal incorrecta | Cambia a **CMD** desde *Terminal: Select Default Profile* |
| `.venv` no existe | No fue creado aún | Ejecuta `setup_venv_from_requirements.cmd` |
| Dependencias no instaladas | Falta `requirements.txt` | Crea con `pip freeze > requirements.txt` |

---

## 🧩 Integración con VS Code

1. `Ctrl+Shift+P` → **Python: Select Interpreter**  
   → Selecciona `.venv\Scripts\python.exe`.  
2. Si no aparece, usa **Enter Interpreter Path → Find...**  
3. Cambia terminal a **Command Prompt (CMD)** si ves errores PowerShell.  
4. Para refrescar dependencias:  
   - `Python: Restart Language Server` o  
   - `Developer: Reload Window`.

---

## 🧠 Tips avanzados

- Puedes mantener **varios entornos** (`.venvA`, `.venvB`) para pruebas.  
- Divide dependencias (`requirements.txt` y `requirements-dev.txt`).  
- Usa `reset_venv_from_requirements.cmd` para limpiar conflictos de versiones.

---

💡 **Consejo final:**  
Un entorno por proyecto, `requirements.txt` versionado, y scripts siempre en la raíz.  
Con estos comandos tendrás entornos limpios, reproducibles y fáciles de usar.

---

© 2025 – Documentación técnica unificada basada en *README friendly + profesional + guías completas*.
