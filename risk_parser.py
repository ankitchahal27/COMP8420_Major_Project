from edgar import Company, set_identity

# Set your identity (email) required by the SEC EDGAR API
# IMPORTANT: Replace with your own email address
set_identity("your_email@example.com")

def fetch_risk_section(ticker: str) -> str:
    """
    Fetches the 'Item 1A: Risk Factors' section from the latest 10-K filing
    for a given company ticker using the edgartools library.
    """
    try:
        company = Company(ticker)
        filings = company.get_filings(form="10-K", amendments=False)
        latest_10k = filings.latest(1)

        if not latest_10k:
            return f"No 10-K filings found for {ticker}."

        # Convert the filing to a TenK data object
        tenk_obj = latest_10k.obj()

        # As per the documentation, access risk factors directly via the .risk_factors attribute
        risk_factors_text = tenk_obj.risk_factors

        if not risk_factors_text:
            return f"'risk_factors' section could not be found or is empty in the latest 10-K for {ticker}."

        # Return the text, removing any leading/trailing whitespace
        return risk_factors_text.strip()

    except AttributeError:
        # This will catch cases where a very old filing might not have the .risk_factors attribute
        return f"'risk_factors' attribute not found for {ticker}. The filing may be too old or in an unexpected format."
    except Exception as e:
        # This will catch other errors like network issues.
        return f"An error occurred while processing {ticker}: {e}"

