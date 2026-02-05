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
| `Scripts CMD/open_venv_here.cmd` | Abre el entorno virtual (`venv`) en la carpeta actual, útil para pruebas o trabajo directo. |
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
│   └── requirements_example.txt
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
   Este script creará un entorno `venv` e instalará las dependencias de `requirements_example.txt`.

4. **Activa el entorno virtual manualmente (si prefieres hacerlo tú).**
   ```bash
   venv\Scripts\activate
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
python -m venv venv

# Activar entorno en CMD
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Listar paquetes instalados
pip list
```
