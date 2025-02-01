# src/theme_extraction.py

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# Make sure stopwords are downloaded:
# nltk.download('stopwords')

def extract_key_themes(df, text_column="reviewText", top_n=10):
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import CountVectorizer

    # This line returns a set of stopwords
    stop_words = set(stopwords.words("english"))
    # Convert it to a list
    stop_words = list(stop_words)

    vectorizer = CountVectorizer(stop_words=stop_words)
    text_data = df[text_column].fillna("").astype(str).values
    X = vectorizer.fit_transform(text_data)

    word_counts = X.toarray().sum(axis=0)
    vocab = vectorizer.get_feature_names_out()
    freq_dict = dict(zip(vocab, word_counts))

    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[:top_n]

