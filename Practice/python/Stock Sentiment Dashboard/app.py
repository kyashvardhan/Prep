# app.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import random
import datetime

app = dash.Dash(__name__)
analyzer = SentimentIntensityAnalyzer()

# Dummy Twitter/News API simulation (replace with real APIs if needed)
def get_fake_news_headlines(stock="Tesla"):
    sample = [
        f"{stock} shares surge amid investor confidence.",
        f"Market reacts negatively to {stock}'s new product launch.",
        f"{stock} under scrutiny for new controversy.",
        f"Analysts predict {stock} to outperform this quarter.",
    ]
    return [random.choice(sample) for _ in range(5)]

def analyze_sentiment(text_list):
    sentiments = []
    for text in text_list:
        score = analyzer.polarity_scores(text)['compound']
        sentiments.append(score)
    return sum(sentiments) / len(sentiments) if sentiments else 0

# App layout
app.layout = html.Div([
    html.H1("📈 Live Stock Sentiment for Tesla", style={'textAlign': 'center'}),
    dcc.Interval(id='interval', interval=5000, n_intervals=0),
    dcc.Graph(id='sentiment-graph'),
])

sentiment_data = []

@app.callback(Output('sentiment-graph', 'figure'), Input('interval', 'n_intervals'))
def update_graph(n):
    headlines = get_fake_news_headlines()
    avg_sentiment = analyze_sentiment(headlines)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    sentiment_data.append({'time': timestamp, 'sentiment': avg_sentiment})
    if len(sentiment_data) > 20:
        sentiment_data.pop(0)

    fig = {
        'data': [{
            'x': [x['time'] for x in sentiment_data],
            'y': [x['sentiment'] for x in sentiment_data],
            'type': 'line',
            'name': 'Sentiment Score'
        }],
        'layout': {
            'yaxis': {'range': [-1, 1]},
            'title': 'Live Sentiment Over Time'
        }
    }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
