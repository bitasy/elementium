import sys
from typing import Dict

from tornado.ioloop import IOLoop

from engine.game_state import GameState
from web.webserver import GameServer

if __name__ == '__main__':
    lobby_map: Dict[int, GameState] = {}
    # Temporary global lobby
    global_lobby = GameState()
    lobby_map[1] = global_lobby
    server = GameServer(lobby_map)
    server.listen(int(sys.argv[1]))
    IOLoop.current().run_sync(global_lobby.start)
    IOLoop.current().start()
