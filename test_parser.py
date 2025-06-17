from risk_parser import fetch_risk_section

# List of tickers to test
tickers = ["AAPL"]

print("--- Fetching Risk Factors from Latest 10-K Filings ---")

for t in tickers:
    print(f"\n--- Processing: {t} ---")
    
    # Fetch the 'Item 1A' section
    risk_section = fetch_risk_section(t)
    
    # Check if the section was found and print the first 1000 characters
    if "An error occurred" in risk_section or "not found" in risk_section:
        print(risk_section)
    else:
        print(risk_section)

print("\n--- All tickers processed. ---")