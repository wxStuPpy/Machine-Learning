from sklearn.neighbors import KNeighborsRegressor
import joblib
import os

def func():
    # 散乱的训练数据（不是规则等差）
    x = [[1, 5, 2],
         [2, 1, 3],
         [3, 7, 4],
         [4, 2, 6],
         [6, 8, 5],
         [7, 3, 9],
         [8, 6, 1]]
    y = [10, 8, 15, 14, 20, 22, 18]  # 目标值随意指定，和 x 没有简单规律

    # 建立 KNN 回归器
    estimator = KNeighborsRegressor(n_neighbors=3)
    estimator.fit(x, y)

    # 确保保存目录存在
    os.makedirs("../../modules", exist_ok=True)

    # 保存模型
    joblib.dump(estimator, "../../modules/knn_model.pkl")

    # 预测一组新样本
    test_point = [[5, 4, 6]]
    prediction = estimator.predict(test_point)
    print(f"输入 {test_point} 的预测结果:", prediction)

    # 加载模型再预测，验证持久化
    estimator2 = joblib.load("../../modules/knn_model.pkl")
    print(f"(加载模型后) 输入 {test_point} 的预测结果:", estimator2.predict(test_point))

if __name__ == "__main__":
    func()
