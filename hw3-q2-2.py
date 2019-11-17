# EX 2.2. - Conjunctive query & Ranking score
#
#

# 2.2.0 We define some functions:

import math
from textblob import TextBlob as tb

# to get the TF
def tf(word, doc):
    return doc.count(word) / len(doc)
# to get number of documents containing a word
def n_containing(word, doclist):
    return sum(1 for doc in doclist if word in doc.split())

# strings that represent intro and plot of every document

LINE_NUMBERS = 30000
Docum_and_words = []
for i in range(LINE_NUMBERS):
    file = "Cleantsv/filmclean-"+str(i)+'.tsv' #we can change the name depending to results of 2.1
    file1 = open(file, encoding="utf8") 
    line = file1.read() # Use this to read file content as a stream: 
    words = line.split('\t') 
    wordssplitted1 = words[14].split()
    wordssplitted2 = words[15].split()
    words = wordssplitted1+wordssplitted2
    A = " ".join(words)
    Docum_and_words.append(A)
#I have the list of documents with intro and plot
Docum_and_words[0]

# SAmple Output: 
# midnight 1983 american crime horror thriller film 3 direct j lee thompson screenplay origin written william robert film star charl bronson lead role support cast includ lisa eilbach andrew steven gene davi ge #


# 2.2.0 We define a dictionary with idf in order to save computational costs

with open(r"dicturls.json", 'r') as file:
    data = file.read()
dicturls = json.loads(data) 
with open(r"dictionary.json", 'r') as file:
    data = file.read()
diction = json.loads(data) #first dict with every word and a unique value
with open(r"dictionary1.json", 'r') as file:
    data = file.read()
diction2 = json.loads(data)#first inverted dict with number and list of document with a word that has that number in diction
import math
from textblob import TextBlob as tb


def tf(word, doc):
    return doc.count(word) / len(doc)
def n_containing(word, doclist):
    return sum(1 for doc in doclist if word in doc.split())

def idf(word, doclist):
    return math.log(len(doclist) / float(n_containing(word, doclist)))

def tfidf(word, doc, doclist):
    return (tf(word, doc) * idf(word, doclist))

# This is a dictionary with inside associated to every word in dictionary (the one that matched indexes and words) 
# the number of documents it is in on the 30.000 of the database, so we can easily build a idf database 
# and so compute with low cost the tf-idf.

ncontain = {}
for i in diction:
    refer = diction[i]
    #print(i)
    ncontain[i] = len(diction2[refer])
with open('ncontain.json', 'w') as fp:
    json.dump(ncontain, fp)
with open(r"ncontain.json", 'r') as file:
    data = file.read()
ncontain = json.loads(data) #first dict with every word and a unique value

# idfdict is the dictionary that if you select a word will give you its idf. We save it as a json file.

import math
idfdict = {}
for i in ncontain:
    idfdict[i]=math.log(30000 / ncontain[i])
with open('idfdict.json', 'w') as fp:
    json.dump(idfdict, fp)
with open(r"idfdict.json", 'r') as file:
    data = file.read()
idfdict = json.loads(data)

with open(r"idfdict.json", 'r') as file:
    data = file.read()
idfdict = json.loads(data)
#idfdict.keys()



# 2.2.1 Inverted Index

# Second dictionary with the tf-idf values
# We are ready to do very easily the dictionary with key : ([document, tf-idf]) because we already saved the idf in a dictioonary so the next code will be pretty fast in creating the dict. We save it a json file.

dictionar3 = {}
#length = 0
for i in range(30000):
    file = "Cleantsv/filmclean-"+str(i)+'.tsv'
    temp = []
    for j in Docum_and_words[i].split():
            if j not in temp:
                #dicus = {}
                code = diction[j]
                value = tf(j, Docum_and_words[i].split())*idfdict[j]
                li = [file, value]
                if code not in dictionar3:
                    #dicus[file]=value
                    dictionar3[code] = [li]
                else:   
                    #dicus[file]=value
                    dictionar3[code].append(li)
                temp.append(j)
import json

with open('Dictionary2.json', 'w') as fp:
    json.dump(dictionar3, fp)



# Now we import the files we need and prepare the code for the search engine2

import pandas as pd
import json
with open(r"dicturls.json", 'r') as file:
    data = file.read()
dicturls = json.loads(data) 
with open(r"Dictionary.json", 'r') as file:
    data = file.read()
diction = json.loads(data) #first dict with every word and a unique value
with open(r"Dictionary1.json", 'r') as file:
    data = file.read()
diction2 = json.loads(data)#first inverted dict with number and list of document with a word that has that number in diction
with open(r"ncontain.json", 'r') as file:
    data = file.read()
ncontain = json.loads(data) #dict with number of times a word appear in all the cod
with open(r"idfdict.json", 'r') as file:
    data = file.read()
