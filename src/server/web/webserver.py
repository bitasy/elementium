from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError


class GameServer(TCPServer):
    def __init__(self, player_lobby_map):
        super().__init__()
        self.player_lobby_map = player_lobby_map

    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b";")  # replace with length byte and read_bytes for performance
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
