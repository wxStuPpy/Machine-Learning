import pandas as pd
from datetime import datetime

# 构造几个时间对象
t1 = pd.Timestamp(year=2025, month=5, day=15)    # Pandas Timestamp
t2 = pd.to_datetime('2025-6-12')                 # 字符串转 Timestamp
t3 = datetime(2023, 2, 2, 11, 33, 44)            # Python datetime

print("t1 (Timestamp):", t1, type(t1))
print("t2 (Timestamp):", t2, type(t2))
print("t3 (datetime):", t3, type(t3))
print("="*40)

df = pd.read_csv("students.csv", parse_dates=["date"])
print("读取后的 DataFrame：")
print(df)

print("\n列类型信息：")
print(df.dtypes)   # 可以看到 date 列是 datetime64[ns] 类型
