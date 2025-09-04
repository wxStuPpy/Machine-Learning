import numpy as np
from sklearn.linear_model import LinearRegression
import  joblib


def dm_01_regression_predict():
    # 特征数据 X（二维，每行是一个样本，每列是一个特征）
    x = [[80, 86],
         [82, 80],
         [85, 78],
         [90, 90],
         [86, 82],
         [82, 90],
         [78, 80],
         [92, 94]]

    # 目标值 y（一维，每个样本对应一个结果）
    y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]

    # 转换为 numpy 数组（更标准）
    X = np.array(x)
    Y = np.array(y)

    # 实例化模型
    estimator = LinearRegression()
    print('estimator:', estimator)

    # 模型训练
    estimator.fit(X, Y)
    print('coef:', estimator.coef_)           # 回归系数
    print('intercept:', estimator.intercept_) # 截距

    # 预测新数据
    mypredict = estimator.predict([[90, 80]])
    print('mypredict:', mypredict)

    # 模型的拟合优度 R^2
    print("R^2 score:", estimator.score(X, Y))

    #模型保存
    joblib.dump(estimator,'../modules/LinearRegression.pkl')

    #模型使用
    estimator1=joblib.load('../modules/LinearRegression.pkl')
    print(estimator1.predict([[90, 80]]))

if __name__ == "__main__":
    dm_01_regression_predict()
