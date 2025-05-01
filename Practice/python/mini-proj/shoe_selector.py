#!/usr/bin/env python3
"""
shoe_selector.py
"""

import requests
import argparse
import os
import sys

OWM_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(api_key, city):
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(OWM_URL, params=params)
    response.raise_for_status()
    data = response.json()
    weather_desc = data['weather'][0]['main']
    temperature = data['main']['temp']
    return temperature, weather_desc

def recommend_shoes(activity, style, temp, weather_desc):
    shoes = {
        'running': {
            'casual': 'Casual running sneakers',
            'formal': 'Performance running shoes'
        },
        'office': {
            'casual': 'Loafers or minimalist sneakers',
            'formal': 'Leather Oxfords or Derby shoes'
        },
        'party': {
            'casual': 'Stylish sneakers or Chelsea boots',
            'formal': 'Elegant dress shoes or heels'
        },
        'hiking': {
            'casual': 'Trail sneakers or lightweight hiking shoes',
            'formal': 'Durable waterproof hiking boots'
        },
        'beach': {
            'casual': 'Flip-flops or sandals',
            'formal': 'Stylish espadrilles'
        }
    }

    recommendation = shoes.get(activity.lower(), {}).get(style.lower(), "Casual sneakers")

    if 'Rain' in weather_desc or 'Snow' in weather_desc:
        recommendation += " (waterproof recommended)"

    if temp < 5:
        recommendation += " (insulated for cold weather)"
    elif temp > 25:
        recommendation += " (breathable and lightweight)"

    return recommendation

def main():
    parser = argparse.ArgumentParser(description="ShoeSelector - Personalized shoe recommendations.")
    parser.add_argument('--city', required=True, help="City name (e.g., 'Paris,FR')")
    parser.add_argument('--activity', required=True, help="Your planned activity (e.g., running, office, party, hiking, beach)")
    parser.add_argument('--style', required=True, choices=['casual', 'formal'], help="Preferred style (casual/formal)")
    args = parser.parse_args()

    api_key = os.getenv("OWM_API_KEY")
    if not api_key:
        print("Error: Please set OWM_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)

    try:
        temp, desc = get_weather(api_key, args.city)
        print(f"\n🌤️ Current weather in {args.city}: {temp:.1f}°C, {desc}\n")
        shoe = recommend_shoes(args.activity, args.style, temp, desc)

        print(f"👟 Recommended shoes for {args.activity.title()} ({args.style.title()} style):")
        print(f"  - {shoe}\n")

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
