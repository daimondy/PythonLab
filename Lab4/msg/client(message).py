import socket

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print('Введите сообщение или стоп-слово (stop)')
while True:
    msg = input('Ваше сообщение:\n')
    client.send(bytes(msg, 'UTF-8'))
    if msg == 'stop':
        print('Отключение от сервера')
        break
    out_msg = client.recv(1024).decode()
    print('От сервера: ', out_msg)
client.close()
