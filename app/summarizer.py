from transformers import pipeline

# Load summarization model once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_risk_text(text: str, max_len: int = 130) -> str:
    """
    Summarize long risk section text into 1-2 paragraphs.

    Args:
        text (str): Full risk section
        max_len (int): Max summary length in tokens

    Returns:
        str: Summary
    """
    # BART cannot handle very long text, so truncate if needed
    text = text[:3000]

    summary = summarizer(text, max_length=max_len, min_length=40, do_sample=False)
    return summary[0]['summary_text']
