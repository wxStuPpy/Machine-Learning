import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 200  # 数据量

# 特征生成
gender = np.random.choice(["Male", "Female"], size=n_samples)
tenure = np.random.randint(0, 72, size=n_samples)  # 在网月数
monthly_charges = np.round(np.random.uniform(20, 120, size=n_samples), 2)
total_charges = np.round(tenure * monthly_charges + np.random.normal(0, 50, size=n_samples), 2)
contract_type = np.random.choice(["Month-to-month", "One year", "Two year"], size=n_samples, p=[0.6, 0.25, 0.15])
internet_service = np.random.choice(["DSL", "Fiber optic", "None"], size=n_samples, p=[0.4, 0.4, 0.2])
has_paperless_billing = np.random.choice(["Yes", "No"], size=n_samples)
region = np.random.choice(["North", "South", "East", "West"], size=n_samples)

# 标签（流失与否），简单规则：短期合约 + 高月费 更容易流失
churn_prob = (
    (contract_type == "Month-to-month").astype(int) * 0.4 +
    (monthly_charges > 80).astype(int) * 0.3 +
    (internet_service == "Fiber optic").astype(int) * 0.2 +
    np.random.rand(n_samples) * 0.2
)
churn = np.where(churn_prob > 0.5, "Yes", "No")

# 组装 DataFrame
df = pd.DataFrame({
    "gender": gender,
    "tenure": tenure,
    "monthly_charges": monthly_charges,
    "total_charges": total_charges,
    "contract_type": contract_type,
    "internet_service": internet_service,
    "has_paperless_billing": has_paperless_billing,
    "region": region,
    "churn": churn
})

# 保存为 CSV 文件（不带索引）
df.to_csv("telecom_churn.csv", index=False, encoding="utf-8-sig")

print("数据已保存为 telecom_churn.csv")
print(df.head())
