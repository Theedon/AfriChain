import os
from datetime import datetime

import requests
from langchain_core.tools import tool


@tool
def get_weather(city: str, date=datetime.now()) -> dict:
    """
    Retrieves the current weather information for a given city.

    Args:
        city (str): The name of the city to retrieve the weather for.
        date (datetime, optional): The date to retrieve the weather for. Defaults to the current date.

    Returns:
        dict: A dictionary containing the following weather information:
            - city (str): The name of the city.
            - description (str): A description of the current weather.
            - temperature (float): The current temperature in Kelvin.
            - humidity (int): The current humidity percentage.
            - wind_speed (float): The current wind speed in meters per second.

    Raises:
        requests.exceptions.RequestException: If there is an error making the API request.
    """
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
