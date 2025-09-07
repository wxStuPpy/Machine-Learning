import socket

# 创建 TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端
client_socket.connect(('127.0.0.1', 8888))

# 发送消息
while True:
    msg = input("Enter message (type 'exit' to quit): ")
    if msg.lower() == 'exit':
        break
    client_socket.sendall(msg.encode())

    # 接收服务端回复
    data = client_socket.recv(1024)
    print("Server replied:", data.decode())

client_socket.close()
