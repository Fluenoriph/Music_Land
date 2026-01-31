import socket
import json


# Получаем данные от интерфейса юзера -------------------------------------------------
# Ventilation_calc. data
user_typed_data = [63.4, 3.2, 3.8, 15, 15, 307.8, 1.5] # 7 item, is rectangle hole

calc_data_json_dump = json.dumps(user_typed_data)


client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост локальной машины
port = 12345  # устанавливаем порт сервера
client.connect((hostname, port))  # подключаемся к серверу

client.sendall(calc_data_json_dump.encode())

print("Data sent to server")

client.close()

client.close()