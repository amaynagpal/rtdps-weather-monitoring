# Weather Monitor

Weather Monitor is a web application that provides real-time weather information and historical weather data visualization for cities worldwide. It features an intuitive interface with interactive charts displaying temperature trends and weather condition distributions.

## Features

- Real-time weather data retrieval for any city
- Display of current weather conditions including temperature, feels-like temperature, and weather description
- Interactive charts showing:
  - Last 7 days temperature trend
  - Daily temperature summary
  - Weather condition distribution
- Responsive design for both desktop and mobile devices

## Technologies Used

- Backend: Python with Flask
- Frontend: HTML, CSS (Tailwind CSS), JavaScript
- Data Visualization: Chart.js
- External API: OpenWeatherMap API

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/amaynagpal/rtdps-weather-monitoring.git
   ```
   OR
   you can also download the zip file and then open it in your vs code 

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenWeatherMap API key:
   - Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/)
   - Get your API key from your account dashboard
   - Create a `.env` file in the project root and add your API key:
     ```
     OPENWEATHERMAP_API_KEY=your_api_key_here
     ```

5. Initialize the database:
   ```
   python init_db.py
   ```

6. Run the application:
   ```
   python app.py
   ```

7. Open your web browser and navigate to `http://127.0.0.1:5000`
   

## Usage

1. Enter a city name in the search bar and click "Get Weather"
2. View the current weather information and interactive charts
3. Explore historical data and weather trends for the selected city

## ScreenShots of Project
### Landing Page:
<img width="960" alt="image" src="https://github.com/user-attachments/assets/e19f7c5a-e1ab-4e8d-93c6-ce3bc308edc4">

### Weather Report:
<img width="960" alt="image" src="https://github.com/user-attachments/assets/695152e9-aaed-4962-90a4-b91aa65c6ab4">
<img width="960" alt="image" src="https://github.com/user-attachments/assets/fe42767e-c2e4-4301-91a9-5e681d8ef724">
<img width="960" alt="image" src="https://github.com/user-attachments/assets/d806d489-6fdd-42e4-8ce8-5a44ffd2b358">

## Acknowledgements

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Chart.js](https://www.chartjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Flask](https://flask.palletsprojects.com/)
