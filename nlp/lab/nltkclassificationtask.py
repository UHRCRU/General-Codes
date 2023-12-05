import nltk
from nltk.corpus import movie_reviews
import re
import random
#1.1
print(len(movie_reviews.words()))
print(movie_reviews.categories())
print("positive reviews:", len(movie_reviews.fileids('pos')))
print("negative reviews:", len(movie_reviews.fileids("neg")))
print(nltk.FreqDist(movie_reviews.words()))
print("most common 15 words", nltk.FreqDist(movie_reviews.words()).most_common(15))
#2.0 defining a short review:
text1 = """Mr. Matt Damon was outstanding, fantastic, excellent, wonderfully subtle, superb, terrific, and memorable in his portrayal of Mulan."""
#2.1 lowercase the text
text1 = text1.lower()
print("exercise2.1", text1)
#2.2 tokenize the text
print('exercise2.2', re.findall('.[A-z]+',text1))
text1 = re.findall('.[A-z]+',text1)
#2.3 document_function
document = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids()]
random.shuffle(document)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
featuresets = [(document_features(document), category) for (document,category) in document]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print("exercise 2.3", classifier.labels())

print("exercise 2.3", document_features(text1))
#2.4
print("exercies 2.4:", classifier.classify(document_features(text1)))
#2.5

print("exercise 2.5Ç")
dist = classifier.prob_classify(document_features(text1))
for label in dist.samples():
    print("%s: %f" % (label, dist.prob(label)))
#3.0"""
text1 = """Mr. Steven Seagal was outstanding, fantastic, excellent, wonderfully subtle, superb, terrific, and memorable in his portrayal of Mulan."""
print("exercise 3.0:", classifier.classify(document_features(text1)))
#4.0
text1 = """Mr. Matt Damon was outstanding, fantastic."""
print("exercise 4.0:", classifier.classify(document_features(text1)))
#5.0
print("exercise 5.0:")
classifier.show_most_informative_features(30)
