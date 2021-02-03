import sys
from typing import Dict

from tornado.ioloop import IOLoop

from game_state import GameLoop
from webserver import GameServer

if __name__ == '__main__':
    player_lobby_map: Dict[int, int] = {}
    server = GameServer(player_lobby_map)
    server.listen(int(sys.argv[1]))
    game_loop = GameLoop(player_lobby_map)
    game_loop.start()
    IOLoop.current().start()
