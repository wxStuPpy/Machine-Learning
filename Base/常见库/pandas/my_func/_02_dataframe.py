import pandas as pd

df = pd.DataFrame({
    'name': ['zhang','li','wang'],
    'age': [1,2,3]
})

print(df)

def func(x):
    print(f'x的内容是:{x}')
    print(f'x的类型是:{type(x)}')

df.apply(func,axis=0)#默认是列
