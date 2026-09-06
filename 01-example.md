# Guía Rápida: Configuración de Disco Maestro Multipropósito (Ventoy + Windows To Go + Almacenamiento)

## 1. Instalación y preparación del disco con Ventoy
Ejecute la aplicación **Ventoy2Disk** > Seleccione el disco > Antes de instalar, acceda a:
```
Opción (Option) > Estilo de partición (Partition Style) > GPT
```
```
Opción (Option) > Configuración de partición (Partition Configuration) > Preservar espacio al final del disco (Reserve Space)
```
## 2. Creación de particiones para Windows To Go (WTG)
### Partición de arranque EFI
```cmd
diskpart
list disk
select disk X
create partition efi size=300
format quick fs=fat32 label="boot"
assign letter=S
```
### Partición del sistema operativo Windows To Go
```cmd
create partition primary
format quick fs=ntfs label="ntfs"
assign letter=W
```
## 3. Restauración de la imagen del sistema mediante Clonezilla
Restaure la imagen correspondiente a la **partición de arranque EFI** sobre la partición `boot` creada en el paso anterior.<br>Restaure la imagen correspondiente al **sistema operativo** sobre la partición `ntfs`.
## 4. Modificación del tipo de partición EFI en Windows
```cmd
diskpart
list disk
select disk X
list partition
select partition Y
```
Asigne el GUID correspondiente al tipo de partición **EFI System Partition**: `set id=c12a7328-f81f-11d2-ba4b-00a0c93ec93b override`
## 5. Reconstrucción del BCD (Boot Configuration Data)
```cmd
bcdboot W:\Windows /l es-es /s S: /f ALL
```
## 6. Creación del enlace `vlnk` de Ventoy (integración del arranque WTG)
```
VentoyVlnk > Create > Navegue dentro de la partición EFI hasta la ruta: `\EFI\Microsoft\Boot\` > Seleccione el archivo `bootmgfw.efi` > Mover el archivo `bootmgfw.vlnk.efi` generado a la partición principal de Ventoy
```
## 7. Creación de particiones de datos adicionales
```cmd
diskpart
select disk X
create partition primary
format quick fs=ntfs label="DATOS"
assign letter=D
```
