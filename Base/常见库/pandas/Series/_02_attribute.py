import numpy as np
import pandas as pd

# 读取 CSV 文件，并将 'id' 列作为行索引
df = pd.read_csv('./text.csv', index_col='id')
print(df.head())  # 打印前 5 行，方便查看数据结构

# -------------------------------
# 使用 loc 按索引取行
# -------------------------------
first_row = df.loc[1]  # 按行索引 '1' 获取第一行
print(first_row)       # 输出 Series，每个列名对应一个值
print(type(first_row)) # <class 'pandas.core.series.Series'>，单行被表示为 Series

# -------------------------------
# 使用 iloc 按行号取行
# -------------------------------
first_row = df.iloc[0] # 按行号 0 获取第一行
print(first_row)
print(type(first_row)) # <class 'pandas.core.series.Series'>

# -------------------------------
# 查看数据类型
# -------------------------------
print("整行 dtype:", first_row.dtype)       # 行的元素类型，如果混合类型通常是 object
print("age 列 dtype:", df['age'].dtype)     # 整列 dtype，例如 int64
print("name 的具体元素类型:", type(first_row['name']))  # 单个元素类型，例如 <class 'str'>

# -------------------------------
# Series 的属性示例
# -------------------------------
print("first_row.shape:", first_row.shape)  # Series 的形状，一维数组，长度等于列数
print("first_row.size:", first_row.size)    # 元素个数
print("first_row.values:", first_row.values) # Series 的值，返回 ndarray
print("first_row.index:", first_row.index)   # Series 的索引，即 DataFrame 的列名
