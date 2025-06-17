from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def extract_topics_per_company(risk_texts, num_clusters=4, top_n=10):
    """
    Apply TF-IDF + KMeans to extract topic keywords per company.

    Args:
        risk_texts (dict): {ticker: risk_text}
        num_clusters (int): Number of clusters to extract per company
        top_n (int): Number of keywords per cluster

    Returns:
        dict: {ticker: {cluster_id: [keywords]}}
    """
    all_topics = {}

    for ticker, text in risk_texts.items():
        vectorizer = TfidfVectorizer(stop_words="english", max_df=0.9)
        X = vectorizer.fit_transform([sent.strip() for sent in text.split('.') if len(sent) > 10])

        if X.shape[0] < num_clusters:  # fallback
            all_topics[ticker] = {0: ["Not enough data"]}
            continue

        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(X)

        terms = vectorizer.get_feature_names_out()
        topics = {}

        for i in range(num_clusters):
            center = kmeans.cluster_centers_[i]
            top_indices = center.argsort()[-top_n:][::-1]
            keywords = [terms[i] for i in top_indices]
            topics[i] = keywords

        all_topics[ticker] = topics

    return all_topics
