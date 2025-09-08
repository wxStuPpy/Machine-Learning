import pandas as pd

df = pd.read_csv('name.csv')

# 按 age 降序排序
print(df.sort_values(by='age', ascending=False))

# 按索引升序排序
print(df.sort_index())

# 年龄最大前三
print(df.nlargest(3, 'age'))

# 分数最小两名
print(df.nsmallest(2, 'score'))

# 分数排名
df['score_rank'] = df['score'].rank(ascending=False)
print(df)

# 按 score 降序，若 score 相同，再按 age 降序
df_sorted = df.sort_values(by=['score', 'age'], ascending=[False, False])

print(df_sorted)


print('*'*25)
df1 = pd.DataFrame({
    'name': ['zhang', 'wang', 'li', 'wang'],
    'age': [20, 22, 19, 22]
})
print(df1)
# 默认去重，保留第一次出现
print(df1.drop_duplicates())

# 只考虑 name 列去重
print(df1.drop_duplicates(subset=['name'], keep='last'))
