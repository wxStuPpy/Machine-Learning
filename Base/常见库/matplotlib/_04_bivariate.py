import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,4))

xx=np.linspace(1,10,5)
yy=np.logspace(1,5,5,base=2)

plt.scatter(x=xx,y=yy)
plt.grid()
plt.show()