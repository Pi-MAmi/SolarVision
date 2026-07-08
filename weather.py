import requests

CITIES = {


    "Adana": (37.0000, 35.3213),
    "Adıyaman": (37.7648, 38.2786),
    "Afyonkarahisar": (38.7569, 30.5387),
    "Ağrı": (39.7191, 43.0503),
    "Aksaray": (38.3687, 34.0370),
    "Amasya": (40.6539, 35.8330),
    "Ankara": (39.9334, 32.8597),
    "Antalya": (36.8969, 30.7133),
    "Ardahan": (41.1105, 42.7022),
    "Artvin": (41.1828, 41.8183),
    "Aydın": (37.8560, 27.8416),
    "Balıkesir": (39.6484, 27.8826),
    "Bartın": (41.6344, 32.3375),
    "Batman": (37.8812, 41.1351),
    "Bayburt": (40.2552, 40.2249),
    "Bilecik": (40.1553, 29.9833),
    "Bingöl": (38.8854, 40.4983),
    "Bitlis": (38.4006, 42.1095),
    "Bolu": (40.7395, 31.6116),
    "Burdur": (37.7203, 30.2908),
    "Bursa": (40.1950, 29.0600),
    "Çanakkale": (40.1553, 26.4142),
    "Çankırı": (40.6013, 33.6134),
    "Çorum": (40.5506, 34.9556),
    "Denizli": (37.7765, 29.0864),
    "Diyarbakır": (37.9144, 40.2306),
    "Düzce": (40.8438, 31.1565),
    "Edirne": (41.6771, 26.5557),
    "Elazığ": (38.6748, 39.2232),
    "Erzincan": (39.7500, 39.5000),
    "Erzurum": (39.9043, 41.2679),
    "Eskişehir": (39.7767, 30.5206),
    "Gaziantep": (37.0662, 37.3833),
    "Giresun": (40.9128, 38.3895),
    "Gümüşhane": (40.4603, 39.4814),
    "Hakkâri": (37.5744, 43.7408),
    "Hatay": (36.2021, 36.1600),
    "Iğdır": (39.9204, 44.0436),
    "Isparta": (37.7648, 30.5566),
    "İstanbul": (41.0082, 28.9784),
    "İzmir": (38.4237, 27.1428),
    "Kahramanmaraş": (37.5753, 36.9228),
    "Karabük": (41.2061, 32.6204),
    "Karaman": (37.1811, 33.2150),
    "Kars": (40.6013, 43.0975),
    "Kastamonu": (41.3887, 33.7827),
    "Kayseri": (38.7225, 35.4875),
    "Kırıkkale": (39.8468, 33.5153),
    "Kırklareli": (41.7351, 27.2252),
    "Kırşehir": (39.1425, 34.1709),
    "Kilis": (36.7184, 37.1212),
    "Kocaeli": (40.7654, 29.9408),
    "Konya": (37.8746, 32.4932),
    "Kütahya": (39.4192, 29.9857),
    "Malatya": (38.3552, 38.3095),
    "Manisa": (38.6191, 27.4289),
    "Mardin": (37.3122, 40.7351),
    "Mersin": (36.8121, 34.6415),
    "Muğla": (37.2153, 28.3636),
    "Muş": (38.9462, 41.7539),
    "Nevşehir": (38.6247, 34.7140),
    "Niğde": (37.9698, 34.6766),
    "Ordu": (40.9862, 37.8797),
    "Osmaniye": (37.0742, 36.2478),
    "Rize": (41.0201, 40.5234),
    "Sakarya": (40.7569, 30.3781),
    "Samsun": (41.2867, 36.3300),
    "Siirt": (37.9333, 41.9500),
    "Sinop": (42.0264, 35.1551),
    "Sivas": (39.7477, 37.0179),
    "Şanlıurfa": (37.1674, 38.7955),
    "Şırnak": (37.5164, 42.4611),
    "Tekirdağ": (40.9781, 27.5117),
    "Tokat": (40.3139, 36.5544),
    "Trabzon": (41.0015, 39.7178),
    "Tunceli": (39.1081, 39.5471),
    "Uşak": (38.6823, 29.4082),
    "Van": (38.5012, 43.3720),
    "Yalova": (40.6550, 29.2769),
    "Yozgat": (39.8181, 34.8147),
    "Zonguldak": (41.4564, 31.7987)

}




def get_weather(city="Bursa"):

    if city not in CITIES:
        city = "Bursa"

    lat, lon = CITIES[city]

    url = (

        "https://api.open-meteo.com/v1/forecast"

        f"?latitude={lat}"

        f"&longitude={lon}"

        "&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"

    )

    r = requests.get(url, timeout=5)

    r.raise_for_status()

    current = r.json()["current"]

    return {

        "city": city,

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