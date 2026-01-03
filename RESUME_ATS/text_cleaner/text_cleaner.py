import re
import nltk
from nltk.corpus import stopwords

import nltk
from nltk.corpus import stopwords

def get_stopwords():
    try:
        return set(stopwords.words("english"))
    except LookupError:
        nltk.download("stopwords", quiet=True)
        return set(stopwords.words("english"))


stop_words = get_stopwords()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text)

    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)
