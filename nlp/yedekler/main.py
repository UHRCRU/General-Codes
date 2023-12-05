import nltk
import random
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize

review = "Mr. Matt Damon was outstanding, fantastic, excellent, wonderfully subtle, superb, terrific, and memorable in his portrayal of Mulan."

#nltk.download('movie_reviews')

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

feature_set = [(document_features(doc), category) for (doc, category) in documents]
all_words_frequency = nltk.FreqDist()

test_set = feature_set[:400]
train_set = feature_set[400:]

classifier = nltk.NaiveBayesClassifier.train(train_set)

review_lowercased = review.lower()
review_tokenized = word_tokenize(review_lowercased)
review_features = document_features(review_tokenized)
review_classified = classifier.classify(review_features)
prob_of_pos= classifier.prob_classify(review_features).prob('pos')
prob_of_neg= classifier.prob_classify(review_features).prob('neg')

print("---Task 2.2---\n")

print("Lowercased Text: {}\n".format(review_lowercased))
print("Tokenized Text: {}\n".format(review_tokenized))
print("Features Text: {}\n".format(review_features))
print("Classified Text: {}\n".format(review_classified))
print("Probability of pos: {}\n".format(prob_of_pos))
print("Probability of neg: {}\n".format(prob_of_neg))

print("---Task 2.3---\n")

review2 = "Mr. Steven Seagal was outstanding, fantastic, excellent, wonderfully subtle, superb, terrific, and memorable in his portrayal of Mulan."

print("Lowercased Text: {}\n".format(review2.lower()))
print("Tokenized Text: {}\n".format(word_tokenize(review2.lower())))
print("Features Text: {}\n".format(document_features(word_tokenize(review2))))
print("Classified Text: {}\n".format(classifier.classify(document_features(word_tokenize(review2)))))
print("Probability of pos: {}\n".format(classifier.prob_classify(document_features(word_tokenize(review2))).prob('pos')))
print("Probability of neg: {}\n".format(classifier.prob_classify(document_features(word_tokenize(review2))).prob('neg')))

print("---Task 2.4---\n")

review3 = "Mr. Matt Damon was outstanding, fantastic."

print("Lowercased Text: {}\n".format(review3.lower()))
print("Tokenized Text: {}\n".format(word_tokenize(review3.lower())))
print("Features Text: {}\n".format(document_features(word_tokenize(review3))))
print("Classified Text: {}\n".format(classifier.classify(document_features(word_tokenize(review3)))))
print("Probability of pos: {}\n".format(classifier.prob_classify(document_features(word_tokenize(review3))).prob('pos')))
print("Probability of neg: {}\n".format(classifier.prob_classify(document_features(word_tokenize(review3))).prob('neg')))

print("---Task 2.5---")
print(classifier.show_most_informative_features(30)) 