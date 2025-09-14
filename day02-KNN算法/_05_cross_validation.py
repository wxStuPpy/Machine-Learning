import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 定义交叉验证函数
def cross_validation():
    # 1️⃣ 加载数据集
    iris = load_iris()  # 加载鸢尾花数据集
    # 2️⃣ 数据集划分：训练集80%，测试集20%
    x_train, x_test, y_train, y_test = train_test_split(
        iris['data'], iris['target'],
        test_size=0.2,        # 测试集占20%
        random_state=1        # 随机种子，保证可复现
    )

    # 3️⃣ 特征标准化（对训练集做fit_transform，对测试集只做transform）
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)    # 训练集标准化
    x_test = scaler.transform(x_test)          # 测试集标准化，使用训练集的均值和方差

    # 4️⃣ 定义基础KNN模型
    estimator = KNeighborsClassifier()

    # 5️⃣ 设置网格搜索的参数范围
    param_grid = {'n_neighbors':[1,3,5,7]}  # 调整邻居数

    # 6️⃣ 使用GridSearchCV进行网格搜索 + 5折交叉验证
    estimator = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=10)

    # 7️⃣ 训练网格搜索模型（必须调用fit）
    estimator.fit(x_train, y_train)

    # 8️⃣ 输出网格搜索的结果
    print("最佳交叉验证分数:", estimator.best_score_)       # 最佳平均交叉验证准确率
    print("最佳模型:", estimator.best_estimator_)            # 得到最佳参数组合对应的模型
    print("最佳参数:", estimator.best_params_)                # 对应的参数组合
    print("交叉验证详细结果:", estimator.cv_results_)        # 每个参数组合的交叉验证结果（字典形式）

    # 9️⃣ 将详细结果转换成DataFrame保存为CSV
    frame = pd.DataFrame(estimator.cv_results_)
    frame.to_csv(path_or_buf='./mygridsearchcv.csv')        # 保存文件到当前目录

    # 🔟 在测试集上评估模型准确率
    print("测试集准确率:", estimator.score(x_test, y_test)) # 使用最佳模型对测试集进行评估

# 主程序入口
if __name__ == '__main__':
    cross_validation()  # 调用函数
