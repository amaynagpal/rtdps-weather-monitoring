import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
    API_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
    UPDATE_INTERVAL = 300  # 5 minutes in seconds
    CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    DATABASE_PATH = 'data/weather_data.db'
    TEMPERATURE_UNIT = 'celsius'  # or 'fahrenheit'
    ALERT_THRESHOLD = 35  # in Celsius
    CONSECUTIVE_ALERTS = 2