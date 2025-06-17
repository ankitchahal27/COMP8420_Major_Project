from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
from typing import List, Dict
import torch

# Load FinBERT model and tokenizer once
model_name = "yiyanghkust/finbert-tone"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline
finbert_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def analyze_sentiment(sentences: List[str]) -> List[Dict]:
    """
    Apply FinBERT sentiment classification to each sentence.

    Args:
        sentences (List[str]): Cleaned and split risk factor sentences.

    Returns:
        List[Dict]: [{"sentence": "...", "label": "positive"/"negative"/"neutral", "score": 0.98}, ...]
    """
    results = []
    outputs = finbert_pipeline(sentences, truncation=True)

    for sentence, out in zip(sentences, outputs):
        results.append({
            "sentence": sentence,
            "label": out['label'].lower(),   # lowercase for consistency
            "score": round(out['score'], 4)  # probability
        })

    return results
