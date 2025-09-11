import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# 生成示例数据
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B'], 100)
})

# 1. matplotlib：需手动设置样式
plt.scatter(data['x'], data['y'], c='blue', alpha=0.6)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Matplotlib Scatter Plot')
plt.show()

# 2. pandas：基于 DataFrame 直接调用，简化代码
data.plot(kind='scatter', x='x', y='y', c='red', alpha=0.6)
plt.title('Pandas Scatter Plot')  # 仍需用 matplotlib 补充标题
plt.show()

# 3. seaborn：支持按类别着色，默认样式更优
sns.scatterplot(data=data, x='x', y='y', hue='category', alpha=0.6)
plt.title('Seaborn Scatter Plot')
plt.show()