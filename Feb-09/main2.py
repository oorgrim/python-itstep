from udp_client import UDP_Client

def main():
    server_address = '192.168.111.2'
    server_port = 11400

    client = UDP_Client(server_address, server_port)

    client.send("Hello!")

    response = client.receive()
    print("Сообщение от сервера:", response)

    client.close()

if __name__ == "__main__":
    main()