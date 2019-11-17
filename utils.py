# to obtain all the filtered words from the tsv files

def filtering(string):
    
    sentence1 = str(string).lower() # converting all in lower character to don't have double characters
    sentence2 = ''.join([i for i in sentence1 if not i.isdigit()]) # removing all the numbers
    
    # removing stopwords
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(sentence2)
    no_stopwords = [w for w in word_tokens if not w in stop_words]

    # removing punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    no_punctuation = tokenizer.tokenize(str(no_stopwords))

    # stemming data
    ps = PorterStemmer() 
    stemming = []  
    for w in no_punctuation:
        stemming.append(ps.stem(w))
    stemmed_data = list(set(stemming))
    
    return stemmed_data 
