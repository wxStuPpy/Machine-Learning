import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或者 ['SimSun'] 宋体
rcParams['axes.unicode_minus'] = False

# 1. 使用内置数据集（鸢尾花数据集）
iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")  # 小费数据集
flights = sns.load_dataset("flights")  # 航班数据集

# 创建一个 2x2 的子图布局
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 14))

# 2. 绘制散点图（带分类着色）
sns.scatterplot(
    data=iris,
    x="sepal_length",  # x轴：花萼长度
    y="sepal_width",  # y轴：花萼宽度
    hue="species",  # 按花的种类着色
    style="species",  # 按花的种类使用不同标记
    s=100,  # 点的大小
    ax=axes[0, 0]  # 指定子图位置
)
axes[0, 0].set_title("鸢尾花萼长度与宽度的关系", pad=10)
axes[0, 0].set_xlabel("花萼长度 (cm)")
axes[0, 0].set_ylabel("花萼宽度 (cm)")

# 3. 绘制柱状图（展示分类数据的平均值）
sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    errorbar=('ci', 68),  # 新版本替代写法
    ax=axes[0, 1]
)
axes[0, 1].set_title("不同日期的账单金额分布（按性别分组）", pad=10)
axes[0, 1].set_xlabel("星期")
axes[0, 1].set_ylabel("平均总账单金额 ($)")

# 4. 绘制箱线图（展示数据分布和离群点）
sns.boxplot(
    data=tips,
    x="time",  # x轴：用餐时间（午餐/晚餐）
    y="tip",  # y轴：小费金额
    hue="smoker",  # 按是否吸烟分组
    ax=axes[1, 0]
)
axes[1, 0].set_title("小费金额分布（按用餐时间和是否吸烟分组）", pad=10)
axes[1, 0].set_xlabel("用餐时间")
axes[1, 0].set_ylabel("小费金额 ($)")

# 5. 绘制热力图（展示数据相关性）
# 处理航班数据为矩阵形式
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(
    data=flights_pivot,
    annot=True,
    fmt="d",
    cmap="YlGnBu",
    linewidths=.5,
    ax=axes[1, 1]
)
axes[1, 1].set_title("不同年份和月份的航班乘客数量", pad=10)
axes[1, 1].set_xlabel("年份")
axes[1, 1].set_ylabel("月份")

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.show()
