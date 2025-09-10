import seaborn as sns
import matplotlib.pyplot as plt

# 加载 seaborn 自带的“餐厅小费”数据集
tips = sns.load_dataset('tips')

# 定义一个函数：把性别映射成颜色
def recode_sex(sex):
    if sex == 'Female':
        return 'red'
    else:
        return 'blue'

# 使用 transform，把 sex 列转化为颜色列
#tips['sex_color'] = tips['sex'].map({'Female': 'pink', 'Male': 'blue'})
tips['sex_color'] = tips['sex'].transform(recode_sex)  # 每个元素依次调用 recode_sex

print(tips.head(3))

# ================= 绘制散点图 =================
plt.figure(figsize=(8, 4))

plt.scatter(
    x=tips['total_bill'],     # X 轴：总消费金额
    y=tips['tip'],            # Y 轴：小费金额
    c=tips['sex_color'],      # 点的颜色：性别映射 (Female=red, Male=blue)
    s=tips['size'] * 10,      # 点的大小：用就餐人数（size）放大 10 倍
    alpha=0.5                 # 点的透明度：0.5 表示半透明
)

plt.title("Tips vs Total Bill")  # 图表标题
plt.xlabel("Total Bill")         # X 轴标题
plt.ylabel("Tip")                # Y 轴标题
plt.grid()                       # 显示网格
plt.show()
