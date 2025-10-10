import matplotlib.pyplot as plt
import torch
import pandas as pd
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from torch.utils.data import TensorDataset


# 创建数据集
def create_dataset():
    # 1. 读取数据（确保文件路径正确，若报错可改为绝对路径）
    data = pd.read_csv('../data/house_prices.csv')
    # 2. 去除无关列（Id列无意义）
    data.drop(['Id'], axis=1, inplace=True)
    # 3. 划分特征（x）和目标（y）
    x = data.drop('SalePrice', axis=1)
    y = data['SalePrice']
    # 4. 划分训练集和测试集（random_state=42确保结果可复现）
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    # 5. 特征工程
    # 5.1 区分数值型和分类型特征列
    numerical_features = x.select_dtypes(exclude=['object']).columns  # 排除字符串列（分类型）
    categorical_features = x.select_dtypes(include=['object']).columns  # 选择字符串列（分类型）

    # 5.2 数值型特征管道：缺失值填充（均值）→ 标准化
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),  # 步骤1：填充缺失值
        ('scaler', StandardScaler())  # 步骤2：标准化
    ])

    # 5.3 分类型特征管道：缺失值填充（NaN）→ 独热编码（修正格式！）
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='NaN')),  # 步骤1：填充缺失值（二元元组）
        ('onehot', OneHotEncoder(handle_unknown='ignore'))  # 步骤2：独热编码（二元元组）
    ])

    # 5.4 组合列转化器（分别处理数值/分类型特征）
    transformer = ColumnTransformer(transformers=[
        ('numerical', numerical_transformer, numerical_features),  # 数值特征处理
        ('categorical', categorical_transformer, categorical_features)  # 分类型特征处理
    ])

    # 5.5 执行特征转化（训练集fit+transform，测试集仅transform）
    x_train = transformer.fit_transform(x_train)  # 训练集：拟合转换器并转化
    x_test = transformer.transform(x_test)  # 测试集：用训练集的转换器转化（避免数据泄露）

    # 5.6 转化为DataFrame（方便查看特征，可选步骤）
    x_train_df = pd.DataFrame(
        x_train.toarray(),  # 稀疏矩阵→稠密数组（独热编码后可能为稀疏矩阵）
        columns=transformer.get_feature_names_out()
    )
    x_test_df = pd.DataFrame(
        x_test.toarray(),
        columns=transformer.get_feature_names_out()
    )

    # 6. 构建PyTorch Tensor数据集（float类型，避免后续模型报错）
    # 目标值y转为二维张量（匹配模型输出形状，常见优化）
    train_dataset = TensorDataset(
        torch.tensor(x_train_df.values, dtype=torch.float32),  # 特征：float32
        torch.tensor(y_train.values, dtype=torch.float32)
    )
    test_dataset = TensorDataset(
        torch.tensor(x_test_df.values, dtype=torch.float32),
        torch.tensor(y_test.values, dtype=torch.float32)
    )

    # 返回：训练集、测试集、特征维度（模型输入大小）
    return train_dataset, test_dataset, x_train_df.shape[1]


# 主流程
# 1.加载数据
train_dataset, test_dataset, feature_num = create_dataset()
# print(f"特征维度（模型输入大小）：{feature_num}")
# print(f"训练集样本数：{len(train_dataset)}")
# print(f"测试集样本数：{len(test_dataset)}")

# 2.创建模型
model = nn.Sequential(
    nn.Linear(feature_num, 128),
    nn.BatchNorm1d(128),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(128, 1),
)


# 3.自定义损失函数
def log_rmse(y_pred, target):
    y_pred = torch.clamp(y_pred, 1, float('inf'))
    mse = nn.MSELoss()
    return torch.sqrt(mse(torch.log(y_pred), torch.log(target)))


# 4.模型训练和测试
def train_test(model, train_dataset, test_dataset, lr, epoch_num, batch_size, device):
    # 1.初始化
    # 1.1初始化参数
    def init_weights(m):
        # 对Linear层进行初始化
        if type(m) == nn.Linear:
            nn.init.xavier_uniform_(m.weight)

    model.apply(init_weights)
    # 1.2将模型加载到设备
    model = model.to(device)
    # 1.3定义优化器
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    # 定义训练误差和测试误差列表
    train_loss_list = []
    test_loss_list = []

    # 2.模型训练
    for epoch in range(epoch_num):
        model.train()
        # 2.1创建DataLoader
        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        train_loss_total = 0
        # 2.2按批次迭代训练模型
        for batch_idx, (x, y) in train_loader:
            # 将数据加载到设备
            x, y = x.to(device), y.to(device)
            # 2.2.1前向传播
            y_pred = model(x)
            # 2.2.2计算损失
            loss_value = log_rmse(y_pred.squeeze(), y)
            # 2.2.3反向传播
            loss_value.backward()
            # 2.2.4更新参数
            optimizer.step()
            optimizer.zero_grad()

            # 累加损失
            train_loss_total += loss_value.item() * x.shape[0]
        this_train_loss = train_loss_total / len(train_dataset)
        train_loss_list.append(this_train_loss)

        # 3.模型测试
        model.eval()
        # 3.1定义DataLoader
        test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        # 3.2计算测试误差
        test_loss_total = 0
        with torch.no_grad():  # 测试时关闭梯度计算
            for x, y in test_loader:
                x, y = x.to(device), y.to(device)
                y_pred = model(x)
                loss_value = log_rmse(y_pred.squeeze(), y)
                test_loss_total += loss_value.item() * x.shape[0]
        this_test_loss = test_loss_total / len(test_dataset)
        test_loss_list.append(this_test_loss)
        print(f'epoch: {epoch + 1}, train_loss: {this_train_loss}, test_loss: {this_test_loss}')
    return train_loss_list, test_loss_list


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
lr = 0.1
epoch_num = 200
batch_size = 64
train_loss_list, test_loss_list = train_test(model, train_dataset, test_dataset, lr, epoch_num, batch_size,
                                             device)
# 画图
plt.plot(train_loss_list, color='red', label='train')
plt.plot(test_loss_list, color='blue', label='test')
plt.legend()
plt.show()
