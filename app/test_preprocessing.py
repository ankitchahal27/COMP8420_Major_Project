from risk_parser import fetch_risk_section
from preprocessor import clean_and_split

tickers = ["AAPL"]

for ticker in tickers:
    print(f"\n--- {ticker} ---")
    raw_text = fetch_risk_section(ticker)
    sentences = clean_and_split(raw_text)
    
    for s in sentences[:]:
        print("•", s)
