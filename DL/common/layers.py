import numpy as np

from DL.common.functions import *


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        y = x.copy()
        y[self.mask] = 0
        return y

    def backward(self, dy):
        dx = dy.copy()
        dx[self.mask] = 0
        return dx


class Sigmoid:
    def __init__(self):
        self.y = None

    def forward(self, x):
        y = sigmoid(x)
        self.y = y
        return y

    def backward(self, dy):
        dx = dy * (1.0 - self.y) * self.y
        return dx


class Affine:
    def __init__(self, W, b):
        self.W = W  # 权重矩阵
        self.b = b  # 偏置向量
        self.X = None  # 存储前向传播的输入X（用于反向传播）
        self.original_x_shape = None  # 存储输入X的原始形状（用于反向传播时恢复形状）
        self.dW = None  # 权重W的梯度（用于参数更新）
        self.db = None  # 偏置b的梯度（用于参数更新）

    def forward(self, X):
        self.original_x_shape = X.shape
        self.X = X.reshape(X.shape[0], -1)
        y = self.X @ self.W + self.b
        return y

    def backward(self, dy):
        dX = dy @ self.W.T
        dX = dX.reshape(*self.original_x_shape)
        self.dW = self.X.T @ dy
        self.db = np.sum(dy, axis=0)
        return dX


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, X, t):
        self.t = t
        self.y = softmax(X)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss

    def backward(self, dy=1):
        n = self.y.shape[0]
        if self.y.size == self.t.size:
            dx = self.y - self.t
        else:
            dx = self.y.copy()
            dx[np.arange(n), self.t] -= 1
        return dx / n
