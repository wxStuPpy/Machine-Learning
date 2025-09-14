import pandas as pd
import numpy as np
import time
from pyecharts.charts import Bar3D
from pyecharts.commons.utils import JsCode
import pyecharts.options as opts
from sqlalchemy import create_engine

# -----------------------------
# 设置 pandas 显示选项
# -----------------------------
pd.set_option('display.width', None)         # 自动适配屏幕宽度，避免换行显示
pd.set_option('display.max_columns', None)   # 显示所有列，不被省略

# -----------------------------
# 1. 数据读取
# -----------------------------
df1 = pd.read_csv('data1.csv')  # 读取第一个 CSV 文件
df2 = pd.read_csv('data2.csv')  # 读取第二个 CSV 文件

# 将 'Date' 列转换为 datetime 类型，方便后续时间计算
df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d')
df2['Date'] = pd.to_datetime(df2['Date'], format='%Y-%m-%d')

# -----------------------------
# 1.1 数据合并
# -----------------------------
merge_data = pd.concat([df1, df2])  # 将两个数据表纵向合并（堆叠行）

# -----------------------------
# 2. 数据预处理
# -----------------------------

# 2.1 删除空值
merge_data.dropna(inplace=True)

# 2.2 筛选订单金额大于 100 的数据（去除异常值/小额订单）
merge_data = merge_data[merge_data['Order Amount'] > 100]

# 2.3 统一会员 ID 格式（转字符串，避免不同类型合并时冲突）
merge_data['Member ID'] = merge_data['Member ID'].astype(int).astype(str)

# 2.4 计算最大日期（整个数据集的最大订单日期）
merge_data['max_year'] = merge_data['Date'].max()

# 2.5 计算每条记录距离最大日期的间隔（天数）
merge_data['interval'] = merge_data['max_year'] - merge_data['Date']  # 结果是 timedelta 类型
merge_data['interval'] = merge_data['interval'].transform(lambda x: x.days)

# 删除中间列
merge_data.drop('max_year', axis=1, inplace=True)

# 2.6 提取年份，方便后续分年度分析
merge_data['year'] = merge_data['Date'].dt.year

# -----------------------------
# 3. RFM 基础构建
# -----------------------------
rfm_gb = merge_data.groupby(['Member ID', 'year'], as_index=False).agg({
    'interval': 'min',           # R（最近一次消费距离今天的天数，越小越好）
    'Order Number': 'count',     # F（消费频率，订单数）
    'Order Amount': 'sum'        # M（消费金额，总和）
})

# 修改列名，统一为 RFM
rfm_gb.columns = ['Member ID', 'year', 'r', 'f', 'm']

# -----------------------------
# 4. RFM 分箱与打分
# -----------------------------

# 4.1 手动设置分箱区间（根据 describe() 统计结果设置）
r_bins = [-1, 274, 851.5, 1242]                # R 越小分数越高
f_bins = [0, 4, 7.5, 16]                       # F 越大分数越高
m_bins = [3009, 16592, 38053, 67500]           # M 越大分数越高

# 4.2 使用 pd.cut 将 R/F/M 分段打分
rfm_gb['r_score'] = pd.cut(
    rfm_gb['r'], bins=r_bins,
    labels=[i for i in range(len(r_bins) - 1, 0, -1)]  # R 越小分数越高，倒序打分
)
rfm_gb['f_score'] = pd.cut(
    rfm_gb['f'], bins=f_bins,
    labels=[i for i in range(1, len(f_bins), 1)]       # F 越大分数越高
)
rfm_gb['m_score'] = pd.cut(
    rfm_gb['m'], bins=m_bins,
    labels=[i + 1 for i in range(len(m_bins) - 1)]     # M 越大分数越高
)

# 4.3 将 R/F/M 打分转为字符串，方便拼接
rfm_gb['r_score'] = rfm_gb['r_score'].astype(np.str_)
rfm_gb['f_score'] = rfm_gb['f_score'].astype(np.str_)
rfm_gb['m_score'] = rfm_gb['m_score'].astype(np.str_)

# 4.4 拼接为 RFM Group（如 "321" 表示 r=3, f=2, m=1）
rfm_gb['rfm_group'] = rfm_gb['r_score'] + rfm_gb['f_score'] + rfm_gb['m_score']
rfm_gb['rfm_group'] = rfm_gb['rfm_group'].astype(np.int_)

# -----------------------------
# 5. RFM 分组可视化准备
# -----------------------------

# 5.1 按 rfm_group & year 分组，统计会员人数
display_data = rfm_gb.groupby(['rfm_group', 'year'], as_index=False)['Member ID'].count()
display_data.columns = ['rfm_group', 'year', 'count']

# 5.2 设置颜色池（蓝 → 红渐变，用于区分数量高低）
range_color = [
    "#313695","#4575b4","#74add1","#abd9e9",
    "#e0f3f8","#ffffbf","#fee090","#fdae61",
    "#f46d43","#d73027","#a50026"
]

range_max = int(display_data['count'].max())  # 最大值作为颜色映射上限

# -----------------------------
# 6. 绘制 3D 柱状图（RFM 可视化）
# -----------------------------
c = (
    Bar3D()
    .add(
        "",
        [d.tolist() for d in display_data.values],   # 转为 list 作为输入
        xaxis3d_opts=opts.Axis3DOpts(type_='category', name='rfm_group'),
        yaxis3d_opts=opts.Axis3DOpts(type_='category', name='year'),
        zaxis3d_opts=opts.Axis3DOpts(type_='value', name='count')
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=range_max, range_color=range_color),  # 设置颜色映射
        title_opts=opts.TitleOpts(title='RFM 分析 3D 可视化')                       # 标题
    )
)

# 6.1 输出到本地 HTML 文件，浏览器打开即可查看
c.render()
#6.2导入到mysql
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/rfm_db?charset=utf8')
rfm_gb.to_sql('rfm_table',engine,index=False,if_exists='append')
print(pd.read_sql('show tables', engine))
