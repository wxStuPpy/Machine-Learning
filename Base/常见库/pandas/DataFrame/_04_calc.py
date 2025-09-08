import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('name.csv')

print(df)
print((df * 2))
print((df + df[:3]))