import numpy as np
import pandas as pd

# 读取数据
df = pd.read_csv("students.csv")
print("原始数据：")
print(df)

# 定义平均值计算函数（只定义一次）
def my_mean(x):
    return x.mean()

# 按姓名分组计算成绩平均值
print("\n按姓名分组的成绩平均值：")
print(df.groupby(['name'], as_index=False)['score'].agg(my_mean))

# 自定义聚合函数：计算多种统计量
def complex_agg_dict(scores):
    return {
        'mean': scores.mean(),
        'max_min_diff': scores.max() - scores.min(),
        'std': scores.std(),
        'pass_rate': (scores >= 80).sum() / len(scores)
    }

# 应用复杂聚合函数
result = df.groupby('name', as_index=False)['score'].agg(complex_agg_dict)
print("\n按姓名分组的多种统计量：")
print(result)

# 定义平方计算函数
def func_mux(x):
    return x**2

# # 同时应用平均值和平方函数（使用已定义的my_mean，避免重名）
# result1 = df.groupby(['name'], as_index=False)['score'].agg([my_mean, func_mux])
# print("\n按姓名分组的平均值和平方值：")
# print(result1)
