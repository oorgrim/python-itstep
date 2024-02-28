import socket

class UDP_Server:
    def __init__(self, port):
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(('localhost', self.port))
        self.running = False

    def start(self):
        self.running = True
        print(f"Сервер работает на порте {self.port}")
        while self.running:
            message, address = self.server.recvfrom(1024)
            print(f"Получено сообщение от {address}: {message.decode()}")
            self.server_socket.sendto("OK", address)

    def stop(self):
        self.running = False
        self.server.close()
