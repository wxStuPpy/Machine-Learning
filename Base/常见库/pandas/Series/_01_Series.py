import numpy as np
import pandas as pd

#1.1ndarray转
arr=np.array([1,2,3,4])
s1=pd.Series(data=arr)
print(s1)
print(type(s1))

#1.2列表转化
s2=pd.Series(data=['ni','hao'],index=['name','age'])#data可以省略不写
print(s2)
print(type(s2))

s3=pd.Series(data={'name':'111','age':'22'},index=['age','name'])#data可以省略不写
print(s3)
print(type(s3))