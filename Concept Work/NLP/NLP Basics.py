#NLP Basics
#Import modules
import string
import nltk

from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
from nltk.util import ngrams

#Concept 1 - Text Cleaning
def clean_text(text):
    clean_text = text.lower()
    clean_text = clean_text.translate(str.maketrans("","",string.punctuation))
    return clean_text

sentance_1 = "I told her okay, come through!"
sentance_clean = clean_text(sentance_1)
print(f"Original: {sentance_1}\nClean: {sentance_clean}")

#Concept 2 - Tokenization
def token_words(text):
    tokenized_words = TextBlob(text).words
    return tokenized_words

sentance_2 = "I AM the best!! Better than the rest!?"
sentance_clean = clean_text(sentance_2)
words_1 = token_words(sentance_clean)
print(f"Tokenization: {words_1}")

#Concept 3 - Stopword Removal
def stopword_removal(words):
    new_words = []
    stop_words = set(stopwords.words("english"))
    for word in words:
        if word not in stop_words:
            new_words.append(word)
    return new_words

new_words = stopword_removal(words_1)
print(f"New Words: {new_words}")

#Concept 4 - Lemmatization
def lemmatization(words):
    lemmatized = []
    for word in words:
        word1 = Word(word)
        lemmatized.append(word1.lemmatize())
    return lemmatized

wordset = ["runner","studies","libraries","booking","lifting"]
new_wordset = lemmatization(wordset)

print(f"Wordset 1: {wordset}\nNew Wordset: {new_wordset}")

#Concept 5 - Frequency Counter
def frequency_counter(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word,0) + 1
    return freq

freq = frequency_counter(new_words)
print(freq)

#Concept 6 - n grams
gpt_words = ["cars", "drive", "fast"]

print("Bigram")
bigram = list(ngrams(gpt_words,2))
print(bigram)
print("Trigram")
trigram = set(ngrams(gpt_words,3))
print(trigram)