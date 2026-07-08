import requests

LAT = 40.1950
LON = 29.0600


def get_weather():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}"
        f"&longitude={LON}"
        "&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
    )

    r = requests.get(url, timeout=5)

    r.raise_for_status()

    current = r.json()["current"]

    return {

        "city": "Bursa",

        "temperature": current["temperature_2m"],

        "humidity": current["relative_humidity_2m"],

        "wind": current["wind_speed_10m"],

        "weather": weather_text(current["weather_code"]),

        "icon": weather_icon(current["weather_code"])

    }


def weather_text(code):

    table = {

        0: "Açık",

        1: "Az Bulutlu",

        2: "Parçalı Bulutlu",

        3: "Bulutlu",

        45: "Sisli",

        48: "Kırağı",

        51: "Çisenti",

        53: "Hafif Yağmur",

        55: "Yağmur",

        61: "Yağmur",

        63: "Sağanak",

        65: "Şiddetli Yağmur",

        71: "Kar",

        80: "Sağanak",

        95: "Fırtına"

    }

    return table.get(code, "Bilinmiyor")


def weather_icon(code):

    if code == 0:
        return "☀"

    if code in [1, 2]:
        return "🌤"

    if code == 3:
        return "☁"

    if code in [45, 48]:
        return "🌫"

    if code in [51, 53, 55, 61, 63, 65, 80]:
        return "🌧"

    if code == 71:
        return "❄"

    if code == 95:
        return "⛈"

    return "☀"