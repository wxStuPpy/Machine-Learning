import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4,5,6],
    'b': [1,2,3]
})

print("原始数据：")
print(df)

# 普通向量化函数（Pandas 本身支持逐元素运算）
def func1(x, y):
    return (x + y) / 2

df['avg1'] = func1(df['a'], df['b'])

# 含条件判断的函数，需要显式向量化
def func2(x, y):
    if x == 2:
        return np.nan
    else:
        return (x + y) / 2

vec_func2 = np.vectorize(func2)
df['avg2'] = vec_func2(df['a'], df['b'])

print("\n计算结果：")
print(df)

@np.vectorize
def func3(x, y):
    if x == 2:
        return np.nan
    else:
        return (x + y) / 3

print("\n计算结果：")
print(func3(df['a'],df['b']))
