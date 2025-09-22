import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# -------------------------------
# 1. 读取数据
# -------------------------------
titanic = sns.load_dataset("titanic")

# 缺失值处理
titanic['age'] = titanic['age'].fillna(titanic['age'].mean())
titanic['embarked'] = titanic['embarked'].fillna(titanic['embarked'].mode()[0])

# 选择部分特征
X = titanic[['pclass', 'age', 'sex', 'sibsp', 'parch', 'fare', 'embarked']]
y = titanic['survived']

# One-Hot 编码（处理分类特征）
X = pd.get_dummies(X, drop_first=True)

# 划分训练 / 测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# -------------------------------
# 2. 训练 GBDT 模型
# -------------------------------
gbdt = GradientBoostingClassifier(
    n_estimators=200,    # 基学习器数量（弱分类器数）
    learning_rate=0.1,   # 学习率
    max_depth=3,         # 每棵树的最大深度（通过 max_depth 控制基分类器的复杂度）
    random_state=42
)

gbdt.fit(X_train, y_train)

# -------------------------------
# 3. 模型评估
# -------------------------------
y_pred = gbdt.predict(X_test)
y_pred_pro = gbdt.predict_proba(X_test)[:, 1]

print("✅ 准确率:", accuracy_score(y_test, y_pred))
print("\n✅ 分类报告:\n", classification_report(y_test, y_pred, target_names=['died', 'survived']))
print("✅ ROC-AUC:", roc_auc_score(y_test, y_pred_pro))

# -------------------------------
# 4. 绘制 ROC 曲线
# -------------------------------
fpr, tpr, thresholds = roc_curve(y_test, y_pred_pro)
plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, color="blue", label=f"ROC curve (AUC={roc_auc_score(y_test, y_pred_pro):.2f})")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate (Recall)")
plt.title("ROC Curve (GBDT)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
