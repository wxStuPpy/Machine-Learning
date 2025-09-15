import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  StandardScaler
from sklearn.neighbors import KNeighborsClassifier


def demo():
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target']
                                                        , test_size=0.2, random_state=1)
    #标准化
    scaler = StandardScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)
    
    #模型训练
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(x_train,y_train)

    #模型预测
    x=[[5.1,3.5,1.4,0.2],[4.6,3.3,1.1,0.1]]
    x=scaler.transform(x)
    print(classifier.predict(x))
    print(classifier.predict_proba(x))

    #模型评估
    print(f'测试集:{classifier.score(x_test, y_test)}')

    #使用预测结果
    y_predict = classifier.predict(x_test)
    print(accuracy_score(y_test, y_predict))

if __name__ == '__main__':
    demo()