from sklearn.datasets import load_iris

# 加载数据集
iris = load_iris()

# 前 5 条特征数据
print("前5条特征数据：")
print(iris.data[:5])

# 标签（整数编码）
print("\n标签：")
print(iris.target[:10])  # 只看前10个

# 标签名称
print("\n标签名称：")
print(iris.target_names)

# 特征名称
print("\n特征名称：")
print(iris.feature_names)

#数据集描述
print('\n数据集描述')
print(iris.DESCR)