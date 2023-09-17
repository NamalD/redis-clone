import socket

PORT = 6379
PING_RESPONSE_CONTENT = "+PONG\r\n"

# Response has to be encoded as binary
PING_RESPONSE = PING_RESPONSE_CONTENT.encode("utf-8")


def main():
    print("Starting server on port {}".format(PORT))

    server_socket = socket.create_server(("localhost", PORT), reuse_port=True)

    while True:
        # wait for client
        (connection, client_ip) = server_socket.accept()
        print("Client connected on IP: {}".format(client_ip))

        # Respond to PING
        connection.send(PING_RESPONSE)


if __name__ == "__main__":
    main()
