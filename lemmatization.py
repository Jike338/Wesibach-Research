import nltk
from nltk.stem import 	WordNetLemmatizer
import pandas as pd

nltk.download('punkt')
nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w))) 


# to read data in a single excel file
csv = pd.read_csv("test_2.csv")
csv['all'] = csv[csv.columns[1:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1
)

new_csv = csv['all']

counter =1
for txt in new_csv:
    print("Processing document #: " + str(counter))
    tokenization = nltk.word_tokenize(txt)
    print(tokenization)