import pandas as pd
import numpy as np

# 设置随机种子保证复现
np.random.seed(42)

# 总订单数
n = 100

# 先生成 10 个会员 ID，后面随机重复
member_ids = np.random.randint(1, 100, size=10)

data = {
    "Member ID": np.random.choice(member_ids, size=n, replace=True),  # 允许重复
    "Consumption Date": pd.to_datetime(
        np.random.choice(pd.date_range("2015-01-01", "2018-12-31"), size=n)
    ).strftime("%Y-%m-%d"),
    "Order Number": np.random.randint(1000, 9999, size=n),
    "Order Amount": np.random.randint(1, 10001, size=n),
}

df = pd.DataFrame(data)
print(df.head(10))

# 保存为 CSV
df.to_csv("data2.csv", index=False, encoding="utf-8-sig")
