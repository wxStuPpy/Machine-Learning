import pandas as pd
df = pd.read_csv('name.csv')

#1与Series计算
age = df['age']
print(age + 10)
print('*'*30)

#2series之间进行计算
# 会优先计算索引一致的 索引不一致按照顺序计算
# 不匹配的使用NAN
recv_age=age.sort_values(ascending=False)
print(age + age)
print(recv_age+age)