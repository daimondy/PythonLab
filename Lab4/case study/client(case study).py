import socket

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print('Пример: |1 - a*b c - a*(b 2 -c 2 ) + (b-c+a)*(12+b)/(c-a)| ')
while True:
    msg = input('Введите a, b и с для решения примера через пробел:\n')
    client.send(msg.encode())
    print('Ответ:', client.recv(1024).decode())
