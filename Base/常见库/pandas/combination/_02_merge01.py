import pandas as pd

# 学生表
df_students = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Zhang', 'Wang', 'Li']
})

# 成绩表
df_scores = pd.DataFrame({
    'id': [1, 2, 4],   # 注意：这里加了一个 id=4，学生表中没有
    'score': [88, 92, 75]
})

# 默认 inner join（交集，只保留两边都有的 id）
print("=== inner（默认）===")
print(pd.merge(df_students, df_scores, on='id', how='inner'))

# left join（保留左表的全部，右表匹配不到的填 NaN）
print("\n=== left ===")
print(pd.merge(df_students, df_scores, on='id', how='left'))

# right join（保留右表的全部，左表匹配不到的填 NaN）
print("\n=== right ===")
print(pd.merge(df_students, df_scores, on='id', how='right'))

# outer join（并集，左右表的键都保留，缺失值填 NaN）
print("\n=== outer ===")
print(pd.merge(df_students, df_scores, on='id', how='outer'))
