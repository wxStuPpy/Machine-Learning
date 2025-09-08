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



data = {
    'district': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'view_num': [5, 15, 8, 20, 12, 7, 25, 18],
    'price': [100, 150, 120, 200, 130, 110, 180, 170],
    'area': [50, 60, 55, 80, 65, 58, 75, 70]
}
df1 = pd.DataFrame(data)
print(df1)


# 按照 district 分组，做多个聚合统计
agg_result = df1.groupby('district').agg(
    avg_price=('price', 'mean'),        # 平均房价
    max_price=('price', 'max'),         # 最高房价
    min_view=('view_num', 'min'),       # 最少看房人数
    total_view=('view_num', 'sum'),     # 总看房人数
    house_count=('price', 'count'),     # 房源数量
    avg_area=('area', 'mean'),          # 平均面积
    price_per_sqm=('price', lambda x: (x.sum() / df1.loc[x.index, 'area'].sum()))  # 每平米均价
)
print(agg_result)

