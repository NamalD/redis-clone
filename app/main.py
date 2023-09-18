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

        parse_request(request)
        writer.write(PING_RESPONSE_BYTES)


def parse_request(request: bytes):
    print("Request: {}".format(request))

    data_type_byte, *rest = request
    data_type = parser.parse_data_type(data_type_byte)
    print(data_type)

    if data_type == parser.RedisDataType.ARRAY:
        parser.parse_array(rest)

    rest_as_bytes = bytes(rest)
    print("Rest: {}".format(rest_as_bytes))


if __name__ == "__main__":
    asyncio.run(main())
