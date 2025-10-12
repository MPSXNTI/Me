import re
from collections import Counter

def limpiar_texto(t):
    return re.findall(r"[\wáéíóúüñ]+", t.lower())

def main():
    texto = input("Ingresa un texto: ")
    palabras = limpiar_texto(texto)
    print(f"Número de palabras: {len(palabras)}")
    conteo = Counter(palabras).most_common(10)
    print("Top 10 palabras:")
    for w, c in conteo:
        print(f"{w}: {c}")

if __name__ == "__main__":
    main()