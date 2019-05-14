import socket

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Сервер запущен.")
print("Ожидание ответа от клиента...")
clientConn, clientAddr = server.accept()
print("Подключенный клиент:", clientAddr)

previous_msg = 'Поступившего ранее сообщения не было.'

while True:
    msg = clientConn.recv(1024).decode()
    if msg == 'stop':
        print("Клиент отключен.")
        clientConn.close()
        break
    previous_msg.encode()
    clientConn.send(bytes(previous_msg, 'UTF-8'))
    previous_msg = msg
