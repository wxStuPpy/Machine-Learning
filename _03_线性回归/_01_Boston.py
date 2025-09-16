import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

data_url = 'http://lib.stat.cmu.edu/datasets/boston'
raw_df = pd.read_csv(data_url, sep=r'\s+', skiprows=22, header=None)

data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

x_train, x_test, y_train, y_test = train_test_split(
    data, target,
    test_size=0.2,
    random_state=22
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = SGDRegressor(
    loss='squared_error',  # 平方损失（适合回归）
    learning_rate='constant',  # 恒定学习率
    eta0=0.01,  # 初始学习率
    random_state=22  # 固定随机种子，确保结果可复现
)
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
mse = mean_squared_error(y_test, y_predict)
print(f"测试集均方误差（MSE）: {mse:.4f}")
