import socket
import time

connection_socket = socket.socket()
connection_socket.connect(("127.0.0.1", 5000))

try:
    while True:
        connection_socket.sendall(b"Hello World!")
        data = connection_socket.recv(1024)
        print(data)
        time.sleep(2)
finally:
    connection_socket.close()
