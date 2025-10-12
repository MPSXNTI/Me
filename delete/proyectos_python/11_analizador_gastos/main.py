import pandas as pd
import matplotlib.pyplot as plt

def main():
    ruta = input("Ruta CSV de gastos: ")
    df = pd.read_csv(ruta)
    # Se esperan columnas: categoria, monto, fecha
    df["monto"] = pd.to_numeric(df["monto"], errors="coerce").fillna(0)
    por_cat = df.groupby("categoria")["monto"].sum().sort_values(ascending=False)
    print(por_cat)
    por_cat.plot(kind="bar")
    plt.title("Gasto por categoría")
    plt.xlabel("Categoría"); plt.ylabel("Monto")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()