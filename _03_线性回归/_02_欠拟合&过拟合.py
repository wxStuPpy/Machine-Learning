import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # 1. 固定随机种子，生成二次函数数据（含噪声）
    np.random.seed(111)
    x = np.random.uniform(-3, 3, size=100)  # [-3,3)均匀分布的100个x值
    # 真实函数：y = 0.5x² + x + 2，叠加均值0、方差1的正态噪声
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 2. 手动构造特征矩阵：线性特征X（x） + 二次特征X²（x²）
    X = x.reshape(-1, 1)  # 转换为二维数组 (100, 1)
    X1 = np.hstack([X, X ** 2])  # 拼接后形状 (100, 2)，每行为 [x_i, x_i²]

    # 3. 训练二次多项式回归模型
    model = LinearRegression()
    model.fit(X1, y)  # 用 [x, x²] 拟合y
    y_predict = model.predict(X1)  # 预测结果

    # 4. 计算并打印均方误差（MSE）
    mse = mean_squared_error(y, y_predict)
    print(f"二次多项式回归的均方误差（MSE）: {mse:.4f}")
    print(f"模型系数（x的系数, x²的系数）: {np.round(model.coef_, 4)}")  # 接近 [1, 0.5]
    print(f"模型截距（常数项）: {np.round(model.intercept_, 4)}")  # 接近 2

    # 5. 绘图：原始数据 + 平滑拟合曲线
    plt.figure(figsize=(10, 6))  # 设置画布大小
    # 绘制原始数据散点
    plt.scatter(x, y, alpha=0.6, label='原始数据（含噪声）', color='#1f77b4')

    # 关键优化：对x排序，确保拟合线平滑（避免无序x导致的线条交叉）
    x_sorted = np.sort(x)  # 对x从小到大排序
    X_sorted = x_sorted.reshape(-1, 1)  # 排序后的线性特征
    X1_sorted = np.hstack([X_sorted, X_sorted ** 2])  # 排序后的二次特征矩阵
    y_predict_sorted = model.predict(X1_sorted)  # 排序后的预测值

    # 绘制平滑的拟合曲线
    plt.plot(x_sorted, y_predict_sorted, color='red', linewidth=2, label='二次回归拟合曲线')

    # 补充图表标签和图例
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('二次多项式回归拟合：y = 0.5x² + x + 2 + 噪声', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(alpha=0.3)  # 添加网格线，便于观察
    plt.show()