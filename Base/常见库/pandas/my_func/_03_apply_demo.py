import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': [np.nan,'li','wang'],
    'age': [1,np.nan,np.nan]
})
print("原始数据：")
print(df)

# 定义函数：计算 Series 中缺失值的数量
def null_sum(vec):
    return pd.isnull(vec).sum()

def null_percent(vec):
    return null_sum(vec)/vec.size

# 对每一列应用
print("\n每列缺失值数量：")
print(df.apply(null_sum))

print('\n缺失占比')
print(df.apply(null_percent))