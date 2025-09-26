import numpy as np
import matplotlib.pyplot as plt
from common.gradient import numerical_diff


def f(x):
    return 0.01 * x ** 2 + 0.1 * x


def tangent_line(f, x):
    k = numerical_diff(f, x)
    b = f(x) - k * x
    return lambda x: k * x + b


x = np.arange(0.0, 20.0, 0.1)
y = f(x)

f_line = tangent_line(f, x=6)
y_line = f_line(x)

plt.plot(x, y, c='r')
plt.plot(x, y_line, c='b')
plt.show()
