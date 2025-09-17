
---

# 1️⃣ MAE（Mean Absolute Error，平均绝对误差）

### 定义

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

* $y_i$：真实值
* $\hat{y}_i$：预测值
* $n$：样本数量

### 特点

* 衡量预测值与真实值的平均差距
* 对异常值（outliers）不敏感，因为不平方
* 单位和原数据相同，直观

---

# 2️⃣ MSE（Mean Squared Error，均方误差）

### 定义

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

### 特点

* 对预测误差进行平方 → 放大大误差的影响
* 对异常值敏感
* 单位是原数据单位的平方，不容易直观理解

---

# 3️⃣ RMSE（Root Mean Squared Error，均方根误差）

### 定义

$$
\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

### 特点

* 对异常值敏感，和 MSE 类似
* 单位和原数据相同 → 比 MSE 更直观
* 常用在回归问题中做模型比较

---

# 4️⃣ 对比总结表

| 指标   | 公式                                         | 是否平方误差          | 对异常值敏感 | 单位      |   |       |
| ---- | ------------------------------------------ | --------------- | ------ | ------- | - | ----- |
| MAE  | ( \frac{1}{n}\sum                          | y\_i-\hat{y}\_i | )      | 否       | 否 | 原数据单位 |
| MSE  | $\frac{1}{n}\sum (y_i-\hat{y}_i)^2$        | 是               | 高      | 原数据单位平方 |   |       |
| RMSE | $\sqrt{\frac{1}{n}\sum (y_i-\hat{y}_i)^2}$ | 是               | 高      | 原数据单位   |   |       |

---

# 5️⃣ 使用场景

* **MAE**：想平均衡量误差，且希望对异常值不敏感
* **MSE / RMSE**：希望更关注大误差的情况，RMSE比MSE单位直观

---

💡 **Python 示例**：

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
```

---


