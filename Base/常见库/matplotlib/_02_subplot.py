import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x ** 2
y4 = np.exp(x / 10)

# 创建 2 行 2 列的子图布局
plt.figure(figsize=(10, 8))  # 设置整个画布的大小

# 第 1 个子图（左上角）
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='blue')
plt.title('sin(x)')
plt.grid(alpha=0.3)

# 第 2 个子图（右上角）
plt.subplot(2, 2, 2)
plt.plot(x, y2, color='red')
plt.title('cos(x)')
plt.grid(alpha=0.3)

# 第 3 个子图（左下角）
plt.subplot(2, 2, 3)
plt.plot(x, y3, color='green')
plt.title('x²')
plt.grid(alpha=0.3)

# 第 4 个子图（右下角）
plt.subplot(2, 2, 4)
plt.plot(x, y4, color='purple')
plt.title('e^(x/10)')
plt.grid(alpha=0.3)

# 调整子图之间的间距（避免标题和标签重叠）
plt.tight_layout()

plt.show()
