from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError


class EchoServer(TCPServer):
    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b";")  # replace with length byte and read_bytes for performace
                if data[:3] == b'id:':
                    cli_id = data[3:-1]
                    await stream.write(data)  # Handshake
                    break
                else:
                    await stream.write(b'id;')  # Couldn't get id, try again
            except StreamClosedError:
                print('Stream closed while trying to get id')
        while True:
            try:
                data = await stream.read_until(b";")
                print('%s: %s' % (cli_id.decode(), data.decode()))
            except StreamClosedError:
                break


if __name__ == '__main__':
    server = EchoServer()
    server.listen(88889)
    IOLoop.current().start()
