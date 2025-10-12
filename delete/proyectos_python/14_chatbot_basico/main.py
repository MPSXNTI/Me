REGLAS = {
    "hola": "¡Hola! ¿En qué puedo ayudarte?",
    "adios": "¡Hasta luego!",
    "ayuda": "Puedo responder saludos y despedidas por ahora."
}

def responder(msg):
    m = msg.lower().strip()
    for k, v in REGLAS.items():
        if k in m:
            return v
    return "No entendí, ¿puedes reformular?"

if __name__ == "__main__":
    while True:
        txt = input("> ")
        if txt.lower() in ("salir", "exit", "quit"):
            break
        print(responder(txt))