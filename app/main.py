import socket

PORT = 6379
PING_RESPONSE_CONTENT = "+PONG\r\n"
REQUEST_BUFFER_SIZE = 1024

# Response has to be encoded as binary
PING_RESPONSE = PING_RESPONSE_CONTENT.encode("utf-8")


def main():
    print("Starting server on port {}".format(PORT))

    server_socket = socket.create_server(("localhost", PORT), reuse_port=True)

    # Wait for client
    (connection, client_ip) = server_socket.accept()
    print("Client connected on IP: {}".format(client_ip))

    while True:
        # Wait for a request
        request = connection.recv(REQUEST_BUFFER_SIZE)
        while len(request) > 0:
            print("Request: {}".format(request))

            # Respond to PING
            connection.send(PING_RESPONSE)

            # Wait for another request
            request = connection.recv(REQUEST_BUFFER_SIZE)


if __name__ == "__main__":
    main()
