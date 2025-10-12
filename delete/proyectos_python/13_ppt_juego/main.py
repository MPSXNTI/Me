import random

OPCIONES = ("piedra", "papel", "tijera")
GANA_A = {"piedra": "tijera", "tijera": "papel", "papel": "piedra"}

def jugar(rondas=3):
    jugador_pts = pc_pts = 0
    for _ in range(rondas):
        jug = input("Elige (piedra/papel/tijera): ").strip().lower()
        if jug not in OPCIONES:
            print("Opción inválida."); continue
        pc = random.choice(OPCIONES)
        print(f"PC eligió: {pc}")
        if jug == pc: print("Empate")
        elif GANA_A[jug] == pc: print("¡Ganaste!"); jugador_pts += 1
        else: print("Perdiste"); pc_pts += 1
    print(f"Marcador final -> Tú: {jugador_pts} | PC: {pc_pts}")

if __name__ == "__main__":
    jugar(5)