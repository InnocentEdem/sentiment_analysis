# main.py

import os
from src.data_downloader import download_amazon_reviews_kaggle
from src.data_loader import load_amazon_reviews
from src.sentiment_analysis import analyze_sentiment
from src.theme_extraction import extract_key_themes
from src.visualization import create_wordcloud

def main():
    # --- 1. Download the Kaggle dataset ---
    dataset_name = "mehmetisik/amazon-review"
    local_path = "data/raw"
    download_amazon_reviews_kaggle(dataset_name=dataset_name, local_path=local_path)

    # --- 2. Load the CSV file ---
    # After unzipping, check the actual CSV name in data/raw/ (e.g., "AmazonReview.csv")
    csv_filename = os.path.join(local_path, "amazon_review.csv")
    # For demonstration, load a subset of rows for speed; remove `nrows=10000` to load all
    df = load_amazon_reviews(csv_filename, nrows=10000)

    # --- 3. Perform sentiment analysis on "reviewText" ---
    df = analyze_sentiment(df, text_column="reviewText")

    # --- 4. Calculate sentiment distribution ---
    sentiment_counts = df["Sentiment"].value_counts()
    total_reviews = len(df)

    pos_pct = (sentiment_counts.get("Positive", 0) / total_reviews) * 100
    neg_pct = (sentiment_counts.get("Negative", 0) / total_reviews) * 100
    neu_pct = (sentiment_counts.get("Neutral", 0) / total_reviews) * 100

    print("\n=== SENTIMENT ANALYSIS REPORT ===")
    print(f"Total Reviews Analyzed: {total_reviews}")
    print(f"Positive: {pos_pct:.1f}%")
    print(f"Negative: {neg_pct:.1f}%")
    print(f"Neutral:  {neu_pct:.1f}%")

    # --- 5. Extract top recurring themes (words) ---
    top_n = 10
    top_words = extract_key_themes(df, text_column="reviewText", top_n=top_n)
    print(f"\n=== TOP {top_n} RECURRING WORDS ===")
    for word, freq in top_words:
        print(f"{word}: {freq}")

    # Convert list of tuples to dict for word cloud
    word_freq_dict = dict(top_words)
    create_wordcloud(word_freq_dict, output_filename="analysis_results_wordcloud.png", 
                     title="Word Cloud of Amazon Reviews")

    # (Optional) Print a small sample of the data
    print("\n=== SAMPLE REVIEWS & SENTIMENT ===")
    print(df[["reviewText", "Sentiment"]].head(5))

if __name__ == "__main__":
    main()
