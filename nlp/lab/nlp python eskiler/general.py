from nltk.util import pad_sequence
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import flatten
from nltk import word_tokenize
from nltk import sent_tokenize


res = list(pad_sequence(text2[0],
                        pad_left=True, left_pad_symbol="<s>",
                        pad_right=True, right_pad_symbol="</s>",
                        n=3))
print(res)
print(list(ngrams(res, n=2)))

res1 = list(pad_both_ends(text2[1], n=2))
print(res1)

list(bigrams(pad_both_ends(text2[2], n=2)))

padded_bigrams = list(pad_both_ends(text2[1], n=2))
list(everygrams(padded_bigrams, max_len=10))
list(flatten(pad_both_ends(sent, n=2) for sent in text2))
