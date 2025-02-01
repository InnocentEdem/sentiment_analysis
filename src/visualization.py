# src/visualization.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud

def create_wordcloud(freq_dict, output_filename="wordcloud.png", title="Word Cloud"):
    """
    Generates and saves a word cloud image from a frequency dictionary.
    freq_dict: dict of {word: frequency}
    """
    wc = WordCloud(width=800, height=400, background_color='white')
    wc.generate_from_frequencies(freq_dict)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title(title)
    plt.savefig(output_filename)
    plt.show()
    print(f"Word cloud saved as {output_filename}.")
