# Классический неблокирующий сервер

import select
import socket


# Функция handle должна быть максимально компактной
# и максимально быстрой, т.к. время выполнения будет суммироваться
# к времени отклика всех клиентов.
# 1 клиент = 1 сек. ожидания. 10 клиентов = 10 сек. ожидания (каждый)
def handle(connection_socket):
    data = connection_socket.recv(1024)
    if not data:
        connections.remove(connection_socket)
        connection_socket.close()
        return
    print(data)
    connection_socket.sendall(data)


connection_socket = socket.socket()
connection_socket.setblocking(False)
connection_socket.bind(("127.0.0.1", 5000))

# Очередь подключений
connection_socket.listen(5)

connections = [connection_socket]

print("Ожидание подключений")
try:
    while True:
        # _ = Это значение, которая не нужно - неиспользуемые переменные (unuse value)
        # (read_sockets, write_sockets, error_sockets)
        read_sockets, _, _ = select.select(connections, [], [])
        for row in read_sockets:
            # Пришёл новый клиент
            if row == connection_socket:
                connect, a = connection_socket.accept()
                print("Подключён ", a)
                connections.append(connect)
            else:
                # Прослушиваем старых клиентов
                handle(row)
finally:
    connection_socket.close()
