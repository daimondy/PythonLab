import socket


def det(chislo):
    return (chislo[0] * chislo[4] * chislo[8] + chislo[1] * chislo[5] * chislo[6] + chislo[2] * chislo[3] * chislo[7] -
            chislo[2] * chislo[4] * chislo[6] - chislo[0] * chislo[5] * chislo[7] - chislo[1]*chislo[3]*chislo[8])


LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Сервер запущен.")
print("Ожидание ответа от клиента...")
clientConn, clientAddr = server.accept()
print("Подключенный клиент:", clientAddr)

chislo = clientConn.recv(1024).decode().strip().split(' ')
chislo = [int(a) for a in chislo]

otvet = str(det(chislo))
clientConn.send(otvet.encode())
clientConn.close()
