import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import jieba
import os

data_df=pd.read_csv('./data.csv',encoding='utf-8-sig')
data_df['label']=data_df['label'].map({'positive':0,'negative':1,'neutral':2})

stopwords=[]
with open('./stopwords.txt','r',encoding='utf-8-sig') as f:
    lines=f.readline()
    stopwords=[line.strip() for line in lines]

stopwords=list(set(stopwords))


