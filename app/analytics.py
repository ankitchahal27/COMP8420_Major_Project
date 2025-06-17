from typing import List, Dict
from collections import Counter

def aggregate_sentiment(results: List[Dict]) -> Dict:
    """
    Aggregates sentiment labels and computes sentiment counts and risk score.

    Args:
        results (List[Dict]): Output from sentiment.py, one dict per sentence.

    Returns:
        Dict: {
            "counts": {"positive": X, "neutral": Y, "negative": Z},
            "risk_score": float,
            "total": int
        }
    """
    labels = [r["label"] for r in results]
    counts = Counter(labels)
    total = sum(counts.values())

    # Default 0 for any missing class
    positive = counts.get("positive", 0)
    neutral = counts.get("neutral", 0)
    negative = counts.get("negative", 0)

    risk_score = (negative / total) - (positive / total) if total > 0 else 0

    return {
        "counts": {"positive": positive, "neutral": neutral, "negative": negative},
        "risk_score": round(risk_score, 3),
        "total": total
    }
