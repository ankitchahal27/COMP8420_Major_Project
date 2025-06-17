from sentiment import analyze_sentiment
from preprocessor import clean_and_split
from risk_parser import fetch_risk_section
from analytics import aggregate_sentiment
from visualizer import plot_sentiment_distribution

import plotly.io as pio
import plotly.graph_objects as go
import plotly.offline as pyo

tickers = ["AAPL", "MSFT"]
results = {}

for ticker in tickers:
    print(f"\nProcessing {ticker}...")
    raw = fetch_risk_section(ticker)
    sentences = clean_and_split(raw)
    sentiments = analyze_sentiment(sentences[:20])  # limit for speed
    agg = aggregate_sentiment(sentiments)
    results[ticker] = agg

fig = plot_sentiment_distribution(results)
pio.show(fig)  # This opens the chart in a browser or notebook
