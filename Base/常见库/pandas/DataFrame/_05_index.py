import pandas as pd

# 读取 CSV 文件，并将 'age' 列设置为索引
df = pd.read_csv('name.csv', index_col='age')
print("设置 age 为索引：")
print(df)

# 在 Pandas 中，90%以上的函数，都是在源数据上拷贝一份修改返回副本，
# 这类函数都有一个特点，即: inplace 参数
# 如果 inplace=True，则会修改本身数据
# 设置了索引后，列元素就不包括索引这一列
# print(df.set_index('age'))

# 取消设置的索引（重置为默认 RangeIndex）
df.reset_index(inplace=True)
print("\n重置索引后：")
print(df)

# 重新以 'score' 作为索引，直接修改当前 DataFrame
df.set_index(keys='score', inplace=True)
print("\n设置 score 为索引：")
print(df)

print('*' * 30)

# 查看部分行索引 和 部分列索引
print("前三个行索引:", df.index[:3])      # 索引是分数列 (score)，取前3个分数
print("前三个列索引:", df.columns[:3])    # 列名包括 id, name, age, city 等

# 修改索引名 和 列名
idx_name = {88: 888, 92: 9292}   # 将索引中 88 改为 888，92 改为 9292
col_name = {'id': 'uid'}         # 将列名 id 改为 uid
df.rename(index=idx_name, columns=col_name, inplace=True)
print("\n修改后的 DataFrame：")
print(df)

# 也可以把 index 和 columns 转成列表，手动修改后再赋值回去
idx_list = df.index.to_list()    # 把索引转换为列表
idx_list[0] = 100                # 手动修改第一个索引值
col_list = df.columns.to_list()  # 把列名转换为列表
col_list[1] = 'uuid'             # 修改第二个列名（例如 name -> uuid）

# 重新赋值给 df 的 index 和 columns
df.index = idx_list
df.columns = col_list

print("\n手动修改 index 和 columns 后：")
print(df)

# 新增一列（直接赋值）
df['work'] = 'teacher'                      # 给所有行新增一列，值都为 "teacher"
df['age*uuid'] = df['age'] * df['uuid']     # 新增一列，存储 age 与 uuid 的乘积
print("\n新增两列：work, age*uuid")
print(df)

# 删除一列
df.drop('work', axis='columns', inplace=True)   # 删除 work 列
print("\n删除 work 列：")
print(df)

# 删除一行
df.drop(100, axis='rows', inplace=True)        # 删除索引为 100 的那一行
print("\n删除索引=100 的行：")
print(df)

# 插入一列
df.insert(loc=1, column='gender', value=['M', 'F', 'M', 'F', 'M'])
# loc=1 表示插在第1列后面（即第二列位置）
# column 指定新列名
# value 是插入的值，长度必须与行数相同
print("\n插入 gender 列：")
print(df)

# 插入一行
new_row = pd.DataFrame([[25, 7, 'new_user', 'Xiamen', 175]],
                       columns=['age', 'uuid', 'name', 'city', 'age*uuid'],
                       index=[9999])  # 设定新行的索引为 9999
df = pd.concat([df, new_row])          # 使用 concat 拼接新行
print("\n插入一行：")
print(df)
