# 导入库
import matplotlib.pyplot as plt   # 绘图库，通常用 plt 作为别名（你原来写成 matplotlib as plt 会报错）
import pandas as pd               # 数据分析库

# -------------------------------
# 读取 CSV/文本文件
# -------------------------------
df = pd.read_csv('name.csv')    # 读取文本/CSV文件，生成 DataFrame
print(df.head(2))                 # 查看前两行数据，方便检查文件读取情况

# -------------------------------
# 取出某一列数据
# -------------------------------
name = df['name']                 # 取 DataFrame 的 'name' 列，返回 Series
# name = df.name                  # 等效写法
print(name)                       # 打印 name 列
print('*'*20)                     # 分割线，方便阅读输出

# -------------------------------
# 统计各值出现的次数
# -------------------------------
print(name.value_counts())         # 返回 Series，索引是不同的 name 值，值是计数
print('*'*20)

# -------------------------------
# 统计行数和维度
# -------------------------------
print(name.count())               # 统计非空值数量（有效数据的个数）
print(name.shape)                 # 返回 Series 的维度，元组形式，例如 (行数,)
print('*'*20)

# -------------------------------
# 对 'age' 列进行描述性统计
# -------------------------------
print(df['age'].describe())       # 返回统计信息：count, mean, std, min, 25%, 50%, 75%, max
