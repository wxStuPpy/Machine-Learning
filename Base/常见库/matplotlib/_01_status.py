import matplotlib.pyplot as plt

x = [-1, 3, 6]
y = [0, 4, 9]

plt.figure(figsize=(5,3))
plt.xlim(-3,10)
plt.ylim(-1,10)
plt.xlabel('x', size=20)
plt.ylabel('y', size=12)
plt.title('Simple Line Plot', size=7)
plt.grid(True, linestyle='--', alpha=0.7)
plt.plot(x, y, marker='o', color='b')
plt.show()