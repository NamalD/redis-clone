import asyncio
import app.parser as parser
from asyncio import StreamReader, StreamWriter

PORT = 6379
REQUEST_BUFFER_SIZE = 1024


PING_RESPONSE_CONTENT = "+PONG\r\n"
PING_RESPONSE_BYTES = PING_RESPONSE_CONTENT.encode("utf-8")


async def main():
    print("Starting server on localhost:{}".format(PORT))

    server = await asyncio.start_server(handle_client, "localhost", PORT, reuse_port=True)

    async with server:
        await server.serve_forever()


async def handle_client(reader: StreamReader, writer: StreamWriter):
    while True:
        print("Client connected")

        request = await reader.read(REQUEST_BUFFER_SIZE)

        if not request:
            writer.close()
            return

        parsed = parser.parse_request(request)
        print(parsed)

        # Respond with PONG for every request
        writer.write(PING_RESPONSE_BYTES)


if __name__ == "__main__":
    asyncio.run(main())
