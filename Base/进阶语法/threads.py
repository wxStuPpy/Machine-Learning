import threading
import time

# 线程要执行的函数
def worker(name, delay):
    for i in range(3):
        print(f"Thread {name} running iteration {i+1}")
        time.sleep(delay)
    print(f"Thread {name} finished")

# 创建线程对象
t1 = threading.Thread(target=worker, args=("A", 1))
t2 = threading.Thread(target=worker, args=("B", 2))

# 启动线程
t1.start()
t2.start()

# 等待线程执行完成
t1.join()
t2.join()

print("All threads finished")
