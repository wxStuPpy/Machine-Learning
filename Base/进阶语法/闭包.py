def make_counter():
    count = 0  # 外层函数的局部变量

    def counter():
        nonlocal count  # 表示使用外层函数的 count
        count += 1
        return count

    return counter  # 返回内层函数

# 使用闭包
c = make_counter()
print(c())  # 输出: 1
print(c())  # 输出: 2
print(c())  # 输出: 3
