import pandas as pd

# 读取数据
df = pd.read_csv("students.csv")
print("原始数据：")
print(df)

# 按 name 分组，计算组内平均分，并返回每行对应的平均分
df['group_mean'] = df.groupby('name')['score'].transform('mean')

# 组内中心化：每个 score 减去组平均分
df['score_centered'] = df['score'] - df['group_mean']

print("\n分组转换结果：")
print(df)
