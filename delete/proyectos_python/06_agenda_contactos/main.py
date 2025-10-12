import csv
from pathlib import Path

ARCHIVO = Path("contactos.csv")
CAMPOS = ["nombre", "telefono", "email"]

def guardar_contacto(contacto):
    existe = ARCHIVO.exists()
    with ARCHIVO.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        if not existe:
            writer.writeheader()
        writer.writerow(contacto)

def buscar_contactos(q):
    if not ARCHIVO.exists(): return []
    with ARCHIVO.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [r for r in reader if q.lower() in (r["nombre"]+r["email"]).lower()]

def main():
    while True:
        op = input("(n)uevo, (b)uscar, (s)alir: ").strip().lower()
        if op == "n":
            nombre = input("Nombre: "); tel = input("Teléfono: "); email = input("Email: ")
            guardar_contacto({"nombre": nombre, "telefono": tel, "email": email})
            print("Guardado.")
        elif op == "b":
            q = input("Buscar: "); resultados = buscar_contactos(q)
            for r in resultados: print(r)
        elif op == "s":
            break

if __name__ == "__main__":
    main()