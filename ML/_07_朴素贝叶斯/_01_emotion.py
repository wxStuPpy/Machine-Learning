import jieba
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# -----------------------------
# 1. 加载数据
# -----------------------------
data_df = pd.read_csv('./data.csv', encoding='utf-8-sig')
data_df['label'] = data_df['label'].map({'positive': 0, 'negative': 1, 'neutral': 2})
y = data_df['label']

# -----------------------------
# 2. 加载停用词
# -----------------------------
stopwords = []
with open('./stopwords.txt', 'r', encoding='utf-8-sig') as f:
    stopwords = [line.strip() for line in f.readlines()]
stopwords = list(set(stopwords))  # 去重

# -----------------------------
# 3. 文本分词
# -----------------------------
comment_list = [' '.join(jieba.lcut(line)) for line in data_df['comment']]

# -----------------------------
# 4. 特征向量化（CountVectorizer）并去掉停用词
# -----------------------------
vectorizer = CountVectorizer(stop_words=stopwords)
X = vectorizer.fit_transform(comment_list)
feature_names = vectorizer.get_feature_names_out()
X = X.toarray()

# -----------------------------
# 5. 划分训练集/测试集（示例：前9条训练，后3条测试）
# -----------------------------
x_train, y_train = X[:7, :], y.values[:7]
x_test, y_test = X[7:, :], y.values[7:]

# -----------------------------
# 6. 训练朴素贝叶斯模型
# -----------------------------
model = MultinomialNB(alpha=1)
model.fit(x_train, y_train)

# -----------------------------
# 7. 预测与评估
# -----------------------------
y_pred = model.predict(x_test)
print("测试集预测标签:", y_pred)
print("准确率:", model.score(x_test, y_test))
