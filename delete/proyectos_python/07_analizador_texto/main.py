from collections import Counter
from pathlib import Path
import re

def tokens(path):
    texto = Path(path).read_text(encoding="utf-8", errors="ignore").lower()
    return re.findall(r"[\wáéíóúüñ]+", texto)

def main():
    archivo = input("Ruta del archivo .txt: ").strip()
    palabras = tokens(archivo)
    print(f"Total palabras: {len(palabras)}")
    for w, c in Counter(palabras).most_common(20):
        print(f"{w}: {c}")

if __name__ == "__main__":
    main()