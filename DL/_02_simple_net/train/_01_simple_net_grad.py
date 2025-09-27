import numpy as np
from DL.common.functions import softmax, cross_entropy_error
from DL.common.gradient import numerical_gradient

# 定义一个简单神经网络类
class SimpleNet:
    # 初始化
    def __init__(self):
        self.W = np.random.randn(2, 3)

    # 前向传播
    def forward(self, X):
        a = X @ self.W
        return softmax(a)

    # 计算损失值
    def loss(self, x, t):
        y = self.forward(x)
        return cross_entropy_error(y, t)


if __name__ == '__main__':
    # 定义数据
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])
    # 定义神经网络模型
    net = SimpleNet()
    # 计算梯度
    f = lambda _: net.loss(x, t)
    gradW = numerical_gradient(f, net.W)
    print(gradW)
