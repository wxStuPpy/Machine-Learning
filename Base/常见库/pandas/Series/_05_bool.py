import pandas as pd

# 读取 CSV 文件，生成 DataFrame
df = pd.read_csv('name.csv')

# 构造一个布尔列表（True/False），用于布尔索引
# 注意：布尔列表的长度必须和 DataFrame 行数一致
bool_list = [True, False, True, False, True, False]

# 使用布尔列表筛选行：True 的行会被保留，False 的行会被过滤掉
print(df[bool_list])

# 取出 'age' 列，得到一个 Series
age = df['age']

# 计算 'age' 列的平均值
print(f'average age = {age.mean()}')

# 用布尔条件筛选：筛选出 'age' 大于平均值的行
print(df[age > age.mean()])

# 同样的条件筛选，但只取出 'age' 列本身
print(ages[ages > ages.mean()])
