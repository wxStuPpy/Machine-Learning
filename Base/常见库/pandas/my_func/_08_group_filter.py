import pandas as pd

# 读取数据
df = pd.read_csv("students.csv")
print("原始数据：")
print(df)

print(df.groupby('name').filter(lambda x: x['score'].mean() > 80))
