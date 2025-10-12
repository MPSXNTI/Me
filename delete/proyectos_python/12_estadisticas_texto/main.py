import pandas as pd
import re

def palabras(texto):
    return re.findall(r"[\wáéíóúüñ]+", texto.lower())

def main():
    t = input("Texto: ")
    ws = palabras(t)
    s = pd.Series(ws)
    print("Total palabras:", len(ws))
    print("Longitud media:", s.str.len().mean())
    print("Más comunes:")
    print(s.value_counts().head(10))

if __name__ == "__main__":
    main()