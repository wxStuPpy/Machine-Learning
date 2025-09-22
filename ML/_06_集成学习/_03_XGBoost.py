import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold,GridSearchCV
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import class_weight
import numpy as np


def init_data():
    data = pd.read_csv("winequality-red.csv", sep=';')
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1].apply(lambda x: 0 if x <= 4 else (1 if x <= 6 else 2))

    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    pd.concat([x_train, y_train], axis=1).to_csv('./train.csv', index=False)
    pd.concat([x_test, y_test], axis=1).to_csv('./test.csv', index=False)

def train_and_cv():
    train_data = pd.read_csv('./train.csv')
    test_data = pd.read_csv('./test.csv')

    x_train = train_data.iloc[:, :-1]
    y_train = train_data.iloc[:, -1]
    x_test = test_data.iloc[:, :-1]
    y_test = test_data.iloc[:, -1]

    print("训练集/测试集维度:", x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    print(y_train.value_counts())

    sample_weight = class_weight.compute_sample_weight(class_weight='balanced', y=y_train)
    model = XGBClassifier(
        objective='multi:softmax',
        eval_metric='mlogloss'
    )

    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2],
        'subsample': [0.7, 1.0],
        'colsample_bytree': [0.7, 1.0]
    }

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    estimator = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring='accuracy',
        cv=skf,
        verbose=1,
        n_jobs=-1
    )

    estimator.fit(x_train, y_train, sample_weight=sample_weight)
    print("最优参数:", estimator.best_params_)
    print("最优交叉验证准确率:", estimator.best_score_)

    best_model = estimator.best_estimator_
    y_pred = best_model.predict(x_test)
    print("测试集准确率:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    init_data()
    train_and_cv()
