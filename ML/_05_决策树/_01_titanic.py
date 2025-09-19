import seaborn as sns
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 1. 读取数据
titanic = sns.load_dataset("titanic")

# 2. 数据预处理
titanic['age'] = titanic['age'].fillna(titanic['age'].mean())  # 填充缺失值
X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']

# One-hot 编码
X = pd.get_dummies(X, drop_first=True)

# 3. 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=1
)

# 4. 决策树模型
model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=5,
    min_samples_split=10,
    random_state=1
)
model.fit(X_train, y_train)

# 5. 模型预测
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]  # 正类(生还)的概率

# 6. 模型评估
print("准确率:", accuracy_score(y_test, y_pred))
print("\n分类报告:\n", classification_report(y_test, y_pred, target_names=['died', 'survived']))

# 7. 计算 ROC-AUC
roc_auc = roc_auc_score(y_test, y_pred_proba)
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# 8. 绘制 ROC 曲线
plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, color='red', linewidth=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0,1], [0,1], linestyle='--', color='gray', label='Random Guess')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR = Recall)')
plt.title('ROC Curve for Titanic Survival')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 9. 可视化决策树
plt.figure(figsize=(12,6))
plot_tree(
    model,
    max_depth=5,
    filled=True,
    feature_names=X.columns,
    class_names=['died','survived']
)
plt.show()
