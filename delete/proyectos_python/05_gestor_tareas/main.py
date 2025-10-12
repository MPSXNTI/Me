import json
from pathlib import Path

ARCHIVO = Path("tareas.json")

def cargar():
    if ARCHIVO.exists():
        return json.loads(ARCHIVO.read_text(encoding="utf-8"))
    return []

def guardar(tareas):
    ARCHIVO.write_text(json.dumps(tareas, ensure_ascii=False, indent=2), encoding="utf-8")

def agregar(tareas, desc):
    tareas.append({"desc": desc, "done": False})

def listar(tareas):
    for i, t in enumerate(tareas, 1):
        estado = "✅" if t["done"] else "⏳"
        print(f"{i}. {estado} {t['desc']}")

def completar(tareas, idx):
    tareas[idx]["done"] = True

def main():
    tareas = cargar()
    while True:
        cmd = input("(a)gregar, (l)istar, (c)ompletar, (q)uitar, (x) salir: ").strip().lower()
        if cmd == "a":
            desc = input("Descripción: ").strip()
            if desc: agregar(tareas, desc); guardar(tareas)
        elif cmd == "l":
            listar(tareas)
        elif cmd == "c":
            try:
                idx = int(input("Índice a completar: ")) - 1
                completar(tareas, idx); guardar(tareas)
            except Exception:
                print("Índice inválido.")
        elif cmd == "q":
            try:
                idx = int(input("Índice a eliminar: ")) - 1
                tareas.pop(idx); guardar(tareas)
            except Exception:
                print("Índice inválido.")
        elif cmd == "x":
            break
        else:
            print("Comando no reconocido.")

if __name__ == "__main__":
    main()