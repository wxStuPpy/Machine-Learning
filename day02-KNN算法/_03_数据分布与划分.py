import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def show_iris():
    iris = load_iris()
    print(iris.feature_names)

    d = pd.DataFrame(data=iris['data'], columns=iris.feature_names)
    d['label']=iris['target']
    d['label']=d['label'].map({0:'setosa',1:'versicolor',2:'virginca'})
    col1='sepal length (cm)'
    col2='petal width (cm)'

    sns.lmplot(data=d,x=col1,y=col2,hue='label')
    plt.xlabel(col1)
    plt.ylabel(col2)
    # 添加网格线，调整图例
    plt.grid(linestyle='--', alpha=0.6)
    plt.legend(title='Species', loc='best')
    plt.title('iris')
    plt.show()

def traintest_split():
    iris = load_iris()
    x_train,x_test,y_train,y_test=train_test_split(iris['data'],iris['target']
                                                   ,test_size=0.2,random_state=1)
    print(len(iris['data']))
    print(f'x_train {len(x_train)}')
    print(f'x_test {len(x_test)}')


if __name__ == '__main__':
    show_iris()
    traintest_split()