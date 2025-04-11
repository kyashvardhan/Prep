#!/usr/bin/env python3
"""
csk_player_stats.py
--by yvk

CSK Player Stats Analysis (2020-2025)

This script analyzes sample performance data for Chennai Super Kings (CSK) players
covering the seasons from 2020 to 2025. It calculates yearly totals for matches,
runs, and wickets, identifies the top run-scorer each year, and visualizes performance
trends using line and bar charts.

Usage:
    python csk_player_stats.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_sample_data():
    """
    Create sample CSK player statistics data for seasons 2020-2025.
    Data includes details such as:
        - Year
        - Player
        - Matches played
        - Total runs scored
        - Total wickets taken
        - Role (Batsman, Bowler, All-rounder, or Wicketkeeper)
    """
    data = [
        # Year 2020
        {'Year': 2020, 'Player': 'MS Dhoni',            'Matches': 14, 'Runs': 210, 'Wickets': 0,  'Role': 'Wicketkeeper'},
        {'Year': 2020, 'Player': 'Ruturaj Gaikwad',       'Matches': 14, 'Runs': 620, 'Wickets': 0,  'Role': 'Batsman'},
        {'Year': 2020, 'Player': 'Ravindra Jadeja',       'Matches': 14, 'Runs': 280, 'Wickets': 12, 'Role': 'All-rounder'},
        {'Year': 2020, 'Player': 'Deepak Chahar',         'Matches': 14, 'Runs': 100, 'Wickets': 16, 'Role': 'Bowler'},
        # Year 2021
        {'Year': 2021, 'Player': 'MS Dhoni',            'Matches': 12, 'Runs': 190, 'Wickets': 0,  'Role': 'Wicketkeeper'},
        {'Year': 2021, 'Player': 'Ruturaj Gaikwad',       'Matches': 12, 'Runs': 700, 'Wickets': 0,  'Role': 'Batsman'},
        {'Year': 2021, 'Player': 'Ravindra Jadeja',       'Matches': 12, 'Runs': 310, 'Wickets': 14, 'Role': 'All-rounder'},
        {'Year': 2021, 'Player': 'Deepak Chahar',         'Matches': 12, 'Runs': 120, 'Wickets': 18, 'Role': 'Bowler'},
        # Year 2022
        {'Year': 2022, 'Player': 'MS Dhoni',            'Matches': 15, 'Runs': 230, 'Wickets': 0,  'Role': 'Wicketkeeper'},
        {'Year': 2022, 'Player': 'Ruturaj Gaikwad',       'Matches': 15, 'Runs': 750, 'Wickets': 0,  'Role': 'Batsman'},
        {'Year': 2022, 'Player': 'Ravindra Jadeja',       'Matches': 15, 'Runs': 330, 'Wickets': 15, 'Role': 'All-rounder'},
        {'Year': 2022, 'Player': 'Deepak Chahar',         'Matches': 15, 'Runs': 130, 'Wickets': 20, 'Role': 'Bowler'},
        # Year 2023
        {'Year': 2023, 'Player': 'MS Dhoni',            'Matches': 16, 'Runs': 240, 'Wickets': 0,  'Role': 'Wicketkeeper'},
        {'Year': 2023, 'Player': 'Ruturaj Gaikwad',       'Matches': 16, 'Runs': 800, 'Wickets': 0,  'Role': 'Batsman'},
        {'Year': 2023, 'Player': 'Ravindra Jadeja',       'Matches': 16, 'Runs': 350, 'Wickets': 16, 'Role': 'All-rounder'},
        {'Year': 2023, 'Player': 'Deepak Chahar',         'Matches': 16, 'Runs': 140, 'Wickets': 22, 'Role': 'Bowler'},
        # Year 2024
        {'Year': 2024, 'Player': 'MS Dhoni',            'Matches': 15, 'Runs': 250, 'Wickets': 0,  'Role': 'Wicketkeeper'},
        {'Year': 2024, 'Player': 'Ruturaj Gaikwad',       'Matches': 15, 'Runs': 820, 'Wickets': 0,  'Role': 'Batsman'},
        {'Year': 2024, 'Player': 'Ravindra Jadeja',       'Matches': 15, 'Runs': 360, 'Wickets': 17, 'Role': 'All-rounder'},
        {'Year': 2024, 'Player': 'Deepak Chahar',         'Matches': 15, 'Runs': 150, 'Wickets': 24, 'Role': 'Bowler'},
        # Year 2025
        {'Year': 2025, 'Player': 'MS Dhoni',            'Matches': 14, 'Runs': 260, 'Wickets': 0,  'Role': 'Wicketkeeper'},
        {'Year': 2025, 'Player': 'Ruturaj Gaikwad',       'Matches': 14, 'Runs': 850, 'Wickets': 0,  'Role': 'Batsman'},
        {'Year': 2025, 'Player': 'Ravindra Jadeja',       'Matches': 14, 'Runs': 370, 'Wickets': 18, 'Role': 'All-rounder'},
        {'Year': 2025, 'Player': 'Deepak Chahar',         'Matches': 14, 'Runs': 160, 'Wickets': 26, 'Role': 'Bowler'},
    ]
    return pd.DataFrame(data)

def analyze_stats(df):
    """
    Analyze the CSK stats data:
        - Calculate total matches, runs, and wickets for each year.
        - Identify the top run-scorer for each year.
    """
    # Calculate overall totals per year
    yearly_stats = df.groupby('Year').agg({
        'Matches': 'sum',
        'Runs': 'sum',
        'Wickets': 'sum'
    }).reset_index()
    
    # Identify the top run-scorer in each year
    top_run_scorers = df.loc[df.groupby('Year')['Runs'].idxmax()][['Year', 'Player', 'Runs']]
    
    print("Yearly CSK Stats (2020-2025):")
    print(yearly_stats)
    print("\nTop Run-Scorer Each Year:")
    print(top_run_scorers)
    
    return yearly_stats, top_run_scorers

def plot_stats(yearly_stats):
    """
    Generate and display the following visualizations:
        - A line plot for total runs per year.
        - A bar chart for total wickets per year.
    """
    # Set the Seaborn style for better aesthetics.
    sns.set(style="whitegrid")

    # Plot total runs per year
    plt.figure(figsize=(10, 5))
    plt.plot(yearly_stats['Year'], yearly_stats['Runs'], marker='o', linestyle='-', color='blue', label='Total Runs')
    plt.title('Total Runs by CSK (2020-2025)')
    plt.xlabel('Year')
    plt.ylabel('Total Runs')
    plt.legend()
    plt.savefig('csk_total_runs.png')
    plt.show()

    # Plot total wickets per year
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Year', y='Wickets', data=yearly_stats, palette='Greens_d')
    plt.title('Total Wickets by CSK (2020-2025)')
    plt.xlabel('Year')
    plt.ylabel('Total Wickets')
    plt.savefig('csk_total_wickets.png')
    plt.show()

def main():
    df = create_sample_data()
    print("CSK Player Stats (2020-2025):")
    print(df)
    yearly_stats, top_run_scorers = analyze_stats(df)
    plot_stats(yearly_stats)
    
if __name__ == "__main__":
    main()
