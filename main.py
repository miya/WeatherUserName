import os
import requests
from twython import Twython

WEATHER_ICONS = {
    200: "⚡",
    201: "⚡",
    202: "⚡",
    210: "⚡",
    211: "⚡",
    212: "⚡",
    221: "⚡",
    230: "⚡",
    231: "⚡",
    232: "⚡",
    300: "🌧",
    301: "🌧",
    302: "🌧",
    310: "🌧",
    311: "🌧",
    312: "🌧",
    313: "🌧",
    314: "🌧",
    321: "🌧",
    500: "🌦",
    501: "🌦",
    502: "🌦",
    503: "🌦",
    504: "🌦",
    511: "❄️",
    520: "🌧",
    521: "🌧",
    522: "🌧",
    531: "🌧",
    600: "❄️",
    601: "❄️",
    602: "❄️",
    611: "❄️",
    612: "❄️",
    613: "❄️",
    615: "❄️",
    616: "❄️",
    620: "❄️",
    621: "❄️",
    622: "❄️",
    701: "🌫",
    711: "🌫",
    721: "🌫",
    731: "🌫",
    741: "🌫",
    751: "🌫",
    761: "🌫",
    771: "🌫",
    781: "🌫",
    800: "☀️",
    801: "🌤",
    802: "⛅️",
    803: "☁️",
    804: "☁️"

}

city_id = "1850147"
user_name = "miya"

open_weather_map_api_key = os.environ.get("open_weather_map_key")
open_weather_map_api = "http://api.openweathermap.org/data/2.5/weather"

twitter_consumer_key = os.environ.get("twitter_consumer_key")
twitter_consumer_secret = os.environ.get("twitter_consumer_secret")
twitter_access_key = os.environ.get("twitter_access_key")
twitter_access_secret = os.environ.get("twitter_access_secret")


def get_weather_icon():
    query = {
        "APPID": open_weather_map_api_key,
        "id": city_id,
        "mode": "json",
    }
    r = requests.get(open_weather_map_api, params=query)
    weather_id = r.json()["weather"][0]["id"]
    return WEATHER_ICONS[weather_id]


def change_twitter_profile():
    twitter = Twython(
        twitter_consumer_key,
        twitter_consumer_secret,
        twitter_access_key,
        twitter_access_secret
    )
    weather_user_name = f"{user_name} {get_weather_icon()}"
    twitter.update_profile(name=weather_user_name)


if __name__ == "__main__":
    change_twitter_profile()
