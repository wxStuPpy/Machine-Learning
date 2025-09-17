from random import shuffle

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import calinski_harabasz_score

def func():
    # 生成测试数据
    x, y = make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1,-1],[0,0],[1,1],[2,2],[3,3]],
        cluster_std=[0.4,0.2,0.2,0.2,0.5],
        random_state=10,
        shuffle=True
    )

    # 可视化原始数据（真实簇）
    plt.figure()
    plt.scatter(x[:,0], x[:,1], c=y, marker='o', cmap='viridis')
    plt.title("Original Clusters")
    plt.show()

    # KMeans 聚类
    y_predict = KMeans(
        n_clusters=5,           # 这里应该和实际簇数一致
        random_state=10,
        init='k-means++',
        n_init=10
    ).fit_predict(x)

    # 可视化聚类结果
    plt.figure()
    plt.scatter(x[:,0], x[:,1], c=y_predict, marker='o', cmap='viridis')
    plt.title("KMeans Predicted Clusters")
    plt.show()

    # 评估聚类质量
    score = calinski_harabasz_score(x, y_predict)
    print("Calinski-Harabasz Score:", score)

if __name__ == '__main__':
    func()
