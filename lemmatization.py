import nltk
from nltk.stem import 	WordNetLemmatizer
import pandas as pd
from csv import DictReader

nltk.download('punkt')
nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w))) 


# to read data in a single excel file
csv = pd.read_csv("31.csv")
csv['all'] = csv[csv.columns[1:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1
)
new_csv = csv['wku']+csv['all']
last_doc = ""
for num, txt in enumerate(new_csv):
    print(len(txt))
    
    if str(txt)[0].isnumeric():
        last_doc = txt
    else:
        last_doc = last_doc + " " + txt
    print(len(last_doc))
    print(last_doc[0])
    tokenization = nltk.word_tokenize(last_doc)    