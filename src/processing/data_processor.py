from datetime import datetime
from src.storage.database import Database
from src.processing.alerts import AlertSystem

class DataProcessor:
    def __init__(self):
        self.db = Database()
        self.alert_system = AlertSystem()

    def process_weather_data(self, city, data):
        processed_data = {
            'city': city,
            'main': data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'dt': datetime.fromtimestamp(data['dt'])
        }
        self.db.insert_weather_data(processed_data)
        self.alert_system.check_alert(processed_data)
        return processed_data

    def get_daily_summary(self, city, date):
        data = self.db.get_daily_data(city, date)
        if not data:
            return None

        temps = [record['temp'] for record in data]
        weather_conditions = [record['main'] for record in data]

        summary = {
            'city': city,
            'date': date,
            'avg_temp': sum(temps) / len(temps),
            'max_temp': max(temps),
            'min_temp': min(temps),
            'dominant_weather': max(set(weather_conditions), key=weather_conditions.count)
        }
        return summary