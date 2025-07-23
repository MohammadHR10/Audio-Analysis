import nltk
from nltk.util import ngrams
from collections import Counter

def extract_bigrams(text):
    # Download tokenizer resources if not already present
    nltk.download('punkt')
    # Tokenize and lowercase the transcript
    tokens = nltk.word_tokenize(text.lower())
    # Extract bigrams (or try trigrams for more structure)
    bigrams = list(ngrams(tokens, 2))
    # Count and display top patterns
    trending = Counter(bigrams).most_common(10)
    print("Top Trending Bigrams:")
    for phrase, count in trending:
        print(f"{' '.join(phrase)}: {count}")
    return trending, tokens 