import numpy as np
from numpy.linalg import inv, det, eig

# ===============================
# 一、数组创建
# ===============================
arr1 = np.array([1, 2, 3])                       # 从列表
arr2 = np.array([[1, 2], [3, 4]])                # 从嵌套列表

zeros_arr = np.zeros((2, 3))                     # 全 0
ones_arr = np.ones((3, 3))                       # 全 1
full_arr = np.full((2, 2), 7)                    # 常数数组
eye_arr = np.eye(3)                              # 单位矩阵

arange_arr = np.arange(0, 10, 2)                 # 等差数列
linspace_arr = np.linspace(0, 1, 5)             # 等间隔序列

rand_arr = np.random.rand(2, 3)                  # 0~1 均匀分布
randn_arr = np.random.randn(2, 3)                # 标准正态分布
randint_arr = np.random.randint(0, 10, (2, 3))   # 随机整数

# ===============================
# 二、数学运算函数
# ===============================
a = np.array([1.2, 2.7, -3.5, 4.9])

print("sum:", np.sum(a))
print("mean:", np.mean(a))
print("std:", np.std(a))
print("min:", np.min(a))
print("max:", np.max(a))
print("prod:", np.prod(a))

print("round:", np.round(a))
print("floor:", np.floor(a))
print("ceil:", np.ceil(a))
print("abs:", np.abs(a))

print("power:", np.power(a, 2))
print("sqrt:", np.sqrt(np.abs(a)))

print("sin:", np.sin(a))
print("cos:", np.cos(a))
print("tan:", np.tan(a))

print("exp:", np.exp(a))
print("log:", np.log(np.abs(a)+1))

# ===============================
# 三、数组操作
# ===============================
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print("shape:", b.shape)
print("reshape:", b.reshape(3, 2))
print("transpose:\n", b.T)
print("flatten:", b.flatten())

# ===============================
# 四、统计函数（按轴操作）
# ===============================
print("sum axis=0:", np.sum(b, axis=0))
print("sum axis=1:", np.sum(b, axis=1))

# ===============================
# 五、逻辑判断
# ===============================
c = np.array([1, 2, 3, 4])
print("where:", np.where(c > 2, 1, 0))
print("all > 0:", np.all(c > 0))
print("any > 3:", np.any(c > 3))

# ===============================
# 六、线性代数
# ===============================
A = np.array([[1, 2],
              [3, 4]])
print("inv(A):\n", inv(A))
print("det(A):", det(A))

# 特征值和特征向量
eigvals, eigvecs = eig(A)
print("eigvals:", eigvals)
print("eigvecs:\n", eigvecs)

# 去重和排序特征值
eigvals_unique_sorted = np.sort(np.unique(eigvals))
print("Unique & sorted eigenvalues:", eigvals_unique_sorted)

# 矩阵相乘示例
B = np.array([[5, 6],
              [7, 8]])
C = A @ B   # 或者 np.dot(A, B)
print("A @ B =\n", C)
