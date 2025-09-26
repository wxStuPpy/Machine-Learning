from sklearn.feature_selection import VarianceThreshold
import pandas as pd


X = pd.DataFrame({
    'feature1': [1, 1, 1, 1, 1],   # 方差为0
    'feature2': [1, 2, 3, 4, 5],   # 方差大
    'feature3': [0, 0, 1, 0, 0]    # 方差小
})

# 定义低方差阈值，例如0.1
selector = VarianceThreshold(threshold=0.1)

# 进行降维
X_reduced = selector.fit_transform(X)

print("原始特征:", X.columns.tolist())
print("保留特征后的数据:\n", X_reduced)
print("保留的特征索引:", selector.get_support(indices=True))
