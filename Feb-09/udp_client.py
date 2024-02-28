import socket

class UDP_Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        self.sock.sendto(message.encode("utf8"), (self.server_address, self.server_port))

    def receive(self):
        data, addr = self.sock.recvfrom(1024)
        return data.decode()

    def close(self):
        self.sock.close()