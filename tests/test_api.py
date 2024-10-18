import unittest
from src.api.openweathermap import OpenWeatherMapAPI

class TestOpenWeatherMapAPI(unittest.TestCase):
    def setUp(self):
        self.api = OpenWeatherMapAPI()

    def test_get_weather_data(self):
        data = self.api.get_weather_data('London')
        self.assertIsNotNone(data)
        self.assertIn('main', data)
        self.assertIn('temp', data['main'])

if __name__ == '__main__':
    unittest.main()