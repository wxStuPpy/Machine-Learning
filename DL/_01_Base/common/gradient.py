import numpy as np


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def _numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    # 遍历x中的特征i
    for i in range(x.size):
        tmp = x[i]
        x[i] = tmp + h
        fxh1 = f(x)
        x[i] = tmp - h
        fxh2 = f(x)
        grad[i] = (fxh1 - fxh2) / (2 * h)
        x[i] = tmp
    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient(f, X)
    grad = np.zeros_like(X)
    for i, x in enumerate(X):
        grad[i] = _numerical_gradient(f, x)
    return grad


if __name__ == '__main__':
    # 测试函数：f(x) = x1² + x2²
    def function_2(x):
        return x[0] ** 2 + x[1] ** 2


    # 单个样本的梯度
    x = np.array([3.0, 4.0])
    print(numerical_gradient(function_2, x))
    # 批量样本的梯度
    X = np.array([[3.0, 4.0], [1.0, 2.0]])
    print(numerical_gradient(function_2, X))
