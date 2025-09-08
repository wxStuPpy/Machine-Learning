import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('name.csv')

print(df)
# 打印整个 DataFrame

print(df.head(n=2))
# 打印前 2 行数据

print(df.keys())
# 打印列名（Index(['id', 'name', 'age', 'score', 'city'], dtype='object')）

print(df.info())
# 打印 DataFrame 的整体信息（列数、行数、数据类型、内存占用等）

print(df.describe(exclude=['int', 'float']))
# 只描述非数值型数据（比如 object 类型：name 和 city）

print(df.describe(include='all'))
# 全部列的统计信息（数值列 + 类别列都会显示）

print(df.mean(numeric_only=True))
# 数值型列的平均值（id、age、score）

print(df[df['age'] > df['age'].mean()])
print(df['age'].mean())