import os
import tweepy
import requests

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


class WeatherUserName:

    def __init__(self, user_name, city_id):
        self.OPEN_WEATHER_MAP_API = "http://api.openweathermap.org/data/2.5/weather"
        self.TWITTER_USER_NAME = user_name
        self.CITY_ID = city_id
        self.OPEN_WEATHER_MAP_API_KEY = os.environ.get("OPEN_WEATHER_MAP_API_KEY")
        self.TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
        self.TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
        self.TWITTER_ACCESS_KEY = os.environ.get("TWITTER_ACCESS_KEY")
        self.TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")
        self.change_twitter_profile()

    def get_weather_icon(self):
        query = {
            "APPID": self.OPEN_WEATHER_MAP_API_KEY,
            "id": self.CITY_ID,
            "mode": "json",
        }
        r = requests.get(self.OPEN_WEATHER_MAP_API, params=query)
        weather_id = r.json()["weather"][0]["id"]
        return WEATHER_ICONS[weather_id]

    def change_twitter_profile(self):
        weather_icon = self.get_weather_icon()
        user_name = "{} {}".format(self.TWITTER_USER_NAME, weather_icon)
        auth = tweepy.OAuthHandler(self.TWITTER_CONSUMER_KEY, self.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(self.TWITTER_ACCESS_KEY, self.TWITTER_ACCESS_SECRET)
        api = tweepy.API(auth)
        api.update_profile(name=user_name)


if __name__ == "__main__":
    WeatherUserName(user_name="miya", city_id=1850147)

