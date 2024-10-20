import requests
from collections import defaultdict
import datetime

weather_data = defaultdict(list)

def fetch_weather(city, api_key):
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    response = requests.get(BASE_URL, params={'q': city, 'appid': api_key, 'units': 'metric'})
    return response.json() if response.status_code == 200 else None

def log_weather(city, temperature):
    today = datetime.date.today()
    weather_data[today].append((city, temperature))

def generate_summary():
    today = datetime.date.today()
    if today in weather_data:
        avg_temp = sum(temp for _, temp in weather_data[today]) / len(weather_data[today])
        max_temp = max(temp for _, temp in weather_data[today])
        min_temp = min(temp for _, temp in weather_data[today])
        print(f"Summary for {today}: Avg Temp: {avg_temp:.2f}°C, Max Temp: {max_temp:.2f}°C, Min Temp: {min_temp:.2f}°C")
