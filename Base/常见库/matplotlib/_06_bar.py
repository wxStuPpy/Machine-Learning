import pandas as pd
import matplotlib.pyplot as plt

# 创建示例数据：每个城市的人数
data = {
    'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu'],
    'count': [120, 95, 80, 60, 75]
}

df = pd.DataFrame(data)

# 设置 city 为索引，这样绘图时 x 轴是城市
df.set_index('city', inplace=True)

# 定义一个函数来绘制柱状图，演示 **kwargs
def plot_bar(dataframe, **kwargs):
    """
    dataframe: 传入一个 DataFrame，要求有一个数值列
    **kwargs: 额外传入的 matplotlib 参数，比如 color, figsize, title 等
    """
    ax = dataframe.plot(kind='bar', **kwargs)  # 这里 **kwargs 会传给 matplotlib
    ax.set_ylabel('Count')                     # 设置 y 轴标题
    ax.set_xlabel('City')                      # 设置 x 轴标题
    ax.set_title('City Counts')                # 图表标题
    plt.grid(True)                             # 显示网格
    plt.show()

# 调用函数，传递额外参数 color, figsize
plot_bar(df, color='skyblue', figsize=(8,4), legend=False)
