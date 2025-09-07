import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 创建 Series 对象
# -------------------------------
s1 = pd.Series(
    data=[1, 3, 5, 7, 11, 9],          # 数据
    index=['A', 'B', 'C', 'D', 'E', 'F']  # 自定义索引
)
print(s1)  # 打印整个 Series

# -------------------------------
# 基本属性和方法示例（已注释）
# -------------------------------
# print(len(s1))            # Series 的长度（元素个数）
# print(s1.size)            # Series 的大小，等于 len(s1)
# print(s1.head(n=3))       # 查看前 3 个元素
# print(s1.tail(n=2))       # 查看后 2 个元素
# print(s1.to_list())       # 转换为 Python 列表
# print(s1.to_frame())      # 转换为 DataFrame，列名默认为 0

# print(s1.describe())      # 描述统计信息（count, mean, std, min, 25%, 50%, 75%, max）
# print(s1.max())           # 最大值
# print(s1.mean())          # 平均值
# print(s1.std())           # 标准差（默认 ddof=1，样本标准差）

# print(s1.drop_duplicates()) # 删除重复值，返回新的 Series
# print(s1.unique())          # 返回 Series 中唯一值的数组

# -------------------------------
# 排序操作
# -------------------------------
print(s1.sort_values(ascending=False))  # 按值降序排序
print(s1.sort_index())                  # 按索引升序排序

# -------------------------------
# 统计值计数
# -------------------------------
print(s1.value_counts())  # 每个值出现的次数，返回 Series，索引是值，值是计数

# -------------------------------
# 绘制直方图
# -------------------------------
s1.hist()     # 绘制 Series 的直方图（柱状显示每个值的频率）
plt.show()    # 显示图形窗口（脚本中必须调用）
