#!/usr/bin/env python3
"""
tomorrow_weather_notifier.py
Fetch tomorrow's weather forecast for a specified city and email you a summary.
"""

import os
import sys
import argparse
import requests
import datetime
import smtplib
from email.message import EmailMessage

API_URL = "https://api.openweathermap.org/data/2.5/forecast"

def fetch_tomorrow_forecast(api_key, city):
    """Fetch 5-day forecast and pick the forecast closest to 12:00 tomorrow."""
    params = {"q": city, "appid": api_key, "units": "metric"}
    resp = requests.get(API_URL, params=params)
    resp.raise_for_status()
    data = resp.json()
    tomorrow = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).date()
    # find entry closest to 12:00
    best = None
    best_diff = datetime.timedelta(days=99)
    for entry in data.get("list", []):
        dt = datetime.datetime.utcfromtimestamp(entry["dt"])
        if dt.date() == tomorrow:
            diff = abs(dt - datetime.datetime.combine(tomorrow, datetime.time(12,0)))
            if diff < best_diff:
                best_diff, best = diff, entry
    if not best:
        raise ValueError("Could not find tomorrow's forecast.")
    # build summary
    weather = best["weather"][0]["description"].title()
    temp = best["main"]["temp"]
    feels = best["main"]["feels_like"]
    humidity = best["main"]["humidity"]
    dt_local = dt + datetime.timedelta(seconds=data["city"]["timezone"])
    return dt_local.strftime("%Y-%m-%d %H:%M"), weather, temp, feels, humidity

def send_email(smtp_server, smtp_port, user, password, to_addr, subject, body):
    """Send an email via SMTP."""
    msg = EmailMessage()
    msg["From"] = user
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port) as s:
        s.starttls()
        s.login(user, password)
        s.send_message(msg)

def main():
    parser = argparse.ArgumentParser(description="Tomorrow's Weather Notifier")
    parser.add_argument("--city", required=True, help="City name, e.g. 'London,UK'")
    parser.add_argument("--to", required=True, help="Recipient email address")
    args = parser.parse_args()

    # Load config from env
    api_key     = os.getenv("OWM_API_KEY")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port   = int(os.getenv("SMTP_PORT", "587"))
    email_user  = os.getenv("EMAIL_USER")
    email_pass  = os.getenv("EMAIL_PASS")

    if not all([api_key, smtp_server, email_user, email_pass]):
        print("Error: Please set OWM_API_KEY, SMTP_SERVER, EMAIL_USER, and EMAIL_PASS", file=sys.stderr)
        sys.exit(1)

    try:
        dt, weather, temp, feels, humidity = fetch_tomorrow_forecast(api_key, args.city)
    except Exception as e:
        print(f"Failed to fetch forecast: {e}", file=sys.stderr)
        sys.exit(1)

    subject = f"Tomorrow's Weather in {args.city.split(',')[0]}: {weather}, {temp:.1f}°C"
    body = (
        f"Forecast for {args.city} at {dt} (local time):\n"
        f"  Condition : {weather}\n"
        f"  Temperature: {temp:.1f} °C (feels like {feels:.1f} °C)\n"
        f"  Humidity   : {humidity}%\n\n"
        "Stay prepared!"
    )

    try:
        send_email(smtp_server, smtp_port, email_user, email_pass, args.to, subject, body)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
