<details><summary></summary>

# Guía Técnica: Configuración de Disco Maestro Multipropósito (Ventoy + Windows To Go + Almacenamiento)

**Nombre de archivo sugerido:** `Guia_Configuracion_Master_Disk_WTG.md`

---

## Introducción

Este documento describe, paso a paso, el procedimiento técnico para estructurar un disco USB o SSD externo de alto rendimiento como un **"Disco Maestro"** multipropósito. La solución final combina tres capacidades en un único dispositivo de almacenamiento:

1. Un entorno de arranque múltiple (**multibot**) gestionado por **Ventoy**, capaz de lanzar isos de utilidades, sistemas live y herramientas de mantenimiento.
2. Una instalación funcional de **Windows To Go (WTG)** integrada de forma nativa en el menú de arranque de Ventoy mediante el mecanismo `vlnk`.
3. Particiones de almacenamiento adicionales para datos personales o de trabajo.

> **Nota general:** Este procedimiento implica operaciones de bajo nivel sobre tablas de particiones y sectores de arranque. Un error en la selección del disco de destino puede provocar **pérdida total de datos** en el disco equivocado. Verifique siempre el número de disco (`disk X`) antes de ejecutar cualquier comando destructivo.

### Requisitos previos

| Elemento | Descripción |
|---|---|
| Disco de destino | USB 3.0/3.1 o SSD externo (se recomienda mínimo 128 GB) |
| Herramienta Ventoy | Última versión estable descargada desde el sitio oficial |
| Medio Clonezilla | ISO o USB de arranque con Clonezilla Live |
| Imágenes de origen | Imagen previa de las particiones `boot` (EFI) y `ntfs` (Windows) generada con Clonezilla |
| Medio de instalación de Windows | USB de instalación de Windows (para acceder al entorno de recuperación/CMD) |
| Herramienta VentoyVlnk | Utilidad oficial de Ventoy para Windows |
| Equipo con arranque UEFI | El firmware debe soportar UEFI (no Legacy/BIOS puro) |

---

## 1. Instalación y preparación del disco con Ventoy

El primer paso consiste en preparar el disco base con Ventoy, dejando espacio reservado al final para las particiones que alojarán Windows To Go y el almacenamiento adicional.

### 1.1 Instalar Ventoy en el disco objetivo

1. Ejecute la aplicación **Ventoy2Disk** (en Windows) o el script `Ventoy2Disk.sh` (en Linux).
2. Seleccione el disco físico correcto en el desplegable de dispositivos.

> **Advertencia:** Confirme minuciosamente la letra/identificador del disco. Ventoy formateará por completo el dispositivo seleccionado.

### 1.2 Configurar el esquema de partición GPT

Antes de instalar, acceda a:

```
Opción (Option) > Estilo de partición (Partition Style)
```

Seleccione **GPT**. Este esquema es obligatorio para el arranque UEFI nativo y es requisito indispensable para que Windows To Go arranque correctamente en modo UEFI.

### 1.3 Reservar espacio al final del disco

Dentro del mismo panel de opciones, acceda a:

```
Opción (Option) > Configuración de partición (Partition Configuration)
```

Seleccione la opción de **preservar espacio al final del disco** ("Reserve Space") e indique el tamaño total que necesitará para:

- La partición EFI de WTG (recomendado: 300–500 MB).
- La partición NTFS del sistema Windows To Go (recomendado: 64–128 GB, según la imagen a restaurar).
- Las particiones de datos adicionales (el remanente que desee destinar a almacenamiento).

> **Consejo técnico:** Calcule el espacio reservado con margen adicional (10–15 %) para evitar reajustes posteriores, ya que redimensionar particiones tras la instalación de Ventoy puede requerir herramientas externas y presenta riesgo de corrupción de datos.

4. Confirme la instalación. Ventoy creará su partición principal (donde se almacenarán las ISOs) y dejará el espacio reservado como no asignado al final del disco.

---

## 2. Creación de particiones para Windows To Go (WTG)

Con el espacio reservado disponible, se procede a crear manualmente las dos particiones que alojarán el sistema Windows To Go. Esto puede realizarse desde `diskpart`, un Live CD de particionado, o el propio entorno de Clonezilla/GParted.

### 2.1 Partición de arranque EFI

- **Sistema de archivos:** FAT32
- **Etiqueta (label):** `boot`
- **Tamaño:** 300–500 MB

Ejemplo utilizando `diskpart`:

