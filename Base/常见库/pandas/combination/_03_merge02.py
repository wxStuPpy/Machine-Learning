import pandas as pd

# 学生表
df_students = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Zhang', 'Wang', 'Li', 'Zhao'],
    'city_id': [101, 102, 101, 104]   # city_id=104 在城市表里不存在
})

# 城市表
df_cities = pd.DataFrame({
    'city_id': [101, 102, 103],
    'city_name': ['Beijing', 'Shanghai', 'Guangzhou']
})

# inner join（交集）
print("=== inner（默认）===")
print(pd.merge(df_students, df_cities, on='city_id', how='inner'))

# left join（保留所有学生，城市缺失填 NaN）
print("\n=== left ===")
print(pd.merge(df_students, df_cities, on='city_id', how='left'))

# right join（保留所有城市，缺失的学生填 NaN）
print("\n=== right ===")
print(pd.merge(df_students, df_cities, on='city_id', how='right'))

# outer join（并集，学生和城市的键都保留）
print("\n=== outer ===")
print(pd.merge(df_students, df_cities, on='city_id', how='outer'))
