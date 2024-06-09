import os
from datetime import datetime

import requests
from langchain_core.tools import tool


@tool
def get_weather(city: str, date=datetime.now()) -> dict:
    """return the weather details of a city at a time"""
    api = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        weather = {
            "city": data["name"],
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }

        return weather
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
