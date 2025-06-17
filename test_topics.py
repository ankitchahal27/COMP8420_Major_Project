from risk_parser import fetch_risk_section
from preprocessor import clean_and_split
from topics import extract_topics_per_company
from visualizer import generate_wordcloud_image

import matplotlib.pyplot as plt

# Example ticker to test
tickers = ["AAPL", "MSFT"]
risk_texts = {}

# Step 1: Fetch and store risk sections
for ticker in tickers:
    text = fetch_risk_section(ticker)
    risk_texts[ticker] = text

# Step 2: Extract topics
topics = extract_topics_per_company(risk_texts, num_clusters=3, top_n=10)
print("Extracted Topics:", topics)

# Step 3: Generate word clouds and display them
for ticker in topics:
    fig = generate_wordcloud_image(topics[ticker])
    plt.figure(figsize=(6, 4))
    plt.imshow(fig)
    plt.axis("off")
    plt.title(f"Word Cloud - {ticker}")
    plt.show()
