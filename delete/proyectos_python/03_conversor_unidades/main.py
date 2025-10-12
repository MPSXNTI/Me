def c_to_f(c): return c * 9/5 + 32
def f_to_c(f): return (f - 32) * 5/9

def main():
    print("Conversor de temperatura")
    unidad = input("Convierte a (C/F): ").strip().upper()
    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("Ingresa un número válido.")
        return
    if unidad == "F":
        print(f"{valor} °C -> {round(c_to_f(valor), 2)} °F")
    elif unidad == "C":
        print(f"{valor} °F -> {round(f_to_c(valor), 2)} °C")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()