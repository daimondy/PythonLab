import socket
from time import gmtime, strftime


def ur(chislo):
    a, b, c = chislo[0], chislo[1], chislo[2]
    if (c - a) != 0:
        primer = abs(1 - a * b ** c - a * (b ** 2 - c ** 2) + (b - c + a)
                     * (12 + b) / (c - a))
        return primer
    else:
        return'Ошибка! Деление на ноль.'


LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Сервер запущен.")
print("Ожидание ответа от клиента...")
clientConn, clientAddr = server.accept()
print("Подключенный клиент:", clientAddr)
while True:
    data = clientConn.recv(1024)
    msg = data.decode()
    if msg == 'datetime':
        clientConn.send(strftime("%Y-%m-%d %H:%M:%S", gmtime()).encode())
    print("Клиент отключен.")
    clientConn.close()
