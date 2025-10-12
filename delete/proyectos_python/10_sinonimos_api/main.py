import requests

def sinonimos(palabra):
    url = f"https://api.datamuse.com/words?rel_syn={palabra}&lang=es"
    r = requests.get(url, timeout=10); r.raise_for_status()
    return [item["word"] for item in r.json()]

if __name__ == "__main__":
    q = input("Palabra: ").strip()
    print(sinonimos(q)[:20])