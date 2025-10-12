import os, requests

API_KEY = os.getenv("OPENWEATHER_API_KEY", "TU_API_KEY_AQUI")

def clima(ciudad="Santiago,CL"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": ciudad, "appid": API_KEY, "units": "metric", "lang": "es"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"{ciudad}: {temp}°C, {desc}")

if __name__ == "__main__":
    clima()