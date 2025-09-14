
---

### 1. `fit`

```python
scaler.fit(x_train)
```

* **作用**：计算出数据的统计量（比如均值、方差、最大值、最小值等，具体看是什么方法）。
* **结果**：把这些统计量 **保存到 scaler 对象里**。
* **不会改变原始数据**。
* 类似于“学习参数”。

例子：
`StandardScaler.fit` 会计算每一列特征的：

* 均值 μ
* 标准差 σ

并保存下来。

---

### 2. `transform`

```python
x_test_scaled = scaler.transform(x_test)
```

* **作用**：用 `fit` 得到的统计量（μ 和 σ），对数据进行转换。
* **不会重新计算统计量**，只用已有的。
* 用在测试集、新样本、验证集。

例子：
`(x - μ) / σ`

---

### 3. `fit_transform`

```python
x_train_scaled = scaler.fit_transform(x_train)
```

* 等价于：先 `fit(x_train)` 再 `transform(x_train)`。
* 一步完成 **学习参数 + 转换数据**。
* 常用于训练集。

---

### 🚦 为什么不能对测试集用 `fit_transform`？

* 如果你对测试集也 `fit_transform`，那就是重新计算了均值和方差。
* 测试集的信息会“泄露”到模型里（数据穿越）。
* 正确做法：训练集 `fit_transform`，测试集 `transform`。

---

✅ **总结一句话**：

* `fit`：学参数（只保存，不改变数据）。
* `transform`：用学到的参数来变换数据。
* `fit_transform`：训练集的一站式操作。

---
