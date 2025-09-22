import seaborn as sns
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

titanic = sns.load_dataset("titanic")
titanic['age'] = titanic['age'].fillna(titanic['age'].mean())  # 填充缺失值
x = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']
x = pd.get_dummies(x, drop_first=True)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, stratify=y, test_size=0.2, random_state=1
)

model_tr = DecisionTreeClassifier()  # 单独的决策树
model_rf = RandomForestClassifier(n_estimators=10)  # 单独的随机森林

param_grid_rf = {
    'n_estimators': [20, 30, 40, 50],
    'max_depth': [2, 4, 6, 7, 8],
    'max_features': ['sqrt', 'log2'],
    'random_state': [2, 3, 4]
}

estimator_rf = GridSearchCV(
    estimator=RandomForestClassifier(),  # 基础模型是随机森林
    param_grid=param_grid_rf,
    cv=5
)

# 4. 训练
model_tr.fit(x_train, y_train)
model_rf.fit(x_train, y_train)
estimator_rf.fit(x_train, y_train)  # 训练网格搜索的随机森林

# 5. 输出最优参数
print("随机森林最优参数：", estimator_rf.best_params_)
best_rf = estimator_rf.best_estimator_  # 最优随机森林模型

# 6. 模型预测
# 单棵决策树预测
y_pred_tr = model_tr.predict(x_test)
# 随机森林预测
y_pred_rf = model_rf.predict(x_test)
# 网格搜索最优随机森林预测
y_pred_best_rf = best_rf.predict(x_test)

# 7. 模型评估
from sklearn.metrics import accuracy_score, classification_report

print("=== 决策树 ===")
print("准确率:", accuracy_score(y_test, y_pred_tr))
print("分类报告:\n", classification_report(y_test, y_pred_tr, target_names=['died', 'survived']))

print("\n=== 随机森林 ===")
print("准确率:", accuracy_score(y_test, y_pred_rf))
print("分类报告:\n", classification_report(y_test, y_pred_rf, target_names=['died', 'survived']))

print("\n=== 网格搜索最优随机森林 ===")
print("准确率:", accuracy_score(y_test, y_pred_best_rf))
print("分类报告:\n", classification_report(y_test, y_pred_best_rf, target_names=['died', 'survived']))
