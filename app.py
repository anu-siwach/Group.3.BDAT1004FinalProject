from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_weather_data(latitude, longitude):
    api_key = "04f2d2e4949cb5fa07abad0c1dbdb0f7"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetchweather')
def fetch_weather():
    latitude = 44.3894  # Latitude for Barrie
    longitude = -79.6903  # Longitude for Barrie
    weather_data = fetch_weather_data(latitude, longitude)

    if weather_data:
        weather_info = {
            'location': weather_data['name'] + ', ' + weather_data['sys']['country'],
            'temperature': str(weather_data['main']['temp']) + '°C',
            'feels_like': str(weather_data['main']['feels_like']) + '°C',
            'condition': weather_data['weather'][0]['description'],
            'wind_speed': str(weather_data['wind']['speed']) + 'm/s ' + str(weather_data['wind']['deg']) + '°',
            'pressure': str(weather_data['main']['pressure']) + 'hPa',
            'humidity': str(weather_data['main']['humidity']) + '%',
            'dew_point': str(weather_data['main'].get('dew_point', 'N/A')) + '°C',
            'visibility': str(weather_data.get('visibility', 'N/A')) + 'm'
        }
        return render_template('fetch-weather.html', weather_info=weather_info)
    else:
        return render_template('fetch-weather.html', weather_info=None)

@app.route('/linechart')
def line_chart():
    return render_template('visuals.html', latitude=44.3894, longitude=-79.6903, api_key="04f2d2e4949cb5fa07abad0c1dbdb0f7")


if __name__ == '__main__':
    app.run(debug=True)
 
