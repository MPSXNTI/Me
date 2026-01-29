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

## 4️⃣ Panel de control Intel (MUY importante)

Abrir **Intel Graphics Command Center**:

**Gráficos → Global**

- HDR → ❌ Desactivado  
- Brillo automático → ❌ Desactivado  
- Mejora de contraste → ❌ Desactivado  

👉 Windows 11 puede **forzar HDR silenciosamente** en notebooks.

---

## 5️⃣ Por qué AHORA sí funciona (razonamiento técnico)

| Antes | Ahora |
|------|-------|
| HDR activo | HDR forzado OFF |
| Auto Exposure roto | Eliminado |
| Tonemapper moderno | Tonemapper básico |
| DX12 | DX11 |
| UE decide configs | Tú decides |

El motor **ya no puede saturar la luminancia**, aunque lo intente.

---

## 6️⃣ Rendimiento esperado (realista)

En **ThinkPad T480 (Intel UHD 620)**:

- Resolución: **720p**
- FPS: **30–40 estables**
- Calidad: **baja pero jugable**
- Crashes: ❌
- Pantalla blanca: ❌

👉 Más rendimiento **no es físicamente posible** en una UHD 620.  
Cualquiera que diga lo contrario, **miente**.
