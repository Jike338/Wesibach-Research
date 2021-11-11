import nltk
from nltk.stem import 	WordNetLemmatizer
from nltk.corpus import wordnet
import pandas as pd
import csv as csvWriter
import argparse
import string

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Training Station')
    parser.add_argument('--csv', type= str, required = True)
    args = parser.parse_args()
    print(pd.__version__)

    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    wordnet_lemmatizer = WordNetLemmatizer()

    def listToString(s):
        str1 = " "
        return (str1.join(s))

    def construct_sentence_from_list(l):
        res = ""
        for word in l:
            if word not in string.punctuation:
                res += " " + word
            else:
                res += word 
        return res

    def lemmatize(in_list):
        out_list = []
        for word in in_list: 
            word = wordnet_lemmatizer.lemmatize(word)
            out_list.append(word)
        
        return out_list

    # function to convert nltk tag to wordnet tag
    def nltk_tag_to_wordnet_tag(nltk_tag):
        if nltk_tag.startswith('J'):
            return wordnet.ADJ
        elif nltk_tag.startswith('V'):
            return wordnet.VERB
        elif nltk_tag.startswith('N'):
            return wordnet.NOUN
        elif nltk_tag.startswith('R'):
            return wordnet.ADV
        else:          
            return None

    def lemmatize_sentence(sentence):
        #tokenize the sentence and find the POS tag for each token
        nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))  
        #tuple of (token, wordnet_tag)
        wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
        lemmatized_sentence = []
        for word, tag in wordnet_tagged:
            if tag is None:
                #if there is no available tag, append the token as is
                lemmatized_sentence.append(word)
            else:        
                #else use the tag to lemmatize the token
                lemmatized_sentence.append(wordnet_lemmatizer.lemmatize(word, tag))
            
        return construct_sentence_from_list(lemmatized_sentence)

    print("--------------------------reading csv--------------------------")
    # to read data in a single excel file
    csv = pd.read_csv(str(args.csv))
    csv['all'] = csv[csv.columns[1:]].apply(
        lambda x: ' '.join(x.dropna().astype(str)),
        axis=1
    )
    
    new_csv = csv['wku'].map(str) +csv['all'].map(str)
    new_csv = new_csv.dropna()
    new_csv = new_csv.reset_index(drop=True)
    tokenization_l = []

    print("--------------------------lemmatizing--------------------------")

    for num, txt in enumerate(new_csv):
        print("Processing document #: ", num)
        curr_doc = txt
        if num < len(new_csv)-1:
            if not str(new_csv[num+1])[0].isnumeric():
                curr_doc = curr_doc + " " + new_csv[num+1]
        
        if not str(txt)[0].isnumeric():
            continue
        # tokenization = nltk.word_tokenize(curr_doc) 
        tokenization_value = lemmatize_sentence(curr_doc)
        # tokenization_value = listToString(tokenization_value)
        tokenization_wku = tokenization_value[0:7]
        tokenization_value = tokenization_value[7:]
        tokenization_l.append({'wku': tokenization_wku, 'value': tokenization_value})

    # df = pd.DataFrame(tokenization_l, columns=['wku', 'value'])
    # df.to_csv('res2.csv', index=False)

    print("--------------------------writing csv--------------------------")
    
    out_file_name = str(args.csv).split('.')[0]+"_l.csv"
    with open(out_file_name, 'w') as csvfile:
        writer = csvWriter.writer(csvfile)
        writer.writerow(['wku', 'value'])
        for patent in tokenization_l:
            writer.writerow([patent['wku'], patent['value']])