# import socket

# s_ip = '127.0.0.1' 
# s_port = 8020
# size = 1024
# address = (s_ip,s_port)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#     client_socket.connect(address) # 주소 전달로 서버 접속
#     client_socket.send('Hello !'.encode())
#     message = client_socket.recv(size)
#     print("{}".format(message))

#!/usr/bin/python
import socket
my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 8820))
message = 'hello server'
my_socket.send(message.encode())
response_data = my_socket.recv(1024).decode()
print("Received: %s" % response_data)
my_socket.close