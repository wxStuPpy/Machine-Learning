import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# -----------------------------
# 1. 加载数据
# -----------------------------
df = pd.read_csv("telecom_churn.csv")

# -----------------------------
# 2. 特征 / 标签分离
# -----------------------------
X = df.drop("churn", axis=1)  # 特征
y = df["churn"].map({"No": 0, "Yes": 1})  # 标签转为 0/1

# -----------------------------
# 3. One-Hot 编码（处理分类变量）
# -----------------------------
X_encoded = pd.get_dummies(X, drop_first=True)

# -----------------------------
# 4. 划分训练集和测试集
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 5. 标准化（仅针对数值特征）
# -----------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------------
# 6. 模型训练（逻辑回归 + CV 调优）
# -----------------------------
# 定义基础模型
base_model = LogisticRegression(max_iter=500, solver='liblinear')

# 定义网格搜索参数
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],   # 正则化强度
    'penalty': ['l1', 'l2']          # 正则化类型
}

# GridSearchCV: 5 折交叉验证
grid = GridSearchCV(estimator=base_model, param_grid=param_grid, cv=5, scoring='roc_auc', n_jobs=-1)
grid.fit(X_train, y_train)

# 最佳参数和最佳模型
print("最佳参数:", grid.best_params_)
print("最佳CV AUC:", grid.best_score_)

# 使用最佳模型进行预测
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)
y_pred_pro = best_model.predict_proba(X_test)[:, 1]

# -----------------------------
# 7. 模型评估
# -----------------------------
print("准确率:", accuracy_score(y_test, y_pred))
print("\n分类报告:\n", classification_report(y_test, y_pred, target_names=["No", "Yes"]))
roc_auc = roc_auc_score(y_test, y_pred_pro)
print(f'ROC_AUC: {roc_auc:.4f}')

# -----------------------------
# 8. 绘制 ROC 曲线
# -----------------------------
fpr, tpr, thresholds = roc_curve(y_test, y_pred_pro)
plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, color='red', linewidth=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0,1], [0,1], linestyle='--', color='gray')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR = Recall)')
plt.title('ROC Curve')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
