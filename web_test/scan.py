import socket
import threading
import queue
import time


class PortScanner:
    MAX_THREADS = 100

    def __init__(self, ips, port_range_values):
        self.ips = ips
        self.port_range = range(port_range_values[0], port_range_values[1] + 1)

        # Объект очереди по умолчанию без параметров.
        self.queue = queue.Queue()

        # Заполняем очередь кортежами из адреса и порта.
        self.create_work_queue()

        print(time.time())

        self.thread_computing()

        print(time.time())

    def thread_computing(self):
        threads = []

        for _ in range(min(PortScanner.MAX_THREADS, self.queue.qsize())):
            thread = threading.Thread(target=self.check_port)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def create_work_queue(self):
        for ip in self.ips:
            for port in self.port_range:
                self.queue.put((ip, port))

    # Проверка подключения к порту по сокету: ip и порт.
    def check_port(self):
        while not self.queue.empty():
            socket_data = self.queue.get()

            try:
                sock = socket.socket()
                sock.settimeout(1)

                if sock.connect_ex(socket_data) == 0: # Может проверить 1 ?
                    print(f"> На адресе [{socket_data[0]}]: порт {socket_data[1]} открыт")
                sock.close()
            except: # Найти исключения !
                pass

            self.queue.task_done()


scanner = PortScanner(["192.168.50.1"], [20, 100])

#-----------------------------
import socket
import threading
import schedule
import time
import logging

# Настройка логирования
logging.basicConfig(
    filename="scanner.log",
    level=logging.INFO,
    format="%(asctime)s — %(message)s"
)

# Параметры сканера
HOST = "127.0.0.1"
START_PORT = 20
END_PORT = 100
MAX_THREADS = 100

# Сканер портов с ограничением потоков
def scan_ports():
    logging.info("Сканирование началось.")


    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)

    def check_port(host, port):
        with semaphore:
            try:
                s = socket.socket()
                s.settimeout(1)
                if s.connect_ex((host, port)) == 0:
                    print(f"[+] Порт {port} открыт")
                else:
                    print("Close")
                s.close()
            except:
                pass

    for port in range(START_PORT, END_PORT + 1):
        t = threading.Thread(target=check_port, args=(HOST, port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    logging.info("Сканирование завершено.")

# Настройка расписания
# schedule.every().day.at("23:00").do(scan_ports)
schedule.every(0.1).minutes.do(scan_ports)

# Цикл планировщика
while True:
    schedule.run_pending()
    time.sleep(1)








# --------------------------------------------------------------------------------------
import argparse
import socket
import sys

def parse_ports(port_arg):
    if '-' in port_arg:
        start, end = port_arg.split('-')
        return range(int(start), int(end)+1)
    else:
        return [int(port_arg)]

def scan_port(ip, port, verbose=False):
    with socket.socket() as s:
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Порт {port} открыт")
        elif verbose:
            print(f"[-] Порт {port} закрыт")

def main():
    parser = argparse.ArgumentParser(description="Простой порт-сканер")
    parser.add_argument("-ip", required=True, help="IP-адрес для сканирования")
    parser.add_argument("-port", required=True, help="Порт или диапазон (например, 22 или 20-80)")
    parser.add_argument("-verbose", action="store_true", help="Подробный вывод")

    args = parser.parse_args()

    try:
        ports = parse_ports(args.port)
    except ValueError:
        print("[!] Ошибка: неверный формат порта. Используй 22 или 20-80.")
        sys.exit(1)

    for port in ports:
        scan_port(args.ip, port, args.verbose)

main()