idfdict = json.loads(data) #dict with the idf for every word
with open(r"Dictionary2.json", 'r') as file:
    data = file.read()
diction3 = json.loads(data) #second inverted dictionary wit doc and tfidf for eevry word
import math

#We prepare the code for the search engine.
# Here there are the functions to easily compute the cosine similarity given two vectors.

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
from scipy.spatial.distance import cosine

def simple_dot(a, b):
    dsum = 0.
    for ((idx,), val) in np.ndenumerate(a):
        dsum += float(val) * float(b[idx])
    return dsum

def l2_norm(a):
    return math.sqrt(np.dot(a, a))

def cosine_similarity(a, b):
    return np.dot(a,b) / (l2_norm(a)* l2_norm(b))
np.dot([1,2],[3,4])


# We remind that Docume_and_words is a list with inside every intro-plot(preprocessed) for every document, so we can just accees to it for my research, next cell is just a reminder of the preprocess function..

import io 
import nltk
import csv
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 
from nltk.stem import PorterStemmer 

 
ps = PorterStemmer() 
#the fuction preprocess the string as asked in the hmk
def preprocess(sentence):
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [ps.stem(w) for w in tokens if not w in stopwords.words('english')]
    return " ".join(filtered_words)


# 2.2.2 Executing the query

# Now we build the search engine2. The heap sorting is in the 'cossim' list that will have all the possible values of cosine similarity we have found for the query. We will print the dataframe with the best 20 results.

#We define the function to receive the dataset, given an input
import heapq as hq
def tf(word, doc):
    return doc.count(word) / len(doc)
y = list(input().split())
def searchengine2(y):
    if not y:
        return print("Error: string not found!")
    for i in range(len(y)):
        y[i]= preprocess(str(y[i]))
    #Now I tranform the list of input in a list of the codes in the dictiionary based on the input
    yfinal=[] #use this because some words have no match in the vocabulary
    for i in range(len(y)):
        if y[i] in diction:
            yfinal.append(diction[y[i]])
    #Now I have to search inside the lists of values from the keys i foundb and see if some films match in the various keys.
    if  len(yfinal)<len(y):
        return print('There are no movies, in our database, that match all the words you typed. ')
    else:
        starting_values = diction2[yfinal[0]]
        final_values = starting_values.copy()
        for codes in range(1,len(yfinal)):
            new = []
            for film in final_values:
                if film in diction2[yfinal[codes]]:
                    new.append(film)
            final_values = new
        megaDataframe = pd.DataFrame(columns = ['Title', 'Intro', 'Url', 'Similarity'])
        if not final_values:
            return print("No movies matched our query, we need more movies to compare")
        else:  
            lstofl = []
            #here there is a lstofl that has vectors associated with every document, in order of final_values
            for film in final_values:
                item = []
                for code in yfinal:
                    for value in diction3[code]:
                        if film in value:
                            item.append(value[1])
                            break
                lstofl.append(item) 
            #Now we have to create the inquiry vector and get the cosine similarity of beetween it and every component of lstofl 
            query = []
            for i in y:
                query.append(tf(i,y)*idfdict[i])
            cossim = []
            for vector in lstofl:
                cossim.append(cosine_similarity(query, vector))
        #the cosine similarity in order of appereance of my document
            dict_sim = {}
            for indx in range(len(cossim)):
                sim = cossim[indx]
                if sim not in dict_sim:
                    dict_sim[sim]=[final_values[indx]]
                else:
                    dict_sim[sim].append(final_values[indx])
            Peak = 20 #the maximum number of rows I will plot
            #heap algorithm
            cossim = list(set(cossim))
            to_select = hq.nlargest(Peak, cossim)   
            k=0
            #Now i have the name key(cossim) and values(docum) and I have to take the first 15 of them.
            for i in to_select:
                if(k<Peak):
                    for document in dict_sim[i]:
                            if(k>Peak):
                                return megaDataframe
                            totakeurl = document.replace('Cleantsv/filmclean-','')
                            totakeurl = str(int(totakeurl.replace('.tsv', '')))
                            url = dicturls[totakeurl]
                            Similarity = format(i, '.10g')
                            temporary = pd.read_csv('Tsvfiles/'+'film'+(totakeurl)+'.tsv',delimiter='\t' )
                            title = temporary['title'][0]
                            intro =  temporary['intro'][0].replace('\r\n','')
                            new_row = [title, intro, url, Similarity]
                            megaDataframe.loc[k]=new_row
                            k=k+1
            return  megaDataframe
A = searchengine2(y)


#Let's see some examples! As we use simple strings and with not many repetitions it's possible more than one value will be one, as we will put a more difficult query we will have lower similarity probably.

y = list(input().split())
searchengine2(y)
