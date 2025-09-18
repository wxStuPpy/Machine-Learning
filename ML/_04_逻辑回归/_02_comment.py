import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix, classification_report,
    roc_curve, roc_auc_score
)
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

iris = load_iris()
X = iris.data[iris.target != 2]
y = iris.target[iris.target != 2]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = LogisticRegression(C=1.0, max_iter=200, solver='liblinear')
# C=1.0 正则化强度（越小正则化越强），max_iter=200 最大迭代次数
# solver='liblinear' 适用于小数据集和二分类问题
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]  # 预测属于类别1的概率，用于 ROC

# 4. 混淆矩阵（直观展示 TP、FP、FN、TN）
cm = confusion_matrix(y_test, y_pred)  # 生成混淆矩阵
plt.figure(figsize=(4, 3))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["setosa", "versicolor"],  # 横轴预测类别
            yticklabels=["setosa", "versicolor"])  # 纵轴真实类别
plt.xlabel("predict label")  # 横坐标标题
plt.ylabel("real label")     # 纵坐标标题
plt.title("confusion_matrix")
plt.show()

# 5. 精确率 / 召回率 / F1-score
print("分类报告:")
print(classification_report(y_test, y_pred, target_names=["setosa", "versicolor"]))
# classification_report 会输出：
# precision（精确率）、recall（召回率）、f1-score（综合指标）、support（样本数）

# 6. ROC 曲线 & AUC
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)  # 计算 ROC 曲线的点
auc = roc_auc_score(y_test, y_pred_prob)  # 计算 AUC 值（越接近1越好）

plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f"ROC curve (AUC = {auc:.2f})", color="red")  # ROC 曲线
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")  # 随机分类的参考虚线
plt.xlabel("FP (FPR)")          # 横轴是假正率 False Positive Rate
plt.ylabel("TP (TPR = Recall)") # 纵轴是真正率 True Positive Rate
plt.title("ROC curve")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
