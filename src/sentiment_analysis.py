# src/sentiment_analysis.py

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure VADER is downloaded. If not, uncomment:
# nltk.download('vader_lexicon')

def analyze_sentiment(df, text_column="reviewText"):
    """
    Performs sentiment analysis on `text_column` using NLTK's VADER.
    Returns a new DataFrame with an added `Sentiment` column.
    """
    sia = SentimentIntensityAnalyzer()

    sentiments = []
    # Fill NaNs with empty string, convert to str
    for text in df[text_column].fillna("").astype(str):
        scores = sia.polarity_scores(text)
        compound = scores['compound']

        if compound >= 0.05:
            sentiments.append("Positive")
        elif compound <= -0.05:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

    df["Sentiment"] = sentiments
    return df
