import numpy as np
from DL.common.functions import softmax, sigmoid, cross_entropy_error
from DL.common.gradient import numerical_gradient


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def forward(self, X):
        W1, b1 = self.params['W1'], self.params['b1']
        W2, b2 = self.params['W2'], self.params['b2']
        a1 = X @ W1 + b1
        z1 = sigmoid(a1)
        a2 = z1 @ W2 + b2
        y = softmax(a2)
        return y

    def loss(self, X, t):
        y = self.forward(X)
        return cross_entropy_error(y, t)

    def accuracy(self, X, t):
        y_proba = self.forward(X)
        y = np.argmax(y_proba, axis=1)
        return np.sum(y == t) / len(t)

    def numerical_gradient(self, X, t):
        # 定义目标函数
        loss_f = lambda _: self.loss(X, t)
        # 对每个参数进行梯度计算
        grads = {}
        grads['W1'] = numerical_gradient(loss_f, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_f, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_f, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_f, self.params['b2'])
        return grads
