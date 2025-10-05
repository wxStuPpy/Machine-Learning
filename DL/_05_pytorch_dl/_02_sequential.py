import torch
import torch.nn as nn

model = nn.Sequential(
  nn.Linear(3, 4),
  nn.Tanh(),
  nn.Linear(4, 4),
  nn.ReLU(),
  nn.Linear(4, 2),
  nn.Softmax(dim=1),
)

# 初始化参数
def init_weights(m):
  # 对Linear层进行初始化
  if type(m) == nn.Linear:
    nn.init.xavier_uniform_(m.weight)
    m.bias.data.fill_(0.01)

model.apply(init_weights) # apply会遍历所有子模块并依次调用函数

output = model(torch.randn(10, 3))
print("输出：\n", output)

from torchsummary import summary
# input_size:特征数，batch_size:样本数
summary(model, input_size=(3,), batch_size=10, device="cpu")