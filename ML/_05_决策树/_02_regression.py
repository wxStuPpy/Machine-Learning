from cProfile import label
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x=np.arange(1,11,1).reshape(-1,1)
y=np.array([5.56,5.70,5.91,6.40,6.80,7.05,8.70,8.90,9.00,9.05])
print(x)
print(y)

model1=DecisionTreeRegressor(max_depth=1)
model2=DecisionTreeRegressor(max_depth=3)
model3=LinearRegression()

model1.fit(x,y)
model2.fit(x,y)
model3.fit(x,y)

x_test=np.arange(1,10,0.01).reshape(-1,1)
y_pred1=model1.predict(x_test)
y_pred2=model2.predict(x_test)
y_pred3=model3.predict(x_test)

print(f'\n shape-->{y_pred1.shape,y_pred2.shape,y_pred3.shape}\n')

plt.figure(figsize=(16,8))
plt.scatter(x,y,label='data')

plt.plot(x_test,y_pred1,label='max_depth=1')
plt.plot(x_test,y_pred2,label='max_depth=3')
plt.plot(x_test,y_pred3,label='linear')
plt.xlabel('data')
plt.ylabel('target')
plt.legend()
plt.show()