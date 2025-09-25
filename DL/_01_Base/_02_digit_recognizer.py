import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

from common.functions import softmax,sigmoid
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib

def get_data():
    data=pd.read_csv('../data/train.csv')
    X=data.drop(['label'],axis=1);
    y=data['label']

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
    scaler = MinMaxScaler()
    X_train=scaler.fit_transform(X_train)
    X_test=scaler.transform(X_test)

    return X_test,y_test

def init_network():
    network=joblib.load('../data/nn_sample')
    return network

def forward(network, x):
    w1, b1 = network['W1'], network['b1']
    w2, b2 = network['W2'], network['b2']
    w3, b3 = network['W3'], network['b3']

    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)
    return y

x,y=get_data()
network = init_network()
y_probe=forward(network, x)
y_pred=np.argmax(y_probe,axis=1)
accuracy_cnt=np.sum(y_pred==y)
print(accuracy_cnt)
