import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def get_data():
    data=pd.read_csv('../../data/train.csv')
    X=data.drop(['label'],axis=1)
    y=data['label']

    x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
    scaler = MinMaxScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)

    #将数据都转为np.array
    y_train=y_train.values
    y_test=y_test.values

    return x_train,x_test,y_train,y_test