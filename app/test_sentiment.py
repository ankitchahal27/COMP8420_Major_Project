from risk_parser import fetch_risk_section
from preprocessor import clean_and_split
from sentiment import analyze_sentiment

ticker = "AAPL"

print(f"\n--- {ticker} ---")
raw_text = fetch_risk_section(ticker)
sentences = clean_and_split(raw_text)
sentiment_results = analyze_sentiment(sentences[:10])  # limit to first 10 for speed

for result in sentiment_results:
    print(f"[{result['label']}] ({result['score']}) → {result['sentence']}")
