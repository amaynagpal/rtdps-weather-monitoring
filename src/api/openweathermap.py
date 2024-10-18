import requests
from config.config import Config

class OpenWeatherMapAPI:
    def __init__(self):
        self.api_key = Config.API_KEY
        self.base_url = Config.API_BASE_URL

    def get_weather_data(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric' if Config.TEMPERATURE_UNIT == 'celsius' else 'imperial'
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data for {city}: {response.status_code}")
            return None