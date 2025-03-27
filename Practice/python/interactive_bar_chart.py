import matplotlib.pyplot as plt
import numpy as np

def interactive_bar_chart(categories, values, title="Bar Chart", xlabel="Categories", ylabel="Values", color='skyblue'):
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=color, edgecolor='black')

    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Interactive labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval,2), ha='center', fontsize=12)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    categories = ['Python', 'JavaScript', 'C++', 'Java', 'Rust']
    values = np.random.randint(10, 100, len(categories))

    interactive_bar_chart(categories, values, title="Programming Languages Popularity", xlabel="Languages", ylabel="Popularity (%)")
