import numpy as np
from sklearn.preprocessing import  MinMaxScaler

def func():
    x=[[1,20,300],[2,19,391],[4,10,209]]
    scaler = MinMaxScaler()
    x=scaler.fit_transform(x)
    print(x)

if __name__=='__main__':
    func()
