import pandas as pd

# 示例1：生成指定起始和结束日期的每日日期
print("示例1：生成2023年1月的所有日期（每日）")
dates1 = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
print(dates1)
print()

# 示例2：生成指定数量的工作日（跳过周末）
print("示例2：从2023-10-01开始的5个工作日")
dates2 = pd.date_range(start='2023-10-01', periods=5, freq='B')
print(dates2)
print()

# 示例3：生成每2小时的时间序列
print("示例3：从指定时间开始，每2小时的10个时间点")
dates3 = pd.date_range(start='2023-01-01 08:00', periods=10, freq='2H')
print(dates3)
print()

# 示例4：生成每月最后一个工作日
print("示例4：2023年每个月的最后一个工作日")
dates4 = pd.date_range(start='2023-01-01', end='2023-12-31', freq='BM')
print(dates4)
print()

# 示例5：生成每3周的日期（以周一结束）
print("示例5：每3周，以周一为结束日")
dates5 = pd.date_range(start='2023-01-01', periods=5, freq='3W-MON')
print(dates5)
print()

# 示例6：生成每15分钟的时间序列
print("示例6：某天内每15分钟的时间点")
dates6 = pd.date_range(start='2023-05-01 09:00', end='2023-05-01 12:00', freq='15T')
print(dates6)
print()

# 示例7：生成季度末日期
print("示例7：2020-2023年的季度末日期")
dates7 = pd.date_range(start='2020-01-01', end='2023-12-31', freq='Q')
print(dates7)
