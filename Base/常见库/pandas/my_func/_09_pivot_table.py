import pandas as pd

df = pd.DataFrame({
    'student': ['zhang', 'zhang', 'li', 'li', 'wang', 'wang'],
    'subject': ['Math', 'English', 'Math', 'English', 'Math', 'English'],
    'score': [88, 92, 75, 85, 90, 80],
    'class': ['A', 'A', 'A', 'B', 'B', 'B']
})

print("原始数据：")
print(df)

table = pd.pivot_table(df, values='score', index='student', columns='subject')
print(table)

table = pd.pivot_table(df, values='score', index='class', columns='subject', aggfunc='mean')
print(table)

table = pd.pivot_table(df, values='score', index='class', columns='subject', aggfunc=['mean','max'])
print(table)

table = pd.pivot_table(df, values='score', index=['class','student'], columns='subject', aggfunc='mean')
print(table)
