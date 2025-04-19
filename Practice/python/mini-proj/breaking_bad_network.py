#!/usr/bin/env python3
"""
breaking_bad_network.py

Builds and analyzes a character co‑occurrence network for Breaking Bad.

- Fetches episodes from the Breaking Bad API.
- Builds a graph where nodes are characters and edges are weighted by shared episodes.
- Computes and prints top characters by centrality and weighted degree.
- Visualizes the network (node size ~ centrality, edge width ~ co‑occurrence count).

Dependencies:
    pip install requests networkx matplotlib
"""

import requests
import networkx as nx
import matplotlib.pyplot as plt
import sys

API_URL = "https://breakingbadapi.com/api/episodes?series=Breaking+Bad"

def fetch_episodes():
    """Fetch all Breaking Bad episodes from the API."""
    resp = requests.get(API_URL)
    resp.raise_for_status()
    return resp.json()

def build_network(episodes):
    """
    Build a co‑occurrence network:
      - Node for each character
      - Edge weight = number of episodes both appear in
    """
    G = nx.Graph()
    for ep in episodes:
        chars = ep.get("characters", [])
        # ensure nodes
        for c in chars:
            G.add_node(c)
        # add/weight edges
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                a, b = chars[i], chars[j]
                if G.has_edge(a, b):
                    G[a][b]['weight'] += 1
                else:
                    G.add_edge(a, b, weight=1)
    return G

def analyze_and_print(G):
    """Compute and print top characters by degree centrality and weighted degree."""
    centrality = nx.degree_centrality(G)
    top_cent = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Top 10 by degree centrality:")
    for name, cent in top_cent:
        print(f"  {name}: {cent:.3f}")

    wdeg = sorted(G.degree(weight='weight'), key=lambda x: x[1], reverse=True)[:10]
    print("\nTop 10 by weighted degree (shared episodes):")
    for name, deg in wdeg:
        print(f"  {name}: {deg}")

    return centrality

def visualize(G, centrality):
    """Visualize the network: node size ∝ centrality, edge width ∝ weight."""
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, k=0.25, iterations=50)

    # Node sizes
    node_sizes = [3000 * centrality[n] for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos,
                           node_size=node_sizes,
                           node_color='gold',
                           alpha=0.8)

    # Edge widths
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]
    widths = [w * 0.1 for w in weights]
    nx.draw_networkx_edges(G, pos,
                           edgelist=edges,
                           width=widths,
                           alpha=0.5,
                           edge_color='gray')

    # Label only the top central characters
    top_nodes = {n for n, _ in sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]}
    labels = {n: n for n in top_nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=9)

    plt.title("Breaking Bad Character Co‑occurrence Network")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    print("Fetching Breaking Bad episodes…")
    episodes = fetch_episodes()
    print(f"Retrieved {len(episodes)} episodes. Building network…")
    G = build_network(episodes)
    centrality = analyze_and_print(G)
    visualize(G, centrality)

if __name__ == "__main__":
    try:
        main()
    except requests.RequestException as e:
        print("Error fetching data:", e, file=sys.stderr)
        sys.exit(1)
