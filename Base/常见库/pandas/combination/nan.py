import pandas as pd
import numpy as np

# 构造 DataFrame，包含缺失值
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'age': [20, np.nan, 22, 21, np.nan, 23],
    'score': [88, 92, np.nan, 85, 90, np.nan],
    'city': ['Beijing', 'Shanghai', None, 'Shenzhen', 'Chengdu', None]
})

print("原始数据：")
print(df)

# ==================== 1. 查看缺失值 ====================
print("\n缺失值布尔矩阵：")
print(df.isnull())

print("\n每列缺失值数量：")
print(df.isnull().sum())

print("\n是否存在缺失值：")
print(df.isnull().values.any())

# ==================== 2. 删除缺失值 ====================
print("\n删除包含缺失值的行：")
print(df.dropna())

print("\n删除包含缺失值的列：")
print(df.dropna(axis=1))

# ==================== 3. 填充缺失值（线性/非线性） ====================
# 线性填充：使用前一个值填充（ffill），或后一个值填充（bfill）
print("\n线性填充 ffill（前向填充）：")
print(df.fillna(method='ffill'))

print("\n线性填充 bfill（后向填充）：")
print(df.fillna(method='bfill'))

# 非线性填充：使用均值、中位数、众数等
print("\n非线性填充：均值填充")
print(df.fillna(df.mean(numeric_only=True)))

print("\n非线性填充：中位数填充")
print(df.fillna(df.median(numeric_only=True)))

print("\n非线性填充：众数填充")
print(df.fillna(df.mode().iloc[0]))  # 取第一行众数

# 指定值填充
print("\n指定值填充（缺失填 -1）：")
print(df.fillna(-1))
