import socket
from time import gmtime, strftime

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Сервер запущен.")
print("Ожидание ответа от клиента...")
clientConn, clientAddr = server.accept()
print("Подключенный клиент:", clientAddr)
msg = clientConn.recv(1024).decode()
if msg == 'datetime':
    clientConn.send(strftime("%Y-%m-%d %H:%M:%S", gmtime()).encode())
print("Клиент отключен.")
clientConn.close()
