function getWeather() {
    const city = document.getElementById('cityInput').value;
    fetch('/get_weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ city: city }),
    })
    .then(response => response.json())
    .then(data => {
        displayWeather(data);
        getSummary(city);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function displayWeather(data) {
    const weatherResult = document.getElementById('weatherResult');
    weatherResult.innerHTML = `
        <div class="flex">
            <img src="http://openweathermap.org/img/w/${data.weather[0].icon}.png" alt="Weather icon" class="weather-icon">
            <div>
                <div class="temperature">${data.main.temp}°C</div>
                <div class="description">${data.weather[0].description}</div>
            </div>
        </div>
        <div>Feels like: ${data.main.feels_like}°C</div>
        <div>Humidity: ${data.main.humidity}%</div>
        <div>Wind: ${data.wind.speed} m/s</div>
    `;
}

function getSummary(city) {
    fetch('/get_summary', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ city: city }),
    })
    .then(response => response.json())
    .then(data => {
        displaySummary(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function displaySummary(data) {
    const weatherSummary = document.getElementById('weatherSummary');
    weatherSummary.innerHTML = `
        <div class="summary-title">Daily Summary:</div>
        <div class="summary-content">
            <div>Average Temperature: ${data.daily_summary.avg_temp.toFixed(2)}°C</div>
            <div>Max Temperature: ${data.daily_summary.max_temp.toFixed(2)}°C</div>
            <div>Min Temperature: ${data.daily_summary.min_temp.toFixed(2)}°C</div>
            <div>Dominant Weather: ${data.daily_summary.dominant_weather}</div>
        </div>
        <div class="summary-title">Weather Distribution:</div>
        <div class="summary-content">
            ${Object.entries(data.weather_distribution).map(([condition, count]) => 
                `<div>${condition}: ${count}</div>`
            ).join('')}
        </div>
    `;
}