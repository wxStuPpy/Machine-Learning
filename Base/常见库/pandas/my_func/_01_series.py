import pandas as pd

df = pd.DataFrame({
    'name': ['zhang','li','wang'],
    'age': [1,2,3]
})

print(df)

# 定义函数
def func1(x: int) -> int:
    return x**2

# my_func 到 'age' 列
df['age_squared'] = df['age'].apply(func1)
print(df)

def func2(x,e)->int:
    return x**e

df['age_power']=df['age'].apply(func2,e=3)
print(df)

