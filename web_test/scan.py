import socket
import threading
import timeit


def check_port_single_thread():
    for port in range(20, 100):
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex(('127.0.0.1', port))

        if result == 0:
            print(f"[+] Порт {port} открыт")
        s.close()

def check_port_multi_thread():





execution_time = timeit.timeit(lambda: check_port_single_thread(), number=1)

print('Code time:', execution_time)