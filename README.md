# COMP8420_Major_Project
STUDENT NAME: ANKIT CHAHAL(47917903)

# RiskNarrator – NLP-Based Company Risk Analysis

This project analyzes the "Risk Factors" section from company 10-K reports using Natural Language Processing (NLP). It summarizes risk disclosures, classifies sentiment, and extracts dominant themes using topic modeling.

The goal is to help users quickly understand and compare risk narratives across companies through automated processing and interactive visualizations.

---

## 🚀 How to Run

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

Example:
```bash
python test_sentiment.py
```


