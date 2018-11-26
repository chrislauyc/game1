import nltk
from itertools import permutations
english_vocab = set(w.lower() for w in nltk.corpus.words.words())

wordlist = []
letters = ['w','n','o','g','r']
per = permutations(letters,4)
for w in list(per):
    word = ''
    for el in w:
        word += el
    if word in english_vocab:
        wordlist.append(word)
print(wordlist)