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
new_csv = new_csv.dropna()
last_doc = ""
for num, txt in enumerate(new_csv):
    curr_doc = ""
    last_doc = txt
    if str(txt)[0].isnumeric():
        curr_doc = txt
    else:
        curr_doc = last_doc + " " + curr_doc
    tokenization = nltk.word_tokenize(curr_doc)    
    print(tokenization)