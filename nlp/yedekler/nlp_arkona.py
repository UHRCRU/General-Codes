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




#***********step 1*******************
nltk.corpus.gutenberg.fileids()
burgess = nltk.corpus.gutenberg.words('burgess-busterbrown.txt')
paradise = nltk.corpus.gutenberg.words('milton-paradise.txt')
moby = nltk.corpus.gutenberg.words('melville-moby_dick.txt')

burgess_raw = nltk.corpus.gutenberg.raw('burgess-busterbrown.txt')
paradise_raw = nltk.corpus.gutenberg.raw('milton-paradise.txt')
moby_raw = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
#*************step2*******************
num_ch_burgess = len(gutenberg.raw('burgess-busterbrown.txt'))
num_ch_paradise = len(gutenberg.raw('milton-paradise.txt'))
num_ch_moby = len(gutenberg.raw('melville-moby_dick.txt'))
print("Number of chars in burgess-busterbrown.txt is:"+str(num_ch_burgess))
print("Number of chars in milton-paradise.txt is:"+str(num_ch_paradise))
print("Number of chars in melville-moby_dick.txt is:"+str(num_ch_moby))


print("*****************************************************")


num_wd_burgess = len(gutenberg.words('burgess-busterbrown.txt'))
num_wd_paradise = len(gutenberg.words('milton-paradise.txt'))
num_wd_moby = len(gutenberg.words('melville-moby_dick.txt'))
print("Number of words in burgess-busterbrown.txt is:"+str(num_wd_burgess))
print("Number of words in milton-paradise.txt is:"+str(num_wd_paradise))
print("Number of words in melville-moby_dick.txt is:"+str(num_wd_moby))    


print("*****************************************************")  


num_sentences_burgess = len(gutenberg.sents('burgess-busterbrown.txt'))           
num_sentences_paradise = len(gutenberg.sents('milton-paradise.txt'))               
num_sentences_moby = len(gutenberg.sents('melville-moby_dick.txt'))
print("Number of sentences in burgess-busterbrown.txt is:"+str(num_sentences_burgess))
print("Number of sentences in milton-paradise.txt is:"+str(num_sentences_paradise))
print("Number of sentences in melville-moby_dick.txt is:"+str(num_sentences_moby))


print("\n\n")  

num_voc_burgess = len(set(w.lower() for w in gutenberg.words('burgess-busterbrown.txt')))
num_voc_paradise = len(set(w.lower() for w in gutenberg.words('milton-paradise.txt')))
num_voc_moby = len(set(w.lower() for w in gutenberg.words('melville-moby_dick.txt')))
print("Number of vocabularies in burgess-busterbrown.txt:"+str(num_voc_burgess))
print("Number of vocabularies in milton-paradise.txt is:"+str(num_voc_paradise))
print("Number of vocabularies in melville-moby_dick.txt:"+str(num_voc_moby))


print("\n\n")

#********step3******************
print("3gramburgess")
print(list(nltk.ngrams(burgess, 3)))

print("4gramburgess")
print(list(nltk.ngrams(burgess, 4)))

print("5gramburgess")
print(list(nltk.ngrams(burgess, 5)))

print("\n\n")



print("3gramParadise")
print(list(nltk.ngrams(paradise, 3)))

print("4gramParadise")
print(list(nltk.ngrams(paradise, 4)))

print("5gramParadise")
print(list(nltk.ngrams(paradise, 5)))


print("3gramMOby")
print(list(nltk.ngrams(moby, 3)))

print("4gramMOby")
print(list(nltk.ngrams(moby, 4)))

print("5gramMOby")
print(list(nltk.ngrams(moby, 5)))

print("\n\n")

#*********step4****************
tokenized_text_burgess = [list(map(str.lower, word_tokenize(sent)))
                  for sent in sent_tokenize(burgess_raw)]

n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_burgess)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'burgess-busterbrown.txt' (3gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'burgess-busterbrown.txt' (3gram):", model.logscore("respect"))
print("probabilities 3gram burgess")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect) =", no)
n = 4
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_burgess)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'burgess-busterbrown.txt' (4gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'burgess-busterbrown.txt' (4gram):", model.logscore("respect"))
print("probabilities 4gram burgess")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect) =", no)
n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_burgess)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'burgess-busterbrown.txt' (5gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'burgess-busterbrown.txt' (5gram):", model.logscore("respect"))
print("probabilities 5gram burgess")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect) =", no)
###############################################################################
tokenized_text_paradise = [list(map(str.lower, word_tokenize(sent)))
                  for sent in sent_tokenize(paradise_raw)]

n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_paradise)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'milton-paradise.txt' (3gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'milton-paradise.txt' (3gram):", model.logscore("respect"))
print("probabilities 3gram paradise")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect) =", no)
n = 4
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_paradise)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'milton-paradise.txt' (4gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'milton-paradise.txt' (4gram):", model.logscore("respect"))
print("probabilities 4gram paradise")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect) =", no)
n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_paradise)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'milton-paradise.txt' (5gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'milton-paradise.txt' (5gram):", model.logscore("respect"))
print("probabilities 5gram paradise")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect =", no)
####################################################################################

tokenized_text_moby = [list(map(str.lower, word_tokenize(sent)))
                  for sent in sent_tokenize(moby_raw)]

n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_moby)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'melville-moby_dick.txt' (3gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'melville-moby_dick.txt' (3gram):", model.logscore("respect"))
print("probabilities 3gram moby")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect) =", no)
n = 4
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_moby)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'melville-moby_dick.txt' (4gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'melville-moby_dick.txt' (4gram):", model.logscore("respect"))
print("probabilities 4gram moby")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect) =", no)
n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text_moby)
model = MLE(n)

model.fit(train_data, padded_sents)
print("Log score (log probability) for 'excellent' word in 'melville-moby_dick.txt' (5gram):", model.logscore("excellent"))
print("Log score (log probability) for 'respect' word in 'melville-moby_dick.txt' (5gram):", model.logscore("respect"))
print("probabilities 5gram moby")
no = model.score('excellent')
print("p(excellent) =", no)
no = model.score('respect')
print("p(respect) =", no)

