#!/usr/bin/env python3
"""
breaking_bad_sentiment_network.py
"""

import requests
import networkx as nx
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

EPISODES_API = "https://breakingbadapi.com/api/episodes?series=Breaking+Bad"
QUOTES_API   = "https://breakingbadapi.com/api/quotes"

def fetch_json(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def build_cooccurrence_graph(episodes):
    G = nx.Graph()
    for ep in episodes:
        chars = ep.get("characters", [])
        for c in chars:
            G.add_node(c)
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                a, b = chars[i], chars[j]
                if G.has_edge(a, b):
                    G[a][b]['weight'] += 1
                else:
                    G.add_edge(a, b, weight=1)
    return G

def compute_sentiment(quotes):
    analyzer = SentimentIntensityAnalyzer()
    scores = {}
    counts = {}
    for q in quotes:
        author = q.get("author","").strip()
        text   = q.get("quote","").strip()
        if author and text:
            comp = analyzer.polarity_scores(text)["compound"]
            scores[author] = scores.get(author, 0.0) + comp
            counts[author] = counts.get(author, 0) + 1
    # average
    return {author: scores[author]/counts[author] for author in scores}

def visualize(G, sentiment):
    centrality = nx.degree_centrality(G)
    pos = nx.spring_layout(G, k=0.3, iterations=50)
    
    # Node sizes and colors
    node_sizes  = [3000 * centrality.get(n,0) for n in G.nodes()]
    node_colors = []
    for n in G.nodes():
        s = sentiment.get(n, 0.0)
        # map sentiment [-1,1] to [0,1] for colormap
        node_colors.append((1 - s)/2)  # red=neg, green=pos
    
    # Edges
    edges  = G.edges()
    widths = [G[u][v]['weight']*0.1 for u,v in edges]
    
    plt.figure(figsize=(14,14))
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=widths, alpha=0.4, edge_color='gray')
    nodes = nx.draw_networkx_nodes(
        G, pos,
        node_size=node_sizes,
        node_color=node_colors,
        cmap=plt.cmRdYlGn,
        alpha=0.9
    )
    nx.draw_networkx_labels(
        G, pos,
        labels={n:n for n in G.nodes() if centrality.get(n,0)>0.02},
        font_size=8
    )
    plt.colorbar(nodes, label="Average Sentiment (red=neg, green=pos)")
    plt.title("Breaking Bad Character Co‑occurrence Network with Sentiment")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    try:
        episodes = fetch_json(EPISODES_API)
        quotes   = fetch_json(QUOTES_API)
    except requests.RequestException as e:
        print("API fetch error:", e, file=sys.stderr)
        sys.exit(1)
    
    G = build_cooccurrence_graph(episodes)
    sentiment = compute_sentiment(quotes)
    visualize(G, sentiment)

if __name__ == "__main__":
    main()
