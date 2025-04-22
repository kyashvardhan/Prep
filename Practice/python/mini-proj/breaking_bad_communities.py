#!/usr/bin/env python3
"""
breaking_bad_communities.py
Dependencies:
    pip install requests networkx matplotlib vaderSentiment
"""

import requests
import sys
import networkx as nx
from networkx.algorithms import community
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

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
    sums, counts = {}, {}
    for q in quotes:
        author = q.get("author","").strip()
        text   = q.get("quote","").strip()
        if author and text:
            score = analyzer.polarity_scores(text)["compound"]
            sums[author]   = sums.get(author, 0.0) + score
            counts[author] = counts.get(author, 0) + 1
    return {a: sums[a]/counts[a] for a in sums}

def detect_communities(G):
    # Greedy modularity communities
    comms = list(community.greedy_modularity_communities(G, weight='weight'))
    # map node -> community index
    mapping = {}
    for idx, comm in enumerate(comms):
        for node in comm:
            mapping[node] = idx
    return mapping, comms

def analyze_communities(comms, sentiment):
    print("Communities and their average sentiment:\n")
    for idx, comm in enumerate(comms):
        vals = [sentiment.get(n, 0.0) for n in comm]
        avg = sum(vals) / len(vals)
        print(f" Community {idx} (size {len(comm)}): avg sentiment {avg:.2f}")
    print()

def visualize(G, sentiment, com_map):
    pos = nx.spring_layout(G, k=0.3, iterations=40)
    centrality = nx.degree_centrality(G)
    
    # Node colors = community, sizes ~ centrality
    node_colors = [com_map.get(n, -1) for n in G.nodes()]
    node_sizes  = [1000 * centrality[n] + 100 for n in G.nodes()]
    
    plt.figure(figsize=(12,12))
    nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color='gray',
                           width=[G[u][v]['weight']*0.05 for u,v in G.edges()])
    nodes = nx.draw_networkx_nodes(G, pos,
                                   node_size=node_sizes,
                                   node_color=node_colors,
                                   cmap=plt.cm.tab20,
                                   alpha=0.9)
    # Label only major characters
    labels = {n: n for n, c in centrality.items() if c > 0.03}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)
    
    plt.colorbar(nodes, label="Community Index")
    plt.title("Breaking Bad Character Communities")
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
    com_map, comms = detect_communities(G)
    analyze_communities(comms, sentiment)
    visualize(G, sentiment, com_map)

if __name__ == "__main__":
    main()
