from collections import OrderedDict
from DL.common.gradient import numerical_gradient
from DL.common.layers import *


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)
        # 定义层结构
        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['ReLU1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])
        # 定义最后一层:SoftMaxWithLoss
        self.lastLayer = SoftmaxWithLoss()

    def forward(self, X):
        # 对于神经网络中的每一层 依次调用forward
        for layer in self.layers.values():
            X = layer.forward(X)
        return X

    def loss(self, X, t):
        y = self.forward(X)
        return self.lastLayer.forward(y, t)

    def accuracy(self, X, t):
        y_pred = self.forward(X)  # 预测分类数值
        y = np.argmax(y_pred, axis=1)
        return np.sum(y == t) / len(t)

    # 1.使用数值微分法计算梯度
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

    # 2.反向传播计算梯度
    def gradient(self, X, t):
        # 前向传播
        self.loss(X, t)
        # 反向传播
        dy = 1
        dy = self.lastLayer.backward(dy)
        # 将神经网络层的所有层翻转处理
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dy = layer.backward(dy)
        # 提取各层梯度
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W2'], grads['b2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db
        return grads
