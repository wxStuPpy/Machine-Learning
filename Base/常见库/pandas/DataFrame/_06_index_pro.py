import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('name.csv')
print("原始 DataFrame：")
print(df)

# ========== 指定行和列 ==========
# loc：基于标签（行索引值 + 列名）
print("\nloc 按行索引值 + 列名 取数据：")
print(df.loc[[0, 1, 2], ['name', 'age']])  # 取第0/1/2行，并选择 'name' 和 'age' 两列

# iloc：基于位置（行号 + 列号）
print("\niloc 按行号 + 列号 取数据：")
print(df.iloc[[0, 2, 4], [0, 1, 2]])  # 取第0/2/4行，取第0/1/2列

# ========== 取所有行的部分列 ==========
print("\nloc 取所有行 + 指定列：")
print(df.loc[:, ['name', 'age']])  # 所有行，只要 'name' 和 'age' 列

print("\niloc 取所有行 + 指定列号：")
print(df.iloc[:, [0, 1, 2]])  # 所有行，取第0/1/2列

# ========== range 的用法 ==========
print("\niloc + range 取前3列：")
print(df.iloc[:, range(3)])  # 所有行，取第0~2列

print("\niloc + range 步长取列：")
print(df.iloc[:2, range(0, 4, 2)])  # 前2行，取第0列和第2列

print("\niloc 切片 取行列（带步长）：")
print(df.iloc[:1, 1:4:2])  # 第0行（前1行），取第1~3列，步长为2，即取第1列和第3列
