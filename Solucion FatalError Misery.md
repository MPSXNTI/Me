# Solución definitiva – MISERY (Intel UHD Graphics 620)

Notebook Lenovo ThinkPad T480 – Windows 11

---

## Hardware objetivo

- GPU: Intel UHD Graphics 620
- Tipo: iGPU
- API estable: DirectX 11
- Resolución recomendada: 1280x720

---

## 1. Engine.ini (OBLIGATORIO)

**Ruta:**
C:\Users\TU_USUARIO\AppData\Local\Misery\Saved\Config\WindowsNoEditor\

Crear o editar el archivo **Engine.ini** y dejar **SOLO** este contenido:

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

**Motivo técnico:**
Desactiva Auto Exposure, HDR y postprocesado que la Intel UHD 620 no calcula correctamente y que provoca la pantalla blanca.

---

## 2. GameUserSettings.ini (config segura iGPU)

**Archivo:** GameUserSettings.ini

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

Luego:

- Clic derecho → Propiedades
- Marcar **Solo lectura**

**Nota importante:**
Solo este archivo debe estar en solo lectura.  
El ejecutable **NUNCA**.

---

## 3. Opciones de lanzamiento (Steam)

Steam → Propiedades → Opciones de lanzamiento:

```text
-dx11
```

**Motivo:**
Evita DX12, que causa crashes y errores de creación de proceso en iGPU Intel.

---

## Resultado esperado

- Sin pantalla blanca / sobreexposición
- Sin fatal error al iniciar partida
- Juego estable en Intel UHD Graphics 620
- Rendimiento esperado: 30–40 FPS en 720p