```cmd
diskpart
list disk
select disk X
create partition efi size=300
format quick fs=fat32 label="boot"
assign letter=S
```

### 2.2 Partición del sistema operativo Windows

- **Sistema de archivos:** NTFS
- **Etiqueta (label):** `ntfs`
- **Tamaño:** según la imagen del sistema a restaurar

```cmd
create partition primary
format quick fs=ntfs label="ntfs"
assign letter=W
```

> **Nota:** No es necesario asignar letras permanentes en este punto; se utilizan únicamente como referencia temporal para las siguientes fases.

---

## 3. Restauración de la imagen del sistema mediante Clonezilla

Con las particiones `boot` y `ntfs` creadas y formateadas, se procede a desplegar el contenido del sistema operativo previamente respaldado.

1. Arranque el equipo desde el medio de Clonezilla Live.
2. Seleccione el modo **Device-Image** (dispositivo a imagen o viceversa, según corresponda).
3. Elija la ubicación donde reside la imagen de origen (unidad local, red o almacenamiento externo).
4. Seleccione el modo experto y utilice la función **`restoreparts`** para restaurar particiones individuales (no el disco completo), evitando así sobrescribir el resto de la tabla de particiones del Disco Maestro.

```bash
# Ejemplo conceptual del flujo dentro de Clonezilla (modo experto)
# restoreparts: restaura una partición de origen (imagen) sobre una partición de destino existente
```

5. Restaure la imagen correspondiente a la **partición de arranque EFI** sobre la partición `boot` creada en el paso anterior.
6. Restaure la imagen correspondiente al **sistema operativo** sobre la partición `ntfs`.

> **Advertencia crítica:** Verifique con extremo cuidado la correspondencia entre partición de origen y partición de destino. Utilizar `restoreparts` sobre la partición incorrecta puede sobrescribir la partición de Ventoy o las particiones de datos ya existentes.

---

## 4. Modificación del tipo de partición EFI en Windows

Tras restaurar las imágenes, es necesario indicar explícitamente al sistema que la partición restaurada debe tratarse como una partición del **sistema EFI**, ya que el proceso de clonado no siempre preserva este atributo de tipo de partición GPT.

1. Arranque en un entorno Windows funcional (puede ser el propio WTG en un primer arranque de prueba, o un sistema Windows externo con el disco conectado).
2. Abra el **Símbolo del sistema (CMD)** como administrador.
3. Ejecute `diskpart` y localice el disco y partición correctos:

```cmd
diskpart
list disk
select disk X
list partition
select partition Y
```

4. Asigne el GUID correspondiente al tipo de partición **EFI System Partition**:

```cmd
set id=c12a7328-f81f-11d2-ba4b-00a0c93ec93b override
```

> **Nota técnica:** El GUID `c12a7328-f81f-11d2-ba4b-00a0c93ec93b` es el identificador estándar (definido por la especificación UEFI) para particiones del sistema EFI. El modificador `override` es necesario porque `diskpart` normalmente restringe el cambio de tipo en particiones que ya contienen un sistema de archivos formateado.

---

## 5. Reconstrucción del BCD (Boot Configuration Data)

Con la partición EFI correctamente tipificada, se deben regenerar los archivos de arranque para vincular el gestor de arranque de Windows con la instalación restaurada.

1. Arranque el equipo desde un **medio de instalación USB de Windows** (no el Disco Maestro).
2. En la pantalla de instalación, acceda a **Reparar el equipo > Solucionar problemas > Símbolo del sistema**.
3. Identifique las letras de unidad asignadas a las particiones `boot` (EFI) y `ntfs` (sistema) del Disco Maestro. En este entorno de recuperación, las letras pueden diferir de las habituales (por ejemplo, la partición EFI podría estar bajo `S:` y el sistema bajo `W:`); utilice `diskpart` y `list volume` para confirmarlas.
4. Ejecute `bcdboot` para generar los archivos de arranque:

```cmd
bcdboot W:\Windows /l es-es /s S: /f ALL
```

### Descripción de los parámetros

| Parámetro | Función |
|---|---|
| `W:\Windows` | Ruta de origen de los archivos del sistema operativo instalado, a partir de los cuales se generará el entorno de arranque. |
| `/l es-es` | Define el idioma (locale) de los archivos de arranque a generar; ajústelo según el idioma deseado para el menú de arranque. |
| `/s S:` | Especifica la unidad de destino (la partición EFI, en este caso `S:`) donde se escribirán los archivos de arranque UEFI. |
| `/f ALL` | Indica que se deben crear archivos de arranque compatibles con todos los firmwares soportados (UEFI y BIOS/Legacy), maximizando la compatibilidad del medio. |

