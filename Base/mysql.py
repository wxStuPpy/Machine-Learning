from pymysql import Connection

# 1️⃣ 连接数据库
coon = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    charset='utf8mb4' ,
    autocommit=True
)

print("MySQL 版本:", coon.get_server_info())

# 2️⃣ 获取游标
cursor = coon.cursor()

# 3️⃣ 选择数据库
coon.select_db('test')

# 4️⃣ 删除旧表（如果存在）
cursor.execute("DROP TABLE IF EXISTS python_table")

# 5️⃣ 创建表
cursor.execute('''
    CREATE TABLE python_table (
        id INT PRIMARY KEY AUTO_INCREMENT,
        age INT,
        name VARCHAR(50)
    )
''')

# 6️⃣ 插入数据
data = [
    (25, 'Alice'),
    (30, 'Bob'),
    (22, 'Charlie'),
    (28, 'David'),
    (35, 'Eve')
]

# 使用 executemany 批量插入
cursor.executemany(
    "INSERT INTO python_table (age, name) VALUES (%s, %s)",
    data
)

# 7️⃣ 提交事务 已经开启自动提交
#coon.commit()

# 8️⃣ 查询并打印测试
cursor.execute("SELECT * FROM python_table")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 9️⃣ 关闭连接
cursor.close()
coon.close()
