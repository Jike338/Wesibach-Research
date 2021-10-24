import stanza


nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
doc = nlp('make Artificial Intelligence interesting It is sure that this is true')
for sent in doc.sentences:
    for word in sent.words:
        if(word.deprel == "xcomp"):
            print(sent.words[word.head-1].text + "_" + word.text)

print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')

# nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt')
# doc = nlp('We want to make sure that we will win first place to receive a new computer.')
# for token in doc.sentences[0].tokens:
#     print(f'token: {token.text}\twords: {", ".join([word.text for word in token.words])}')



# stanza.download('en')   # This downloads the English models for the neural pipeline
# nlp = stanza.Pipeline() # This sets up a default neural pipeline in English
# doc = nlp("We want to make sure that we will win first place to receive a new computer.")
# doc.sentences[0].print_dependencies()