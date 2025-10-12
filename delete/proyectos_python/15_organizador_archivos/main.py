import shutil
from pathlib import Path

REGLAS = {
    ".jpg": "imagenes",
    ".png": "imagenes",
    ".pdf": "documentos",
    ".txt": "texto",
    ".csv": "datos",
}

def organizar(origen="."):
    p = Path(origen)
    for archivo in p.iterdir():
        if archivo.is_file():
            ext = archivo.suffix.lower()
            destino = REGLAS.get(ext, "otros")
            (p / destino).mkdir(exist_ok=True)
            (p / destino / archivo.name).write_bytes(archivo.read_bytes())
            archivo.unlink()

if __name__ == "__main__":
    organizar(".")