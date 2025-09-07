import re

# 待匹配的字符串
s = '123456 123 444 123'

# -------------------------------
# re.match(pattern, string)
# 尝试从字符串的 **开头**匹配正则表达式
# -------------------------------
match = re.match('123', s)
print("re.match:", match)         # <re.Match object; span=(0, 3), match='123'>
if match:
    print("match.span():", match.span())  # 返回匹配位置 (start, end)

# -------------------------------
# re.search(pattern, string)
# 扫描整个字符串，返回第一个匹配到的对象
# -------------------------------
match = re.search('444', s)
print("re.search:", match)        # <re.Match object; span=(12, 15), match='444'>
if match:
    print("match.span():", match.span())

# -------------------------------
# re.findall(pattern, string)
# 返回 **字符串中所有匹配的子串**，返回列表
# -------------------------------
all_matches = re.findall('123', s)
print("re.findall:", all_matches)  # ['123', '123', '123']

# 也可以查找所有数字
numbers = re.findall(r'\d+', s)
print("All numbers:", numbers)     # ['123456', '123', '444', '123']


text = "My phone numbers are 123-456-7890 and 987.654.3210."

# 匹配数字
print(re.findall(r'\d+', text))
# ['123', '456', '7890', '987', '654', '3210']

# 匹配电话号码格式 xxx-xxx-xxxx 或 xxx.xxx.xxxx
print(re.findall(r'\d{3}[-.]\d{3}[-.]\d{4}', text))
# ['123-456-7890', '987.654.3210']

# 匹配单词
print(re.findall(r'\b\w+\b', text))
# ['My', 'phone', 'numbers', 'are', '123', '456', '7890', 'and', '987', '654', '3210']

# 匹配开头
print(re.findall(r'^My', text))
# ['My']

# 匹配结尾
print(re.findall(r'3210\.$', text))
# ['3210.']

# 使用分组提取区号和号码
matches = re.findall(r'(\d{3})[-.](\d{3})[-.](\d{4})', text)
print(matches)
# [('123','456','7890'), ('987','654','3210')]
