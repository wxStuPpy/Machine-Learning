
---

## 1. **SGD（随机梯度下降，Stochastic Gradient Descent）**

* **更新公式**：
  [
  w \leftarrow w - \eta \nabla L(w)
  ]
* 特点：

  * 每次用一个 mini-batch 近似整体梯度，参数更新快。
  * 学习率 (\eta) 固定，可能收敛慢。
  * 在非凸问题中容易卡在鞍点或局部极小值。

---

## 2. **Momentum（动量法）**

* **核心思想**：引入“惯性”，让参数更新不仅依赖当前梯度，还考虑之前的方向。
* **公式**：
  [
  v \leftarrow \alpha v - \eta \nabla L(w)
  ]
  [
  w \leftarrow w + v
  ]

  * (\alpha)：动量系数（一般 0.9 左右）
* 特点：

  * 能加速收敛（尤其在深谷、鞍点附近）。
  * 更新更平滑，不会来回震荡。

---

## 3. **AdaGrad**

* **核心思想**：对每个参数设置不同的学习率，训练时逐渐减小。
* **公式**：
  [
  h \leftarrow h + (\nabla L(w))^2
  ]
  [
  w \leftarrow w - \frac{\eta}{\sqrt{h} + \epsilon} \nabla L(w)
  ]

  * (h)：累计梯度平方和。
* 特点：

  * 对稀疏特征效果好（更新频繁的参数 → 学习率变小；更新稀疏的参数 → 学习率保持大）。
  * 但缺点是 **学习率单调递减，后期几乎停更**。

---

## 4. **RMSProp**

* **核心思想**：改进 AdaGrad，使用指数加权移动平均（EMA）来避免学习率过早衰减。
* **公式**：
  [
  h \leftarrow \beta h + (1 - \beta)(\nabla L(w))^2
  ]
  [
  w \leftarrow w - \frac{\eta}{\sqrt{h} + \epsilon} \nabla L(w)
  ]

  * (\beta \approx 0.9)：衰减系数。
* 特点：

  * 学习率不会像 AdaGrad 那样过快衰减。
  * 在非凸问题（深度学习）中表现更好。

---

## 5. **Adam（Adaptive Moment Estimation）**

* **核心思想**：结合 Momentum 和 RMSProp 的优点。
* **公式**：

  * 一阶动量（类似 Momentum）：
    [
    m \leftarrow \beta_1 m + (1 - \beta_1)\nabla L(w)
    ]
  * 二阶动量（类似 RMSProp）：
    [
    v \leftarrow \beta_2 v + (1 - \beta_2)(\nabla L(w))^2
    ]
  * 偏差修正：
    [
    \hat{m} = \frac{m}{1 - \beta_1^t}, \quad \hat{v} = \frac{v}{1 - \beta_2^t}
    ]
  * 参数更新：
    [
    w \leftarrow w - \eta \frac{\hat{m}}{\sqrt{\hat{v}} + \epsilon}
    ]
* 特点：

  * **收敛快，适合大数据/非凸问题**。
  * 默认参数（(\beta_1=0.9, \beta_2=0.999)）通常效果不错。
  * 但在某些任务上可能不如 SGD + Momentum 的最终收敛效果好。

---

## 📌 总结对比表

| 方法           | 思想                 | 学习率特点 | 优点               | 缺点      |
| ------------ | ------------------ | ----- | ---------------- | ------- |
| **SGD**      | 基础梯度下降             | 固定    | 简单，收敛稳定          | 慢，易卡鞍点  |
| **Momentum** | 加动量（惯性）            | 固定    | 收敛快，减震荡          | 学习率需调   |
| **AdaGrad**  | 自适应学习率（累积）         | 单调递减  | 稀疏特征效果好          | 后期学习率过小 |
| **RMSProp**  | 指数加权平均梯度平方         | 平稳    | 避免 AdaGrad 学习率衰减 | 需调超参数   |
| **Adam**     | Momentum + RMSProp | 自适应   | 收敛快，常用           | 有时泛化差   |

---