> **Consejo técnico:** Si el sistema restaurado no arranca tras este paso, verifique que la partición EFI (`S:`) esté correctamente formateada en FAT32 y que no falten permisos de escritura sobre la misma.

---

## 6. Creación del enlace `vlnk` de Ventoy (integración del arranque WTG)

Esta fase es la que permite que la instalación de Windows To Go aparezca como una entrada seleccionable directamente en el menú de arranque de Ventoy, sin necesidad de reconfigurar el firmware ni utilizar un gestor de arranque externo.

1. Ejecute la herramienta oficial **VentoyVlnk** en un entorno Windows.
2. Haga clic en el botón **Create**.
3. Navegue dentro de la partición EFI hasta la ruta:

```
\EFI\Microsoft\Boot\
```

4. Seleccione el archivo `bootmgfw.efi`.
5. VentoyVlnk generará un archivo resultante denominado `bootmgfw.vlnk.efi`.
6. Copie o mueva el archivo `bootmgfw.vlnk.efi` generado a la **partición principal de Ventoy** (la misma unidad donde se almacenan los archivos ISO).

> **Nota técnica:** El archivo `.vlnk.efi` funciona como un puntero simbólico interpretado por el propio gestor de arranque de Ventoy: al seleccionarlo desde el menú, Ventoy redirige la ejecución hacia el `bootmgfw.efi` real ubicado en la partición EFI de WTG, permitiendo el arranque de Windows To Go sin necesidad de modificar las entradas de arranque del firmware (UEFI NVRAM).

> **Consejo:** Reinicie el equipo y verifique que la nueva entrada aparece en el menú de Ventoy antes de continuar con la creación de particiones adicionales, a fin de detectar cualquier inconveniente mientras el estado del disco aún es sencillo de depurar.

---

## 7. Creación de particiones de datos adicionales

Con el entorno WTG completamente funcional e integrado en el menú de Ventoy, se procede a aprovechar el espacio libre restante del disco para almacenamiento de propósito general.

1. Abra `diskpart` o la **Administración de discos** y localice el espacio no asignado remanente en el Disco Maestro.
2. Cree una o varias particiones según sus necesidades de organización (por ejemplo, una partición para documentos y otra para respaldo de proyectos).

```cmd
diskpart
select disk X
create partition primary
format quick fs=ntfs label="DATOS"
assign letter=D
```

### Recomendaciones de formato

| Sistema de archivos | Caso de uso recomendado |
|---|---|
| **NTFS** | Uso exclusivo en entornos Windows; soporta permisos avanzados y archivos individuales de gran tamaño. |
| **exFAT** | Compatibilidad multiplataforma (Windows, macOS, Linux); ideal si el disco se usará en distintos sistemas operativos. |

> **Nota final:** Etiquete claramente cada partición de datos para facilitar su identificación en el menú de Ventoy y en el explorador de archivos. Evite nombrar estas particiones con etiquetas idénticas a `boot` o `ntfs`, reservadas para el entorno WTG, con el fin de prevenir confusiones al momento de realizar mantenimiento futuro del disco.

---

## Resumen del resultado final

Al completar esta guía, el Disco Maestro quedará estructurado de la siguiente manera:

1. **Partición principal de Ventoy** — contiene las ISOs de arranque y el archivo `bootmgfw.vlnk.efi`.
2. **Partición EFI de WTG** (`boot`, FAT32, sin letra asignada) — arranque UEFI de Windows To Go.
3. **Partición del sistema WTG** (`ntfs`, NTFS) — instalación funcional de Windows.
4. **Partición(es) de datos** (NTFS/exFAT) — almacenamiento de propósito general.

> **Recomendación de mantenimiento:** Conserve una copia de la imagen generada con Clonezilla (particiones `boot` y `ntfs`) en un medio independiente. Esto permitirá reconstruir el entorno WTG rápidamente en caso de corrupción del disco, sin necesidad de repetir la instalación completa de Windows.
</details>

<!-- Última actualización DD/MM/AAAA ; Ln [--.---] ; Col [---.---] -->

-

<!--
# ÍNDICE GENERAL Y RANGOS DE LÍNEAS
| Nombre | Rango Línea |
|--------|-------------|
| (-) - | [-] |
-->
<details><summary></summary></details>
