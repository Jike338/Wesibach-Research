import nltk
from nltk.stem import 	WordNetLemmatizer
import pandas as pd

nltk.download('punkt')
nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()
text = "orange oranges"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w))) 



#generate generates => (bias) => lower fre
#apple apples => apple (unbiased) => higher fre *
