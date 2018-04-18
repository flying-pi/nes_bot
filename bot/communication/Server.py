import socket
import threading


class Server(threading.Thread):
    ip = '0.0.0.0'
    port = 123
    start_event = None

    def init(self,ip, port):
        self.ip = ip
        self.port = port
        self.start_event = threading.Event()
        return self.start_event

    def run(self) -> None:
        super().run()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(1)
        self.start_event.set()
        client_sock, address = server.accept()
        print(client_sock)
        data = client_sock.recv(16)
        print(data)
