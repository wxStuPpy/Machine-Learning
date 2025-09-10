import pandas as pd

t1 = pd.Timestamp(year=2025, month=5, day=15, hour=14, minute=30, second=45)
print("t1:", t1)

# 1️⃣ 获取日期和时间的各个组成部分
print("年:", t1.year)        # 2025
print("月:", t1.month)       # 5
print("日:", t1.day)         # 15
print("小时:", t1.hour)      # 14
print("分钟:", t1.minute)    # 30
print("秒:", t1.second)      # 45

# 2️⃣ 常见日期属性
print("星期几 (0=周一):", t1.dayofweek)    # 3 (周四)
print("星期几 (1=周日):", t1.isoweekday()) # 4 (周四)
print("一年中的第几天:", t1.dayofyear)     # 135
print("季度:", t1.quarter)                # 2

# 3️⃣ 时间计算
print("加 10 天:", t1 + pd.Timedelta(days=10))
print("减 2 小时:", t1 - pd.Timedelta(hours=2))

# 4️⃣ 类型转换
print("转 datetime:", t1.to_pydatetime())
print("转字符串 (默认):", str(t1))
print("转字符串 (自定义格式):", t1.strftime("%Y/%m/%d %H:%M:%S"))

# 5️⃣ 比较操作
print("是否在 2025 年:", t1.year == 2025)
print("是否闰年:", t1.is_leap_year)
