import re
import nltk
from typing import List



from nltk.tokenize import sent_tokenize


def clean_and_split(text: str) -> List[str]:
    """
    Cleans the raw 10-K 'Item 1A' text and splits it into sentences.

    Parameters:
        text (str): Raw text of the risk section.

    Returns:
        List[str]: A list of cleaned, well-formed sentences.
    """

    # Remove headers like "Forward-Looking Statements" or item headings
    text = re.sub(r'ITEM\s+1A[.\s:-]+RISK\s+FACTORS', '', text, flags=re.IGNORECASE)
    text = re.sub(r'FORWARD-LOOKING STATEMENTS', '', text, flags=re.IGNORECASE)

    # Remove all caps section titles (common in filings)
    text = re.sub(r'\n[A-Z\s,]{5,}\n', '\n', text)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Tokenize into sentences
    sentences = sent_tokenize(text)

    # Filter out very short or meaningless lines
    sentences = [s.strip() for s in sentences if len(s.strip()) > 30]

    return sentences
