import numpy as np
import pandas as pd

df1=pd.read_csv('df1.csv')
df2=pd.read_csv('df2.csv')
df3=pd.read_csv('df3.csv')

pd.concat([df1, df2, df3])#按行拼接 参考列名
print(pd.concat([df1, df2, df3],axis='rows'))#按行拼接 效果同上

print(pd.concat([df1, df2, df3], axis=1))

s1=pd.Series(['x','y','z'])
print(pd.concat([df1,s1]))#忽略行索引 会自动填充

print()
print("\n=== concat df1 + df4 ===")
df4=pd.DataFrame([['A','B','C']],columns=['id','name','age'])
print(pd.concat([df1, df4],ignore_index=True))