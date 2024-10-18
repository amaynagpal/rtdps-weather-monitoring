from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from src.api.openweathermap import OpenWeatherMapAPI
from src.processing.data_processor import DataProcessor
from src.visualization.visualizer import Visualizer
from config.config import Config

app = Flask(__name__)

api = OpenWeatherMapAPI()
processor = DataProcessor()
visualizer = Visualizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    data = api.get_weather_data(city)
    
    if data:
        processed_data = processor.process_weather_data(city, data)
        summary = processor.get_daily_summary(city, processed_data['dt'].strftime('%Y-%m-%d'))
        
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        
        daily_summary = visualizer.get_daily_summary(city, start_date, end_date)
        weather_distribution = visualizer.get_weather_distribution(city, start_date, end_date)
        
        # Ensure summary includes all required fields
        if summary:
            summary['avg_temp'] = summary.get('avg_temp', processed_data['temp'])
            summary['max_temp'] = summary.get('max_temp', processed_data['temp'])
            summary['min_temp'] = summary.get('min_temp', processed_data['temp'])
        else:
            summary = {
                'avg_temp': processed_data['temp'],
                'max_temp': processed_data['temp'],
                'min_temp': processed_data['temp']
            }
        
        return jsonify({
            'current': processed_data,
            'summary': summary,
            'chart_data': visualizer.get_chart_data(city),
            'daily_summary': daily_summary,
            'weather_distribution': weather_distribution
        })
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)