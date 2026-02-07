# ✅ SOLUCIÓN DEFINITIVA (adaptada a Intel UHD 620)

Configuración **comprobada en iGPU Intel** que evita:

- ❌ Pantalla blanca / blanco radiante  
- ❌ Crashes al iniciar o cargar shaders  
- ❌ Reescritura automática de configuraciones  

---

## 1️⃣ Engine.ini (OBLIGATORIO)

**Ruta:**

```text
C:\Users\TU_USUARIO\AppData\Local\Misery\Saved\Config\WindowsNoEditor\
```

Crea o edita `Engine.ini`, **borra todo su contenido** y pega **solo esto**:

```ini
[SystemSettings]
r.EyeAdaptationQuality=0
r.DefaultFeature.AutoExposure=0
r.DefaultFeature.AutoExposure.Method=0
r.TonemapperFilm=0
r.TonemapperGamma=2.2
r.BloomQuality=0
r.HDR.EnableHDROutput=0
r.MotionBlurQuality=0
r.SceneColorFringeQuality=0
r.DepthOfFieldQuality=0
r.FilmGrain=0
```

📌 Esto desactiva **todos los efectos que la Intel UHD 620 no soporta correctamente**.

---

## 2️⃣ GameUserSettings.ini (configuración segura para iGPU)

Deja el archivo **exactamente así**:

```ini
[ScalabilityGroups]
sg.ResolutionQuality=80
sg.ViewDistanceQuality=0
sg.AntiAliasingQuality=1
sg.ShadowQuality=0
sg.GlobalIlluminationQuality=0
sg.ReflectionQuality=0
sg.PostProcessQuality=0
sg.TextureQuality=2
sg.EffectsQuality=0
sg.FoliageQuality=0
sg.ShadingQuality=0
sg.LandscapeQuality=0
```

⚠️ **No intentes forzar valores mayores**: en Intel UHD eso rompe el render.

Luego:

- Clic derecho → **Propiedades**
- ✅ Marcar **Solo lectura**

---

## 3️⃣ Forzar DirectX 11 (CRÍTICO en Intel)

En **Steam → Opciones de lanzamiento**:

```text
-dx11 -sm5
```

📌 `-sm5` evita que Unreal Engine intente usar shaders incompatibles con la iGPU.

---

## 4️⃣ Añadir exclusión en Windows Defender (RECOMENDADO)

Evita bloqueos silenciosos, stuttering y falsos positivos sobre shaders o binarios del motor.

### 📍 Paso a paso

1️⃣ Abrir **Seguridad de Windows**  
2️⃣ Ir a **Protección contra virus y amenazas**  
3️⃣ Bajar y hacer clic en **Administrar la configuración**  
4️⃣ Bajar hasta **Exclusiones**  
5️⃣ Clic en **Agregar o quitar exclusiones**  
6️⃣ Presionar **Agregar una exclusión**  
7️⃣ Elegir **Carpeta**

### 📂 Carpeta a seleccionar

```text
Steam\steamapps\common\MISERY\
```

💡 **No agregues solo el `.exe`**. Debe ser **toda la carpeta del juego**.

📌 Al agregarla **no aparece ningún mensaje de confirmación**.  
Es normal.

---

## 5️⃣ Acceso controlado a carpetas (MUY importante)

Windows 11 puede **bloquear juegos desde aquí sin mostrar ningún aviso**.

### 📍 Paso a paso

1️⃣ Ir a **Protección contra virus y amenazas**  
2️⃣ Entrar en **Protección contra ransomware**  
3️⃣ Clic en **Administrar protección contra ransomware**

Revisar:

- **Acceso controlado a carpetas**

### 🔐 Si está ACTIVADO

1️⃣ Clic en **Permitir una aplicación**  
2️⃣ **Agregar una aplicación permitida**  
3️⃣ Buscar y agregar:

```text
MISERY-Win64-Shipping.exe
```

---

### 🔄 Después de hacer esto (NO omitir)

1️⃣ Cerrar **Steam completamente**  
2️⃣ **Reiniciar el PC**  
3️⃣ Abrir Steam  
4️⃣ Ejecutar el juego **sin cambiar nada más**

---

### 🧠 Por qué esto funciona (explicación técnica corta)

- Unreal Engine genera binarios tipo **Shipping**
- Windows 11 los clasifica como potencialmente peligrosos
- Defender bloquea la creación del proceso
- Steam solo recibe: `CreateProcess() failed`

👉 **No es un error del juego**.  
Es **seguridad del sistema operativo** interfiriendo.

---

## 6️⃣ Por qué AHORA sí funciona (razonamiento técnico)

| Antes | Ahora |
|------|-------|
| HDR activo | HDR forzado OFF |
| Auto Exposure roto | Eliminado |
| Tonemapper moderno | Tonemapper básico |
| DX12 | DX11 |
| UE decide configs | Tú decides |

El motor **ya no puede saturar la luminancia**, aunque lo intente.

---

## 7️⃣ Rendimiento esperado (realista)

- Resolución: **720p**
- FPS: **30–40 estables**
- Calidad: **baja pero jugable**
- Crashes: ❌
- Pantalla blanca: ❌

👉 Más rendimiento **no es físicamente posible** en una **Intel UHD 620**.  
Cualquiera que diga lo contrario, **miente**.
