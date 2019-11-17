#!/usr/bin/env python
# coding: utf-8

# ### Question3 
# 
# 

# ### Define a new score!
# 

# In[ ]:


import pickle
import pandas as pd


# get query from user
query = str(input("please your request:"))
query = query.split(" ")

# open the Vocabulary for reading
fileObject = open('path of vocabulary', 'rb')  
vocab=pickle.load(f)
vocab = vocab.split("\n")  

#searching in vocabulary for finding word
terms_list=[]
for w in query:
    # if each word of query is in the vocabulary
    if w in vocab: 
        t_id = vocabulary.index(word)
        terms_list.append(t_id)
                
# find related documents
documents=[]
for i in terms_list:
    if i in dictionary:
        documents.append(dictionary[i])

fileObject.close()


#put result in data frame and show to 10 
output_df = pd.DataFrame(columns=['Title','Intro','Url','similarity'])
try:
    for j in documents:
        output_df=output_df.append({'Title': ,'Intro': ,'Url': ,'similarity': }, ignore_index=True)

    output_df=output_df.sort_values(by='similarity', ascending=False)
    output_df.head(10)

except:
    print('Not found any movies')

