import pandas as pd

data_ = {
    'name': ['zhang', 'wang', 'li'],
    'age': [11, 22, 33],
    'id': [1, 2, 3]
}

frame = pd.DataFrame(data=data_,index=['A','B','C'],columns=['name','id','age'])
print(frame)


# 按行输入数据，每个子列表是一行
data_rows = [
    ['zhang', 1, 11],
    ['wang', 2, 22],
    ['li', 3, 33]
]

# 创建 DataFrame，指定列名
frame_rows = pd.DataFrame(data_rows, columns=['name', 'id', 'age'], index=['A', 'B', 'C'])
print("\n按行顺序输入的 DataFrame:")
print(frame_rows)
