def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplica(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b

OPERACIONES = {"+": suma, "-": resta, "*": multiplica, "/": divide}

def leer_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def main():
    a = leer_float("Primer número: ")
    b = leer_float("Segundo número: ")
    op = input("Operación (+, -, *, /): ").strip()
    func = OPERACIONES.get(op)
    if not func:
        print("Operación no soportada.")
        return
    try:
        resultado = func(a, b)
        print(f"Resultado: {round(resultado, 2)}")
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()