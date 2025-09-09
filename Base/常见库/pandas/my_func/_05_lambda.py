import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4,5,6],
    'b': [1,2,3]
})

print("原始数据：")
print(df)

print(df.apply(lambda x: x ** 2))