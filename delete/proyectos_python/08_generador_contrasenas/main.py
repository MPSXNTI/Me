import random, string

def generar(longitud=12, mayus=True, numeros=True, simbolos=True):
    base = list(string.ascii_lowercase)
    if mayus: base += list(string.ascii_uppercase)
    if numeros: base += list(string.digits)
    if simbolos: base += list("!@#$%^&*()-_=+[]{};:,.?/")
    random.shuffle(base)
    return "".join(random.choice(base) for _ in range(longitud))

if __name__ == "__main__":
    print(generar(16))