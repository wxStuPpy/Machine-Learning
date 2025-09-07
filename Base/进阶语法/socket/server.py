import socket

# 创建 TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定 IP 和端口
server_socket.bind(('127.0.0.1', 8888))

# 开始监听
server_socket.listen(5)
print("Server listening on 127.0.0.1:8888...")

while True:
    client_socket, addr = server_socket.accept()  # 接受客户端连接
    print(f"Connected by {addr}")

    while True:
        data = client_socket.recv(1024)  # 接收数据
        if not data:
            break
        print("Received:", data.decode())
        client_socket.sendall(data.upper())  # 回传大写数据

    client_socket.close()
    print(f"Connection with {addr} closed")
