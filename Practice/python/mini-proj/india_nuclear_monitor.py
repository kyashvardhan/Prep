#!/usr/bin/env python3
"""
india_nuclear_monitor.py
"""

import matplotlib.pyplot as plt

def get_nuclear_data():
    """
    Nuclear arsenal data as per the latest publicly available report from Federation of American Scientists (FAS), 2025.
    Source: https://fas.org/issues/nuclear-weapons/status-world-nuclear-forces/
    """
    return {
        'Russia': 5449,
        'United States': 5244,
        'China': 410,
        'France': 290,
        'United Kingdom': 225,
        'Pakistan': 170,
        'India': 164,
        'Israel': 90,
        'North Korea': 40
    }

def display_stats(data):
    india_count = data.get('India', 0)
    print(f"\n🇮🇳 India's Current Nuclear Arsenal (2025): {india_count} warheads\n")

    print("🌐 Global Comparison:")
    for country, count in sorted(data.items(), key=lambda x: x[1], reverse=True):
        marker = " (India)" if country == "India" else ""
        print(f"  - {country}: {count} warheads{marker}")

def plot_nuclear_comparison(data):
    countries = list(data.keys())
    arsenals = list(data.values())
    colors = ['#2c3e50' if country != 'India' else '#f39c12' for country in countries]

    plt.figure(figsize=(10, 6))
    bars = plt.barh(countries, arsenals, color=colors)
    plt.xlabel('Number of Nuclear Warheads')
    plt.title("Nuclear Arsenal Comparison (2025)")

    # Annotate bars
    for bar in bars:
        plt.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2,
                 f'{int(bar.get_width())}', va='center', fontsize=9)

    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    data = get_nuclear_data()
    display_stats(data)
    plot_nuclear_comparison(data)

if __name__ == "__main__":
    main()
