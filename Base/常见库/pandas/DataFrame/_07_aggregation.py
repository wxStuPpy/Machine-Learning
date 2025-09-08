import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("students.csv")
print("原始数据：")
print(df)

# 按学生姓名分组，计算各项聚合统计
result = df.groupby('name').agg({
    'score': ['mean', 'max', 'min', 'std', 'count']  # 对成绩进行多种聚合
})

print("\n按姓名分组的聚合统计：")
print(result)

# 按学科分组，求平均成绩
subject_avg = df.groupby('subject')['score'].mean()
print("\n各学科平均分：")
print(subject_avg)

# 同时按姓名和学科分组，查看总分
sum_score = df.groupby(['name', 'subject'])['score'].sum()
print("\n按姓名+学科分组统计：")
print(sum_score)

# 按 score 分组，取平均，再画图
df.groupby('subject')['score'].mean().plot(kind='bar',figsize=(5,5))  # 画柱状图
plt.title("Average score")
plt.ylabel("Average value")
plt.show()
