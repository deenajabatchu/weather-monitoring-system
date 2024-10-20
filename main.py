import time
from data_processing import fetch_weather, log_weather, generate_summary
from alerts import check_alerts

API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def monitor_weather():
    while True:
        for city in CITIES:
            data = fetch_weather(city, API_KEY)
            if data:
                temperature = data['main']['temp']
                log_weather(city, temperature)
                check_alerts(temperature)  # Check for any alerts based on the temperature
                print(f"Weather in {city}: {temperature}°C, {data['weather'][0]['description']}")
        generate_summary()  # Generate daily summary
        time.sleep(300)  # Fetch every 5 minutes

if __name__ == '__main__':
    monitor_weather()