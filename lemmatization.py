import nltk
from nltk.stem import 	WordNetLemmatizer
import pandas as pd
import csv as csvWriter
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Training Station')
    parser.add_argument('--csv', type= str, required = True)
    args = parser.parse_args()
    print(pd.__version__)

    nltk.download('punkt')
    nltk.download('wordnet')
    wordnet_lemmatizer = WordNetLemmatizer()

    def listToString(s):
        str1 = " "
        return (str1.join(s))

    def lemmatize(in_list):
        out_list = []
        for word in in_list: 
            word = wordnet_lemmatizer.lemmatize(word)
            out_list.append(word)
        
        return out_list

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
        tokenization = nltk.word_tokenize(curr_doc) 
        tokenization_value = lemmatize(tokenization)
        tokenization_value = listToString(tokenization_value)
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