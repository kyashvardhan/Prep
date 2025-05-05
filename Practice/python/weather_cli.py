#!/usr/bin/env python3
"""
weather_cli.py
"""

import requests
import argparse
import os
import sys
from datetime import datetime

API_CURRENT = "https://api.openweathermap.org/data/2.5/weather"
API_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"

def fetch_current_weather(api_key, city):
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    res = requests.get(API_CURRENT, params=params)
    res.raise_for_status()
    return res.json()

def fetch_forecast(api_key, city):
    params = {'q': city, 'appid': api_key, 'units': 'metric', 'cnt': 8}  # 24 hours forecast
    res = requests.get(API_FORECAST, params=params)
    res.raise_for_status()
    return res.json()

def weather_advice(temp, condition):
    advice = []
    if "rain" in condition.lower():
        advice.append("Carry an umbrella 🌧️.")
    if temp < 10:
        advice.append("Wear a warm jacket 🧥.")
    elif 10 <= temp <= 20:
        advice.append("Consider a light sweater 🧣.")
    elif temp > 30:
        advice.append("Stay hydrated and wear sunscreen 🧴.")
    else:
        advice.append("Enjoy your day! 😎")

    return ' '.join(advice)

def display_weather(current, forecast):
    city = current['name']
    country = current['sys']['country']
    temp = current['main']['temp']
    condition = current['weather'][0]['description'].title()
    feels_like = current['main']['feels_like']
    humidity = current['main']['humidity']
    wind_speed = current['wind']['speed']

    print(f"\n🌤️ Weather in {city}, {country} on {datetime.now().strftime('%Y-%m-%d %H:%M')}:")
    print(f"  - Temperature: {temp:.1f}°C (Feels like {feels_like:.1f}°C)")
    print(f"  - Condition  : {condition}")
    print(f"  - Humidity   : {humidity}%")
    print(f"  - Wind Speed : {wind_speed} m/s")
    print(f"\n💡 Advice: {weather_advice(temp, condition)}")

    print("\n📅 24-hour Forecast:")
    for entry in forecast['list']:
        time = datetime.fromtimestamp(entry['dt']).strftime('%b %d %H:%M')
        temp_forecast = entry['main']['temp']
        desc_forecast = entry['weather'][0]['description'].title()
        print(f"  - {time} | {temp_forecast:.1f}°C | {desc_forecast}")

def main():
    parser = argparse.ArgumentParser(description="WeatherCLI - Simple Weather Reports")
    parser.add_argument('--city', required=True, help="City (e.g., 'Berlin,DE')")
    args = parser.parse_args()

    api_key = os.getenv("OWM_API_KEY")
    if not api_key:
        print("Error: Set OWM_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)

    try:
        current = fetch_current_weather(api_key, args.city)
        forecast = fetch_forecast(api_key, args.city)
        display_weather(current, forecast)
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
