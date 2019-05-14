import socket


def det(chislo):
    return chislo[0], chislo[4], chislo[1], chislo[3]


LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Сервер запущен.")
print("Ожидание ответа от клиента...")
clientConn, clientAddr = server.accept()
print("Подключенный клиент:", clientAddr)

increace = clientConn.recv(1024).decode()
chislo = clientConn.recv(1024).decode().strip().split(' ')
chislo = [int(increace) * int(a) for a in chislo]

otvet = str(chislo)
clientConn.send(otvet.encode())
clientConn.close()
