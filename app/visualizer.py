import plotly.graph_objects as go
from typing import Dict
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from io import BytesIO
import base64
from typing import List

def plot_sentiment_distribution(company_sentiments: Dict[str, Dict]) -> go.Figure:
    """
    Creates a grouped bar chart comparing sentiment across companies.

    Args:
        company_sentiments (Dict[str, Dict]): Each key is a ticker, value is counts dict.

    Returns:
        plotly.graph_objects.Figure
    """
    companies = list(company_sentiments.keys())
    sentiments = ["positive", "neutral", "negative"]

    # Extract counts
    data = {s: [company_sentiments[c]["counts"].get(s, 0) for c in companies] for s in sentiments}

    fig = go.Figure()
    for sentiment in sentiments:
        fig.add_trace(go.Bar(
            x=companies,
            y=data[sentiment],
            name=sentiment.capitalize()
        ))

    fig.update_layout(
        title="Sentiment Distribution per Company",
        barmode="group",
        xaxis_title="Company Ticker",
        yaxis_title="Sentence Count",
        height=500
    )

    return fig


def generate_wordcloud_image(cluster_keywords: dict) -> List[Image.Image]:
    images = []
    for cluster_id, keywords in cluster_keywords.items():
        text = ' '.join(keywords)
        wordcloud = WordCloud(width=600, height=400, background_color='white').generate(text)
        img = wordcloud.to_image()
        images.append(img)
    return images
