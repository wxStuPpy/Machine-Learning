import torch
import matplotlib.pyplot as plt
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset

# 1.构建数据集 创建数据加载器
X = torch.randn(100, 1)
# 预设真实系数
w = torch.tensor([2.5])
b = torch.tensor([5.2])
# 定义拟合目标值y
y = w * X + b + torch.randn(100, 1) * 0.5
print(y.shape)
# 构建dataset
dataset = TensorDataset(X, y)
# 构建dataloader
dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

# 2.构建模型
model = torch.nn.Linear(1, 1)

# 3.定义损失函数和优化器
loss = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)

# 4.模型训练
epoch_num = 300
loss_list = []
for epoch in range(epoch_num):
    total_loss = 0
    # 1个轮次的迭代
    for X_train, y_train in dataloader:
        # 4.1前向传播(预测)
        y_pred = model(X_train)
        # 4.2计算损失
        loss_value = loss(y_pred, y_train)
        # total_loss变为终点 可能会出现错误 可以借住item
        total_loss += loss_value.item() * X_train.shape[0]
        # 4.3反向传播
        loss_value.backward()
        # 4.4更新参数
        optimizer.step()
        # 4.5梯度清零
        optimizer.zero_grad()

    # 计算平均损失
    loss_list.append(total_loss / len(dataset))

# 打印参数
print(f"拟合的权重: {model.weight.item():.4f}")
print(f"拟合的偏置: {model.bias.item():.4f}")
# 画图
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].plot(loss_list)
ax[0].set_xlabel('epoch')
ax[0].set_ylabel('loss')
ax[1].scatter(X.numpy(), y.numpy())
y_pred = model(X)
plt.plot(X.numpy(), y_pred.detach().numpy(), color='red')
plt.show()
