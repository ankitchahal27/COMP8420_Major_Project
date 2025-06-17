# COMP8420_Major_Project
STUDENT NAME: ANKIT CHAHAL(47917903)

# RiskNarrator – NLP-Based Company Risk Analysis

This project analyzes the "Risk Factors" section from company 10-K reports using Natural Language Processing (NLP). It summarizes risk disclosures, classifies sentiment, and extracts dominant themes using topic modeling.

The goal is to help users quickly understand and compare risk narratives across companies through automated processing and interactive visualizations.

---

##  How to Run

1. **Install dependencies** (recommended in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the main application**:
   ```bash
   python app.py
   ```

3. The Gradio web interface will open in your browser for interactive use.

---

##  About the Test Files

Each major component of the pipeline has a corresponding test script. If something doesn't work, you can debug or verify functionality by running the appropriate test file individually:

- `test_preprocessing.py`: Verifies risk text preprocessing
- `test_parser.py`: Checks extraction of the “Risk Factors” section
- `test_sentiment.py`: Tests sentiment classification
- `test_topics.py`: Validates topic extraction (TF-IDF + KMeans)
- `testing_final.py`: End-to-end test combining all modules

You can run any test file using:
```bash
python test_<module>.py
```
---

##  Example: How to Add Tickers

You can analyze up to **5 tickers at a time**. Here’s how to add tickers like `AAPL`, `MSFT`, and `AMZN`:

### Step-by-Step Instructions

1. **Enter a ticker symbol** (e.g., `aapl`) in the input box labeled `Enter S&P 500 Ticker`.
2. Click the **"Add Ticker"** button.
3. Confirm the ticker is added — it will appear in the `Selected Tickers` list below.
4. Repeat steps 1–3 for each additional ticker.
5. Example sequence:
   - Input: `aapl` → click **Add Ticker** → Status: `AAPL added`
   - Input: `msft` → click **Add Ticker** → Status: `MSFT added`
   - Input: `amzn` → click **Add Ticker** → Status: `AMZN added`

Once done, proceed with analysis using the "Analyse" button in the UI.

---  



