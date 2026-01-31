import socket
import sys

def check_port(host, port):
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"[+] Порт {port} открыт")
    elif result == 111 or result == 10061:
        print(f"[-] Порт {port} закрыт")
    else:
        print(f"[?] Порт {port} фильтруется или неизвестный ответ ({result})")
    s.close()

host = sys.argv[1]

for port in range(20, 26):
    check_port("ip_addr", port)