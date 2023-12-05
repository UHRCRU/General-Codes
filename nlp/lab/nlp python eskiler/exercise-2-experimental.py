import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown
import re
import random
from nltk.util import pad_sequence
from nltk.util import bigrams
from nltk.util import everygrams
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import flatten
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.lm import MLE
from nltk import sent_tokenize

#1st-2nd steps
print(nltk.corpus.gutenberg.fileids())
moby_dick = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
print("moby dick's length:", len(moby_dick))
milton_paradise = nltk.corpus.gutenberg.words('milton-paradise.txt')
print("milton paradise's length:", len(milton_paradise))
whitman_leaves = nltk.corpus.gutenberg.words('whitman-leaves.txt')
print("whitman leaves' length:", len(whitman_leaves))

#3rd step
print("mob dick's ngrams, ngram 3: ")
for i in moby_dick:
    n3_moby_dick = ngrams(i, n = 3)
    print(list(n3_moby_dick))
print("ngram 4: ")
for i in moby_dick:
    n4_moby_dick = ngrams(i, n = 4)
    print(list(n4_moby_dick))
print("ngram 5: ")
for i in moby_dick:
    n5_moby_dick = ngrams(i, n = 5)
    print(list(n5_moby_dick))

print("milton paradise's ngrams, ngram 3: ")
for i in milton_paradise:
    n3_milton_paradise = ngrams(i, n = 3)
    print(list(n3_milton_paradise))
print("ngram 4: ")
for i in milton_paradise:
    n4_milton_paradise = ngrams(i, n = 4)
    print(list(n4_milton_paradise))
print("ngram 5: ")
for i in milton_paradise:
    n5_milton_paradise = ngrams(i, n = 5)
    print(list(n5_milton_paradise))

print("whitman leaves' ngrams, ngram 3: ")
for i in whitman_leaves:
    n3_whitman_leaves = ngrams(i, n = 3)
    print(list(n3_whitman_leaves))
print("ngram 4: ")
for i in whitman_leaves:
    n4_whitman_leaves = ngrams(i, n = 4)
    print(list(n4_whitman_leaves))
print("ngram 5: ")
for i in whitman_leaves:
    n5_whitman_leaves = ngrams(i, n = 5)
    print(list(n5_whitman_leaves))

tokenized_moby_dick = [list(map(str.lower, word_tokenize(sent))) for sent in sent_tokenize(moby_dick)]
n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_moby_dick)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of moby_dick_3gram word 'wise':", model.logscore("wise"))
print("Log score of moby_dick_3gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram moby dick")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)

n = 4
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_moby_dick)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of moby_dick_4gram word 'wise':", model.logscore("wise"))
print("Log score of moby_dick_4gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram moby dick")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)

n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_moby_dick)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of moby_dick_4gram word 'wise':", model.logscore("wise"))
print("Log score of moby_dick_4gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram moby dick")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)

###########################################################################

tokenized_milton_paradise = [list(map(str.lower, word_tokenize(sent))) for sent in sent_tokenize(tokenized_milton_paradise)]
n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_milton_paradise)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of milton_paradise_3gram word 'wise':", model.logscore("wise"))
print("Log score of milton_paradise_3gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram milton paradise")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)

n = 4
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_moby_dick)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of milton_paradise_4gram word 'wise':", model.logscore("wise"))
print("Log score of milton_paradise_4gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram milton paradise")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)

n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_moby_dick)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of milton_paradise_4gram word 'wise':", model.logscore("wise"))
print("Log score of milton_paradise_4gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram milton paradise")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)

#############################################

tokenized_whitman_leaves = [list(map(str.lower, word_tokenize(sent))) for sent in sent_tokenize(tokenized_whitman_leaves)]
n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_whitman_leaves)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of whitman_leaves_3gram word 'wise':", model.logscore("wise"))
print("Log score of whitman_leaves_3gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram milton paradise")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)

n = 4
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_whitman_leaves)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of whitman_leaves_4gram word 'wise':", model.logscore("wise"))
print("Log score of whitman_leaves_4gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram whitman_leaves")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)

n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_whitman_leaves)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score of whitman_leaves_4gram word 'wise':", model.logscore("wise"))
print("Log score of whitman_leaves_4gram word 'respect':", model.logscore("respect"))
print("probabilities 3gram whitman_leaves")
no = model.score('wise')
print("p(wise) =", no)
no = model.score('respect')
print("p(respect) =", no)
