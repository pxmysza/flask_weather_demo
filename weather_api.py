from dotenv import load_dotenv
import os
import requests

load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1"
API_KEY = os.getenv("WEATHER_API_KEY")

class ConnectionMixin:

    @staticmethod
    def get_weather_details(city: str) -> dict:
        r = requests.get(f"{BASE_URL}/forecast.json?key={API_KEY}&q={city}&days=1&aqi=no&alerts=no").json()
        return {
            "city": city,
            "temperature": r["current"]["temp_c"],
            "humidity": r["current"]["humidity"],
            "overcast": r["current"]["cloud"],
            "wind_speed": r["current"]["wind_kph"],
            "air_pressure": r["current"]["pressure_mb"],
            "chance_of_rain": r["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"],
            "chance_of_snow": r["forecast"]["forecastday"][0]["day"]["daily_chance_of_snow"]
        }
