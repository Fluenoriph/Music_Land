import socket


server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12345  # устанавливаем порт сервера
server.bind((hostname, port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений

print("Server running")

con, _ = server.accept()  # принимаем клиента

data = con.recv(1024)
message = data.decode()
print(message)

con.close()  # закрываем клиента
server.close()






