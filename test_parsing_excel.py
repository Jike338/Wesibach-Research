import pandas as pd
import stanza
import stopwordsiso
from stopwordsiso import stopwords
import string
import operator
import numpy as np
# to read data in a single excel file
new_csv = pd.read_csv("test_2.csv")
new_csv = new_csv['descriptions']

# dictionary for phrase and term
phrase_l = {}
term_l = {}

# get the stop words list
sw_l = stopwords('en')

counter = 1
for txt in new_csv:

    # we omit those that are empty
    if not isinstance(txt, str):
        continue

    print("Processing document #: " + str(counter))

    # periodically save our variable values
    if counter % 50 == 0:
        np.savetxt('phrase_l.txt', phrase_l)
        np.savetxt('term_l.txt', term_l)
    counter += 1

    # get the phrases (without removing stop words from original document) and their frequency count
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
    doc = nlp(txt)
    for sent in doc.sentences:
        for word in sent.words:
            if word.deprel == "amod":
                phrase = word.text.lower() + "_" + sent.words[word.head - 1].text.lower()
                if phrase in phrase_l.keys():
                    phrase_l[phrase] = phrase_l[phrase] + 1
                else:
                    phrase_l[phrase] = 1
            elif word.deprel == "compound" or word.deprel == "flat" or word.deprel == "xcomp":
                phrase = sent.words[word.head - 1].text.lower() + "_" + word.text.lower()
                if phrase in phrase_l.keys():
                    phrase_l[phrase] = phrase_l[phrase] + 1
                else:
                    phrase_l[phrase] = 1

    # get the words (that is not a stop word) and their frequency count
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    txt = txt.split(" ")
    num_l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for word in txt:
        word = word.lower()
        if word not in sw_l and word not in num_l:
            if word in term_l.keys():
                term_l[word] = term_l[word] + 1
            else:
                term_l[word] = 1

    # print result
    print(dict(sorted(phrase_l.items(), key=operator.itemgetter(1), reverse=True)))
    print(dict(sorted(term_l.items(), key=operator.itemgetter(1), reverse=True)))
    term_l_cp = dict(sorted(term_l.items(), key=operator.itemgetter(1), reverse=True))
