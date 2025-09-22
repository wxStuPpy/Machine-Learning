import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import jieba

data_df=pd.read_csv('./data.csv',encoding='utf-8-sig')
data_df['label']=data_df['label'].map({'positive':0,'negative':1,'neutral':2})



