import seaborn as sns
import matplotlib.pyplot as plt

data_list = sns.load_dataset('tips')

print(data_list.head(5))

# 绘制直方图，展示总账单（total_bill）的分布情况
plt.figure(figsize=(16, 8))                 # 设置画布大小为 16x8
plt.hist(x=data_list['total_bill'], bins=10) # 绘制直方图，total_bill 分 10 个区间
plt.title('consume')                        # 设置图表标题
plt.grid()                                  # 添加网格线，便于观察分布
plt.show()                                  # 显示图表
