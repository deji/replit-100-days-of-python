import requests, json
from urllib.parse import quote

from typing import Union, List


def translate_wmo_code(code: Union[str, List[int]]):
    wmo_codes_text = {
        "0": "Sunny/Clear",
        "1": "Mainly Sunny/Clear",
        "2": "Partly Cloudy",
        "3": "Cloudy",
        "45": "Foggy",
        "48": "Rime Fog",
        "51": "Light Drizzle",
        "53": "Drizzle",
        "55": "Heavy Drizzle",
        "56": "Light Freezing Drizzle",
        "57": "Freezing Drizzle",
        "61": "Light Rain",
        "63": "Rain",
        "65": "Heavy Rain",
        "66": "Light Freezing Rain",
        "67": "Freezing Rain",
        "71": "Light Snow",
        "73": "Snow",
        "75": "Heavy Snow",
        "77": "Snow Grains",
        "80": "Light Showers",
        "81": "Showers",
        "82": "Heavy Showers",
        "85": "Light Snow Showers",
        "86": "Snow Showers",
        "95": "Thunderstorm",
        "96": "Light Thunderstorms With Hail",
        "99": "Thunderstorm With Hail"
    }
    if isinstance(code, list):
        words = [wmo_codes_text.get(str(i), "Unknown") for i in code]
        if len(words) == 1:
            return words[0]
        elif len(words) == 2:
            return f"{words[0]} and {words[1]}".capitalize()
        else:
            return f"{', '.join(words[:-1])}, and {words[-1]}".capitalize()

    return wmo_codes_text.get(str(code), "Unknown")


timezone = "GMT+1"
location = "NG34 8FZ, UK"

result = requests.get(
    f"https://nominatim.openstreetmap.org/search?q={location}&format=json&limit=1",
    headers={"User-Agent": "My test app"})

if result.status_code != 200:
    print("Error when calling Nominatim")
    print(result.status_code, result.text)
    exit()

geolocation = result.json()
# print("=====geocoding api:\n", json.dumps(geolocation, indent=2))
latitude = geolocation[0]["lat"]
longitude = geolocation[0]["lon"]

result = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={quote(timezone.upper())}"
)
user = result.json()
# print("=====weather api:\n", json.dumps(user, indent=2))

print(f"""The weather over the next week in {geolocation[0]["display_name"]}
will be {translate_wmo_code(list(set(user["daily"]["weathercode"])))}
with a high of {max(user["daily"]["temperature_2m_max"])} and a low of {min(user["daily"]["temperature_2m_min"])} ℃
""")
