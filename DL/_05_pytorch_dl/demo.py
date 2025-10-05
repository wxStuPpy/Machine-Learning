import matplotlib.pyplot as plt
import torch
import pandas as pd
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from torch.utils.data import TensorDataset, DataLoader


# ==============================
# 数据预处理部分
# ==============================
def create_dataset():
    # 1. 读取数据
    data = pd.read_csv('../data/house_prices.csv')

    # 2. 去除无关列
    data.drop(['Id'], axis=1, inplace=True)

    # 3. 划分特征与目标
    x = data.drop('SalePrice', axis=1)
    y = data['SalePrice']

    # 4. 划分训练/测试集
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # 5. 特征工程
    numerical_features = x.select_dtypes(exclude=['object']).columns
    categorical_features = x.select_dtypes(include=['object']).columns

    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='NaN')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    transformer = ColumnTransformer(transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

    # 转换数据
    x_train = transformer.fit_transform(x_train)
    x_test = transformer.transform(x_test)

    # 兼容稀疏矩阵/稠密矩阵
    x_train_dense = x_train.toarray() if hasattr(x_train, "toarray") else x_train
    x_test_dense = x_test.toarray() if hasattr(x_test, "toarray") else x_test

    x_train_df = pd.DataFrame(x_train_dense, columns=transformer.get_feature_names_out())
    x_test_df = pd.DataFrame(x_test_dense, columns=transformer.get_feature_names_out())

    # 转换为 PyTorch TensorDataset
    train_dataset = TensorDataset(
        torch.tensor(x_train_df.values, dtype=torch.float32),
        torch.tensor(y_train.values, dtype=torch.float32)
    )
    test_dataset = TensorDataset(
        torch.tensor(x_test_df.values, dtype=torch.float32),
        torch.tensor(y_test.values, dtype=torch.float32)
    )

    return train_dataset, test_dataset, x_train_df.shape[1]


# ==============================
# 模型定义部分
# ==============================
def build_model(feature_num):
    model = nn.Sequential(
        nn.Linear(feature_num, 128),
        nn.BatchNorm1d(128),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(128, 1),
        nn.Softplus()  # 确保输出为正值，避免log(负数)
    )
    return model


# ==============================
# 自定义损失函数
# ==============================
def log_rmse(y_pred, target):
    y_pred = torch.clamp(y_pred, 1, float('inf'))
    mse = nn.MSELoss()
    return torch.sqrt(mse(torch.log(y_pred), torch.log(target)))


# ==============================
# 训练与测试函数
# ==============================
def train_test(model, train_dataset, test_dataset, lr, epoch_num, batch_size, device):
    # 初始化权重
    def init_weights(m):
        if isinstance(m, nn.Linear):
            nn.init.xavier_uniform_(m.weight)

    model.apply(init_weights)
    model = model.to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.5)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    train_loss_list, test_loss_list = [], []

    for epoch in range(epoch_num):
        # ---- 训练 ----
        model.train()
        total_train_loss = 0
        for batch_idx, (x, y) in enumerate(train_loader):
            x, y = x.to(device), y.to(device)
            y_pred = model(x)
            loss = log_rmse(y_pred.squeeze(), y)

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            total_train_loss += loss.item() * x.size(0)

        avg_train_loss = total_train_loss / len(train_dataset)
        train_loss_list.append(avg_train_loss)

        # ---- 测试 ----
        model.eval()
        total_test_loss = 0
        with torch.no_grad():
            for x, y in test_loader:
                x, y = x.to(device), y.to(device)
                y_pred = model(x)
                loss = log_rmse(y_pred.squeeze(), y)
                total_test_loss += loss.item() * x.size(0)

        avg_test_loss = total_test_loss / len(test_dataset)
        test_loss_list.append(avg_test_loss)

        scheduler.step()

        print(f"Epoch [{epoch + 1:03d}/{epoch_num}]  "
              f"Train Loss: {avg_train_loss:.4f}  Test Loss: {avg_test_loss:.4f}")

    return train_loss_list, test_loss_list


# ==============================
# 主流程
# ==============================
if __name__ == "__main__":
    # 1. 加载数据
    train_dataset, test_dataset, feature_num = create_dataset()

    # 2. 创建模型
    model = build_model(feature_num)

    # 3. 训练参数
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    lr = 1e-3
    epoch_num = 200
    batch_size = 64

    # 4. 训练模型
    train_loss_list, test_loss_list = train_test(
        model, train_dataset, test_dataset, lr, epoch_num, batch_size, device
    )

    # 5. 绘制训练曲线
    plt.figure(figsize=(8, 5))
    plt.plot(train_loss_list, label='Train Loss', color='red')
    plt.plot(test_loss_list, label='Test Loss', color='blue')
    plt.xlabel('Epoch')
    plt.ylabel('Log RMSE')
    plt.title('Training and Testing Loss Curve')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('loss_curve.png', dpi=200)
    plt.show()
