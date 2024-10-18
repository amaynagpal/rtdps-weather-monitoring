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

5. Run the application:
   ```
   python app.py
   ```

6. Open your web browser and navigate to `http://127.0.0.1:5000`
   

## Usage

1. Enter a city name in the search bar and click "Get Weather"
2. View the current weather information and interactive charts
3. Explore historical data and weather trends for the selected city

## ScreenShots of Project
### Landing Page:
![image](https://github.com/user-attachments/assets/27c7039f-8145-478e-b252-5b8233f534b8)
### Weather Report:
![image](https://github.com/user-attachments/assets/d53a6ac0-b850-415c-91c6-182ee46e820f)
<br>
![image](https://github.com/user-attachments/assets/e6320e60-19e1-48ba-85e5-fefb6d5b07f4)

## Acknowledgements

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Chart.js](https://www.chartjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Flask](https://flask.palletsprojects.com/)
