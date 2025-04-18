#!/usr/bin/env python3
"""
moon_phase_calendar.py
"""

import argparse
import datetime
import csv
import ephem
import matplotlib.pyplot as plt

def generate_moon_phases(year):
    """
    For each day of the specified year, compute the Moon's illumination percentage.
    Returns a list of (date, illumination).
    """
    phases = []
    date = datetime.date(year, 1, 1)
    end = datetime.date(year + 1, 1, 1)
    while date < end:
        # PyEphem uses UTC; pass date as a string
        moon = ephem.Moon(str(date))
        illumination = moon.phase  # percentage illuminated (0–100)
        phases.append((date.isoformat(), illumination))
        date += datetime.timedelta(days=1)
    return phases

def save_csv(phases, filename):
    """
    Save the phase data to a CSV file with headers: Date,Illumination
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Illumination'])
        writer.writerows(phases)
    print(f"Saved CSV: {filename}")

def plot_phases(phases, filename):
    """
    Plot illumination over time and save as PNG.
    """
    dates = [datetime.datetime.fromisoformat(d) for d, _ in phases]
    illum = [i for _, i in phases]

    plt.figure(figsize=(12, 4))
    plt.plot(dates, illum, '-', lw=1, color='navy')
    plt.fill_between(dates, illum, color='lightgray', alpha=0.5)
    plt.title(f"Daily Moon Illumination for {dates[0].year}")
    plt.xlabel("Date")
    plt.ylabel("Illumination (%)")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    print(f"Saved plot: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Moon Phase Calendar Generator")
    parser.add_argument('--year', type=int, default=datetime.date.today().year,
                        help="Year for which to generate the calendar (default: current year)")
    parser.add_argument('--output_csv', type=str, default="moon_phases.csv",
                        help="Output CSV filename")
    parser.add_argument('--output_png', type=str, default="moon_phases.png",
                        help="Output plot PNG filename")
    args = parser.parse_args()

    print(f"Generating Moon Phase Calendar for {args.year}...")
    phases = generate_moon_phases(args.year)
    save_csv(phases, args.output_csv)
    plot_phases(phases, args.output_png)

if __name__ == "__main__":
    main()
