import random

def main():
    objetivo = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            intento = int(input("Adivina un número (1-100): "))
        except ValueError:
            print("Por favor ingresa un número entero.")
            continue
        intentos += 1
        if intento == objetivo:
            print(f"¡Correcto! Lo lograste en {intentos} intentos.")
            break
        print("Más grande" if intento < objetivo else "Más pequeño")

if __name__ == "__main__":
    main()