import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. 加载数据
iris = load_iris()
X = iris.data
y = iris.target

# 只取前两类花
X = X[y != 2]
y = y[y != 2]

# 2. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. 标准化（逻辑回归依赖梯度，特征缩放能提高收敛效果）
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. 训练逻辑回归模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. 预测 & 评估
y_pred = model.predict(X_test)
print("测试集准确率:", accuracy_score(y_test, y_pred))
print("分类报告 :\n", classification_report(y_test, y_pred))
