import torch
from torch import nn, optim

# 定义模型
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        # 只定义一个全连接层
        self.linear = nn.Linear(5, 3)
        self.linear.weight.data = torch.randn(5, 3).T
        self.linear.bias.data = torch.tensor([1.0, 2.0, 3.0])

    def forward(self, x):
        x = self.linear(x)
        return x

# 输入数据
X = torch.randn(2, 5)
# 目标值
target = torch.randn(2, 3)

model = Model()
output = model(X)
print(f'output: {output}')

loss = nn.MSELoss()
loss_value = loss(output, target)
print(f'loss_value:{loss_value}')

# 反向传播
loss_value.backward()

# 定义优化器
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 更新参数
optimizer.step()
optimizer.zero_grad()

# 打印模型参数
for param in model.state_dict():
    print(param)
    print(model.state_dict()[param])
