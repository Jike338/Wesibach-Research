import stanza
import stopwordsiso
from stopwordsiso import stopwords
import string
import operator

# example of detecting phrases
# nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
# doc = nlp('make Artificial Intelligence interesting It is sure that this is true')
# for sent in doc.sentences:
#     for word in sent.words:
#         if(word.deprel == "xcomp"):
#             print(sent.words[word.head-1].text + "_" + word.text)
#
# print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')

# dictionary for phrase and term
phrase_l = {}
term_l = {}

# get the stop words list
sw_l = stopwords('en')


# read filename file
with open('./', 'r') as f:
    txtName = "test.csv"
    while txtName:
        txt = open(txtName + ".txt", "r")
        txt = str(txt.read())

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

        txtName = f.readline()


# remove term whose frequency is in the top 5% among all
# num_remove = len(term_l)*0.05
# for i in range(0, num_remove):
#     term_l.remove(term_l_cp.keys()[i])
#
# # remove term whose frequency count is <= 20
# for term in term_l:
#     if term_l[term] <= 20:
#         term_l.remove(term_l[term])