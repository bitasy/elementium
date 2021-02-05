from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError

from engine.game_state import GameState


class GameServer(TCPServer):
    def __init__(self, lobby_map):
        # This object will "hold" many streams, not just one
        super().__init__()
        self.lobby_map = lobby_map

    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b";", max_bytes=500)
                if data[:3] == b'id:':
                    cli_id = data[3:-1]
                    await stream.write(data)  # Handshake
                    lobby_id = 1  # Temporary global lobby
                    lobby: GameState = self.lobby_map[lobby_id]
                    player = lobby.add_player(cli_id.decode(), stream)
                    break
                else:
                    await stream.write(b'id;')  # Couldn't get id, try again
            except StreamClosedError:
                print('Stream closed while trying to get id')
        while True:
            try:
                data = await stream.read_until(b";", max_bytes=500)
                data_str = data.decode()[:-1]  # remove ;
                new_input = {int(i[:i.index(':')]): int(i[i.index(':')+1:]) for i in data_str.split(',')}
                player.new_input(new_input)
            except StreamClosedError:
                break
