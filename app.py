from app.risk_parser import fetch_risk_section
from app.preprocessor import clean_and_split
from app.sentiment import analyze_sentiment
from app.analytics import aggregate_sentiment
from app.visualizer import plot_sentiment_distribution, generate_wordcloud_image
from app.summarizer import summarize_risk_text
from app.topics import extract_topics_per_company

import gradio as gr

selected_tickers = []

def add_ticker(ticker):
    ticker = ticker.upper().strip()
    if not ticker:
        return selected_tickers, "Ticker cannot be empty"
    if ticker in selected_tickers:
        return selected_tickers, f"{ticker} already added"
    if len(selected_tickers) >= 5:
        return selected_tickers, "Maximum 5 tickers allowed"
    selected_tickers.append(ticker)
    return selected_tickers, f"{ticker} added"

def clear_tickers():
    selected_tickers.clear()
    return selected_tickers, "Ticker list cleared"

def analyse_tickers():
    if not selected_tickers:
        return "Please add at least one ticker.", None, "", {}

    sentiment_summary = {}
    risk_texts = {}

    for ticker in selected_tickers:
        try:
            text = fetch_risk_section(ticker)
            risk_texts[ticker] = text
            summary_text = summarize_risk_text(text)
            sentences = clean_and_split(text)
            sentiments = analyze_sentiment(sentences[:30])
            summary = aggregate_sentiment(sentiments)

            summary['summary_text'] = summary_text
            sentiment_summary[ticker] = summary

        except Exception as e:
            sentiment_summary[ticker] = {
                "counts": {"positive": 0, "neutral": 0, "negative": 0},
                "risk_score": 0, "total": 0,
                "summary_text": "Error."
            }

    # Generate sentiment chart
    fig = plot_sentiment_distribution(sentiment_summary)

    # Topic modeling + word clouds
    topics = extract_topics_per_company(risk_texts, num_clusters=3)
    topic_gallery = {
        ticker: generate_wordcloud_image({
            f"cluster_{cluster_id}": keywords
            for cluster_id, keywords in topic_clusters.items()
        })
        for ticker, topic_clusters in topics.items()
    }


    return (
        f"Analysis complete for: {', '.join(selected_tickers)}",
        fig,
        "\n\n".join([f"{t}: {sentiment_summary[t]['summary_text']}" for t in selected_tickers]),
        topic_gallery
    )

with gr.Blocks() as demo:
    gr.Markdown("## 🧠 RiskNarrator: S&P500 Risk Factor Analyzer")

    ticker_input = gr.Textbox(label="Enter S&P 500 Ticker", placeholder="e.g., AAPL")
    add_btn = gr.Button("Add Ticker")
    clear_btn = gr.Button("Clear Tickers")
    ticker_display = gr.Textbox(label="Selected Tickers (max 5)", interactive=False)
    status_output = gr.Textbox(label="Status", interactive=False)

    analyse_btn = gr.Button("Analyse")
    result_text = gr.Textbox(label="Output", interactive=False)
    chart_output = gr.Plot(label="Sentiment Distribution Chart")

    summary_box = gr.Textbox(label="Summary of Risk Factors", lines=15, interactive=False)

    # Topic model result state and output
    topic_gallery_dict = gr.State({})

    with gr.Accordion("Risk Themes by Company (Word Clouds)", open=False) as topic_section:
        gallery_outputs = []
        for i in range(5):  # max 5 companies
            gallery = gr.Gallery(label=f"Company {i+1} Themes", visible=False, columns=2, height=300)
            gallery_outputs.append(gallery)

    def update_galleries(topic_gallery):
        outputs = []
        for idx, ticker in enumerate(selected_tickers):
            images = topic_gallery.get(ticker, [])
            visible = len(images) > 0
            outputs.append(gr.update(value=images, visible=visible))
        # Fill empty galleries to hide them
        while len(outputs) < 5:
            outputs.append(gr.update(value=[], visible=False))
        return outputs

    add_btn.click(add_ticker, inputs=ticker_input, outputs=[ticker_display, status_output])
    clear_btn.click(clear_tickers, outputs=[ticker_display, status_output])
    analyse_btn.click(
        analyse_tickers,
        outputs=[result_text, chart_output, summary_box, topic_gallery_dict]
    ).then(
        update_galleries,
        inputs=[topic_gallery_dict],
        outputs=gallery_outputs
    )

if __name__ == "__main__":
    demo.launch()
