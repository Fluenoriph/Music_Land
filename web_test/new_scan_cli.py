import typer
import socket
import threading


class PortScanner:
    MAX_THREADS = 100

    def __init__(self, host, port):
        self.host = host
        self.port = PortScanner.parse_port_argument(port)
        self.threads = []
        self.semaphore = threading.Semaphore(PortScanner.MAX_THREADS)

    def scanning(self):
        for port in self.port:
            thread = threading.Thread(target=self.check_port, args=(self.host, port))
            thread.start()
            self.threads.append(thread)

        for thread in self.threads:
            thread.join()

    @staticmethod
    def parse_port_argument(port_arg):
        if '-' in port_arg:
            start_port, end_port = port_arg.split('-')

            return range(int(start_port), int(end_port) + 1)
        else:
            return [int(port_arg)]

    def check_port(self, host, port):
        with self.semaphore:
            try:
                sock = socket.socket()
                sock.settimeout(1)

                if sock.connect_ex((host, port)) == 0:
                    print(f"> Порт [ {port} ] открыт !")
                else:
                    print("close")
                sock.close()
            except:  # ???? type
                pass


app = typer.Typer()

@app.command()
def scan(host_arg: str, port_arg: str):
    port_scan = PortScanner(host_arg, port_arg)
    port_scan.scanning()

app()
