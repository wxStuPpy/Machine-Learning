import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

digits = load_digits()
df = pd.DataFrame(digits.data, columns=[f'pixel_{i}' for i in range(digits.data.shape[1])])
df.insert(0, 'target', digits.target)

x_train, x_test, y_train, y_test = train_test_split(
    df.iloc[:, 1:],  # 特征
    df['target'],  # 标签
    stratify=df['target'],
    test_size=0.2,
    random_state=22
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

estimator = KNeighborsClassifier(n_neighbors=3)
param_grid = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8]}
estimator = GridSearchCV(param_grid=param_grid, cv=5, estimator=estimator)
estimator.fit(x_train, y_train)
print(estimator.best_score_)
print(estimator.best_params_)

y_predict = estimator.predict(x_test)
print("测试集准确率:", accuracy_score(y_predict, y_test))
best_model = estimator.best_estimator_
joblib.dump(best_model, "../modules/knn_best.pkl")  # 保存最佳模型

x_test_images = x_test.reshape(-1, 8, 8)
plt.figure(figsize=(12, 6))
for i in range(20):  # 显示前 20 张图片
    plt.subplot(4, 5, i + 1)
    plt.imshow(x_test_images[i], cmap='gray')
    plt.title(f'True:{y_test.values[i]}\nPred:{y_predict[i]}')
    plt.axis('off')
plt.tight_layout()
plt.show()
