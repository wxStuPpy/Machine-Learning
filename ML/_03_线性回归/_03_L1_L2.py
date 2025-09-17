import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso, Ridge
import warnings
warnings.filterwarnings('ignore')
# 1. 构造数据
np.random.seed(42)
n_samples, n_features = 50, 10
X = np.random.randn(n_samples, n_features)

# 真实系数：只有前 2 个特征有用，其余都是 0
true_coef = np.zeros(n_features)
true_coef[0:2] = [3, -2]
y = X @ true_coef + np.random.normal(0, 0.5, size=n_samples)

# 2. 拟合普通线性回归
lr = LinearRegression().fit(X, y)

# 3. 拟合 Ridge（L2 正则化）
ridge = Ridge(alpha=1.0).fit(X, y)

# 4. 拟合 Lasso（L1 正则化）
lasso = Lasso(alpha=0.1).fit(X, y)

# 5. 打印系数
print("真实系数:      ", true_coef)
print("普通回归系数:  ", np.round(lr.coef_, 3))
print("Ridge 回归系数:", np.round(ridge.coef_, 3))
print("Lasso 回归系数:", np.round(lasso.coef_, 3))

# 6. 可视化对比
plt.figure(figsize=(10,6))
plt.plot(true_coef, "o-", label="real coef", linewidth=2)
plt.plot(lr.coef_, "o-", label="ordinary", linewidth=2)
plt.plot(ridge.coef_, "o-", label="Ridge (L2)", linewidth=2)
plt.plot(lasso.coef_, "o-", label="Lasso (L1)", linewidth=2)
plt.axhline(0, color="gray", linestyle="--")
plt.xlabel("feature")
plt.ylabel("coef")
plt.title("Lasso vs Ridge")
plt.legend()
plt.show()
