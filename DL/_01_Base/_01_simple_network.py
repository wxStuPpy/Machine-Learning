import numpy as np
from common.functions import sigmoid, identity


def init_network():
    network = {
        'W1': np.array([[1, 2, 3], [4, 5, 6]]),  # 第1层权重（2输入→3隐藏单元）
        'b1': np.array([0.1, 0.2, 0.3]),  # 第1层偏置
        'W2': np.array([[1, 2], [3, 4], [5, 6]]),  # 第2层权重（3隐藏单元→2隐藏单元）
        'b2': np.array([0.4, 0.5]),  # 第2层偏置
        'W3': np.array([[1, 2], [3, 4]]),  # 第3层权重（2隐藏单元→2输出）
        'b3': np.array([0.6, 0.7])  # 第3层偏置
    }
    return network


def forward(network, x):
    w1, b1 = network['W1'], network['b1']
    w2, b2 = network['W2'], network['b2']
    w3, b3 = network['W3'], network['b3']

    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, w3) + b3
    y = identity(a3)

    return y

if __name__ == '__main__':
    network = init_network()
    x = np.array([1.0, 0.5])
    output = forward(network, x)
    print("神经网络输出：", output)
