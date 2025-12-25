import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

def summarize(text, ratio=0.3):
    stop_words = set(stopwords.words("english"))

    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    word_freq = {}
    for word in words:
        if word.isalnum() and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word]

    select_length = max(1, int(len(sentences) * ratio))
    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:select_length]

    return " ".join(summary_sentences)
