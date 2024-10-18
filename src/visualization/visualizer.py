from src.storage.database import Database
from datetime import datetime, timedelta
from collections import Counter

class Visualizer:
    def __init__(self):
        self.db = Database()

    def get_chart_data(self, city):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        data = self.db.get_data_range(city, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        
        dates = [datetime.fromisoformat(row['dt']).strftime('%Y-%m-%d') for row in data]
        temperatures = [row['temp'] for row in data]
        
        return {
            'dates': dates,
            'temperatures': temperatures
        }

    def get_daily_summary(self, city, start_date, end_date):
        data = self.db.get_data_range(city, start_date, end_date)
        daily_data = {}
        for row in data:
            date = datetime.fromisoformat(row['dt']).strftime('%Y-%m-%d')
            if date not in daily_data:
                daily_data[date] = []
            daily_data[date].append(row['temp'])
        
        dates = sorted(daily_data.keys())
        temps = [sum(daily_data[date]) / len(daily_data[date]) for date in dates]

        return {
            'dates': dates,
            'temperatures': temps
        }

    def get_weather_distribution(self, city, start_date, end_date):
        data = self.db.get_data_range(city, start_date, end_date)
        weather_conditions = [row['main'] for row in data]
        condition_counts = dict(Counter(weather_conditions))

        return {
            'labels': list(condition_counts.keys()),
            'data': list(condition_counts.values())
        }